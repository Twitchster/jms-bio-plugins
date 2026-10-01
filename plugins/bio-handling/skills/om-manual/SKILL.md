---
name: om-manual
description: >
  This skill should be used when a JMS Bio-HANDLING engineer asks to "draft the O&M", "write the
  operation and maintenance manual", "put together the O&M for the hopper / silo / screw / belt",
  "fill out the 01 33 00 closeout forms", "equipment maintenance summary forms", "maintenance
  requirements form", "spare parts list for the O&M", or needs closeout documentation for JMS equipment.
metadata:
  version: "0.5.0"
---

# O&M Manual Drafting

Draft the initial Operation & Maintenance manual for JMS Bio-HANDLING equipment. The Project Engineer drafts it, and the target is to submit 2 weeks before equipment delivery, before Status 4.0 (Initial Shipment). Load `jms-bio-conventions` for naming and folders.

## Sources, in order of authority

1. **The approved submittal** for the equipment (e.g., "AS - <proj> - <spec section>"). When the O&M draft, a vendor manual or a spare parts list disagrees with the approved submittal, use the approved submittal data.
2. The spec section's O&M requirements, plus 01 33 00 / 01 78 xx closeout requirements.
3. Vendor O&M manuals, cutsheets, lubrication charts and spare parts lists for purchased components (SEW, Baldor, TCC/Martin, Rotork, AFP, Vortex, Kistler, sensors, panels).
4. JMS drawings: GA, assemblies, BOM, and the as-built sales BOM from `07 Shop & Field Docs`.
5. A prior JMS O&M for the same product, used as the template.

**Ask for a prior JMS O&M first.** It sets the section order, cover page, revision block and boilerplate. Search SharePoint and Outlook for "O&M" plus the product name if the connector is available. Without one, use the default outline in `references/om-outline.md` and say that it is a default, not the JMS template.

When source data is missing or conflicting, **ask** rather than assume. Record every open item in an "Open Items" list at the front of the draft.

## Procedure

1. Build the equipment list: tag numbers, descriptions, P/Ns, quantities, and vendor + model for every purchased component.
2. Confirm vendor identity against the approved submittal. Vendor spare-parts lists have named the wrong manufacturer before (e.g., a fan vendor different from the blower actually supplied).
3. Draft each section per the outline. Put operating limits (gate open/close only, fill limits, rpm limits, startup/shutdown sequences) in Operation, with the basis stated.
4. Build maintenance tables from vendor intervals: task, interval, lubricant/part, quantity, reference.
5. Build the spare parts list from the approved submittal and the vendor recommendations.
6. If the spec requires closeout forms (Equipment Maintenance Summary, Maintenance Requirements), fill one per equipment item or motor as required. Bookmark them as appendices.
7. Assemble vendor documents as bookmarked appendices. Use English cutsheets and nameplates.
8. Set "Prepared By" to the drafting PE's initials. Ask for them; don't assume. File name: `PROJ-PRODUCT_OM_REVX`.

## Output

- A draft in the format requested (Word .docx by default for an editable O&M). Include a bookmarked-PDF assembly plan listing each appendix and its source file.
- An Open Items list with owner (PE / vendor / PM).
- A check table: every equipment tag in the approved submittal appears in the O&M and the maintenance tables.

## Missing information

Follow the `source-documents` skill for every gap. The usual sources:
- approved submittal: equipment data and tags
- vendor O&M manuals: lubrication and intervals
- 01 78 23 / 01 33 00: required contents and forms
- Sales BOM in `07 Shop & Field Docs`: as-shipped configuration

Ask for the specific file and section rather than a general request.

## Verification

Cross-check every tag, model number, lubricant, quantity and interval against its source document. Mark anything that couldn't be verified.
