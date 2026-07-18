---
name: launch-audit
description: Audit and finish a local-business website before handoff. Use after implementation to test functionality, responsive layout, accessibility, SEO, performance, content integrity, and conversion paths.
---

# Launch Audit

1. Run the repository's formatter, type checker, linter, tests, and production build when available. For a Laravel project, this means `composer validate`, Laravel Pint, and `php artisan test` alongside any JS-ecosystem tooling in `package.json`.
2. Start the site and inspect every route at mobile and desktop sizes. Use browser automation/screenshots when available.
3. Test header navigation, mobile menu, every CTA, contact links, forms, map/directions, gallery controls, and footer links. For a project using `../booking-engine/SKILL.md`, attempt to double-book the same staff/slot as part of this pass and confirm it's rejected, and confirm the queue-worker requirement for booking notifications is documented for deployment.
4. Check keyboard navigation, focus visibility, labels, headings, landmarks, alt text, contrast, reduced motion, and error messages.
5. Check title/description uniqueness, indexability, canonical URLs, social metadata, structured data validity, and sitemap/robots behavior.
6. Inspect image sizing, layout shift, unnecessary client JavaScript, font loading, and obvious performance bottlenecks.
7. Search for placeholder copy, invented claims, broken links, console errors, overflow, and missing empty/loading/error states.
8. Fix material issues, rerun affected checks, and summarize verified results plus any configuration the user must provide.
