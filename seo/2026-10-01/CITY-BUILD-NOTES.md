# Final nine city pages: build and SEO evidence

Built October 1, 2026 for local review. This batch is not committed, pushed, or deployed. The original production website is unchanged. The preview retains `noindex, nofollow`.

## Scope and preservation

Added Columbia City, Bluffton, Grabill, Woodburn, Harlan, Hoagland, Angola, Kendallville, and Syracuse. The site now has 53 built pages, including all 17 city pages and the service-area directory. About and the `/contact-ghl` integration route remain unresolved from the 55-page inventory; launch work remains separate.

Each new page keeps its original URL, title tag, meta description, primary H1, production canonical, and leading “Custom Blinds and Shades in [city], Indiana” heading. Harlan keeps its original H1 without adding “In.” There are no city redirects, consolidations, or new local-office claims. Existing homepage and product keyword targets are unchanged.

All nine live URLs returned HTTP 200 on October 1. Their titles, descriptions, H1s, and normalized editorial text match the September 25 source archive. Fresh HTML is saved locally under `homepage/research/city-batch-2026-10-01/`; this research directory is Git-ignored. The original metadata, headings, and full editorial text are retained in the tracked `homepage/locations/source-baseline.json`. See [live verification](live-source-verification.json) and [before/after inventory](city-content-comparison.json).

## Semrush evidence and decisions

Refreshed `resource_organic` for each exact live city URL using database `us`, up to 50 rows sorted by position. This is US Organic Research data, not Fort Wayne device/location-specific Position Tracking or Search Console. The retrieval date is October 1; the observations themselves are dated below. Raw responses, including no-data responses, are saved in the nine `semrush-*.json` files beside this document.

| Page | Returned evidence | Content decision |
| --- | --- | --- |
| Bluffton | “best blinds fort wayne indiana” 76, August 12; “window treatments fort wayne indiana” 96, September 5 | Retain city URL and metadata; retain useful blind/shade topics and Fort Wayne business-base context. Keep the page focused on Bluffton service. |
| Harlan | “best blinds fort wayne indiana” 73, August 12 | Preserve Harlan target and source product topics. Do not turn the page into another Fort Wayne homepage. |
| Syracuse | One Lanesville query at 8, August 15 | Unrelated location; do not add Lanesville copy or claim this is a Syracuse ranking. |
| Columbia City, Grabill, Woodburn, Hoagland, Angola, Kendallville | `ERROR 50 / NOTHING FOUND` | No usable observations returned. This does not prove the pages have no rankings or justify removing them. |

Bluffton also returned an unrelated Zionsville query at 27 on August 6; Harlan returned a Lanesville query at 82 on August 15. Neither became a content target. These isolated results do not establish harmful cannibalization. No consolidation is proposed from this evidence.

## Content retained and corrected

The drafts preserve useful product and service coverage while removing repeated town praise, unverified local job histories, unattributed customer assertions, and broad return-on-investment promises. The approved city layout adds readable product links, installation steps, FAQs, and consultation actions. New copy is customer-facing and contains no em dashes.

