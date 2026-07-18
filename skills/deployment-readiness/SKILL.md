---
name: deployment-readiness
description: Confirm a site is ready to deploy and document how, per stack — Astro/static to Cloudflare/Netlify, Laravel to VPS/cPanel with queue+scheduler, React/Vite. Never deploys without explicit request. Use at the HANDOFF state to produce a pre-deployment checklist.
---

# Deployment Readiness

Never deploy or purchase hosting without an explicit request from the user. This skill prepares and documents; it does not push to production on its own.

## Per-stack notes

- **Astro / static HTML**: build to static assets; host on Cloudflare Pages, Netlify, or any static host. No server, minimal/near-zero monthly cost — a genuine selling point.
- **Laravel (Blade/Livewire/Inertia)**: VPS or cPanel with PHP + database. Requires a **queue worker** (`php artisan queue:work` via supervisor/systemd) for notifications and a **scheduler** (cron → `schedule:run`) if used. Set `APP_ENV=production`, `APP_DEBUG=false`, run migrations, cache config/routes/views.
- **React + Vite (SPA)**: build static bundle; host like a static site, but confirm the separate API/backend it depends on is deployed and reachable.

## Pre-deployment checklist

Confirm before recommending go-live: environment variables set, production build succeeds, database migrations run, queue worker and scheduler configured (if used), file/storage permissions correct, SSL + domain + redirects, caching/compression on, backups configured, error logging on, a rollback path exists, forms/booking verified against real targets, cookie/consent handled, and the site is indexable (not left `noindex`).

Hand the outcome to `../client-handoff/SKILL.md`. List anything still required (real domain, real SMTP/booking keys) as a blocker rather than deploying around it.
