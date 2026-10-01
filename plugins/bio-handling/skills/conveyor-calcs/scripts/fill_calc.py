#!/usr/bin/env python3
"""Write input values and cell comments into a JMS calculation workbook WITHOUT
touching anything else (macros, images, drawings, formatting, other sheets).

Usage:
  python3 fill_calc.py --template <blank.xlsm|.xlsx> --out <filled file>
                       --values values.json [--comments comments.json]
                       [--sheet Design] [--author "Claude (for ASB)"]
  python3 fill_calc.py --verify --template <blank> --out <filled> --values values.json

values.json   {"M23": 30, "P10": "Screenings Belt Conveyor", "AK5": "date:2026-10-01",
               "M20": "=AP10*0+6*2000/AP10", "U6": null}
              numbers -> numeric cell; strings -> text; "=..." -> formula;
              "date:YYYY-MM-DD" -> Excel date serial; true/false -> boolean; null -> clear.
--allow-formula M20   cells whose template formula may be replaced (refused otherwise)
comments.json {"M23": "Spec 2.6.C.4.a: 24 in min; 30 in per ASB (10/1/26)."}
              Legacy Excel comments (Excel 'Notes'). An existing comment on the same
              cell is replaced; other existing comments are kept.

Why XML-level: openpyxl drops embedded images and some drawing parts when it saves,
and the JMS templates contain images (and VBA in the .xlsm). This script edits only:
  - the target sheet XML (the listed cells, plus a <legacyDrawing> link if needed)
  - that sheet's comments part and VML drawing (created if absent)
  - that sheet's .rels, [Content_Types].xml (only if a new part is added)
  - workbook.xml calcPr: fullCalcOnLoad="1" so Excel recalculates on open
Every other zip entry is copied byte-for-byte. Run --verify afterwards: it proves
that only the intended cells changed and that vbaProject.bin and media are identical.
"""
import argparse
import datetime as dt
import json
import re
import sys
import zipfile
from copy import deepcopy

from lxml import etree

NS = {
    "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "pr": "http://schemas.openxmlformats.org/package/2006/relationships",
    "ct": "http://schemas.openxmlformats.org/package/2006/content-types",
}
M = "{%s}" % NS["m"]
R_NS = NS["r"]
REL_COMMENTS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments"
REL_VML = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/vmlDrawing"
CT_COMMENTS = "application/vnd.openxmlformats-officedocument.spreadsheetml.comments+xml"
CT_VML = "application/vnd.openxmlformats-officedocument.vmlDrawing"

# order of child elements of <worksheet> (ECMA-376) - used to place <legacyDrawing>
WS_ORDER = ["sheetPr", "dimension", "sheetViews", "sheetFormatPr", "cols", "sheetData", "sheetCalcPr",
            "sheetProtection", "protectedRanges", "scenarios", "autoFilter", "sortState", "dataConsolidate",
            "customSheetViews", "mergeCells", "phoneticPr", "conditionalFormatting", "dataValidations",
            "hyperlinks", "printOptions", "pageMargins", "pageSetup", "headerFooter", "rowBreaks", "colBreaks",
            "customProperties", "cellWatches", "ignoredErrors", "smartTags", "drawing", "legacyDrawing",
            "legacyDrawingHF", "drawingHF", "picture", "oleObjects", "controls", "webPublishItems",
            "tableParts", "extLst"]


def col_to_num(col):
    n = 0
    for ch in col:
        n = n * 26 + (ord(ch) - 64)
    return n


def split_ref(ref):
    m = re.fullmatch(r"([A-Z]{1,3})(\d+)", ref)
    if not m:
        raise ValueError(f"bad cell reference {ref}")
    return m.group(1), int(m.group(2))


def excel_serial(d):
    return (d - dt.date(1899, 12, 30)).days


def resolve_sheet(z, sheet_name):
    wb = etree.fromstring(z.read("xl/workbook.xml"))
    rels = etree.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    for s in wb.iter(M + "sheet"):
        if s.get("name") == sheet_name:
            rid = s.get("{%s}id" % R_NS)
            for rel in rels:
                if rel.get("Id") == rid:
                    tgt = rel.get("Target")
                    path = tgt.lstrip("/") if tgt.startswith("/") else "xl/" + tgt
                    return path
    raise SystemExit(f"Sheet '{sheet_name}' not found")


def rels_path_for(part):
    d, f = part.rsplit("/", 1)
    return f"{d}/_rels/{f}.rels"