| City | Useful original topics carried forward | Specific improvements |
| --- | --- | --- |
| Columbia City | Cellular, motorized, shutters, solar/roller, Roman; original trim, wide views, newer openings; measuring and installation | Link the existing Columbia City shutter guide without copying it. Replace unsupported installation/referral claims with practical trim, frame, and clearance guidance. |
| Bluffton | Cellular, motorized, shutters, solar/roller, Roman; older and newer windows; consultation and installation | Remove the Bluffton University reference. Link the existing Bluffton blackout guide. Explain fabric opacity versus gaps at the edges. |
| Grabill | Wood/faux wood, cellular, roller, vertical patio-door blinds, motorized controls; older and rural windows | Retain patio-door detail. Remove community stereotypes, “countless” installations, guaranteed longevity/ROI, and automatic evening/weekend availability. |
| Woodburn | Faux wood, cellular, Roman, solar, shutters; older, ranch, and rural openings | Correct the blanket claim that faux wood is lighter than wood. Remove immunity to all warping/fading and promised resale/energy returns. |
| Harlan | Double-cell cellular, wood, solar, motorized, Roman; older frames and exposed windows | Remove the Route 24/southeast-of-Fort-Wayne description. Explain that cell count alone does not establish twice the insulation; remove draft-elimination and automatic smart-home compatibility claims. |
| Hoagland | Blackout cellular, wood/faux wood, solar, roller, motorization; porches, workshops, manufactured/modular homes | Remove the southwestern-Allen-County description and unlimited weekend promise. Distinguish interior shades from products suitable for outdoor exposure. Retain privacy guidance without guaranteeing complete darkness or sealed drafts. |
| Angola | Cellular, motorized, shutters, solar/roller, Roman; older homes, lake-area homes, seasonal access | Retain view/glare and seasonal scheduling topics without asserting completed lake-home projects. Make room conditions, motor compatibility, and exact-address appointment arrangements explicit. |
| Kendallville | Cellular, motorized, shutters, solar/roller, Roman; replacements, older openings, new construction | Remove the Mid-America Science Park reference and unverified local testimonials. Add useful bracket, renovation timing, and care questions. |
| Syracuse | Cellular, motorized, shutters, solar/roller, Roman; year-round and seasonal homes, lake views | Use “Syracuse Lake”; retain lake-area context without inventing project history. Clarify raised-shade stack space, room conditions, and seasonal access. |

Original editorial sections ranged from 1,184 to 1,813 words; rebuilt main sections are approximately 1,075 to 1,136 words including headings and actions. Counts are not ranking targets, and the before/after scopes differ slightly. Larger reductions in Grabill, Woodburn, Harlan, and Hoagland remove substantial repeated marketing and unsupported performance/financial claims. Topic guards help prevent useful source topics from disappearing, but do not prove ranking preservation. Review material content changes before production cutover and retain the baseline for rollback.

Product corrections are consistent with primary-source guidance reviewed during this batch: [Graber wood versus faux wood](https://www.graberblinds.com/inspiration/window-treatments-101/real-wood-blinds-vs-faux-wood-blinds/), [composite and faux wood materials](https://www.graberblinds.com/window-treatments/blinds/composite-and-faux-wood-blinds/), [Graber motorization options](https://www.graberblinds.com/solutions/motorization/), [privacy and light control](https://www.graberblinds.com/solutions/privacy-and-light-control/), and [Department of Energy cellular shade guidance](https://www.energy.gov/cmei/buildings/articles/interior-cellular-shades-boost-home-energy-performance). Product availability and features still need confirmation for a customer's selected order.

## Implementation and checks

- Nine editable templates in `homepage/pages/`; source metadata in `locations/source-baseline.json`; registration in `build_locations.py`. They reuse existing CSS, header, footer, compact buttons, and assets.
- All 17 city directory links now resolve locally. Existing city links in articles are localized by the shared builder; all 12 article texts and titles remain exact.
- No hero review badges, owner video, maps, invented testimonials, or local address schema were added to city pages. Schema remains WebPage plus BreadcrumbList referencing the existing business.
- Build-currentness, all-page structure/schema/link/asset checks, exact blog preservation, 13 detail-page migration checks, service-page checks, location checks, and `git diff --check` passed.
- Location checks now preserve all 18 location routes and guard the new pages' useful source topics, contextual guide links, and known unsuitable phrases.
- Customer-copy guard scanned all 17 rendered city pages: zero blocking findings and zero review warnings. All nine new templates also received contextual editorial review. This is a review check, not a newly installed deployment gate.
- Browser checks covered all nine pages at 320, 390, 768, and 1280 CSS pixels: no horizontal overflow, one H1, centered hero headings, loaded hero images, and in-bounds 48px-high primary actions. Desktop cards, mobile hero/FAQ layout, mobile menu, and directory navigation were checked separately.

## Still separate from this build

Confirm outlying service coverage and any travel arrangements before final publication, especially Angola and Syracuse. No travel fees or guaranteed appointment availability have been invented. The pages invite customers to provide their exact address.

Lead delivery, the About page, `/contact-ghl`, final product-content review, analytics, the complete 122-URL migration map, and production indexation/domain changes remain in the launch plan. Forms are still preview-only and do not send leads. Current Netlify remains the earlier 40-page deployment until a new deployment is requested.
