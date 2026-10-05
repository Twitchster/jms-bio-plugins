# O&M Required Documents, by Product

What to ask for when a user asks for an O&M for a project with a Bio-BELT, Bio-SCREW (shafted or shaftless), Bio-HOPPER, Bio-GATE or Bio-DIVERTER. Built from the drafter notes in the six JMS starting-point templates (`templates/`, written by the JMS technical writer, R. Nesman), Oct 2026.

**How to present it.** Show the user one batched list for the product(s) in the request:
1. Part A (every product), then the product's Part B list, then Part C if the product has an SEW drive.
2. Mark each item **Blocking** (can't draft that part without it) or **Non-blocking** (draft with a placeholder and an OPEN comment).
3. Drop the conditional items the user has already ruled out. Keep the rest with their "only if" condition, so the user can say "n/a".
4. After the list, show the product's **configuration facts**. Don't ask the user to answer them; say you will read them from the drawings, BOM and submittal and show your findings for confirmation before drafting.

**Location shorthand:** `S:\<YY> PROJECTS\<proj> <City, ST>\` is the project folder. "TW SharePoint" is the Technical Writing / Aftermarket Parts – Document Control SharePoint the templates point to. Locations are as the templates gave them in Oct 2026 and may move; if a file isn't where stated, ask the user rather than guess.

**Basis tags:** [Template] = stated in the template's drafter notes. [Judgment] = added by this plugin; verify.

---

## Part A — Every product

| # | Document | What it feeds | Usual location | Status |
|---|---|---|---|---|
| A1 | **Approved submittal** (latest "AS" revision, with the customer response) | Scope of Supply text and feature list; Field Service; Scope Exclusions; Clarifications (Diverter); starting spare-parts list; warranty period (often); catalog cuts for Appendix A; calculations list for Appendix C | `05 Submittals\<equipment>\Rev X\` | **Blocking** |
| A2 | **Latest GA, SA and FA drawing sheets, in a numerical revision** | Appendix B; spare-parts table (the GA table governs over the submittal list; ask the PM about discrepancies); customer tag numbers (drawing notes); shipping condition; anchorage details; which optional paragraphs apply | Flatter Files ("FF" in the templates) / PDM released drawings. An alphabetical revision means not released: ask Design | **Blocking** |
| A3 | **Engineering BOM** | Carbon steel vs stainless (keep or delete every "cross-contamination" passage); anchor type (adhesive anchors appear on the BOM); purchased components that need cat cuts | Epicor / drawing BOM; as-shipped sales BOM in `07 Shop & Field Docs\Sales BOMs` | **Blocking** |
| A4 | **Equipment spec section** (with addenda) and the **O&M paragraphs** it references (Div 01, e.g., 01 78 23 / 01 33 00) | Cover: spec section number, plant name, location, Engineer of Record; footer spec section; required O&M contents and closeout forms | Contract spec from the PM | **Blocking** for the cover and required contents |
| A5 | **Project identity**: JMS project number, customer, plant name, location (city, state), customer tag/serial numbers, O&M revision number and release date, drafting PE's initials | Cover; header (Location, JMS Project No.); footer (Prepared By); Appendix F revision history | Spec cover, drawing notes, PM. Ask for the initials; don't assume | **Blocking** |
| A6 | **Latest calculations** that appear in the submittal | Appendix C; "do not exceed design parameters" references | `03 Engineering\01 Calculations\<Product>\Process` and `\Structural` (current only, not `Old`) | Non-blocking for drafting; required for issue |
| A7 | **Vendor cat cuts plus installation, O&M and lubrication information** for every purchased component (the submittal usually has the cut sheet only) | Appendix A; maintenance and lubrication tables that say "refer to the manufacturer's information in Appendix A" | Submittal cat cuts + TW SharePoint `1 - O&M Creation Reference > Manufacturer Supplemental Info`; `Supplier Data` on S:\ | **Blocking** for each table row that cites it |
| A8 | **Anchor manufacturer (Hilti or other) cat cut and installation instructions** — every product except the Bio-DIVERTER (never anchored) and the Bio-GATE (template has no anchor text) | Section 4.1 and anchorage steps; Appendix A | Submittal; Hilti website/PROFIS output; `03 Vendor` | **Blocking** when anchors are in JMS scope |
| A9 | **Field service scope** (trips, days, what's included), if not explicit in the submittal | Field Service section; the "schedule JMS field service" paragraph in 4.1 (delete it if no field service) | Submittal; PM | Blocking if the submittal is unclear |
| A10 | **Warranty period** for this project | Policies > Warranty ("period of XXXXX") | Submittal, contract, or PM | Non-blocking (placeholder) |
| A11 | **JMS controls documentation** — only if JMS supplied controls | Appendix E; startup, shutdown and alarm references | Controls submittal; PM | Non-blocking; if JMS supplied no controls, App E says so |
| A12 | Startup reports | Appendix D | Not available for the first issue. Leave the placeholder | Not needed |

---

## Part B — Product-specific documents

### Bio-BELT (template `Bio-BELT_OM_Rev1_Starting_Point.docx`)

| # | Document | Needed when | What it feeds | Status |
|---|---|---|---|---|
| BB1 | **Belt cut sheet** (belt manufacturer data) plus the belt maker's maintenance and troubleshooting information | Always. If it's not in the submittal, request it [Template] | Appendix A; belt troubleshooting rows | **Blocking** |
| BB2 | **Belt splice method**: FA drawing note ("belt to be vulcanized" or "field spliced") | Always | Chooses the vulcanized or laced installation paragraph and the lacing maintenance row | **Blocking** |
| BB3 | **Splice kit cat cut and O&M** (typically Flexco; "375" = hinged) | Only if field spliced/laced | Appendix A; lacing inspection row | Blocking if laced |
| BB4 | **E-stop pull-cord switch installation instructions**, including wiring (not just the cut sheet) [Template] | Always (template assumes one) | E-stop install step; Appendix A | **Blocking** |
| BB5 | **Zero-speed switch installation instructions**, including wiring and calibration (not just the cut sheet) [Template] | Always | Zero-speed install and calibration steps; Appendix A | **Blocking** |
| BB6 | **Belt alignment switch installation instructions** (typically CCC Model TA; JMS keeps them in the Mfr Cat Cut folder and S:\ Supplier Data) | Only if alignment switches are on the BOM | Install step, safety text, PM row; Appendix A | Blocking if used |
| BB7 | **Plow cat cut, installation instructions, maintenance information**; for an electric actuator also limit-switch adjustment information | Only if a plow is on the BOM and is handwheel- or electrically actuated | Plow install and adjustment steps, PM and lube rows; Appendix A | Blocking if used |
| BB8 | **Gravity take-up counterweight weight** (on the drawings; else ask Engineering) and take-up design details | Only for a gravity take-up | Take-up installation and tensioning text | Blocking if gravity take-up |
| BB9 | **Idler manufacturer information** (Rex/Rexnord idlers need lubrication; Superior Moxie rolls don't) | Always (decides whether idler lube rows stay) | Idler lube and PM rows; Appendix A | **Blocking** |
| BB10 | **Drum pulley bearing lubrication information for every pulley bearing**: head/drive and tail; for a gravity take-up also the bend pulleys and the take-up pulley | Always | Lubrication table; Appendix A | **Blocking** |
| BB11 | **V-belt drive (Dodge) installation, tensioning, maintenance and lubrication information** | Only if a V-belt connects the gearmotor to the drive shaft (rare, e.g., 24001) | V-belt install and PM rows | Blocking if used |
| BB12 | **Dodge reducer maintenance and lubrication information** (type, quantity, interval) | Only if a Dodge reducer replaces SEW (rare) | Lubrication table; Appendix A | Blocking if used |
| BB13 | **Wash box** information | Only if a wash box is supplied | Wash box PM/troubleshooting row | Non-blocking |

Not covered by the template [Template]: chain-and-sprocket drives. If the drive uses one, flag it; tensioning, lubrication and maintenance text must be written and the template note says so.

### Bio-SCREW, shafted (template `Bio-SCREW_Shafted_OM_Rev0_Starting_Point.docx`)

| # | Document | Needed when | What it feeds | Status |
|---|---|---|---|---|
| BS1 | **Gearmotor installation instructions, including wiring** [Template] | Always | Drive installation step; Appendix A | **Blocking** |
| BS2 | **E-stop pull-cord switch installation instructions**, including wiring | Always (template assumes one) | E-stop install step; Appendix A | **Blocking** |
| BS3 | **Zero-speed switch installation instructions**, including wiring | Always | Zero-speed install step; Appendix A | **Blocking** |
| BS4 | **Hanger bearing cat cut and lubrication information** (TCC, CI or Screw Conveyor Parts; JMS usually specifies a style such as 226; plastic hangers need no grease but keep the wear row) | Only if hanger bearings are used | Hanger PM, lube and shutdown rows; Appendix A | Blocking if used |
| BS5 | **Automatic lubrication system refill instructions** | Only if an auto-lube system is supplied | Lube rows; Appendix A | Blocking if used |
| BS6 | **End (roller) bearing lubrication information** if not Dodge Type E / S-2000 (the template's 3-month NLGI #2 lithium-complex row comes from Dodge) | Only if a different bearing is used | Lube table | Non-blocking (check) |
| BS7 | Packing gland seal confirmation (drawings/BOM) | Always; template assumes packing glands | Packing gland PM and lube rows | Non-blocking |

### Bio-SCREW, shaftless (template `Bio-SCREW_Shaftless_OM_Rev1_Starting_Point.docx`)

BS1–BS3, BS5 and BS7 apply as above (hanger bearings don't exist on a shaftless screw). Also:

| # | Document | Needed when | What it feeds | Status |
|---|---|---|---|---|
| BL1 | **Zero-speed switch model.** The calibration procedure in Initial Startup is for the **Siemens Milltronics MFA 4P + MSP-12** only. Another switch: delete that step and use its manufacturer's instructions | Always | Initial Startup calibration step; Appendix A | **Blocking** |
| BL2 | **Liner details** from the drawings: UHMW liner segments and retainers (the template uses a ¼" wear limit) | Always | Liner installation step, liner replacement procedure, PM row | Non-blocking (verify) |
| BL3 | **Field-welded spiral joint confirmation** (SA/FA drawings): spiral shipped in sections with match marks and a flight alignment plate. The template's procedure uses 9018 rod and a 200–300 °F preheat; Engineering should confirm these for the spiral material [Judgment] | Only if the screw ships in pieces | Spiral field-weld procedure | Blocking if shipped in pieces |
| BL4 | **Hold-down details** (SA drawings) | Only if the screw has hold-downs | Troubleshooting row | Non-blocking |

### Bio-HOPPER (template `Bio-HOPPER_OM_Rev0_Starting_Point.docx`)

Scope rules [Template]: the template always includes a **live bottom with screws**, optionally a **leveling screw**; those screws need no separate Bio-SCREW O&M. A completely separate screw does. A **Bio-GATE gets its own O&M**; this one only references it.

| # | Document | Needed when | What it feeds | Status |
|---|---|---|---|---|
| BH1 | **Anchorage details** (drawings): cast-in-place vs drilled/cored after the pour | Always | Chooses the anchor installation paragraph | **Blocking** |
| BH2 | **Squareness tolerance on the FA sheets** (contact the designer if missing) | Only if the hopper ships in pieces | Assembly step | Blocking if shipped in pieces |
| BH3 | **Load disc / load stand installation and re-leveling instructions** (Kistler Morse; JMS copy on TW SharePoint `4 - Misc. Technical Writing Reference > ... > MFR Cat Cuts and O&M Manuals`) | Only if load discs/stands are supplied | Load disc install, leveling and wiring steps; Appendix A | Blocking if used |
| BH4 | **Level sensor cat cut with installation details and wiring** (typically Siemens SITRANS ultrasonic or radar) | Only if a level sensor is supplied | Sensor install and wiring steps; Appendix A | Blocking if used |
| BH5 | **Discharge gate documents**: knife gate cat cut and O&M (manual; DeZurik was the basis), **or** the separate JMS Bio-GATE O&M | Only if a discharge gate is supplied | Gate install step; startup and shutdown references | Blocking if a gate is supplied |
| BH6 | **Gearmotor installation instructions with wiring, for each drive** (live bottom screws and leveling screw may have separate gearmotors; include both) | Always | Install steps; Appendix A; lubrication tables | **Blocking** |
| BH7 | **E-stop and zero-speed switch installation instructions** with wiring | Always | Wiring step; Appendix A | **Blocking** |
| BH8 | **Hanger bearing cat cut and lube information** | Only if a hopper screw uses hanger bearings (uncommon) | PM and lube rows | Blocking if used |
| BH9 | **Automatic lubrication system refill instructions** | Only if supplied | Lube rows | Blocking if used |
| BH10 | **Drag chain conveyor VFD electronic shear pin information** (e.g., Hapman, in the "Manufacturer's Cat Cuts & O&M Info" folder) | Only if the hopper is part of a Bio-SYSTEM (dry system) with a drag chain conveyor | Added electrical inspection text | Blocking if applicable |
| BH11 | Bearing lubrication information if not Dodge Type E / S-2000 | Only if different | Lube table | Non-blocking |

### Bio-GATE (template `Bio-GATE_OM_Rev0_Starting_Point.docx`)

The template assumes an **electric actuator** (Rotork IQ3 basis, kept generic). Pneumatic, hydraulic or manual actuators need careful edits to Sections 4, 5 and 6 [Template]. No anchor text.

| # | Document | Needed when | What it feeds | Status |
|---|---|---|---|---|
| BG1 | **Actuator O&M manual** (installation, wiring, maintenance, lubrication or a statement that there is none, troubleshooting, limit-switch setup) | Always | Install, startup, PM, lube and troubleshooting references; Appendix A | **Blocking** |
| BG2 | **Actuator controls information**, which is often a separate document from the O&M manual | Always | Startup/shutdown and troubleshooting references; Appendix A | **Blocking** |
| BG3 | **Non-rising-stem bearing cut sheet and lubrication information** (type, interval, quantity) | Only for a non-rising stem (no bearing on a rising stem) | PM and lube rows | Blocking if non-rising stem |
| BG4 | **Seal arrangement** from the drawings (which sides take which seal length; drain present or not) | Always | Seal replacement procedure; drain troubleshooting row | Non-blocking (verify) |
| BG5 | **Host equipment O&M** (e.g., the Bio-HOPPER O&M) | Only if the gate is part of larger JMS equipment | Reference its scope and field service instead of repeating them (avoids double-counting service days) | Non-blocking |

### Bio-DIVERTER (template `Bio-DIVERTER_OM_Rev0_Starting_Point.docx`)

Rotork actuator basis; never anchored; gear units not typical [Template].

| # | Document | Needed when | What it feeds | Status |
|---|---|---|---|---|
| BD1 | **Inputs-page data**: JMS project no., location (city, state), tag no., plant name, spec no., Engineer of Record, customer, O&M rev no., O&M release date, Prepared By, **local JMS representative** (name, company, address, phone), **JMS Project Manager** | Always | The last-page input content controls; they feed the cover, header, footer, contact page and Appendix H by REF fields | **Blocking** |
| BD2 | **Actuator O&M manual** and **actuator controls information** (separate documents for Rotork), plus the **Rotork one-sheet wiring diagram** (Engineering usually provides it for the submittal) | Always | Appendix A: Supplemental Vendor Information; install, startup, PM and troubleshooting references | **Blocking** |
| BD3 | **Bearing cat cut plus maintenance and lubrication information.** Rarely in the submittal: send the BOM line item to Engineering and ask for it (some is on TW SharePoint manufacturer info) | Always | PM and lube rows; Appendix A | **Blocking** |
| BD4 | **Rotork right-angle gearbox lubrication requirements** | Only if the actuator has a right-angle gearbox | Replace the "sealed for life" sentence; add a lube row | Blocking if used |
| BD5 | **Downstream JMS equipment O&M** (e.g., the Bio-SCREW O&M), checked to make sure it covers attaching the diverter outlets | Only if the outlets connect to JMS equipment with its own O&M | Installation reference ("Refer to the separate JMS xxxxx O&M") | Non-blocking |
| BD6 | **Actuator assembly details** from the drawings | Only if the actuator ships unassembled (e.g., 23020 bifurcated chute) | New actuator assembly steps | Blocking if unassembled |
| BD7 | **Gear unit paragraph and data** (copy the paragraph from another product's template) | Only if a gear unit is supplied (not typical) | Storage section; lube | Blocking if used |
| BD8 | **Blank Comment & Response Log PDF** | Always | Appendix H | Non-blocking |

---

## Part C — SEW gear unit or gearmotor (Bio-BELT, Bio-SCREW, Bio-HOPPER; Bio-GATE/DIVERTER only if a gear unit is supplied)

| # | Document | What it feeds | Usual location | Status |
|---|---|---|---|---|
| C1 | **SEW quote or order confirmation** for each unit: type designation, **mounting position**, **lubricant volume and type**, and the note that the motor bearing shield was removed / oil added | Lubrication section (mounting position, oil quantity); the "motor bearings sealed for life" sentence. If the shield note is missing, tell the user to raise it with the drives contacts named in the template (Philip and Andy) | `03 Engineering\03 Vendor\<Product>\Quotes` | **Blocking** |
| C2 | **Current SEW catalog page with the mounting-position diagram** for that unit type and position | Image placed under the mounting-position legend | SEW website/catalog (download only with the user's permission) or the user | **Blocking** |
| C3 | **"FOR REFERENCE - SEW Closing Plugs.pdf"** | Plug thread size for the unit (red box around the table row) | JMS O&M reference files (location not stated in the templates; ask) | **Blocking** |
| C4 | **Current SEW operating instructions** for the gear unit series | Oil-plug tightening torque (Nm → lb-ft), lubricant tables. Template values come from the 02/2023 manual; check for a newer one | SEW website or `03 Vendor\<Product>\Technical` | **Blocking** |
| C5 | **Engineering's decision on a break-in oil change** (about 500 h) | Add the break-in row only if Engineering says so | Engineering | Non-blocking (default: omit) |
| C6 | **Non-SEW motor data** (e.g., Baldor cat cut with frame designation and regreasing data) | Motor regreasing rows only for a non-SEW, non-explosion-proof motor. "XP" in a Baldor frame = explosion proof; must also read Class II Div 1 (not Div 2); VECP is not XP | Submittal; motor vendor | Blocking if a non-SEW motor is used |
| C7 | **Non-SEW reducer** maintenance, lubrication and troubleshooting information | Only if the reducer isn't SEW. The screw templates then need SEW text removed throughout | Submittal; vendor | Blocking if used |

**A preliminary Product Data PDF from `sew-drive-selection` is not the quote.** Use it only as a flagged placeholder for mounting position and oil quantity until the SEW quote or order confirmation is in hand [Judgment].

---

## Configuration facts per product

Read these from the documents, then show the user a table of fact → finding → evidence (sheet/note/BOM line) before filling. Each one keeps or deletes template paragraphs.

### All products
- Mostly carbon steel or stainless? (BOM) → keep or remove every "cross-contamination" passage.
- Field service included? (submittal) → keep or delete Field Service paragraphs and the 4.1 scheduling paragraph.
- Anchors in JMS scope, and adhesive anchors on the BOM? → anchor paragraphs and the Hilti cat cut.
- Spare parts: GA table vs submittal list → use the GA table; ask the PM about differences.
- JMS controls supplied? → Appendix E content.
- SEW gearmotor, SEW reducer + other motor, or non-SEW? → lubrication-section options.

### Bio-BELT
- Shipped fully assembled, in sections, or in sections with supports attached (SA drawings).
- Take-up: gravity or screw (another type: ask Engineering).
- Drive: direct on the drive pulley shaft (typical), V-belt (rare) or chain (not covered).
- Splice: vulcanized or laced (FA notes).
- Sidewall belt? (A sidewall belt won't ship on a roll; delete roll-handling text.)
- Plow: none, manual handwheel, or electric actuator.
- Alignment switches, wash box, idler brand.
- Pulley bearings: one expansion and one fixed per shaft (drawings). If both are the same, notify Engineering.
- Take-up rollers assumed sealed for life; check the roller type.

### Bio-SCREW (shafted and shaftless)
- Shipped assembled or in pieces (SA/FA).
- Floor-mounted (keep the grout step) or hung from above (delete it).
- Hanger bearings (shafted only), auto-lube, packing glands, drain pipe (bottom of trough or low end plate), hold-downs (shaftless).
- Zero-speed switch model (shaftless calibration step is MFA 4P + MSP-12 only).

### Bio-HOPPER
- Ships in two pieces (upper assembled in the field, lower live bottom assembled) or fully assembled.
- Welded or bolted construction; roof (welded or bolted) or open top.
- Anchors cast-in-place or drilled/cored.
- Load discs/stands: none, on the floor under the columns, or on top of the columns.
- Leveling screw (horizontal screw at the top); installed in the field or shop-installed; open top allows lowering it in.
- Live bottom screws shafted or shaftless (liner and hold-down rows only for shaftless).
- Grizzly bars, transition chutes, flexible chutes, ladder, stairs, handrails, platform, pump loadout connection, bypass discharge chute.
- Discharge gate: none, knife gate, or JMS Bio-GATE; attached to the hopper or a transition chute.
- Separate gearmotors for live bottom and leveling screws.
- Part of a Bio-SYSTEM with a drag chain conveyor.

### Bio-GATE
- Actuator type (electric assumed).
- Stand-alone or part of larger equipment.
- Mounted between two items (repeat the connection steps) or one side only.
- Rising or non-rising stem; drain fitted.

### Bio-DIVERTER
- Two drop points (Figures 1–3) or three or more (Figures 4–6).
- Ships in sections or assembled.
- Downstream: stand-alone/existing plant equipment (repeat connection steps) or JMS equipment with its own O&M (reference it).
- Actuator pre-assembled; Rotork or other; right-angle gearbox.
- Clarifications in the submittal, or none.
