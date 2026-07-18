---
name: responsive-design
description: Build every local-business website mobile-first and fully responsive across all devices — phones, tablets, laptops, desktops, and large screens. Use during implementation of any site, in any stack, and verify the result at real breakpoints before handoff.
---

# Responsive Design

Every site this plugin builds is mobile-first and works on any device in the world. Most local-business traffic — salons especially — is on phones, so the phone layout is the primary design, not an afterthought squeezed down from desktop.

## Mobile-first method

- Write base (unprefixed) CSS for the smallest screen — a single, comfortable column at ~320px. Layer wider layouts on top with `min-width` media queries; never start from a desktop layout and patch downward with `max-width` overrides.
- With Tailwind, this is the default: unprefixed utilities target mobile, and `sm:` / `md:` / `lg:` / `xl:` add complexity upward. Don't invert it.
- Reach for intrinsic layout before breakpoints: `flex-wrap`, CSS grid with `repeat(auto-fit, minmax(...))`, `clamp()` for fluid type and spacing. A layout that flexes on its own needs fewer hard breakpoints and adapts to screen sizes you didn't explicitly test.

## Breakpoints to design and check

Design so nothing breaks *between* these, not just at them:

- **320px** — small phone. The true floor. No horizontal scroll, ever.
- **375px** — typical phone.
- **414–430px** — large phone.
- **768px** — tablet portrait.
- **1024px** — tablet landscape / small laptop.
- **1280–1440px** — desktop.
- **1920px+** — large/wide screens: cap content width (e.g. `max-width` on a centered container) so line lengths stay readable and the layout doesn't stretch edge-to-edge.

## Rules that must hold at every width

- No horizontal overflow. Watch fixed widths, oversized images, wide tables, `100vw` inside padded containers, and long unbroken strings (URLs, emails) — use `max-width: 100%`, `overflow-x-auto` on wide tables, and `overflow-wrap: break-word`.
- Touch targets at least 44×44px with adequate spacing — no tiny tap zones, no links packed too close on mobile.
- Body text stays readable without zoom (~16px minimum on mobile); line length caps around 65–75 characters on wide screens.
- Include `<meta name="viewport" content="width=device-width, initial-scale=1">` — without it, mobile styles don't apply at all. Verify it's present in the base layout.
- Respect safe areas on notched devices where relevant (`env(safe-area-inset-*)`), and keep fixed/sticky headers from covering content or overlapping on short landscape screens.
- Navigation collapses to an accessible mobile menu (keyboard-operable, focus-trapped when open) per `../frontend-craft/SKILL.md`; the booking flow and any admin tables from `../booking-engine/SKILL.md` must be fully usable on a phone — stack or horizontally scroll wide tables rather than clipping them.
- Images use responsive sizing (`srcset`/`sizes`, or the framework's responsive image component) so phones don't download desktop-sized files.

## Verification

Responsive work isn't done until it's checked at real sizes, not assumed from the CSS. Using Playwright MCP or whatever browser automation is available (same pattern as `../image-pipeline/SKILL.md`):

1. Load every page at 320, 375, 768, 1024, and 1440px, plus one large width (1920px).
2. At each width confirm: no horizontal scrollbar, no clipped or overlapping text, no element escaping the viewport, tap targets aren't cramped, and the mobile menu opens/closes and traps focus.
3. Screenshot each page at mobile and desktop widths to confirm the layout visually holds, not just that the DOM fits.
4. Check one short-height landscape case (e.g. 812×375) so a fixed header doesn't swallow the hero.
5. Fix anything that breaks and re-check that width — don't leave a known overflow or an unreachable control.
