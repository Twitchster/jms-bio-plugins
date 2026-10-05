# Filling the JMS O&M Starting-Point Templates

How the six templates in `templates/` work and how to fill them so the result matches what the JMS technical writer intended. Run `scripts/om_template_tool.py inspect <template>` for the full list of drafter notes. This file is the summary and the rules that apply across templates.

## Template inventory (Oct 2026)

| Product | File | Rev | Notes | Differences from the common structure |
|---|---|---|---|---|
| Bio-BELT | `Bio-BELT_OM_Rev1_Starting_Point.docx` | 1 | 127 | Belt Handling; Belt Tensioning and Belt Tracking; gravity/screw take-up options; plow, splice, alignment switch, V-belt and Dodge options. One template covers several belts: repeat the per-belt items with each tag |
| Bio-SCREW shafted | `Bio-SCREW_Shafted_OM_Rev0_Starting_Point.docx` | 0 | 44 | Hanger bearing options; assumes SEW gear reducer |
| Bio-SCREW shaftless | `Bio-SCREW_Shaftless_OM_Rev1_Starting_Point.docx` | 1 | 41 | Field-weld procedure for spiral joints; Liner Replacement Procedures; MFA 4P/MSP-12 calibration; hold-downs |
| Bio-HOPPER | `Bio-HOPPER_OM_Rev0_Starting_Point.docx` | 0 | 123 | Always a live bottom; leveling screw, load discs, gates, chutes, access and pump loadout options; three shutdown cases (empty, material in hopper, alarm) |
| Bio-GATE | `Bio-GATE_OM_Rev0_Starting_Point.docx` | 0 | 27 | Electric actuator basis; Seal Replacement; storage asks to move the gate every 2 weeks; no anchor text; Startup and Shutdown only |
| Bio-DIVERTER | `Bio-DIVERTER_OM_Rev0_Starting_Point.docx` | 0 | 49 | **Inputs page** at the end with content controls feeding REF fields; Appendix A is "Supplemental Vendor Information", E is "Controls Information", plus **Appendix H: Comment & Response Log Template**; Clarifications section; Component Naming Conventions with dual vs multiple drop-point figures; odd-page section breaks; no anchors |

**Common structure:** cover (product, tag/serial/customer number, plant name, location, specification section, Engineer of Record, revision, month and year); Contact Information; 1 Scope of Supply (Equipment Data, Special Tools, Field Service, Scope Exclusions, Spare Parts); 2 Safety Precautions (Equipment-Specific Safety in belt, screws and hopper); 3 Delivery, Handling and Storage; 4 Installation Instructions; 5 Operating Procedures; 6 Maintenance, Lubrication and Troubleshooting; 7 Policies (Warranty, Liability, Returns, Delivery, Thread Lubricant, Standard Erecting Practices); Appendices A Catalog Cuts, B Equipment Drawings, C Calculations, D Startup Reports, E Controls, F O&M Revision History.

**Header:** "Location: XXXX" and "JMS Project No.: XXXX". **Footer:** equipment name, "Specification Section: XX XX XX", and "Document Prepared By: XX" (PE initials).

## Conventions in the templates

- **Yellow highlight = fill-in or choice.** When filled or decided, remove the highlight. Text that stays as written is not highlighted.
- **Square brackets = optional text or alternatives**, e.g. `[slide][knife]`, `[Grout beneath the supports ...]`. Keep the right one, delete the rest and the brackets. Each choice has a drafter comment that says when it applies.
- **Comments by R. Nesman = drafter/reviewer notes.** None go to the customer. Some comments are only screenshots (empty text) that illustrate the note before them.
- **"INSERT ..." and X strings** (XXXX, xxxxx, "X (Number) X (description from scope)") are placeholders for project text.
- **Cross-references and captions are Word fields** (REF, SEQ Figure, TOC, PAGEREF). Deleting options changes numbering. Step references written as text, such as the hopper's "3.c. and 3.e.", must be fixed by hand.

## Fill procedure

1. **Inspect** the template (`inspect --json`) and keep the output; it is the drafting instruction set. If the user supplies a newer template revision, inspect that one instead and note any changed notes.
2. **Settle the configuration facts** (`om-required-documents.md`, last section) from the documents. Show the user each fact, the option it selects and the evidence. Get a confirmation before drafting.
3. **Prepare the working copy**: `prepare <template> <PROJ-PRODUCT_OM_REVX>.docx`. This removes all template comments and makes Word offer a field update on open.
4. **Edit the XML** following the `docx` skill's "Editing existing documents" method: unzip, `merge_runs.py`, edit `word/document.xml` in place without reformatting, rezip, `validate.py --original`. Keep the template's styles, numbering, images and section breaks. Never rebuild the document from scratch.
   - Fill every highlighted field and remove its highlight.
   - Resolve every bracket set by its note's condition. Delete unused figures with their captions, and unused table rows.
   - Write Scope of Supply, Field Service, Exclusions, Clarifications and Spare Parts from the approved submittal and the GA spare-parts table. Keep the template's sentences around them ("Additional service trips ...").
   - Remove all "cross-contamination" text when the equipment is mostly carbon steel; keep it for stainless.
   - Fix hand-typed step references after deleting options.
