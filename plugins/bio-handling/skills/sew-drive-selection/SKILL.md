---
name: sew-drive-selection
description: >
  This skill should be used when a JMS Bio-HANDLING engineer asks to "select the SEW gearmotor",
  "pick the motor from the calc sheet", "size the drive on the SEW website", "run the SEW
  configurator", "find an SEW gear unit for this screw / belt / live bottom", "use the calculator
  results to select the reducer", "what SEW options do we use", or shares a Bio-SCREW,
  Bio-LIVEBOTTOM, leveling screw or belt conveyor calculation sheet and wants a JMS-compliant
  gearmotor selection from SEW-EURODRIVE's online DriveConfigurator.
metadata:
  version: "0.4.0"
---

# SEW Gearmotor Selection from Calculation Sheet Data

Take the drive requirements from a JMS calculation sheet, apply the **JMS SEW Gearmotor/Gearbox Selection standard** and the project spec, and search SEW-EURODRIVE's online **DriveConfigurator** (AC gearmotors) in the browser. The output is a documented, JMS-compliant selection that the PE confirms with SEW.

**Governing sources, in order:**
1. Project specifications.
2. `references/jms-sew-selection-procedure.md` (the JMS standard: every option, product-type gearbox choice, contact-SEW triggers). Note that it is Rev 0 and not yet approved.
3. JMS lessons in `design-checks` → `references/drives-motors.md`.

Load `jms-bio-conventions` for naming and folders. Use `source-documents` for anything missing.

**Scope:** this is a catalog pre-selection, not an engineered quote. SEW's quote and order confirmation govern. The skill never orders, requests a quote or adds anything to a cart on the SEW site.

## Step 1 — Extract requirements from the calc sheet

1. Run `scripts/extract_calc_values.py <file.xlsx>` to list labeled numeric cells with cached values. If the cached values are empty, ask the user to open and save the file in Excel, or send a PDF of the results page.
2. Map the fields in `references/calc-field-map.md`: design HP, rpm (and VFD range), torque, shaft diameter, axial thrust, overhung load, incline, duty hours and starts. **Cite the sheet and cell for every value.** On first use of a calculator version, show the mapping table and have the user confirm it.
3. Check the calculator version. Bio-SCREW calcs made before the Jun 2026 update used lift HP factor 1.3 (now 1.7) and an old shaft table. Flag this; don't silently re-compute.
4. Compute in code:
   - Output torque Ma [lb-in] = 63,025 × P [HP] / n [rpm], using design HP at design rpm.
   - Required fB = the spec value (AGMA Class 2 → ≥1.4, Class 3 → ≥2.0), else the JMS minimum 1.4. **Don't accept candidates above fB 3** (the standard warns this can be detrimental to the gearbox).
   - Motor HP: what the calc and fabricator quote call for. Don't oversize.
   - Duty: S1-100% if running ≥8 h/day. Flag frequent starts for review.

## Step 2 — Screen for "contact SEW" cases before searching

Per the JMS standard, these go to SEW directly. The configurator result, if run at all, is labeled **preliminary**:
- ambient >40 °C/104 °F, or the spec requires a thermal calculation
- elevation ≥2,000 ft
- "especially low output speeds" needed
- hazardous classification of any kind. SEW goes only to Class I Div 2. **Div 1 → an SEW motor can't be used.**
- grounding: conductive fleece required, or the spec demands Aegis rings (not possible with SEW → exception or other motor)
- a non-SEW motor needing an adapter
- bearing calculations required by the spec (give SEW the axial and overhung loads)
- reinforced-bearing decision (give SEW the thrust-calc value; a pillow block between the product and the gearbox usually means none)

Also pull the spec items that change options: voltage, thermistors vs thermostats, synthetic oil, sight glass, encapsulated terminal box, IE class, poles, SF/AGMA class, coatings. Use `source-documents` if the spec isn't in hand.

## Step 3 — Search and configure on the SEW DriveConfigurator

Follow `references/sew-website-procedure.md`, which includes the exact field mechanics for the site. In summary:

