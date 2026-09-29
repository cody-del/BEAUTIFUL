# Outdoor Shades, Repair, and Cleaning preview build

Built September 27, 2026. Local previews only; no GitHub push, Netlify deployment, DNS change, redirect, or production-page replacement was performed in this batch.

## Evidence and intent

The September 25 live-site archive and page briefs were cross-checked against the three live service pages. Semrush US `resource_organic` reports were refreshed for each exact URL with a 50-row limit, sorted by position. Raw responses, observation timestamps, and report links are in the adjacent `outdoor-shades-rankings.json`, `blind-shade-repair-rankings.json`, and `blind-and-shade-cleaning-rankings.json` files.

| Page | Returned rows | Observation dates (UTC) | Relevant examples from the report |
| --- | --- | --- | --- |
| Outdoor Shades | 49 | August 4–September 26, 2026 | outdoor sun shade installation near me #4; sun shade installation near me #4; patio shade near me #10; outdoor blinds for patio near me #11 |
| Blind & Shade Repair | 50 | August 2–September 23, 2026 | wood blind repair near me #9 and #10; mini blinds repair #12; window blind repair #13; cellular shade repair and restringing queries in the teens |
| Blind & Shade Cleaning | 50 | August 3–September 26, 2026 | blinds cleaners near me #16; blind cleaning #22; blinds cleaning near me #28 |

These are database observations, not current local-pack positions or a complete query inventory. Retrieval date is distinct from observation date. Duplicate keyword rows were retained without combining ranks. Unrelated geography and competitor-branded searches were not added to the content. The cleaning report's #28 observation for “blinds cleaning near me” and the older audit's #18 observation are from different dates; this is not evidence of an effect from these unpublished changes.

## Preserved SEO elements

- Exact canonical URLs: `/services/outdoor-shades`, `/services/blind-shade-repair`, and `/services/blind-and-shade-cleaning`.
- Exact existing title tags, verified against the archived pages.
- One H1 per page retaining the service and Fort Wayne, Indiana.
- Distinct outdoor-purchase, repair, and cleaning intent. Repair and cleaning remain separate pages and link to one another where appropriate.
- Outdoor topics: patio, deck, porch, pergola, gazebo, three-season room, roller shades, solar-screen fabrics, openness, manual/motorized controls, side guides/zip tracks, mounting, clear vinyl, protected natural materials, installation, weather, and care.
- Repair topics: wood/faux wood/vinyl/mini/vertical blinds, cords and restringing, tilt mechanisms, slats, vanes, carriers and tracks, roller/Roman/cellular shades, motorized controls, Graber, compatible parts, service process, and repair versus replacement.
- Cleaning topics: wood finishes, faux wood, aluminum/mini/vinyl/vertical blinds, cellular/pleated/roller/Roman/solar shades, dust, grease, marks, material-specific care, ultrasonic suitability, removal/reinstallation arrangements, pricing scope, and cleaning versus mechanical repair.
- Existing related article URLs retained, including the original `/blog-post/outdoor-patio-shades-guild-fort-wayne` spelling.

## Intentional content changes

The meta descriptions were rewritten only where the old text contained promises that the research could not substantiate:

- Outdoor: replaced blanket “block sun & bugs” and seasonal-extension language with patio use, solar fabrics, controls, and consultation.
- Repair: removed universal “all brands” and “same-day quotes.” The new description still names repair, broken cords, stuck shades, controls, and Fort Wayne.
- Cleaning: removed “all types,” universal ultrasonic availability, and allergen-removal promises. The new description names professional cleaning, Fort Wayne, dust, grease, and fabric care.

Body copy retains the relevant service subjects without fixed completion times, invented prices, temperature/UV guarantees, universal weather resistance, or unsupported warranties. Ultrasonic cleaning remains a visible topic, with availability and suitability to be confirmed for the product. Original claims have not been erased from the research archive.

This is intended to make the content clearer and more defensible; rankings cannot be guaranteed. Before production launch, the client should confirm cleaning methods/equipment, supported repair brands and parts, service fees, removal/reinstallation arrangements, outdoor product limits, warranties, and turnaround expectations. Those details can strengthen the final copy once verified.

## Design and implementation

- Outdoor Shades uses the approved photo hero, compact buttons, review badges, and review carousel.
- Repair and Cleaning use shorter pale-blue split introductions, existing product images, and service-specific call/contact buttons. Header and mobile-bar contact labels on those pages avoid implying that repairs or cleaning are free.
- Clean text panels, divided service details, installation/service steps, native FAQ disclosures, and collapsed city lists use the existing brand typography and colors.
- No decorative product icons, owner video, owner video still, new generated imagery, or removed promotion was added.
- Existing outdoor preview imagery and previously sourced live-site blind/cellular-shade images are illustrative, not labeled as documented repair or cleaning jobs.
- Homepage menus, cards, care links, footer, and Contact page now link to these local rebuilt routes. Unbuilt destinations still use the current live site.
- Shared generator supports service templates in `homepage/pages/`; service styles are in `homepage/dist/service.css`. WebPage, Service, and BreadcrumbList data reference the existing business entity without invented prices or ratings.
- Preview noindex/robots protections remain. The Contact form remains explicitly preview-only and does not transmit leads.

## Validation

- All eight built HTML pages: exact archived title tags; canonicals; one H1; unique IDs; parseable JSON-LD; existing local routes/assets and same-page fragment targets; no unresolved template tokens. Existing product/Home/Contact descriptions remain unchanged; the three service-description exceptions are documented above.
- New services: no owner video, em dashes, or removed promotion; key source topics and article links retained.
- New layouts checked at 320, 390, 768, 1024, and 1440px with no document horizontal overflow. Desktop and mobile hero/content layouts visually inspected.
- Mobile Services navigation into Cleaning, cleaning-to-Contact CTA, cleaning FAQ, and outdoor FAQ interactions verified. Contact preview-only notice confirmed. No captured JavaScript errors on the outdoor page.
- Generator `--check`, JavaScript syntax, and Git whitespace checks passed.

Next suggested batch: the general Window Treatments service page and About page, then the preserved product-detail URLs in the original SEO page briefs. Do not migrate or consolidate ranking URLs simply to shorten the menu.