5. **Mark what's still open with comments** (the `docx` skill's `comment.py`), never in body text: "OPEN – <item> – needs <document> from <owner>", "ASSUMPTION – ...", "PLACEHOLDER – ...". An unresolved field may stay highlighted only if it carries an OPEN comment.
6. **Appendices.** Build a list of every appendix item with its source file: App A cat cuts and supplemental vendor information; App B GA/SA/FA sheets at numerical revision; App C current calcs; App D placeholder page; App E controls or a statement that JMS supplied none; App F revision row; App H (Diverter) blank comment & response log. The PDF assembly is done by the PE; list it, don't invent content for it.
7. **Revision history (App F):** date MM/DD/YYYY, revision (0 for first release), "Initial release." and the PE's initials. Add a row for every external revision.
8. **Check:** run `check <file>` and fix every item it reports except intentional OPEN placeholders. Render to PDF (`docx` skill) and look at the cover, a scope page, the lubrication section and the last page.
9. **Hand-off note to the PE:** open in Word, accept the field update (or Ctrl+A, F9, then repeat inside the header and footer), then search for "Error" to catch broken cross-references. The Table of Figures can be deleted if no figures remain.

## SEW lubrication block (belt, screws, hopper)

Template text was taken from the SEW manual released 02/2023. Use the current manual if there is a newer one.

1. **Mounting position** from the SEW quote. Put the current SEW catalog diagram for that position under the legend, replacing "[INSERT PIC OF MOUNTING POSITION FROM SEW MANUAL]", and write the position in the text.
2. **Oil quantity** from the SEW quote (per unit; hopper live bottom and leveling screws may differ).
3. **Oil type:** keep the template text that tells the user to use the oil on the nameplate. SEW advises against mixing brands, even of the same oil type; an unlisted oil is SEW brand, and switching brands needs a flush.
4. **Closing plug thread size** from "FOR REFERENCE - SEW Closing Plugs.pdf" using the unit's model. Mark that row in the template table with a red box.
5. **Plug tightening torque** for that thread from the current SEW manual table ("tightening torques for oil level plugs, oil drain plugs ..."), written as "xx lb-ft (xx Nm)". 1 N·m = 0.7376 lb-ft; round sensibly and compute it in code.
6. **Motor bearings:** keep "The motor bearings are sealed for life ..." only for an SEW or explosion-proof motor. For SEW, confirm the quote notes the bearing shield removed / oil added. If the note is missing, flag it for the drives contacts named in the template (Philip and Andy).
7. **Motor regreasing rows** only for a non-SEW, non-explosion-proof motor (check the Baldor frame for XP plus Class II Div 1; VECP is not XP). Fill interval, quantity and grease from the motor maker's data in App A.
8. **Break-in oil change** (about 500 h) only if Engineering asks for it.
9. **Breather valve protective band** paragraph is SEW-specific. Remove or reword it for other reducers.
10. **Non-SEW reducer:** remove every "SEW" reference, and use the actual reducer's maintenance, lubrication and troubleshooting data.

## Bearing defaults

The roller bearing row (every 3 months, until grease purges, NLGI #2 lithium complex) comes from Dodge Type E and S-2000 bearings. Use it only after confirming the bearing type; otherwise use the actual bearing maker's data. Diverter and gate bearings usually need data from Engineering (send the BOM line item).

## Per-template notes worth knowing

- **Bio-DIVERTER:** fill the **inputs page first** (last page: content controls for project no., location, tag, plant, spec no., EoR, customer, O&M rev and date, Prepared By, local rep name/company/address/phone, PM). Fill the content controls in the XML, and also update the cached text of each REF field result that points to them (bookmarks JMSPROJECTNO, LOCATION, TAGNO, PLANTNAME, SPECNO, ENGINEEROFRECORD, CUSTOMER, OMREVNO, OMRELEASEDATE), so the document reads right before Word refreshes fields. Don't delete the bookmarks or content controls. The cover-page "ver" bookmark text is white on purpose. Delete the inputs page only in the PDF version. Blank pages between sections come from odd-page section breaks; don't remove them.
- **Bio-DIVERTER storage** intentionally omits the "rotate rotating parts" bullet (partial-turn equipment). The gear unit storage paragraph was removed; add it back from another template only if a gear unit is supplied.
- **Bio-GATE** storage keeps "move the gate every 2 weeks". If the gate belongs to larger JMS equipment, reference that O&M's scope and field service rather than repeating them.
- **Bio-HOPPER:** a JMS Bio-GATE at the discharge gets the separate Bio-GATE O&M. The hopper text then references it in installation, startup and all three shutdown cases. Knife gates reference App A instead.
- **Bio-SCREW shaftless:** liner replacement uses the ¼" wear limit and UHMW preformed "U" liners; check both against the drawings.
- **Bio-BELT:** the gravity take-up text was written before that design was final; review it against the current drawings. Belt roll handling doesn't apply to sidewall belts.
