#!/usr/bin/env python3
"""Validate the jms-bio-plugins marketplace and, optionally, enforce a version bump.

Usage:
  python3 scripts/validate_plugin.py                      # structure checks only
  python3 scripts/validate_plugin.py --base origin/main   # also require a version bump
                                                          # if plugin files changed vs base

Checks:
  - .claude-plugin/marketplace.json: valid JSON; name, owner, plugins present.
    Each entry has a name and a ./ relative source that exists, and does not
    also set 'version'.
  - each plugin: .claude-plugin/plugin.json valid JSON; name equals the entry name;
    semver version; no top-level bin/ (claude.ai org sync rejects it).
  - each skill: SKILL.md with YAML frontmatter; name equals the folder name;
    description present, under 1024 characters and without < or > (Claude rejects
    XML-like tags); every references/... or scripts/... path mentioned
    in the skill exists. A path prefixed by another skill's name is a
    cross-skill reference and is checked there.
  - .mcp.json (if present) is valid JSON; update-source.json (if present) names owner/repo and holds no token.
  - with --base: if anything under a plugin's folder changed, its version must be
    greater than on the base ref, and CHANGELOG.md must mention the new version.
Exit code 1 on any error.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors, warnings = [], []


def err(msg):
    errors.append(msg)


def load_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:  # noqa: BLE001
        err(f"{os.path.relpath(path, ROOT)}: invalid JSON ({e})")
        return None


def semver(v):
    m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(v or ""))
    return tuple(int(x) for x in m.groups()) if m else None


def check_skill(skill_dir, all_skill_names):
    name = os.path.basename(skill_dir)
    p = os.path.join(skill_dir, "SKILL.md")
    rel = os.path.relpath(p, ROOT)
    if not os.path.isfile(p):
        err(f"{os.path.relpath(skill_dir, ROOT)}: missing SKILL.md")
        return
    text = open(p, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        err(f"{rel}: missing YAML frontmatter")
        return
    fm = m.group(1)
    fm_name = re.search(r"^name:\s*(\S+)", fm, re.M)
    if not fm_name or fm_name.group(1) != name:
        err(f"{rel}: frontmatter name must be '{name}'")
    if not re.search(r"^description:", fm, re.M):
        err(f"{rel}: frontmatter description missing")
    desc = re.search(r"^description:(.*?)(?=^\S|\Z)", fm, re.M | re.S)
    if desc and re.search(r"[<>]", desc.group(1).replace(">\n", "\n", 1).lstrip().lstrip(">")):
        err(f"{rel}: description cannot contain < or > (Claude rejects XML-like tags such as <project>)")
    if desc and len(" ".join(desc.group(1).split())) > 1024:
        err(f"{rel}: description longer than 1024 characters")
    for ref in set(re.findall(r"(?:references|scripts)/[\w.\-]+\.(?:md|py|json|sh)", text)):
        if os.path.exists(os.path.join(skill_dir, ref)):
            continue
        # cross-skill reference such as "design-checks → references/x.md" or "sew-drive-selection/references/x.md"
        if any(os.path.exists(os.path.join(os.path.dirname(skill_dir), s, ref)) for s in all_skill_names):
            continue
        err(f"{rel}: referenced file not found: {ref}")


def check_plugin(entry):
    src = entry.get("source")
    pname = entry.get("name")
    if not isinstance(src, str) or not src.startswith("./"):
        err(f"marketplace entry '{pname}': source must be a ./relative path (org sync requirement)")
        return None
    if ".." in src:
        err(f"marketplace entry '{pname}': source must not contain '..'")
        return None
    pdir = os.path.join(ROOT, src[2:])
    if not os.path.isdir(pdir):
        err(f"marketplace entry '{pname}': source path does not exist: {src}")
        return None
    if "version" in entry:
        err(f"marketplace entry '{pname}': don't set 'version' here; keep it only in plugin.json")
    manifest = load_json(os.path.join(pdir, ".claude-plugin", "plugin.json"))
    if manifest is None:
        return None
    if manifest.get("name") != pname:
        err(f"{src}/.claude-plugin/plugin.json: name '{manifest.get('name')}' must equal entry name '{pname}'")
    if re.search(r"[<>]", manifest.get("description", "")):
        err(f"{src}/.claude-plugin/plugin.json: description cannot contain < or >")
    if len(manifest.get("description", "")) > 500:
        err(f"{src}/.claude-plugin/plugin.json: description over 500 characters (team limit)")
    if not semver(manifest.get("version")):
        err(f"{src}/.claude-plugin/plugin.json: version must be MAJOR.MINOR.PATCH")
    if os.path.isdir(os.path.join(pdir, "bin")):
        err(f"{src}: top-level bin/ directory is rejected by claude.ai org sync; use scripts/")
    if os.path.exists(os.path.join(pdir, ".mcp.json")):
        load_json(os.path.join(pdir, ".mcp.json"))
    us_path = os.path.join(pdir, "update-source.json")
    if os.path.exists(us_path):
        us = load_json(us_path)
        if us is not None:
            if not re.fullmatch(r"[\w.-]+/[\w.-]+", str(us.get("repository", ""))):
                err(f"{src}/update-source.json: repository must be 'owner/name'")
            elif us["repository"].startswith("OWNER/"):
                warnings.append(f"{src}/update-source.json: repository is still the placeholder OWNER/...")
            if any(k in json.dumps(us).lower() for k in ("token", "password", "ghp_", "github_pat_")):
                if re.search(r"(ghp_|github_pat_)[A-Za-z0-9_]+", json.dumps(us)):
                    err(f"{src}/update-source.json: looks like it contains a GitHub token — remove it")
    sk_root = os.path.join(pdir, "skills")
    names = sorted(d for d in os.listdir(sk_root) if os.path.isdir(os.path.join(sk_root, d))) if os.path.isdir(sk_root) else []
    for d in names:
        check_skill(os.path.join(sk_root, d), names)
    return src[2:].rstrip("/"), manifest.get("version")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def check_bump(base, plugin_path, new_version):
    changed = git("diff", "--name-only", f"{base}...HEAD", "--", plugin_path)
    if changed.returncode != 0:
        err(f"git diff against {base} failed: {changed.stderr.strip()}")
        return
    if not changed.stdout.strip():
        print(f"  {plugin_path}: no changes vs {base}; no bump needed")
        return
    old = git("show", f"{base}:{plugin_path}/.claude-plugin/plugin.json")
    if old.returncode != 0:
        print(f"  {plugin_path}: new on this branch; version {new_version}")
        return
    try:
        old_v = json.loads(old.stdout).get("version")
    except json.JSONDecodeError:
        old_v = None
    if not (semver(new_version) and semver(old_v) and semver(new_version) > semver(old_v)):
        err(f"{plugin_path}: files changed but version {old_v} -> {new_version} was not increased. "
            f"Bump version in plugin.json, or Claude won't deliver the update.")
    changelog = os.path.join(ROOT, "CHANGELOG.md")
    if not (os.path.isfile(changelog) and f"## {new_version}" in open(changelog, encoding="utf-8").read()):
        err(f"CHANGELOG.md: add a '## {new_version} — <date> — <author>' entry describing the change")
    else:
        print(f"  {plugin_path}: version {old_v} -> {new_version}, changelog entry found")


def main():
    base = None
    if "--base" in sys.argv:
        base = sys.argv[sys.argv.index("--base") + 1]
    mp = load_json(os.path.join(ROOT, ".claude-plugin", "marketplace.json"))
    plugins = []
    if mp is not None:
        for field in ("name", "owner", "plugins"):
            if field not in mp:
                err(f"marketplace.json: missing '{field}'")
        for entry in mp.get("plugins", []):
            r = check_plugin(entry)
            if r:
                plugins.append(r)
    if base and not errors:
        print(f"Version check against {base}:")
        for path, version in plugins:
            check_bump(base, path, version)
    for w in warnings:
        print(f"WARNING: {w}")
    if errors:
        print("\nValidation FAILED:")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    print("\n✓ Validation passed")


if __name__ == "__main__":
    main()
