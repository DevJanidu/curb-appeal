---
name: website-director
description: Orchestrate an end-to-end premium local-business website build or redesign. Use for salons, law firms, restaurants, clinics, trades, agencies, and other location-based service businesses when the user asks to create, improve, or complete a website.
---

# Website Director

## Workflow

1. Inspect the repository, framework, routes, components, styles, assets, scripts, and current git state — or confirm the working directory is empty/has no recognized project. Laravel/Composer/Blade is a recognized stack alongside React, Astro, Vue, Svelte, and plain HTML.
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
   ```

3. Convert the reply into a compact site plan: audience, primary conversion, pages, required content, trust signals, integrations, and constraints. For anything still missing that's material to the design (business name, vertical, primary conversion), ask one short follow-up question rather than guessing. For everything else, make a sensible assumption and mark it as a clearly labeled placeholder.
4. Determine the project type — ask if it isn't already clear from the brief:

   ```
   What kind of project is this?
   1. Frontend only — a marketing/brochure site, no booking or backend
   2. Frontend + booking — a customer-facing appointment/reservation system
   3. ERP / management system — full salon or business management (staff, scheduling, service catalog, reporting) beyond customer-facing booking
   ```

   - **Frontend only** → scaffold **Astro**, no further question.
   - **Frontend + booking** or **ERP / management system** → ask which stack before scaffolding:

     ```
     Which stack should I build it in?
     1. Laravel + Blade + Livewire (recommended — simplest path, pairs directly with this plugin's booking and admin tooling)
     2. Laravel + Inertia + React (same backend, React-based frontend)
     3. React + Vite frontend only, talking to a separate API you already have or will build (advanced — this plugin's booking/admin guidance assumes a Laravel backend)
     ```

   If step 1 found an existing project, skip both questions above and keep using its existing stack instead. Otherwise scaffold per `../frontend-craft/SKILL.md`'s commands for whichever combination results.
5. Load `../industry-blueprints/SKILL.md` and select the closest vertical.
6. Load `../art-direction/SKILL.md` before choosing layout, typography, color, imagery, motion, and component language.
7. Load `../conversion-copy/SKILL.md` for page copy and calls to action.
8. If the project type from step 4 is "frontend + booking" or "ERP / management system," load `../booking-engine/SKILL.md` before implementation — see that skill for how ERP-tier scope differs from plain booking.
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
