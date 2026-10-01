# JMS Engineering Standard — SEW Gearmotor/Gearbox Selection

Transcribed from `SEW_Selection_Procedure.docx`, supplied by Amr Banawan on Sep 30 2026. This file is the authoritative JMS source for this skill. Where it conflicts with anything else in the plugin, this file wins; project specifications win over this file.

**Document status:**
- Header: "Standard: 00-000-00, Revision 0, Owner: DED, Revision Date: TBD"
- Footer: "Checked by: --, Approved by: --"
- File created Jun 9 2026, last modified Jul 10 2026

**This is a Rev 0 draft without recorded check or approval.** Treat it as current JMS practice, but say so when citing it. Replace this file when an approved revision is issued.

## 1. Purpose and scope

The standard gives standardized references for SEW gearmotors and gearboxes: technical characteristics, selection considerations and application. It applies to all Project Engineers and related technical staff who design, specify, procure or apply SEW gearmotors/gearboxes. It defines the JMS standard configurations, explains option choices, and gives guidance by product type.

## 2. Responsibilities (Project Engineers)

- Apply JMS company standards for SEW gearmotor/gearbox selection.
- Verify technical suitability for the application.
- Incorporate customer requirements where applicable.
- Ensure third-party vendors sizing or purchasing gearmotors/gearboxes for JMS equipment capture the JMS standards and project requirements.

## 3. References

The references are the project specifications and the SEW drive configurator website.

## 4. SEW configuration options

The table follows the JMS standard in the order the SEW DriveConfigurator presents the options. "JMS std" = JMS standard configuration.

| Option | Selection | Notes |
|---|---|---|
| Gear unit design | Project specific | By product/project; see §5 |
| Motor type | AC motor | JMS std |
| Motor Hertz | 60 Hz | JMS std; may change outside the USA |
| Motor power (HP) | Project specific | Calculated per the project specifications |
| Output speed (rpm) | Project specific | Calculated per the project specifications |
| Service factor | Minimum 1.4 | JMS std minimum 1.4 unless the spec dictates. AGMA Class 2 = min 1.4; AGMA Class 3 = min 2.0. **Caution: don't go above SF 3; it can be detrimental to the gearbox.** |
| International efficiency class | IE3 – Premium efficiency | JMS std; deviate only if the spec dictates |
| Number of poles | 4 (1,800 rpm) | JMS std. 2-pole = 3,600 rpm; 6-pole = 1,200 rpm. Deviate only if the spec dictates. |
| Duration factor | S1-100% / project specific | S1-100% if the motor runs at least 8 h/day (most JMS projects). The number of on/off starts per day may require a change. |
| Adapter between gear unit and motor | Project specific | Only for a non-SEW motor (adapter flange). Not covered by the procedure; go to SEW for sizing. |
| Ambient temperature max | No thermal calculation | SEW motors are rated to +40 °C (104 °F) standard. **"No thermal calculation" must be selected to move forward in the configurator.** Higher ambient, or a spec-required thermal calculation → **contact SEW**. |
| Elevation (not in configurator) | 0–2,000 ft | At or above 2,000 ft → **contact SEW** |
| Especially low output speeds | Unchecked | If the gearbox needs it → **contact SEW** |
| Frequency inverter operation (VFD) | Yes (check it) | All SEW motors come inverter duty as standard. Checking it automatically sets the thermal class to the JMS standard and adds thermal motor protection (JMS std). Not technically required, but good practice. |
| Grounding rings | Project specific | Only on motors known to run on a VFD **and** only if the spec dictates. SEW can't provide typical grounding rings; it offers a conductive fleece it states is equivalent. Spec calls for **Aegis** rings → can't be provided with an SEW motor. Conductive fleece required → contact SEW (not in the configurator). |
| Mounting position | Project specific | Affects oil volume and SEW construction |
| Pivoting angle | Project specific | Affects oil volume and SEW construction |
| Built-in type (flange and shaft) | Project specific | By product; see §5 |
| Shaft size | Project specific | Size and type from project calculations |
| Digital motor interface | Without digital motor integration | JMS std |
| Torque arm | Project specific | By product; **Bio-BELT requires the torque arm** (§5) |
| Terminal box position | Project specific, typically 0° | Keep clear for maintenance and installation |
| Cable entry position | Project specific, typically X | Keep clear for maintenance and installation |
| Extra warranty | Not selected | JMS std. SEW standard warranty is 2 yr; checking it extends to 3 yr and automatically adds extras (and SEW gear oil) |
| Base/top coat | US13 Stainless Steel Gray | JMS std |
| Surface protection | OS4 | JMS std |
| Motor output design | Standard | |
| Second shaft end | No selection | |
| Oil seal material (motor section of the procedure) | Standard if the motor is not on a VFD; **Premium Sine Seal conductive** if on a VFD | JMS std |
| Motor voltage | Project specific | Most jobs 230/460 V |
| Motor brake | None | |
| Thermal class | 155 (F) | JMS std; deviate only if the spec calls for it |
| Motor degree of protection | IP66 | JMS std |
| Motor thermostat | Included – winding thermostat | JMS std. The alternative is 3 TF temperature sensors (thermistors). **Try not to provide thermistors even if the spec calls for them.** If no exception can be taken, a separate relay device is required in the control panel. |
| Temperature detection | No selection | |
| Motor encoder | None | |
| Motor connector | No selection | |
| Ventilation type | Fan-cooled | |
| Ventilation canopy | Only for M4 / vertically mounted motors | |
| Fan wheel design | Standard | |
| Backstop | None | |
| Condensation drain hole | Yes | JMS std |
| Strip heater | Included, 115 V | JMS std |
| Encapsulated design (terminal box) | No | JMS std; only if the spec calls for it (rare) |
| Breather valve | Stainless steel | JMS std (listed twice in the source) |
| Lubricant | CLP 220 (mineral) | JMS std. CLP HC if the spec dictates synthetic. Extended warranty auto-selects SEW gear oil. |
| Oil seal | Two oil seals | JMS std |
| Oil seal material (gear unit options) | FKM | JMS std |
| Gear unit with reduced backlash | No / unchecked | JMS std; only for very accurate positioning (almost never) |
| Joint bonding | No | |
| Oil sight glass | None | JMS std; only if the spec dictates (rare) |
| Safety cover | No | |
| Bearing calculations (not in configurator) | Project specific | Only if the spec dictates. Contact SEW; the PE provides axial and overhung loads. |
| Reinforced bearings (not in configurator) | Project specific | Complete the thrust calculation and give the value to SEW to decide. A pillow block between the product and the gearbox must be analyzed; typically no reinforced bearings are then needed. |
| Hazard classification | Project specific | **Contact SEW directly for quotation/selection.** SEW goes only up to Class I Division 2; if Division 1 is required, an SEW motor can't be used. |

