---
name: performance-audit
description: Check and improve Core Web Vitals and load performance against practical Lighthouse gates — LCP, CLS, fonts, images, unused JS, third parties, caching, and compression. Use at the TEST state. Fix controllable issues; explain third-party limits honestly.
---

# Performance Audit

## Practical gates

Aim for Lighthouse **Performance ≥ 85, Accessibility ≥ 95, Best Practices ≥ 95, SEO ≥ 95**. Do not promise 100 — some factors (embedded maps, third-party booking widgets, ad/analytics scripts) are outside your control. State those honestly.

## Inspect

- **LCP**: prioritize/preload the hero image; avoid render-blocking resources above the fold.
- **CLS**: explicit `width`/`height`/`aspect-ratio` on all media (ties to `../responsive-design/SKILL.md`); reserve space for embeds/fonts.
- **Fonts**: `font-display: swap`, preload the critical face, drop unused weights.
- **Images**: modern formats + responsive sizes from `../image-pipeline/SKILL.md`; lazy-load below fold.
- **JavaScript**: remove/defer unused JS; avoid shipping a heavy client bundle for a mostly-static site (a reason Astro/Blade beat SPA for brochure sites — see `../seo/SKILL.md`).
- **Third parties**: defer maps/widgets/analytics; load on interaction where possible.
- **Delivery**: enable caching and compression (gzip/brotli) at the host.

## Report & fix

Run Lighthouse where available (or the framework's build report), fix what you control, re-measure, and record remaining third-party limitations in the handoff rather than hiding them.
