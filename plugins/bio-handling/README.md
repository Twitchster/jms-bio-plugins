# bio-handling

A Claude plugin for JMS Bio-HANDLING project engineers. It encodes JMS standards, workflows and lessons learned so Claude can help with submittals, drawing checks, design checks and O&M manuals the way the PE team does them.

## Components

| Skill | Use it for | Example requests |
|---|---|---|
| jms-bio-conventions | Folders, file naming, email subjects, P/N designators, drawing standards, workflows, roles. Other skills load it. | "Where does the stamped RISA report go?" "What's the designator for a wedge gate?" |
| submittal-review | Spec section review (clarifications/exceptions/RFIs) and R&R comment-response logs | "Review 46 01 01 for exceptions." "We got an R&R on 25003 — build the response log." |
| drawing-check | Fab check packages and vendor approval drawings | "Do my fab check on this package." "Is this Vortex gate approval drawing OK?" |
| design-checks | Screws, gates, hoppers/live bottoms/silos, drives/motors, RISA/seismic/anchors | "Check this Bio-SCREW calc." "What head load for this slide gate blade?" |
| om-manual | Lists the documents needed, then drafts the O&M from the JMS starting-point templates (Bio-BELT, Bio-SCREW shafted/shaftless, Bio-HOPPER, Bio-GATE, Bio-DIVERTER; templates included); 01 33 00 closeout forms | "Create the O&M for the 25026 shaftless screws." "What do you need for the hopper O&M?" |
| conveyor-calcs | Spec → JMS Bio-BELT (REV 4.7) or Screw Process (REV 21) calc workbook: batched questions, Claude-doc review, SEW selection, close-out; delivers the filled workbook + SEW Product Data PDF. Blank templates included. | "Fill out the belt conveyor calc from this spec." |
| sew-drive-selection | Turns calc-sheet drive data into a JMS-compliant SEW gearmotor selection on SEW's online DriveConfigurator (via the browser on your computer), following the JMS SEW Selection standard; outputs a selection summary and a draft quote request | "Select the SEW gearmotor from this Bio-SCREW calc." |
| plugin-update | Checks the plugin's GitHub repository for a newer version and, only when asked, packages it for you to install. Never updates on its own. | "Check for plugin updates." "Update the bio-handling plugin." |
| source-documents | When information is missing, asks for the specific file known to contain it (with location, section and what's needed), in one batched request; used by all the skills above | "What file do you need for the motor spec?" |

**Connector:** Microsoft 365 (Outlook, SharePoint, Teams). Each user signs in with their own JMS account. The S:\ drive and Outlook Public Folders are not reachable through it; attach those files directly.

No agents or hooks.

## Where the content came from

The rules come from Bio-HANDLING engineering emails, procedures and project lessons, Mar–Sep 2026. Each design recommendation is tagged [Code/Spec], [JMS std], [Lesson] or [Judgment]. Where JMS history conflicts, the current position is stated and the conflict is flagged; shaft tolerances and the gate head-load basis are examples. Names in `roles.md` are as of Sep 2026. Use roles in documents.

## Updates

Updates are manual. The plugin pulls from the repository named in `update-source.json` only when a user asks ("update the bio-handling plugin"), then hands them a `.plugin` file to install. Every release needs a version bump and a CHANGELOG entry in the repository. The repository is public, so no GitHub account is needed to update.

## Maintaining it

- **Standards change often.** Update the reference files when a procedure changes: SEW selection, calculator versions, shaft tolerance, gate policy. Then bump the version in `.claude-plugin/plugin.json`.
- **The gate standard clarification is a draft.** Engineering management wanted official verbiage; replace the draft in `submittal-review/references/standard-clarifications.md` when it exists.
- **Source map:** add rows to `source-documents/references/source-map.md` whenever the team learns where a piece of information reliably lives. Spec section numbers there are typical examples, not fixed.
- **SEW standard:** `sew-drive-selection/references/jms-sew-selection-procedure.md` transcribes the Rev 0 (unapproved) JMS SEW standard. Replace it when an approved revision is issued. The website steps were verified against DriveConfigurator Release 26.7 (Sep 2026); SEW may change the site.
- **Calculator cell maps:** once a calculator's cells are confirmed, add them to `sew-drive-selection/references/calc-field-map.md`.
- **O&M templates:** when Technical Writing revises a starting point, replace the file in `om-manual/templates/`, re-run `scripts/om_template_tool.py inspect` on it, and update `om-required-documents.md` and `om-template-rules.md` for any changed drafter notes. The generic `om-outline.md` is only for products without a template.

## Limits

- Claude does not replace the engineer of record or the stamping engineer. All calcs and letters need PE review.
- Content is internal to JMS. Don't distribute outside the company.

Author: Amr Banawan, Project Engineer, Bio-HANDLING. Version 0.6.0.
