---
name: website-director
description: Orchestrate an end-to-end, production-ready website build or redesign for any service business, with the deepest support for salons. Runs a deterministic state machine from detection through handoff. Use whenever a user asks to create, improve, continue, or audit a business website.
---

# Website Director

Run one deterministic state machine. Move forward through states in order; never jump randomly, re-ask a completed question, or restart intake because optional information is missing. Persist progress so a later session resumes instead of starting over.

## State machine

Each state has an entry condition, an exit condition, an artifact, and a failure behavior. On failure, follow `../error-recovery` guidance in the operating rules: record the blocker in the state file, continue independent work, never rerun an unchanged failing command.

| # | State | Do | Skill | Exit artifact |
|---|---|---|---|---|
| 1 | DETECT | Classify the workspace and read any saved `project-brief.md` / state file. | `../project-detector/SKILL.md` | classification + stack |
| 2 | INTAKE | Collect business info in plain language (or accept a pasted brief). | `../business-intake/SKILL.md` | confirmed / placeholder buckets |
| 3 | CLASSIFY | Fix the project type (brochure / booking / ERP) — always asked, never inferred. | this skill | project type |
| 4 | RECOMMEND | Recommend project type + stack from outcome questions. | `../project-recommender/SKILL.md` | chosen stack + mode |
| 5 | CONFIRM | Summarize plan; get an explicit go-ahead. | this skill | user approval |
| 6 | PLAN | Assemble and save the plan. | `../project-planner/SKILL.md` | `project-brief.md`, state file |
| 7 | PREPARE | Scaffold (only if empty) or confirm existing stack. Never scaffold into a non-empty dir. | `../frontend-craft/SKILL.md` | project skeleton |
| 8 | BUILD | Design tokens, then shell + core pages. | `../design-system/SKILL.md`, `../salon-blueprint/` or `../business-blueprints/`, `../frontend-craft/` | core pages |
| 9 | CONTENT | Write copy; run integrity scan. | `../conversion-copy/SKILL.md`, `../content-integrity/SKILL.md` | verified copy |
| 10 | IMAGES | Source, optimize, verify imagery. | `../image-pipeline/SKILL.md` | images + `image-sources.json` |
| 11 | INTEGRATIONS | Wire forms/booking to real targets. | `../form-integrations/SKILL.md`, `../booking-engine/SKILL.md` | working forms/booking |
| 12 | SEO | Technical SEO, structured data, sitemap/robots. | `../seo/SKILL.md` | SEO applied |
| 13 | RESPONSIVE | Mobile-first, verified at all breakpoints. | `../responsive-design/SKILL.md` | responsive verified |
| 14 | TEST | Accessibility, security, performance, launch audit. | `../accessibility-audit/`, `../security-audit/`, `../performance-audit/`, `../launch-audit/` | audit reports |
| 15 | FIX | Fix material issues; re-run affected checks. | relevant skill | issues resolved |
| 16 | HANDOFF | Deployment readiness + plain-language handoff. | `../deployment-readiness/SKILL.md`, `../client-handoff/SKILL.md` | `HANDOFF.md` |
| 17 | COMPLETE | Report what's done and what needs real info. | this skill | summary |

CLASSIFY (state 3): always ask this as its own message, never inferred and never skipped — the only exception is the user stating it in so many words:

```
What kind of project is this?
1. Frontend only — a marketing/brochure site, no booking or backend
2. Frontend + booking — a customer-facing appointment/reservation system
3. ERP / management system — full business management beyond customer-facing booking
```

If DETECT found an existing project, keep its stack (skip the stack question in RECOMMEND) but still confirm the project type.

## State file — `.curb-appeal/project-state.json`

Written/updated by `../project-planner/SKILL.md` and each state. Update atomically where practical.

```json
{
  "schemaVersion": 1,
  "classification": "new | existing-website | existing-unknown | mixed",
  "stack": "astro | laravel-blade | laravel-livewire | laravel-inertia-react | react-vite | vue | svelte | static-html | unknown",
  "projectType": "brochure | booking | erp",
  "vertical": "salon | restaurant | law | clinic | …",
  "buildMode": "quick | full | custom",
  "currentStage": "BUILD",
  "completedStages": ["DETECT", "INTAKE", "CLASSIFY", "RECOMMEND", "CONFIRM", "PLAN", "PREPARE"],
  "pendingDecisions": [],
  "placeholders": ["address", "testimonials"],
  "requiredBeforeLaunch": ["real phone"],
  "validation": { "plugin": "pass", "state": "pass" },
  "updatedAt": "2026-07-18T00:00:00Z"
}
```

Never store secrets, credentials, or private customer messages in this file. If the file is missing, invalid, or outdated, rebuild it from project evidence rather than trusting it blindly, and never initialize a scaffold over a partially-built project.

## Central business data

Create one stack-appropriate source of truth (typed config, JSON, or DB) — never duplicate business data across components. Fields: `business` (name, type, description, phone, whatsapp, email), `location` (address, city, coords, directions URL, accessibility), `hours`, `serviceCategories`, `services` (id, category, name, description, duration, price, priceQualifier, featured, bookable), `staff` (id, name, role, specialties, bio, image, bookingTarget), `gallery`, `testimonials` (verified flag), `faqs`, `booking` (mode, providerURL, policies), `socials`, `seo`, `legal`, `integrations`. Render only confirmed fields; keep placeholders out of JSON-LD; keep NAP identical everywhere. See `../salon-blueprint/references/content-model.md` for the salon shape.

## Default page set

Home, About, Services/Pricing, Team, Gallery/Work, Contact, hours/location, testimonials, socials, legal footer. Quick Launch builds a focused subset (Home, Services, Contact) at the same quality bar. Combine pages only when the brief benefits.

## Operating rules

- One question per message; wait for the reply. Never bundle intake, confirmation, project-type, and stack questions together.
- A short description ("build me a salon website") is never a substitute for intake — offer the intake choices first (`../business-intake/SKILL.md`), unless a substantially complete brief was pasted or the user said to skip.
- Never re-ask a skipped/answered field; at most one optional follow-up, then proceed with labeled placeholders.
- Never invent facts (awards, reviews, people, prices, addresses, hours, availability, statistics, certifications). Unknown = labeled placeholder, enforced by `../content-integrity/SKILL.md`.
- Never scaffold into a non-empty directory, replace a framework automatically, or restart intake for an existing project with a valid brief — summarize detected context and proceed with the requested change.
- Prefer a fast first usable build (shell → data → core pages → images → polish → audit) over building every optional feature before the primary conversion works.
- Give short progress updates; don't dump command logs. Ask before deployment, purchases, sending messages, or destructive actions.
- On failure: read and classify the error, try a safe fix, never rerun an unchanged failing command, preserve progress, and separate existing-project failures from ones this build introduced.
