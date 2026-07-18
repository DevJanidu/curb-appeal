# Local Business Web Studio

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

In an interactive `claude` session:

```
/plugin marketplace add <owner>/<repo>
/plugin install local-business-web-studio@lyco-labs
```

Replace `<owner>/<repo>` with wherever this repo ends up living (for example `your-org/local-business-web-studio`). If the repo is private, make sure you're authenticated with your git provider first (`gh auth login` for GitHub, or an SSH key loaded in `ssh-agent`) — Claude Code reuses your existing git credentials.

To test a local checkout before publishing anywhere:

```
/plugin marketplace add ./local-business-web-studio
/plugin install local-business-web-studio@lyco-labs
```

## Use

Once installed, just describe the website you want in any project — e.g. "Build a booking-first website for this hair salon" — and Claude follows the `website-director` workflow automatically. You can also invoke a skill directly:

```
/local-business-web-studio:website-director
```

See `assets/project-brief.template.md` for the intake questions worth answering up front (business details, brand assets, integrations) so Claude has less to assume.

## Updating

```
/plugin marketplace update lyco-labs
```

## License

MIT — see [LICENSE](LICENSE).
