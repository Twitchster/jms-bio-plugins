#!/usr/bin/env python3
"""Build JMS submittal cut-sheet packets: strip old markups, box the selected
options in the JMS style, add labels where needed, and merge each component's
files into one packet behind a cover sheet that lists the equipment tags.

Requires PyMuPDF (pip install pymupdf --break-system-packages).

JMS markup style (ASB / agaiser examples, Oct 2026): Bluebeam-type Rectangle,
red 1 pt border, orange fill (1, .502, .251) at 30 % opacity, author = the PE's
username, drawn around the selected table row / model line; a second box on a
selected table column where the selection is a cell. Labels (only when the box
alone doesn't say it): red Helvetica 12 pt FreeText, no border.

Commands
  audit  <dir> [--json out.json]        old markups, text layer, security, pages
  find   <pdf> <text> [--page N]        exact token matches + detected row box
  rows   <pdf> --page N                 table rows PyMuPDF detects on a page
  packet <plan.json> <out.pdf>          build a component packet (see below)
  render <pdf> <outdir> [--pages 1,3] [--dpi 80]

packet plan (JSON):
{
  "author": "ABanawan",
  "title": "25026 - Zero Speed Switch",            # PDF title + first bookmark
  "cover": {"file": "<library>/Gearbox/SEW/#Component Cover Sheet.pdf",  # optional
            "tags": ["SSC-1", "SSC-2"], "heading": "Zero Speed Switch"},
  "items": [
    {"file": "<path>.pdf", "bookmark": "Electro-Sensors SCP cut sheet",
     "pages": [1, 2],                                # optional subset (1-based, original numbering)
     "marks": [
       {"page": 2, "text": "800-020100", "mode": "row",
        "note": "Spec 46 21 73 2.6.H: 115 VAC zero-speed switch"},
       {"page": 2, "text": "810-000005", "mode": "row"},
       {"page": 5, "text": "Min. Pulley", "occurrence": 2, "mode": "column",
        "through": "1.5 38 1.5 38", "label": "OR compound"},
       {"page": 3, "rect": [27, 420, 256, 438]}
     ]}
  ]
}
mark modes: row (default; table row, else the text line) | line | block (text block +
adjacent label tile) | text | column (header cell down to the row
of "through", or the whole column) | rect.  "occurrence": pick the Nth match.
"note" goes into the markup's comment (not printed); "label" prints red text.
Every item is copied with ALL existing markups removed first.
"""
import argparse
import json
import os
import re
import sys

import pymupdf

if hasattr(pymupdf, "no_recommend_layout"):
    pymupdf.no_recommend_layout()

RED = (1, 0, 0)
ORANGE = (1, 0.5019608, 0.2509804)
FILL_OPACITY = 0.3
PAD = 2.0
LABEL_SIZE = 12


# ---------- finding things on a page ----------

def norm(t):
    return re.sub(r"[\s ]+", " ", t).strip().lower()


def find_exact(page, text):
    """Exact token-sequence matches (RS-5X does not match RS-5XL)."""
    words = page.get_text("words")
    target = norm(text).split(" ")
    toks = [norm(w[4]) for w in words]
    n, hits = len(target), []
    for i in range(len(words) - n + 1):
        seq = toks[i:i + n]
        last_ok = seq[-1] == target[-1] or seq[-1].rstrip(",;:)*") == target[-1]
        if seq[:-1] == target[:-1] and last_ok:
            r = pymupdf.Rect(words[i][:4])
            for w in words[i + 1:i + n]:
                r |= pymupdf.Rect(w[:4])
            hits.append(r)
    return hits


def line_rect(page, hit):
    cy = (hit.y0 + hit.y1) / 2
    h = hit.y1 - hit.y0
    r = pymupdf.Rect(hit)
    words = sorted(page.get_text("words"), key=lambda w: w[0])
    # grow left/right across words on the same baseline with gaps < 3 x line height
    for direction in (1, -1):
        edge = r.x1 if direction == 1 else r.x0
        cand = [w for w in words if abs((w[1] + w[3]) / 2 - cy) < 0.35 * h]
        cand = cand if direction == 1 else list(reversed(cand))
        for w in cand:
            if direction == 1 and w[0] >= edge - 0.5 and w[0] - edge < 3 * h:
                r |= pymupdf.Rect(w[:4]); edge = r.x1
            elif direction == -1 and w[2] <= edge + 0.5 and edge - w[2] < 3 * h:
                r |= pymupdf.Rect(w[:4]); edge = r.x0
    return r


_TABLE_CACHE = {}


