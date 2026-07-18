---
name: project-planner
description: Turn confirmed intake plus the chosen project type and stack into a concrete, saved plan — page list, data model, integrations, placeholders, and required-before-launch items. Writes project-brief.md and the resumable state file. Use at the PLAN state.
---

# Project Planner

## Produce the plan

From the intake buckets (`../business-intake/SKILL.md`) and the recommendation (`../project-recommender/SKILL.md`), assemble:

- Vertical + one primary and one secondary conversion (`../business-blueprints/SKILL.md` or `../salon-blueprint/SKILL.md`).
- Page list and homepage modules for the chosen build mode.
- Central business-data shape to create (see `../website-director/SKILL.md`'s business-data section).
- Integrations needed (forms/booking) and whether keys exist.
- Placeholders and required-before-launch items, carried verbatim from intake.

## Save it

1. Write a human-readable `project-brief.md` at the project root — confirmed facts plus clearly labeled placeholders. This is what a future session reads to avoid re-asking.
2. Write/update `.curb-appeal/project-state.json` (schema in `../website-director/SKILL.md`): schema version, classification, stack, project type, vertical, completed/current stage, pending decisions, placeholders, validation status, updated-at. Never store secrets or private customer messages. Update atomically where practical.

## Confirm before building

Summarize the plan in plain language and get a go-ahead before scaffolding or editing. Don't re-open intake for optional gaps — proceed with placeholders. Once confirmed, hand back to `../website-director/SKILL.md` to enter PREPARE/BUILD.