def norm_target(base_part, target):
    if target.startswith("/"):
        return target.lstrip("/")
    parts = base_part.rsplit("/", 1)[0].split("/")
    for seg in target.split("/"):
        if seg == "..":
            parts.pop()
        elif seg and seg != ".":
            parts.append(seg)
    return "/".join(parts)


class FormulaCellError(Exception):
    pass


def set_cell(sheet_root, ref, value, allow_formula_overwrite=()):
    col, rownum = split_ref(ref)
    if isinstance(value, str) and ("<openpyxl" in value or " object at 0x" in value):
        raise ValueError(f"{ref}: value looks like a Python object repr, not data: {value[:60]}")
    sd = sheet_root.find(M + "sheetData")
    row = None
    for r in sd.findall(M + "row"):
        rn = int(r.get("r"))
        if rn == rownum:
            row = r
            break
        if rn > rownum:
            row = etree.Element(M + "row", r=str(rownum))
            r.addprevious(row)
            break
    if row is None:
        row = etree.SubElement(sd, M + "row", r=str(rownum))
    cell = None
    for c in row.findall(M + "c"):
        cc, _ = split_ref(c.get("r"))
        if cc == col:
            cell = c
            break
        if col_to_num(cc) > col_to_num(col):
            cell = etree.Element(M + "c", r=ref)
            c.addprevious(cell)
            break
    if cell is None:
        cell = etree.SubElement(row, M + "c", r=ref)
    if cell.find(M + "f") is not None and ref not in allow_formula_overwrite:
        raise FormulaCellError(
            f"{ref} holds a template formula. Inputs never overwrite formulas; if this is truly intended, "
            f"pass it in --allow-formula (e.g. a capacity cell deliberately tied to density).")
    # clear content and dynamic-array metadata, keep style
    for attr in ("cm", "vm"):
        if attr in cell.attrib:
            del cell.attrib[attr]
    for child in list(cell):
        cell.remove(child)
    if "t" in cell.attrib:
        del cell.attrib["t"]
    if value is None:
        return
    if isinstance(value, bool):
        cell.set("t", "b")
        etree.SubElement(cell, M + "v").text = "1" if value else "0"
    elif isinstance(value, (int, float)):
        etree.SubElement(cell, M + "v").text = repr(value) if isinstance(value, float) else str(value)
    elif isinstance(value, str) and value.startswith("="):
        etree.SubElement(cell, M + "f").text = value[1:]
    elif isinstance(value, str) and value.startswith("date:"):
        d = dt.date.fromisoformat(value[5:])
        etree.SubElement(cell, M + "v").text = str(excel_serial(d))
    else:
        cell.set("t", "inlineStr")
        is_ = etree.SubElement(cell, M + "is")
        t = etree.SubElement(is_, M + "t")
        t.text = str(value)
        if t.text != t.text.strip():
            t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")


VML_HEAD = ('<xml xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" '
            'xmlns:x="urn:schemas-microsoft-com:office:excel">'
            '<o:shapelayout v:ext="edit"><o:idmap v:ext="edit" data="%d"/></o:shapelayout>'
            '<v:shapetype id="_x0000_t202" coordsize="21600,21600" o:spt="202" path="m,l,21600r21600,l21600,xe">'
            '<v:stroke joinstyle="miter"/><v:path gradientshapeok="t" o:connecttype="rect"/></v:shapetype>')


def vml_shape(shape_id, ref):
    col, row = split_ref(ref)
    c0, r0 = col_to_num(col) - 1, row - 1
    anchor = f"{c0 + 1}, 15, {max(r0 - 1, 0)}, 10, {c0 + 4}, 15, {r0 + 4}, 4"
    return (f'<v:shape id="_x0000_s{shape_id}" type="#_x0000_t202" '
            f'style="position:absolute;margin-left:0;margin-top:0;width:216pt;height:96pt;z-index:{shape_id};visibility:hidden" '
            f'fillcolor="#ffffe1" o:insetmode="auto"><v:fill color2="#ffffe1"/>'
            f'<v:shadow on="t" color="black" obscured="t"/><v:path o:connecttype="none"/>'
            f'<v:textbox style="mso-direction-alt:auto"><div style="text-align:left"></div></v:textbox>'
            f'<x:ClientData ObjectType="Note"><x:MoveWithCells/><x:SizeWithCells/>'
            f'<x:Anchor>{anchor}</x:Anchor><x:AutoFill>False</x:AutoFill>'
            f'<x:Row>{r0}</x:Row><x:Column>{c0}</x:Column></x:ClientData></v:shape>')


def next_free(names, pattern):
    n = 1
    while pattern % n in names:
        n += 1
    return n


