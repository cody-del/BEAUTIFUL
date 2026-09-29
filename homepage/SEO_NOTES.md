# Beautiful Blinds & Shades homepage rebuild

**Full-site research update, September 25, 2026:** Before building additional pages, use [the full SEO audit and migration plan](../seo/2026-09-25/README.md), including its 55 page briefs and 122-URL preservation map. It supersedes the limited September 22 ranking/audit baseline below. No live changes were made by that audit.

Prepared September 22, 2026. This is a design review, not a production replacement. No live pages, URLs, redirects, DNS, or Semrush settings have been changed.

## Design direction

The approved reference to follow is the Naples Bahama & Colonial landing page, not an editorial or magazine layout. Use Manrope Regular (400) for H1 and main H2 headings, Manrope Medium (500) for H3 and small footer headings, a centered photo hero with a dark overlay, a floating white rounded navigation bar, substantial rounded calls to action, and rounded product/service cards. Do not use thin diagonal arrows, heavy extra-bold headlines, serif magazine typography, em dashes, or generic marketing filler.

Preserve the client's original palette: blue `#67b2e8`, green `#bfdd9f`, charcoal `#333`, white, and pale gray. Supporting dark backgrounds are blue-charcoal. Original logo and product imagery come from the live client website. The owner video poster comes directly from Wistia media `cfwf2ryb20`; a generic blog avatar has not been used as the owner portrait.

## Evidence and limits

Semrush project: `30275556`, `www.beautifulblindsandshades.com`.

The connector exposes Site Audit and Organic Research data. The Position Tracking campaign discovery returned `targets: null`, so no Fort Wayne-specific daily campaign positions or device-level history were available through that response. The following positions are from the US Organic Research database, not a live Fort Wayne search or a new local ranking test. Individual observation dates differ.

| Query | Homepage position | Observation date (UTC) |
| --- | ---: | --- |
| blinds fort wayne indiana | 3 | 2026-08-21 |
| window treatments fort wayne | 5 | 2026-08-20 |
| fort wayne window treatments | 5 | 2026-08-25 |
| window treatments fort wayne indiana | 5 | 2026-09-05 |
| window blinds fort wayne | 9 | 2026-09-15 |
| blinds fort wayne | 10 | 2026-08-14 |

Raw data, source HTML, source CSS, sitemap, video metadata, and review widget snapshots are retained in `research/`. The keyword CSV includes source timestamps and converted dates. The 50-row broad report and 100-row Fort Wayne report are bounded samples, not a full-domain audit or traffic measurement.

The existing Semrush Site Audit is dated July 27, 2026, not today: 60 crawled pages, 77 errors, 61 warnings, and 146 notices. Reported issues include 75 structured-data markup errors, one 4xx error, one broken internal link, nine pages with multiple H1s, and 40 links with no anchor text. These are historical findings that require a fresh crawl before launch, not all confirmed current defects.

## Homepage decisions implemented

- Preserve the current homepage title and description for the first design iteration.
- Preserve the root homepage URL and production canonical, normalized to the existing preferred `https://www.beautifulblindsandshades.com/` host.
- Keep the homepage's primary commercial intent: custom window treatments in Fort Wayne, with blinds, shades, and shutters explicitly named.
- Use one clear H1 and crawlable HTML for all primary copy, product links, FAQs, and contact information.
- September 27 user decision: retain the live homepage's exact primary H1, “Beautiful Window Treatments Fort Wayne Indiana,” for the initial migration. Name custom blinds, shades, and shutters in the supporting hero sentence. Do not replace this heading for stylistic reasons; any later change needs a separately justified SEO decision.
- Preserve exact URLs for linked product, repair, cleaning, outdoor-shade, motorization, and service-area pages. In this separate review site, those links open the current client website.
- Keep product sections concise and give each product its own destination, avoiding duplicate full product-page content on the homepage.
- Use a simpler LocalBusiness JSON-LD record based on the original business information. Remove the old mixed Offer/Product catalog and stale image reference from the new homepage. No aggregate-rating or self-serving review rich-result markup is included.
- Reuse the real client review excerpts and dated 5.0 / 36 review snapshot from the site's connected review widget. These are static snapshots and should be refreshed before launch. Do not invent reviews or review counts.
- Load the original Wistia introduction after the visitor clicks play. Primary content is available without the player.
- Use the original LeadConnector consultation form, with a direct contact-page fallback. No lead was submitted during testing.
- Keep analytics off this review copy to avoid polluting production measurement. The existing production GA4 ID is recorded in the original HTML and must be restored/tested for launch.
- Protect the review copy with `noindex, nofollow`. This must be removed only from the intended production homepage at release.

