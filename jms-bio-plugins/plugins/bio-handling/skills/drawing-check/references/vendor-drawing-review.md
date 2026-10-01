# Vendor / Purchased-Item Approval Drawing Review

Sign-off order: the Designer signs first, then the Project Engineer. Purchasing sends the drawings and holds SO lines until engineering releases them.

## Compare against the PO/RFQ and JMS design
- [ ] Model/part number, quantity and tag numbers agree with the PO and the JMS BOM.
- [ ] Interface dimensions: flange bolt patterns, hole sizes and locations, shaft and bore sizes, mounting footprint, clearances to stairs, platforms and explosion panels.
- [ ] Materials and grades agree with the spec (304/316, galvanizing, domestic/BABA). Ask Quality for a BABA certificate where required.
- [ ] Ratings: pressure (flex joints, chutes, gates), hazardous-area class/division, NEMA/IP, service factor, voltage and phase.
- [ ] Cable lengths let controllers mount outside hazardous areas (e.g., 32 ft vs 5 ft).
- [ ] English cutsheets and nameplates for motors.
- [ ] Code basis on vendor structural calcs agrees with the project (IBC edition, seismic parameters).

## Product-specific points
- **TCC / Martin screws:** signed approval drawings are required for all projects. TCC won't share internal drawings of stock CEMA components. TCC/Martin doesn't provide marked-up-print dimensional reports as standard; request photos, inspection records and a test-run video before approving shipment.
- **SEW gearmotors:** check the unit type by product (Bio-SCREW = F parallel-shaft, B14 flange, hollow shaft; Bio-BELT = K helical-bevel, hollow shaft with torque arm, conduit box not on the conveyor-frame side). Also check mounting position (it drives oil volume), terminal box and cable entry location, and inverter-duty features (TF sensors, FKM seals) noted in the quote. Torque-arm sleeve and pin dimensions are in the SEW catalog.
- **Baldor motors:** datasheets are stock and don't reflect spec accessories. Say so in the submittal.
- **Aluminum handrail (Samana/Moultrie):** minimum P-loop 7" c-c.
- **Flexible chutes/joints:** minimum heights ~4" (US Bellows, Elasto-Valve), 6" (PROCO). Check the pressure rating.
- **Stairs (Elevated Steel etc.):** check the stamped calc package, foundation locations, landing elevations and headroom (OSHA 7.5 ft min near explosion panels).
- **Outsourced hoppers:** weld sizing and callouts are Engineering's responsibility. Give the fabricator the RISA report. Use the Fully Welded / Field Welded Hopper example PDFs to show stitch vs full welds.
- **Pull-cord switches:** replacements may have a different mounting-hole pattern. Check form and fit, not just function.

## Decision
- **Approve:** matches.
- **Approve as Noted:** minor corrections the vendor can make without resubmitting.
- **Revise & Resubmit:** interface, rating or material mismatch.
- A deviation that is cheaper with no loss of function may be approved. Notify Quality so it isn't NCR'd.
