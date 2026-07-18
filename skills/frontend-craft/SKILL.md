---
name: frontend-craft
description: Implement production-quality responsive local-business websites — React, Astro, Vue, Svelte, Laravel/Blade, or plain HTML/CSS. Scope is local-business website work only (salons, law firms, restaurants, clinics, trades); do not use for general-purpose app development in these frameworks.
---

# Frontend Craft

## Scaffolding a new project

When the working directory has no existing project (empty, or no recognized framework/package manifest), scaffold one from scratch instead of assuming a stack:

1. Use the brief's "Framework/hosting constraints" answer if the user gave one. Otherwise recommend a stack using the rules below and confirm it in one line before running any scaffold command — don't scaffold on a guess without a quick check-in.
2. Recommendation rules when unstated:
   - Booking/reservation is a primary or secondary conversion → **Laravel + Blade + Livewire** (pairs directly with `../booking-engine/SKILL.md`; add Filament for the admin side). Use **Laravel + Inertia + React** instead only if the brief explicitly wants a React frontend.
   - Brochure/marketing site with no booking backend → **Astro** — best default for SEO and performance on a content-led local-business site; drop in a React/Vue island only where real interactivity is needed.
   - Brief names a specific stack or host (Vercel, Cloudflare Pages, an existing React team, shared PHP hosting) → follow it, and match the two: Vercel/Cloudflare Pages suit Astro, shared PHP hosting suits Laravel, plain HTML needs no host-specific tooling.
3. Scaffold commands:
   - **Astro**: `npm create astro@latest . -- --template minimal --install --git --yes`
   - **React + Vite (SPA)**: `npm create vite@latest . -- --template react-ts`
   - **Vue**: `npm create vite@latest . -- --template vue-ts`
   - **Svelte**: `npm create vite@latest . -- --template svelte-ts`
   - **Laravel + Blade**: `laravel new . --no-interaction` (fall back to `composer create-project laravel/laravel .` if the `laravel` installer isn't available)
   - **Laravel + Inertia + React**: `laravel new . --react --no-interaction`
   - **Plain HTML/CSS**: no scaffold tool — create the file structure directly.
4. Once scaffolded, everything else in this file applies exactly as it would to a pre-existing project of that stack — there's no separate, lower bar for a project Claude just created.

## Implementation

- Preserve the detected stack, routing, package manager, linting, and component conventions — or the one just scaffolded above.
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
