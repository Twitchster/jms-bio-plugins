#!/usr/bin/env python3
"""Compare the installed bio-handling plugin with a local clone of the update repository.

Usage:
  python3 check_update.py --installed <installed-plugin-root> --repo <clone-root> [--package <out.plugin>]

Reads:
  <installed-plugin-root>/.claude-plugin/plugin.json      installed version
  <installed-plugin-root>/update-source.json              plugin_path, changelog_path
  <clone-root>/<plugin_path>/.claude-plugin/plugin.json   available version
  <clone-root>/<changelog_path>                           release notes

Prints installed vs available version, then the CHANGELOG sections newer than the
installed version. Exit codes: 0 = update available, 3 = already up to date,
2 = error.
With --package (only when an update is available), validates the repo with
scripts/validate_plugin.py if present, then zips <plugin_path> into the given
.plugin file.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import zipfile


def semver(v):
    m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(v or "").strip())
    return tuple(int(x) for x in m.groups()) if m else None


def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def changelog_since(text, installed):
    """Return changelog sections whose version is newer than the installed one."""
    out, keep = [], False
    for line in text.splitlines():
        m = re.match(r"^##\s+(\d+\.\d+\.\d+)", line)
        if m:
            v = semver(m.group(1))
            keep = bool(v and installed and v > installed)
        if keep:
            out.append(line)
    return "\n".join(out).strip()


def package(src_dir, out_path):
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(src_dir):
            dirs[:] = [d for d in dirs if d not in ("__pycache__", ".git")]
            for f in files:
                if f == ".DS_Store" or f.endswith(".pyc"):
                    continue
                full = os.path.join(root, f)
                z.write(full, os.path.relpath(full, src_dir))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--installed", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--package")
    a = ap.parse_args()
    try:
        inst_manifest = read_json(os.path.join(a.installed, ".claude-plugin", "plugin.json"))
        cfg = read_json(os.path.join(a.installed, "update-source.json"))
        plugin_path = cfg.get("plugin_path", "plugins/bio-handling")
        remote_dir = os.path.join(a.repo, plugin_path)
        remote_manifest = read_json(os.path.join(remote_dir, ".claude-plugin", "plugin.json"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"ERROR: {e}")
        sys.exit(2)

    if remote_manifest.get("name") != inst_manifest.get("name"):
        print(f"ERROR: repository plugin name '{remote_manifest.get('name')}' does not match installed "
              f"'{inst_manifest.get('name')}'. Refusing to continue.")
        sys.exit(2)

    iv, rv = inst_manifest.get("version"), remote_manifest.get("version")
    print(f"Installed version: {iv}")
    print(f"Available version: {rv}  ({cfg.get('repository')}@{cfg.get('branch', 'main')})")
    if not (semver(iv) and semver(rv)):
        print("ERROR: a version is not MAJOR.MINOR.PATCH")
        sys.exit(2)
    if semver(rv) <= semver(iv):
        print("Up to date." if semver(rv) == semver(iv) else
              "Installed copy is NEWER than the repository. Do not downgrade without the user's say-so.")
        sys.exit(3)

    cl = os.path.join(a.repo, cfg.get("changelog_path", "CHANGELOG.md"))
    notes = changelog_since(open(cl, encoding="utf-8").read(), semver(iv)) if os.path.isfile(cl) else ""
    print("\nWhat changed:\n" + (notes or "(no CHANGELOG entries found for the new version(s))"))

    if a.package:
        validator = os.path.join(a.repo, "scripts", "validate_plugin.py")
        if os.path.isfile(validator):
            r = subprocess.run([sys.executable, validator], cwd=a.repo, capture_output=True, text=True)
            print("\nValidation:", r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip())
            if r.returncode != 0:
                print(r.stdout)
                print("ERROR: repository failed validation; not packaging.")
                sys.exit(2)
        package(remote_dir, a.package)
        print(f"\nPackaged {plugin_path} v{rv} -> {a.package}")
    sys.exit(0)


if __name__ == "__main__":
    main()
