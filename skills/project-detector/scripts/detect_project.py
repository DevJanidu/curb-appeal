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

pkg = {}
if (root / "package.json").is_file():
    try:
        pkg = json.loads((root / "package.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        pass
deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}

signals = []
stack = "unknown"
if "artisan" in names and "@inertiajs/react" in deps:
    stack, signals = "laravel-inertia-react", ["artisan", "@inertiajs/react"]
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

classification = "new" if not files else "existing-website" if stack != "unknown" else "existing-unknown"
print(json.dumps({
    "root": str(root), "classification": classification, "stack": stack,
    "confidence": "high" if signals else "low", "signals": signals,
    "package_manager": manager if pkg else None,
    "has_saved_brief": "project-brief.md" in names,
    "file_count": len(files)
}, indent=2))
