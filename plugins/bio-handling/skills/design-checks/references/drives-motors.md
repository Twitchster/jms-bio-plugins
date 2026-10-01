# Drives, Motors, Sensors

## SEW selection — JMS standard configuration

**Authoritative source:** the JMS Engineering Standard "SEW Gearmotor/Gearbox Selection" (Rev 0 draft, owner DED), transcribed in `sew-drive-selection/references/jms-sew-selection-procedure.md`. For selection work, use the `sew-drive-selection` skill. The summary below is kept for quick checks; where it differs, the standard governs.

- AC 60 Hz, 4-pole (1800 rpm), IE3.
- Service factor ≥1.4 unless spec'd (AGMA Class 2 ≥1.4, Class 3 ≥2.0; don't exceed ~3).
- S1-100% duty if the motor runs ≥8 h/day; frequent starts may change this. Always check "Frequency inverter operation" in the configurator: all SEW motors are inverter duty, and checking it sets thermal class F and thermal protection.
- Thermal class 155 (F), IP66, winding thermostat, 115 V strip heater, condensation drain hole.
- Avoid 3 TF thermistors even if spec'd; if no exception can be taken, a separate relay is needed in the control panel.
- Fan-cooled (canopy only for M4/vertical).
- None of: brake, encoder, backstop, digital interface, encapsulated terminal box, second shaft end, extra warranty (standard 2 yr; selecting 3 yr auto-adds extras and SEW gear oil).
- Coating US13 Stainless Steel Gray + OS4, stainless breather.
- Oil: CLP 220 mineral (CLP HC synthetic only if spec'd).
- Seals: two FKM oil seals; Premium Sine Seal conductive if on a VFD (the standard lists oil seal material twice; see the note in the transcription). No oil sight glass, no reduced backlash.
- Voltage usually 230/460 V. Terminal box typically 0°, cable entry X (keep clear for maintenance).
- Mounting position and pivot angle affect oil volume. Changing orientation in the field requires an oil adjustment.

## Gear unit by product
| Product | SEW unit |
|---|---|
| Bio-SCREW | F parallel-shaft helical, B14 flange, hollow shaft (K occasionally) |
| Bio-BELT | K helical-bevel, hollow shaft with torque arm; conduit box not on the conveyor-frame side |
| Bio-LIVEBOTTOM | F or K, B14, hollow shaft |
| Bio-LEVELING SCREW | F B14 hollow or FAS screw-conveyor unit |

Third-party vendors sizing drives must follow these standards.

## Contact SEW when
- Ambient >40 °C/104 °F or a thermal calc is spec'd (the configurator must stay on "No thermal calculation").
- "Especially low output speeds" would be needed.
- A non-SEW motor needs an adapter.
- Elevation ≥2,000 ft.
- Bearing calcs are needed (give axial and overhung loads).
- Reinforced bearings are considered. A pillow block between the product and the gearbox usually means none are needed.
- The area is hazardous. SEW's own motors go only to Class I Div 2, but per ASB (Oct 2026) SEW makes the final motor selection from JMS's datasheet and sources a suitable motor (other vendor if needed). Run the selection anyway and always state the area classification in the SEW request.
- Grounding rings are spec'd. Not standard; only if spec'd and on a VFD. SEW offers conductive fleece, not Aegis rings (take exception or use another motor).
- Hollow-shaft bore limits gearbox swaps (KA67 = 1.5"; KA77 min 1.75").
- SEW datasheets don't say "inverter duty". The variant adds 3 TF sensors and an FKM seal, noted in the quote. SEW letters confirm NEMA MG1 Part 31.

## Motors
- Usual drive: SEW gearbox + Baldor motor. Baldor datasheets are stock and don't reflect spec accessories; note this in submittals.
- NEMA design A vs B differ mainly in rotor design. Design letters don't reflect modern premium-efficiency motors, so question customer NEMA B requirements. [Judgment]
- Hazardous areas (25034):
  - All suppliers on a job should use the same spec motor (e.g., Baldor XPFC, 1.15 SF, winding thermostats, Class II Div 1, Class F).
  - XPNV/TENV explosion-proof motors are SF 1.0 and likely to be rejected.
  - Gyrator/spout drives are designed for direct-line duty.
  - Provide English cutsheets and nameplates.

## Sensors and switches
- Zero-speed:
  - Milltronics MSP-12 (JMS standard) is NEMA 4X only.
  - Milltronics XPP-5 is ATEX only.
  - For Class I Div 2, use Turck C1D2 proximity switches, an SCP200 shaft speed switch, or a rated inductive sensor + remote monitor.
  - 4B WDA + SR2V5-1 is Class II Div 1, not Class I.
- Pull-cord e-stops: specs now call for DPDT. PCD-2S → RS-5 (RS-5X is explosion-proof). The replacement has a different mounting-hole pattern.
- Specify sensor cable lengths that let controllers mount outside hazardous areas.

## Control panels
- NEMA 4X: conduit entries through watertight 4X fittings or bottom-entry devices; cutting the enclosure bottom risks the rating.
- Floor-standing panel size is driven by field terminals, intrinsic barriers and the UPS.
- Floor vs wall mounting can be an EoR preference; confirm in the submittal meeting.
- Allow ~8 weeks for panel shops.
