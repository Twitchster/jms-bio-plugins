# What's new in bio-handling

Plain-language summary for the person installing the update. The full technical log is `CHANGELOG.md` in the GitHub repository (Twitchster/jms-bio-plugins).

## Since 0.7.1 (now 0.7.3, Oct 13 2026)

### Claude looks before it asks you (0.7.3)
Before asking you for a file or a value, Claude now searches, in this order:
1. what you've already shared in the chat
2. the **Equipment List PDFS** library on OneDrive, for any cut sheet, data sheet or vendor manual
3. **your Outlook email** for the project number and name, including attachments such as vendor quotes
4. SharePoint
5. **Read.AI** meeting transcripts and summaries, if you've connected Read.AI

It tells you what it found, with the source, and asks only for what it couldn't find, saying where it looked. It will not ask you for a cut sheet without searching the library first.

**Optional:** connect **Read.AI** in Claude's connectors. Claude can then use your project meeting transcripts and summaries: decisions, commitments, open questions. If it isn't connected, Claude will mention this once per conversation.

**Setup this relies on:**
- the Microsoft 365 connector signed in with your JMS account (email and SharePoint)
- the `Equipment List PDFS` folder synced to your PC through OneDrive and connected in the Claude desktop app (for cut-sheet work)

### SEW data for O&Ms is built in (0.7.2)
- **Closing-plug thread size and plug tightening torques** by gear unit size, in Nm and lb-ft (e.g. FA97 → M22x1.5 → 44 lb-ft / 60 Nm).
- **Recommended oil brands** for the two common SEW oil types (mineral CLP VG 220; food-grade synthetic CLP HC NSF H1 VG 460), plus bearing greases.
- **SEW service intervals, the oil-level check, extended storage and troubleshooting,** from the SEW gear unit manual (edition 02/2023).
- **The SEW Appendix A inserts** (standard, and TorqLOC) are included in the plugin and added to O&Ms automatically when SEW gear units are supplied.
- Claude no longer asks you for the closing-plug sheet or the SEW manual; it only checks whether SEW has issued a newer manual.

### Smaller fixes
- An example in the plugin still said the area classification decides whether SEW can be used. It now matches the current rule: the classification decides the JMS-selected switches and sensors and goes in the notes to SEW; it doesn't block the gearmotor selection.

## 0.7.1 (Oct 6 2026)
- Fixed the install error "description cannot contain XML tags" from 0.7.0.

## 0.7.0 (Oct 5 2026)
- New **cut-sheet markup** workflow for submittals. Claude:
  - lists the purchased components from the spec and calcs
  - picks spec-compliant options from the library
  - marks them up in the JMS style
  - saves one PDF per component plus a selection log to `Equipment List PDFS\Projects\<project number>\`
