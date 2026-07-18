---
name: project-recommender
description: Recommend the project type and technology by asking outcome questions, not framework questions. Translates plain-language goals into brochure / external-booking / native-booking / ERP and a stack, with a one-line rationale. Use at the RECOMMEND state.
---

# Project Recommender

Non-technical users choose outcomes, not frameworks. Ask what the site should *do*, then translate.

## Outcome question

Present exactly this, then wait:

```
What should this website do?

1. Show the business and generate calls, WhatsApp messages, or enquiries
2. Use an existing external booking system
3. Include a new online appointment-booking system
4. Include a complete business-management system
5. I'm not sure — recommend the best option
```

## Translation

| Choice | Project type | Recommended stack |
|---|---|---|
| 1 | Brochure / lead-gen | **Astro** |
| 2 | External booking (link out) | **Astro** |
| 3 | Native booking | **Laravel + Blade + Livewire** |
| 4 | ERP / management | **Laravel + Blade + Livewire** (Filament admin) |
| 5 | Recommend | ask 1–2 outcome questions, then pick from above |

- Use **Laravel + Inertia + React** only when the interaction is genuinely app-like (rich client state), not for a normal brochure or booking site — it costs SSR/SEO complexity (see `../seo/SKILL.md`).
- If `../project-detector/SKILL.md` found an existing project, **preserve its stack** — recommend project type only, never a migration unless the user explicitly asks.

## Explain briefly

Give one line each on: what the visitor experience will be, the cost/maintenance implication (static hosting vs. a server with a queue worker), and the technical choice. Then let the user confirm or override. Don't run everyone through a framework questionnaire.

## Build modes

Offer **Quick Launch** (core pages, production quality), **Full Business Website** (all supporting pages), or **Custom**. Quick Launch is still responsive, accessible, SEO-ready, optimized, and tested, with real CTAs — never a lower bar, only fewer pages.
