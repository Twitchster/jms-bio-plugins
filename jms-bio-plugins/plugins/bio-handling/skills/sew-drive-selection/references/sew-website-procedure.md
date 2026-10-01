# SEW DriveConfigurator — Browser Procedure

Verified against DriveConfigurator Release 26.7 on the US site, Sep 30 2026. The site is an ASP.NET app with server postbacks; expect each change to reload parts of the page.

## Which SEW tool

- **Use: DriveConfigurator → Gearmotors → AC gearmotors (catalog search by HP, rpm and fB).**
  URL: `https://www.seweurodrive.com/os/catalog/easy.aspx?id=default_acgearmotor&language=en_US&country=US`
  Entry page (all products): `https://www.seweurodrive.com/os/catalog/dispatcher.aspx?country=US&language=en_US`
- **Explosion-proof units:** entry page → Explosion-proof designs → AC gearmotors (`easy.aspx?id=default_atexmotor…`). Use only when the area classification allows SEW (max Class I Div 2) and the PE agrees.
- **Don't use SEW "Drive Selection"** (`/os/ds/`) for screws. Its applications are only Hoist, Trolley, Rotary table, and Roller, Chain and Belt conveyor. It has no screw conveyor or live bottom. Its Belt conveyor application may be a cross-check for Bio-BELT, but the catalog search remains the primary method.
- No login or registration is needed for either tool.

## Page mechanics (important)

- **Cookie banner:** a cookie banner appears at the bottom, stating that closing it accepts cookies. Don't click "Okay" unless the user has agreed. The search, variants, options and summary all worked with the banner left open.
- **Stale refs:** element refs go stale after every postback. After each change, re-read the page (`read_page` interactive, or `find`) before the next click.
- **Numeric fields** (Infragistics editors) ignore programmatic value setting. For each field:
  1. Focus and select it via JavaScript by element id.
  2. Type the value with real keystrokes.
  3. Press Tab.
  4. Wait about 4–5 s for the postback.

  Field ids on the Search step (current release):

  | Field | Element id |
  |---|---|
  | Motor power P [HP] | `igtxtctl00_ctl00_MainContent_tcTabControlArea_tab_Data_UltraNumericEditorMotorLeistungTextBox` |
  | Torque Ma [lb-in] | `…_UltraNumericEditorDrehmomentTextBox` |
  | Output speed na [rpm] | `…_UltraNumericEditorAbtriebsdrehzahl` |
  | Gear ratio i | `…_UltraNumericEditorUebersetzungTextBox` |
  | Service factor fB | `…_UltraNumericEditorBetriebsfaktor` |

  The `…` prefix is `igtxtctl00_ctl00_MainContent_tcTabControlArea_tab_Data_`. If the ids have changed, list the visible text inputs with JavaScript and match them by the label in their table row.
- **Dropdowns** (gear unit design, motor type, country, IE class, poles, duty, adapter, ambient) accept `form_input` with the option text. Each selection triggers a postback.
- The page opens with the last session's values (e.g., an R97 at 20 HP). Set every field; don't rely on the defaults.

## Step 1 — Search tab

Set these fields:

| Field | Value |
|---|---|
| Gear unit design | Per §5 of the JMS standard: Bio-SCREW F (K uncommon) · Bio-BELT K · Bio-LIVEBOTTOM F or K · Bio-LEVELING SCREW F (or FAS unit) |
| Motor type | DR.. AC motor |
| Country/area of use | USA (UR 60 Hz), or Canada (CSA 60Hz) for Canadian jobs |
| Motor power P [HP] | calc/design HP. Leave torque blank unless searching by torque. |
| Output speed na [rpm] | calc rpm (leave ratio blank) |
| Service factor fB | required fB |
| International efficiency class | IE3 (JMS std) unless spec'd |
| Number of poles | 4-pole |
| Duration factor | S1-100% |
| Frequency inverter operation | **Always check** (JMS standard: all SEW motors are inverter duty; checking sets thermal class F and adds thermal protection) |
| Adapter | Without (an adapter is only for non-SEW motors → go to SEW) |
| Ambient temperature max. | **"No thermal calculation"** (required by the JMS standard to proceed). Ambient >40 °C or a spec'd thermal calc → contact SEW; don't pick +40/+60 °C here. |
| Especially low output speeds | **Unchecked.** If it seems needed → contact SEW (JMS standard). |

