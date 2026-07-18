---
name: frontend-craft
description: Implement production-quality responsive local-business websites — Next.js, React, Astro, Vue, Svelte, Laravel/Blade, or plain HTML/CSS. Scope is local-business website work only (salons, law firms, restaurants, clinics, trades); do not use for general-purpose app development in these frameworks.
---

# Frontend Craft

## Implementation

- Preserve the detected stack, routing, package manager, linting, and component conventions.
- Build semantic page landmarks and reusable components without premature abstraction.
- Store repeated business data—services, staff, testimonials, hours, navigation—in structured data rather than duplicated markup.
- Use responsive images with explicit dimensions, meaningful alt text, lazy loading below the fold, and optimized formats supported by the framework.
- Make navigation, menus, dialogs, galleries, forms, and carousels keyboard accessible.
- Give forms real labels, validation messages, loading/success/error states, spam mitigation hooks, and a working submission target or clearly documented adapter.
- Add map embeds with accessible titles and a direct directions link; defer loading when practical.
- Add per-page metadata, canonical handling where supported, Open Graph basics, sitemap/robots support, and valid LocalBusiness-derived structured data using verified facts only.
- Respect `prefers-reduced-motion`, visible focus, contrast, touch targets, and zoom.

## Laravel / Blade implementation

- Compose views from a shared Blade layout plus `x-` components (e.g. `<x-service-card>`, `<x-nav>`) — same "reusable components without premature abstraction" rule as any other stack.
- Validate every form server-side with a dedicated Form Request class; return old input and field-level errors to Blade via `@error`/`old()` rather than hand-rolled validation.
- Build CSS/JS through Vite (`resources/css`, `resources/js`, `@vite` directive) — do not hand-link unbundled assets.
- Include `@csrf` on every POST/PUT/DELETE form.
- Prefer route-model binding and named routes over hardcoded URLs.
- Every rule elsewhere in this file (semantic landmarks, structured data over duplicated markup, accessible forms/galleries/dialogs, metadata, responsive checkpoints) applies to Blade output exactly as it does to JSX or plain HTML — there is no separate, lower bar for server-rendered PHP views.

## Responsive checkpoints

Check at approximately 320, 375, 768, 1024, and 1440px. Prevent clipped text, horizontal overflow, overlapping fixed elements, unreadable line lengths, and oversized hero sections on short screens.
