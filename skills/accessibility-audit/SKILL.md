---
name: accessibility-audit
description: Verify a site meets WCAG 2.2 AA — semantics, keyboard operation, focus management, labels/errors, contrast, alt text, reduced motion, touch sizes, zoom, and accessible dialogs/galleries/maps. Use at the TEST state, with automated (Axe) plus manual checks.
---

# Accessibility Audit

Target **WCAG 2.2 AA**. Run Axe (or equivalent) where available, then check manually — automation catches perhaps half of real issues.

## Checklist

- **Structure**: semantic landmarks (`header/nav/main/footer`), one `h1`, no skipped heading levels, a working skip link.
- **Keyboard**: every interactive element reachable and operable by keyboard; visible focus; logical tab order; focus trapped in open dialogs and restored on close.
- **Forms**: real labels, programmatic error association, status announced via `aria-live` (ties to `../form-integrations/SKILL.md`).
- **Color/contrast**: text ≥ 4.5:1 (large text ≥ 3:1); never color as the only signal.
- **Images**: meaningful alt text; decorative images `alt=""`.
- **Motion**: honor `prefers-reduced-motion`; no motion-only information.
- **Targets/zoom**: touch targets ≥ 44×44px; usable at 200% zoom and 320px width.
- **Components**: accessible dialogs, menus, carousels/galleries; map embeds have titles and a text directions link.
- **Screen reader**: navigate key flows (home → services → primary CTA) and confirm they make sense aurally.

## Report & fix

List issues by severity, fix everything controllable, and re-verify. Note any genuine third-party limitation (e.g. an embedded widget) honestly rather than hiding it.
