#!/usr/bin/env python3
"""Inspect a JMS O&M starting-point template, or check a filled O&M for leftovers.

Standard library only.

  inspect <file.docx> [--json out.json]
      Lists every drafter comment with its section and anchor text, the
      highlighted fill-in text, bracketed options, placeholders, content
      controls and header/footer fields. Run it on a template before filling,
      and on any newer template revision the user supplies.

  prepare <template.docx> <out.docx>
      Makes the working copy for drafting: removes every template comment
      (drafter notes and their screenshot comments) from document.xml and all
      comment parts, and sets Word to offer a field update on open. Every
      other part is copied byte-for-byte. Run inspect first and keep its output:
      the notes are the drafting instructions.

  check <file.docx>
      Quality check on a filled O&M. Reports leftover "Note to O&M" comments,
      yellow highlights, placeholders (XXX, INSERT, MONTH YEAR, ...), unresolved
      [option][option] brackets, broken cross-references ("Error! Reference
      source not found") and header/footer placeholders. Exit code 1 when
      anything is left, 0 when clean.
"""
import argparse
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

PLACEHOLDER_PATTERNS = [
    (r"\bX{2,}\b|\bx{3,}\b", "X placeholder"),
    (r"\bINSERT\b", "INSERT instruction"),
    (r"MONTH YEAR", "cover date"),
    (r"\bPLANT NAME\b", "plant name"),
    (r"\bLOCATION \(CITY", "location"),
    (r"Tag Number/Serial Number/Customer Provided", "tag number"),
    (r"XX XX XX", "spec section"),
    (r"Error! Reference source not found|Error! Bookmark not defined", "broken cross-reference"),
    (r"Note to (the )?O&M", "drafter note in body text"),
    (r"DELETE THIS PAGE", "inputs page still present (delete in PDF)"),
]


def text_of(el):
    out = []
    for node in el.iter():
        if node.tag == W + "t" and node.text:
            out.append(node.text)
        elif node.tag == W + "tab":
            out.append("\t")
    return "".join(out)


def load(path):
    z = zipfile.ZipFile(path)
    names = z.namelist()
    doc = ET.fromstring(z.read("word/document.xml"))
    styles = {}
    if "word/styles.xml" in names:
        for s in ET.fromstring(z.read("word/styles.xml")).iter(W + "style"):
            sid = s.get(W + "styleId")
            n = s.find(W + "name")
            styles[sid] = n.get(W + "val") if n is not None else sid
    comments = {}
    if "word/comments.xml" in names:
        for c in ET.fromstring(z.read("word/comments.xml")).iter(W + "comment"):
            comments[c.get(W + "id")] = {
                "author": c.get(W + "author", ""),
                "text": " ".join(text_of(p) for p in c.iter(W + "p")).strip(),
            }
    hf = {}
    for n in names:
        if re.match(r"word/(header|footer)\d+\.xml$", n):
            t = text_of(ET.fromstring(z.read(n))).strip()
            if t:
                hf[n.split("/")[-1]] = t
    return doc, styles, comments, hf


def heading_level(p, styles):
    ppr = p.find(W + "pPr")
    if ppr is None:
        return None
    ps = ppr.find(W + "pStyle")
    if ps is None:
        return None
    name = styles.get(ps.get(W + "val"), ps.get(W + "val")) or ""
    m = re.match(r"heading\s*(\d)", name, re.I)
    return int(m.group(1)) if m else None


def walk(doc, styles):
    """Yield per-paragraph info in document order, tracking section path and comment anchors."""
    body = doc.find(W + "body")
    path = []
    open_c = {}
    anchors = {}
    paras = []
    for p in body.iter(W + "p"):
        lvl = heading_level(p, styles)
        ptxt = text_of(p).strip()
        if lvl and ptxt:
            path = path[: lvl - 1] + [ptxt]
        hl = []
        for node in p.iter():
            if node.tag == W + "commentRangeStart":
                open_c[node.get(W + "id")] = []
                anchors.setdefault(node.get(W + "id"), {"section": " > ".join(path), "anchor": ""})
            elif node.tag == W + "commentRangeEnd":
                cid = node.get(W + "id")
                if cid in open_c:
                    anchors[cid]["anchor"] = "".join(open_c.pop(cid))[:160]
            elif node.tag == W + "commentReference":
                anchors.setdefault(node.get(W + "id"), {"section": " > ".join(path), "anchor": ""})
            elif node.tag == W + "r":
                t = "".join(x.text or "" for x in node.iter(W + "t"))
                for buf in open_c.values():
                    buf.append(t)
                rpr = node.find(W + "rPr")
                if rpr is not None and t.strip():
                    h = rpr.find(W + "highlight")
                    if h is not None and h.get(W + "val") not in (None, "none"):
                        hl.append(t)
        paras.append({"section": " > ".join(path), "text": ptxt, "highlight": "".join(hl).strip()})
    return paras, anchors


