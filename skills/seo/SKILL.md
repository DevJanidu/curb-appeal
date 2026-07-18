---
name: seo
description: Make a local-business website fully SEO-ready — technical SEO, structured data, sitemaps, Core Web Vitals, and local-search optimization — regardless of stack or project type. Use during and after implementation of any site built with this plugin.
---

# SEO

## Per-page technical SEO

- Unique title (roughly 50–60 characters) and meta description (roughly 150–160 characters) per page — never duplicated across pages, never left as a generic default.
- Self-referencing canonical URL on every page.
- `robots` meta: `index, follow` on public pages; `noindex, nofollow` on admin/dashboard/auth routes (Filament panel, booking-confirmation pages containing PII, etc.).
- Exactly one `<h1>` per page, with a logical heading order beneath it — no skipped levels.
- Descriptive, keyword-relevant `alt` text on every meaningful image, per `../frontend-craft/SKILL.md`.

## Structured data (JSON-LD)

- Use the most specific schema.org type the vertical supports (`HairSalon`, `BeautySalon`, `NailSalon`, `Restaurant`, `Attorney`/`LegalService`, `MedicalClinic`, etc.), falling back to `LocalBusiness` only if nothing more specific fits.
- Populate `name`, `address`, `telephone`, `openingHours`, `geo`, `priceRange`, `url`, `image` — but **only from real, verified brief answers**. Never fill a structured-data field with a placeholder or guessed value; omit the field entirely if it's unknown. Unlike visible placeholder content, JSON-LD is machine-read — a fabricated phone number or address here actively misleads search engines and anyone who trusts it, and "clearly label demo content" doesn't help since nothing renders it visibly.
- Add a `Service` entry for each real service/price from the brief; skip anything without confirmed pricing rather than inventing a number.
- Add `AggregateRating`/`Review` schema only from verified testimonials — already banned as fabricated content by `../website-director/SKILL.md`'s operating rules, and doubly so here since fake review schema is a common, detectable spam pattern that search engines actively penalize.
- Add `BreadcrumbList` for any site with nested pages, and `FAQPage` schema if the page has real FAQ content.

## Sitemap & robots.txt

- Generate an XML sitemap that updates automatically as pages/services change — not a hand-maintained static list that drifts out of sync.
- `robots.txt` allows all public routes, disallows admin/dashboard/auth/API routes, and references the sitemap URL.
- Stack-specific:
  - **Astro**: `@astrojs/sitemap` integration.
  - **Laravel** (Blade or Inertia): `spatie/laravel-sitemap`, or a route that generates XML from the same service/page data already driving the site — never a second, separately maintained list.
  - **React + Vite only (SPA)**: a build-time script that walks known routes; a sitemap generated only at client runtime won't get crawled reliably.

## Open Graph & social cards

Per page: `og:title`, `og:description`, `og:image` (1200×630, a real image, not a generic logo crop), `og:type`, `og:url`, and `twitter:card` (`summary_large_image`).

## Rendering & crawlability — this is where stack choice matters most

- **Astro**: static/server-rendered by default — SEO-safe out of the box.
- **Laravel + Blade**: server-rendered — SEO-safe out of the box.
- **Laravel + Inertia + React**: enable Inertia SSR (`@inertiajs/react` server rendering, `php artisan inertia:start-ssr`). Without it, content renders client-side only and risks incomplete indexing. Use Inertia's `<Head>` component for per-page meta once SSR is on.
- **React + Vite only (SPA)**: the weakest choice for SEO — pure client-side rendering by default. If this stack was chosen (see `../frontend-craft/SKILL.md`), add a build-time prerendering step for public marketing pages rather than shipping a JS-only shell, and flag this tradeoff to the user up front if SEO matters to them — it's a direct consequence of the stack choice made in `../website-director/SKILL.md` step 6.

## Local SEO

- Keep NAP (name, address, phone) byte-for-byte identical across visible page content, structured data, and any footer/contact block — inconsistent NAP actively hurts local ranking.
- Embed a real map (not a static image) pointing at the verified address, with an accessible title and a direct directions link, per `../frontend-craft/SKILL.md`.
- Weave the service area / city naturally into page copy (headings, service descriptions) rather than keyword-stuffing — coordinate with `../conversion-copy/SKILL.md`.

## Core Web Vitals

- Explicit `width`/`height` (or `aspect-ratio`) on every image to prevent layout shift.
- `font-display: swap` and preload the critical above-the-fold font; avoid loading unused font weights.
- Defer/lazy-load anything below the fold and avoid render-blocking third-party scripts on first load.

## Verification

Before considering SEO work done, check it rather than assuming the markup is correct:

- Fetch `/sitemap.xml` and `/robots.txt` directly and confirm they return valid content, not a 404.
- Parse each page's JSON-LD as JSON to confirm it's syntactically valid.
- Confirm title/description are non-empty and differ across every page — a template that silently repeats the same fallback text on every route is a common, easy-to-miss failure.
- If Playwright MCP or other browser automation is available (same pattern as `../image-pipeline/SKILL.md`'s verification step), load a few key pages and inspect the rendered `<head>`, not just the server-sent HTML, to catch cases where client-side rendering strips or fails to inject meta tags.
