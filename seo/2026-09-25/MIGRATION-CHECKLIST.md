# Migration and measurement checklist

Prepared September 25, 2026. This is the acceptance plan for the future full-site launch, not work already completed. The current Netlify deployment is a homepage preview. Do not point the client's domain to it until the full route inventory is implemented and checked.

## Before writing and building

- Export Search Console performance by page/query for the last 16 months, with recent 28-day and prior-period views. Separate branded, Fort Wayne commercial, product, repair/cleaning and city queries.
- Export GA4 organic landing-page sessions, form completions and tracked calls. Record tracking gaps rather than substituting Semrush traffic estimates for leads.
- Recover or configure a usable Semrush tracking campaign for Fort Wayne on mobile and desktop, recording exact location, device, engine and date. The current connector returned no targets. Keep local pack observations separate from normal organic positions.
- Track the eight priority asset groups from AUDIT.md. Include core Fort Wayne phrases, material/product phrases, repair, cleaning, motorization and key city terms. Obtain an initial observation before launch; collect trend history where scheduling allows.
- Export current CMS URLs, hosting redirects and Search Console links. Reconcile with the 122-URL map to catch undiscovered routes, assets and old redirects.
- Confirm service boundaries, product brands, actual warranties, turnaround, ownership/experience claims and permission for genuine installation photos. Use claims-to-verify.csv as an interview agenda for David.
- Freeze current source HTML and metadata as the baseline. The local audit archive already preserves the discovered pages; back it up with the project because raw research is gitignored.

## Build acceptance

- Every retained indexable page has a real route at its existing path, returns 200 and contains its main content in the initial HTML.
- Preserve the four priority pages' current titles/descriptions initially, except an independently verified factual error. Stage broader title and copy experiments later.
- Fix wrong-city/product content immediately in the rebuilt copy; preserving rankings does not require retaining factual mistakes.
- Give each page its intended topic, a clear H1, coherent subheadings and a unique useful description. Do not impose arbitrary word counts or keyword-density quotas.
- Preserve category-to-product links, product-to-category breadcrumbs, city-directory links and contextual guide-to-product links. Avoid dozens of unrelated exact-match links in every paragraph.
- Provide stable, absolute production canonicals. Do not canonicalize every product or city page to the homepage.
- Replace live-domain links in preview navigation with the proper internal routes once those routes exist. Test the real crawl graph rather than assuming a visible dropdown is crawlable.
- Add the missing Bluffton blackout article to the production sitemap. Include only intended canonical, indexable, successful URLs. Keep /contact-ghl excluded while it remains noindex.
- Validate truthful page-specific business, service, article and breadcrumb schema. No generic Outdoor Shades subject on every article, invented prices, or invented aggregate ratings.
- Preserve useful image alt text, add explicit dimensions and responsive sizes, and avoid eager loading of every full-size image. Archive/migrate owned assets and check whether Webflow/CDN dependencies will remain available after the hosting move.
- Retain the real owner video and test playback on the deployed origin and mobile browsers. Confirm long-term availability or obtain an authorized durable video asset.
- Test mobile menu, dropdown focus/Escape, tap-to-call, review controls, FAQ/city disclosures and form labels at representative narrow and wide widths. No horizontal overflow or inaccessible hidden navigation.
- Connect the consultation form to the approved CRM/recipient. Test success, failure, duplicate submissions and spam controls with an authorized test lead; confirm actual receipt. Never display success without delivery acceptance.
- Implement and verify analytics events for consultation submission and phone clicks, preserving existing tracking/verification identifiers. Phone clicks are not the same as completed calls.
- Measure performance on the new pages and check available field data. No Core Web Vitals pass is asserted by this audit.

## Redirect and route acceptance

- Review each proposed redirect against the old intent and final destination. All high-confidence destinations in the audit currently return 200, but must be retested on the rebuilt site.
- Use explicit permanent redirects for confirmed replacements. Preserve current working HTTPS/www normalization. Avoid chains, loops and redirects to unrelated homepages.
- Treat ambiguous legacy routes and legal-policy URLs individually. A genuine 404/410 is appropriate when there is no equivalent and the content is intentionally retired; it must not return the homepage with a 200 status.
- Retain all current city/product URLs at the initial design launch, including long or misspelled slugs. Consider slug cleanup only as a separate evidence-backed change.
- If a later consolidation is approved, move the genuinely useful material to its owner, redirect the retired URL, update internal links and the sitemap, and monitor both query groups. Do not combine a noindex rule with an intended canonicalization/redirect experiment without a clear reason.
- Keep migration redirects for at least a year, preferably longer where people or links still use them. Relevant guidance: [Google site moves](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes).

## Launch gate

- Keep the production domain on the current site until the complete approved site passes route/content/form checks. No homepage-only cutover.
- Keep review environments excluded from search; at production launch remove the preview's noindex meta tag, `X-Robots-Tag: noindex` header and blocking robots rule from the production environment only. Retain intentional noindex routes such as the integration utility. Confirm the delivered HTTP headers, not just source configuration.
- Remember that a robots.txt block can prevent a crawler from seeing a noindex directive. Plan preview exclusion deliberately and do not rely on robots.txt alone to guarantee removal from search.
- Confirm production HTTPS, preferred hostname, sitemap URL, canonical host, all retained 200 routes and all approved redirects before changing routing/DNS.
- Preserve Search Console verification, GA/GTM identifiers and existing email/DNS records if hosting changes. A same-domain hosting move does not call for an unnecessary domain change.
- Save a rollback deployment and a timestamped change log. Release during a period when someone can verify forms and key pages immediately.
- Submit the production sitemap and inspect representative priority URLs in Search Console after launch.

## After launch

| Window | Checks | Response |
| --- | --- | --- |
| Immediately and first day | Key URLs, redirects, robots/canonicals, contact delivery, phone links, analytics | Any unexpected noindex, widespread 404/5xx or broken lead delivery is an incident: fix or restore the last working deployment promptly. |
| Daily for two weeks | Local tracked rankings, top landing pages, indexing issues, crawl errors and leads | Compare the same device/location/query set. Investigate URL switching or losses with Search Console evidence; do not rewrite pages in response to one noisy position. |
| Weekly for weeks 3-8 | Query/page clicks, impressions, conversions, redirect hits, errors and field performance | Compare similar date windows and seasonality. Annotate changes. Separate demand change from technical breakage or lost relevance. |
| Before each later content batch | Baseline for the affected pages, proposed change and success measure | Change one content group at a time. Preserve earlier versions and review results before the next batch. |

Proposed review trigger, not an industry rule: investigate a sustained top-10 exit for a core tracked phrase or a material drop in several priority pages over comparable periods. A 20% traffic threshold is unreliable with very small counts; review absolute clicks, leads, seasonality and indexing together. Automated monitoring has not been scheduled by this audit.