**Interpretation note:** the source lists "Oil seal material" twice.
- Motor section: Standard, or Premium Sine Seal conductive on a VFD.
- Gear-unit section: FKM, with two oil seals.

Apply both as written: two FKM gear-unit oil seals, plus Premium Sine Seal conductive where the procedure calls for it on VFD motors. If the configurator offers only one seal choice that conflicts, ask the PE, and note it for the SEW quote.

## 5. Gear unit design by product type (SEW)

| Bio product | SEW gearbox | JMS typical options | Notes |
|---|---|---|---|
| Bio-SCREW | F = parallel-shaft helical | B14 flange, hollow shaft (**FAZ**) | Other flange/shaft types per project requirements |
| Bio-SCREW | K = helical-bevel | Hollow shaft (KA) | Not common; used in certain instances. Other shaft types/options per project. |
| Bio-BELT | K = helical-bevel | Hollow shaft (KA), **torque arm with mounting hardware** | Shaft position is project specific, by gearmotor orientation. **Conduit box not on the same side as the conveyor frame.** |
| Bio-LIVEBOTTOM | F = parallel-shaft helical | B14 flange, hollow shaft (FAZ) | Other flange/shaft types per project |
| Bio-LIVEBOTTOM | K = helical-bevel | B14 flange, hollow shaft (KAZ) | Other flange/shaft types per project |
| Bio-LEVELING SCREW | F = parallel-shaft helical | B14 flange, hollow shaft (FAZ) | Other flange/shaft types per project |
| Bio-LEVELING SCREW | FAS = Screw Conveyor Unit | N/A | Drive designed for CEMA screw conveyors; output shaft selected by project calculations |

(The type codes in parentheses are the DriveConfigurator "Built-in type" names matching the options listed. The source shows pictures, not codes.)
