---
name: source-documents
description: >
  This skill should be used whenever information needed to finish a JMS Bio-HANDLING task is missing,
  unclear or conflicting (for example motor requirements, seismic parameters, material properties,
  hazardous-area classification, concrete strength, control philosophy, coatings, BABA, test or
  O&M requirements), or when the user asks "what file do you need", "where would I find that",
  "which document has the motor spec", "what should I send you". Every other bio-handling skill
  (submittal-review, drawing-check, design-checks, om-manual) uses it before asking the user for information.
metadata:
  version: "0.4.1"
---

# Asking for the Right Source Document

When a task needs information that hasn't been provided, don't ask a vague "can you send more info?" and don't assume. Identify the specific document known to contain that information, then ask for that file. Say where it usually lives, which section to look in, and exactly what is needed from it.

## Procedure

1. **List the gaps.** Write down every missing, unclear or conflicting input the task needs, as specific items: e.g., "motor service factor", "SDC and Ip", "cake bulk density", "concrete f'c at the hopper pad".

2. **Check what is already available before asking:**
   - files attached or shared earlier in the conversation, including sections of a spec already provided that point to another section
   - if the Microsoft 365 connector is available, a search of Outlook and SharePoint using the search terms in `references/source-map.md` together with the project number
   - where the information is found this way, cite it (document, section or sheet) and don't ask

3. **Map each remaining gap to its source.** Use `references/source-map.md` to find the document that contains it, where that document usually lives, and the section or sheet to read. Where more than one document can hold it, name the primary one and the fallback.

4. **Ask once, batched.** Send one request covering all gaps. Group it by document so the user gathers each file once. Use this format for each file:
   - **File:** the document name as the team knows it, e.g. "Project spec, Section 41 12 13 + the general motor section it references"
   - **Usually at:** location, e.g. `S:\<YY> PROJECTS\<proj>…\` subfolder, SharePoint, Outlook thread, Public Folders
   - **Look at:** section, paragraph or drawing sheet type
   - **Needed for:** the specific values and why they matter to this task
   - **If you don't have it:** the direct question to answer instead, and the assumption that would be used and marked in the output if the item stays open

   Mark each item **Blocking** (the task can't be finished correctly without it) or **Non-blocking** (can proceed with a stated assumption).

5. **Keep working on everything not blocked.** Mark placeholders clearly (`[CONFIRM: motor SF — spec §2.05]`) and list them in an "Open Items" block at the top of the output.

6. **When the file arrives:**
   - read the relevant section in full, including referenced sections and any addenda
   - quote the governing text with its paragraph number
   - if it points to another document (e.g., "motors per Section 26 05 13"), repeat from step 3 for that document instead of stopping

## Precedence when sources disagree

- Addenda and conformed specs supersede the bid spec. Always ask whether addenda affect the section.
- A written RFI response or EoR comment supersedes the contract document for the item it addresses.
- For O&M and closeout, the approved submittal governs over drafts, vendor manuals and spare-parts lists.
- Between contract documents, use the order-of-precedence clause in the General/Supplementary Conditions. If it can't be found, report the conflict and ask; don't pick a side.
- JMS internal standards apply only where the contract documents are silent.

## Example request

> To finish the SEW gearmotor selection for 24057 I need two files:
>
> 1. **Project spec — the screw conveyor section (e.g., 46 71 xx) plus the general motor section it references.** Usually at: `05 Submittals\...\Spec` or the contract spec PDF from the PM. Look at: Part 2 drive/motor paragraphs and the referenced motor section. Needed for: service factor, NEMA design letter, inverter-duty requirement, thermostats vs thermistors, space heater voltage, enclosure. *Blocking.* If you don't have it: tell me the SF and whether the motor is on a VFD; otherwise I'll use the JMS standard (SF ≥1.4, inverter duty checked) and flag it.
> 2. **Electrical hazardous-area classification drawing** (E-series sheet, "Area Classification"). Look at: the room or area where the screw sits. Needed for: Class/Division, which decides whether SEW can be used at all (max Class I Div 2). *Blocking if the area might be Div 1.*

## Reference

- `references/source-map.md`: information → document → location → section, with connector search terms
