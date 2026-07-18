---
name: business-blueprints
description: Choose the right information architecture, conversions, pages, trust signals, schema type, and content rules per vertical — salon/beauty, barbershop, spa, restaurant, law firm, clinic, real estate, trades, hotel, gym, education, and general local business. Use during planning to adapt the build to the business type. Salons load ../salon-blueprint/SKILL.md for deeper coverage.
---

# Business Blueprints

Pick the closest vertical below. For salon/beauty/spa/barbershop/nail/lash, use `../salon-blueprint/SKILL.md` instead — it goes deeper. Each blueprint names: primary/secondary conversions, key pages, homepage modules, trust signals, required facts, schema.org type, and content restrictions. Never force one page structure across every vertical. Choose one primary and one secondary conversion and place the primary action in header, hero, mid-page proof, and closing CTA.

## Salon / beauty / spa / barbershop
Deep coverage in `../salon-blueprint/SKILL.md`. Conversions: book / call / WhatsApp. Schema: `HairSalon`/`BeautySalon`/`NailSalon`/`DaySpa`.

## Restaurant / café
- Conversions: reserve, order, call, directions.
- Modules: HTML menu with prices/dietary labels, signature dishes, atmosphere gallery, hours, map, events/private dining.
- Trust: real reviews, hygiene rating if verified. Schema: `Restaurant`. Keep menus as HTML, never image-only PDFs.

## Law firm
- Conversions: request consultation, call, confidential inquiry.
- Modules: practice areas, attorney credentials, process, jurisdictions, verified outcomes only, FAQs, disclaimers.
- Restrictions: no guarantees, no unverified outcome claims. Tone: calm, authoritative. Schema: `Attorney`/`LegalService`.

## Clinic / medical / dental
- Conversions: book appointment, call, new-patient inquiry.
- Modules: services/treatments, practitioners + credentials, insurance/payment, patient info, hours, location, accessibility.
- Restrictions: no outcome guarantees, no unapproved medical claims; include required disclaimers. Schema: `MedicalClinic`/`Dentist`.

## Real estate
- Conversions: book viewing, request valuation, call, saved-search inquiry.
- Modules: listings/featured properties, agent profiles, areas served, process, testimonials. Schema: `RealEstateAgent`.

## Construction / trades
- Conversions: request quote, call, WhatsApp.
- Modules: services, project/portfolio gallery (real work only), service area, process, licensing/insurance if verified, guarantees only if real. Schema: `HomeAndConstructionBusiness` / specific trade type.

## Hotel / hospitality
- Conversions: check availability / book, call, directions.
- Modules: rooms/rates, amenities, gallery, location/attractions, policies, reviews. Schema: `Hotel`/`LodgingBusiness`. Never fake live availability.

## Gym / fitness / studio
- Conversions: start trial, book class, join, call.
- Modules: classes/schedule, memberships/pricing, trainers, facilities gallery, testimonials. Schema: `HealthClub`/`ExerciseGym`.

## Education / tutoring
- Conversions: enroll, book consultation, request info.
- Modules: programs/courses, outcomes, staff, schedule/terms, fees, FAQs. Schema: `EducationalOrganization`.

## General local business
- Conversions: call, request quote, book, visit.
- Modules: outcome-led hero, service overview, proof, process, service area, team, FAQs, contact, map/hours. Schema: `LocalBusiness`.

## Shared rules
- Required facts before launch: business name, address, phone, hours, at least one real conversion path. Mark anything unconfirmed as a placeholder per `../content-integrity/SKILL.md`; never invent it.
- Coordinate schema with `../seo/SKILL.md` and structure data via `../website-director/SKILL.md`'s central business-data source.
