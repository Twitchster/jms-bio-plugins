# Calc Sheet → Drive Selection Field Map

The JMS calculators (Bio-SCREW, Screw Conveyor Thrust Calculator, Bio-LIVEBOTTOM, belt conveyor calcs) live in `\\JMS-CLT-FS01\JMS ENGINEERING\Bio-HANDLING Tools`. Their cell layouts are not recorded in this plugin yet. Locate each value by its label, using `scripts/extract_calc_values.py`, and confirm the mapping with the user on first use of a calculator version.

## Fields to find

| Needed for SEW | Likely calc labels (search terms) | Used for | Required? |
|---|---|---|---|
| Design shaft power [HP] | "total HP", "design HP", "required HP", "HP at shaft", "motor HP" | Search: motor power; torque calc | Yes |
| Selected motor HP | "motor HP", "selected motor", "use" | Search: motor power | Yes |
| Screw / pulley speed [rpm] | "RPM", "screw speed", "operating speed", "N" | Search: output speed | Yes |
| Speed range (VFD) | "min RPM", "max RPM", "turndown" | Torque at low speed; VFD checkbox | If VFD |
| Torque [lb-in or ft-lb] | "torque", "shaft torque", "full-load torque" | Check vs Ma | If given (else compute 63,025·HP/rpm) |
| Service factor | "SF", "service factor", "AGMA class" | Search: fB | Spec or JMS min 1.4 |
| Drive shaft diameter [in] | "shaft dia", "drive shaft", "shaft size" | Variants: hollow bore | Yes (hollow shaft) |
| Axial thrust [lb] | "thrust", "axial load" (Thrust Calculator) | SEW confirmation (site gives no axial capacity) | Yes for inclined/vertical or high-thrust |
| Overhung load [lb] | "OHL", "overhung", "radial load" | Check vs permitted FRa | If chain/belt drive or side load |
| Incline [deg] | "incline", "angle" | Mounting/pivot, oil fill, context | Yes for screws |
| Material, capacity, fill | "capacity", "% fill", "density" | Re-check capacity if actual rpm differs | Context |
| Operating hours per day / starts per day | "hours", "hrs/day", "starts", "cycles" | Duration factor (S1-100% if ≥8 h/day) | If available; else from spec |
| Calculator version/date | title block, revision cell, "rev", file date | Flag pre-Jun 2026 Bio-SCREW calcs | Yes |

## Rules

- Use the calculator's final or selected values, not intermediate scratch cells. If two cells could be the design HP, show both and ask.
- Convert units explicitly (ft-lb × 12 = lb-in; kW × 1.341 = HP) and show the conversion.
- After the user confirms a mapping for a calculator version, record the sheet/cell map in the output file's Inputs section so the next run can reuse it. Suggest adding it to this file in the next plugin update.
