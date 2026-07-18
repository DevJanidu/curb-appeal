---
name: security-audit
description: Check a site (especially any backend, booking, or forms) for common web security issues — CSRF, input validation, authorization, secrets handling, XSS/SQL safety, uploads, webhook signatures, headers, and dependency hygiene. Use at the TEST state for any build with a backend or forms.
---

# Security Audit

Scope scales with the build: a static brochure needs headers + no leaked secrets; a Laravel booking/ERP build needs the full list.

## Always

- No secrets committed (`.env`, API keys, tokens) — verify `.gitignore` covers them; never embed secret keys in client-side code.
- Security headers where the host allows (CSP, `X-Content-Type-Options`, `Referrer-Policy`, HSTS on HTTPS).
- No verbose error/debug output in production.
- Dependencies free of known-critical advisories (`npm audit` / `composer audit`).

## Backend (Laravel / any server)

- CSRF protection on all state-changing forms.
- Server-side validation on every input (Form Requests); never trust client values (durations, prices, slot validity — ties to `../booking-engine/SKILL.md`).
- Authorization checks on staff/admin/booking-management actions (policies/gates), not just authentication.
- Parameterized queries / ORM only — no string-built SQL. Escape output to prevent XSS.
- File uploads: validate type/size, store outside the webroot or on object storage, never trust the filename.
- Webhook endpoints: verify provider signatures and process idempotently (payments especially).
- Rate limiting on auth, forms, and booking endpoints. Audit logs for sensitive actions; sensible data retention.

## Rule

Never weaken authentication, disable CSRF, or expose secrets to make a test pass — fix the test setup instead. Report findings by severity and fix controllable ones before launch.
