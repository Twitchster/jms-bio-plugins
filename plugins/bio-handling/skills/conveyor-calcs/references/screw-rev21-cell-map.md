# Screw Conveyor Process (Design Sheet) REV 21 (Revision sheet: 21, Jun 2026) — Design sheet cell map

Generated from the blank template with `scripts/inspect_template.py`, using the template's own color legend (yellow FFFFCC = primary input, blue D9E1F2 = secondary input). Only Design-sheet inputs are filled; the other sheets are never written.

**Worked-example notes** come from the first JMS run of this workflow (25026 SSC-1 shaftless screenings screw (Spec 41 12 13.36, 40 05 93, dwg M-211), Oct 2026). They show what each input meant in practice and where its value came from. They are examples, not defaults: re-derive every value from the current project's documents.

**Revision check:** at intake, run `inspect_template.py` on the template being used. If the Revision-sheet number or the input list differs from this file, stop and rebuild the map before filling. A changed layout would put values in the wrong cells without any error.

**Formula defaults:** AP11 (density) and AP12 (solids content) hold formulas (`=Reference!CB1`, `=Reference!CC1`) that pull defaults from the material table. When the spec gives values, overwrite them with `fill_calc.py --allow-formula AP11 AP12` and comment the source. The first run did this (70 lb/ft³, 20%).

**Gearbox output speed:** AJ21 stays blank until the SEW selection (close-out). Torsion and thrust results depend on it; for previews, use a temporary copy with the target speed.

## Inputs

