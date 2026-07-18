#!/usr/bin/env python3
"""Dependency-free structural validation for Curb Appeal."""
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
errors = []
for manifest in [root / ".claude-plugin/plugin.json", root / ".claude-plugin/marketplace.json", root / ".codex-plugin/plugin.json"]:
    try:
        json.loads(manifest.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{manifest.relative_to(root)}: {exc}")

skills = list((root / "skills").glob("*/SKILL.md"))
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
        target = (path.parent / ref).resolve()
        if ref.startswith("../") and not target.exists():
            errors.append(f"{path.relative_to(root)}: broken reference {ref}")

if errors:
    print("\n".join(f"ERROR: {e}" for e in errors))
    sys.exit(1)
print(f"OK: {len(skills)} skills and 3 manifests validated")
