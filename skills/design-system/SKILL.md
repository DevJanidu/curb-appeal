---
name: design-system
description: Produce a deterministic visual system before building pages — a three-word direction, color/type roles, scales, spacing, radius, shadows, component styles, imagery mood, motion, and breakpoints. Use at the BUILD state before any page markup. Supersedes ad-hoc styling.
---

# Design System

Generate tokens **before** pages, so every page draws from one system instead of improvised styling. This absorbs and formalizes `../art-direction/SKILL.md`'s direction step.

**Default direction**: `website-director` now defaults new builds to `../editorial-luxury-theme/SKILL.md` (a fixed "sharp editorial luxury" system — zero radius, espresso/gold, Poppins). Use this skill's direction picker only when the brief clearly wants something else (soft/rounded spa, playful/family business, or client-supplied brand that conflicts with editorial luxury).

## 1. Pick one direction

Choose a single named direction that fits the brand — never blend several:

`luxury minimal` · `soft spa` · `organic wellness` · `sharp editorial` · `modern feminine` · `premium barbershop` · `clinical beauty` · `warm family` · `professional corporate` · `bold contemporary` · `rustic local` · `elegant hospitality`

State it as a three-word direction (e.g. `warm / tactile / confident`).

## 2. Emit tokens

Define, as real tokens in the stack's idiom (CSS custom properties, Tailwind theme, etc.):

- **Color roles**: background, surface, text, muted text, border, one primary action color (verified contrast ≥ 4.5:1 for text), one accent. Not a random palette — roles.
- **Type**: one display face + one readable text face with resilient fallbacks; a modular scale.
- **Spacing scale**, **container widths**, **radius** (0 for sharp/editorial, generous for soft/spa), **shadow** levels, **motion** durations/easing (reduced under `prefers-reduced-motion`).
- **Breakpoints**: align to `../responsive-design/SKILL.md`.

## 3. Component styles

Define button (primary/secondary/ghost), form field + error state, card, nav, footer, and image treatment from the tokens — so components are consistent by construction.

## Anti-generic rules

- Don't default every salon to pastel + rounded cards. Match the direction to the actual brand.
- Don't make a local-business site look like a generic SaaS dashboard (no random glass panels, gradient hero blobs, or endless card grids).
- Create hierarchy through scale, spacing, and composition — not decoration piled on. Hand tokens to `../frontend-craft/SKILL.md` for implementation.
