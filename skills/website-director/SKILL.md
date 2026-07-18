---
name: website-director
description: Orchestrate an end-to-end premium local-business website build or redesign. Use for salons, law firms, restaurants, clinics, trades, agencies, and other location-based service businesses when the user asks to create, improve, or complete a website.
---

# Website Director

## Workflow

1. Inspect the repository, framework, routes, components, styles, assets, scripts, and current git state — or confirm the working directory is empty/has no recognized project. Laravel/Composer/Blade is a recognized stack alongside Next.js, React, Astro, Vue, Svelte, and plain HTML.
2. If the user's message doesn't already contain brief details (business name, industry, services, etc.), respond with the brief below and ask them to fill in and paste back what they can. Make clear they can leave fields blank — nothing is required. Wait for their reply before moving to step 3.

   ```
   # Website brief

   - Business name:
   - Industry:
   - Location/service area:
   - Primary audience:
   - Primary conversion:
   - Secondary conversion:
   - Required pages:
   - Services and prices:
   - Team members:
   - Brand colors/fonts:
   - Existing logo/photos:
   - Address, phone, email, hours:
   - Social links:
   - Testimonials (verified):
   - Integrations:
   - Reference sites (for direction only):
   - Framework/hosting constraints:
   ```

3. Convert the reply into a compact site plan: audience, primary conversion, pages, required content, trust signals, integrations, and constraints. For anything still missing that's material to the design (business name, vertical, primary conversion), ask one short follow-up question rather than guessing. For everything else, make a sensible assumption and mark it as a clearly labeled placeholder.
4. If step 1 found no existing project, scaffold one now — see `../frontend-craft/SKILL.md` for stack selection and the exact scaffold commands. Use the brief's "Framework/hosting constraints" answer when given; otherwise apply the recommendation rules there and confirm the inferred choice in one line before scaffolding.
5. Load `../industry-blueprints/SKILL.md` and select the closest vertical.
6. Load `../art-direction/SKILL.md` before choosing layout, typography, color, imagery, motion, and component language.
7. Load `../conversion-copy/SKILL.md` for page copy and calls to action.
8. If booking or reservation is a primary or secondary conversion (salons, clinics, trades, restaurants with reservations), load `../booking-engine/SKILL.md` before implementation.
9. Load `../frontend-craft/SKILL.md` while implementing.
10. Load `../launch-audit/SKILL.md` before completion and fix material failures.

## Default page set

Build Home, About, Services/Pricing, Team, Gallery or Work, Contact, location/opening-hours content, testimonials, social links, and legally appropriate footer links. Combine pages only when the business or brief benefits from a focused one-page site.

## Operating rules

- Never imitate a reference site exactly. Extract principles and create an original design.
- Do not use fake awards, reviews, people, case results, statistics, addresses, or certifications. Clearly label demo content.
- Prefer one strong visual concept over a collage of unrelated UI trends.
- Make every page usable at 320px width through wide desktop screens.
- Use real integrations only when keys/configuration exist; otherwise provide a graceful placeholder and setup note.
- Finish the implementation, run relevant checks, and report only genuine remaining blockers.
