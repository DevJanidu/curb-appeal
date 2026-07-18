---
name: form-integrations
description: Wire contact and inquiry forms to a real, working target — never a form that fakes success. Supports Laravel, SMTP, Resend, Formspree, Web3Forms, webhook, CRM, and WhatsApp adapters, with validation, accessible states, and spam protection. Use at the INTEGRATIONS state.
---

# Form Integrations

## Non-negotiable

No form may show a success message unless it actually delivered to a real target. If nothing is configured, mark the form **pending** (a visible, honest note) and never simulate a successful submission.

## Adapters

Pick based on stack and what the user has:

- **Laravel**: controller → database + queued mail notification (the default for a Laravel build).
- **SMTP / Resend**: transactional email when there's no app backend.
- **Formspree / Web3Forms**: hosted form endpoints for static/Astro sites with no backend.
- **Webhook / CRM**: POST to a provided endpoint (Zapier, HubSpot, etc.).
- **WhatsApp**: a `wa.me` link with a prefilled message — valid as a primary contact path, but it's a link, not a form submission.

## Every form must have

- Real `<label>`s tied to inputs; required/optional marked.
- Server-side validation where a backend exists; client-side assistance always.
- Distinct **loading**, **success**, and **failure** states, announced to screen readers (`aria-live`).
- Spam mitigation: honeypot + timing check at minimum; rate limiting on the backend.
- Privacy consent where personal data is collected; never log full submissions with PII in plaintext.
- CSRF protection on backend forms (`@csrf` in Laravel).

## Verify

Submit the form end-to-end (or through the adapter's test mode) and confirm the message actually arrives before calling it done. A form that "looks wired" but delivers nowhere is a failure, not a placeholder. Coordinate booking flows with `../booking-engine/SKILL.md`.
