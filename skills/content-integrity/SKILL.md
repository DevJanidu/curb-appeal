---
name: content-integrity
description: Detect and block fabricated or unsafe content — invented reviews, awards, statistics, staff, prices, placeholder contacts in production, generic AI filler, unsupported claims, NAP inconsistencies, placeholder JSON-LD, and empty CTAs. Use during CONTENT and again before TEST/launch.
---

# Content Integrity

Scan all copy and data before it ships. Classify every item as **Ready**, **Needs confirmation**, **Safe placeholder** (labeled, non-production-blocking), or **Blocked from publishing**.

## Block (never ship)

- Invented reviews, testimonials, ratings, awards, certifications, or statistics.
- Invented people (named staff without a real person behind them) or fabricated company history.
- Unconfirmed prices, hours, addresses, or phone numbers presented as real.
- Placeholder contact details (`example.com`, `555-…`, `Lorem ipsum`) left in production output.
- Placeholder or guessed values inside JSON-LD / structured data (machine-read — invisible to a human reviewer, so doubly dangerous).
- Regulated claims without required disclaimers (medical/legal/financial outcomes, guarantees).
- Copied text from a reference site.

## Flag (needs confirmation)

- Unsupported superlatives ("best", "#1", "leading") without evidence.
- Fake urgency/scarcity ("only 2 slots left") not backed by real data.
- NAP (name/address/phone) that differs between page content, footer, and structured data.
- Empty or dead CTAs (a "Book now" that goes nowhere — see `../form-integrations/SKILL.md`).
- Generic AI phrasing ("welcome to", "we pride ourselves", "nestled in the heart of").

## Report

Produce a short list grouped by the four classes. **Blocked** items must be fixed or removed before launch; **Safe placeholders** may ship if clearly labeled and listed in the client handoff's replace-before-launch section. Coordinate labeling with `../business-intake/SKILL.md`'s buckets and copy with `../conversion-copy/SKILL.md`.
