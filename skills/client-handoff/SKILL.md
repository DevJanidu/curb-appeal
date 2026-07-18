---
name: client-handoff
description: Produce a plain-language handoff document for a non-technical owner — what was built, how to edit content/services/images, how forms and booking work, what still needs real information, and how to maintain the site. Use at the HANDOFF state. Never include credentials.
---

# Client Handoff

Write `HANDOFF.md` (or `README-client.md`) at the project root, in plain language a non-technical business owner can follow. No jargon, no credentials, ever.

## Include

1. **What was built** — the site in one paragraph, and the pages included.
2. **What visitors do** — the primary action (call/WhatsApp/book/enquire) and where it appears.
3. **Editing content** — where business info, services, prices, staff, and images live (the central business-data source), and how to change them safely.
4. **Forms & booking** — how they work, where submissions/appointments go, and what a customer experiences.
5. **Replace before launch** — every labeled placeholder and required-before-launch item from intake (real phone, address, hours, real photos, real prices). This is the most important section.
6. **Configuration needed** — any keys/services the owner must supply (SMTP/email, booking provider, image API, domain) — described, not the secret values themselves.
7. **SEO & testing** — what was set up (metadata, sitemap, structured data) and what was verified.
8. **Deployment** — how/where it goes live, per `../deployment-readiness/SKILL.md`.
9. **Maintenance** — routine updates, dependency updates, backups.

## Rules

- Never write real passwords, API keys, or tokens into the handoff.
- Be honest about what is a placeholder and what is production-ready — pair with `../content-integrity/SKILL.md`'s report.
- Keep it short and scannable; a business owner should be able to act on it without asking follow-up questions.
