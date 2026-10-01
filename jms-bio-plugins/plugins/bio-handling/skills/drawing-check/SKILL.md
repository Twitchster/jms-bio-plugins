---
name: drawing-check
description: >
  This skill should be used when a JMS Bio-HANDLING engineer asks to "do my fab check", "check this
  drawing package", "review these fabrication drawings", "check the detail drawings", "review this
  vendor approval drawing", "sign off on the TCC drawings", "is this vendor drawing OK", "check the
  shop drawings", or shares a fab check package, weldment/machined-part drawings, a BOM, or a
  supplier approval drawing (TCC/Martin, Vortex, Samana, Elevated Steel, outsourced hopper fabricators).
metadata:
  version: "0.4.0"
---

# Drawing and Fab Check

Check JMS fabrication drawing packages and vendor approval drawings the way the Project Engineer does at the end of the fab-check routing. Load `jms-bio-conventions` for routing, naming and designators, and `design-checks` when a finding needs an engineering calculation.

## Inputs

- The drawing PDF(s): fab check package, or vendor approval drawing.
- The governing references: approved submittal drawings/GA, spec section, calcs, and for vendor drawings the JMS design drawing and PO/RFQ.
- The project number and product.

If the approved submittal or the design drawing isn't provided, check against JMS standards only, and state that the design-intent comparison was not done.

Read every sheet. For scanned or image-heavy PDFs, view the pages as images; don't rely on text extraction alone.

## Mode A — JMS fab check package

Work through `references/fab-check-checklist.md` sheet by sheet. For each finding record:
- Drawing no. / sheet / zone or item
- Finding
- Category: **Error** (form/fit/function, safety, spec/contract, quality) or **Preference**
- Required correction
- Who fixes it: Detailer, or Designer (design change → design manager assigns)

Keep true errors separate from preferences. Fab-check policy is to release 95%+ correct and to return items to engineering only for design intent, form/fit/function, customer/contract, safety or quality.

Output the findings table, then a one-line verdict: "Check complete — no errors", "Check complete with corrections", or "Hold — design change required". Markups go in the Bluebeam Studio session. Don't create a second copy of a locked package.

## Mode B — Vendor / purchased-item approval drawing

Work through `references/vendor-drawing-review.md`. Compare against the JMS design drawing and PO:
- dimensions and interfaces (bolt patterns, flange hole patterns, shaft/bore sizes)
- materials and finishes
- ratings (pressure, hazardous area, IP/NEMA)
- quantities and tag numbers

The output is a findings table plus a recommendation: Approve / Approve as Noted / Revise & Resubmit. Deviations that cost less with no loss of function can be approved, but note them for Quality so they aren't NCR'd. The Designer signs first, then the PE.

## Always check

- **Interfaces between suppliers.** Mismatched hole patterns between vendor gates and JMS frames have been caught at this step, e.g. a Vortex gate vs a hopper live-bottom flange.
- **Hardware callouts** are complete: grade, finish, size, stamped/tagged anchor rods.
- **Weld callouts on outsourced weldments.** Outside shops don't have the JMS shop's tribal knowledge.
- **Lifting provisions** on weldments of roughly 1,000 lb or more.

## Missing information

When a check can't be completed because a reference is missing (approved submittal drawings, design calc, spec materials paragraph, PO, vendor datasheet), follow the `source-documents` skill. Ask for the specific file, its usual location and the sheet or section needed. Continue checking everything else against JMS standards, and list the unverified items.

## Verification

Cite a drawing number and sheet for every finding. If a dimension can't be read or verified, list it as "unable to verify" rather than approving it.