1. Use the person's preferred browser, and read that browser's skill first. Open AC gearmotors; no login is needed.
2. **Search tab:**
   - gear unit design per product (§5 of the standard: Bio-SCREW F, K uncommon; Bio-BELT K; live bottom F or K; leveling screw F or FAS)
   - DR.. AC motor, USA (UR 60 Hz), HP, output rpm, fB
   - IE3, 4-pole, S1-100%
   - **Frequency inverter operation checked** (JMS good practice; sets thermal class F and thermal protection)
   - adapter Without
   - ambient **"No thermal calculation"**
   - especially-low-speeds unchecked
3. **Filter results yourself.** The site's tolerance returns units down to 80% of the requested fB. Keep rows with:
   - required fB ≤ fB ≤ 3
   - na within the acceptable range
   - Ma ≥ required torque
   - a hollow bore that matches the calc shaft

   Rank by smallest frame first, then fB nearest target. Keep the top 3.
4. **Variants tab:**
   - mounting position and pivot angle per layout (both affect oil volume)
   - built-in type per product: Bio-SCREW/live bottom/leveling **FAZ or KAZ (B14 + hollow)**; Bio-BELT **KA + torque arm**; FAS for a CEMA screw-conveyor unit
   - hollow bore = calc shaft
   - terminal box 0° and cable entry X unless blocked (Bio-BELT conduit box not on the conveyor-frame side)
   - digital interface Without
5. **Options tab:** set every option per §4 of the standard. The site defaults are **not** JMS-compliant: IP54 and 3020 Traffic red appeared by default and must be changed to **IP66** and **US13 Stainless Steel Gray + OS4**. If an option isn't offered, note it for the quote; don't substitute.
6. **Summary tab:** record the technical data (type designation, fB, torque, permitted overhung load, oil quantity, current, weight, options). Never click "Add to shopping cart", Forward, Save as template, Request or Order. Downloading a dimension sheet or CAD file needs the user's permission.

## Step 4 — Checks and output

Run the checks in code and report pass/fail:
- **Speed:** actual na vs calc rpm. If they differ by more than about 5%, re-check capacity/fill in the calc.
- **Torque and fB:** required ≤ fB ≤ 3. Ma ≥ required.
- **Bore and mounting:** bore = shaft. Mounting position and pivot angle match the layout.
- **Loads:** permitted FRa ≥ calc overhung load. The axial load goes to SEW (the site shows no axial capacity).
- **Configuration compliance:** go option-by-option against §4 of the standard. List every deviation with its reason (spec-driven, or not offered).
- **Spec compliance:** NEMA design letter, SF, thermistors (recommend an exception; otherwise note that a panel relay is needed), grounding, oil type, IE class.

Deliverables:
1. **Selection summary** (.xlsx by default) with these sections:
   - Inputs (with calc cell references)
   - Derived requirements
   - Candidates table (designation, HP, na, Ma, i, fB, bore)
   - Selected configuration: every Search/Variants/Options value, each tagged [Spec], [JMS std §4/§5] or [Project]
   - Checks
   - Deviations and exceptions
   - SEW confirmations needed

   Name it `PROJ-PRODUCT_SEW-SELECTION_REVX`; it belongs in `03 Engineering\01 Calculations\<Product>\Process`.
2. **Draft email** to the SEW district sales engineer requesting a formal quote. Include the type designation, the full options list, loads for bearing checks, and the contact-SEW items. Use the JMS subject format and the project CC. Draft only; send only with the user's explicit approval.

## Rules

- Never enter credentials, accept terms, or submit anything on SEW's site. Ask before accepting the cookie banner; the whole flow has worked with it left open.
- The website may change. The procedure was verified against DriveConfigurator Release 26.7 (Sep 30 2026). If a screen differs, read the page and adapt, record the difference, and never guess what a field means.
- Every value in the output traces to the calc sheet (cell), the spec (paragraph), the SEW Summary page, or the JMS standard (section).
- Third-party vendors sizing SEW drives for JMS equipment (e.g., TCC) must meet the same standard. Use this skill's checks on their selections too.
