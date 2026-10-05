# Equipment List PDFS library

Snapshot from the Oct 5 2026 audit (`scripts/cutsheet_markup.py audit`): 108 PDFs, about 510 MB. Re-run the audit at the start of a job if the library may have changed, and update this file when it has.

## Location and access
- `C:\Users\<user>\OneDrive - Jim Myers & Sons, Inc\Equipment List PDFS`, owned by ASB and shared to the Bio PE team with edit access. Each user adds it to their OneDrive ("Add shortcut to My files").
- Files are often cloud-only on the computer. Staging a file downloads it; reading it from the device shell fails until it's downloaded.
- `Projects\<project number>\` holds the outputs. The Microsoft 365 connector can read the text of the library (files under 100 MB) but can't fetch the files, so markup needs a linked computer.

## Top-level folders
Actuator (Gate_Plow_Diverter), Anchors, Bearing (Hanger) Automatic Lubricators, Bearings, Belt Alignment Switch, Belt Splice Kits, Belts, Drum Pulleys, E-Stop, Expansion Joint, Gate, Gearbox, Grounding Ring_Shaft, Idlers, Level Sensor_Transmitter_Radar, Lighting System, Limit Switch, Load Cell, Load Stand, Motor, Scrapper - Belt, Vibrator, Zero Speed Switch. Below each: vendor folders, and sometimes model folders.

## File conventions
- **Numbered prefixes** (`1 …`, `2 …`, `4 - …`) set the order of a component packet. Gearbox/SEW, for example:
  1. `#Component Cover Sheet`
  2. `1` datasheet
  3. `2` dimensional sheet
  4. `3` mounting positions
  5. items 4–10 from `Common Items to be included`
- **`#Component Cover Sheet.pdf`** is a blank page for the equipment name and tags. The library copies carry stale tags; always strip them and rewrite.
- **Empty `.delete` / `.Delete` files** are placeholders for project-specific inserts, usually from the vendor quote: "Insert gearbox datasheet", "Insert motor datasheet", Rotork "Wiring Diagram from quote" and "Drawing provided with quote", Limitorque "Request Datasheet".
- **`Archive`, `Old`, `Locked` = superseded.** Use the current file.
- **`FOR REFERENCE` files are for decoding**, not packet pages. Example: the SEW catalog, whose Section 3 holds the type-designation nomenclature.
- **Generic and part-number-specific copies** of the same sheet sit side by side in the level-sensor folders (e.g. `echomax_xps_fi01_en 2024.pdf` and `... - 7ML1118-0CA30.pdf`). Which one to use is still an open question.
- **Not packet material:** `.stp` models, a `.lnk` shortcut (`Motor/SEW - Shortcut (from Gearbox).lnk`), and `#Contact Cody Marks for.drawings` (a note).
- **The SEW catalog is 101.9 MB**, over the connector's 100 MB read limit; it's readable only through the linked computer.