def fill(template, out, values, comments, sheet="Design", author="Claude (for ASB)", allow_formula=()):
    zin = zipfile.ZipFile(template)
    names = zin.namelist()
    data = {n: zin.read(n) for n in names}
    infos = {n: zin.getinfo(n) for n in names}
    sheet_part = resolve_sheet(zin, sheet)
    sroot = etree.fromstring(data[sheet_part])

    errors = []
    for ref, v in values.items():
        try:
            set_cell(sroot, ref, v, allow_formula)
        except (FormulaCellError, ValueError) as e:
            errors.append(str(e))
    if errors:
        raise SystemExit("Refusing to write; fix these first:\n  " + "\n  ".join(errors))

    if comments:
        rpath = rels_path_for(sheet_part)
        rroot = etree.fromstring(data[rpath]) if rpath in data else etree.Element("{%s}Relationships" % NS["pr"], nsmap={None: NS["pr"]})
        cpart = vpart = None
        for rel in rroot:
            if rel.get("Type") == REL_COMMENTS:
                cpart = norm_target(sheet_part, rel.get("Target"))
            if rel.get("Type") == REL_VML:
                vpart = norm_target(sheet_part, rel.get("Target"))
        existing_ids = {rel.get("Id") for rel in rroot}

        def new_rid():
            i = 1
            while f"rId{i}" in existing_ids:
                i += 1
            existing_ids.add(f"rId{i}")
            return f"rId{i}"

        ct = etree.fromstring(data["[Content_Types].xml"])
        if cpart is None:
            n = next_free(set(names) | set(data), "xl/comments%d.xml")
            cpart = f"xl/comments{n}.xml"
            data[cpart] = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                           f'<comments xmlns="{NS["m"]}"><authors></authors><commentList></commentList></comments>').encode()
            etree.SubElement(rroot, "{%s}Relationship" % NS["pr"], Id=new_rid(), Type=REL_COMMENTS,
                             Target="../" + cpart.split("xl/", 1)[1])
            etree.SubElement(ct, "{%s}Override" % NS["ct"], PartName="/" + cpart, ContentType=CT_COMMENTS)
        if vpart is None:
            n = next_free(set(names) | set(data), "xl/drawings/vmlDrawing%d.vml")
            vpart = f"xl/drawings/vmlDrawing{n}.vml"
            data[vpart] = (VML_HEAD % (n + 100) + "</xml>").encode()
            rid = new_rid()
            etree.SubElement(rroot, "{%s}Relationship" % NS["pr"], Id=rid, Type=REL_VML,
                             Target="../" + vpart.split("xl/", 1)[1])
            if not any(d.get("Extension", "").lower() == "vml" for d in ct.findall("{%s}Default" % NS["ct"])):
                etree.SubElement(ct, "{%s}Default" % NS["ct"], Extension="vml", ContentType=CT_VML)
            ld = etree.Element(M + "legacyDrawing")
            ld.set("{%s}id" % R_NS, rid)
            # insert in schema order
            idx = WS_ORDER.index("legacyDrawing")
            after = None
            for child in sroot:
                tag = etree.QName(child).localname
                if tag in WS_ORDER and WS_ORDER.index(tag) < idx:
                    after = child
            if after is not None:
                after.addnext(ld)
            else:
                sroot.append(ld)
        data[rpath] = etree.tostring(rroot, xml_declaration=True, encoding="UTF-8", standalone=True)
        data["[Content_Types].xml"] = etree.tostring(ct, xml_declaration=True, encoding="UTF-8", standalone=True)

        # comments part
        croot = etree.fromstring(data[cpart])
        authors = croot.find(M + "authors")
        alist = [a.text for a in authors]
        if author not in alist:
            etree.SubElement(authors, M + "author").text = author
            alist.append(author)
        aid = alist.index(author)
        clist = croot.find(M + "commentList")
        replaced = set()
        for c in list(clist):
            if c.get("ref") in comments:
                clist.remove(c)
                replaced.add(c.get("ref"))
        for ref, text in comments.items():
            c = etree.SubElement(clist, M + "comment", ref=ref, authorId=str(aid))
            t = etree.SubElement(etree.SubElement(c, M + "text"), M + "r")
            rpr = etree.SubElement(t, M + "rPr")
            etree.SubElement(rpr, M + "sz", val="9")
            etree.SubElement(rpr, M + "rFont", val="Tahoma")
            tt = etree.SubElement(t, M + "t")
            tt.text = text
            tt.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        data[cpart] = etree.tostring(croot, xml_declaration=True, encoding="UTF-8", standalone=True)

        # VML: remove shapes for replaced refs, add one per comment
        vtxt = data[vpart].decode("utf-8", errors="replace")
        for ref in comments:
            col, row = split_ref(ref)
            r0, c0 = row - 1, col_to_num(col) - 1
            vtxt = re.sub(r'<v:shape\b(?:(?!</v:shape>).)*?<x:Row>%d</x:Row>\s*<x:Column>%d</x:Column>.*?</v:shape>' % (r0, c0),
                          "", vtxt, flags=re.S)
        ids = [int(x) for x in re.findall(r'_x0000_s(\d+)', vtxt)]
        m = re.search(r'<o:idmap[^>]*data="(\d+)', vtxt)
        base = (int(m.group(1)) * 1024) if m else 1024
        nid = max(ids + [base]) + 1
        shapes = "".join(vml_shape(nid + i, ref) for i, ref in enumerate(comments))
        vtxt = vtxt.replace("</xml>", shapes + "</xml>")
        data[vpart] = vtxt.encode("utf-8")

    data[sheet_part] = etree.tostring(sroot, xml_declaration=True, encoding="UTF-8", standalone=True)

    # force full recalculation on open
    wbx = data["xl/workbook.xml"].decode("utf-8")
    if "<calcPr" in wbx:
        if "fullCalcOnLoad" not in wbx:
            wbx = re.sub(r"<calcPr\b", '<calcPr fullCalcOnLoad="1"', wbx, count=1)
    data["xl/workbook.xml"] = wbx.encode("utf-8")

    with zipfile.ZipFile(out, "w") as zout:
        for n in names:
            info = infos[n]
            zi = zipfile.ZipInfo(n, date_time=info.date_time)
            zi.compress_type = info.compress_type
            zi.external_attr = info.external_attr
            zout.writestr(zi, data[n])
        for n in data:
            if n not in infos:
                zout.writestr(zipfile.ZipInfo(n), data[n], compress_type=zipfile.ZIP_DEFLATED)