## Keyword overlap decisions

Multiple ranking URLs do not by themselves prove harmful cannibalization. Do not delete or redirect these pages solely because they share words with the homepage.

| Page | Intended role | Current decision |
| --- | --- | --- |
| `/` | Broad Fort Wayne commercial window-treatment intent | Preserve as primary destination; protect its leading positions |
| `/products/blinds` | Blinds styles, options, selection, and local installation | Preserve URL; keep product-specific intent |
| `/products/shades` | Shades styles, fabrics, operation, and local installation | Preserve URL; keep product-specific intent |
| `/products/plantation-shutters` | Plantation shutter selection and installation | Preserve URL; keep product-specific intent |
| `/services/outdoor-shades` | Outdoor and patio shade installation | Preserve URL and strong service visibility |
| `/services/blind-shade-repair` | Repair intent | Preserve; do not merge with new-product pages |
| `/services/blind-and-shade-cleaning` | Cleaning intent | Preserve; do not merge with repair or replacement |
| `/blog-post/motorized-blinds-and-shades-in-fort-wayne` | Educational motorization guide | Preserve; it ranks for motorized queries and secondary broad terms |
| `/services/window-treatments` | General consultation and installation service | Review overlap; current title/H1 substantially overlap homepage. Differentiate toward the service/process if retained |
| `/beautiful-blinds-shades-service-areas/blinds-and-shades-fort-wayne-indiana` | Fort Wayne location landing page | Candidate for consolidation review, not an implemented redirect |
| `/blog-post/fort-wayne-window-treatments-guide` | Informational comparison guide | Keep informational and link readers to relevant commercial pages |

The Fort Wayne location page appears well below the homepage in the sampled broad queries: position 97 versus 5 for `window treatments fort wayne`, and 76 versus 3 for `blinds fort wayne indiana`. This supports prioritizing the homepage, but does not show that removing the location page will improve rankings.

Before any consolidation, compare page/query data in Search Console over a meaningful period, including seasonality; inspect backlinks, conversions, unique queries, and ranking URL changes. If two pages truly serve the same intent and one has no distinct value, merge useful content into the stronger destination and implement a one-to-one permanent redirect. Recheck internal links, canonicals, and the sitemap. Keep productive informational and product pages.

## Before a production launch

1. Review this homepage design and wording first. Rebuild the other pages only after the design direction is accepted.
2. Refresh Semrush and Search Console baselines. Resolve the missing Position Tracking campaign targets before claiming a daily Fort Wayne ranking baseline.
3. Reconcile all 53 sitemap URLs against Search Console, backlinks, analytics, and a fresh crawl. `research/url-preservation-map.csv` currently preserves every URL unchanged; it is not a complete historical URL inventory.
4. Review the existing form's policy links: its Privacy Policy and Terms of Service currently point to `https://www.example.com`. Fix those in the form provider using real client policy pages before launch. This homepage does not alter the external form configuration.
5. Confirm the existing offer and lead times with the business. The old repeated “Buy 2 Get 1 FREE” banner was not carried into this concept without confirmation that the promotion is still active. The existing two-to-three-week estimate is qualified and requires current confirmation.
6. Confirm the physical address and service hours in LocalBusiness schema. Do not represent the business as having a walk-in showroom; its owner says it brings samples to the customer.
7. Restore and test production analytics, consent behavior, call tracking, form delivery, and thank-you/conversion events. Test submissions need explicit authorization because they create real leads.
8. Remove review-only noindex directives on production, preserve the preferred host/root canonical, and make every retained route return its correct status. Never serve this homepage as a 200 fallback for missing product URLs.
9. Validate HTML, mobile layout, structured data, response headers, redirects, sitemap, robots rules, and actual field performance. No Lighthouse score or Core Web Vitals pass has been claimed.
10. Launch in a controlled step with backups and monitor indexation, query/page traffic, leads, and positions. No redesign can guarantee zero ranking fluctuation.

Guidance checked against [Google's site migration documentation](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) and [review snippet rules](https://developers.google.com/search/docs/appearance/structured-data/review-snippet).
