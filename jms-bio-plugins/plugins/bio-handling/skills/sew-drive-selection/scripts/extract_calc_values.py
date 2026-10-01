#!/usr/bin/env python3
"""List labeled numeric values from a JMS calculation workbook.

Usage: python3 extract_calc_values.py <workbook.xlsx|.xlsm> [--grep WORD ...]

For every numeric cell (cached value), prints sheet, cell, the nearest text label
(same row to the left, or the cell above), the value, and any unit text to its right.
Formulas are not evaluated: values come from the workbook's last save in Excel.
If most values show as None, ask the user to open and save the file in Excel.
"""
import sys
import openpyxl

DRIVE_TERMS = ["hp", "horsepower", "rpm", "speed", "torque", "service", "sf", "shaft",
               "dia", "thrust", "axial", "overhung", "ohl", "radial", "incline", "angle",
               "capacity", "fill", "motor", "reducer", "ratio", "rev", "version"]


def label_for(ws, r, c):
    for cc in range(c - 1, max(0, c - 8), -1):
        v = ws.cell(r, cc).value
        if isinstance(v, str) and v.strip():
            return v.strip()
    if r > 1:
        v = ws.cell(r - 1, c).value
        if isinstance(v, str) and v.strip():
            return v.strip()
    return ""


def unit_for(ws, r, c):
    v = ws.cell(r, c + 1).value
    return v.strip() if isinstance(v, str) and len(v.strip()) <= 15 else ""


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    path = sys.argv[1]
    terms = [t.lower() for t in sys.argv[3:]] if "--grep" in sys.argv[2:3] else DRIVE_TERMS
    wb = openpyxl.load_workbook(path, data_only=True, read_only=False)
    total = empty = 0
    wbf = openpyxl.load_workbook(path, data_only=False, read_only=False)
    for ws in wb.worksheets:
        wsf = wbf[ws.title]
        for row in ws.iter_rows():
            for cell in row:
                f = wsf.cell(cell.row, cell.column).value
                is_formula = isinstance(f, str) and f.startswith("=")
                v = cell.value
                if is_formula and v is None:
                    empty += 1
                    lab = label_for(ws, cell.row, cell.column)
                    if not terms or any(t in lab.lower() for t in terms):
                        print(f"{ws.title}!{cell.coordinate}\t{lab[:60]}\tNO CACHED VALUE\t\tformula {f[:40]}")
                    continue
                if not isinstance(v, (int, float)) or isinstance(v, bool):
                    continue
                total += 1
                lab = label_for(ws, cell.row, cell.column)
                if terms and not any(t in lab.lower() for t in terms):
                    continue
                print(f"{ws.title}!{cell.coordinate}\t{lab[:60]}\t{v}\t{unit_for(ws, cell.row, cell.column)}"
                      f"\t{'formula' if is_formula else 'input'}")
    print(f"\n# numeric cells: {total}; formula cells with no cached value: {empty}", file=sys.stderr)
    if empty and empty > total * 0.3:
        print("# WARNING: many formulas have no cached values. Ask the user to open and save in Excel.",
              file=sys.stderr)


if __name__ == "__main__":
    main()
