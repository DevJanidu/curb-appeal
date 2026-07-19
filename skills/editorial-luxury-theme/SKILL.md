---
name: editorial-luxury-theme
description: Apply the "Sharp Editorial Luxury" visual system — zero-radius cards/buttons, espresso/taupe/gold palette, Poppins, uppercase letter-spaced labels with eyebrow accents, and a fixed component set (hero, cards, wizard, footer, WhatsApp widget). Use as the default visual direction for new local-business builds instead of picking a fresh direction in design-system, unless the brief clearly calls for a different feel (e.g. a playful kids' business, a soft spa wanting rounded softness).
---

# Editorial Luxury Theme

A concrete, ready-to-apply visual system extracted from a production salon build. Use this in place of the "pick one direction" step in `../design-system/SKILL.md` when the brief doesn't push toward a different aesthetic. It still needs `../design-system/SKILL.md`'s process (tokens before pages) — this skill supplies the actual token values and component patterns instead of inventing new ones each time.

## Direction

`sharp / editorial / confident` — hard edges, generous whitespace, restrained gold accents, uppercase micro-type. Never soften this into rounded corners or pastel colors; the zero-radius rule is the signature, not an oversight.

## When to deviate

Skip this theme (fall back to `../design-system/SKILL.md`'s full direction picker) when the brief explicitly wants: a soft/rounded spa or wellness feel, a playful/family/children's business, a budget/casual trade business, or the client supplies their own brand colors and type that conflict with espresso/gold. Otherwise, use this as the default.

## Core tokens

```css
:root {
  --primary-color: #3F352C;   /* espresso — primary actions, headers, footer */
  --secondary-color: #BDA18C; /* taupe/gold — accents */
  --accent-color: #BDA18C;
  --background-color: #FFFFFF;
  --text-color: #000000;

  --heading-font: 'Poppins', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --body-font: 'Poppins', system-ui, -apple-system, 'Segoe UI', sans-serif;

  --ivory-2: #FFFFFF;
  --card: #ffffff;
  --taupe: #B4A79E;
  --line: #E6DCD3;
  --gold-deep: #3F352C;
  --gold-soft: #BDA18C;
  --blush: #E6DCD3;

  /* Sharp, modern — cards & buttons have NO radius. Do not add one. */
  --radius: 0px;

  --shadow-sm: 0 2px 10px -4px rgba(0,0,0,0.16);
  --shadow-md: 0 18px 44px -26px rgba(0,0,0,0.30);
  --shadow-lg: 0 30px 70px -30px rgba(0,0,0,0.38);

  --container: 80%;
  --space: clamp(4rem, 9vw, 8rem);
  --transition: 0.35s cubic-bezier(.22,.61,.36,1);
}
```

Swap `--primary-color` / `--secondary-color` per brand if the client has existing colors, but keep the relationship (one dark neutral for surfaces/text, one warm muted accent) and keep radius at 0. Full starter stylesheet with every component class: `references/tokens.md`.

## Signature patterns (apply consistently)

- **Eyebrow label**: uppercase, `letter-spacing: 0.28em`, `font-size: 0.72rem`, with a 34px horizontal line before the text. Precedes every section heading.
- **Buttons**: uppercase, `letter-spacing: 0.14em`, `font-size: 0.8rem`, solid espresso fill, no radius, lift 2px + darken on hover. Variants: primary (espresso), accent (gold), outline, ghost (for dark hero backgrounds), whatsapp (brand green).
- **Cards**: 1px hairline border in `--line`, 4:5 (or 4:3 for services) media aspect-ratio, lift + image zoom on hover, footer row separated by a top hairline.
- **Header**: sticky, translucent-blur background, uppercase nav links with an underline sweep on hover/active.
- **Hero**: full-bleed image or slider, bottom-aligned content, dark gradient overlay, trust-badge row under a hairline divider.
- **Footer / CTA bands**: solid espresso background, cream/white text, gold-soft accents.
- **Booking/quote wizard**: numbered circular step indicators (filled espresso when active, gold with checkmark when done), option cards and date/slot grids with a hairline border that turns gold on hover and inverts to espresso when selected.
- **Forms**: uppercase labels, no-radius inputs, gold focus ring.

## Anti-drift rules

- Never introduce rounded corners on cards, buttons, or media — this breaks the "sharp" identity.
- Never swap Poppins for a serif or script display face without the client asking for a softer/traditional feel.
- Keep uppercase letter-spacing only on labels/buttons/nav, never on body copy or long headings.
- Hand the resulting tokens to `../frontend-craft/SKILL.md` for implementation in whatever stack the project uses (Blade classes, Tailwind config, Astro CSS, etc.) — this skill defines the system, not the markup.
