# Bio-BELT Calculator-Estimate Template REV 4.7 (Revision sheet: 4) — Design sheet cell map

Generated from the blank template with `scripts/inspect_template.py`, using the template's own color legend (yellow FFFFCC = primary input, blue D9E1F2 = secondary input). Only Design-sheet inputs are filled; the other sheets are never written.

**Worked-example notes** come from the first JMS run of this workflow (CLCWA screenings belt conveyor (Spec 46 21 73 para 2.6), Oct 2026). They show what each input meant in practice and where its value came from. They are examples, not defaults: re-derive every value from the current project's documents.

**Revision check:** at intake, run `inspect_template.py` on the template being used. If the Revision-sheet number or the input list differs from this file, stop and rebuild the map before filling. A changed layout would put values in the wrong cells without any error.

## Inputs

| Cell (span) | Label | Class | Template value | Dropdown source | Worked-example note |
|---|---|---|---|---|---|
| U4 | PROJECT NO.: | primary |  |  | Source: spec footer – this is the Engineer's project no. (W09-2401462). Replace with the JMS project no. when assigned. |
| AK4 | BY: | primary |  |  |  |
| U5 | LOCATION: | primary |  |  | Source: spec footer 'CLCWA WWRF New Headworks Design'. City/state not given in Section 46 21 73. |
| AK5 | DATE: | primary |  |  |  |
| U6 | CUSTOMER: | primary |  |  | OPEN: customer (GC) not identified in the spec. Fill from bid docs / PO. |
| AK6 | REVISION: | primary |  |  | Rev A = first issue (preliminary, spec only). Change if JMS uses a different convention. |
| U7 | ENGINEER: | primary |  |  | OPEN: Engineer of Record firm not named in Section 46 21 73 (check spec cover / Div 01). |
| AK7 | REV DATE: | primary |  |  |  |
| U8 | DESCRIPTION: | primary |  |  | Section 46 21 73 'Mechanical Screens (Multi-Rake Screens)' – belt conveyor is para 2.6. File used: Addendum 2 copy with internal markups (G. Hyde 4/17/26, J. Morrison 4/20/26). Belt Conveyor Motor Data Sheet supplement (3.6.A.2) i… |
| AK8 | PAGE: | primary |  |  |  |
| AN8 | OF | primary |  |  |  |
| P10 | IDENTIFICATION: | primary |  |  | OPEN: equipment tag TBD - not in the spec – take from P&IDs / equipment schedule. |
| AP10 | DENSITY: | primary |  |  | 65 lb/ft3 per ASB direction (10/1/26) – the spec gives no density. Material is raw, unwashed 6 mm screenings (washer/compactor deleted, 2.7). Power is set by the 6 tph mass because M20 is tied to it; density only changes volume (1… |
| AP11 | SOLIDS CONTENT: | primary |  |  | Not in spec. Feeds the Data Sheet only – fill if the screen supplier provides it. |
| P12 | JMS ASSEMBLY: | primary |  |  | Assigned at order entry. |
| AP12 | NOTES: | primary |  |  | PRELIMINARY - spec only, no drawings. Inputs come only from Section 46 21 73 para 2.6 (Addendum 2). Length/incline, skirt length, supports and impact zones are placeholders. Every input carries a comment with its source, assumptio… |
| P14 | DRIVE ARRANGEMENT: | primary |  |  | Spec 2.6.C.5.d: drive motor direct-connected to a shaft-mounted helical gearmotor at the conveyor head shaft. Drive efficiency 0.95 (List tab). |
| P15 | SERVICE DUTY: | primary |  |  | ASSUMPTION – spec silent. Belt runs whenever any screen runs plus an adjustable overrun (2.9.H.2); screens run on differential level/timer and continuously in storm mode. 'Standard' chosen; feeds Data Sheet only. |
| P16 | AREA CLASSIFICATION: | primary |  |  | OPEN – BLOCKING for motor and sensor selection. Spec conflict: belt motor is 'TEFC' (2.6.C.5.b, not explosion-proof) but pull cords and zero-speed sensor are NEMA 7 (2.6.C.15/16 = Class I hazardous). Screen motors are Class 1 Div … |
| P17 | CONVEYED MATERIAL: | primary |  |  | Spec 2.6.A.2: receives screenings from all three 6 mm (1/4 in) multi-rake screens simultaneously and conveys to a disposal container. Washer/compactor removed (2.7), so screenings are wet and unwashed. |
| AM19 | SKIRTBOARD LENGTH: | primary |  |  | PLACEHOLDER – skirtboards are required (2.6.C.13: 3/8 in HDPE, 304 SS brackets) but length is not given. Full 40 ft used (conservative; three load points). Skirt friction = 240 lb = ~52% of Te, so this input governs HP. Shorten to… |
| M20 | DESIGN VOLUME LOADING: | primary |  |  | Formula = 6 wet tons/hr (2.6.C.1) x 2000 / density (AP10), so M19 always equals the spec 6 tph. G. Hyde markup on the 6 tph line says 'Confirm' – verify basis with the EoR (non-blocking: belt is at ~16% of volume capacity). |
| AM20:AO20 | SKIRTBOARD FRICTION FACTOR: | secondary | 0.14 |  |  |
| M21 | SPEED: | primary |  |  | Spec 2.6.C.5.d: 100 FPM final belt speed. |
| AM21 | QUANTITY OF PLOWS: | primary |  |  | No plows in spec – discharge over the head pulley to the container. |
| AM22 | QUANTITY OF SCRAPERS: | primary |  |  | Spec 2.6.C.11: one doctor-style urethane wiper at the discharge pulley. |
| M23 | BELT WIDTH: | primary |  |  | 30 in per ASB direction (10/1/26); spec 2.6.C.4.a minimum is 24 in, so 30 in complies. Pulleys 2 in wider than belt (2.6.C.8.a) = 32 in face, matches the pulley PN formula. Bearing centers become 38 in (AU61). |
| AM23 | WASH BOX: | primary |  |  | No wash box in spec. |
| M24 | HORIZONTAL LENGTH: | primary |  |  | PLACEHOLDER (no drawings) – see M25. |
| AM24 | BELT SCALE: | primary |  |  | No belt scale in spec. |
| M25 | MINIMUM INCLINE LENGTH: | primary |  |  | PLACEHOLDER – no drawings. Spec 2.6.C.2/3: 40'-0" centerline length, 20 deg MAX incline. Modeled as the bounding case: full 40 ft at 20 deg (Type 2), lift 13.7 ft. Real layout (likely a horizontal load section under the 3 screens,… |
| AM25 | TYPE OF PLOW: | primary |  |  | No plows. |
| M26 | INCLINE ANGLE: | primary |  |  | Spec 2.6.C.3.a: maximum 20 deg (bounding value). [Judgment] 20 deg is steep for wet screenings on a plain sidewall belt (rollback); cleats may be needed if the final incline approaches 20 deg. |
| M27 | BELT LOAD RATING: | primary |  |  | Spec 2.6.C.4.a: rated tension 220 PIW. Calc T1 = 838 lb = ~28 PIW on 30 in (~13% of rating). G. Hyde markup circles '2-ply' and writes '4 ply' – resolve belt construction (sidewall base belt) with the belt supplier; not material t… |
| M28 | BELT THICKNESS: | primary |  |  | Spec 2.6.C.4.a: 2-ply synthetic carcass, 1/8 in top x 1/16 in bottom covers – ~5/16 in overall assumed (JMS standard 0.3125). Confirm with the belt cut sheet (thicker if 4-ply). |
| AM28 | TYPE OF TAKE UP: | primary |  |  | Spec 2.6.C.6.b: protected screw take-ups at the tail, SS adjusting rods. Spec min travel = 1% of belt length (~83 ft belt = ~10 in); sheet selects 12 in (AV28) – OK. |
| M29 | BELT TYPE | primary |  |  | Synthetic (fabric) carcass per 2.6.C.4.a. |
| AM29 | LAGGING ON HEAD PULLEY?: | primary |  |  | Spec 2.6.C.8.a: drive pulley lagged with 1/4 in min plain vulcanized rubber. Spec says 'tail-end drive pulley' – ambiguous; the drive is at the head (2.6.C.5.d), so read as head/drive pulley only. |
| AM30 | LAGGING THICKNESS: | primary |  | "N/A,.25,.375,.5" | Spec min 1/4 in; 3/8 in (JMS common) used – meets the minimum. Use .25 if plain lagging is only offered at 1/4 in. |
| M31 | CARRYING IDLER TYPE: | primary |  | "FLAT,TROUGHING" | SPEC CONFLICT: 2.6.C.9.a says 'all idlers flat type'; 2.6.C.9.b says carry idlers '20 degree troughing'. Belt has raised sides (2.6.C.4.c). G. Hyde markup: 'Flat on sidewall'. Modeled FLAT / 0 deg to match a sidewall belt. This al… |
| AM31 | DRIVE PULLEY SHAFT SIZE: | primary |  |  | Spec 2.6.C.7: shaft min 1-15/16 in; combined shock/fatigue factor 1.5 on bending and torsion; max combined shear 6,000 psi; drive shafts keyed. Sheet method alone passes 1-15/16 (D req'd 1.53 in). Spec method at motor nameplate to… |
| M32 | CARRYING IDLER TROUGH  ANGLE: | primary |  |  | 0 deg – flat idlers for the sidewall belt (see M31). |
| AM32 | TAIL PULLEY SHAFT SIZE: | primary |  |  | Spec min 1-15/16 in (non-driven). Spec 12,000 psi max bending with 1.5 factor: ~2,770 psi at 1-15/16 (tail tension 295 lb/side + 295 lb pulley) – OK. |
| M33 | AVERAGE CARRYING IDLER SPACING: | primary |  |  | Spec 2.6.C.9.b: carry idlers 4'-0" max centers, 1'-9" max at load areas. 4.0 used (spec max); the true average is a little lower once load zones are laid out – small effect on Te. |
| AM33 | SHAFT MATERIAL: | primary |  |  | Shaft material not specified – JMS standard 1045. Spec stainless clauses (2.2.H 316; 2.6.C.10 304 frame) don't name shafting; confirm the EoR accepts carbon-steel shafts. |
| M34 | AVERAGE RETURN IDLER SPACING: | primary |  |  | Spec 2.6.C.9.b: return idlers flat, 10'-0" max centers (spec text reads 10"-0" – typo, also flagged in J. Morrison markup). |
| AM34 | GEARBOX WEIGHT: | primary |  |  | Enter after the SEW selection – adds overhung moment to the drive shaft and bearing load (P90). |
| M35 | DRUM PULLEY DIA: | primary |  |  | Spec 2.6.C.8.b: pulleys 12 in minimum diameter, engineered class. |
| AM35 | PULLEY WEIGHT: | primary |  |  | JMS conservative default 295 lb (actual 12 in x 32 in pulley is lighter). |
| M36 | IDLER SIZE: | primary |  |  | Spec 2.6.C.9.a: CEMA C, 5 in dia, 1/8 in urethane-coated rolls, HDG brackets, sealed bearings. |
| AM36 | ANGLE BTW TENSION AND OVERHUNG LOAD: | primary |  |  | JMS standard 90 deg. |
| P58 | Selected Drum RPM | primary |  |  | From the SEW selection. Target = design drum speed P56 = 29.96 rpm (100 FPM on 12.75 in lagged dia). L10 (P93) and idler rpm (M78) show errors or 0 until this is filled. |
| AU58 | Selected Horsepower | primary |  |  | Spec 2.6.C.5.a: 3 HP motor required (230/460V, 3-ph, 60 Hz, TEFC, motor SF 1.15). Calc min 1.49 HP with bounding geometry, so SF = 2.0. Gear unit is AGMA Class II (2.6.C.5.d) – JMS min gear service factor 1.4; spec 2.2.F.3: reduce… |
| J61 | GEARBOX: | primary |  |  |  |
| Q61 | GEARBOX: | primary |  |  |  |
| J62 | RATIO: | primary |  |  |  |
| J63 | GEARBOX OUTPUT: | primary |  |  |  |
| Q63 | GEARBOX OUTPUT: | primary |  |  |  |
| J64 | MOUNTING: | primary |  |  | Spec: shaft-mounted gearmotor. JMS std for Bio-BELT = SEW KA hollow shaft + torque arm; conduit box not on the conveyor-frame side. |
| Q64 | MOUNTING: | primary |  |  |  |
| J65 | MOTOR: | primary |  |  |  |
| Q65 | MOTOR: | primary |  |  |  |
| J67 | DESIGN: | primary |  |  | No NEMA design letter in Section 46 21 73 (check the Motor Data Sheet supplement). |
| J68 | EXPLOSION RATING: | primary |  |  | OPEN – depends on area classification (see P16). |
| J69 | DRIVE NOTES: | primary |  |  | Spec 2.6.C.5: 3 HP, 230/460V, 3-ph, 60 Hz, TEFC, SF 1.15, shaft-mounted AGMA Class II helical gearmotor at head shaft, 100 FPM. Spec 2.2.F: reducer input rating >= motor HP, oil-immersed ball/roller bearings, no periodic re-greasi… |
| M79 | IDLER SPACING: | primary |  |  | Spec 2.6.C.9.b: 1'-9" max at load areas – 1.5 ft (largest list value <= 1.75). |
| M80 | # OF IMPACT ZONES: | primary |  |  | One load zone under each of the 3 screen discharge chutes (2.6.A.2). |
| M81 | LENGTH OF IMPACT ZONES: | primary |  |  | OPEN: impact-zone length depends on the screen chute size and spacing – from drawings or the screen supplier. |
| AL88 | CONVEYOR BELT | primary |  | "FLAT, SIDEWALL, CLEATED SIDEWALL" | Spec 2.6.C.4.c: raised sides min 1-1/2 in above belt center; G. Hyde markup reads this as a sidewall belt (flat pulleys and idlers). If a troughed/molded-edge belt is intended instead, revisit M31, M32, K105, K108. |
| AL89 | BELT CONVEYOR TYPE (SEE IMAGES): | primary |  | "Type 1,Type 2,Type 3,Type 4,Type 5" | Type 2 (all incline) = bounding placeholder matching M24/M25. Change when the layout is known (likely Type 3). |
| AL90 | CONVEYOR DIMENSION A: | primary |  |  |  |
| AL92 | CONVEYOR DIMENSION C: | primary |  |  |  |
| AL95 | MATERIAL OF CONSTRUCTION: | primary |  | "304 SS,304L,316L" | Spec 2.6.C.10.a: frame, supports, spreaders 304 SS; skirt brackets and drip pans 304 SS; hardware 316 SS (2.6.C.17; G. Hyde note 'Scope says 304 - use 316' on hardware). General clauses 1.4.F (304L min) and 2.2.H (316) conflict wi… |
| K97 | GUIDELERS: | primary |  | "Yes,No" | Not specified. |
| Z97 | QTY: | primary |  |  |  |
| AL97 | QTY. OF 2' SUPPORTS: | primary |  |  | OPEN: supports 'at the locations shown on the plans' (2.6.C.10.c) – quantities TBD from drawings. |
| K98 | TYPE OF PRIMARY SCRAPER: | primary |  | "None,JMS,MARTIN" | Spec 2.6.C.11: doctor-style, replaceable urethane blade, twist-type tensioner. JMS wiper assumed – confirm it matches, else Martin. |
| AL98 | QTY. OF 5' SUPPORTS: | primary |  |  |  |
| K99 | SECONDARY SCRAPER: | primary |  | "Yes,No" | Only one wiper specified. |
| AL99 | QTY. OF 10' SUPPORTS: | primary |  |  |  |
| K100 | E-STOP SWITCH: | primary |  |  | Spec 2.6.C.15: 2 pull cords (one each side), orange, NEMA 7, 120V. 501434 = NEMA 7/9, 2 DP/DT, explosion-proof (DPDT per current JMS practice). Verify the P/N is current (502187 is obsolete). |
| Z100 | QTY: | primary |  |  | Qty 2 per 2.6.C.15.a. |
| AL100 | QTY. OF 15' SUPPORTS: | primary |  |  |  |
| K101 | ZERO SPEED: SENSOR: | primary |  |  | OPEN – spec 2.6.C.16: zero-speed sensor NEMA 7, 120V. No list option is confirmed NEMA 7 / Class I: MSP-12 is NEMA 4X only; XPP-5 is ATEX-only (23051 lesson); SCP-1000 rating not confirmed. Select once the area class (P16) is know… |
| AL101 | QTY. OF 20' SUPPORTS: | primary |  |  |  |
| K102 | BELT ALIGNMENT SWITCH: | primary |  | "N/A,TA-2,TA-2X (EXP.PROOF)" | Not specified. |
| K103 | BELTSCALE: | primary |  | "Yes,No" | Not specified. |
| AL103 | SPLICE TYPE: | primary |  | "Mechanical,Vulcanized" | Spec 2.6.C.4.b: shop or field vulcanized endless splice. CONFLICT: spare parts (2.10.B.2.b) list lacing tools and 2 lacing kits (mechanical splice) – clarify. |
| AL104 | SPLICE MODEL: | primary |  | "N/A,RS187,375" | N/A for a vulcanized splice. |
| K105 | HEAD PULLEY TYPE: | primary |  | "Flat, Crown" | SPEC CONFLICT: 2.6.C.8.a says 'positive crowned drum'; G. Hyde markup says 'flat drum used on sidewall'. Flat used for the sidewall belt – needs an exception/clarification in the submittal. |
| K106 | HEAD PULLEY LAGGING TYPE: | primary |  | "N/A, Smooth, Chevron, Herringbone, Diamond" | Spec 2.6.C.8.a: 'plain' vulcanized rubber lagging = Smooth (herringbone would be a deviation). |
| AL106 | COVER TYPE: | primary |  | "NONE,WEATHER,ODOR" | No top cover in spec. Spec does require a #16 ga SS return-belt cover on top of the frame (2.6.C.10.b) – make sure it is costed. |
| K107 | HEAD PULLEY LAGGING DURO.: | primary |  | "N/A, 40, 60" | Not specified; 60 duro = Superior standard. |
| AL107 | COVER LENGTH: | primary |  |  |  |
| K108 | TAIL PULLEY TYPE: | primary |  | "Flat, Crown" | Same flat-vs-crown conflict as K105. |
| K109 | LAGGING ON TAIL PULLEY?: | primary |  |  | Only the drive pulley is lagged per 2.6.C.8.a (see AM29). |
| AL109 | PE STAMP: | primary |  | "Yes,No" | OPEN: Section 46 21 73 doesn't require sealed calcs. Check Div 01 and structural general notes (seismic anchorage). |
| K110 | LAGGING THICKNESS: | primary |  | "N/A,.25,.375,.5" |  |
| K111 | TAIL PULLEY LAGGING TYPE: | primary |  | "N/A, Smooth, Chevron, Herringbone, Diamond" |  |
| K112 | TAIL PULLEY LAGGING DURO.: | primary |  | "N/A, 40, 60" |  |

## Key result cells (read after recalculation)

| Cell | Label (nearest text) |
|---|---|
| M19 | DESIGN WEIGHT LOADING: |
| M20 | DESIGN VOLUME LOADING: |
| M30 | BELT WEIGHT: |
| P38 | Material Weight |
| P40 | Combined Weight |
| P41 | Distance Between Skirts |
| P42 | Depth of Material |
| P48 | Skirtboard Friction |
| P50 | Belt Cleaning Resistance |
| P52 | Belt Capacity |
| P53 | Capacity Utilization |
| AU37 | Minimum Tension 2% Sag |
| AU38 | Inches of Sag Between Idlers |
| AU43 | Force to Lift or Lower Material Load |
| AU47 | Resistance of Accessories |
| AU48 | Te |
| AU50 | T2 |
| AU51 | T1 |
| AU53 | Tail Pulley Tension |
| P56 | Design Drum RPM |
| P57 | Required Torque @ Drum |
| P58 | Selected Drum RPM |
| AU55 | Horsepower Required at Belt |
| AU57 | Min Required Motor Horsepower |
| AU58 | Selected Horsepower |
| AU59 | Safety Factor |
| AJ67 | T |
| AJ68 | D |
| AU61 | Bearing Centers |
| AU64 | Resultant Belt Tension |
| AU65 | Resultant Load |
| AU66 | Belt Resis. Moment Load |
| AU69 | Selected Shaft Okay? |
| AU70 | tan(α) Acceptable? |
| AV28 | TAKE UP LENGTH: |
| AV29 | LAGGING ON HEAD PULLEY?: |
| AU74 | Calculated Idler Load |
| AU76 | Unit Impact Force |
| AU77 | Impact Force Less Than CIL or CILR? |
| P90 | Radial Load per Bearing |
| P93 | L10 Bearing Life |
| M74 | PART NUMBER: |
| M78 | IDLER ROLL RPM: |
| AM34 | GEARBOX WEIGHT: |
| K113 | HEAD PULLEY PART NUMBER: |
| K114 | TAIL PULLEY PART NUMBER: |
