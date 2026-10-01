# Source Map: which document holds which information

**How to use:** find the information needed, then ask for the primary source (and the fallback if the primary may not have it).

**Section numbers** are typical CSI MasterFormat numbers seen on wastewater jobs. They vary by project and engineer. Find the real number from the spec table of contents or from the cross-reference in the equipment section; never tell the user a section number as fact without seeing it.

**Locations:**
- JMS: `S:\<YY> PROJECTS\<proj> <City, ST>\` (not reachable via connector; ask the user to attach)
- SharePoint: Bio-BLUEPRINTS, JMS-STATUS (connector-searchable)
- Outlook: project threads (connector-searchable)
- Outlook Public Folders: project email archive (not reachable via connector)

## 1. Contract / specification requirements

| Information needed | Primary source → section to read | Fallback | Usually at | M365 search terms |
|---|---|---|---|---|
| Equipment scope, quantities, tags | Equipment spec section, Part 1 "Summary/Scope" + equipment schedule | Contract mechanical drawings (M-series); JMS proposal/PO | Contract spec PDF from PM; `05 Submittals` | `<proj> spec`, `<proj> section` |
| Capacity, duty, operating hours | Equipment spec Part 1 "Design/Performance Requirements"; equipment data sheet/schedule | Process drawings, P&IDs; Bio-BLUEPRINT bid notes | Spec; Blueprint | `<proj> capacity`, `design criteria` |
| Material properties (bulk density, % solids, grit, temperature, flow behavior) | Equipment spec design criteria | Upstream dewatering or dryer vendor data (centrifuge/press/dryer submittal); Solids Handling Technologies test report if one exists | Spec; `03 Vendor\...\Technical` | `<proj> cake solids`, `density` |
| Motor requirements (SF, NEMA design, efficiency, inverter duty, thermostats/thermistors, heaters, voltage, enclosure) | Equipment spec Part 2 "Drives/Motors" **and** the general motor section it references (often Div 26, 40, 43 or 46, e.g., "Common Motor Requirements") | Electrical drawings (motor schedule, one-line); EoR electrical comments | Contract spec | `<proj> motor`, `service factor`, `inverter duty` |
| Gear reducer requirements (AGMA class, SF, bearing life) | Equipment spec Part 2 "Drive units" + general reducer section if referenced | — | Spec | `<proj> reducer`, `AGMA` |
| Hazardous-area classification (Class/Div, group) | Electrical area classification drawing (E-series), or electrical general notes | Equipment spec; NFPA 820 table in spec; EoR comments | Contract drawings | `<proj> hazardous`, `Class I Div`, `area classification` |
| Seismic parameters (code edition, SDC, Ss/S1/SDS, Ip, Ie, Risk Category) | Structural general notes drawing (S-001/S-0.1) | Seismic requirements spec section (Div 01 or 13 48 xx); geotechnical report | Contract drawings | `<proj> seismic`, `SDC`, `importance factor` |
| Wind, snow, roof live loads | Structural general notes | Equipment or building spec | Contract drawings | `<proj> wind speed` |
| Concrete strength, pad dimensions, anchor type (cast-in vs post-installed), edge distances | Structural drawings (plans/details) + general notes | Contractor RFI response; field measurements | Contract drawings; RFIs | `<proj> anchor`, `f'c`, `pad`, `RFI` |
| Wall construction for anchorage (grouted vs hollow CMU, concrete) | Architectural wall sections / structural masonry notes | Contractor confirmation by RFI | Contract drawings | `<proj> CMU`, `grout` |
| Materials of construction (304/316, liners, hardware) | Equipment spec Part 2 "Materials" / schedule of materials | General metals/fastener sections (Div 05) | Spec | `<proj> stainless`, `316` |
| Coatings, surface prep, passivation/pickling | Coatings section (09 96 xx) + equipment spec "Finishes" | — | Spec | `<proj> coating`, `09 96`, `passivation` |
| Domestic material / BABA / AIS | Division 00/01 (Supplementary Conditions, Product Requirements, funding-agency clauses) | PM or contract; Quality (BABA letter) | Contract docs | `<proj> BABA`, `domestic` |
| Gate pressure rating, leakage, actuator requirements | Equipment spec gate paragraphs + any referenced gate section (e.g., 40 05 59.xx) | EoR comment history | Spec | `<proj> slide gate`, `psi` |
| Controls scope, control philosophy, I/O, signals, PLC by whom | Instrumentation & controls sections (Div 40 90 xx / control strategies / loop descriptions) + P&IDs (I-series) | Electrical one-lines; EoR controls comments | Spec + drawings | `<proj> control strategy`, `P&ID`, `PLC` |
| Submittal contents and format | Equipment spec Part 1 "Submittals" + 01 33 00 | PM | Spec | `<proj> 01 33 00` |
| O&M contents, closeout forms | 01 78 23 (O&M data) / 01 33 00 closeout forms + equipment spec O&M paragraph | Contractor's closeout checklist | Spec; contractor email | `<proj> O&M`, `closeout`, `maintenance summary` |
| Shop tests, field tests, performance test, startup/training days | Equipment spec Part 3 "Field Quality Control / Startup / Training" + 01 75 xx/01 79 xx | — | Spec | `<proj> performance test`, `startup` |
| Warranty terms | Equipment spec Part 1 "Warranty" + General Conditions | Subcontract/PO | Spec; contract | `<proj> warranty` |
| Changes after bid | **Addenda** and conformed spec | RFI log; change orders | PM / contractor | `<proj> addendum`, `conformed` |

