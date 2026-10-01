# Screw Conveyors

## JMS calculator (Bio-SCREW, `\\JMS-CLT-FS01\JMS ENGINEERING\Bio-HANDLING Tools\Bio-SCREW`)
- Jun 2026 update:
  - corrected shaft shear-stress table (the old one oversized shafts)
  - hanger bearing selection renamed Hanger/Liner (choose a UHMW liner for shaftless)
  - lift HP factor changed from 1.3 to 1.7
  - thrust calculations added for bearing checks (separate Screw Conveyor Thrust Calculator)
  - Hardox liner option for grit shaftless screws
- The pneumatic actuator section of the older screw calculator is inaccurate and limited to cylinders under 4".
- **Conveyors Inc (CI) vs JMS HP (25018):**
  - CI incline efficiency factor R = 0.51 at 27° with 2/3-pitch flights, vs JMS 0.9.
  - CI uses 94% drive × 94% motor (88.4%), vs JMS 95%.
  - Incline factors are similar at full pitch but diverge strongly with special flights.
  - The old JMS calculator had a CI-style factor; the newer one dropped it, and alignment was pending.
  - **Treat the JMS incline factor with special flights as possibly unconservative until this is resolved.**

## Design rules
- Inclined screws ≤25° use full-pitch flights. [JMS std]
- Design to the HP quoted by the fabricator (TCC), not an oversized motor. [JMS std]
- Construction: 304 SS pipe and flights with hardened carbon-steel shafts. Coupling bolts are typically zinc plated. [JMS std]
- Shaft OD tolerance at bearings and reducer bores: -0.001/-0.004 in (current PE-team value; see drawing-check for history). [JMS std]
- Shaft material: SS316 has lower yield torque than CS1045. Check against motor max torque. [Lesson 24018]
- Runout: TCC/Martin standard TIR 0.015" over 6", accepted as the JMS standard when the spec is silent. [JMS std]
- Covers are hinged (a lift-off 2'x4' cover ≈50 lb is a fall/trip hazard). [JMS std]
- Slide gate opening = trough ID (a 12" screw → 13" square). [JMS std]
- Wear-indicating trough liners come from TCC/Martin. Curbell supplies UHMW.
- Use anti-seize on bolted trough section flanges. 25 bolts sheared on disassembly at 24018. [Lesson]
- Low-range speed sensors (e.g., TURCK BI20): drill and tap the trough bottom so the sensor presses on the liner close to the shaftless flights. New sensor types need new brackets.

## Shaftless verticals (Greg Hyde guidance) [JMS std / Judgment]
- Pull shaftless verticals: no lower bearing needed. This is preferred over shafted, whose bottom seals leak and kill bearings.
- Feeder and vertical are the same size. Size the feeder at 35–40% fill.
- Vertical rpm ≈ 1.4 × feeder rpm. Keep the feeder under 30 rpm so the vertical stays under 40 rpm; high rpm shears sludge to paste.
- Calculate spiral elongation under pull and compression under push.
- Alternatives:
  - PC pumps (vulnerable to trash)
  - piston pumps (robust but costly)
  - en masse drag (poor for wet sludge)

## Conveyor selection [JMS std]
- Screws handle wet to dry material, but not peanut-butter-sticky material.
- Tubular drag, en masse drag and bucket elevators are for dry or friable material (≈80% DS is OK, wet grit is OK, wet sludge is not). En masse is preferred for high volume or a steep incline.

## Bio-SCREW-PACTOR standard features (Mar 2026 markup, ref. Spirac Spiro-Press)
- Larger outer U-trough at the press head; spring-loaded hinge.
- Top cover: buy-out pull handle, SS weld hinges, two SS draw latches.
- Spray system: cone-pattern nozzles at ~40–60 psi; supply pipe sized for cumulative flow; solenoid + cut-off on an adjustable timer.
- Drainage: 3"–4" drain from the press head bottom to a lower drain box (rubber hose at trough breaks); lower drainage deck with a removable cover.
- Spiral and drum:
  - Carolina brush on the spiral OD
  - wedge wire flat side in, with generous outer bands
  - spiral-end-to-door gap 8"–9" max
  - drum ID level with the liner at 6 o'clock
  - hold-downs near the press head so the spiral can't lift

## Pump-fed live bottoms / seals
- Cinch-Seal shaft seals perform poorly under backpressure (21027 La Crosse leakage). Options: a packing gland or tail-end redesign, or newer units with replaceable internals. [Lesson]
