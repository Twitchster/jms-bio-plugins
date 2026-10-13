---
name: source-documents
description: >
  This skill should be used whenever information needed to finish a JMS Bio-HANDLING task is missing,
  unclear or conflicting (for example motor requirements, seismic parameters, material properties,
  hazardous-area classification, concrete strength, control philosophy, coatings, BABA, test or
  O&M requirements), or when the user asks "what file do you need", "where would I find that",
  "which document has the motor spec", "what should I send you". Every other bio-handling skill
  (submittal-review, drawing-check, design-checks, om-manual, cutsheet-markup, conveyor-calcs) uses it before asking the user for information.
metadata:
  version: "0.7.3"
---

# Asking for the Right Source Document

When a task needs information that hasn't been provided, don't ask a vague "can you send more info?" and don't assume. Identify the specific document known to contain that information, then ask for that file. Say where it usually lives, which section to look in, and exactly what is needed from it.

## Procedure

1. **List the gaps.** Write down every missing, unclear or conflicting input the task needs, as specific items: e.g., "motor service factor", "SDC and Ip", "cake bulk density", "concrete f'c at the hopper pad".

2. **Search before asking (ASB rule, Oct 2026).** Go through these sources in order and ask only for what is still missing:
   1. **The conversation:** attached or shared files, including spec sections that point to another section.
   2. **The Equipment List PDFS library** (OneDrive, shared by ASB) for every cut sheet, data sheet, vendor manual or installation instruction. Search the folder names, the file names and the text, including `Archive` folders and `SEW reference Information for O&M creation`.
      - Through the linked computer when the folder is connected (see `cutsheet-markup` → `references/library.md`).
      - Otherwise through the Microsoft 365 connector (SharePoint/OneDrive search; text only, files under 100 MB).
      - **Never ask the user for a cut sheet without searching the library first.** When you do ask, say what you searched and didn't find.
   3. **The user's own Outlook email** through the Microsoft 365 connector. Search the project number, the project or plant name, and the item. Read the threads and their attachments, e.g. vendor quotes with data sheets, EoR comments, RFI responses, PM decisions.
      - Only the signed-in user's mailbox is searched. The connector can't see anyone else's.
      - Use project-specific facts from email only for that project.
   4. **SharePoint** (Bio-BLUEPRINTS, JMS-STATUS, team sites) with the search terms in `references/source-map.md` plus the project number.
   5. **Read.AI meeting transcripts and summaries,** if the Read.AI connector is connected: decisions, verbal commitments, open questions from project meetings.

   Cite everything found this way (document and section, email date and sender, or meeting and date), and don't ask for it. Email and meeting statements are evidence, not contract documents. When they conflict with the spec or the approved submittal, report the conflict per "Precedence" below.

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

## Read.AI connector notice
At the start of a project task, if no Read.AI tools are available in the session, tell the user once in a single line: Read.AI can be connected as a connector in Claude, and then I can use their meeting transcripts and summaries as a project source. Don't repeat it in the same conversation. If Read.AI is connected, search it for the project number and name as step 2.5 above.

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
> 2. **Electrical hazardous-area classification drawing** (E-series sheet, "Area Classification"). Look at: the room or area where the screw sits. Needed for: Class/Division for the JMS-selected switches and sensors, and the notes to SEW (SEW sources a suitable motor for the classification). *Blocking for the switches and sensors, not for the gearmotor selection.*

## Reference

- `references/source-map.md`: information → document → location → section, with connector search terms
