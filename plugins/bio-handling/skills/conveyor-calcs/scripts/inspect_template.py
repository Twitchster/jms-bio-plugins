#!/usr/bin/env python3
"""Inspect a JMS calculation workbook: version, input cells, dropdowns and labels.

Usage:
  python3 inspect_template.py <workbook.xlsx|.xlsm> [--sheet Design] [--json out.json] [--all]

What it does:
  - Reads the color legend on the 'Instructions' sheet (column B fills next to
    "Primary input", "Secondary input", "Calculation", "Primary output pass",
    "Output warning", "Output failure").
  - Classifies every non-empty or filled cell on the Design sheet by that legend.
  - For each input cell, prints: cell, class, label (nearest text to the left or
    above), current value, data-validation list (dropdown source) and any existing
    comment.
  - Prints the template revision from the 'Revision' sheet (highest revision number).

Use it at intake (step 1) to confirm the template revision matches the cell map
in references/, and to rebuild the map when JMS issues a new template revision.
Reads with openpyxl in read-only fashion; never writes the workbook.
"""
import argparse
import json
import re
import sys
import warnings

import openpyxl
from openpyxl.utils import range_boundaries, get_column_letter

warnings.filterwarnings("ignore")

LEGEND_KEYS = [
    ("primary_input", r"primary input"),
    ("secondary_input", r"secondary input"),
    ("calculation", r"calculation"),
    ("output_pass", r"output.*pass"),
    ("output_warning", r"output.*warning"),
    ("output_failure", r"output.*fail"),
]


def color_key(cell):
    f = cell.fill
    if not f or not f.fill_type:
        return None
    c = f.fgColor
    if c is None:
        return None
    if c.type == "rgb" and c.rgb not in (None, "00000000"):
        return ("rgb", str(c.rgb))
    if c.type == "theme":
        return ("theme", c.theme, round(c.tint or 0, 3))
    if c.type == "indexed":
        return ("indexed", c.indexed)
    return None


def read_legend(wb):
    if "Instructions" not in wb.sheetnames:
        return {}
    ws = wb["Instructions"]
    legend = {}
    for row in ws.iter_rows(min_row=1, max_row=30):
        for c in row:
            if not isinstance(c.value, str):
                continue
            for key, pat in LEGEND_KEYS:
                if re.search(pat, c.value, re.I) and key not in legend:
                    # swatch is the cell to the left (column B) in JMS templates
                    sw = ws.cell(c.row, c.column - 1) if c.column > 1 else None
                    ck = color_key(sw) if sw is not None else None
                    if ck:
                        legend[key] = ck
    return legend


def template_revision(wb):
    if "Revision" not in wb.sheetnames:
        return None
    ws = wb["Revision"]
    revs = []
    for row in ws.iter_rows(min_row=1, max_row=300, max_col=6):
        for c in row:
            if isinstance(c.value, (int, float)) and not isinstance(c.value, bool) and 0 <= c.value < 1000 and c.column <= 3:
                revs.append(c.value)
    return max(revs) if revs else None


def label_for(ws, r, col, merged_lookup):
    # walk left along the row for a text label, skipping the cell's own merged block
    for cc in range(col - 1, max(0, col - 25), -1):
        v = ws.cell(r, cc).value
        if v is None:
            anchor = merged_lookup.get((r, cc))
            if anchor:
                v = ws.cell(*anchor).value
        if isinstance(v, str) and v.strip() and not v.strip().startswith("="):
            return v.strip().replace("\n", " ")[:80]
    for rr in range(r - 1, max(0, r - 3), -1):
        v = ws.cell(rr, col).value
        if isinstance(v, str) and v.strip() and not v.strip().startswith("="):
            return v.strip().replace("\n", " ")[:80]
    return ""


