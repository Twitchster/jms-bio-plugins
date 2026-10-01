---
name: submittal-review
description: >
  This skill should be used when a JMS Bio-HANDLING engineer asks to "review this spec section",
  "go through the spec for exceptions", "write clarifications", "what do we need to take exception to",
  "respond to these submittal comments", "we got an R&R", "build the comment response log",
  "draft Section 1", or shares an equipment specification (e.g., 41 12 13, 46 01 01, 14500, 41 52 19)
  or an engineer-of-record comment set for Bio-SCREW, Bio-BELT, Bio-HOPPER, Bio-SILO, gates or chutes.
metadata:
  version: "0.4.1"
---

# Submittal and Spec Review

Review customer specifications and engineer-of-record (EoR) comments for JMS Bio-HANDLING equipment. Produce outputs the PE can put straight into the submittal. Load `jms-bio-conventions` for folders, naming and workflow owners.

## Establish context first

Confirm or find:
- project number, City/ST, contractor and EoR
- spec section(s) and product(s)
- submittal revision, and whether this is a first submittal or an R&R

If the Microsoft 365 connector is available, search Outlook for the project number plus "Submittal Return Notice" or "R&R" to get the latest comment set and prior responses. Ask for missing documents rather than guessing.

## Mode A — Spec section review (first submittal)

1. Read the whole section, including Part 1 QA/submittal requirements, and the referenced sections the user supplies (01 33 00, 09 96 00, 05 50 00, 40 05 59, 01 xx BABA/domestic clauses).
2. Walk the checklist in `references/spec-review-checklist.md`.
3. Classify every requirement that matters into one of four categories:
   - **Comply**: no note needed; omit these unless asked for a full compliance matrix.
   - **Comply with clarification**: JMS meets the intent, but wording needs to be pinned down.
   - **Exception**: JMS will not or cannot meet it. State the alternative offered.
   - **Question / RFI**: contradictory, missing or ambiguous. Flag it to the customer rather than guessing.
4. Use the standard verbiage in `references/standard-clarifications.md` where it fits, and adapt it to the project.
5. Output a table with columns: Spec ¶, Requirement (short quote), Category, JMS Position / Proposed wording, Owner (PE/Designer/PM/Vendor), Notes. Order it by spec paragraph. Put high-risk items (performance guarantees, gate pressure ratings, sealed calcs, BABA, hazardous-area ratings, control philosophy) in a short summary above the table.

## Mode B — R&R / comment response

1. Number every comment as received. Don't merge or drop any.
2. For each comment, record: Reviewer comment (verbatim), Owner (Designer / PE / PM / Vendor), JMS response (draft), Documents affected (drawing numbers, calc, datasheet), and Status (Open / Drafted / Closed).
3. Response style:
   - Answer the comment directly and cite where the change appears (drawing, sheet, revision cloud).
   - Where JMS disagrees, state the engineering basis in neutral terms ("JMS design basis is…"), not argument.
   - Where the request goes beyond the spec, say it will be handled as a change order.
4. Flag comments that expand scope, contradict earlier approved revisions, or require a sealed calc or a new vendor document. Those drive schedule.
5. Output the log as a table ready to paste into Section 1 – Comment and Response Log, and into the Blueprint Submittal Comments tab. If asked for a file, produce an .xlsx with the same columns.

## Judgment rules

- **Never imply compliance with sluice gate or leakage specifications** (AWWA C561, 40 05 59.35) for JMS screw-conveyor slide or wedge gates. See the gate clarification in the standard verbiage.
- If a performance spec (e.g., discharge rate with a modulating gate) doesn't define control philosophy or who owns integration, clarify it. The 22067 Portland dispute started this way.
- Read the QA sections for domestic-material and BABA rules before accepting vendor hardware. Under BABA, domestic steel is required; imported hardware is generally acceptable. Verify per project.
- Check the building code edition and the seismic design category. SDC B nonstructural components are exempt per ASCE 7 Ch 13 (label them exempt). Ie = 1.5 implies Risk Category IV.
- Unreasonable loads (e.g., a 250 psf hopper roof live load) can be challenged with a proposed value (JMS has obtained 100 psf).
- Fully stainless equipment needs no coating system under a typical 09 96 00. Submit a passivation procedure instead.
- Keep separate submittals (hopper vs screw) on separate threads and logs.

## Missing information

When an input needed for the review isn't in the files provided, follow the `source-documents` skill: map each gap to the document known to hold it (e.g., motor requirements → equipment spec Part 2 + referenced motor section; seismic → structural general notes; BABA → Division 00/01), then ask for those files in one batched request. Always ask whether addenda or a conformed spec affect the section.

## Verification

Before handing back:
- Every requirement quote must match the source text. Mark anything paraphrased.
- Every comment in the R&R set must appear in the log.
- Unresolved facts must be marked "confirm with <owner>" rather than filled in.