def tables(page):
    key = (id(page.parent), page.number)
    if key not in _TABLE_CACHE:
        try:
            _TABLE_CACHE[key] = page.find_tables().tables
        except Exception:
            _TABLE_CACHE[key] = []
    return _TABLE_CACHE[key]


def table_rows(page):
    out = []
    for ti, t in enumerate(tables(page)):
        for ri, row in enumerate(t.rows):
            cells = [c for c in row.cells if c]
            if cells:
                r = pymupdf.Rect(cells[0])
                for c in cells[1:]:
                    r |= pymupdf.Rect(c)
                out.append((ti, ri, r, t))
    return out


def block_rect(page, hit):
    """Text block containing the hit, plus filled shapes (label tiles) beside it."""
    r = None
    for b in page.get_text("blocks"):
        br = pymupdf.Rect(b[:4])
        if br.intersects(hit):
            r = br; break
    if r is None:
        return line_rect(page, hit)
    for d in page.get_drawings():
        fr = d.get("rect")
        if not d.get("fill") or fr is None or fr.width > page.rect.width * 0.6:
            continue
        ov = min(fr.y1, r.y1) - max(fr.y0, r.y0)
        left_gap = r.x0 - fr.x1      # tile to the left of the text (typical label tile)
        right_gap = fr.x0 - r.x1
        if ov > 0.5 * min(fr.height, r.height) and (fr.intersects(r) or -2 <= left_gap < 25 or -2 <= right_gap < 6):
            r |= fr
    return r


def row_rect(page, hit):
    cy = (hit.y0 + hit.y1) / 2
    best = None
    for ti, ri, r, t in table_rows(page):
        if r.y0 - 1 <= cy <= r.y1 + 1 and r.x0 - 2 <= hit.x0 and hit.x1 <= r.x1 + 2:
            if best is None or r.height < best.height:
                best = r
    return best or line_rect(page, hit)


def column_rect(page, hit, through=None):
    cx = (hit.x0 + hit.x1) / 2
    for t in tables(page):
        tb = pymupdf.Rect(t.bbox)
        if not tb.contains(hit.tl) and not (tb.x0 <= cx <= tb.x1 and tb.y0 - 2 <= hit.y0 <= tb.y1):
            continue
        cells = [pymupdf.Rect(c) for row in t.rows for c in row.cells if c]
        col = [c for c in cells if c.x0 - 1 <= cx <= c.x1 + 1]
        if not col:
            continue
        # narrowest cells at this x define the column width (merged headers are wider)
        wmin = min(c.width for c in col)
        col = [c for c in col if c.width <= wmin * 1.6]
        top = min(min(c.y0 for c in col), hit.y0 - PAD)
        r = pymupdf.Rect(min(c.x0 for c in col), top, max(c.x1 for c in col), max(c.y1 for c in col))
        if through:
            th = find_exact(page, through)
            th = [x for x in th if x.y0 > hit.y0]
            if th:
                r.y1 = row_rect(page, th[0]).y1
        return r
    return pymupdf.Rect(hit)


# ---------- drawing ----------

def strip_markups(doc):
    n = 0
    for page in doc:
        a = page.first_annot
        while a:
            nxt = a.next
            page.delete_annot(a)
            n += 1
            a = nxt
    return n


def add_box(page, rect, author, note=""):
    annot = page.add_rect_annot(pymupdf.Rect(rect))
    annot.set_colors(stroke=RED, fill=ORANGE)
    annot.set_border(width=1)
    annot.set_info(title=author, subject="Rectangle", content=note or "")
    annot.update()
    doc = page.parent
    gs = doc.get_new_xref()
    doc.update_object(gs, f"<< /Type /ExtGState /ca {FILL_OPACITY} /CA 1 >>")
    ap = doc.xref_get_key(annot.xref, "AP/N")
    if ap[0] == "xref":
        apx = int(ap[1].split()[0])
        doc.xref_set_key(apx, "Resources", f"<< /ProcSet [/PDF] /ExtGState << /JMSGS {gs} 0 R >> >>")
        doc.update_stream(apx, b"/JMSGS gs\n" + doc.xref_stream(apx))
    doc.xref_set_key(annot.xref, "FillOpacity", str(FILL_OPACITY))  # Bluebeam reads this
    return annot


