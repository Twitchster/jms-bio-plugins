# Selection log format

File: `<Project Number>-Selection Log.xlsx`, saved in `Equipment List PDFS\Projects\<project number>\` next to the PDFs. Build it with `scripts/selection_log.py log.json <out.xlsx>`; the script's docstring has the JSON layout. Keep `log.json` in the session so revisions start from it.

**Why it exists:** six months later, an engineer of record asks "why RS-5X?" or an R&R questions a selection. The log answers with the spec paragraph, the cut-sheet page, and the decision.

## Sheets
| Sheet | One row per | Columns |
|---|---|---|
| Components | selected item | item, equipment, source (spec / calc / jms-std), spec para or calc cell, tags, qty, vendor, model / part number, library file, marked pages, output PDF, status (final / provisional / missing data sheet) |
| Compliance | spec requirement checked | item, requirement, spec para, what the cut sheet offers (file, page), result (compliant / deviation / n/a), note |
| Decisions | deviation | item, deviation, options considered, decision (accept / RFI / exception / open), decided by, date, RFI or exception reference |
| Revisions | submittal revision | rev, date, what changed |

## Rules
- **Fill Compliance as you select (step 4),** not after. It is the evidence the PE reviews and the independent check uses.
- **Write requirements the way the spec states them,** and cite the paragraph. Cite the cut-sheet page for what's offered.
- **Decisions:** "accept" means the PE accepted a deviation without an exception. Record who decided and when.
- **Highlighting:** provisional items, deviations and open decisions are shaded so they stand out.
- **After an R&R:** add a Revisions row, update the affected rows, and save the log under the same name. The PDFs get new revision files; the log is the running record.
