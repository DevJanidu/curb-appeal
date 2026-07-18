---
name: industry-blueprints
description: Choose the right information architecture, trust signals, conversion paths, and page modules for salons, law firms, restaurants, and other local businesses. Use during website planning or vertical adaptation.
---

# Industry Blueprints

## Salon and beauty

- Primary conversions: book appointment, call, WhatsApp.
- Modules: service categories with duration/price, stylists, transformation gallery, testimonials, hygiene/brand story, location and hours, booking CTA.
- Tone: polished, warm, aspirational, easy to scan.

### Visual direction

Pick one archetype per brief in `../art-direction/SKILL.md` — do not default to the same look for every salon:

- **Soft/spa**: rounded corners, pastel-plus-one-accent palette, airy whitespace. Fits day spas, wellness-leaning salons, family-friendly barbers.
- **Sharp/editorial**: zero border-radius, high-contrast palette, bold geometric type. Fits high-fashion salons, barbershops, and brands wanting an assertive, modern edge.

### Booking flow

Service → stylist (optional, skippable) → date/time with live availability → customer details → confirmation, with an immediate on-screen confirmation plus email/SMS confirmation. Implement with `../booking-engine/SKILL.md`.

### Gallery

Organize transformation/before-after images into a grid by service category (color, cut, styling) rather than a single undifferentiated feed — visitors scan for the result they want. Reveal rows with the staggered scroll animation described in `../art-direction/SKILL.md`.

### Stylist/team module

Portfolio-card pattern per stylist: photo, name, specialty tags, and a "book with [name]" CTA that pre-selects them in the booking flow.

## Law firm

- Primary conversions: request consultation, call, submit confidential inquiry.
- Modules: practice areas, attorney credentials, process, jurisdictions served, representative outcomes only if verified and compliant, FAQs, disclaimers.
- Tone: calm, authoritative, clear. Avoid guarantees or unsupported claims.

## Restaurant and café

- Primary conversions: reserve, order, call, get directions.
- Modules: menu with dietary labels and prices, signature dishes, atmosphere gallery, hours, map, events/private dining, reservation CTA.
- Tone: sensory but concise. Keep menus accessible as HTML, not image-only PDFs.

## General local business

- Primary conversions: call, request quote, book, visit.
- Modules: outcome-led hero, service overview, proof, process, service area, team, FAQs, contact, map/hours.

## Selection rule

Choose one primary and one secondary conversion. Put the primary action in the header, hero, mid-page proof section, and closing CTA without making every section feel like an advertisement.