def place_label(page, box, text):
    lines = text.split("\n")
    w = max(len(l) for l in lines) * LABEL_SIZE * 0.55 + 8
    h = len(lines) * LABEL_SIZE * 1.2 + 6
    pr = page.rect
    options = [
        pymupdf.Rect(box.x1 + 4, box.y0, box.x1 + 4 + w, box.y0 + h),      # right
        pymupdf.Rect(box.x0 - 4 - w, box.y0, box.x0 - 4, box.y0 + h),      # left
        pymupdf.Rect(box.x0, box.y0 - h - 2, box.x0 + w, box.y0 - 2),      # above
        pymupdf.Rect(box.x0, box.y1 + 2, box.x0 + w, box.y1 + 2 + h),      # below
    ]
    words = [pymupdf.Rect(x[:4]) for x in page.get_text("words")]
    best, best_overlap = None, None
    for r in options:
        if not pr.contains(r):
            continue
        overlap = sum(1 for wr in words if wr.intersects(r))
        if best is None or overlap < best_overlap:
            best, best_overlap = r, overlap
    r = best or options[0] & pr
    a = page.add_freetext_annot(r, text, fontsize=LABEL_SIZE, fontname="helv", text_color=RED,
                                align=pymupdf.TEXT_ALIGN_LEFT)
    a.update()
    return a, best_overlap


def resolve(page, m):
    if "rect" in m:
        return [pymupdf.Rect(m["rect"])]
    hits = find_exact(page, m["text"])
    if not hits:
        return []
    if "occurrence" in m:
        k = m["occurrence"] - 1
        hits = [hits[k]] if k < len(hits) else []
    mode = m.get("mode", "row")
    fn = {"row": lambda h: row_rect(page, h), "line": lambda h: line_rect(page, h),
          "text": lambda h: pymupdf.Rect(h), "block": lambda h: block_rect(page, h),
          "column": lambda h: column_rect(page, h, m.get("through"))}[mode]
    return [fn(h) for h in hits]


def mark_doc(doc, marks, author, page_map, report, label_author):
    failed = 0
    for m in marks:
        if m["page"] not in page_map:
            report.append(f"  SKIPPED    p{m['page']} not in included pages"); continue
        page = doc[page_map[m["page"]]]
        rects = resolve(page, m)
        what = m.get("text", "rect")
        if not rects:
            failed += 1
            report.append(f"  NOT FOUND  p{m['page']}  {what!r}"); continue
        if len(rects) > 1:
            report.append(f"  AMBIGUOUS  p{m['page']}  {what!r}: {len(rects)} matches, all marked; set 'occurrence'")
        for r in rects:
            r = pymupdf.Rect(r.x0 - PAD, r.y0 - PAD, r.x1 + PAD, r.y1 + PAD) & page.rect
            add_box(page, r, author, m.get("note", ""))
            msg = f"  MARKED     p{m['page']}  {what!r} [{m.get('mode', 'row') if 'rect' not in m else 'rect'}] at {tuple(round(v) for v in r)}"
            if m.get("label"):
                a, ov = place_label(page, r, m["label"])
                a.set_info(title=label_author, subject="Text Box"); a.update()
                msg += f"  label {m['label']!r}" + (f" (overlaps {ov} words - check)" if ov else "")
            report.append(msg)
    return failed


# ---------- packet ----------

def cover_page(plan, author):
    c = plan.get("cover") or {}
    tags = c.get("tags") or []
    if c.get("file"):
        doc = pymupdf.open(c["file"])
        strip_markups(doc)
        doc.select([0])
    else:
        doc = pymupdf.open()
        doc.new_page(width=612, height=792)
    page = doc[0]
    lines = ([c["heading"]] if c.get("heading") else []) + tags
    if lines:
        w = page.rect.width
        r = pymupdf.Rect(w * 0.15, 110, w * 0.85, 110 + 32.2 * len(lines) + 12)
        a = page.add_freetext_annot(r, "\n".join(lines), fontsize=28, fontname="helv",
                                    text_color=(0, 0, 0), align=pymupdf.TEXT_ALIGN_CENTER)
        a.set_info(title=author, subject="Text Box")
        a.update()
    return doc


def cmd_packet(plan_path, out):
    plan = json.load(open(plan_path))
    author = plan.get("author") or "JMS"
    report = [f"PACKET {plan.get('title', '')}  ->  {out}"]
    final = pymupdf.open()
    toc = []
    failed = 0
    if plan.get("cover") is not None:
        cdoc = cover_page(plan, author)
        final.insert_pdf(cdoc, annots=True)
        toc.append([1, plan.get("title") or "Cover", 1])
        report.append(f"  COVER      tags {plan['cover'].get('tags')}")
    for item in plan["items"]:
        src = pymupdf.open(item["file"])
        removed = strip_markups(src)
        pages = item.get("pages") or list(range(1, src.page_count + 1))
        page_map = {p: i for i, p in enumerate(pages)}
        if item.get("pages"):
            src.select([p - 1 for p in pages])
        report.append(f"ITEM {os.path.basename(item['file'])}  ({len(pages)} p, {removed} old markups removed)")
        failed += mark_doc(src, item.get("marks", []), author, page_map, report, author)
        start = final.page_count + 1
        final.insert_pdf(src, annots=True)
        toc.append([1, item.get("bookmark") or os.path.splitext(os.path.basename(item["file"]))[0], start])
    final.set_toc(toc)
    final.set_metadata({"title": plan.get("title", ""), "author": author, "creator": "JMS bio-handling plugin"})
    final.save(out, garbage=3, deflate=True)
    report.append(f"WROTE {out}  ({final.page_count} pages, {os.path.getsize(out) / 1e6:.1f} MB)")
    print("\n".join(report))
    return 1 if failed else 0


