# Status badge implementation reference

## Contract

Expose one small API:

```text
StatusBadge(value, optionalLabel, optionalSize)
normalizeStatus(value) -> canonical key
getStatusDefinition(value) -> key, label, variant, colors
```

Keep the registry, aliases, label formatter, and variant tokens separate from rendering so filters, exports, tests, and server views can reuse them.

## TypeScript / React / Next.js

Use `components/ui/status-badge.tsx`, `lib/statuses.ts`, and tests. Define a typed variant union and immutable registry. The component accepts raw backend values and exposes stable `data-status`/`data-variant` attributes. Do not accept arbitrary color classes at page call sites.

With Tailwind, keep all six complete variant class sets statically discoverable in the component/variant utility. With CSS variables, define six global token sets selected through `data-variant`. After mutations, use the existing state tool (React state, TanStack Query, SWR, Redux, server refresh, or Inertia) to update the record or invalidate the exact query after success.

## Laravel Blade / Livewire

Recommended structure:

```text
app/Support/Statuses/StatusRegistry.php
app/View/Components/StatusBadge.php
resources/views/components/status-badge.blade.php
tests/Unit/StatusRegistryTest.php
```

Render `<x-status-badge :status="$record->status" />`. Keep normalization/matching out of Blade conditionals. Livewire must render the shared component from current state after a successful action. Preserve enum backing values, casts, migrations, and validation.

## Inertia React

Use the React component with raw Laravel values. After success, update the row or partially reload the resource. Avoid duplicate PHP/TypeScript registries; if both runtimes need mapping, use one tested shared JSON registry or generate one side from a canonical source.

## Styling baseline

```css
.status-badge {
  display: inline-flex;
  align-items: center;
  gap: .375rem;
  min-height: 1.625rem;
  padding: .25rem .625rem;
  border: 1px solid;
  border-radius: 9999px;
  font-size: .75rem;
  line-height: 1rem;
  font-weight: 500;
  white-space: nowrap;
}
.status-badge__dot {
  width: .375rem;
  height: .375rem;
  flex: none;
  border-radius: 9999px;
  background: currentColor;
}
```

Apply canonical colors by variant. Permit a documented compact size only for genuinely dense tables; pages must not invent sizes.

## Migration search

Search for `status`, `badge`, `chip`, `pill`, enum labels, color utility classes, beige/stone/tan classes, conditional class strings, and columns printing `.status` directly. Inspect email/PDF/print output separately because screen CSS may not apply.
