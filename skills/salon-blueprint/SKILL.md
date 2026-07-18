---
name: salon-blueprint
description: Plan and build conversion-focused websites for hair salons, beauty salons, spas, nail studios, lash and brow studios, makeup artists, and barbershops. Use for salon briefs, salon redesigns, salon service menus, galleries, stylist pages, local SEO, WhatsApp/contact conversion, and appointment-booking experiences.
---

# Salon Blueprint

Read `references/content-model.md` when structuring business data. Read `references/page-recipes.md` when planning pages or sections.

## Fast intake

Require only business name, salon type, location, main services, primary action, and contact method to begin. Accept a complete brief when supplied. Mark unknown facts as placeholders; never invent prices, staff, reviews, awards, address, or opening hours.

## Choose one conversion model

- **Lead-first:** WhatsApp, call, or inquiry. Use when no real booking backend exists.
- **External booking:** Link to the salon's verified Fresha, Booksy, Square, Vagaro, or other provider without simulating availability.
- **Native booking:** Load `../booking-engine/SKILL.md`; build server-validated availability and conflict protection.

Never present a fake booking calendar or simulated success as functional booking.

## Build order

1. Create the structured salon data source.
2. Build the shared shell, navigation, persistent mobile booking action, and footer.
3. Build Home and Services first; verify the primary action.
4. Add Gallery, Team, About, and Contact only when supported by the brief.
5. Source imagery, implement local SEO, and run responsive/launch audits.

## Salon-specific quality bar

- Group services into scannable categories with confirmed price and duration.
- Let gallery filters correspond to real service categories.
- Connect each stylist CTA to that stylist or service when booking supports it.
- Put location, hours, phone, WhatsApp, directions, and cancellation policy where customers can find them quickly.
- Avoid beauty claims that imply guaranteed outcomes.
- Design for one-handed mobile use; keep the primary booking/contact action reachable.
- Use one original art direction appropriate to the brand, not the same pastel template for every salon.
