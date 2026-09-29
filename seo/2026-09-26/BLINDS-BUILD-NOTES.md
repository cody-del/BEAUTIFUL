# Custom Blinds: first category-page build

Built September 26, 2026. This is a local redesign preview, not a change to the client's live website.

## Scope and evidence

- Existing page: https://www.beautifulblindsandshades.com/products/blinds
- Local preview: http://127.0.0.1:4317/products/blinds/
- Source content: September 25 crawl, `homepage/research/audit-2026-09-25/content-pages.json`, cross-checked against the live page.
- Earlier page brief: `seo/2026-09-25/PAGE-BRIEFS.md`, section `/products/blinds`.
- Semrush US Organic Research refreshed September 26. Raw results and report URLs are in `blinds-rankings-top50.json` and `homepage-local-rankings.json` alongside this file. The category request is the top 50 rows, not its entire keyword footprint. The September 25 audit retains the broader export.
- Observation dates vary: August 10 to September 26 for the category sample, August 11 to September 15 for the homepage sample. Retrieval date is not the ranking observation date. These are Semrush database positions, not a fresh Fort Wayne GPS-specific search or Search Console performance report.

## Ranking decisions

| Query | Homepage | Blinds category | Decision |
| --- | ---: | ---: | --- |
| blinds fort wayne indiana | 3 | Not in this top-50 category sample | Preserve the homepage's broad local focus. |
| blinds fort wayne | 10 | Not in this top-50 category sample | Do not reposition the category as a replacement homepage. |
| best blinds fort wayne indiana | 7 | 21 | Answer selection questions on the category rather than repeating near-identical local sales paragraphs. |
| best blinds fort wayne | 10 | 22 | Retain natural relevance and product comparison; avoid unsupported superlatives. |
| custom mini blinds near me | Not requested | 26 | Keep mini-blind coverage and the original detail-page link. |
| measure and install blinds near me | Not requested | 35 | Keep measuring and installation prominent. |
| blinds installation near me | Not requested | 40 | Retain a dedicated installation section and explain the process. |

The category also appears for `budget blinds fort wayne` at 13. Budget Blinds is another business's name, so the new page explains materials and budget without pretending to be that company or repeating its name as a sales phrase.

These rankings justify preserving the topic and URL structure. They do not prove that a proposed wording change will improve rankings. Changes below have specific usability, accuracy, or technical reasons and need post-launch monitoring.

## What stays

- Exact existing title: **Custom Blinds Fort Wayne | Window Blinds | Beautiful Blinds & Shades**.
- Exact existing meta description: **Fort Wayne custom blind experts. Wood, faux wood, aluminum & vertical blinds. Precise measurement & pro installation. Free consultation. Call Beautiful Blinds!**
- Original `/products/blinds` canonical target and slug; no consolidation or redirects applied to the client's website.
- Wood, faux wood, aluminum, vinyl, mini, vertical, panel track, Venetian, and motorized blind topics.
- Room selection, cost considerations, in-home samples, custom measurements, installation, and local coverage.
- All four existing blind-detail URLs, the existing product-card photos, and related service destinations.
- The approved homepage's navigation, heading font, brand colors, reviews, and mobile call controls. Homepage copy and metadata were not rewritten in this change.

## Targeted edits and reasons

| Change | Reason |
| --- | --- |
| Promote the existing local category heading to a single H1 | The old page had no H1. |
| Add the original URL as canonical and add matching breadcrumb/CollectionPage data | Give the category a consistent identity. No fabricated prices, product offers, or review schema. |
| Replace repeated phrases such as “window blinds Fort Wayne” embedded in sentences with normal grammar | Preserve the subject while making the page readable and distinct from the homepage. |
| Consolidate duplicate measuring and installation paragraphs | Keep the same process information in one useful section. |
| Keep material and room coverage, with short comparison cards | Help buyers choose and retain relevant product detail. |
| Correct product-link labels from “View Shades” to the actual blind style | Make navigation descriptive and accurate. |
| Add answers about cost, wood versus faux wood, sliding doors, measuring, timing, and repair | Address purchase questions using the existing service/product coverage. |
| Remove unverified “thousands of homes,” 15+ year lifespan, fixed 2–3 week timing, and universal compatibility promises | Avoid carrying unsupported claims into the new site. Ask David before adding specific warranty, availability, or delivery claims. |
| Add consultation buttons after comparisons, installation, and at the end | Give visitors a next step when they have enough information to enquire. |

Business facts and product ranges are carried from the live site. Current product availability and supported motorized controls still require client confirmation before final launch; the copy qualifies these as product-dependent. Photographs illustrate products and are not labeled as completed client installations. Customer quotes are copied unchanged from the approved homepage.

## Implementation and validation

- Static HTML output: `homepage/dist/products/blinds/index.html`.
- Editable content: `homepage/pages/blinds.html`.
- Shared shell generator: `homepage/build_pages.py`, using the homepage header, badges, reviews, business schema, and footer.
- Category-only styling: `homepage/dist/category.css`.
- Shared JavaScript now tolerates pages without the homepage video and form.
- Homepage header, product card, and footer now link to the local category route. Other unbuilt pages continue to link to the live client website.
- Category consultation buttons point to the existing live `/contact` page until the redesigned contact page and lead delivery are ready. No new form or false submission success was introduced.
- Passed: exact title/description comparison, canonical target, one H1, duplicate-ID check, JSON-LD parsing, asset existence, retained child links, subject coverage, no em dashes, and preview `noindex` check.
- Browser checked at widths 320, 390, 768, 1024, and 1440: no horizontal document overflow; responsive cards; mobile menu and treatment accordion; keyboard Escape; review navigation and expansion; FAQ expansion.
- Homepage regression check: consultation button initialization, review enhancement, video control presence, and navigation into the new category. No captured JavaScript errors.
- `python3 homepage/build_pages.py --check` and `node --check homepage/dist/script.js` pass.

## Release status

Not pushed or published in this turn. The client website and existing Netlify deployment are unchanged. The local preview retains the site's `noindex` meta tag, robots exclusion, and Netlify preview header configuration.

Before moving the client's production domain, follow `seo/2026-09-25/MIGRATION-CHECKLIST.md`: check deployed URL normalization (the Python preview adds a trailing slash for directory pages), serve the intended canonical URL consistently, confirm contact delivery, review remaining business claims, and remove preview indexation blocks only for production. Recheck the saved queries by landing page after launch; compare with Search Console when available. No ranking improvement or loss-free migration is guaranteed.
