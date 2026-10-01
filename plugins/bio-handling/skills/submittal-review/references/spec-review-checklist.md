# Spec Review Checklist — Bio-HANDLING equipment

Work through each area. Record only items needing clarification, exception or an RFI. For each, also record the item that confirms compliance if the user asks for a full matrix.

## Commercial / QA (Part 1)
- [ ] Submittal contents required: calcs, sealed structural calcs, O&M, spare parts, closeout forms (01 33 00 Equipment Maintenance Summary / Maintenance Requirements).
- [ ] Sealed/stamped calcs required? By whom (licensed structural engineer, state)? Code edition (IBC 2018 vs 2021; ASCE 7 edition).
- [ ] Domestic material / BABA / AIS clauses; stainless shapes/fasteners "made in USA" language.
- [ ] Warranty wording (an R1 has been rejected for warranty wording alone).
- [ ] Shop tests, field tests, performance tests. What load and duration, who operates, and what control mode.
- [ ] Training and startup days; O&M timing.

## Performance
- [ ] Capacity basis: wet lb/hr or ft³/hr, % solids, bulk density. Missing material properties (flowability, angle of repose, cohesion) → state assumptions in the submittal.
- [ ] Performance tied to modulating gates or load cells without a defined control philosophy → clarify.
- [ ] JMS performance test convention: full hopper, gates fully open, screw at 20 rpm.

## Materials and finishes
- [ ] Stainless grade (304 vs 316) for troughs, flights, hardware, anchors. Hilti has no 1" mechanical anchor in 316 SS; KWIK BOLT TZ2 is the only 316 SS mechanical anchor for heavy loads.
- [ ] Shafts: JMS uses 304 SS pipe and flights with hardened carbon-steel shafts. Switching to SS316 shafts lowers yield torque (check against motor max torque).
- [ ] Coatings: fully SS → passivation procedure instead of a 09 96 00 system. Pickling/passivation of welds if spec'd. Blasted SS finish on hoppers is a BU standard, not a spec item.
- [ ] Hardware: A307 Gr A bolts / A563 Gr A HDG heavy hex nuts acceptable per typical spec. Anchor rods must be stamped or tagged. F1554 Gr36 HDG can be hard to source (Gr55 S1 HDG has been accepted).
- [ ] Liners (UHMW, Hardox for grit), wear-indicating liners.

## Mechanical
- [ ] Screw: shafted vs shaftless, pitch, incline, fill, rpm limits, runout tolerance (spec silent → JMS accepts Martin/TCC TIR 0.015" over 6").
- [ ] Covers: hinged is the JMS standard; lift-off covers are a hazard.
- [ ] Gates: pressure rating, leakage, orientation (horizontal), actuator type, open/close time, modulating vs open/close. JMS gates are open/close only.
- [ ] Flexible chutes: minimum achievable height (~4–6"), pressure rating, lead time (~12–14 wk neoprene).
- [ ] Access: stairs/platforms material (HDG vs aluminum), grating type (15-W-2 often non-stock; 19-W-4 easier), live loads, OSHA ladder rules.

## Drives and electrical
- [ ] Motor spec: NEMA design letter, service factor, inverter duty, thermostats vs thermistors, space heaters, IP/NEMA rating.
- [ ] Hazardous-area classification by location (inside silo shell vs dust collector). SEW max is Class I Div 2. XP motors are SF 1.0 and likely to be rejected where SF 1.15 is spec'd. All suppliers on one job should use the same spec motor.
- [ ] Grounding rings / bearing protection (SEW offers conductive fleece, not Aegis rings; take exception or use another motor).
- [ ] Speed switches: rating vs area classification.
- [ ] Pull-cord e-stops: DPDT switches now common in specs.
- [ ] Controls scope boundaries: who supplies the PLC, integration, and signals exchanged.

## Structural
- [ ] Seismic: SDC, Ip, Ie, Risk Category. SDC B → exempt. Belt tension live loads never go in seismic load cases.
- [ ] Wind, roof live loads, platform live loads (100 psf typical for stairs).
- [ ] Anchorage: post-installed vs cast-in, concrete strength, CMU grouted or hollow, edge distances. JMS doesn't do concrete design.
- [ ] Support spans much over ~15 ft exceed JMS practice.

## Items that are change orders if requested later
- Features beyond spec (indicator color conventions, extra instrumentation, upgraded materials).
