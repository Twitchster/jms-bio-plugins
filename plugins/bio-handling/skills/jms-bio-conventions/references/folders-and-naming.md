# Folders, Tools and Naming

## Project drive

`S:\` = `\\Jms-clt-fs01\projects` (VPN needed remotely). Path pattern: `S:\<YY> PROJECTS\<proj> <City, ST>\`

Top-level project subfolders in common use:
- `03 Engineering\` (standard below)
- `04 Drawings\` — `02 Approved for Submittal`; `03 Drawing Checks\01 Submittal Drawings`; `03 Drawing Checks\03 Fabrication Drawings\Check Packages`
- `05 Submittals\<equipment>\Rev X\` (with `Customer Response`)
- `07 Shop & Field Docs\` — final sales BOMs (`Sales BOMs`)

### 03 Engineering folder standard (May 2026)

| Folder | Contents |
|---|---|
| 00 Project Management | PM files |
| 01 Calculations\<Product>\Process | Current process calcs only; superseded → `Old` |
| 01 Calculations\<Product>\Structural | Structural incl. anchorage; superseded → `Old` |
| 02 PE\Review | Sent to the stamping PE (Element 30) |
| 02 PE\Reports / Drawings / Models | Returned stamped reports, stamped drawings, models; superseded → `Old` |
| 03 Vendor\<Product>\Quotes | By equipment type/brand |
| 03 Vendor\<Product>\Technical / Models / Drawings | Vendor calcs, 2D, submittals, models |
| 04 Epicor | Not for engineers |
| 05 Design | Designers; design-review notes |
| 06 Eng Sub\<Product>\Rev A… | Everything the PM needs for a submittal: calc reports, datasheets, PE reports |

PMs must also file vendor info correctly.

## Tools and shared locations

- Bio-HANDLING Tools: `\\JMS-CLT-FS01\JMS ENGINEERING\Bio-HANDLING Tools` — Bio-SCREW calculator (updated Jun 2026), Screw Conveyor Thrust Calculator, Bio-LIVEBOTTOM calculator with the LiveBottom Calculation Procedure (Sep 2026), gate calculator. Lifting lug calc sheet is on the Engineering drive.
- The JMS screw conveyor calculator's pneumatic actuator section is inaccurate and limited to cylinders under 4".
- Standards: `\\JMS-CLT-FS01\JMS ENGINEERING\Standards\External Standards` (e.g., ASME Y14.5-2018) and `...\Standards\Internal Standards\Modeling & Detailing` (Designer Guideline).
- Training: `\\JMS-CLT-FS01\JMS ENGINEERING\Training`; Bluebeam Studio guide at `\\JMS-CLT-FS01\COMPANY\Systems Training`.
- Supplier data: `\\JMS-CLT-FS01\PROJECTS\Supplier Data`. Sales product info: `\\JMS-CLT-FS01\SALES\Products\5. Bio-HANDLING`.
- SolidWorks PDM standards: `C:\_EPDM_JMS\SOLIDWORKS STANDARDS` ("Get Latest" before running macros).
- Egnyte is used to exchange RISA models/reports with Element 30.
- Engineering subscriptions: ASTM Compass, AWS Standards eLibrary, RISA, Hilti PROFIS, CompanyCam.
- Project Blueprints/Bluesheets: SharePoint Bio-HANDLING Product Unit > General > Bio-BLUEPRINTS\<year>.
- JMS-STATUS.xlsm: SharePoint ProductDevelopment. Use the Excel desktop app, online only (no offline copies), and work only in your own view.

## Product designators (for projects submitted after Mar 23 2026)

| Code | Product | Code | Product |
|---|---|---|---|
| BBC | Belt conveyor | BLB | Live bottom |
| BRB | Receiving bin | BMS | Misc |
| BBE | Bucket elevator | BSC | Screw (was CS/LS/FS) |
| BDG | Diverter | BSL | Silo |
| BDC | Drag conveyor | BRL | Rotary leveler |
| BSF | Sliding frame | BHP | Hopper |
| BSG | Slide gate | BWG | Wedge gate |

Re-ordered parts get new part numbers when the old P/Ns are tied to existing POs (e.g., SA01 → SA11).
New purchased P/Ns (5xxxxx) are created as SolidWorks models first, then CADLinked to Epicor; Epicor-only numbers get overwritten. Epicor part numbers can't contain spaces. Never change an existing part description.

## Drawing and BOM text rules

- Follow ASME Y14.5. Weldment sheet 1 shows only weld-relative dimensions and weld callouts; part details go on later sheets. Keep all sheets together with the job traveler.
- Weld callouts carry sizes. Hole dimensions to three decimal places.
- No fractions on machined-part prints. Decimals under 1" need a leading zero (0.005", not .005") for the ballooning software.
- Finish notes (polish, blast, etc.) go in the drawing NOTES section, never only in the model description or metadata.
- Sheet-metal BOM callouts read gauge (e.g., "11GA"), not only decimals. Note: the updated sheet-metal macro omits gauge from the size description, so check the BOM text.
- Hardware descriptions include the surface finish (e.g., HDG).
- UHMW and neoprene are modeled as sheet metal with the gauge table.
