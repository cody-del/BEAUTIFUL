# Monroeville, Warsaw, and Hicksville preview batch

Prepared September 29, 2026. Local build only, bringing the preview to 39 pages. No GitHub push, Netlify deployment, redirect, or production indexation change was made.

## Preserved routes and metadata

| Page | Original route retained | Metadata decision |
| --- | --- | --- |
| Monroeville | `/beautiful-blinds-shades-service-areas/window-treatments-monroeville-indiana` | Original title, description, primary H1, and canonical preserved. The incorrect second H1 about Woodburn is removed. |
| Warsaw | `/beautiful-blinds-shades-service-areas/window-treatments-warsaw-indiana` | Original title, description, H1, and canonical preserved. |
| Hicksville | `/beautiful-blinds-shades-service-areas/window-treatments-hicksville-indiana` | Title and H1 change only the state from Indiana to Ohio. The original Ohio description and legacy canonical/URL remain. WebPage and breadcrumb labels use Ohio. Coverage confirmation is still outstanding. |

The original metadata, headings, and editorial text are preserved in `homepage/locations/source-baseline.json`. The existing archived HTML references are retained there. The original URLs were also opened this turn; the browser search source was cached, so this is not represented as a fresh origin crawl.

## Source-to-draft decisions

### Monroeville

The original rich text describes Woodburn throughout. It is not valid Monroeville content and was not migrated by replacing town names. The draft introduces Monroeville enquiries and in-home selection, then retains useful product subjects: wood/faux wood, cellular, Roman, solar, and shutters. It explains mounting depth, large openings, budget, sample comparison, measuring, a reviewed quote, ordering, installation, operation, and follow-up.

Removed or corrected: Woodburn geography and community claims; categorical statements that faux wood is lighter, never warps/cracks/fades, and lasts longer; assumed shutter resale value; guaranteed energy savings or payback; unsupported manufacturing and lifespan promises. Original product topics remain accessible through relevant category and detail-page links. New motorization guidance links to the existing exact-text article.

### Warsaw

The original body contains a full Bluffton section followed by Warsaw content. The misplaced Bluffton block is removed completely. The draft retains the useful Warsaw subject matter: views and glare, lake-facing windows where applicable, solar/roller/cellular/Roman shades, shutters, motorization, older openings, patio access, high glass, samples, measuring, installation, and care.

Removed or qualified: generic civic/tourism copy, claims of completed local projects and referrals without supplied evidence, guaranteed energy-cost improvements, and assumptions about material durability near water. Bright views remain the organizing topic, with explicit nighttime privacy and mounting considerations. No actual lake project is claimed. Existing product imagery is used illustratively; the hero uses a residential roller-shade image rather than a city skyline.

### Hicksville

The original title/H1 say Indiana, but the description, main body, and original service directory identify Hicksville, Ohio. The preview aligns the visible heading, title, and breadcrumb with Ohio while keeping the old `hicksville-indiana` route. This is a geographic correction, not an attempt to rank for a new market. The business remains identified as based in Fort Wayne; no Ohio office or address is added.

The draft retains all original treatment subjects and the consultation-to-installation process, removes unverified local jobs/referrals and neighborhood claims, and asks visitors to confirm arrangements for their address. The client's current Ohio coverage, appointment limits, and fees have not yet been confirmed. This route is prepared for review but is not cleared for production. The legacy source description still mentions a free consultation; confirm that policy before launch along with the page's coverage.

For scale, the archived editorial bodies were approximately 1,783 words for Monroeville (all Woodburn), 2,466 for Warsaw (about 1,273 in the Warsaw portion), and 1,280 for Hicksville. Draft main sections including headings/actions contain approximately 915, 975, and 895 words respectively. These counts use whitespace splitting, measure slightly different content boundaries, and are recorded as a scope check rather than an SEO target.

All three pages are editorial revisions, not exact-text migrations. Title and URL preservation do not prove ranking safety. The factual corrections are justified by the source defects; useful original details should still be reviewed before production. Original blog wording is unchanged.

## Semrush evidence

Exact-URL `resource_organic` reports were retrieved September 29 with database `us`, limit 30, sorted by position. Raw responses, including errors, are saved as `semrush-monroeville.json`, `semrush-warsaw.json`, and `semrush-hicksville.json` beside this file.

- Monroeville and Warsaw returned `ERROR 50 :: NOTHING FOUND`. This means no rows were returned for those requests, not that the pages have no rankings, traffic, links, or value.
- Hicksville returned four rows referencing Cummingsville and Thompsonville, including a repeated Roman-shade phrase at different positions. Those town queries are not evidence of Hicksville, Ohio performance and were not adopted as targets. Observation timestamps are in August/September 2026, not necessarily the retrieval date.
- No new verified city/device Position Tracking or Search Console baseline was obtained in this batch. The previous audit's project discovery returned no usable tracking targets. Do not treat the US URL reports as current local rank monitoring or infer a migration result before launch.

## Design and navigation

The three templates reuse the Auburn page's header, compact hero actions, typography, three product cards, open guidance rows, installation section, native FAQ disclosures, and closing contact actions. New CSS only handles the secondary service-area link below the final CTA. No hero reviews, owner video, decorative material icons, new staged-image generation, fake project attribution, or em dashes were added.

The directory now links locally to Auburn plus these three cities; the remaining 13 cities still link to their original live routes. The source list of 17 city URLs is unchanged.

## Verification and remaining work

- Shared build is current. The location check verifies all five location routes, preserved metadata with the documented Ohio exception, one expected H1, absence of wrong-city body text, and all 17 directory destinations.
- Exact article text/title checks pass for all 12 blogs. The whole-site check passes across 39 pages for H1s, IDs, JSON-LD, noindex, internal destinations, and assets. Existing 13 product-detail migration checks pass.
- Desktop heroes and representative interior sections were visually checked. All three pages were checked at 320, 390, 768, and 1280 pixels without horizontal overflow. Keyboard FAQ activation, mobile menu access, and local directory links were checked in the browser.
- Forms remain unconnected; no enquiry was submitted or claimed delivered. Preview search exclusion remains intact.

Next planned batch: Fort Wayne, Huntertown, Leo-Cedarville, and New Haven. Keep the Fort Wayne city page distinct from the homepage, and link the Huntertown and Leo-Cedarville guides without copying them. Final coverage confirmation, business facts, delivery integrations, complete route reconciliation, and launch review remain open.