def cells_of(xml_bytes):
    root = etree.fromstring(xml_bytes)
    out = {}
    for c in root.iter(M + "c"):
        out[c.get("r")] = etree.tostring(c)
    return out


def verify(template, out, values, sheet="Design"):
    a, b = zipfile.ZipFile(template), zipfile.ZipFile(out)
    ok = True
    if b.testzip() is not None:
        print("FAIL: output zip is corrupt"); return False
    sheet_part = resolve_sheet(a, sheet)
    allowed = {sheet_part, "xl/workbook.xml", "[Content_Types].xml", rels_path_for(sheet_part)}
    for n in a.namelist():
        if n not in b.namelist():
            print(f"FAIL: part missing in output: {n}"); ok = False
        elif a.read(n) != b.read(n) and n not in allowed and not re.match(r"xl/(comments\d+\.xml|drawings/vmlDrawing\d+\.vml)$", n):
            print(f"FAIL: unexpected change in {n}"); ok = False
    for n in ("xl/vbaProject.bin",):
        if n in a.namelist():
            same = a.read(n) == b.read(n)
            print(f"{n} identical: {same}"); ok &= same
    media_same = all(a.read(n) == b.read(n) for n in a.namelist() if n.startswith("xl/media/"))
    print(f"media identical: {media_same}"); ok &= media_same
    ca, cb = cells_of(a.read(sheet_part)), cells_of(b.read(sheet_part))
    changed = {k for k in set(ca) | set(cb) if ca.get(k) != cb.get(k)}
    unexpected = changed - set(values)
    print(f"cells changed: {len(changed)}; intended: {len(values)}; unexpected: {sorted(unexpected)}")
    if unexpected:
        ok = False
    print("VERIFY OK" if ok else "VERIFY FAILED")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--values", required=True)
    ap.add_argument("--comments")
    ap.add_argument("--sheet", default="Design")
    ap.add_argument("--author", default="Claude (for ASB)")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--allow-formula", nargs="*", default=[],
                    help="cells whose template formula may be overwritten (rare; say why in the comment)")
    a = ap.parse_args()
    values = json.load(open(a.values))
    if a.verify:
        sys.exit(0 if verify(a.template, a.out, values, a.sheet) else 1)
    comments = json.load(open(a.comments)) if a.comments else {}
    fill(a.template, a.out, values, comments, a.sheet, a.author, set(a.allow_formula))
    print(f"Wrote {a.out}: {len(values)} values, {len(comments)} comments")
    sys.exit(0 if verify(a.template, a.out, values, a.sheet) else 1)


if __name__ == "__main__":
    main()
