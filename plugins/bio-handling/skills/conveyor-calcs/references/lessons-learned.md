# Lessons Learned — First Runs (Oct 2026)

Technical findings from the first two runs of the workflow:
- Bio-BELT REV 4.7: CLCWA screenings belt, Spec 46 21 73 para 2.6
- Screw REV 21: 25026 SSC-1 shaftless screenings screw, Spec 41 12 13.36 + 40 05 93

Each item is tagged [Spec], [Template], [Judgment] or [ASB decision]. Treat project numbers as examples only.

## Both calculators
- **Spec markups are inputs.** [Spec] The spec PDF carried JMS reviewers' sticky notes and a red "4 ply" markup that conflicted with the printed text. Extract annotations before filling, and list every conflict.
- **Drawings may come later.** [Judgment] Lift and incline drive power more than length. A guessed lift is the riskiest placeholder; use the spec's maximum allowed and flag the results as provisional. When drawings arrive, report the update as a diff: inputs changed, results moved, and whether the gearmotor still works.
- **Engineer overrides stay tagged.** [Judgment] Example: belt width 30 in and density 65 lb/ft³ "per ASB", when the spec minimum was 24 in and the spec gave no density. The record must show they weren't from the spec.
- **LibreOffice recalculation is good for the main numbers.** [Template] In the worked examples, rebuilt sheets matched the originals on every pass/fail output. The exception is XLOOKUP part-number cells (#NAME? in LibreOffice); Excel computes them on open.

## Bio-BELT (REV 4.7)
- **Capacity tie.** [Judgment] Write the volumetric input M20 as `=<tph>*2000/AP10` so the mass capacity always equals the spec value whatever density is entered. Density then only changes volume and skirt load depth.
- **Skirtboards dominate effective tension.** [Template] With full-length skirts (no drawings), skirt friction was about 52–56% of Te. Shorten to the actual skirt length as soon as drawings show it.
- **Drive shaft: check the spec method, not just the sheet.** [Spec] One spec used combined shock/fatigue factor 1.5 on bending and torsion, max combined shear 6,000 psi, at motor nameplate torque.
  - 1-15/16 in passed the sheet method but failed the spec method (about 7,100 psi).
  - 2-7/16 in passed (about 3,600 psi).
  - Sizing on calculated running torque instead would pass 1-15/16. Whether the spec wording ("loads imposed by the conveyor operation") allows that is the engineer's call; ask.
  - **The shaft size sets the SEW hollow bore and frame.** Decide it before step 4.
- **Selected drum rpm (P58) comes from the SEW selection.** [Template] Until it's entered, pulley bearing L10 (P93) shows #DIV/0! and idler rpm shows 0. Gearbox weight (AM34) adds overhung moment; enter it at close-out and re-check the shaft and bearings.
- **Common spec contradictions** [Spec], to list in the conflicts:
  - "flat" idlers in one line and 20° troughing in the next
  - crowned pulleys with a sidewall belt
  - belt ply count vs reviewer markup
  - vulcanized splice vs lacing kits in the spare parts
  - "10"-0"" return idler spacing (likely 10'-0")
- **TEFC motor vs NEMA 7 sensors.** [Spec] A TEFC motor clause alongside NEMA 7 pull cords and sensors signals an area-classification question. It doesn't block the SEW motor selection (SEW sources the motor to the stated classification), but it does block the JMS sensor and switch selection.

## Screw (REV 21)
- **REV 21 is current.** [Template] Jun 2026: lift HP factor 1.7, corrected shaft shear, thrust calculations. Older calcs need re-running.
- **Density and solids defaults are formulas.** [Template] AP11 and AP12 (`=Reference!CB1/CC1`) pull from the material table. When the spec states density or solids, overwrite them with `--allow-formula AP11 AP12` and comment the source.
- **Spiral torsion: the sheet checks 1.0 Fy; specs may require far less.** [Spec] Spec 41 12 13.36 required spiral stress ≤ 0.3 Fy at 2.5× motor nameplate torque. Check it by hand from the sheet's spiral stress (T127) scaled to the spec basis.
  - Motor torque rises as speed falls, so this sets a **minimum gearbox output speed**. Example: 21.9 rpm with a single 1×3 in spiral and a 3 HP motor.
  - Fixes are a higher speed (more wear) or a dual spiral, which cut stress about 57%. Example: the minimum fell to 9.4 rpm, and ASB chose 10 rpm at 8% fill.
  - Always send SEW the floor, e.g. "not below 9.4 rpm", not just the target.
- **Thrust rises as speed drops.** [Template] Push-type incline at 15°: 1,540 lbf at 24 rpm, 4,599 lbf at 10 rpm. It goes to SEW for the gearbox bearing L10 (the spec asked for 100,000 h).
- **Shaftless screws and checks that don't apply.** [Template] The sheet's trough thermal-expansion check can show FAIL for a shaftless screw; it applies to shafted screws only. Say so in the doc rather than "fixing" it.
- **Zero-speed sensors on shaftless screws.** [Spec] Specs often say "tail pulley shaft", which a shaftless screw doesn't have. Sense the drive shaft or flange.
  - The MSP 12 is NEMA 4X only; the XPP-5 was ATEX-only on another job.
  - In a classified area, take an exception or confirm the sensor location is unclassified.
- **Drive-shaft material lists.** [Template] 4150 HT isn't in the sheet list. 4140 Alloy (same 21 ksi allowable as 1045 in the sheet) is the conservative stand-in, and ASB took an exception to 4150.
- **Gear-rating clauses can contradict.** [Spec] One spec required gear rating ≥ 1.5× calculated torque in one clause, and "rated output torque must not exceed motor nameplate torque" in another. Clarify the second as "not less than", and design to JMS 1.4 on nameplate.

## SEW step (both)
- **Pick by margin, not just the smallest unit.** [Judgment] An FA87 at 9.8 rpm technically passed but sat at exactly fB 1.4 and 96% spiral use, with an unverified bore. The FA97 (i = 174.87, 10.08 rpm, fB 2.10, 2.938 in bore) was selected. Mention the cheaper alternative in the SEW request.
- **Deviations seen.** [Template]
  - With inverter operation ticked, the configurator stops offering the standard motor oil seal (FKM remains).
  - An oil sight glass is added when the spec requires oil-level indicators.
  - Mounting position and pivot angle (e.g., a 15° incline) change the oil quantity; set them from the drawings.
