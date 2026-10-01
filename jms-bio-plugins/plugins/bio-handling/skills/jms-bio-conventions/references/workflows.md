# JMS Bio-HANDLING Workflows (as of Sep 2026)

## Submittals and R&Rs

1. The PM sends a Submittal Return Notice (Approved / Approved as Noted / R&R = Revise & Resubmit). The table lists project number, revision, status, "Requires Action from", and comment file location.
2. Put client comments on the Submittal Comments tab of the project Blueprint, each with an owner (Designer / PE / PM / vendor). Designer-only items are closed by the designer.
3. Put responses in "Section 1 – Comment and Response Log" of the resubmittal PDF.
4. Assemble the resubmittal in `05 Submittals\<equipment>\Rev X` and email the PM "ready to go".
5. Metrics: late submittals and R&Rs are a visible Engineering metric (goal zero late). Internal target is first submittal within 70 days (basis debated). JMS-STATUS: column 1.5 = 21 days after the date in column BS, red until the R&R is sent back; "R&R Receipt" stays empty until the R&R is actually received. Enter only ACTUAL dates in black. Never enter a resubmittal date before actually resubmitting.
6. If the customer requires structural calcs signed and sealed, the PE writes the RISA report, and Element 30 reviews and stamps it after approval. Check the building code edition stated (e.g., IBC 2021 vs 2018) before sending.
7. BABA compliance letters come from Quality. The PE supplies stamped structural reports.

## After approval

- **Post-Approval Internal Review (pre-Ops handoff):** within 24–72 hrs of approval, 60–90 min. Covers commitments, make/buy, outsourced-fab materials, buyout and long lead, P/N and Epicor readiness, detailing, schedule. Outputs: Manufacturing Decision Log, JMS-Supplied Fabricator Material Tracker, Buyout/PO Matrix, Long Lead Tracker, Detailing Responsibility Matrix.
- **Approval Transition meeting (PM-run):** Blueprint info, scope, milestone/ship dates, GA walk-through, bid notes/uncommon items, quality requirements, submittal RFIs, purchasing plan. Publishes Key Takeaways and action items. Detailing waits for a formal "ready for detail" notice.
- The designer completes the model and drawing checklist in the Blueprint before detailing.
- **Scope transfers to Bio Engineering (Aug 2026):** routing (PE accountable; route in SolidWorks metadata and on every drawing), design for manufacturing (design around JMS shop capabilities), and purchasing takeoffs (PEs). Expectation: release 95%+ correct. Issues return to engineering only for design intent, form/fit/function, customer/contract, safety or quality. Separate true errors from preferences.
- **Cost control:** compare the developing design against the original estimate. Escalate material cost variances to the Director of Products and the Director of Engineering before the Design/CAD phase.

## Fab checks

Routing: the detailer posts the package plus checklist `JMS-DET-F-<proj>.xlsx` in `04 Drawings\03 Drawing Checks\03 Fabrication Drawings\Check Packages`. Then: detailing lead → manufacturing engineering → weld/manufacturing supervisor → Project Engineer → detailer corrections. Each checker replies "check complete".
- Reviews are done in Bluebeam Studio Sessions, with all markups in one document.
- If the package is locked by another checker, wait and retry. Don't save a second copy, and don't move or rename check packages.
- Design changes found in fab check go to the design manager to assign a designer.
- The PE signs the checklist.

## Vendor / purchased-item approval drawings

- Purchasing sends them. The Designer reviews and signs first, then the Project Engineer. Signing is a PE function, not PM or director.
- TCC/Martin requires signed approval drawings for all projects.
- A supplier drawing that differs from the JMS design may be approved when it costs less with no loss of function, but tell Quality so it isn't NCR'd.
- Before approving shipment of vendor-fabricated items: check as-builts against drawing tolerances. Review photos, test-run video, and inspection and drive-test reports.

## Babtec (QMS)

- The Project Engineer is the primary contact for project Babtec tickets.
- Complaint tasks assigned to engineers must be completed, with time noted, before the complaint closes.
- Disposition, Failure and Responsible fields must be filled.
- Changes to released projects are recorded in Babtec, and the complaint number goes in the revision email.
- Don't zero out sales order lines; capture changes in Babtec for root cause.
- VOC complaints: include the Babtec complaint ID in related emails.

## Drawing revisions

Request format to detailing: What is changing / quantities / why (be very descriptive). All revisions go through the revision process so jobs update. Replacing a component on one job = BOM revision, not obsoleting the common P/N.

## CAD link and Epicor

1. Engineering finalizes P/Ns and purchased items.
2. Detailing runs CAD Link + Flat BOM.
3. Purchased items are pushed to Epicor.
4. Purchasing creates demand by lead time.
- Communicate any change made after CAD linking. CAD link ASAP so long-lead demand exists.
- Common error: cut-list parts flagged Purchased instead of Manufactured.

## Change orders

When a customer adds scope beyond spec:
1. Tell the customer it's a CO.
2. Get quotes.
3. Mark up per the original margin (Product Management, via the project Bio-BLUEPRINT).
4. The PM requests the CO.

Customer-requested features beyond spec (e.g., indicator color conventions) are COs.

## O&M manuals

The PE drafts the initial O&M. Target: submit 2 weeks before equipment delivery, and before Status 4.0 (Initial Shipment).

## Purchasing and procurement

- Purchasing contacts the PE directly for technical questions; the PE coordinates with the designer.
- PO approval over $50,000 needs budgetary data from the Director of Projects.
- The first PO with a new fabricator ships to JMS for inspection before going to the customer.
- JMS doesn't accept supplier deliveries on Fridays.

## JMS-STATUS milestones

Status 2.5 = Detailing & Routing Complete. Status 4.0 = Initial Shipment Date. Column 2.0 = red forecast 190 days after PO receipt; black approval date once approved.