## 2. Project status and customer feedback

| Information needed | Primary source | Fallback | Usually at | M365 search terms |
|---|---|---|---|---|
| Latest EoR comments and required actions | Submittal Return Notice + comment file | Blueprint Submittal Comments tab | Outlook; `05 Submittals\...\Customer Response` | `<proj> Submittal Return Notice`, `R&R` |
| What JMS sold and exceptions taken at bid | JMS proposal/quote + customer PO/subcontract | Bio-BLUEPRINT bid notes | Sales (L:\), Blueprint on SharePoint | `<proj> proposal`, `PO` |
| Open items, responsibilities | Project Bio-BLUEPRINT | Approval Transition key takeaways email | SharePoint Bio-BLUEPRINTS\<year> | `<proj> Blueprint`, `key takeaways` |
| Milestones, ship dates, PM/PE/designer | JMS-STATUS.xlsm | PM | SharePoint ProductDevelopment | `JMS-STATUS` |
| Field conditions, as-found dimensions | Contractor RFIs, field measurements | CompanyCam photos; field service reports | Outlook; CompanyCam | `<proj> RFI`, `field` |
| Quality issues and history | Babtec complaint/NC record | Related email thread | Babtec | `<proj> Babtec`, complaint ID |

## 3. JMS engineering and design data

| Information needed | Primary source | Fallback | Usually at |
|---|---|---|---|
| Current JMS drawings and revision | PDM / Flatter Files released drawings | `04 Drawings\02 Approved for Submittal` | PDM; S:\ |
| Approved design (governs O&M) | Approved submittal "AS - <proj> - <section>" | Last submittal Rev in `05 Submittals` | S:\ |
| Blank JMS calc templates (Bio-BELT REV 4.7, Screw Process REV 21) | Shipped in the plugin: `conveyor-calcs/templates/` | Bio-HANDLING Tools share (newer revisions) | Plugin; `\\JMS-CLT-FS01\JMS ENGINEERING\Bio-HANDLING Tools` |
| Process calcs (HP, torque, capacity, shaft) | `03 Engineering\01 Calculations\<Product>\Process` (current version) | `06 Eng Sub\<Product>\Rev X` | S:\ |
| Structural calcs / RISA model | `01 Calculations\<Product>\Structural`; RISA file | `02 PE\Reports` (stamped) | S:\ |
| Hopper/silo design head, capacity, geometry | Hopper/silo GA + design calc | Tank Connection (or other silo vendor) drawings | S:\ `03 Vendor` |
| BOM, purchased parts, as-shipped config | Sales BOM in `07 Shop & Field Docs\Sales BOMs` | Epicor sales order; Flat BOM report | S:\; Epicor |
| Fab check comments | Check package + `JMS-DET-F-<proj>.xlsx` | Bluebeam Studio session | `04 Drawings\03 Drawing Checks` |

## 4. Vendor / purchased-component data

| Information needed | Primary source | Fallback | Usually at | M365 search terms |
|---|---|---|---|---|
| Motor data (HP, FLA, SF, frame, enclosure, nameplate) | Motor datasheet in vendor quote/submittal (Baldor via SEW) | SEW quote dimension sheet | `03 Vendor\<Product>\Technical` | `<proj> Baldor`, `SEW quote` |
| JMS SEW standard options and gearbox type by product | JMS Engineering Standard "SEW Gearmotor/Gearbox Selection" (in plugin: `sew-drive-selection/references/jms-sew-selection-procedure.md`) | Director of Engineering / standard owner (DED) | Plugin; `\\JMS-CLT-FS01\JMS ENGINEERING\Standards\Internal Standards` (confirm location) | `SEW selection procedure` |
| Gearbox data (ratio, torque, mounting position, oil qty/type, bore, torque arm) | SEW quote/order confirmation + SEW catalog (torque-arm dims) | SEW (District Sales Eng.) | `03 Vendor` | `<proj> SEW`, order number |
| Screw fabrication details, flights, liners, runout, test | TCC/Martin approval drawings + shipment docs (photos, inspection, video) | Weekly TCC project update email | `03 Vendor\...`; SharePoint TCC folder | `<proj> TCC`, `Martin`, SO number |
| Actuators (model, stem, open time, wiring) | Rotork / AFP quote + datasheet | Vendor rep | `03 Vendor` | `<proj> Rotork`, `AFP` |
| Bearings, seals, couplings | Vendor datasheets (Dodge, Cinch-Seal, etc.) | Vendor rep | `03 Vendor` | vendor name + `<proj>` |
| Lubrication and maintenance intervals | Vendor O&M manuals (SEW, Baldor, TCC, actuator, sensor) | Vendor website manual (ask the user to download) | `03 Vendor\...\Technical` | `<proj> O&M` + vendor |
| Instruments/sensors (rating, cable length, wiring) | Instrument datasheet in submittal | Vendor rep | `03 Vendor`; submittal | model number |
| Load cells, calibration | Kistler Morse data + calibration report | Field service report | `03 Vendor`; email | `<proj> Kistler`, `calibration` |
| Stairs/platform design | Fabricator stamped calc package + shop drawings | EoR shop-drawing review comments | `03 Vendor`; email | `<proj> stair`, fabricator name |
| BABA / domestic certificates | Vendor certificate / Quality BABA letter | Quality (Director of Quality) | `03 Vendor`; email | `<proj> BABA certificate` |
