# SEW Reference Data for O&Ms

The SEW information the JMS O&M templates need, taken from ASB's library folder `Equipment List PDFS\SEW reference Information for O&M creation` (added Oct 13 2026). Source: SEW *Assembly and Operating Instructions – Gear Unit Series R.., F.., K.., S.., SPIROPLAN® W..*, document 27801357/EN, edition **02/2023**, the same edition the templates cite. Before issuing an O&M, check SEW's website for a newer edition. If one exists, re-verify the values below and tell the PE.

Use this file for the SEW lubrication block in `om-template-rules.md`, the SEW storage paragraphs, and SEW rows in the maintenance and troubleshooting tables. The quote or order confirmation (mounting position, oil type and quantity) still governs for each unit.

## Files shipped with the plugin (`sew-reference/`)
| File | Use |
|---|---|
| `INSERT IF SEW IS USED - SEW Installation, Maintenance and Lubrication Info (verified 2023-11-18).pdf` (44 p) | **Insert into Appendix A whenever an SEW gear unit is supplied.** Contents: SEW technical notes GM-019-01 (footed reducer mounting), GM-022-01 (installing shaft components), the 4-2014 note on bolt sizes and torques, then manual chapters 6 (inspection/maintenance) and 8.2 (lubricants, lubricant table, fill quantities). |
| `INSERT IF SEW WITH TORQLOC IS USED - GM-046-02 TorqLOC Installation (verified 2023-11-18).pdf` (4 p) | **Also insert into Appendix A when the unit has a TorqLOC hollow shaft** (type designation with ..T, e.g. FT.., KT.., ST.., WT..). It has the TorqLOC installation steps and the retaining-ring and shrink-disc tightening torques by size. Read the torques from the PDF; its tables don't extract cleanly as text. |
| `FOR REFERENCE - SEW Closing Plugs and Tightening Torques (lb-ft).pdf` (1 p) | Look-up only, not an insert: closing-plug thread by gear unit size, plug torques in Nm, and the lb-ft conversion. Tabulated below. |
| `SEW Oil Types for Lubrication Section.docx` | Oil brand lists for the O&M lubrication section. Tabulated below. |

**In the library only:** the full 244-page SEW manual (`SEW Eurodrive O&M Manual.pdf`, 17 MB, 02/2023), and a duplicate `SEW closing plugs.pdf` without the torque table. Use the manual for anything not covered here: mounting-position sheets (ch. 7.9, pp. 159–195), torque arms (4.5), shrink disk (4.8), TorqLOC (4.9), adapters, and the full lubricant tables.

## Closing plugs and tightening torques (oil level, drain, screw plugs, breather valves, sight glasses)
| Gear unit size | Plug thread | Closing plug P/N | Torque Nm | Torque lb-ft |
|---|---|---|---|---|
| R.07–67, F.27–67, K.37–67, K.19/29/39, S.47–67, W.19–59 | M10x1 | 0011426X | 12 | 8.85 |
| R/F/S/K.77–87 | M12x1.5 | 00114308 | 15 | 11.06 |
| R.97–137, F.97–107, K.97–107, K.49, S.97 | M22x1.5 | 00114316 | 60 | 44.25 |
| R.147, F/K.127 | M33x2 | 00114324 | 100 | 73.76 |
| R.167, F/K.157 | M42x2 | 00114278 | 150 | 110.63 |

The manual's torque table (section 4.3.3, p. 36) also lists M8x1 = 8 Nm (5.90 lb-ft) and M16x1.5 = 40 Nm (29.50 lb-ft); no closing plug in the table above uses them. Conversion: 1 Nm = 0.7376 lb-ft. In the O&M write "44 lb-ft (60 Nm)" and round to whole lb-ft unless the PE wants decimals.

**Example:** an FA97 → M22x1.5 → 60 Nm → "44 lb-ft (60 Nm)". Mark the M22x1.5 row in the template's closing-plug table with a red box.

## Lubricant types (O&M lubrication section)
The oil type is set per order and shown on the order confirmation and nameplate. List the brands for that oil type, and keep the template sentence telling the user to stay with the nameplate oil.

