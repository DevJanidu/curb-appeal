# Curb Appeal

A Claude Code plugin for designing and building premium, conversion-focused websites for local businesses — salons, law firms, restaurants, clinics, trades, and other location-based service businesses.

It ships as a set of skills, orchestrated by `website-director`:

- `website-director` — entry point; runs the end-to-end workflow.
- `industry-blueprints` — information architecture and conversion paths per vertical (salon, law firm, restaurant, general).
- `art-direction` — original visual systems, including two salon direction archetypes (soft/spa and sharp/editorial) and scroll-revealed gallery motion.
- `conversion-copy` — page copy and calls to action.
- `frontend-craft` — implementation conventions across React, Astro, Vue, Svelte, Laravel/Blade, and plain HTML.
- `booking-engine` — appointment/reservation booking: data model, conflict prevention, live booking UI, notifications, admin.
- `launch-audit` — pre-handoff QA pass.

## Install

In an interactive `claude` session (not a plain shell — launch `claude` first, then run these):

```
/plugin marketplace add DevJanidu/curb-appeal
/plugin install curb-appeal@lyco-labs
```

This repo is private, so make sure you're authenticated with GitHub first (`gh auth login`, or an SSH key loaded in `ssh-agent`) — Claude Code reuses your existing git credentials.

To test a local checkout before publishing anywhere:

```
/plugin marketplace add /path/to/this/repo
/plugin install curb-appeal@lyco-labs
```

## Use

In your project directory, run `claude` and ask for a site — e.g. "Build a booking-first website for this hair salon." You can also invoke the workflow directly with `/curb-appeal:website-director`.

Claude responds with **only** the brief below and waits — fill in and paste back what you can, nothing is required, leave anything blank. Once you reply, it confirms what it captured (naming anything it's treating as a placeholder) and asks for a go-ahead — it won't re-send the brief or re-ask for fields you already skipped. Then, as a separate question, it asks which kind of project this is:

1. **Frontend only** — a marketing/brochure site → scaffolds **Astro** automatically, no further question.
2. **Frontend + booking** — a customer-facing appointment/reservation system
3. **ERP / management system** — full salon or business management beyond customer-facing booking

For (2) or (3), it then asks which stack to build in — **Laravel + Blade + Livewire** (recommended), **Laravel + Inertia + React**, or a **React + Vite frontend only** talking to a separate API — before scaffolding and running the full build: planning, visual direction, copy, booking/admin (if relevant), implementation, and a pre-handoff audit. You don't need to know or specify a tech stack up front — the brief itself has no framework field.

Once confirmed, Claude saves the brief to **`project-brief.md` in your project's own folder** — a plain file in your project, not something stored inside the plugin (plugins are shared code, not per-project storage). On a later session in that same project, it reads that file back instead of asking again.

To skip a step, paste the brief filled in yourself as your first message instead of waiting to be asked:

```
# Website brief

- Business name:
- Industry:
- Location/service area:
- Primary audience:
- Primary conversion:
- Secondary conversion:
- Required pages:
- Services and prices:
- Team members:
- Brand colors/fonts:
- Existing logo/photos:
- Address, phone, email, hours:
- Social links:
- Testimonials (verified):
- Integrations:
- Reference sites (for direction only):
```

## Updating

```
/plugin marketplace update lyco-labs
```

## License

MIT — see [LICENSE](LICENSE).
