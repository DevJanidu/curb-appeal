# Curb Appeal

A Claude Code and Codex plugin for building production-ready, conversion-focused business websites — with the deepest specialization for salons, spas, barbershops, nail/lash studios, and beauty businesses. It runs a deterministic, non-technical workflow: you describe your business in plain language, and the plugin detects the project, plans, builds, sources images, wires real forms/booking, and applies SEO, accessibility, responsive, and QA work.

Other verticals are fully supported too: restaurants, law firms, clinics, real estate, trades, hotels, gyms, education, and general local business.

## How it works — a 17-state workflow

`website-director` orchestrates a state machine: **DETECT → INTAKE → CLASSIFY → RECOMMEND → CONFIRM → PLAN → PREPARE → BUILD → CONTENT → IMAGES → INTEGRATIONS → SEO → RESPONSIVE → TEST → FIX → HANDOFF → COMPLETE.** Progress is saved to `.curb-appeal/project-state.json` in your project so a later session resumes instead of starting over.

### Skills

- `website-director` — the orchestrator / state machine.
- `project-detector` — classifies new vs. existing projects and the stack before any scaffold or edit.
- `business-intake` — plain-language intake (paste a brief, answer simple questions, or use placeholders).
- `project-recommender` — recommends project type + stack from outcome questions, not framework jargon.
- `project-planner` — writes `project-brief.md` and the resumable state file.
- `design-system` — deterministic visual tokens before any page is built.
- `business-blueprints` — per-vertical IA, conversions, pages, schema, and content rules.
- `salon-blueprint` — deep salon intake, content model, page recipes, and quality bar.
- `conversion-copy` — outcome-led copy and CTAs.
- `content-integrity` — blocks fabricated reviews/awards/prices/people and placeholder-in-production.
- `frontend-craft` — implementation across Astro, Laravel (Blade/Livewire/Inertia), React/Vite, Vue, Svelte, HTML.
- `form-integrations` — wires forms to real targets; never fakes a submission.
- `booking-engine` — appointment/reservation data model, conflict safety, notifications, admin.
- `image-pipeline` — sources, optimizes, and verifies real images; records provenance.
- `responsive-design` — mobile-first, verified across all device breakpoints.
- `accessibility-audit` — WCAG 2.2 AA checks.
- `seo` — technical SEO, structured data, sitemap/robots, Core Web Vitals.
- `security-audit` — CSRF, validation, authorization, secrets, headers, webhooks.
- `performance-audit` — practical Lighthouse gates and Core Web Vitals.
- `deployment-readiness` — per-stack pre-deploy checklist (never deploys without asking).
- `launch-audit` — final pre-handoff QA pass.
- `status-badge-system` — centralized status normalization, accessible badges, reactive updates, and application-wide migration.
- `client-handoff` — plain-language handoff doc for a non-technical owner.

## Install

In an interactive `claude` session (launch `claude` first, then run these):

```
/plugin marketplace add DevJanidu/curb-appeal
/plugin install curb-appeal@lyco-labs
/reload-plugins
```

If the repository is private, make sure you're authenticated with GitHub first (`gh auth login`, or an SSH key in `ssh-agent`) — Claude Code reuses your git credentials. If it's public, no authentication is needed to install.

To test a local checkout:

```
/plugin marketplace add /path/to/this/repo
/plugin install curb-appeal@lyco-labs
```

## Use

Open Claude Code in your website folder and say:

> Use Curb Appeal to build a website for my business. Ask me simple questions.

The plugin detects your project, offers to take a pasted brief / ask simple questions / use placeholders, asks what the site should *do* (in plain language), recommends the stack, saves a plan, and builds — then handles images, forms/booking, SEO, responsive, accessibility, and QA, and produces a `HANDOFF.md`. You never need to name a framework.

## Updating

```
/plugin marketplace update lyco-labs
/reload-plugins
```

## Development

Dependency-free checks run in CI on every push and PR:

```
python scripts/validate_plugin.py        # manifests, versions, frontmatter, refs, secrets, paths
python scripts/validate_state.py --self-test   # project-state schema
python skills/project-detector/scripts/detect_project.py <dir>   # classify a directory
```

## License

MIT — see [LICENSE](LICENSE).