## Files carrying markups from earlier projects (leave as is; strip in working copies)
- `Anchors/HILTI/1 HILTI Kwik Bolt - updated cat cut-Rev1.pdf`
- `Limit Switch/Allen Bradley/1 Limit Switch - Allen Bradley Datasheet.pdf`
- `Vibrator/Navco/Vibrator - NAVCO.pdf`
- `Belts/Belt Service/Conveyor Belt - Belt Service Cut Sheet.pdf`
- `Belt Alignment Switch/Conveyor Components/Belt Alignment - Conveyor Components - Cut Sheet.pdf`
- `Gearbox/SEW/#Component Cover Sheet.pdf`
- `Gearbox/SEW/Common Items to be included/#Component Cover Sheet.pdf`
- `Gearbox/SEW/Common Items to be included/5 - Gearbox - SEW - closing plugs.pdf`
- `Expansion Joint/Proco/Expansion Joint - Proco 271 (LR) 24in X 10 in.pdf`
- `Bearings/Dodge/Archive/Mounted Roller and Plain Bearings (W) - Dodge (CA1GN02-09.25) (Locked).pdf`
- `Actuator (Gate_Plow_Diverter)/Gate Actuator/Limitorque/1 Actuator - Limitorque - MX SERIES B ACTUATOR Cat Cut.pdf`
- `Actuator (Gate_Plow_Diverter)/Gate Actuator/Limitorque/4 Actuator - Limitorque - Base Detail 03-615-0008-1.pdf`
- `Actuator (Gate_Plow_Diverter)/Gate Actuator/Rotork/1 Actuator - Rotork - Slide Gate Actuator.pdf`
- `Actuator (Gate_Plow_Diverter)/Gate Actuator/Rotork/Archive/1 Actuator - Rotork - Slide Gate Actuator.pdf`
- `Actuator (Gate_Plow_Diverter)/Plow and or Diverter Actuator/Rotork/Actuator - Rotork - Cat Cuts (Plow & Diverter).pdf`
- `Actuator (Gate_Plow_Diverter)/Plow and or Diverter Actuator/Rotork/Actuator - Rotork - Cat Cuts (Plow Actuator ONLY).pdf`
- `Level Sensor_Transmitter_Radar/OBS/Siemens Easy Aimer Data Sheet 4-2020.pdf`
- `Level Sensor_Transmitter_Radar/OBS/Siemens HydroRanger 200 HMI Data Sheet 5-2021.pdf`
- `Level Sensor_Transmitter_Radar/OBS/Siemens MultiRanger Reference [Phased out 10.2023].pdf`
- `Level Sensor_Transmitter_Radar/OBS/sitransl_lr120_fi01_en.pdf`
- `Level Sensor_Transmitter_Radar/VEGA/Radar Transmitter - VEGA.pdf`
- `Level Sensor_Transmitter_Radar/Siemens/Siemens Easy Aimer 2 Drawing.pdf`
- `Level Sensor_Transmitter_Radar/Siemens/Siemens Easy Aimer Data Sheet 4-2020 - 7ML1830-1AU.pdf`
- `Level Sensor_Transmitter_Radar/Siemens/echomax_xps_fi01_en 2024 - 7ML1118-0CA30.pdf`
- `Level Sensor_Transmitter_Radar/Siemens/sitransl_lt500_fi01_en 2025 - 7ML6003-1AC00-1AA3.pdf`
- `Scrapper - Belt/Martin/Belt Scraper - Martin QC1 Cleaner - HD MAX - Cat Cut.pdf`
- `E-Stop/Conveyor Components/RS Model/Archive/E-Stop - Conveyor Components Model RS - CAT CUT_old.pdf`
- `Drum Pulleys/Martin (formerly CCI)/Pully Drawings & Models/Head Pulley - Martin - CMES1220X35L3H (3683167_1149919M_P1).pdf`
- `Drum Pulleys/Martin (formerly CCI)/Pully Drawings & Models/Tail Pulley - Martin - CMES1220X35 (3683167_1149923M_P2).pdf`
- `Zero Speed Switch/Siemens Milltronics (MFA-4P)(MSP-12)/4a Zero Speed Switch - Siemens Milltronics MFA-4P Manual.pdf`
- `Zero Speed Switch/Electro Sensors/Zero Speed Switch - Electro Sensor - Cat Cut.pdf`
- `Lighting System/Canty/Lighting System - Canty - HYL 80 LED Process Lighting System TA10620-2-2.pdf`
- `Load Cell/Mettler Toledo/Load Cell - Mettler Toledo - SWC615-PowerMount Datasheet-30T.pdf`
- `Load Cell/Kistler Morse/Load Cell - Kistler Morse -load-disc-ii-load-cell-specification-sheet.pdf`
- `Load Cell/Kistler Morse/Load Cell - Kistler Morse Installation Manual.pdf`
- `Load Cell/Kistler Morse/Load Cell - Kistler Morse svs2000-controller-specification-sheet.pdf`
- `Belt Splice Kits/Flexco/Belt Splice Kit - Flexco - Cat Cut (X2167_enUS_2167_AS).pdf`
- `Belt Splice Kits/Flexco/Selection Guide/Belt Splice Kit - FLEXCO Super-Screw Flexible Rubber Fastening System.pdf`

