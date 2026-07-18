# Curb Appeal

A Claude Code plugin for designing and building premium, conversion-focused websites for local businesses — salons, law firms, restaurants, clinics, trades, and other location-based service businesses.

It ships as a set of skills, orchestrated by `website-director`:

- `website-director` — entry point; runs the end-to-end workflow.
- `industry-blueprints` — information architecture and conversion paths per vertical (salon, law firm, restaurant, general).
- `art-direction` — original visual systems, including two salon direction archetypes (soft/spa and sharp/editorial) and scroll-revealed gallery motion.
- `conversion-copy` — page copy and calls to action.
- `frontend-craft` — implementation conventions across Next.js, React, Astro, Vue, Svelte, Laravel/Blade, and plain HTML.
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

Once installed, just describe the website you want in any project — e.g. "Build a booking-first website for this hair salon" — and Claude follows the `website-director` workflow automatically. You can also invoke a skill directly:

```
/curb-appeal:website-director
```

See `assets/project-brief.template.md` for the intake questions worth answering up front (business details, brand assets, integrations) so Claude has less to assume.

## Updating

```
/plugin marketplace update lyco-labs
```

## License

MIT — see [LICENSE](LICENSE).
