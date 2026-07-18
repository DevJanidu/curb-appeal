---
name: image-pipeline
description: Source, optimize, and verify real images for every image slot — search business-provided assets first, then Unsplash/Pexels/Pixabay; convert to modern formats, generate responsive sizes, write alt text, and confirm each renders. Use whenever a site needs imagery and some or all real business photos are missing.
---

# Image Pipeline

## 1. Define requirements

List every image slot with its role (hero/LCP, gallery, service, team, atmosphere), target orientation, and rendered size. LCP hero images get priority; below-fold images lazy-load.

## 2. Source in priority order

1. **Business-provided assets** — use the brief's real photos/logo first. Always preferred.
2. **Free stock APIs** for remaining slots — Unsplash, Pexels, or Pixabay:
   - Unsplash: `GET https://api.unsplash.com/search/photos?query=...&orientation=landscape`, header `Authorization: Client-ID <UNSPLASH_ACCESS_KEY>`.
   - Pexels: `GET https://api.pexels.com/v1/search?query=...&orientation=landscape`, header `Authorization: <PEXELS_API_KEY>`.
   - Pixabay: `GET https://pixabay.com/api/?key=<PIXABAY_API_KEY>&q=...&image_type=photo&orientation=horizontal`.
   - Search specific queries ("hair salon interior", "barber fade", "nail art closeup"), not generic ones. Avoid duplicate images across slots. Match the chosen visual direction from `../design-system/SKILL.md`.
   - Check size/orientation fits the slot before choosing.

If no key is configured, ask once; if declined, use controlled placeholders per `../design-system/SKILL.md` and produce an acquisition checklist — never block the build.

## 3. Optimize

- Download locally when the license permits (Pexels/Pixabay allow it; Unsplash requires hotlinking their CDN URLs unless downloaded via their API `download` endpoint per their terms).
- Name descriptively (`salon-interior-reception.webp`, not `photo1.jpg`).
- Convert to WebP/AVIF with a fallback; generate responsive sizes (`srcset`/`sizes` or the framework's responsive image component).
- Set explicit `width`/`height` (or `aspect-ratio`) to prevent layout shift, per `../responsive-design/SKILL.md`.
- Lazy-load below-fold; preload/priority the LCP image, per `../performance-audit/SKILL.md`.

## 4. Alt text & integrity

- Write accurate, specific alt text describing the actual image content.
- Never use a stock photo as a named team member's headshot or attach one to a testimonial — that fabricates a real person (banned by `../content-integrity/SKILL.md`). Use a neutral avatar instead.
- Never scrape competitor or general-web images — licensing is unverified.

## 5. Record provenance

Write `image-sources.json` at the project root recording, per image: local path, source (business/Unsplash/Pexels/Pixabay), creator, license, usage rights, and alt text. This is the audit trail for what can legally ship and what the client should later replace.

## 6. Verify

Using Playwright MCP or whatever browser automation is available:

1. Start the dev server and load every page with a sourced image.
2. Confirm each image request returns 200 (not 404/CORS), and each `<img>` has `naturalWidth > 0` after load.
3. Screenshot each page to confirm images are visually present and well-cropped, not stretched or overlapping text.
4. Re-query and re-verify any failure; never leave a broken image or silently swap to a placeholder without saying so.
