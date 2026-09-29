# Sub-product preview build, September 28, 2026

Built all 13 existing detail URLs: four blind styles, seven shade styles, and wood/composite plantation shutters. The preview now contains 34 pages. Nothing was deployed or pushed by this task.

## Ranking evidence and limits

Three Semrush `resource_organic` US subfolder reports were requested on September 28 for the original blinds, shades, and shutter detail folders, with keyword, position, URL, and timestamp columns. All returned `NOTHING FOUND`; raw responses are saved alongside this note. This is unavailable evidence, not a finding that the pages have no rankings, impressions, links, or value. The September 25 page inventory likewise had no returned US keyword rows for these 13 URLs. No page was merged, deleted, or redirected on that basis.

Retained every original detail URL and title tag. Each new canonical is the absolute original production URL. Original primary H1 words remain except for the roller page's incorrect “Solar” heading and the pleated page's “FOrt” typo. Duplicate source H1s are not repeated. The existing seven shade descriptions incorrectly reused “sheer shades”; those descriptions now name the actual product. Blind and shutter descriptions remain unchanged.

## Content treatment

The original product copy is archived in `homepage/subproducts/source-baseline.json`. This is a substantive editorial draft, not an exact-text product import. The 11 populated pages have been condensed into product-specific options, fitting, care, and questions. Repeated city-name insertions, disparaging filler, unsupported numeric performance/pricing/lifespan claims, broad warranty promises, and universal motor/app compatibility claims were not carried over. The two shutter detail pages previously contained effectively only the shared process/CTA text; they now have material-specific guidance.

The original topics remain the basis of each page, but this is not a claim that shortening them will improve rankings. Review the original-versus-draft content and Search Console query/page evidence before production migration. `subproduct-migration.csv` records URLs, metadata changes, and source/draft word counts. The current preview remains noindex. Existing exact blog wording and titles are unchanged.

Technical distinctions were cross-checked with primary manufacturer guidance, not used to imply that every listed option is stocked by this client:

- [Graber shade privacy and light control](https://www.graberblinds.com/solutions/privacy-and-light-control/)
- [Graber solar shade overview](https://www.graberblinds.com/inspiration/window-treatments-101/what-are-solar-shades/)
- [Bali solar shade privacy](https://www.baliblinds.com/inspiration/design-blog/solar-shades--nighttime-privacy-explained/)
- [Graber cleaning instructions](https://www.graberblinds.com/customer-support/cleaning-instructions/)
- [Graber pleated shade construction](https://www.graberblinds.com/window-treatments/shades/pleated-shades/)

Current photos are the assets already imported from the original category pages. They are not represented as verified client installations. No new AI imagery, owner video, hero rating badges, offer, invented warranty, or fabricated review was added.

## Design and internal links

The detail pages reuse the approved header, hero treatment, typography, compact CTAs, brand colors, and footer. Open material/fabric columns, a fitting section, native FAQ disclosures, and two related-product links replace decorative icons or repeated card grids. A small section-navigation row also works on mobile. Contact buttons lead to the existing custom form page.

Category links and links in preserved blogs now resolve locally when the exact destination has been built. Other live-site links remain intact. The builder localizes anchor destinations only; canonicals stay absolute production URLs. Related guides retain their original titles and URLs. Layered/zebra terminology shares one page; no competing synonym route was created.

## Verification

- `python3 homepage/build_pages.py --check`: generated output current.
- `python3 homepage/check_subproduct_migration.py`: 13 original routes/titles, expected H1s, absolute canonicals, category discovery, no hero badges/video, and local migrated destinations passed.
- `python3 homepage/check_blog_migration.py`: all 12 articles exact; 34 pages passed heading, ID, JSON-LD, noindex, local-link, and asset checks.
- Browser: all 13 pages at 320px had no horizontal overflow, loaded hero images, visible section navigation, one H1, and primary CTA targets at least 44px high. Representative checks at 390px, 768px, and the default desktop viewport; mobile menu/submenu and FAQ expansion verified.
- No production lead submission, ranking improvement, Lighthouse score, or live deployment is claimed.
