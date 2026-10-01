# Slide and Wedge Gates

## Policy (Bio-HANDLING engineering, Jul 2026)
- JMS screw-conveyor slide/wedge gates are unique designs. They are not AWWA C561 sluice gates and are not designed to SS slide gate spec 40 05 59.35 beyond materials. Never imply compliance with leakage specs.
- No gate manufacturer recommends horizontal installation.
- Where the spec has no rating, use a minimum baseline shop test of 2–3 psi. Some jobs carried 10 psi (10 psi ≈ 23.1 ft of water).
- Gates are open/close only. Control the discharge rate with screw speed.
- After the 22067 Portland blade deflection failure, gate designs are to be more conservative.

## Blade load basis — read before calculating
- **Current position:** use the full design material head from the hopper or silo design. On 22067 this was H = 40 ft, used in the Sep 2026 actuator-thrust calc for EoR review.
- **History and conflict:**
  - The Jul 2026 22067 letters used a Jenike effective head (Bulletin 123, 1970) of 2.55–3.4 ft.
  - The EoR (Jacobs) fully disagreed with the effective-head approach.
  - In Sep 2026 those calcs were judged incorrect.
  - Some internal notes still describe the "Jenike method" as the blade load basis. Treat that as superseded unless the PE confirms otherwise.
- Initial-fill outlet loads can be 2–4× the effective-head value until fill reaches ≈1.5× silo diameter (Solids Handling Technologies).
- Discharge gate loading also depends on control philosophy (screw speed vs gate position vs load-cell logic).

## Plate checks
- Plate deflection method used: Milan Batista rectangular plate solution in a spreadsheet. A 6" partial opening failed L/360 in one check. Screw rpm doesn't affect blade deflection, because pressure comes from static head.
- Also check:
  - blade stress at first yield
  - roller loads (rated load from the datasheet, e.g., 7,700 lb on 22067)
  - roller positioning in the boundary conditions (a Jacobs comment on 22067)
  - worst-case blade position just off the first rollers
- 22067 reference values (3/4" × 24" × 54" blade): could deflect 0.868" before first yield. Permanent-deflection limit 0.39" at the leading edge. Operating monitoring limit ≤0.31" (≈1/3 SF). The fix was stiffeners under the blade plus 55" stiffening angles (6 per gate).
- Verify the blade thickness callout against the calc. A 1" typo on 22067 came from a copied drawing; the design was 5/8".

## Actuation
- Electric: Rotork IQ series with ACME stems (e.g., IQ10, non-rising stem, 1-1/8"-4 ACME). Larger gates need a bigger ACME rod and a longer open time (25"x25" → 1-1/8" rod, ~65 s).
- Pneumatic (AFP Industries package):
  - NFPA cylinder, tie rods extended, stainless cylinder fasteners
  - 110 VAC solenoid, regulator + filter, flow controls, tubing, canister mufflers
  - plant air ~80 psi; stroke ≈ opening + ~1"
  - get SCFM (e.g., 2.66–3.32 SCFM for an 8–10 s stroke at 80 psi) and the cylinder cut sheet
- Don't use the old JMS screw calculator's pneumatic section for cylinders ≥4".

## Fabrication and assembly
- Wedge gates: note "No. 4 polish (180 grit)" in the NOTES section to help sealing.
- Assembly:
  - seal retaining bolts 50 in-lb, stepped, cross pattern, anti-seize
  - neoprene seal in direct contact with the blade (no gap) when closed
  - roller guide bolts 280 in-lb with anti-seize
- Custom gate seals: Cardinal Rubber.
