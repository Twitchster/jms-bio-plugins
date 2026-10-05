---
name: om-manual
description: >
  This skill should be used when a JMS Bio-HANDLING engineer asks to "draft the O&M", "create an
  O&M for this project", "write the operation and maintenance manual", "put together the O&M for
  the belt / screw / hopper / gate / diverter", "what documents do you need for the O&M", "fill
  out the 01 33 00 closeout forms", "equipment maintenance summary forms", "spare parts list for
  the O&M", or needs closeout documentation for JMS equipment.
metadata:
  version: "0.6.0"
---

# O&M Manual Drafting

Draft the initial Operation & Maintenance manual for JMS Bio-HANDLING equipment from the JMS starting-point templates. The Project Engineer drafts it; the target is to submit 2 weeks before equipment delivery and before Status 4.0 (Initial Shipment). Load `jms-bio-conventions` for naming and folders, `source-documents` for anything missing, and the `docx` skill for editing the Word file.

## Templates (shipped with the plugin)

| Product | Template | Rev |
|---|---|---|
| Bio-BELT | `templates/Bio-BELT_OM_Rev1_Starting_Point.docx` | 1 |
| Bio-SCREW, shafted | `templates/Bio-SCREW_Shafted_OM_Rev0_Starting_Point.docx` | 0 |
| Bio-SCREW, shaftless | `templates/Bio-SCREW_Shaftless_OM_Rev1_Starting_Point.docx` | 1 |
| Bio-HOPPER (always with live bottom; optional leveling screw) | `templates/Bio-HOPPER_OM_Rev0_Starting_Point.docx` | 0 |
| Bio-GATE | `templates/Bio-GATE_OM_Rev0_Starting_Point.docx` | 0 |
| Bio-DIVERTER | `templates/Bio-DIVERTER_OM_Rev0_Starting_Point.docx` | 0 |

If the user supplies a newer template, or a prior JMS O&M for the same product to follow, use theirs and run `scripts/om_template_tool.py inspect` on it first. For other products (silo, live bottom alone, receiving bin, drag conveyor, etc.) there is no template here. Ask for a prior JMS O&M; without one, use `references/om-outline.md` and say it is a generic default, not a JMS template.

**One O&M per product line.** A Bio-GATE always gets its own O&M, even on a hopper. Live bottom and leveling screws are covered by the Bio-HOPPER O&M, but a separate stand-alone screw needs a Bio-SCREW O&M.

## Workflow

### 1. Identify the products and present the required documents
When the user asks for an O&M, **first** work out which template(s) apply (ask if the product or screw type is unclear). Then present the required-documents list from `references/om-required-documents.md` in one message:
- Part A (all products) + the product's Part B + Part C if there is an SEW drive
- each item with what it feeds, where it usually lives, and **Blocking / Non-blocking**
- conditional items with their "only if" condition, unless the user has already ruled them out
- the product's configuration facts, with a note that you'll read them from the drawings, BOM and submittal and confirm them before drafting

Before asking, look for what's already reachable: the conversation, attached files, the user's connected folders, and SharePoint/Outlook through the Microsoft 365 connector. Ask only for what's still missing.

### 2. Read the documents and settle the configuration
- Read the approved submittal, drawings (including notes and tables) and BOM fully.
- Build the equipment list: tags, descriptions, P/Ns, quantities, vendor and model of every purchased component.
- Confirm vendor identity against the approved submittal. Vendor spare-parts lists have named the wrong manufacturer before.
- Show a configuration table: fact, finding, evidence (sheet/note/BOM line), and the template option it selects. Mark anything you couldn't determine. **Wait for the user to confirm.**

### 3. Fill the template
Follow `references/om-template-rules.md`. In short:
1. `python3 scripts/om_template_tool.py inspect <template> --json notes.json` — the drafter notes are the instructions.
2. `python3 scripts/om_template_tool.py prepare <template> <PROJ-PRODUCT_OM_REVX>.docx` — strips the template comments, sets field update on open.
3. Edit the XML per the `docx` skill: fill highlighted fields, resolve bracket options, write scope from the submittal, apply the SEW lubrication block, remove cross-contamination text for carbon steel equipment, fix hand-typed step references.
4. Put open items in Word comments ("OPEN – …", "ASSUMPTION – …", "PLACEHOLDER – …"), not in the body text.
5. `python3 scripts/om_template_tool.py check <file>`, then validate and render per the `docx` skill and look at the pages.

### 4. Deliver
- The filled `.docx`, named `PROJ-PRODUCT_OM_REVX`, with "Prepared By" set to the PE's initials (ask; don't assume).
- An **appendix assembly list**: each appendix item and its source file, marking what's still missing.
- An **open items list** with owner (PE / Engineering / Design / PM / vendor).
- A **check table**: every equipment tag and purchased component in the approved submittal appears in the O&M, the maintenance tables and App A.
- A note to open it in Word, update all fields (also inside the header and footer), and search for "Error".

## Rules
- **The approved submittal governs.** When the O&M draft, a vendor manual or a spare-parts list disagrees with it, use the approved submittal. The exception is spare parts: the GA drawing table is the latest list; raise any difference with the PM.
- **Drawings must be at a numerical revision.** An alphabetical revision means not released: ask Design before using it.
- **Never guess project data**: warranty period, field service days, tag numbers, oil quantities, torques, mounting position. Each comes from a named document, or it stays a highlighted placeholder with an OPEN comment.
- **Keep the template's text and formatting.** Change wording only where a drafter note or the project calls for it; the boilerplate (policies, safety, storage) is JMS-standard.
- If the spec requires closeout forms (Equipment Maintenance Summary, Maintenance Requirements, 01 33 00 / 01 78 23), fill one per equipment item or motor as required and list them as appendices.
- Use English cut sheets and nameplates.

## Missing information
Follow `source-documents` for every gap, naming the specific file and section. The usual sources are in `references/om-required-documents.md`. In short: approved submittal (scope, field service, warranty, cat cuts), drawings (spare parts, tags, options), BOM (materials, anchors, components), SEW quote (mounting position, oil), vendor manuals (lubrication, intervals), spec and Div 01 (cover data, required contents).

## Verification
Cross-check every tag, model number, lubricant, quantity, interval and torque against its source document, and list anything that couldn't be verified. The PE reviews the whole draft before it goes out; it is a contract closeout document.

## References
- `references/om-required-documents.md`: documents to ask for, by product, and the configuration facts
- `references/om-template-rules.md`: template conventions, fill procedure, SEW lubrication block, per-template notes
- `references/om-outline.md`: generic fallback outline for products without a template
- `scripts/om_template_tool.py`: `inspect`, `prepare`, `check`
