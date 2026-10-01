---
name: design-checks
description: >
  This skill should be used when a JMS Bio-HANDLING engineer asks to "check this screw conveyor
  calc", "size the drive", "select the SEW gearbox", "check the gate blade", "what head load for the
  slide gate", "check the live bottom", "review this RISA model", "check the anchors", "is this
  seismic exempt", "check the hopper / silo design", "review the belt conveyor calcs", or asks for
  JMS rules of thumb and lessons learned on screws, shaftless/vertical screws, slide/wedge gates,
  hoppers, live bottoms, silos, belts, motors, gearboxes, anchorage or structural supports.
metadata:
  version: "0.5.0"
---

# Bio-HANDLING Design Checks

Review or develop engineering for JMS Bio-HANDLING equipment using JMS standards, the JMS calculators and lessons learned from past projects. Load `jms-bio-conventions` for tool locations and file naming.

## How to work

1. **Identify the product and the governing inputs:** material (wet cake % DS, bulk density, grit, dried biosolids), capacity, geometry, incline, duty, spec section, code edition, seismic parameters, area classification. List any input that is missing. Don't assume material flow properties silently; state every assumption.
2. **Load the matching reference:**
   - Screws (shafted, shaftless, inclined, vertical, SCREW-PACTOR) → `references/screw-conveyors.md`
   - Slide/wedge gates and actuators → `references/gates.md`
   - Hoppers, live bottoms, silos, chutes, dust collection, load cells → `references/hoppers-silos.md`
   - SEW gearboxes, Baldor motors, hazardous areas, sensors → `references/drives-motors.md`. For an actual SEW selection from calc data, use the `sew-drive-selection` skill. To fill a Bio-BELT or screw calc workbook from a spec, use `conveyor-calcs`.
   - RISA models, seismic, anchors, stairs/platforms, belts structural → `references/structural-anchorage.md`
3. **Check calcs against the current JMS calculator version.** The Bio-SCREW calculator was corrected in Jun 2026 (shaft shear table, lift HP factor 1.3 → 1.7, thrust calcs added). Calcs made with older versions may oversize shafts or understate lift HP. Flag any calc that predates this.
4. **Run the numbers in code, not by estimate.** Show formulas, inputs with units, and results. Report the governing check and its utilization.
5. **Separate what the standard requires from JMS practice and from judgment.** Label each recommendation:
   - [Code/Spec]: required by a code or the project spec
   - [JMS std]: JMS standard practice
   - [Lesson]: learned on a past project
   - [Judgment]: engineering judgment, open to challenge
6. **Where JMS history conflicts, say so.** Present the current position and the conflict; don't pick silently. Examples: shaft tolerances, gate head-load basis.

## Output

- A findings list ordered by severity: **Fails / Unconservative → Questionable input → Improvement**. Each finding has its basis and a suggested fix.
- Calc summaries in a table: check, demand, capacity, ratio, pass/fail.
- If a calc report is requested, name it per the file standard (`PROJ-PRODUCT_CALC_REVX`) and state that it goes in `03 Engineering\01 Calculations\<Product>\Process` or `\Structural`.

## Hard rules

- Slide/wedge gate blades: design for the **full design material head** unless a documented, EoR-accepted basis justifies less. On 22067 the effective-head (Jenike) approach was rejected by the EoR and later judged incorrect; the design head became 40 ft. Initial-fill outlet loads can be 2–4x the effective-head value.
- JMS slide gates are open/close only. Never design for, or imply, partial-open throttling.
- Belt conveyor RISA models: belt tension live loads on the drive and tail pulleys must **not** be copied into seismic ELX/ELZ cases.
- Check SS316 shafts against the motor's maximum torque before replacing CS1045.
- JMS does not do concrete design. Anchorage stops at the Hilti calc and the connection.

## Missing information

Before assuming any input, follow the `source-documents` skill. Map each missing value to its source document and ask for those files in one batched request, marking each item blocking or non-blocking. Examples:
- motor SF or inverter duty → project spec, Part 2 plus the referenced motor section
- SDC/Ip → structural general notes
- f'c or anchor type → structural drawings
- material density or % solids → spec design criteria, or the upstream dewatering vendor
- design head → hopper/silo design calc