def dv_map(ws):
    out = {}
    for dv in ws.data_validations.dataValidation:
        if dv.type != "list":
            continue
        for rng in str(dv.sqref).split():
            minc, minr, maxc, maxr = range_boundaries(rng)
            for r in range(minr, maxr + 1):
                for c in range(minc, maxc + 1):
                    out[f"{get_column_letter(c)}{r}"] = dv.formula1
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("workbook")
    ap.add_argument("--sheet", default="Design")
    ap.add_argument("--json")
    ap.add_argument("--all", action="store_true", help="also list calculation/output cells")
    a = ap.parse_args()

    wb = openpyxl.load_workbook(a.workbook, data_only=False)
    if a.sheet not in wb.sheetnames:
        print(f"ERROR: sheet '{a.sheet}' not found. Sheets: {wb.sheetnames}")
        sys.exit(2)
    legend = read_legend(wb)
    inv = {v: k for k, v in legend.items()}
    ws = wb[a.sheet]
    merged_lookup = {}
    for mr in ws.merged_cells.ranges:
        for r in range(mr.min_row, mr.max_row + 1):
            for c in range(mr.min_col, mr.max_col + 1):
                merged_lookup[(r, c)] = (mr.min_row, mr.min_col)
    dvs = dv_map(ws)

    print(f"Workbook: {a.workbook}")
    print(f"Sheets: {wb.sheetnames}")
    print(f"Template revision (Revision sheet): {template_revision(wb)}")
    print(f"Legend: {legend}")
    if not legend:
        print("WARNING: no color legend found on Instructions; input detection by color is unavailable.")

    cells = []
    for row in ws.iter_rows():
        for c in row:
            ck = color_key(c)
            cls = inv.get(ck)
            if cls is None:
                continue
            if (c.row, c.column) in merged_lookup and merged_lookup[(c.row, c.column)] != (c.row, c.column):
                continue  # not the anchor of a merged block
            if not a.all and cls not in ("primary_input", "secondary_input"):
                continue
            v = c.value
            cells.append({
                "cell": c.coordinate,
                "class": cls,
                "label": label_for(ws, c.row, c.column, merged_lookup),
                "value": v if not isinstance(v, str) else v[:120],
                "is_formula": isinstance(v, str) and v.startswith("="),
                "dropdown": dvs.get(c.coordinate),
                "comment": (c.comment.text[:200].replace("\n", " ") if c.comment else None),
                "comment_author": (c.comment.author if c.comment else None),
            })

    # Collapse horizontal runs of adjacent same-class cells (some templates color an
    # input as several unmerged cells). Keep one entry per run: the first cell holding a
    # value, or the run's first cell if all are empty; record the run span.
    from openpyxl.utils.cell import coordinate_from_string, column_index_from_string
    grouped, run = [], []

    def flush():
        if not run:
            return
        anchor = next((x for x in run if x["value"] is not None), run[0])
        anchor = dict(anchor)
        anchor["span"] = f"{run[0]['cell']}:{run[-1]['cell']}" if len(run) > 1 else run[0]["cell"]
        anchor["dropdown"] = anchor["dropdown"] or next((x["dropdown"] for x in run if x["dropdown"]), None)
        anchor["comment"] = anchor["comment"] or next((x["comment"] for x in run if x["comment"]), None)
        grouped.append(anchor)

    prev = None
    for d in cells:
        col, row = coordinate_from_string(d["cell"])
        ci = column_index_from_string(col)
        if prev and prev[0] == row and prev[1] == ci - 1 and prev[2] == d["class"] and (d["value"] is None or all(x["value"] is None for x in run)):
            run.append(d)
        else:
            flush()
            run = [d]
        prev = (row, ci, d["class"])
    flush()
    cells = grouped

    for d in cells:
        dd = f" [list {d['dropdown']}]" if d["dropdown"] else ""
        print(f"{d['cell']:>6} {d['class']:<15} {d['label'][:45]:<45} = {str(d['value'])[:40]}{dd}")
    print(f"\n{len(cells)} cells listed "
          f"({sum(1 for d in cells if d['class']=='primary_input')} primary inputs, "
          f"{sum(1 for d in cells if d['class']=='secondary_input')} secondary inputs)")
    if a.json:
        with open(a.json, "w") as f:
            json.dump({"workbook": a.workbook, "revision": template_revision(wb), "legend": {k: list(v) for k, v in legend.items()}, "cells": cells}, f, indent=1, default=str)
        print(f"Wrote {a.json}")


if __name__ == "__main__":
    main()