# ---------- audit ----------

def cmd_audit(root, json_out=None):
    rows = []
    for dp, _, fs in os.walk(root):
        for f in sorted(fs):
            if not f.lower().endswith(".pdf"):
                continue
            p = os.path.join(dp, f)
            try:
                d = pymupdf.open(p)
            except Exception as e:
                rows.append({"path": p, "error": str(e)}); continue
            authors, count, pages_with, textless = set(), 0, [], 0
            for pg in d:
                al = list(pg.annots())
                if al:
                    pages_with.append(pg.number + 1)
                for a in al:
                    count += 1; authors.add(a.info.get("title", ""))
                if not pg.get_text().strip():
                    textless += 1
            rows.append({"path": os.path.relpath(p, root), "pages": d.page_count, "old_markups": count,
                         "authors": sorted(authors), "markup_pages": pages_with, "pages_without_text": textless,
                         "secured": bool(d.is_encrypted or (d.permissions & pymupdf.PDF_PERM_ANNOTATE) == 0),
                         "mb": round(os.path.getsize(p) / 1e6, 1)})
    if json_out:
        json.dump(rows, open(json_out, "w"), indent=1)
    marked = [r for r in rows if r.get("old_markups")]
    print(f"{len(rows)} PDFs; {len(marked)} with old markups; "
          f"{sum(1 for r in rows if r.get('pages_without_text'))} with pages lacking text; "
          f"{sum(1 for r in rows if r.get('secured'))} secured")
    for r in rows:
        flags = []
        if r.get("old_markups"):
            flags.append(f"{r['old_markups']} old markups by {', '.join(r['authors'])}")
        if r.get("pages_without_text"):
            flags.append(f"{r['pages_without_text']}/{r['pages']} pages without text")
        if r.get("secured"):
            flags.append("secured (annotating blocked)")
        if flags:
            print(f"  {r['path']}: " + "; ".join(flags))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("audit"); a.add_argument("dir"); a.add_argument("--json")
    f = sub.add_parser("find"); f.add_argument("pdf"); f.add_argument("text"); f.add_argument("--page", type=int)
    r = sub.add_parser("rows"); r.add_argument("pdf"); r.add_argument("--page", type=int, required=True)
    k = sub.add_parser("packet"); k.add_argument("plan"); k.add_argument("out")
    v = sub.add_parser("render"); v.add_argument("pdf"); v.add_argument("outdir")
    v.add_argument("--pages"); v.add_argument("--dpi", type=int, default=80)
    x = ap.parse_args()
    if x.cmd == "audit":
        cmd_audit(x.dir, x.json)
    elif x.cmd == "find":
        doc = pymupdf.open(x.pdf); strip_markups(doc)
        for i in ([x.page - 1] if x.page else range(doc.page_count)):
            for h in find_exact(doc[i], x.text):
                print(f"p{i + 1} hit={tuple(round(v, 1) for v in h)}  row={tuple(round(v) for v in row_rect(doc[i], h))}")
    elif x.cmd == "rows":
        doc = pymupdf.open(x.pdf); strip_markups(doc)
        for ti, ri, rr, _ in table_rows(doc[x.page - 1]):
            print(f"table {ti} row {ri} {tuple(round(v) for v in rr)}")
    elif x.cmd == "packet":
        sys.exit(cmd_packet(x.plan, x.out))
    else:
        doc = pymupdf.open(x.pdf)
        os.makedirs(x.outdir, exist_ok=True)
        for n in ([int(p) for p in x.pages.split(",")] if x.pages else range(1, doc.page_count + 1)):
            out = os.path.join(x.outdir, f"page{n:03d}.png")
            doc[n - 1].get_pixmap(dpi=x.dpi).save(out)
            print(out)


if __name__ == "__main__":
    import warnings
    warnings.filterwarnings("ignore")
    main()