**Search tolerances** (shown in the tolerance pop-ups): power −20%/+50%, torque −20%/+100%, speed −20%/+50%, fB −20%/+200%.

The results table has columns: Designation, Efficiency class, P [HP], na [rpm], Ma [lb-in], i, fB, nMot [rpm], Cyclic duration factor. It is paged, and the rows-per-page setting can be raised to 100. Read all pages, or at least everything with fB ≥ target.

**Filter yourself.** In testing, a 3 HP / 20 rpm / fB 1.4 search returned FA77 units at fB 1.35 and 1.15.

To select a row, click it. The header designation updates; confirm it before continuing. Then click "Next".

## Step 2 — Variants tab

Set these fields:
- Mounting position: M1–M6 per layout.
- Pivoting angle: none unless inclined mounting requires it (affects oil fill).
- Built-in type (F series examples):
  - FA.. hollow shaft; FAF.. B5 flange + hollow; **FAZ.. B14 flange + hollow shaft (JMS standard for Bio-SCREW, live bottom, leveling screw)**
  - FH/FHZ shrink disk; FV splined; FT TorqLOC
  - F.. foot; FZ.. B14 flange solid shaft
  - **FAS.. Screw Conveyor Unit**
  - K series has the analogous KA / KAF / KAZ / KH… Bio-BELT = KA hollow shaft with torque arm.
- Hollow shaft bore: choose the bore equal to the calc shaft diameter. Example: FA77 offered 50 mm, 1.938 in and 2.000 in. If the needed bore isn't offered, go back and select a different size.
- Torque arm: rubber buffers where the design uses a torque arm (Bio-BELT).
- Terminal box position 0° and cable entry X, unless the layout needs otherwise (keep clear for maintenance; belt conduit box not on the conveyor-frame side).
- Digital motor interface: without.

## Step 3 — Options tab

The option groups are: Extended warranty; Corrosion and surface protection; Base / top coat; Output; Motor voltage; Multi-range voltage; Brake; Thermal class; Degree of protection; Temperature sensor; Encoder; Connector; Ventilation; Backstop; Other motor options; Housing material; Shaft; Safety cover; Lubricant; Oil seal; Reduced backlash; Joint bonding; Breather valve; Oil sight glass.

- Set each group per §4 of `jms-sew-selection-procedure.md`. If an option isn't offered, leave a note for the SEW quote instead of choosing something else.
- Site defaults seen: IP54, base/top coat 3020 Traffic red, standard options. These **do not** meet the JMS standard (IP66; US13 Stainless Steel Gray + OS4).

## Step 4 — Summary tab

- Record the technical data table. Fields include:
  - rated motor speed, output speed, overall ratio, output torque, **Service factor SEW-FB**, mounting position, coat, terminal box, cable entry, hollow shaft, design type
  - **Permitted output overhung load**, lubricant quantity
  - motor power, duty, IE class, efficiencies, voltage, connection, wiring diagram, rated current, cos φ, thermal class, protection type
  - inertia, net weight, selected options list
- Available links: CAD data, CAE data, Technical documentation, Product data. Downloads need the user's permission.
- **Never click** "Add to shopping cart", Forward, Save as template, Request product, or Order product.

## Sample from testing (for sanity-checking the procedure)

Search: F, DR AC, USA UR 60 Hz, 3 HP, 20 rpm, fB 1.4.
- Qualifying rows: FA77DRN100LM4 i = 85.52, 21 rpm, 9,030 lb-in, fB 1.45; i = 75.02, 23 rpm, fB 1.70; FA87DRN100LM4 i = 88.01, 20 rpm, fB 2.9.
- The FA77 summary showed permitted overhung load 2,880 lb, lubricant 1.55 gal, 8.4/4.2 A at 230/460 V, 200 lb.

This is an example only; not a recommendation.
