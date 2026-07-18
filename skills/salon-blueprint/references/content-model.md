# Salon content model

Use one typed/configured source of truth where the stack permits it.

- `business`: name, legal/display name, salon type, description, phone, WhatsApp, email, website
- `location`: address, city, region, postal code, coordinates, directions URL, parking/accessibility notes
- `hours`: day, opens, closes, closed flag, exceptions
- `serviceCategories`: id, name, description, order
- `services`: id, category, name, description, duration, price, price qualifier, featured, bookable
- `staff`: id, name, role, bio, specialties, image, booking target
- `gallery`: image, category, service, alt text, source/rights
- `testimonials`: quote, customer display name, source, verified flag
- `booking`: mode, provider URL, policies, deposit rule, cancellation window
- `socials`: platform and verified URL
- `seo`: canonical base, default social image, target service areas

Render only confirmed fields. Keep demo/placeholders out of JSON-LD. Keep NAP identical everywhere.
