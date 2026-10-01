# Fab Check Checklist (Project Engineer pass)

## Title block and BOM
- [ ] Full part number format `proj-designator(+size)-type#` matches the SO/BOM/title block. Designator is correct for the product (BSC, BHP, BLB, BSG, BWG…).
- [ ] Revision and revision description are present. Revisions go through the revision process.
- [ ] BOM make/buy flags are correct. Cut-list parts flagged Purchased instead of Manufactured is a common error.
- [ ] Sheet-metal items called out by gauge (e.g., 11GA), not only by decimal.
- [ ] Hardware descriptions include grade and finish (e.g., A307 Gr A HDG; A563 Gr A HDG heavy hex nut; F1554 Gr36/55 HDG). Nuts and washers are not "A36". Nylon-insert lock nuts are ASME B18.16.6 zinc plated; washers USS/SAE/F436.
- [ ] Anchor rods specify stamping or tagging where the spec requires it.
- [ ] Purchased items (5xxxxx) exist as SolidWorks models and are CADLinked.

## Drawing standard (ASME Y14.5 + JMS)
- [ ] Weldment sheet 1 shows only weld-relative dimensions and weld callouts. Part details are on later sheets.
- [ ] Every weld callout has a size. Outsourced weldments need complete weld symbols.
- [ ] Hole dimensions to three decimals.
- [ ] Machined parts: no fractions, and decimals under 1" have a leading zero.
- [ ] Finish notes are in the NOTES section:
  - **Wedge gates:** "No. 4 polish (180 grit)" in NOTES (not in the part description).
  - Blast finish on SS hoppers (BU standard; not on live bottoms).
  - Pickling/passivation where the spec requires it.
- [ ] Routing is shown on every drawing and in SolidWorks metadata (PE accountable).

## Machined parts and shafts
- [ ] Drive/non-drive shaft OD tolerance at bearings and reducer bores = **-0.001 / -0.004 in** (current PE-team value, Sep 2026).
  - *History:* this value has changed several times (-0.001/-0.003 Jul 2026; +0.000/-0.0012 briefly Jun 2026; -0.002/-0.004 on older prints). Confirm there's no newer team decision before flagging.
- [ ] Shafts going to outside machine shops carry full tolerances. For locational clearance, h9 per Machinery's Handbook has been used.
- [ ] Retaining-ring grooves are toleranced. No carbon-steel retaining ring on a stainless shaft.
- [ ] Shaft material agrees with the calc. SS316 has a lower yield torque than CS1045.
- [ ] Hollow-shaft gearbox bore matches the shaft (e.g., SEW KA67 = 1.5"; KA77 min 1.75").

## Screw conveyors and live bottoms
- [ ] Hinged covers (1/4" steel hinge welded to 2x2x3/16 angle; 3/8"–1/2" handles), not lift-off.
- [ ] Slide gate opening = trough ID (a 12" screw → 13" square).
- [ ] Twin-screw live bottoms share one outlet slot (no divider).
- [ ] Anti-seize called out on bolted trough section flanges.
- [ ] Speed-sensor mounting (drill and tap trough bottom near the flights for shaftless) and bracket for the sensor type.
- [ ] Screw length and hole locations agree with the mating parts. TCC screws have arrived over-length before.

## Gates
- [ ] Blade thickness agrees with the calc. A 1" blade callout on 22067 was a copy-paste typo; the design was 5/8".
- [ ] Assembly notes where applicable: seal retaining bolts 50 in-lb in a cross pattern with anti-seize, no seal gap, roller guide bolts 280 in-lb with anti-seize.
- [ ] Actuator stroke ≈ opening + ~1" (pneumatic). ACME stem size agrees with the actuator selection.

## Hoppers, chutes, structures
- [ ] Vertical C-channel structural attachments carrying hopper load: 100% continuous welds. Horizontal shell stiffeners may be stitch welded.
- [ ] Standard hopper roof plate 1/4". Live-bottom connection L-angle 3/8".
- [ ] Chute plate seams split on a 45° line from the corner.
- [ ] Lifting lugs/ears on weldments of about 1,000 lb or more, with center of mass considered.
- [ ] Anchor size in the Hilti calc = BOM callout = support hole diameter. Concrete strength in the calc agrees with the site.
- [ ] Support spans not much over ~15 ft.
- [ ] Openings between bridged hoppers ≤2" (OSHA treats >2" as a hole to guard).
- [ ] Aluminum handrail P-loops ≥7" c-c. Welded aluminum is mill finish, then anodized.
- [ ] Tolerance/measurement callouts on large hoppers (e.g., leg height).

## Package handling
- [ ] Markups are all in one Bluebeam document or session.
- [ ] Package not moved or renamed.
- [ ] Checklist `JMS-DET-F-<proj>.xlsx` signed.
