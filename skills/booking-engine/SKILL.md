---
name: booking-engine
description: Implement appointment/reservation booking for local businesses — data model, availability, conflict prevention, notifications, and staff-facing management. Use whenever booking a service or table is a primary or secondary conversion (salons, clinics, trades, restaurants with reservations), and as the foundation for an ERP/management-tier project.
---

# Booking Engine

## Data model

- `services` — name, duration, price, category.
- `staff` — name, bio, photo, specialties.
- `availability` — recurring working hours per staff member, plus one-off exceptions (time off, holidays).
- `appointments` — service, staff, customer, start/end time, status (pending, confirmed, cancelled, completed).
- `customers` — name, contact details, notes.

Normalize rather than duplicating service/staff data onto each appointment row. Index `appointments.starts_at` and `appointments.staff_id` — availability queries filter on both constantly.

## Conflict prevention

Compute available slots server-side as: staff working hours, minus existing appointments, minus time-off exceptions, minus any configured buffer time between bookings. Never trust a client-submitted slot as valid — re-check for conflicts inside a database transaction at submission time so two customers can't win the same slot in a race condition. A failed re-check should return the customer to slot selection with a clear message, not a generic error.

Store timestamps in UTC and convert using the salon's configured IANA timezone. Calculate the appointment end from the authoritative service duration, never a client value. Treat pending appointments as slot-blocking only for a defined expiry window. Enforce conflict safety with both a transaction/lock and a database constraint or equivalent overlap strategy where the database supports it; an application-only pre-check is race-prone.

Define before launch: minimum notice, maximum advance window, buffers, cancellation/reschedule window, no-show handling, deposit behavior, taxes, and whether staff selection is optional. Do not guess these policies.

## Interactive booking UI

Drive a 4-step flow — service → stylist/staff (skippable if irrelevant) → date/time → customer details — with a Livewire component (or Alpine.js plus a small JSON availability endpoint if Livewire isn't already in the stack) so slots update live as the customer narrows their choice, with no full-page reload between steps. Because this is a public conversion path, ensure a no-JS fallback works: a plain multi-step Blade form that posts and re-renders server-side still completes a booking.

## Notifications

Send booking confirmation immediately on-screen, then follow up with a Laravel Notification (mail, and SMS via a documented-but-optional channel) plus a reminder before the appointment. Dispatch both as queued jobs, not inline — note in the project's setup docs that a queue worker (`php artisan queue:work`, or a supervisor/systemd entry in production) must be running or these notifications silently never send.

## Admin / staff management

Default to Filament for the staff-facing side — appointments calendar/list, staff CRUD, services CRUD — unless the host project already has an established admin pattern, in which case preserve that instead (per `../website-director/SKILL.md`'s rule to preserve existing conventions).

When the project type is ERP/management rather than plain booking, treat this admin surface as the primary deliverable, not a secondary add-on — staff scheduling, service catalog, and appointment oversight are core to the build. Add inventory, reporting, or other modules only if the brief specifically asks for them; don't invent ERP scope beyond what's requested.

## Testing

Write a PHPUnit feature test that attempts to double-book the same staff member/slot and asserts the second attempt is rejected — this is the one part of the domain that's easy to get subtly wrong (off-by-one buffer math, timezone handling, race conditions) and cheap to pin down with a test.

Also test adjacent slots, buffers, time off, daylight-saving/timezone conversion when relevant, expired pending holds, cancellation releasing a slot, authorization for staff/admin actions, and notification retries. For deposits, use provider webhooks as the payment source of truth and make webhook processing idempotent.
