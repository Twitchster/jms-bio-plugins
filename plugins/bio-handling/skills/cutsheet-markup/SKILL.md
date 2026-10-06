---
name: cutsheet-markup
description: >
  This skill should be used when a JMS Bio-HANDLING engineer asks to "mark up the cut sheets",
  "build the cat cuts for the submittal", "select the purchased components from the spec",
  "put together the component cut sheets or catalog cuts for this project", "which purchased parts does
  this spec need", or shares a project spec and calc sheets for submittal catalog cuts.
metadata:
  version: "0.7.1"
---

# Submittal Cat Cuts: purchased-component selection and markup

Read the project spec and calcs, list the purchased components, select spec-compliant options from the JMS equipment PDF library, and deliver one marked-up PDF per component plus a selection log, saved to the project folder in the library. The workflow was agreed with ASB on Oct 5 2026. It is **v1: not yet run on a live project**. Record what changes on the first jobs in `references/library.md` and this file.

Load with: `source-documents` (missing information), `submittal-review` (deviations become clarifications, exceptions or RFIs), `jms-bio-conventions` (naming, folders), `conveyor-calcs` / `sew-drive-selection` (calc-driven and SEW items).

## Scope
- **Purchased components with vendor data sheets:** switches, sensors, actuators, bearings, gearboxes, motors, anchors, belts, splice kits, idlers, scrapers, load cells, etc.
- **JMS-fabricated equipment** is defined by the calc sheet and drawings, not here. If the library has a cat cut for a calc-driven item, include it.
- **Submittals only**, for now.

## Library and output (fixed)
- **Library:** `C:\Users\<user>\OneDrive - Jim Myers & Sons, Inc\Equipment List PDFS` (ASB's OneDrive, shared to the team with edit access). Details, conventions and known issues: `references/library.md`.
- **Access:** through the computer linked to the session. Ask for the library folder with the folder-access tool if it isn't connected. Files may be cloud-only; staging them downloads them. Without a linked computer, the Microsoft 365 connector can read text only (no files, nothing over 100 MB), which isn't enough to mark up; say so and ask the user to link the computer.
- **Output folder:** `Equipment List PDFS\Projects\<project number>\`. Create it if missing.
- **Output files:** one PDF per selected piece of equipment, `<Project Number>-<Equipment Name>.pdf` (e.g. `25026-Zero Speed Switch.pdf`). If two different selections share an equipment name, add the tag: `25026-Gearbox (SSC-1).pdf`. After an R&R, write a new revision; never overwrite a submitted file.
- **Selection log:** `<Project Number>-Selection Log.xlsx` in the same folder (`references/selection-log.md`, `scripts/selection_log.py`).
- **Never edit library files.** 38 of them carry markups from earlier projects; leave them. Every working copy is stripped of all markups before marking (the packet script does this).

## Markup style (JMS)
- **Selection box:** Bluebeam-type Rectangle, red 1 pt border, orange fill (1, .502, .251) at 30 % opacity, author = the PE's username (e.g. `ABanawan`). Box the whole selected table row or model line. When the selection is a table cell, add a second box on the column, so the cell is where they cross.
- **Selections chain:** a choice on one page can decide a column on another (compound OR → OR/FR/FDA min-pulley column).
- **Unmarked pages:** pages without options stay unmarked; include the whole cut sheet.
- **Labels:** off by default. Add red text labels only when the PE says the project requires them; they spell out the selection for the reader.
- **Cover sheet:** the library's `#Component Cover Sheet` page, stripped, with the equipment name and tags (black Helvetica 28 pt, centered). Library cover sheets carry stale tags (CONV-960/961); never reuse them.

## Workflow
1. **Intake.** The PE provides the project spec (with addenda), calc sheets and any other documents. Ask for the PE's username (markup author) and the equipment tags if they aren't in the documents.
2. **Read and list.** Read everything fully, including annotations and markups. Build the component list. For each item give:
   - source tag: *spec-required* / *calc-driven* / *JMS standard*
   - spec paragraph or calc cell
   - tags and quantity
   - key requirements (voltage, NEMA rating, area classification, materials, ratings, listed manufacturers, "or equal")
   - library availability: file found (path) / missing

   Electrical area classification and control voltage usually decide switch and sensor models. If the documents don't state them, ask (`source-documents`); they are blocking for those items.
3. **PE confirms the list** (add / remove / confirm). Right then, give the **missing data sheets list** (item, what's needed, likely source), so the PE can chase them while selections continue.
4. **Compliance table and selections.** For each item, find the library file and pick the compliant option.
   - Per requirement: requirement → spec paragraph → what the cut sheet offers (file, page) → compliant / deviation.
   - If nothing fully complies, pick the closest option and present the deviation with the alternatives.
   - Mark calc- or quote-dependent items **provisional** (e.g. the SEW data sheet comes from the quote; belt rating and pulley sizes from the final calc).
   - Library choice rules: use the current file, never one in `Archive` or marked `Old`/`Locked`, unless it is the only source; prefer the numbered packet files in a component folder, in their numbered order; use `FOR REFERENCE` files only to decode (e.g. the SEW catalog nomenclature), not as packet pages.
5. **Deviation decisions** with the PE: accept / RFI / exception. Exceptions and RFIs feed `submittal-review`.
6. **Independent check.** Launch a separate review agent that has not seen your reasoning. Give it the spec, calcs, the final list and the compliance table. It re-checks every selection against the spec paragraphs and calc values. Fix what it finds and tell the PE.
7. **Build and mark the PDFs.** Write one plan per component and run `scripts/cutsheet_markup.py packet <plan.json> <out.pdf>`. It strips old markups, marks, adds the cover sheet and merges the files with a bookmark per file.
   - Use `find` first to confirm each target text matches once, and the row box it will draw.
   - Use `mode: block` for selections that aren't in a ruled table (e.g. tiles), `column` with `through` for cell selections, and `rect` for pages without a text layer.
   - **Verify:** no NOT FOUND or AMBIGUOUS in the report; `render` every marked page and look at it, since a box can land on a plausible but wrong row; no old markups left; each file ≤ 30 MB (the limit for writing back to the computer).
8. **PE reviews the PDFs.** Send them in the chat; wait for approval.
9. **Save** the PDFs and the selection log (`scripts/selection_log.py`) to `Projects\<project number>\`.
10. **Missing data sheets.** When the PE provides them:
    - add a clean copy to the library: no project markups, named and numbered like its folder, never overwrite; an older edition moves to that folder's `Archive`
    - update `_Library Index.xlsx` in the library root
    - rebuild the affected PDFs and the log

## Open questions (settle on the first jobs, then record here)
- SEW: include the whole dimensional-sheet file or only the selected size's pages? Mark the selected mounting position?
- `.delete` placeholders (datasheet or wiring diagram from the quote) when the quote isn't in hand: a placeholder page, or hold the PDF?
- Duplicate generic vs part-number-specific level-sensor sheets: which goes in?

## References
- `references/library.md`: library structure, file conventions, the old-markup list, files without a text layer, and examples of past selections
- `references/selection-log.md`: the log format
- `scripts/cutsheet_markup.py`: `audit`, `find`, `rows`, `packet`, `render`
- `scripts/selection_log.py`: writes the log workbook from JSON
