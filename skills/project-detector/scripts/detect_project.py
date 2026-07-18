#!/usr/bin/env python3
"""Read-only project classifier for Curb Appeal."""
import json
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
ignored = {".git", "node_modules", "vendor", "dist", "build", ".next", ".astro"}
files = [p for p in root.rglob("*") if p.is_file() and not ignored.intersection(p.relative_to(root).parts)]
names = {p.relative_to(root).as_posix() for p in files}

def has(pattern):
    return any(p.match(pattern) for p in files)

def read_json(rel):
    path = root / rel
    if path.is_file():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass
    return {}

pkg = read_json("package.json")
deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
composer = read_json("composer.json")
composer_deps = {**composer.get("require", {}), **composer.get("require-dev", {})}

signals = []
stack = "unknown"
if "artisan" in names and "@inertiajs/react" in deps:
    stack, signals = "laravel-inertia-react", ["artisan", "@inertiajs/react"]
elif "artisan" in names and "livewire/livewire" in composer_deps:
    stack, signals = "laravel-livewire", ["artisan", "livewire/livewire"]
elif "artisan" in names:
    stack, signals = "laravel-blade", ["artisan", "resources/views" if has("resources/views/*.blade.php") else "composer"]
elif has("astro.config.*") or "astro" in deps:
    stack, signals = "astro", ["astro.config/package dependency"]
elif has("next.config.*") or "next" in deps:
    stack, signals = "nextjs", ["next.config/package dependency"]
elif "react" in deps and (has("vite.config.*") or "vite" in deps):
    stack, signals = "react-vite", ["react", "vite"]
elif "vue" in deps:
    stack, signals = "vue", ["vue dependency"]
elif "svelte" in deps:
    stack, signals = "svelte", ["svelte dependency"]
elif has("*.html") or has("**/*.html"):
    stack, signals = "static-html", ["HTML files"]

manager = "npm"
for lock, value in [("pnpm-lock.yaml", "pnpm"), ("yarn.lock", "yarn"), ("bun.lockb", "bun"), ("bun.lock", "bun"), ("package-lock.json", "npm")]:
    if lock in names:
        manager = value
        break

# The Curb Appeal plugin repository itself — never treat as a website to build.
is_plugin_repo = ".claude-plugin/marketplace.json" in names and any(n.startswith("skills/") and n.endswith("/SKILL.md") for n in names)

if is_plugin_repo:
    classification = "curb-appeal-plugin"
elif not files:
    classification = "new"
elif stack != "unknown":
    classification = "existing-website"
else:
    classification = "existing-unknown"

print(json.dumps({
    "root": str(root), "classification": classification, "stack": stack,
    "confidence": "high" if (signals or is_plugin_repo) else "low", "signals": signals,
    "package_manager": manager if pkg else None,
    "has_saved_brief": "project-brief.md" in names,
    "file_count": len(files)
}, indent=2))
