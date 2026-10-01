# Step-3 Review Doc Format (Claude doc)

Create the doc with the Docs artifact type (Claude Docs connector). Title: `<PROJ> <TAG> <Conveyor> Calc Review — Rev <X>`, e.g. "25026 SSC-1 Screw Calc Review — Rev A". Keep it short: tables for the facts, one or two sentences of prose per section.

## Sections, in order

1. **Status line** (first paragraph). One sentence giving the result and what is pending. Example: "SSC-1 works on 3 HP with a dual shaftless spiral at 10 rpm and 8% fill; the gearbox output must not be below 9.4 rpm. Waiting on your confirmation to run the SEW selection." Then one line naming the template revision and the source documents.

2. **How to use this doc.** Edit values or status in the register, or comment. Reply "confirmed" in chat when it is right. Name any blocking items.

3. **Design basis decisions.** Table with columns Decision / Choice / Why it matters. List only decisions that change results (torque basis, spiral or belt type, operating point, length basis, scope). Mark each choice as spec, engineer ("per <initials> (date)") or assumption.

4. **Results summary.** Table with columns Check / Demand / Limit / Use % / Result. Include:
   - capacity and fill
   - power (design and maximum) against the motor
   - belt tension and PIW (belt)
   - drive-shaft stress by the sheet method **and** by the spec method if the spec sets one
   - spiral stress on both the sheet basis and the spec basis (screw)
   - thrust (screw; goes to SEW)
   - bearing L10
   - abrasion and compression (screw)

   Say which results are provisional (geometry placeholders, or speed not yet from SEW).

5. **Input register.** Table with columns Cell / Input / Value / Source / Status. Give Status a dropdown: Confirmed / Placeholder / Assumption / Open. Group rows by sheet area (project info, material, geometry, belt or screw, drive, components). Every filled input appears, with the same source text as its cell comment.

6. **Open items.** A checklist. Each line gives the cell, the question, whether it is blocking (and what it blocks), and a proposed answer if there is one.

7. **Spec conflicts and clarifications.** Table with columns Spec ref / Issue / Proposed handling. This list is a deliverable; it feeds `submittal-review`.

8. **SEW request notes.** The target gear unit type, output rpm target and minimum, HP, fB, bore, mounting and pivot, loads (axial thrust, overhung), and motor requirements from the spec (area classification, IEEE 841, NEMA design, SF, voltage, bearing life, nameplate material, spares).

9. **Template findings** (optional). Template behaviour worth knowing: checks that don't apply (e.g., a thermal-expansion check that is for shafted screws only), lookup quirks, and a possible template bug to report to the template owner.

## After each edit round
Re-fill, recalculate, then update sections 1, 3, 4 and 5 in the doc. Change statuses rather than deleting rows. Keep the history of engineer decisions in their comments.

## Optional spreadsheet summary
If the engineer asks for a spreadsheet version, build a separate .xlsx with these tabs:
- Operating Point: live formulas for the speed-dependent torsion checks, so changing the gearbox speed updates them
- Checks
- Open Items: with an Answer column
- Spec Conflicts

If they return it edited, diff it against the version you sent and apply the answers.