def find_placeholders(text):
    hits = []
    for pat, label in PLACEHOLDER_PATTERNS:
        for m in re.finditer(pat, text):
            hits.append((label, m.group(0)))
    return hits


def options_in(text):
    # bracketed options such as [slide][knife] or [Grout beneath ...]
    return re.findall(r"\[[^\[\]]{1,200}\]", text)


def cmd_inspect(path, json_out=None):
    doc, styles, comments, hf = load(path)
    paras, anchors = walk(doc, styles)
    sdts = []
    for sdt in doc.iter(W + "sdt"):
        pr = sdt.find(W + "sdtPr")
        alias = pr.find(W + "alias") if pr is not None else None
        tag = pr.find(W + "tag") if pr is not None else None
        content = sdt.find(W + "sdtContent")
        t = text_of(content).strip()[:60] if content is not None else ""
        if t.startswith("Table of Contents"):
            continue
        sdts.append({"alias": alias.get(W + "val") if alias is not None else "",
                     "tag": tag.get(W + "val") if tag is not None else "", "text": t})
    report = {"file": path, "comments": [], "highlights": [], "options": [], "content_controls": sdts,
              "header_footer": hf}
    for cid, c in comments.items():
        a = anchors.get(cid, {"section": "?", "anchor": ""})
        report["comments"].append({"id": cid, "section": a["section"], "anchor": a["anchor"], **c})
    for p in paras:
        if p["highlight"]:
            report["highlights"].append({"section": p["section"], "text": p["highlight"][:200]})
        for o in options_in(p["text"]):
            report["options"].append({"section": p["section"], "option": o[:200]})

    print(f"FILE: {path}")
    print(f"\n== DRAFTER COMMENTS ({len(report['comments'])})")
    for c in report["comments"]:
        if not c["text"]:
            continue  # image-only comments
        print(f"[{c['section']}] anchor: {c['anchor'][:70]!r}\n    {c['text']}")
    print(f"\n== HIGHLIGHTED FILL-INS ({len(report['highlights'])} paragraphs)")
    for h in report["highlights"]:
        print(f"[{h['section']}] {h['text']}")
    print(f"\n== BRACKETED OPTIONS ({len(report['options'])})")
    for o in report["options"]:
        print(f"[{o['section']}] {o['option']}")
    if sdts:
        print(f"\n== CONTENT CONTROLS ({len(sdts)})")
        for s in sdts:
            print(f"  {s['alias'] or s['tag'] or '-'}: {s['text']}")
    print("\n== HEADER / FOOTER")
    for k, v in hf.items():
        print(f"  {k}: {v}")
    if json_out:
        with open(json_out, "w") as f:
            json.dump(report, f, indent=1)
        print(f"\nJSON written to {json_out}")
    return 0


def cmd_check(path):
    doc, styles, comments, hf = load(path)
    paras, anchors = walk(doc, styles)
    issues = []
    drafter = [c for c in comments.values() if re.search(r"note to (the )?(o&m|whoever)", c["text"], re.I)]
    if drafter:
        issues.append(f"{len(drafter)} template drafter comment(s) still in the file")
    hl = [p for p in paras if p["highlight"]]
    if hl:
        issues.append(f"{len(hl)} paragraph(s) still highlighted")
        for p in hl[:40]:
            print(f"  HIGHLIGHT [{p['section']}] {p['highlight'][:120]}")
    for p in paras:
        for label, hit in find_placeholders(p["text"]):
            issues.append(f"{label}: {hit!r} in [{p['section']}] {p['text'][:90]!r}")
        if re.search(r"\]\s*\[", p["text"]):
            issues.append(f"unresolved option brackets in [{p['section']}] {p['text'][:90]!r}")
    for k, v in hf.items():
        for label, hit in find_placeholders(v):
            issues.append(f"{label}: {hit!r} in {k}")
    cc = sum(1 for p in paras if re.search(r"cross-contamination", p["text"], re.I))
    print(f"INFO: 'cross-contamination' appears in {cc} paragraph(s); keep only for mostly-stainless equipment.")
    open_items = [c for c in comments.values() if c["text"].upper().startswith(("OPEN", "ASSUMPTION", "PLACEHOLDER"))]
    print(f"INFO: {len(open_items)} OPEN/ASSUMPTION/PLACEHOLDER comment(s) for the PE.")
    if issues:
        print(f"CHECK FAILED: {len(issues)} item(s)")
        for i in issues:
            print("  - " + i)
        return 1
    print("CHECK OK: no template leftovers found (fields still need Ctrl+A, F9 in Word, including header/footer).")
    return 0


