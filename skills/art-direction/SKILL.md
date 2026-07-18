---
name: art-direction
description: Create an original premium visual system for a local-business website, including typography, color, spacing, imagery, layouts, components, and restrained motion. Use before or during frontend design of a local-business site.
---

# Art Direction

1. Define a three-word direction tied to the business, such as `editorial / serene / precise`.
2. Establish design tokens for color, type, spacing, radius, shadows, container widths, and motion.
3. Choose one display face and one highly readable text face when available; provide resilient fallbacks.
4. Create hierarchy through scale, spacing, composition, and imagery—not excessive cards, gradients, or decoration.
5. Use a restrained palette with one action color and verified contrast.
6. Favor authentic business imagery. If assets are missing, use intentional neutral compositions or clearly labeled placeholders.

## Anti-generic rules

- Avoid default SaaS dashboards, random glassmorphism, excessive pills, repeated card grids, and purple-gradient templates unless the brand calls for them.
- Vary section rhythm: editorial split, full-bleed visual, focused proof row, structured list, and strong closing composition.
- Keep motion subtle, purposeful, and disabled or reduced for `prefers-reduced-motion`.
- Ensure hover states have equivalent keyboard/focus behavior.

## Two reference direction archetypes

Use these as concrete starting points when a brief calls for either extreme — pick one, don't blend them, and still complete step 1's three-word direction for the specific business.

- **Sharp/editorial**: `--radius: 0` everywhere (buttons, cards, images, inputs — full squares/rectangles), high-contrast palette, bold or uppercase micro-labels and eyebrows, hover communicated through underline, color-invert, or border-weight change rather than shadow or radius change. The sharpness itself is the decoration, so keep spacing, type scale, and section rhythm restrained — do not stack it with heavy shadows or gradients.
- **Soft/spa**: generous radius, pastel-plus-one-accent palette, airy whitespace, rounded imagery crops. Decoration stays minimal here too — softness comes from color and spacing, not added ornament.

## Scroll-revealed gallery motion

When a brief calls for a gallery that animates in on scroll:

- Trigger reveals with `IntersectionObserver` or native CSS scroll-driven animations — avoid scroll-position math in JS.
- Animate only `transform` and `opacity` (translate/fade) so the browser never has to recalculate layout.
- Stagger items within a row by roughly 60–100ms so the reveal reads as a sequence, not a flash.
- Lazy-load offscreen images so the reveal animation isn't racing an unloaded image.
- Must no-op under `prefers-reduced-motion` per the anti-generic rules above — images should simply be present, not animated in.