| Cell (span) | Label | Class | Template value | Dropdown source | Worked-example note |
|---|---|---|---|---|---|
| U4:AF4 | PROJECT NO.: | primary |  |  | JMS project no. confirmed by ASB. EoR (Arcadis) project no. 30003039. |
| AK4:AO4 | BY: | primary |  |  |  |
| U5:AF5 | LOCATION: | primary |  |  | Greater New Haven WPCA - Capacity Upgrades at East Street Pump Station for CSO Reduction (drawing title block). |
| AK5 | DATE: | primary |  |  |  |
| U6:AF6 | CUSTOMER: | primary |  |  | OPEN: customer/contractor not named in the documents. |
| AK6:AO6 | REVISION: | primary |  |  |  |
| U7:AF7 | ENGINEER: | primary |  |  | Arcadis U.S., Inc., Middletown CT (drawing title block). |
| AK7 | REV DATE: | primary |  |  |  |
| U8:AF8 | DESCRIPTION: | primary |  |  | Spec 41 12 13.36 Screw Bulk Material Conveyor; drawings M-206 (plan) and M-211 Section 2 (elevation). |
| AK8:AL8 | PAGE: | primary |  |  |  |
| AN8:AO8 | OF | primary |  |  |  |
| P10:AB10 | IDENTIFICATION: | primary |  |  | Tag SSC-1 per M-211. Grit collector screws GC-1 to GC-4 are not in this calc (ASB). |
| AP10 | CONVEYED MATERIAL: | primary |  |  | Spec 2.1.B: washed and compacted screenings from 3/4 in bar screens. Material factor Fm = 1.5. |
| P11:AB11 | DESCRIPTION: | secondary |  |  |  |
| AP11:AR11 | DENSITY: | primary | formula: =Reference!CB1 |  | Spec 2.1.B maximum density 70 lb/ft3 (replaces the 75 lb/ft3 material default). |
| P12:AB12 | JMS ASSEMBLY: | primary |  |  |  |
| AP12:AR12 | SOLIDS CONTENT: | primary | formula: =Reference!CC1 |  | Spec 2.1.B maximum solids 20% (replaces the 38% default). Low for compacted screenings; no calc impact. |
| P13:R13 | LENGTH: | primary |  |  | 30 ft per spec 2.1.B (approximate; field-verify). M-211 scales to about 27.5 ft; 30 ft kept as conservative (ASB). |
| AP13 | FLOWABILITY: | primary | formula: =Reference!CE1 |  |  |
| P14 | DRIVE ARRANGEMENT: | primary |  |  | Spec 2.3.I.1: shaft-mounted integral gearmotor, close coupled (2.3.I.4.b), mounted to trough end plate (2.3.I.4.a). Efficiency 0.95. |
| AP14 | SIZE: | primary | formula: =Reference!CD1 |  |  |
| P15 | FLOW DIRECTION: | primary |  |  | Spec 2.1.B '3HP, Push-Type'; drive at the low (inlet) end on M-211. |
| AP15 | ABRASIVENESS: | primary | formula: =Reference!CF1 |  |  |
| P16 | SERVICE DUTY: | primary |  |  | Not specified; affects shafted-screw lookups only (no effect on shaftless). |
| AP16:AR16 | MATERIAL TEMPERATURE RANGE: | primary |  |  | Material temperature 32 to 104 F confirmed by ASB (indoor building; 40 05 93 ambient max 40 C). Used only in shafted-screw expansion checks. |
| AW16:AY16 | MIN/ | primary |  |  |  |
| P17 | LIVE BOTTOM: | primary |  |  | No live bottom; three washer/compactor inlet hoppers feed the screw (2.1.A.2). |
| AP17 | OTHER CHARACTERISTICS: | primary | formula: =Reference!CG1 |  |  |
| P18 | AREA CLASSIFICATION: | primary |  |  | Spec 2.3.I.5.b: motors suitable for Class I, Division 2. |
| AP18:BB18 | NOTES: | secondary | -- |  |  |
| J20:L20 | DESIGN CAPACITY: | primary |  |  | Spec 2.1.B maximum loading capacity 80 ft3/hr. |
| AJ20 | GEARBOX: | primary |  |  | SEW-EURODRIVE. FROM CONFIGURATOR SELECTION (10/1/26) - replace with the SEW quote value. |
| AQ20 | GEARBOX: | primary |  |  | SEW FAZ97 (F parallel-shaft helical, B14 flange, hollow shaft = JMS Bio-SCREW std). Full type: FAZ97DRN100LM4/TH/DH. FROM CONFIGURATOR SELECTION (10/1/26) - replace with the SEW quote value. |
| J21 | SCREW DIAMETER: | primary |  |  | Spec 2.1.B minimum screw OD 15.75 in; 16 in is the next standard size. |
| AJ21 | SPEED: | primary |  |  | Output speed 10.08 rpm (1762 / 174.87). Must stay >= 9.4 rpm: spec spiral limit (0.3 Fy at 2.5x motor torque). Capacity speed is 9.82 rpm. FROM CONFIGURATOR SELECTION (10/1/26) - replace with the SEW quote value. |
| AQ21 | SPEED: | primary |  |  | Ratio 174.87 (SEW DriveConfigurator Release 26.7, 10/1/26). Note: the sheet's F97 table lists this ratio at 9.7 rpm on an older motor-speed basis. FROM CONFIGURATOR SELECTION (10/1/26) - replace with the SEW quote value. |
| J22 | SCREW PITCH: | primary | Full |  | Spec 2.3.B.4: constant pitch over the full length. |
| AJ22 | GEARBOX OUTPUT: | primary |  |  |  |
| AQ22 | GEARBOX OUTPUT: | primary |  |  | 2.938 in hollow bore = drive shaft J50. FROM CONFIGURATOR SELECTION (10/1/26) - replace with the SEW quote value. |
| J23 | SCREW TYPE: | primary |  |  | Spec 2.1.A.1 shaftless (shafted unacceptable, 2.1.A.3). Dual spiral per ASB: cuts spiral stress about 57% vs single 1x3. |
| AJ23 | MOUNTING: | primary |  |  | B14 flange (FAZ), mounted to trough end plate per spec 2.3.I.4.a. JMS std for Bio-SCREW. |
| AQ23 | MOUNTING: | primary |  |  | PLACEHOLDER M1, no pivot angle. Set the mounting position and the 15 deg pivot angle from the GA; both change oil quantity. FROM CONFIGURATOR SELECTION (10/1/26) - replace with the SEW quote value. |
| J24 | SCREW PIPE SHAFT: | primary | None |  |  |
| AJ24 | MOTOR: | primary |  |  | SEW motor (SEW sources the final motor from the datasheet). FROM CONFIGURATOR SELECTION (10/1/26) - replace with the SEW quote value. |
| AQ24 | MOTOR: | primary |  |  | DRN100LM4, 3 HP, 1762 rpm, IE3, 230/460 V, 8.4/4.2 A, 155(F), IP66. FROM CONFIGURATOR SELECTION (10/1/26) - replace with the SEW quote value. |
| J25 | SPIRAL SIZE: | primary |  |  | Dual spiral, 1 x 3 in outer / 0.75 x 2.5 in inner (sheet standard for 16 in dual), per ASB. |
| AJ25 | POWER: | primary |  |  | Spec 2.1.B: 3 HP, 460 V / 3 ph / 60 Hz. Calc needs 1.32 HP at max fill. |
| J26:L26 | TROUGH FILL: | primary |  |  |  |
| O26:Q26 | % | primary |  |  | Max fill 12% = 1.5x design (sheet standard). |
| AJ26 | GEARBOX SF: | primary |  |  | SEW service factor fB 2.10 on nameplate (JMS min 1.4, max 3). Spec 2.3.I.4.c needs >= 1.5x calculated torque: 38,640 vs 12,380 in-lb, OK. FROM CONFIGURATOR SELECTION (10/1/26) - replace with the SEW quote value. |
| J27:L27 | INCLINE: | primary |  |  | Spec 2.1.B and M-211: 15 deg. |
| AJ27 | EXPLOSION RATING: | primary |  |  | Spec 2.3.I.5.b Class I Div 2. SEW maximum is Class I Div 2; send the classification with the request so SEW sources a suitable motor. |
| AJ28 | DESIGN: | primary |  |  | NEMA Design B per 40 05 93 2.4.A.5. Not a configurator option; pass to SEW. |
| AJ29:BB29 | DRIVE NOTES: | secondary |  |  | Configured options (JMS std section 4 + spec): inverter-duty box checked (thermal F + protection), TH winding thermostat, DH drain hole, 115 V heater, IP66, FKM motor + two FKM gear seals, SS breather, CLP 220, US13 + OS4. Oil sig… |
| AO41:AQ41 | Drive Efficiency | secondary | formula: =Reference!EP1 |  |  |
| J49 | CONNECTION TYPE: | primary | Flange |  | Spec 2.3.B.10: flanged connection plate welded to the screw, bolted to the drive shaft flange. |
| J50 | SHAFT SIZE: | primary | 2.438 |  | 2-15/16 in, sheet standard for 16 in dual; matches the FAZ97 2.938 in bore. |
| J51 | SHAFT MATERIAL: | primary | 1045 CS |  | Exception to spec 4150 HT (2.3.A.4.d) per ASB. 4140 Alloy used in the calc (21 ksi allowable shear, same as 1045). |
| J53 | PIPE MATERIAL: | primary | None |  | No pipe: flange connection on a shaftless screw. |
| J54 | BOLT SIZE: | primary | None |  |  |
| J55 | BOLT MATERIAL: | primary | None |  |  |
| J56 | BOLT QUANTITY: | primary | 0 |  |  |
| J57 | BOLT PADS: | primary | None |  |  |
| T60:X60 | Motor Power Safety Factor | secondary | 2.5 |  | 2.5x motor torque matches spec 2.3.B.7 (250% of nameplate torque). |
| AA78 | SCREW FLIGHTS | primary |  |  | Carbon Steel 58 ksi per ASB (spec 2.3.A.4.c: cold-formed spring steel >= 220 HB, >= 32,000 in-lb). SPEC CHECK: spiral stress at 2.5x motor torque must be <= 0.3 Fy = 17,400 psi (2.3.B.5 + B.7); sheet M127 checks 1.0 Fy. At 10.08 r… |
| AQ78:BB78 | N/A | primary | -- |  |  |
| K79 | DRIVE END SEAL | primary |  |  | Spec 2.3.I.3: stuffing box, cast iron or galvanized, 1/2 in Teflon packing, lantern ring with SS grease fitting. |
| AA79 | DRIVE END SEAL | primary |  |  |  |
| AI79 | N/A | primary | -- |  |  |
| AQ79:BB79 | -- | primary |  |  |  |
| K80 | TAIL END SEAL | primary |  |  | Spec 2.3.B.11: tail end unrestrained; no tail bearing, thrust plate or end shaft. |
| AA80 | TAIL END SEAL | primary |  |  |  |
| AI80 | -- | primary | -- |  |  |
| AQ80:BB80 | -- | primary |  |  |  |
| K81 | DRIVE END BEARING | primary |  |  | Spec 2.3.I.2.b: drive bearings in the reducer housing, L10 >= 100,000 h, thrust capable. SEW to confirm with 4,562 lbf axial. |
| AA81 | DRIVE END BEARING | primary |  |  |  |
| AI81 | -- | primary | -- |  |  |
| AQ81:BB81 | -- | primary |  |  |  |
| K82 | HANGER/LINER TYPE | primary |  |  | Shaftless: no hanger; UHMW trough liner (bearing factor Fb = 2). |
| AA82 | HANGER/LINER TYPE | primary |  |  |  |
| AI82 | -- | primary | -- |  |  |
| AQ82:BB82 | -- | primary |  |  |  |
| K83 | TAIL END BEARING | primary |  |  |  |
| AA83 | TAIL END BEARING | primary |  |  |  |
| AI83 | -- | primary | -- |  |  |
| AQ83:BB83 | -- | primary |  |  |  |
| K84 | TROUGH | primary |  |  | Spec 2.3.C: U-shaped double-flanged trough, 3/16 in min, 316L. |
| S84 | TROUGH | primary | 10 ga |  |  |
| AA84 | IN | primary |  |  |  |
| AI84 | IN | primary | -- |  |  |
| AQ84:BB84 | -- | primary |  |  |  |
| K85 | COVER | primary |  |  | Spec 2.3.E: flanged covers, 12 ga min 316L, max 4 ft long, 1/16 in gasket, SS bolts. |
| S85 | COVER | primary | 12 ga |  |  |
| AA85 | IN | primary |  |  |  |
| AI85 | IN | primary | -- |  |  |
| AQ85:BB85 | -- | primary |  |  |  |
| K86 | INLET | primary |  |  | Three inlets (2.1.B); square flange confirmed by ASB. Coordinate with the washer/compactor supplier (2.3.F.4). |
| AI86 | -- | primary | 1 |  |  |
| AQ86:BB86 |  | primary |  |  |  |
| K87 | OUTLET | primary |  |  | One outlet with flanged flexible chute to the dumpster (2.3.F.2); square flange confirmed by ASB. |
| AI87 | -- | primary | 1 |  |  |
| AQ87:BB87 |  | primary |  |  |  |
| K88 | COVER HOLDDOWN | primary |  |  | Spec 2.3.E.5: covers fastened with stainless steel bolts. |
| AI88 | -- | primary | -- |  |  |
| AQ88:BB88 | -- | primary |  |  |  |
| K89 | LINER | primary |  |  | Spec 2.3.A.4.e: 1/2 in UHMW liner, two-color wear indicator, 316L clips. |
| S89 | LINER | primary | 1/2 |  |  |
| AA89 | 1/2 | primary |  |  |  |
| AI89 | 1/2 | primary | -- |  |  |
| AQ89:BB89 | -- | primary |  |  |  |
| K90 | GB TO SHAFT COUPLING | primary |  |  | Hollow-bore shaft mount; no coupling. |
| S90:BB90 | GB TO SHAFT COUPLING | primary |  |  |  |
| K91 | ZSS | primary |  |  | MSP 12 per ASB. Spec 2.5.A.1 names MFA-4P + XPP-5 sensing a tail shaft (none on a shaftless screw). MSP 12 is NEMA 4X only while the area is Class I Div 2: take exception or confirm the sensor location is unclassified. |
| S91:AA91 | ZSS | primary | -- |  |  |
| AI91:BB91 | -- | primary |  |  |  |
| K92 | ESTOP | primary |  |  | Spec 2.5.A: pull cord around the full perimeter, NEC rating per area (Class I Div 2). 2 x RS5X per ASB. |
| S92:AA92 | ESTOP | primary | -- |  |  |
| AI92:BB92 | -- | primary |  |  |  |
| K93:BB93 | OTHER1 | primary |  |  |  |
| K94:BB94 | OTHER2 | primary |  |  |  |
| M120:P120 | Screw Deflection | primary | 0.25 |  |  |
| M122:P122 | Screw Thermal Expansion | primary | 0.125 |  |  |
| M123:P123 | Trough Thermal Expansion | primary | 0.125 |  |  |
| M126:P126 | Spiral Compression | primary | 0.08 |  |  |