**Mineral, CLP VG 220:**
- SEW-EURODRIVE "GearOil Base 220"
- Castrol "Optigear BM 220"
- Fuchs "Renolin CLP 220 Plus"
- Mobil "Mobilgear 600 XP 220"
- Klüber Lubrication "Klüberoil GEM 1-220 N"
- Shell "Shell Omala SG 220"
- Sinopec "AP-SGO 220"
- Total "Carter EP 220"

**Synthetic, food-grade, CLP HC NSF H1 VG 460:**
- SEW-EURODRIVE "GearOil Synth 460 H1"
- Bremer & Leguil "Cassida Fluid GL 460"
- Castrol "Optileb GT 460"
- Fuchs "Cassida Fluid GL 460"
- Klüber Lubrication "Klüberoil 4UH-460 N"

The source docx spells the Total product "Cater EP 220". The trade name is *Carter EP 220*; the O&M uses the correct spelling.

**If the quote names another oil type** (e.g. CLP PG polyglycol, or a different viscosity), take the brands from the manual's lubricant table (ch. 8.2.2) for that type and viscosity. Don't reuse these lists.

**SEW rules to keep in the text:**
- Do not mix synthetic lubricants with each other or with mineral lubricants.
- Oils of the same viscosity class from different makers differ; the permitted oil-sump temperatures are maker-specific.
- Using another lubricant voids SEW's liability.
- Latest lubricant tables: www.sew-eurodrive.de/lubricants.

**Bearing grease (gear unit rolling bearings, factory fill):**
- Standard, −40 to +80 °C: SEW "Grease HL 2 E1", Fuchs "Renolit CX-TOM 15", Klüber "Petamo GHY 133 N".
- Food-grade, −40 to +40 °C: SEW "Grease HL 2 H1 E1", Bremer & Leguil "Cassida Grease GTS 2".
- Re-grease when changing the oil:
  - fast-running (input) bearings: fill the cavities between rolling elements 1/3 full
  - slow-running (output) bearings: 2/3 full

**Oil seal temperature limits (oil sump):** NBR −40 to +80 °C; FKM and FKM-PSS −25 to +115 °C.

## Inspection and maintenance intervals (manual 6.2)
| Interval | Task |
|---|---|
| Every 3,000 operating hours, at least every 6 months | Check oil and oil level; listen for bearing noise; inspect seals for leakage; check that screw plugs, sight glass, breather valve and cover screws are tight; for units with a torque arm, check the rubber buffers and replace if needed |
| Mineral oil: per the lubricant change chart, **every 3 years at the latest** | Change the oil; replace rolling-bearing grease (recommended); replace the oil seal (not in the same track) |
| Synthetic oil: per the chart, **every 5 years at the latest** | Same as mineral |
| As needed | Touch up or renew the coating; check the breather valve works |
| From the 5th year | Check backstop blocking effect annually (if a backstop is fitted) |

- **Lubricated for life**, no scheduled oil change: R..07, R..17, R..27; F..27; SPIROPLAN W.
- **Lubricant change chart (6.3):** the interval depends on the sustained oil bath temperature. The chart's average values are at 70 °C. Change more often in severe or aggressive conditions.
- **Adapters (AMS/AM/AQS/AQ/AL/EWH, 6.4):**
  - every 3,000 h or 6 months: running noise, leakage, condensation drain holes
  - at 10,000 h: rotational clearance and coupling ring
  - oil seal: 10,000 h for NBR/FKM seals, 20,000 h for Premium Sine Seal
- **AD input shaft (6.5):** 3,000 h / 6 months as above; oil seal at 10,000 h.
- **Break-in oil change:** not an SEW requirement. Add it only if Engineering asks (template rule).

