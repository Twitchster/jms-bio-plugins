---
name: conveyor-calcs
description: >
  This skill should be used when a JMS Bio-HANDLING engineer asks to "fill out the belt conveyor
  calc", "fill out the screw conveyor calc sheet", "run the Bio-BELT calculator", "do the screw
  process calc from this spec", "take this spec and fill the JMS calculation sheet", "size this
  conveyor and pick the SEW drive", or shares a project spec (and optionally drawings) for a
  Bio-BELT or Bio-SCREW and wants the JMS calculation workbook completed through SEW gearmotor
  selection.
metadata:
  version: "0.5.0"
---

# Conveyor Calculation Workflow (Bio-BELT and Bio-SCREW)

Take project documents, fill the JMS calculation workbook's **Design** sheet, review it with the engineer in a Claude doc, run the SEW selection, close out the sheet, and deliver the workbook plus SEW's product data PDF. This is the workflow agreed with ASB on Oct 1 2026, refined over the first belt and screw runs.

Load with: `source-documents` (intake), `sew-drive-selection` (step 4), `submittal-review` (the spec-conflicts list feeds it), `jms-bio-conventions` (naming, folders).

## Templates (shipped with the plugin)

| Conveyor | Template file | Revision | Cell map |
|---|---|---|---|
| Bio-BELT | `templates/Bio-BELT_Calculator-Estimate_Template_REV_4.7.xlsm` | REV 4.7 (Revision sheet 4) | `references/belt-rev4.7-cell-map.md` |
| Bio-SCREW (shafted and shaftless) | `templates/XXXXX-SCREW_PROCESS_REV21.xlsx` | REV 21 (Jun 2026: lift HP 1.7, shaft shear fix, thrust) | `references/screw-rev21-cell-map.md` |

If the user supplies a newer template, use theirs. Run `scripts/inspect_template.py` on it and compare against the cell map before filling (step 1).

## Hard rules for the workbook

- **Keep the format exactly.** Write values into **Design-sheet input cells only**: yellow = primary input, blue = secondary input, per the Instructions-sheet legend. Never fill other sheets.
- **Never overwrite a template formula.** `fill_calc.py` refuses unless the cell is passed with `--allow-formula`. Use that only for formula defaults the template expects you to override, such as the screw density and solids defaults (AP11, AP12). Say so in the comment.
- **Notes go in cell comments, not cell text.** Every filled input gets a comment with its source:
  - the spec section and paragraph
  - the drawing number
  - "per <initials> (date)" for the engineer's own choices
  - "ASSUMPTION – …" or "PLACEHOLDER – …" (with what would replace it)
  - "OPEN – …" for missing items

  Leave NOTES-type text cells empty; put that text in their comments.
- **Edit with `scripts/fill_calc.py` only.** It changes the Design sheet XML, comments and VML, and copies every other part byte-for-byte; openpyxl saving would drop images and break the .xlsm. It ends with a verification, and the build fails unless it reports `VERIFY OK`.
- **Recalculate only on a throwaway copy.** `scripts/recalc_readout.py` runs LibreOffice on a copy to read results. Never deliver a LibreOffice-saved file.
- **#NAME? in part-number cells is expected.** XLOOKUP part-number cells return #NAME? in LibreOffice; Excel computes them. The delivered file recalculates on open (fullCalcOnLoad).
- **Name the output** `PROJ-TAG_CALC_REVX`, e.g. `CLCWA-BBC_CALC_REVA.xlsm` or `25026-SSC-1_SCREW-PROCESS_CALC_REVA.xlsx`. Keep the template's extension.

## The workflow

### 1. Intake
- Ask for the document checklist via `source-documents`:
  - the equipment spec section **with all addenda**
  - the common motor section (e.g., 40 05 93)
  - Division 01
  - the electrical area classification
  - any motor data sheet
  - drawings (optional at the start; they may not exist yet)
- Read PDFs fully, **including annotations and markups.** Reviewer sticky notes and red markups from JMS staff are inputs. Extract them with PyMuPDF/pypdf, and render the pages to check.
- Run `inspect_template.py <template>` and check its revision and input list against the cell map. If they differ, stop and rebuild the map. Don't fill a changed layout from an old map.

