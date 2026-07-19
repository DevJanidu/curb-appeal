---
name: status-badge-system
description: Create, migrate, and audit a centralized, accessible status badge system across business applications. Use whenever tables, cards, dashboards, detail pages, forms, modals, filters, bookings, appointments, payments, invoices, inventory, orders, users, staff, services, or other records display workflow/status values with plain text, beige labels, duplicated styles, or inconsistent colors.
---

# Status Badge System

Build one reusable badge component/helper and one status registry. Never reproduce status colors or label formatting inside individual pages.

Read `references/implementation.md` before implementing in React/Next.js, Laravel Blade/Livewire, Inertia, or a mixed application.

## Canonical variants

| Variant | Meaning | Background | Text | Border/dot |
|---|---|---|---|---|
| success | positive/complete | `#DCFCE7` | `#166534` | `#22C55E` |
| warning | waiting/attention later | `#FEF3C7` | `#92400E` | `#F59E0B` |
| info | active progress | `#DBEAFE` | `#1E40AF` | `#3B82F6` |
| danger | failed/negative | `#FEE2E2` | `#991B1B` | `#EF4444` |
| neutral | inactive/unknown | `#F3F4F6` | `#374151` | `#9CA3AF` |
| attention | exceptional follow-up | `#FFEDD5` | `#9A3412` | `#F97316` |

Use a soft background, darker readable text, one-pixel matching border, a small `aria-hidden` colored dot, rounded pill, medium weight, and consistent padding/size. Always render readable text; color and dot never replace the label. Preserve contrast in light/dark themes and forced-colors mode.

## Central registry

Store normalized keys in one configurable map:

- `success`: active, confirmed, completed, approved, paid, available, delivered, published, enabled, accepted, in-stock, open
- `warning`: pending, awaiting-approval, processing, on-hold, scheduled, partially-paid, low-stock, draft, waiting, under-review
- `info`: in-progress, ongoing, assigned, booked, dispatched, started, new, submitted
- `danger`: cancelled, rejected, failed, overdue, unpaid, out-of-stock, suspended, blocked, declined, expired
- `neutral`: inactive, disabled, archived, closed, unavailable, not-started, unknown, deleted
- `attention`: no-show, delayed, rescheduled, refunded, returned, partially-completed, needs-attention

Specific mappings override broad aliases. `no-show` is `attention`, not neutral. Unknown, null, or empty values render a safe neutral badge and never throw.

## Normalization and labels

Use one pure normalizer: convert nullish input to `unknown`; trim/lowercase; split camelCase; treat spaces, underscores, and repeated hyphens equally; collapse to one hyphen; apply explicit aliases such as `in-active` and `in_active` → `inactive`.

Use a separate label formatter. Prefer the registry label, then title-case normalized words. Preserve acronyms through explicit labels. Backend/database values and update payloads remain unchanged; normalization is presentation-only.

## Reactive behavior

After a successful mutation, update or invalidate authoritative client state immediately:

- React/Next/Inertia: update local/query state or invalidate/refetch the relevant query.
- Livewire: update bound component state and render the shared badge.
- Blade server post: redirect with fresh model state.

Optimistic updates require rollback on failure. Never leave a visually updated badge after the backend rejects the operation.

## Application-wide migration

Search the project for status columns, raw enum rendering, status ternaries, badge/chip classes, beige labels, and page-local maps. Replace every user-facing display with the shared component across tables, cards, details, dashboards, modals, forms, lists, mobile layouts, and printable views where color is appropriate.

Preserve selectors, filters, API values, database enums, policies, and update logic. Remove obsolete presentation helpers/styles only after confirming no consumers remain.

## Verification

Add unit tests for normalization, aliases, configured statuses, unknown/null fallback, labels, and precedence. Add component/browser tests for visible text, dot, contrast, responsive use, and immediate post-update rendering. Search again after migration and report intentional exceptions.

The work is incomplete while a user-facing raw status or conflicting legacy badge remains.
