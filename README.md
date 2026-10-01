# jms-bio-plugins

A private repository holding JMS Bio-HANDLING plugins for Claude. Right now it holds one: **bio-handling** (`plugins/bio-handling/`). Its contents:

- submittal and spec review
- fab and vendor drawing checks
- design checks
- O&M drafting
- source-document requests
- SEW gearmotor selection

**Keep this repository private.** It contains internal JMS standards, procedures and project lessons.

## How updates reach people (manual by design)

Nothing updates automatically. A person's plugin changes only when they ask Claude to update it.

1. You merge a change into `main` with a version bump and a CHANGELOG entry (see **Releasing a change**).
2. A coworker tells Claude **"check for plugin updates"** or **"update the bio-handling plugin"**.
3. The plugin's `plugin-update` skill:
   - reads the repository named in `plugins/bio-handling/update-source.json`
   - compares versions and shows the CHANGELOG entries since the installed version
   - on an update request, validates the repository and hands the person a `.plugin` file
4. They install it from the file card. It applies to new conversations.

**What each person needs to pull updates:**
- **Read access to this private repository**, granted by the repository owner.
- **GitHub connected to their Claude account.** Credentials are never stored in the plugin.

Anyone without access can still get a `.plugin` file from you directly.

**Keep it manual:**
- **Don't connect this repository to Claude's organization plugin settings with automatic sync on.** If an admin ever connects it there, leave automatic sync off.
- **Don't use Claude's "share plugin" feature for this plugin.** Shared plugins update for recipients automatically.
- **In Claude Code (terminal),** leave marketplace auto-update off; it's off by default. Users run `/plugin marketplace update jms-bio-plugins` when they choose.

Sources: [Manage plugins for your organization](https://support.claude.com/en/articles/13837433) · [Use plugins in Claude](https://support.claude.com/en/articles/13837440) · [Host and maintain a marketplace](https://code.claude.com/docs/en/plugins/host-marketplace)

## First-time install

- **Desktop app:** install the `.plugin` file built from `plugins/bio-handling/` (any Claude session with access can build it by asking "update the bio-handling plugin" once the plugin is installed; for the very first install, the owner sends the file).
- **Claude Code:** `/plugin marketplace add <github-owner>/jms-bio-plugins`, then `/plugin install bio-handling@jms-bio-plugins`. Needs a stored git credential (`gh auth login`, then `gh auth setup-git`).

## Releasing a change

1. Create a branch and edit files under `plugins/bio-handling/`.
2. **Bump `version`** in `plugins/bio-handling/.claude-plugin/plugin.json`:
   - patch (0.3.**1**): wording fixes
   - minor (0.**4**.0): new content or an engineering rule change
   - major: a restructure

   Without a bump, Claude does not deliver the change.
3. Add a matching `## <version> — <date> — <author>` entry to `CHANGELOG.md`. Call out any engineering rule change explicitly.
4. Open a pull request. The **Validate plugin** check runs automatically and fails if:
   - files changed without a version bump, or there's no changelog entry
   - a skill references a file that doesn't exist
   - a manifest is invalid, or a skill name doesn't match its folder
   - something claude.ai org sync rejects (non-relative sources, a top-level `bin/`)
5. A second reviewer approves, then merge. People get it the next time they ask Claude to update the plugin.

Run the same check locally before pushing:

```
python3 scripts/validate_plugin.py --base origin/main
```

## Recommended GitHub settings (repository owner)

- **Settings → Branches → add a rule for `main`:**
  - require a pull request before merging, with at least one approval
  - require the status check **validate** to pass
  - optionally, require review from Code Owners (fill in `.github/CODEOWNERS` with real usernames first)
- **Visibility:** private.
- **Collaborators:** give read access to each person who should be able to pull updates; write access only to maintainers.

## Layout

```
.claude-plugin/marketplace.json     catalog Claude reads (name: jms-bio-plugins)
plugins/bio-handling/               the plugin (its own .claude-plugin/plugin.json holds the version)
scripts/validate_plugin.py          structure + version-bump checks (used by CI)
.github/workflows/validate-plugin.yml
.github/pull_request_template.md
.github/CODEOWNERS                  template — add usernames to enforce reviewers
CHANGELOG.md
```

The version lives only in `plugin.json`. Don't add `version` to the marketplace entry; the validator rejects it.
