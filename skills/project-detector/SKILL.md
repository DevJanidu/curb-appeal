---
name: project-detector
description: Classify a workspace as a new project or an existing Astro, Next.js, React/Vite, Laravel Blade, Laravel Inertia React, Vue, Svelte, or static site before website work. Use at the start of every Curb Appeal build, redesign, continuation, or audit to prevent destructive scaffolding and preserve the existing stack.
---

# Project Detector

Run `python3 scripts/detect_project.py <project-root>` from this skill directory when available. Otherwise inspect the same signals manually.

Return a compact context block containing classification, confidence, stack, package manager, relevant roots, existing brief, test commands, and constraints.

Rules:

- Treat a directory with application files as existing even if its framework is unknown.
- Never scaffold into a non-empty directory.
- Detect Laravel plus React/Inertia before plain Laravel.
- Detect Next.js and Astro before generic React.
- Select the package manager from lockfiles; do not replace it.
- Read `composer.json`, `package.json`, routes, layouts, and project instructions before editing.
- Preserve the detected stack unless the user explicitly requests a migration.
- If evidence conflicts, report `mixed/ambiguous` and ask one focused question.

The script is evidence, not permission to edit. Ignore generated/vendor directories when assessing whether a project is empty.
