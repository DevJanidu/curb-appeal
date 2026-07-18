---
name: frontend-craft
description: Implement production-quality responsive local-business websites — React, Astro, Vue, Svelte, Laravel/Blade, or plain HTML/CSS. Scope is local-business website work only (salons, law firms, restaurants, clinics, trades); do not use for general-purpose app development in these frameworks.
---

# Frontend Craft

## Scaffolding a new project

When the working directory has no existing project, `../website-director/SKILL.md` step 4 determines the project type and — for anything beyond a plain frontend — the stack before this step runs. Scaffold accordingly:

- **Frontend only → Astro**: `npm create astro@latest . -- --template minimal --install --git --yes`
- **Laravel + Blade + Livewire** (recommended for frontend + booking, or ERP/management): `laravel new . --no-interaction` (fall back to `composer create-project laravel/laravel .` if the `laravel` installer isn't available)
- **Laravel + Inertia + React**: `laravel new . --react --no-interaction`
- **React + Vite only**, booking/ERP logic served by a separate API: `npm create vite@latest . -- --template react-ts`

Once scaffolded, everything else in this file applies exactly as it would to a pre-existing project of that stack — there's no separate, lower bar for a project Claude just created. For an existing Vue, Svelte, or plain HTML project found in step 1, the general rules below still apply even though those aren't offered as fresh-scaffold choices.

## Implementation

- Preserve the detected stack, routing, package manager, linting, and component conventions — or the one just scaffolded above.
- Build semantic page landmarks and reusable components without premature abstraction.
- Store repeated business data—services, staff, testimonials, hours, navigation—in structured data rather than duplicated markup.
- Use responsive images with explicit dimensions, meaningful alt text, lazy loading below the fold, and optimized formats supported by the framework.
- Make navigation, menus, dialogs, galleries, forms, and carousels keyboard accessible.
- Give forms real labels, validation messages, loading/success/error states, spam mitigation hooks, and a working submission target or clearly documented adapter.
- Add map embeds with accessible titles and a direct directions link; defer loading when practical.
- Add per-page metadata, canonical handling, Open Graph tags, sitemap/robots support, and structured data — see `../seo/SKILL.md` for the full requirements and stack-specific notes.
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
