# Structural, Seismic, Anchorage

## Responsibilities
- JMS Bio PEs write their own RISA-3D structural reports. Element 30 (James Gerloff PE SE) reviews and stamps them after customer approval.
- Before sending a report for stamp, confirm the code edition matches the contract (IBC 2021 vs 2018 has been caught at stamp).
- JMS does not do concrete design.

## Seismic
- SDC B: nonstructural components are exempt per ASCE 7 Ch 13. Label them exempt. Seismic design is required only for SDC C and above.
- Ie = 1.5 requires Risk Category IV (Ie = 1.25 = Cat III).
- ASD/LRFD combinations come from IBC/ASCE 7 and vary slightly by edition. Start from a template with all combinations and delete the ones that don't apply.
- **Belt conveyors:** belt tension live loads on the drive and tail pulleys must NOT be copied into seismic ELX/ELZ load cases.
- Some projects are exempt by contract or SDC (e.g., 25003 belts). Confirm per project; don't generalize.

## Loads
- Stairs and platforms: 100 psf live load. Hopper roofs: 100 psf typical (250 psf has been successfully challenged).
- Support spans much over ~15 ft exceed spec/JMS practice; relocate supports instead.
- Wind on silo supports: check the empty-silo case (overturning/uplift).

## Anchors
- Hilti PROFIS calcs:
  - Check that the written report and PROFIS utilization agree.
  - Hilti calc size, BOM callout and support hole diameter must agree.
  - Concrete strength assumed in the calc must match the site. [Lesson 24018: calc 3/4", BOM 5/8", holes 3/4", 3,000 vs 4,000 psi → rework to 1" anchors]
- 316 SS: KWIK BOLT TZ2 is the only 316 SS mechanical anchor strong enough for heavy loads. Hilti offers no 1" mechanical anchor in 316 SS.
- Masonry (24047 lesson):
  - Hollow or non-grouted CMU cuts capacity drastically (~260 lb for one eccentric anchor).
  - Grout-filled CMU works.
  - In hollow units use Hilti screens + HIT-270 epoxy, or add a column so the wall connection is nominal.
  - RFI the wall construction early.
- Anchor rods: commonly A36 zinc-coated with grade 2 zinc nuts and washers, or F1554 per spec. State the rod grade on RFQs. Anchor rods must be stamped or tagged per typical spec. For cast-in anchors, check length (embed + sleeve + grout + plate + nut) and alignment for load cells.

## Lifting lugs
- Use the Engineering-drive lifting-lug calculator (e.g., 20,000 lb at SF 1.35).
- Add defined lifting provisions to major weldments (~1,000 lb+), considering center of mass.

## Stairs, rails, grating, ladders
- Grating: 15-W-2 is often non-stock; 19-W-4 is easier to get.
- Aluminum handrail: minimum P-loop 7" c-c. Welded aluminum is mill finish, then anodized.
- OSHA fixed ladders (since 2018): cages and platforms are not required with a proper ladder fall-arrest system, up to 150 ft.
- Specs often require HDG stairs per 05 50 00, with aluminum allowed only where stated.

## RISA model review checklist
- [ ] Units, code edition, and design method (ASD/LRFD) agree with the report text.
- [ ] Load cases: dead, live, material, wind, seismic (if SDC ≥ C), belt tension (not in seismic).
- [ ] Boundary conditions: pins vs fixed at base plates, roller/guide positions.
- [ ] Member sizes, materials and connection assumptions match the drawings and BOM.
- [ ] Deflection limits stated and met; governing utilization reported.
- [ ] Anchor reactions carried into the Hilti calc with matching sizes and concrete strength.
