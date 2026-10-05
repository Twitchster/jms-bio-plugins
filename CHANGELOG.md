# Changelog — bio-handling plugin

Every change to `plugins/bio-handling/` must bump `version` in `plugins/bio-handling/.claude-plugin/plugin.json` and add an entry here. Claude only delivers an update when the version changes, and the PR check enforces the bump.

Format: `## <version> — <date> — <author>`, then what changed and why. Note any change to an engineering rule explicitly, so reviewers can see it.

## 0.7.0 — 2026-10-05 — Amr Banawan
- **New `cutsheet-markup` skill (v1, not yet run on a live project):** submittal cat cuts for purchased components.
  - **What it does:** reads the spec and calcs, lists the components (spec-required / calc-driven / JMS standard), and selects spec-compliant options from the shared OneDrive library `Equipment List PDFS`.
  - **Outputs:** one marked-up PDF per component (`<Project Number>-<Equipment Name>.pdf`) plus `<Project Number>-Selection Log.xlsx`, saved to `Equipment List PDFS\Projects\<project number>\`.
  - **Workflow:** PE confirms the list → missing data sheets list right away → compliance table → deviation decisions (accept / RFI / exception) → independent check → PE reviews the PDFs → save → new data sheets go into the library clean.
- **JMS markup style recorded:** Bluebeam-type rectangle, red 1 pt border, orange fill at 30 %, PE username as author, around the selected row; a column box for cell selections. Labels only when the project requires them. Cover sheet with equipment name and tags.
- **Library rule:** library files are never edited. 38 carry markups from earlier projects, so every working copy is stripped before marking. New data sheets are added clean, never overwritten (older editions go to `Archive`).
- **New scripts:**
  - `cutsheet_markup.py`: `audit`, `find` (whole-token matching, so RS-5X ≠ RS-5XL), `rows`, `packet` (strip / mark / cover sheet / merge with bookmarks), `render`
  - `selection_log.py`: writes the log workbook
- **New references:** `library.md` (structure, conventions, old-markup list, pages without text, additions log, worked examples), `selection-log.md`. Updated the source map and README.

## 0.6.0 — 2026-10-05 — Amr Banawan
- **`om-manual` now drafts from the JMS O&M starting-point templates**, shipped in `om-manual/templates/`: Bio-BELT (Rev 1), Bio-SCREW shafted (Rev 0), Bio-SCREW shaftless (Rev 1), Bio-HOPPER (Rev 0), Bio-GATE (Rev 0), Bio-DIVERTER (Rev 0).
- **New `references/om-required-documents.md`:** what Claude asks for when asked to create an O&M, built from the templates' drafter notes:
  - Part A: documents every product needs (approved submittal, numerical-revision GA/SA/FA, BOM, spec/Div 01, project identity, calcs, vendor installation and lubrication data, anchor instructions, field service, warranty, controls)
  - Part B: product-specific documents, each marked blocking or non-blocking, with its "only if" condition
  - Part C: SEW data (quote for mounting position and oil, catalog mounting diagram, closing-plug PDF, current SEW manual for plug torque)
  - the configuration facts per product that select template options
- **New `references/om-template-rules.md`:** template conventions (highlight = fill-in, brackets = options, comments = drafter notes), the fill procedure, the SEW lubrication block, bearing defaults and per-template quirks (Diverter inputs page, Gate storage, Hopper/Gate split).
- **New `scripts/om_template_tool.py`:** `inspect` (drafter notes with section and anchor, fill-ins, options, content controls), `prepare` (strip template comments, set field update on open), `check` (leftover notes, highlights, placeholders, broken references).
- **Workflow change:** Claude presents the required-documents list first, confirms the configuration it read from the documents, then fills the template. Open items go in Word comments.
- **Rules now explicit:** the approved submittal governs, except the spare-parts list, where the GA table is the latest (raise differences with the PM); drawings must be at a numerical revision; a Bio-GATE always gets its own O&M.
- `om-outline.md` is now only the fallback for products without a template. Updated the source map and README.

## 0.5.1 — 2026-10-01 — Amr Banawan
- Shortened the plugin description to under 500 characters. No skill changes.

## 0.5.0 — 2026-10-01 — Amr Banawan
- **New `conveyor-calcs` skill:** the spec-to-calc workflow agreed in the "Belt conveyor JMS calculations" chat.
  1. intake
  2. first fill with batched blocking/non-blocking questions
  3. Claude-doc review until "confirmed"
  4. SEW selection
  5. close-out using Claude's own selection
  6. deliver the workbook + SEW Product Data PDF
- **Blank templates included:** Bio-BELT Calculator-Estimate REV 4.7 (.xlsm) and Screw Process REV 21 (.xlsx).
- **Design-sheet cell maps for both templates,** generated from the template color legend, with worked-example notes from the first runs (CLCWA belt, 25026 SSC-1 screw).
- **Scripts:**
  - `inspect_template.py`: revision and input-cell check
  - `fill_calc.py`: XML-level fill that keeps macros and images; refuses to overwrite formulas; self-verifies
  - `recalc_readout.py`: LibreOffice recalculation on a throwaway copy
  - Tested by rebuilding both first-run workbooks from the blanks: every recalculated pass/fail output matched.
- **Rule changes:**
  - Area classification no longer blocks the SEW motor selection. SEW sources the final motor, and the classification goes in the SEW notes. It still blocks JMS-selected sensors, switches and enclosures. (ASB)
  - The SEW deliverable is now SEW's Product Data PDF, not a selection spreadsheet. The PDF download procedure and configurator quirks were added to `sew-drive-selection`. (ASB)

## 0.4.1 — 2026-10-01 — Amr Banawan
- Update source set to the public repository `Twitchster/jms-bio-plugins`. Updates need no GitHub account.
- Restored the hidden files lost in the GitHub web upload, without which the plugin can't be installed:
  - `.claude-plugin/marketplace.json`
  - `plugins/bio-handling/.claude-plugin/plugin.json`
  - `plugins/bio-handling/.mcp.json`
  - `.github/*`
  - `.gitignore`
- Docs updated for a public repository.

## 0.4.0 — 2026-09-30 — Amr Banawan
- Added `plugin-update` skill and `update-source.json`.
  - The plugin now knows its private GitHub repository and pulls updates **only when a user asks** ("update the bio-handling plugin").
  - It shows the changelog between versions, validates the repository, and packages the new version for the user to install.
- Distribution is manual by design: no automatic sync, no auto-update.

## 0.3.0 — 2026-09-30 — Amr Banawan
- Added `sew-drive-selection` skill: calc-sheet data → JMS-compliant SEW gearmotor selection on SEW's online DriveConfigurator (verified against Release 26.7).
- Added a transcription of the JMS Engineering Standard "SEW Gearmotor/Gearbox Selection" (Rev 0, unapproved draft, owner DED) as the governing SEW reference.
- **Rule changes:**
  - "Frequency inverter operation" is now always checked.
  - Ambient temperature must stay on "No thermal calculation" (otherwise contact SEW).
  - Thermistors: recommend exception; a panel relay is needed otherwise.

## 0.2.0 — 2026-09-30 — Amr Banawan
- Added `source-documents` skill: maps missing information to the document known to contain it, and asks for those files in one batched request.
- All task skills now use it before asking the user for information.

## 0.1.0 — 2026-09-30 — Amr Banawan
- Initial plugin with five skills:
  - `jms-bio-conventions`
  - `submittal-review`
  - `drawing-check`
  - `design-checks`
  - `om-manual`
- Includes the Microsoft 365 connector.