### 2. First fill
- Fill every input the documents support. Build `values.json` and `comments.json` keyed by cell; see the cell map for meanings and worked-example notes.
- **Without drawings, run in preliminary mode:**
  - Use spec geometry first, tagged "verify against drawings".
  - Where geometry is missing, use the worst case the spec allows and say so.
  - Name the input that dominates the result. On the first belt run, skirtboard length was about 52% of effective tension.
- Recalculate (`recalc_readout.py <file> --outputs --cells …`) and read the results.
- **Send one batch of questions,** each marked **blocking** or **non-blocking**.
  - Area classification is **blocking for JMS-selected sensors, switches and enclosures** (pull cords, zero-speed sensor, alignment switches, panels).
  - It is **not blocking for the motor:** SEW sources the final motor from the datasheet JMS sends. The classification travels with the SEW request instead.
- Compare any spec motor HP against the calculated demand. A large gap is a hint that the assumed geometry is wrong.
- Check spec stress rules that the sheet doesn't cover. See `references/lessons-learned.md`: the belt drive-shaft spec method and the screw spiral 0.3 Fy rule.

### 3. Review (Claude doc)
- Create a Claude doc using the Docs artifact type, with the structure in `references/review-doc-format.md`:
  - input register: cell, value, source, status
  - results summary
  - design-basis decisions
  - open items
  - spec conflicts
  - SEW request notes
- The doc is a register plus results, not a copy of the sheet; the workbook stays the only place anything is calculated.
- The engineer edits the doc, comments on it, or answers questions in chat. If they send back an edited spreadsheet summary, diff it against what you sent.
- After each round: apply the edits, re-fill, recalculate, and update the doc results. Tag every override "per <initials> (date)".
- When a result-driven choice is needed (operating speed, shaft size, spiral type), offer 2–4 options with their computed consequences.
- **Repeat until the engineer replies "confirmed".** Don't start step 4 before that.

### 4. SEW selection
- Run `sew-drive-selection` using the confirmed values:
  - output rpm target **and minimum**, e.g. "10 rpm, not below 9.4" when a stress limit sets a floor
  - motor HP and required fB
  - hollow bore = drive-shaft diameter
  - gear unit type by product, and mounting position
- Put the area classification, spec motor requirements (IEEE 841, NEMA design, SF, bearing life, nameplate, spares) and thrust and overhung loads into the notes for SEW.

### 5. Close-out (use your own selection)
- Enter the configurator selection's values into the sheet. Belt: selected drum rpm (P58), gearbox weight (AM34), drive rows. Screw: gearbox output speed (AJ21), drive rows. See the cell maps.
- Comment each of these cells "from configurator selection (<type designation>) — replace with SEW quote value". The engineer updates them manually when SEW's quote arrives.
- Re-run every check. **If any check fails, go back to step 4** and tell the engineer what changed.

### 6. Deliverables
1. **The final workbook,** verified by `fill_calc.py --verify`.
2. **SEW's Product Data PDF** for the selected unit, downloaded at the end of the configurator: Summary → Product data → PDF. See `sew-drive-selection` → `references/sew-website-procedure.md`.
3. **The spec-conflicts list,** in the review doc; it feeds `submittal-review` as clarifications or exceptions.

Don't deliver a separate SEW-selection spreadsheet. The engineer opens the workbook in Excel, checks that every pass/fail cell reads correctly, and signs off. This is a design calc that may go into a submittal, so the final check is theirs.

## References
- `references/belt-rev4.7-cell-map.md`, `references/screw-rev21-cell-map.md`: every input cell, dropdown, template value, a worked-example note, and the key result cells
- `references/review-doc-format.md`: Claude doc structure for step 3
- `references/lessons-learned.md`: technical findings from the first runs (spec checks the sheets miss, dominant inputs, template quirks)
- `scripts/inspect_template.py`, `scripts/fill_calc.py`, `scripts/recalc_readout.py`
