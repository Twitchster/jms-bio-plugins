---
name: jms-bio-conventions
description: >
  This skill should be used when a JMS Bio-HANDLING project engineer asks "where does this file go",
  "what's the file name format", "what should the email subject be", "what part number designator",
  "who checks this", "how does a submittal / fab check / Babtec ticket / change order work at JMS",
  or when any other bio-handling skill needs JMS folder paths, naming rules, product designators,
  drawing standards, workflow steps or roles. Load it alongside submittal-review, drawing-check,
  design-checks, om-manual, source-documents, sew-drive-selection and conveyor-calcs.
metadata:
  version: "0.5.0"
---

# JMS Bio-HANDLING Conventions

Shared company knowledge for Jim Myers & Sons (JMS) Bio-HANDLING project engineering. Apply these conventions whenever producing files, emails, drawings comments or recommendations for a JMS project.

## Core facts

- JMS divisions: **Bio-HANDLING** ("Bio": screws, belts, hoppers/live bottoms, silos, gates, drag conveyors for biosolids) and **Mega-TREATMENT** ("Mega": settlers, skimmers, VAC, FLOC, AIR, troughs).
- Product naming style: Bio-SCREW, Bio-BELT, Bio-HOPPER, Bio-LIVEBOTTOM, Bio-SILO, Bio-CHUTE, Bio-DIVERTER, Bio-DRAG, Bio-SCREW-PACTOR, Bio-SYSTEM, Bio-CONTROLS.
- Project numbers are `YYNNN` (e.g., 25034). Every project has an email group `<proj>@jmsequipment2.onmicrosoft.com`.
- Company policy: production does not start until there is an approved submittal.

## Email subject format

Use: `<proj>: <City, ST>, Bio-<PRODUCT>, <topic>` — e.g., `25034: Fond du Lac, WI, Bio-SILO, Stair anchor RFI`.
Minimum is project number + City, ST. Copy the PM and CC the project group address so the email files to the project folder. Fix the subject on external threads too. Keep separate submittals (e.g., hopper vs screw) on separate threads.

## File naming

Engineering files: `PROJECTNUMBER-PRODUCT_DOCUMENTTYPE_REVX`, all caps — e.g., `21020-HOPPER_ANCHOR_REV0`.
Part numbers: `project#-designator(+size digit)-part type#`, e.g., `26008-BSC1-M102`. Always use the full number exactly as on the SO/BOM/title block. Designator list: `references/folders-and-naming.md`.

## When drafting anything

1. Identify the project number, City/ST, product and current submittal revision first. If unknown, ask.
2. Put files in the correct project folder location (see `references/folders-and-naming.md`) and say where they belong.
3. Follow the workflow owner rules in `references/workflows.md` — e.g., vendor approval drawings are signed by the Designer, then the Project Engineer; Babtec project tickets route to the PE.
4. Use roles, not names, in anything that will outlive the week. `references/roles.md` lists who held each role as of Sep 2026; staff turnover has been high, so confirm names before addressing people.

## Using Microsoft 365

When the Microsoft 365 connector is available:
- Search Outlook for the project number to find the latest submittal return notice, R&R comments, RFIs and vendor threads.
- Search SharePoint for the project Bio-BLUEPRINT (Bio-HANDLING Product Unit > General > Bio-BLUEPRINTS\<year>) and JMS-STATUS.xlsm.
- **Limits:** the S:\ project drive (\\Jms-clt-fs01\projects) and Outlook Public Folders (project email archive, JMS Contacts Library) are **not** reachable through the connector. Ask the user to attach files from S:\ or from Public Folders when needed. Rarely used files may have moved to the NAS archive (O:\) — check there before reporting a file missing.

## Reference files

- `references/folders-and-naming.md` — project folder standard, tool locations, product designators, drawing/BOM text rules
- `references/workflows.md` — submittals, approval transition, fab checks, vendor drawings, Babtec, change orders, CAD link/Epicor, JMS-STATUS, O&M timing
- `references/roles.md` — who does what (roles first; names as of Sep 2026)

For which document holds a missing piece of information, use the `source-documents` skill.
