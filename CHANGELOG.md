# Changelog — bio-handling plugin

Every change to `plugins/bio-handling/` must bump `version` in `plugins/bio-handling/.claude-plugin/plugin.json` and add an entry here. Claude only delivers an update when the version changes, and the PR check enforces the bump.

Format: `## <version> — <date> — <author>`, then what changed and why. Note any change to an engineering rule explicitly, so reviewers can see it.

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
