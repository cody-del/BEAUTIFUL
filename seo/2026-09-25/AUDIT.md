# SEO audit and content plan

**Beautiful Blinds & Shades · September 25, 2026**

The rebuild should keep the existing domain and current page URLs, carry forward the content that supports rankings, and improve the weakest material in controlled stages. A blanket rewrite or deletion of low-traffic pages is not supported by this evidence. The best immediate opportunities are restoring equivalent legacy redirects, correcting wrong-page content, repairing the broken cellular-shades link, and fixing metadata and schema templates.

No migration can guarantee unchanged rankings. This plan reduces avoidable risk and gives us a baseline for measuring the result.

## Scope and evidence

| Source | Coverage | Important limit |
| --- | --- | --- |
| Fresh public-site crawl | 122 discovered URLs; 55 distinct live HTML pages; 64 final 404 responses; three additional homepage host/scheme variants redirect to the live home page | Discovered through current sitemap, recursively followed internal links, Semrush ranking and backlink URLs. Not a CMS/database export or access-log inventory. Unlinked URLs absent from all sources may remain undiscovered. |
| Current sitemap | 53 URLs, all returned 200 | One indexable article is missing; a noindex utility is correctly absent. |
| Semrush Organic Research, US database | 501 keyword/URL rows, 350 unique queries, 24 exact URLs in the keyword export | Observations span July 30 through September 24, 2026. Not a live Fort Wayne mobile/local-pack ranking check. |
| Semrush organic pages report | 26 URL rows | Page counts differ from deduplicated keyword export counts. Keep the datasets separate; do not force them to match. |
| Historical organic export | 427 rows requested for August 2026 | The report is a monthly/database comparison, with individual observations from July and August; not daily tracking or a causal migration experiment. |
| Semrush Backlink Analytics | 122 returned page rows across two requests | Link counts are Semrush observations, may include repeated/lost/low-quality links, and do not prove transferable authority or unique referring domains across URLs. |
| Semrush project | Project 30275556, www.beautifulblindsandshades.com | Rediscovered in the connected account. Position Tracking campaign discovery returned `targets: null`. No usable city/device daily tracking baseline was available from this response. |
| Saved Semrush Site Audit | July 27, 2026; 60 crawled pages; 77 errors, 61 warnings, 146 notices | Historical. A new independent crawl was performed for this report; the Semrush campaign itself was not rerun or changed. |

Live HTML was archived and inspected for content, headings, descriptions, canonical tags, robots directives, structured data and internal links. This was not a full browser-rendered audit of every viewport, a Core Web Vitals field-data analysis, a Google indexation test, or a lead-delivery test. Search Console clicks/impressions, GA4 conversions, server logs, Google Business Profile performance and the existing hosting redirect export were unavailable. Those remain launch-baseline requirements, not reasons to discard this audit.

## Ranking assets to protect