COMMENT_PARTS = ("word/comments.xml", "word/commentsExtended.xml", "word/commentsIds.xml",
                 "word/commentsExtensible.xml")


def _strip_comment_markup(xml):
    xml = re.sub(r"<w:commentRangeStart\b[^>]*/>", "", xml)
    xml = re.sub(r"<w:commentRangeEnd\b[^>]*/>", "", xml)
    # runs that only carry a comment reference
    xml = re.sub(r"<w:r\b[^>]*>(?:(?!</w:r>).)*?<w:commentReference\b[^>]*/>(?:(?!</w:r>).)*?</w:r>", "",
                 xml, flags=re.S)
    xml = re.sub(r"<w:commentReference\b[^>]*/>", "", xml)
    return xml


def cmd_prepare(src, dst):
    if src == dst:
        print("ERROR: output must differ from the template")
        return 2
    zin = zipfile.ZipFile(src)
    removed = 0
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            name = item.filename
            if name.startswith("[trash]/"):
                continue  # unreferenced leftovers some templates carry
            if name in COMMENT_PARTS:
                xml = data.decode("utf-8")
                if name == "word/comments.xml":
                    removed = len(re.findall(r"<w:comment\b", xml))
                    xml = re.sub(r"<w:comment\b.*?</w:comment>", "", xml, flags=re.S)
                elif name == "word/commentsExtended.xml":
                    xml = re.sub(r"<w15:commentEx\b[^>]*/>", "", xml)
                elif name == "word/commentsIds.xml":
                    xml = re.sub(r"<w16cid:commentId\b[^>]*/>", "", xml)
                else:
                    xml = re.sub(r"<w16cex:commentExtensible\b.*?(?:/>|</w16cex:commentExtensible>)", "", xml,
                                 flags=re.S)
                data = xml.encode("utf-8")
            elif re.match(r"word/(document|header\d+|footer\d+|footnotes|endnotes)\.xml$", name):
                xml = data.decode("utf-8")
                if "comment" in xml:
                    data = _strip_comment_markup(xml).encode("utf-8")
            elif name == "word/settings.xml":
                xml = data.decode("utf-8")
                if "<w:updateFields" not in xml:
                    # schema order: updateFields sits just before these elements
                    after = ["w:hdrShapeDefaults", "w:footnotePr", "w:endnotePr", "w:compat", "w:docVars",
                             "w:rsids", "m:mathPr", "w:attachedSchema", "w:themeFontLang", "w:clrSchemeMapping",
                             "w:doNotIncludeSubdocsInStats", "w:doNotAutoCompressPictures", "w:forceUpgrade",
                             "w:captions", "w:readModeInkLockDown", "w:smartTagType", "sl:schemaLibrary",
                             "w:shapeDefaults", "w:doNotEmbedSmartTags", "w:decimalSymbol", "w:listSeparator"]
                    pos = [xml.find("<" + t) for t in after if xml.find("<" + t) != -1]
                    cut = min(pos) if pos else xml.rfind("</w:settings>")
                    xml = xml[:cut] + '<w:updateFields w:val="true"/>' + xml[cut:]
                data = xml.encode("utf-8")
            zout.writestr(item, data)
    # verify
    doc = zipfile.ZipFile(dst).read("word/document.xml").decode("utf-8")
    left = len(re.findall(r"commentRangeStart|commentReference", doc))
    ET.fromstring(doc.encode("utf-8"))
    print(f"Removed {removed} comment(s); {left} comment markers left in document.xml; updateFields set.")
    print(f"Wrote {dst}")
    return 0 if left == 0 else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("inspect")
    a.add_argument("docx")
    a.add_argument("--json")
    p = sub.add_parser("prepare")
    p.add_argument("template")
    p.add_argument("out")
    b = sub.add_parser("check")
    b.add_argument("docx")
    args = ap.parse_args()
    if args.cmd == "inspect":
        sys.exit(cmd_inspect(args.docx, args.json))
    if args.cmd == "prepare":
        sys.exit(cmd_prepare(args.template, args.out))
    sys.exit(cmd_check(args.docx))


if __name__ == "__main__":
    main()
