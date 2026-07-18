#!/usr/bin/env python3
"""Dependency-free structural validation for Curb Appeal.

Checks: valid JSON manifests, version consistency, skill frontmatter and
name/dir match, duplicate skill names, cross-references that resolve,
no absolute machine paths, and no obvious committed secrets.
"""
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
errors = []

# --- Manifests parse + version consistency ---
manifests = {
    "claude": root / ".claude-plugin/plugin.json",
    "codex": root / ".codex-plugin/plugin.json",
    "marketplace": root / ".claude-plugin/marketplace.json",
}
data = {}
for key, path in manifests.items():
    try:
        data[key] = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path.relative_to(root)}: {exc}")

versions = {}
if "claude" in data:
    versions["claude"] = data["claude"].get("version")
if "codex" in data:
    versions["codex"] = data["codex"].get("version")
if "marketplace" in data:
    for plugin in data["marketplace"].get("plugins", []):
        if plugin.get("name") == "curb-appeal":
            versions["marketplace"] = plugin.get("version")
distinct = {v for v in versions.values() if v is not None}
if len(distinct) > 1:
    errors.append(f"version mismatch across manifests: {versions}")

# --- Skills ---
skills = sorted((root / "skills").glob("*/SKILL.md"))
names = set()
for path in skills:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append(f"{path.relative_to(root)}: missing frontmatter")
        continue
    name = re.search(r"^name:\s*(.+)$", match.group(1), re.M)
    desc = re.search(r"^description:\s*(.+)$", match.group(1), re.M)
    if not name or not desc:
        errors.append(f"{path.relative_to(root)}: name/description required")
        continue
    value = name.group(1).strip()
    if value != path.parent.name or not re.fullmatch(r"[a-z0-9-]+", value):
        errors.append(f"{path.relative_to(root)}: invalid or mismatched name {value}")
    if value in names:
        errors.append(f"duplicate skill name: {value}")
    names.add(value)
    for ref in re.findall(r"`([^`]+\.md)`", text):
        if ref.startswith("../"):
            target = (path.parent / ref).resolve()
            if not target.exists():
                errors.append(f"{path.relative_to(root)}: broken reference {ref}")

# --- Absolute machine paths + committed secrets in shipped text ---
abs_path = re.compile(r"[A-Za-z]:\\Users\\|/Users/[a-z]|/home/[a-z]")
secret = re.compile(
    r"(?i)(-----BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|"
    r"AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9-]{10,})"
)
for path in list(root.glob("skills/**/*.md")) + list(root.glob("skills/**/*.py")) + list(root.glob("scripts/*.py")):
    body = path.read_text(encoding="utf-8", errors="ignore")
    if abs_path.search(body):
        errors.append(f"{path.relative_to(root)}: contains an absolute machine path")
    if secret.search(body):
        errors.append(f"{path.relative_to(root)}: contains a probable committed secret")

if errors:
    print("\n".join(f"ERROR: {e}" for e in errors))
    sys.exit(1)
print(f"OK: {len(skills)} skills and {len(data)} manifests validated")