The [Semrush organic pages report](https://www.semrush.com/analytics/organic/pages/?db=us&q=beautifulblindsandshades.com) attributes about **92% of estimated organic traffic** to these four HTTPS pages. These small modeled estimates are prioritization signals, not measured visits or leads.

| Page | Reported keywords | Estimated traffic share | Rebuild decision |
| --- | ---: | ---: | --- |
| [/services/blind-shade-repair](https://www.beautifulblindsandshades.com/services/blind-shade-repair) | 112 | 35.13% | Keep URL and repair-topic coverage. Refine claims and clarity without stripping service detail. |
| [Homepage](https://www.beautifulblindsandshades.com/) | 20 | 32.43% | Keep broad Fort Wayne commercial ownership, title/description initially, business identity and category/service pathways. |
| [/services/outdoor-shades](https://www.beautifulblindsandshades.com/services/outdoor-shades) | 50 | 13.51% | Preserve outdoor/patio/roller-shade relevance, mounting and motorization information. |
| [/products/blinds](https://www.beautifulblindsandshades.com/products/blinds) | 121 | 10.81% | Preserve category URL and material coverage; remove unnatural keyword repetition carefully. |

Also protect cleaning, plantation shutters, the motorization guide and Auburn. Cleaning and shutters had valuable top-10 observations in the historical export even though the latest modeled traffic is zero. Zero estimated traffic is not proof that a page has no leads or search value.

### Fort Wayne baseline

These are [US Organic Research observations](https://www.semrush.com/analytics/organic/positions/?db=us&q=beautifulblindsandshades.com), with the reported date of each row:

| Query | Best returned homepage position | Observation date |
| --- | ---: | --- |
| blinds fort wayne indiana | 3 | August 21 |
| window treatments fort wayne | 5 | August 20 |
| fort wayne window treatments | 5 | August 25 |
| window treatments fort wayne indiana | 5 | September 5 |
| window blinds fort wayne | 9 | September 15 |
| blinds fort wayne | 10 | August 14 |

A separate Semrush keyword SERP report returned the homepage at **6** for “blinds fort wayne” and **5** for “window treatments fort wayne.” That disagreement is recorded rather than hidden: report datasets and refresh times differ. Neither is a verified live local search from a Fort Wayne device.

The current demand report estimates US monthly volumes of 140 for “blinds fort wayne,” 90 for “window treatments fort wayne,” 70 for “blinds fort wayne indiana,” and 10 for “motorized blinds fort wayne.” Several detailed local product phrases return zero or no row. We should still build useful product coverage for real customers. Do not sum close variants into a promised traffic opportunity, or treat ambiguous Auburn/near-me queries as exclusively Indiana demand.

### Existing movement to investigate

The historical-to-current exports show “blind cleaning companies near me” moving from 4 to 43, “window shades repair near me” from 3 to 16, and “wood interior shutters near me” from 5 to 39. These are database observations and cannot be attributed to the rebuild, which has not replaced the live site. Capture local tracking and Search Console history before launch so existing volatility is not mistaken for a migration problem.

## Highest-priority findings

### 1. Legacy URLs are losing visitors and potentially link value

The fresh crawl verified **64 404 URLs** in the combined discovery set. **22** have a combined **560 reported backlinks** in Semrush. The count is not 560 unique websites and is not a quality assessment.

The [redirect plan](url-preservation-and-redirect-plan.csv) proposes 55 equivalent-page redirects and leaves nine uncertain/restoration cases for review. No redirects were installed. Examples:

| Broken URL | Proposed matching destination |
| --- | --- |
| `/service-area/angola-indiana` | `/beautiful-blinds-shades-service-areas/window-treatments-angola-indiana` |
| `/service-area/leo-cedarville-indiana` | `/beautiful-blinds-shades-service-areas/window-treatments-leo-cedarville-indiana` |
| `/shades/cellular-shades` | `/custom-shades-fort-wayne-indiana/cellular-shades-fort-wayne-indiana` |
| `/contact-us` | `/contact` |
| `/window-treatment-blog` | `/blogs` |

Implement only verified intent matches. Review `/service-area/col`, `/ROUYZ/`, former generic hubs, sheer shades and legal-policy routes separately. Do not send every 404 to the homepage. Use permanent server redirects and keep them long term; Google recommends generally at least a year for migrated URLs. [Google migration guidance](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes).

### 2. Wrong-city and wrong-product content

- [Monroeville](https://www.beautifulblindsandshades.com/beautiful-blinds-shades-service-areas/window-treatments-monroeville-indiana): main copy describes Woodburn. Its CMS rich-text body has approximately **99.4% five-word-shingle Jaccard similarity** with Woodburn's body. This is a reproducible editorial comparison, not a Google score. Rewrite the incorrect body for Monroeville; keep both distinct cities' URLs.
- [Warsaw](https://www.beautifulblindsandshades.com/beautiful-blinds-shades-service-areas/window-treatments-warsaw-indiana): contains the Bluffton content followed by Warsaw content. Remove the misplaced Bluffton section and strengthen the Warsaw-specific material.
- [Hicksville](https://www.beautifulblindsandshades.com/beautiful-blinds-shades-service-areas/window-treatments-hicksville-indiana): title and hero say Indiana; body and footer refer to Ohio. Confirm the intended service locality, align title/H1/body/schema, and retain the existing slug at first launch.
- [Roller shades](https://www.beautifulblindsandshades.com/custom-shades-fort-wayne-indiana/custom-roller-shades-fort-wayne-indiana): hero H1 says Solar Shades. Correct the heading without changing the roller-shades URL.

### 3. Product pages need useful substance, not longer filler

The [wood shutters](https://www.beautifulblindsandshades.com/custom-interior-plantation-shutters-fort-wayne-indiana/custom-wood-plantation-shutters-in-fort-wayne-indiana) and [composite shutters](https://www.beautifulblindsandshades.com/custom-interior-plantation-shutters-fort-wayne-indiana/custom-composite-plantation-shutters-in-fort-wayne-indiana) pages have product headings but almost no material-specific body copy in the fetched HTML. Both largely repeat the same generic process and CTA. Preserve their distinct buying intents and add material, finish, panel/clearance, moisture, care and warranty information confirmed against actual offerings.

Other product pages contain useful comparisons and limitations worth keeping. Improve readability, specificity and evidence instead of replacing every paragraph. On category pages, repeated phrases such as “custom blinds for windows Fort Wayne IN” interrupt ordinary sentences. Use local wording naturally and give shoppers practical comparisons.

### 4. Metadata and heading template problems

- **54 of 55 live pages lack an HTML canonical**, including 53 of the 54 indexable candidates. Missing canonicals are a consolidation/hygiene issue, not proof of a ranking penalty.
- **Four pages have no H1:** blinds, shades, window-treatment service and service-area overview.
- **Nine have multiple H1s:** homepage, About, Monroeville, all four blinds detail pages, Roman shades and the Columbia City shutters article. Fix the hierarchy for clarity; multiple H1s alone do not prove lost rankings.
- **All 12 article titles are raw URL slugs.** Use readable, topic-specific titles in stages; preserve the slugs themselves.
- The Columbia City shutters article has no meta description.
- The [Bluffton blackout article](https://www.beautifulblindsandshades.com/blog-post/blackout-window-treatments-bluffton-homes) is linked internally and returns 200 but is absent from the sitemap.
- `/contact-ghl` already has `noindex`. Check CRM/advertising dependencies before merging it with `/contact`.

### 5. One confirmed broken internal destination

The [cellular energy article](https://www.beautifulblindsandshades.com/blog-post/cellular-shades-fort-wayne-energy-savings) links to `/shades/cellular-shades`, which returns 404. Update the internal link to the current cellular product URL, and add the legacy redirect. This confirms the July Semrush issue is still present.

### 6. Schema needs truthful, page-specific templates

The current JSON-LD parses successfully, but valid JSON is not the same as accurate schema or rich-result eligibility. All 12 article schemas describe the topic as Outdoor Shades, including articles on cellular shades, motorization and shutters. Several modification dates precede publication dates; confirm imported dates rather than inventing new ones.

Sampled product markup supplies `Offer`/`InStock` and currency without a price, and repeats generic view/privacy attributes even on cellular shades. For quote-based service/category pages, use accurate WebPage, Service, business and breadcrumb entities as appropriate. Use Product/Offer only where the actual page and required properties support it. Never invent a price to satisfy a validator. [Google Product snippet requirements](https://developers.google.com/search/docs/appearance/structured-data/product-snippet).

Do not promise organic review stars from the client's own Google/Facebook testimonials. Google excludes self-serving LocalBusiness/Organization review snippets, including embedded reviews. Keep authentic testimonials for visitor trust. [Google review guidance](https://developers.google.com/search/blog/2019/09/making-review-rich-results-more-helpful).

Keep useful FAQs for customers, but do not prioritize FAQ markup as a rich-result opportunity. Google's current documentation changelog says FAQ rich results stopped appearing May 7, 2026. [Google Search documentation updates](https://developers.google.com/search/updates).

The saved Semrush audit's 75 markup errors are historical item-level findings, not 75 broken pages. Revalidate the rebuilt templates rather than carrying that count into a claim about current errors.

## Cannibalization and page ownership

Fifteen queries have multiple returned URLs. That establishes overlap, not harmful cannibalization. The homepage clearly leads broad Fort Wayne queries in this export; many other matches are much weaker. No daily URL-switching data or conversion evidence was available to prove harm.

| Overlap group | Primary owner | Treatment during rebuild |
| --- | --- | --- |
| Broad Fort Wayne window treatments/blinds | Homepage | Keep authority here. Product category pages answer narrower buying decisions. |
| Homepage vs `/services/window-treatments` vs Fort Wayne city page | Homepage for broad local buying; service page for consultation/install process; city page for verified local coverage/projects | Differentiate first. City-to-home consolidation remains conditional on Search Console, links and conversion review. |
| Cellular product vs cellular winter article vs general energy article | Product page for buying; cellular article for insulation/how-to; energy article for comparisons | Keep and cross-link; remove repeated sales introductions and unsupported savings claims. |
| Roller product vs open-concept roller article | Product page for selection; article for coordinating multi-window rooms | Keep both. Correct roller H1 and link the guide to the product. |
| Layered/zebra product vs motorized-zebra article | Existing layered product URL for synonyms; article for automation/operation | No separate zebra synonym landing page at this stage. |
| General motorization | Existing motorization article | Improve established URL before proposing a new competing commercial page. |
| Outdoor service vs outdoor guide | Service for quote/installation; guide for selection, fabric and weather considerations | Preserve both, clarify purpose and links. |
| Local energy article vs general energy guide | General guide for broad comparison | Leo-Cedarville article must earn its own role with specific value. Later merge only if evidence supports it. |
| Monroeville/Woodburn; Warsaw/Bluffton | Each city owns its own real service intent | Correct copied bodies. These are not reasons to redirect one city into another. |

Low-performing city pages should not all receive mass rewrites that swap place names. Replace generic tourism/community praise with confirmed service logistics and relevant, documented examples. Do not invent local projects, offices or quotes. Google distinguishes useful content from doorway pages made for closely related queries. [Google spam policies](https://developers.google.com/search/docs/essentials/spam-policies).

## Content quality and differentiation

The existing content has useful selection topics but often relies on repeated sales language, unsupported performance figures and first-person customer stories that need verification. The [claims register](claims-to-verify.csv) flags 111 passages, including lead times, warranties, lifespan, repair rates, savings and anecdotes. A flag means “verify,” not “proven false.”

Specific review priorities:

- Separate reduced heat loss through a window from household bill savings. Claims of 10-20% savings for local customers need real supporting evidence; do not reuse them as universal outcomes.
- Confirm product-specific UV data, openness, nighttime privacy, wind limits and blackout edge gaps.
- Reconcile 2-3 week and 3-4/4-6 week timing statements by product and current supplier conditions.
- Verify experience years, “hundreds/thousands” of projects, manufacturer relationships, in-stock repair parts and service warranty terms.
- Verify stories attributed to David before writing in his voice. Use supplied real reviews accurately and do not assign them to a city without evidence.
- Confirm the current promotion before reusing the sitewide Buy 2 Get 1 offer.

The [DOE cellular-shade research](https://www.energy.gov/sites/default/files/2021-12/bto-cellular-shades-factsheet-112221.pdf) provides a better starting point for qualified energy discussion than unsupported local savings claims. Match any statistic to its tested conditions and the actual product.

The Semrush top-10 reports include Best Blinds, Budget Blinds and Zeigler's. A focused review of their public sites shows that free in-home consultation is common, not a unique selling point. [Best Blinds](https://bestblindsfortwayne.com/) emphasizes its process and experience; [Zeigler's](https://www.zeiglerswindowcoverings.com/) clearly identifies its manufacturer relationship and product range; [Budget Blinds Fort Wayne](https://www.budgetblinds.com/fortwayne/) also promotes an in-home consultation.

Our differentiation should be evidence of David's actual work: owner involvement, clear product tradeoffs, repair/cleaning expertise, genuine reviews and real installations. The recommendation is an editorial inference from the comparison, not proof that copying any competitor feature improves rankings. Google's people-first guidance supports first-hand usefulness over volume. [Helpful content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).

## Writing and build order

1. **Freeze the baseline and implement the migration requirements.** Maintain URL paths and a reversible deployment. Prepare confirmed legacy redirects and full route coverage.
2. **Protect priority pages:** homepage, repair, outdoor shades, blinds, cleaning, shutters, motorization and Auburn. Bring forward their useful content before making broad stylistic cuts.
3. **Fix clear content/template defects:** Monroeville, Warsaw, Hicksville, roller H1, missing H1s, blog titles, missing description, sitemap and schema.
4. **Build distinct product detail pages:** strengthen weak shutter pages, preserve useful shade/blind comparisons, and connect category-to-child links.
5. **Improve city and editorial content in batches:** use the page briefs and actual business evidence. Measure before consolidating.

No extra pages are recommended solely to hit every keyword spelling. Wood/faux wood and blackout intent can first be covered well on existing category/product pages. Additional dedicated pages should follow confirmed offerings, distinct intent and demand evidence.

Plain HTML or a static generator that emits complete HTML is suitable for this rebuild. There is no inherent ranking bonus for a particular framework. Keep text and links available without client-side rendering, use shared templates to avoid copy/paste mistakes, preserve real URLs, and validate performance on the finished design.

The next build should use [PAGE-BRIEFS.md](PAGE-BRIEFS.md) and the [launch checklist](MIGRATION-CHECKLIST.md). Content is ready to plan and draft page by page; final factual approval, lead delivery, tracking and migration checks still precede replacement of the client's live site.