## Pages without a text layer (ASB to OCR manually; until then place boxes visually with `rect`)
- `Limit Switch/Siemens (for Gate)/Limit Switch for Gate.pdf` (3 of 3 pages)
- `Belts/Belt Service/Conveyor Belt - Belt Service Cut Sheet.pdf` (3 of 3 pages)
- `Gearbox/SEW/Catalog/FOR REFERENCE - SEW Eurodrive O&M Manual UNLOCKED BUT NO BOOKMARKS.pdf` (2 of 244 pages)
- `Gearbox/SEW/Catalog/SEW Adendum to Catalog (Eurodrive Dimensional Sheets) 26873745 (unlock).pdf` (3 of 356 pages)
- `Expansion Joint/Proco/Expansion Joint - Proco 271 (LR) 24in X 10 in.pdf` (1 of 10 pages)
- `Bearings/Dodge/Archive/Mounted Roller and Plain Bearings (W) - Dodge (CA1GN02-09.25) (Locked).pdf` (11 of 540 pages)
- `Bearings/Dodge/Archive/Mounted Roller and Plain Bearings (W) - Dodge (CA1GN02-09.25)(Unlocked).pdf` (11 of 540 pages)
- `Bearings/Dodge/Full Manual/Baldor_Dodge_039509_Catalog (Full Manual)pg 152.pdf` (1 of 756 pages)
- `Bearings/Martin Sprocket (TCC) (Screw Conveyor Bearings)/Fully Catalog/Martin Sprocket - Complete Material Handling Catalog.pdf` (1 of 224 pages)
- `Actuator (Gate_Plow_Diverter)/Gate Actuator/Limitorque/3 Actuator - Limitorque - Drawing 03-653-0006-0 MX-20.pdf` (1 of 1 pages)
- `Actuator (Gate_Plow_Diverter)/Gate Actuator/Limitorque/4 Actuator - Limitorque - Base Detail 03-615-0008-1.pdf` (1 of 1 pages)
- `Actuator (Gate_Plow_Diverter)/Gate Actuator/Limitorque/5 Actuator - Limitorque - MXB Wiring Diagram - WD-MXb-040000-0101.pdf` (1 of 1 pages)
- `Actuator (Gate_Plow_Diverter)/Gate Actuator/Limitorque/6 Actuator - Limitorque - Remote Hand Station - Drawing & Wiring Diagram (19-499-0170-0).pdf` (1 of 1 pages)
- `Actuator (Gate_Plow_Diverter)/Gate Actuator/Rotork/1 Actuator - Rotork - Slide Gate Actuator.pdf` (5 of 6 pages)
- `Actuator (Gate_Plow_Diverter)/Plow and or Diverter Actuator/Rotork/Actuator - Rotork - Cat Cuts (Plow & Diverter).pdf` (5 of 8 pages)
- `Actuator (Gate_Plow_Diverter)/Plow and or Diverter Actuator/Rotork/Actuator - Rotork - Cat Cuts (Plow Actuator ONLY).pdf` (4 of 6 pages)
- `Level Sensor_Transmitter_Radar/E&H/2. Radar Level Sensor Alignment unit - E&H - FAU40.pdf` (1 of 8 pages)
- `Level Sensor_Transmitter_Radar/Siemens/7ML19981DU01 Siemens XPS15.pdf` (1 of 28 pages)
- `Drum Pulleys/Martin (formerly CCI)/Full Catalog/Conveyor Pulleys and Idlers - Martin - Catalog.pdf` (1 of 174 pages)
- `Load Cell/Kistler Morse/Load Cell - Kistler Morse Installation Manual.pdf` (4 of 4 pages)
- `Belt Splice Kits/Flexco/Selection Guide/How_to_order_super_screw_splice.pdf` (2 of 2 pages)

## Additions log
- 2026-10-05: `E-Stop/Conveyor Components/RS Model/E-Stop - Conveyor Components Model RS - CAT CUT (1-page 2025).pdf`. This is the newer one-page edition used on a real submittal, with the project markup removed. The older two-page file is still there.

## Known gaps
- The sidewall belt brochure used on a real submittal (Beltservice "Beltwall corrugated sidewall belting", BSP6201 REV 02/23, 7 pages) isn't in the library. `Belts/Beltwall` holds the 80-page Beltwall technical manual instead.

## Worked examples (from past JMS submittals)
- **E-stop, Conveyor Components RS.** "RS-5X: 2 DP/DT microswitches, explosion proof (NEMA 7 Class I Div 1&2 Groups C&D; Class II Groups E, F, G)" boxed in the Available Models table.
  - The model letters encode contacts (2 = SP/DT, 5 = DP/DT), X = explosion proof, D = dual rated, L = signal lamp.
  - The area classification and contact requirement decide the model.
  - Match whole tokens: RS-5X is not RS-5XL.
- **Zero-speed switch, Electro-Sensors SCP.** "SCP1000, 115 VAC - Standard (800-020100)" in the Ordering table, plus "EZ-SCP Bracket Assembly (810-000005)" under Other Options. SCP1000 has one setpoint and SCP2000 two; the supply voltage decides the row.
- **Sidewall belt, Beltservice Beltwall.**
  - Page 3: compound OR (oil resistant) tile; base belt "BWX2222MI - 220PIW, 2+2 Ply".
  - Page 5: sidewall row 1.5" (38 mm) height × the OR/FR/FDA min-pulley column. The compound chosen on page 3 decides the column on page 5.