## Checking the oil level and changing the oil (manual 6.6)
**Which procedure applies** (code letter by gear unit, M1–M6):
- **A, with oil level plug:** R..37–167 and RX (R..47/57 use B in some mounting positions; check the manual's table on p. 139), F..37–157, K..39/49, K..37–187, S..47–97
- **B, with a cover plate instead of an oil level plug:** R..07–27, F..27, W..10–30, W..19–59
- **C, neither plug nor cover plate:** K..19/29, S..37
- **D/E:** W..37/47

**Key steps for code A:**
1. Lock out, and let the unit cool.
2. Find the oil level plug and breather on the mounting-position sheet.
3. Slowly remove the level plug. A little oil may run out; that is normal.
4. If the oil is low, top up with the same oil through the breather bore up to the lower edge of the level bore.
5. Refit the plugs at the torques above.
6. Check the oil condition via the drain plug. Change the oil if it is heavily contaminated, even if the interval hasn't been reached.

- **Pivoted mounting position:** the oil level can't be checked. The unit ships correctly filled; use the nameplate quantity when changing the oil.
- **Startup (ch. 5):** check the oil level for the mounting position (or the sight glass); remove transport protection; check rotation decoupled; keep plugs and breather accessible.
- **Pseudo-leakage:** a small amount of oil at a shaft seal during run-in, or a film of moisture at the dust lip, is normal. Wipe it with a lint-free cloth and keep watching.

## Fill quantities (manual 8.2.3)
The manual's fill quantities are guide values by mounting position and vary with stages and ratio. **Use the quote / nameplate quantity, never the guide table**, and check at the level plug. Changing the mounting position requires a different fill and SEW consultation; otherwise the warranty is void.

## Extended storage (manual 8.1; O&M storage section)
- **More than 9 months:** SEW recommends the "extended storage" design. It has VCI anti-corrosion in the oil, effective −25 to +50 °C, and treated shaft ends and flanges. Keep the unit sealed until startup.
- **Temperate climate (USA):**
  - packed in containers with desiccant and a moisture indicator: up to 4 years, roofed, protected from rain, snow and shock, with regular checks of packaging and humidity indicator (RH < 50 %)
  - open storage: roofed and enclosed at constant temperature and humidity (5–50 °C, RH < 50 %), no sudden temperature changes, filtered ventilation, no aggressive vapors, no shocks; 2 years or more with regular inspections for cleanliness, damage and corrosion protection
- **Store gear units in their mounting position** (SEW recommendation).

## Troubleshooting (manual 9.1, selected)
| Symptom | Likely cause | Action |
|---|---|---|
| Regular grinding/meshing noise | Bearing damage | Check oil condition; change bearings |
| Knocking noise | Gearing irregularity | Contact SEW (send an audio recording) |
| Noise after mounting | Housing deformed when tightened, or soft foundation | Check mounting; stiffen the foundation |
| Irregular noise | Foreign objects in oil | Check oil; stop the drive; contact SEW |
| Oil at cover | Cover seal leaking or defective | Tighten cover screws; contact SEW if it persists |
| Slight oil at oil seal during run-in / moisture film at dust lip | Pseudo-leakage | Not a fault; wipe and monitor |
| Oil from oil seal, flange or motor | Seal defective, overfilled, or unit not vented | Check oil level and venting; check seals; consult SEW |
| Oil from breather valve | Overfilled, wrong mounting position, or frequent cold starts (foaming) | Correct the oil level; install the breather correctly |

## Mounting and installation data (in the INSERT PDF; summary)
- **Footed reducers (GM-019-01):**
  - ambient 0–40 °C (32–104 °F), free airflow, access to drain/level/breather plugs
  - mounting surface flatness ≤ 0.004 in (sizes 87 and smaller) or ≤ 0.008 in (97 and larger)
  - use dowel pins or a tightening bar where chain or belt side pull acts
- **Installing shaft components (GM-022-01):** never hammer onto shafts; use the tapped hole in the output shaft.
  - Inch thread by shaft diameter: 0–13/16 in → 1/4-20; 7/8–15/16 → 5/16-18; 1–1-1/8 → 3/8-16; 1-1/4–1-3/8 → 1/2-13; 1-1/2–1-7/8 → 5/8-11; 2–3-1/4 → 3/4-10; 3-3/8–4-3/4 → 1-8.
  - Metric: see the PDF.
- **Bolt sizes and torques (4-2014 note):** mounting-hole and bolt diameters by unit (e.g. K87/R97/S87: 3/4 in or M20; K97/R107/S97: 7/8 in or M24). Minimum bolt class 8.8 / SAE grade 8. Bolts must protrude past the nut by at least one bolt diameter. Flange and torque-arm bolt torques are in the PDF.
