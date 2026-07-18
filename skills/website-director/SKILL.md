---
name: website-director
description: Orchestrate an end-to-end premium local-business website build or redesign. Use for salons, law firms, restaurants, clinics, trades, agencies, and other location-based service businesses when the user asks to create, improve, or complete a website.
---

# Website Director

## Workflow

1. Inspect the repository, framework, routes, components, styles, assets, scripts, and current git state — or confirm the working directory is empty/has no recognized project. Laravel/Composer/Blade is a recognized stack alongside React, Astro, Vue, Svelte, and plain HTML. Also check for a saved `project-brief.md` at the project root — if it exists **and has a business name filled in** (not an empty/unfilled template), read it and skip straight to step 6, asking only about anything the user wants to add or change. An empty or unfilled `project-brief.md` counts as no saved brief.
2. Default to showing the brief. Skip straight to step 3 **only** if one of these is true — otherwise, always respond with **only** the brief below (nothing else in that message, no other question bundled in), ask the user to fill in and paste back what they can, make clear they can leave fields blank, then stop and wait for their reply:
   - The user's message already contains a **substantially filled-out brief** — most fields answered, not just the business name or a one-line project description. A message like "build a website for my hair salon" does **not** qualify; that's a project description, not a completed brief, and still needs the template shown.
   - The user has explicitly said something like "skip the brief" / "just use placeholders" / "you decide."

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

3. When the reply arrives — even if it's partial, or they just say "skip it" / "use placeholders" — confirm what you captured in a short summary that names anything you're treating as a placeholder, and ask for a go-ahead before building. Do not re-send the brief template again and do not re-ask for fields already left blank. If a field material to the design (business name, vertical, primary conversion) is still missing, ask about that one specifically as part of this same confirmation message, not as a separate round. If there's still no new information after that single follow-up, proceed with placeholders — never loop back to asking a third time.
4. Once confirmed, convert it into a compact site plan: audience, primary conversion, pages, required content, trust signals, integrations, and constraints.
5. Save the finalized brief — real answers plus clearly labeled placeholders — to `project-brief.md` in the project root, so a future session reads it back in step 1 instead of asking again.
6. Determine the project type. If it isn't already obvious from the brief, ask this **on its own**, in a separate message from the brief/confirmation exchange above:

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
7. Load `../industry-blueprints/SKILL.md` and select the closest vertical.
8. Load `../art-direction/SKILL.md` before choosing layout, typography, color, imagery, motion, and component language.
9. Load `../conversion-copy/SKILL.md` for page copy and calls to action.
10. If the project type from step 6 is "frontend + booking" or "ERP / management system," load `../booking-engine/SKILL.md` before implementation — see that skill for how ERP-tier scope differs from plain booking.
11. Load `../frontend-craft/SKILL.md` while implementing.
12. If any image placeholders remain (no real business photos were provided for them), load `../stock-imagery/SKILL.md` to source and verify real, working images before moving on.
13. Load `../launch-audit/SKILL.md` before completion and fix material failures.

## Default page set

Build Home, About, Services/Pricing, Team, Gallery or Work, Contact, location/opening-hours content, testimonials, social links, and legally appropriate footer links. Combine pages only when the business or brief benefits from a focused one-page site.

## Operating rules

- Ask one question per message and wait for the reply before asking the next. Never bundle the brief request, its confirmation, and the project-type question into a single message.
- A short project description ("build me a salon website") is never a substitute for the brief — always show the actual brief template first unless the user already pasted a substantially completed one or explicitly said to skip it.
- Never re-ask for information the user already left blank or declined to give — confirm what you have (naming placeholders) and move forward. A field gets at most one follow-up, ever.
- Never imitate a reference site exactly. Extract principles and create an original design.
- Do not use fake awards, reviews, people, case results, statistics, addresses, or certifications. Clearly label demo content.
- Prefer one strong visual concept over a collage of unrelated UI trends.
- Make every page usable at 320px width through wide desktop screens.
- Use real integrations only when keys/configuration exist; otherwise provide a graceful placeholder and setup note.
- Finish the implementation, run relevant checks, and report only genuine remaining blockers.
