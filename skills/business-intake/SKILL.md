---
name: business-intake
description: Collect business information from a non-technical user in plain language — offer to accept a full brief, ask simple progressive questions, or use safe placeholders. Use at the INTAKE state before planning any build.
---

# Business Intake

Non-technical users don't know what a "brief" is. Offer three ways in, then collect only what's needed.

## Opening choice

Present exactly this, then wait:

```
I can build this from a complete website brief or a few business details.

1. I have a complete brief — I'll paste it
2. Ask me simple questions
3. Use safe placeholders and let me replace them later
```

- **Option 1**: accept the pasted brief, confirm what was captured, continue.
- **Option 2**: progressive questions (below).
- **Option 3**: proceed with clearly labeled placeholders; record what must be replaced before launch.

## Progressive questions (option 2)

Ask one at a time, plain language, only these to start:

1. Business name
2. Business type (salon, restaurant, law firm, …)
3. Location (city/area)
4. Main services (a few)
5. Main thing you want visitors to do (call, WhatsApp, book, visit)
6. Best contact method

Then ask optional details **only when useful** and one topic at a time: logo, colors, description, prices, staff, hours, address, phone, WhatsApp, email, socials, testimonials, photos, reference sites, booking provider, special features.

## Hard rules

- Never ask the same question twice, and never loop back over a field the user skipped. After one optional follow-up, continue with a labeled placeholder.
- Never invent addresses, phone numbers, staff, testimonials, reviews, awards, certifications, prices, statistics, history, hours, availability, or regulated claims. Unknown = placeholder, per `../content-integrity/SKILL.md`.
- Track three buckets: **confirmed** (real answers), **safe placeholders** (labeled, replace later), **required-before-launch** (must be real before the site goes live — e.g. real phone if the primary action is "call").
- Hand the three buckets to `../project-planner/SKILL.md`, which writes them to `project-brief.md` and the state file.