## Key result cells (read after recalculation)

| Cell | Label (nearest text) |
|---|---|
| AJ21 | SPEED: |
| R25 | SPIRAL SIZE: |
| P31 | Screw Inside Diameter |
| P36 | Flight Factor |
| P40 | Equivalent Capacity |
| P41 | Capacity per Rotation |
| P42 | Conveyor Speed |
| P43 | Capacity |
| P44 | Capacity at Max Fill |
| W44 | FT3/HR |
| AO32 | Lift Height |
| AO42 | Frictional Power |
| AO43 | Material Power |
| AO45 | Total Power |
| AO46 | Total Power at Max Fill |
| T61 | Torque From Motor Power (Gearmotor) |
| T62 | Torque From Motor with Safety Factor |
| AR60 | PSI |
| AK60 | DRIVE SHAFT |
| AX60 | PSI |
| T98 | Total Weight of Screw |
| T109 | Screw Tip Speed |
| T110 | Trough Surface Speed |
| T111 | Bolt circle diameter for flange |
| T112 | Average spiral thickness |
| T113 | Spiral width |
| T114 | Radial  Force from Torque |
| T116 | Diameter Ratio |
| T117 | Wahl's Constant |
| T124 | Screw Abrasion Score |
| T125 | Trough Abrasion Score |
| T126 | IN/FT |
| AB126 | IN/FT |
| M126 | Spiral Compression |
| T127 | PSI |
| M127 | Spiral Stress |
| AB127 | PSI |
| AS96 | Axial Thrust |
| S91 | ZSS |
