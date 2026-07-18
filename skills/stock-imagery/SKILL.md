---
name: stock-imagery
description: Source real, working photos from Unsplash or Pixabay for image placeholders (hero, gallery, service, interior/atmosphere shots), then verify every inserted image actually renders using browser automation (Playwright MCP or equivalent). Use whenever a local-business site has image placeholders and no real business photos were provided.
---

# Stock Imagery

## When to use

- The brief's "Existing logo/photos" field is blank, says "none," or only covers some sections.
- A page has hero, gallery, service-category, or atmosphere image slots with no real business photo to fill them.
- Never for named team member headshots or attached to a specific testimonial — see "What not to do" below.

## Sourcing

1. Check for an API key: `UNSPLASH_ACCESS_KEY` or `PIXABAY_API_KEY` in the project's `.env`/environment. If neither exists, ask the user once whether they want to add a free key (unsplash.com/developers or pixabay.com/api/docs). If they decline or don't respond, fall back to a neutral placeholder composition per `../art-direction/SKILL.md` and stop here — don't block the rest of the build on it.
2. Search with a query specific to the section and vertical, not generic — e.g. "hair salon interior," "hairstylist cutting hair," "modern barbershop chair," not just "salon."
   - Unsplash: `GET https://api.unsplash.com/search/photos?query=...&orientation=landscape` with header `Authorization: Client-ID <UNSPLASH_ACCESS_KEY>`. Use the returned `urls.regular` (or `urls.raw` with size params) directly as the image `src` — hotlinking Unsplash's own URLs is required by their license; don't download and rehost the file.
   - Pixabay: `GET https://pixabay.com/api/?key=<PIXABAY_API_KEY>&q=...&image_type=photo&orientation=horizontal`. Use `largeImageURL` (or `webformatURL` for smaller slots).
3. Pick images that match the site's chosen visual archetype (soft/spa vs sharp/editorial, from `../art-direction/SKILL.md`) — don't drop a moody dark-toned photo into a bright pastel-spa layout, or vice versa.
4. Note in the handoff summary which images are stock, not the business's own photography, so the client knows to swap them in later — this is demo content and stays subject to `../website-director/SKILL.md`'s "clearly label demo content" rule.

## What not to do

- Never use a stock photo as a named team member's headshot, or attach one to a testimonial — that fabricates a real person, which `../website-director/SKILL.md`'s operating rules already prohibit. For a team member without a real photo, use a neutral avatar (initials, icon, or silhouette) instead.
- Don't hotlink images found by browsing the general web outside these two APIs — licensing is unverified and the links tend to break.

## Verification

After inserting images, verify every one actually renders before considering the work done — using Playwright MCP or whatever browser automation tooling is available in the session:

1. Start the project's dev server.
2. Navigate to every page that received a sourced image.
3. Check the network log for each image request: it must be a successful (200) image response, not a 404 or a CORS failure.
4. Check the DOM for broken images — an `<img>` whose `naturalWidth` is 0 after load is broken even if the request technically succeeded.
5. Take a screenshot of each page to confirm the image is visually present and reasonably cropped/positioned, not stretched, cut off, or overlapping text.
6. If any image fails, re-run the search with an adjusted query and re-verify. Don't leave a broken image in place, and don't silently fall back to a placeholder without saying so.
