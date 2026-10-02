# Beautiful Blinds & Shades homepage

Static HTML/CSS/JavaScript website review. The visual reference is Naples Shutter's Bahama & Colonial page, using Beautiful Blinds & Shades branding.

Serve `dist/` locally with `python3 -m http.server 4317 --bind 127.0.0.1 --directory dist` from this folder. The homepage intentionally includes a noindex directive and a canonical to the client's existing domain. Complete the URL inventory and launch checklist before replacing the live website.

Source files:

- `dist/index.html`: homepage and metadata
- `dist/styles.css`: responsive styling
- `dist/script.js`: responsive dropdown navigation, click-to-play video, review carousel, and native form validation
- `dist/assets/`: original client assets and locally hosted Manrope heading font
- `SEO_NOTES.md`: ranking baseline, keyword ownership, and launch requirements
- `research/`: local source evidence and the Semrush baseline, excluded from the hosted artifact

The consultation card is a native four-field form modeled on the Naples project. It validates names, phone, and email locally, but this review build does not transmit or store contact details. Valid submissions show an explicit preview notice, never a success confirmation. Before launch, connect a server-side endpoint to Beautiful Blinds & Shades’ own CRM, add server validation and abuse protection, confirm the appropriate privacy policy, and verify delivery and the existing follow-up workflow. Never reuse another client’s credentials or expose a private CRM key in browser JavaScript. The former embedded form ID was zJjnT8CYHC8I93TcxC76. No live test leads have been sent.

## Service-area map

`dist/service-area-map.html` and `dist/service-area-map.js` render a lazy-loaded Leaflet map with OpenStreetMap tiles and visible attribution. The geographic polygon is an approximate trace of the client-supplied September 22 screenshot, not an administrative boundary. Its solid 3.5px brand-blue (#67b2e8) stroke has a white casing for contrast. Fit-to-boundary behavior preserves the full outline on desktop and mobile; scrolling the page does not zoom the map. The Google business listing remains linked below. Leaflet 1.9.4 is pinned with integrity hashes. Provider references: https://leafletjs.com/examples/quick-start/ and https://operations.osmfoundation.org/policies/tiles/.

## Review and media updates

The Google carousel contains five client-supplied reviews and shows four cards on desktop, with responsive layouts and manual navigation. Long reviews expand in place.

The video thumbnail is an authentic frame at 00:02 of David’s Wistia introduction, media ID `cfwf2ryb20`. The name and role appear below the video as a small black caption. The process section uses a plain background. Existing staged room imagery remains a placeholder and is not documented client installation photography.

## Responsive navigation and video playback

The full-width header contains custom Window Treatments and Services dropdowns on desktop. At 1000px and below it switches to a call button and expandable navigation menu. Mobile menu sections have large touch targets, close on selection or Escape, and scroll independently on short screens. Centered mobile content uses shared widths and alignment. Layout checks cover widths from 320px to 1920px.

The introduction uses native HTML video controls with inline mobile playback and `preload="none"`. It streams the original 720px-wide MP4 from the client’s Wistia delivery CDN after a user clicks Play, avoiding the blank third-party iframe. The existing video thumbnail and caption remain in place. A direct video link appears if playback fails.
# Category pages

Design/content decisions confirmed September 26: omit the buy-two-get-one offer from the rebuild. Do not reintroduce it from archived source pages. Use direct headings and restrained decoration; keep product and review cards, but avoid decorative material icons and numbered room labels. Current room imagery remains in place pending real project photos or approved manufacturer replacements.

The first category preview is available at `/products/blinds/`. Edit its content in `pages/blinds.html` and its styles in `dist/category.css`, then run `python3 homepage/build_pages.py` from the repository root. The generator reuses the current homepage header, reviews, and footer. Hero review badges remain exclusive to the homepage; shared elements are reused to keep them consistent. Run `python3 homepage/build_pages.py --check` before publishing to detect stale generated output. Netlify still publishes the committed `homepage/dist` directory without a build step.

See `../seo/2026-09-26/BLINDS-BUILD-NOTES.md` for the Semrush baseline, content decisions, validation, and migration requirements. Keep the preview noindex protections until the production migration is ready.

## Contact page

The Contact preview is at `/contact/`, with the existing `/contact` canonical. Edit `pages/contact.html` and `dist/contact.css`, then run the shared generator above. The homepage and blinds consultation buttons now point to `/contact`; buttons on the Contact page jump to its form. The form reuses the four required contact fields and adds optional treatment and project-detail fields. Both homepage and Contact forms do not send details. The persistent preview label was removed at the user’s request; submitting still truthfully explains that nothing was sent.

See `../seo/2026-09-26/CONTACT-BUILD-NOTES.md` for preserved metadata, Semrush limitations, and validation.

## Shades and Plantation Shutters

The next category previews are `/products/shades/` and `/products/plantation-shutters/`. Their editable content lives in the matching files under `pages/`; they share `dist/category.css` and the category generator. All 13 original product-detail routes are now built as well. Remaining unbuilt service, location, and company pages continue to link to the live site.

The smaller hero buttons use a 48px minimum height and 14px text across all category and homepage heroes. Owner videos and video stills stay off product pages.

See `../seo/2026-09-27/CATEGORY-BUILD-NOTES.md` for preserved metadata, fresh Semrush evidence, content decisions, image sources, and validation. Run `python3 homepage/build_pages.py --check` before any deployment.

## Blog library and exact article migration

`/blogs/` and all 12 original `/blog-post/` URLs are rebuilt. The homepage's guide carousel includes every original title and link near the bottom. Articles retain their exact source text; `blogs/content.json` stores the imported HTML and fingerprints. Edit layouts in `build_blogs.py` and `dist/blog.css`; carousel controls live in `dist/guides.js`. Run `python3 homepage/build_pages.py` to refresh all pages and the homepage carousel, then `python3 homepage/check_blog_migration.py` to verify article preservation and local routes. Do not rewrite imported article text as part of styling changes. See `../seo/2026-09-27/BLOG-BUILD-NOTES.md` for the narrowly scoped SEO corrections and remaining content review items.

## Shared buttons

Action buttons use `.button` in `dist/styles.css`: 48px minimum height, 14px bold text, 8px corners, and brand green. `.small` is the 44px navigation variant; `.button-outline` uses blue on light sections and white on dark sections. Page styles should change placement or width only. Mobile standalone actions are capped at 300px; forms and product cards fill their containers. Review and guide arrows share 44px circular controls.

The persistent preview notice has been removed from the consultation forms. Lead delivery is still unconnected; the submission handler retains its truthful unsent status.

## Product page design

`dist/product.css` is the shared layer for the four built product categories: blinds, shades, plantation shutters, and outdoor shades. It standardizes section spacing, product cards, open guidance sections, installation steps, city dropdowns, and final consultation actions. Product-specific comparison tables and details remain in `category.css`. Repair, cleaning, contact, and blog pages do not load this layer. New product pages should reuse this layer and `.product-installation` / `.product-final` rather than adding page-specific button or heading styles.

## Product-detail pages

The 13 sub-product pages share `dist/subproduct.css` with the product/category styles. `build_subproducts.py` renders their existing original URLs from `subproducts/editorial.py` and the metadata archived in `subproducts/source-baseline.json`. Do not shorten these routes or replace their title tags during design work. Run the shared builder and `python3 homepage/check_subproduct_migration.py` after edits.

See `../seo/2026-09-28/SUBPRODUCT-BUILD-NOTES.md` for Semrush report limitations, content revisions, verification, and the original-to-draft comparison. All 34 preview pages remain noindex.


## Service-area overview and Auburn pilot

The local preview now contains 36 pages. `build_locations.py` renders `pages/service-area.html` and `pages/auburn.html`, with shared category/product styles and `dist/location.css`. Original metadata and source text are archived in `locations/source-baseline.json`; `locations/city-routes.json` preserves all 17 original city routes. The directory starts collapsed. Auburn links locally; the other 16 towns still lead to their original live pages until rebuilt.

Run `python3 homepage/build_pages.py`, then `python3 homepage/check_location_migration.py` alongside the existing blog and sub-product checks. Keep preview noindex protections. Coverage confirmation and pilot design/content review remain open. See `../seo/2026-09-29/LOCATION-BUILD-NOTES.md`.

## Monroeville, Warsaw, and Hicksville

The preview now contains 39 pages. The three new city templates reuse the Auburn layout and `build_locations.py`. Monroeville and Warsaw preserve their original metadata and primary H1s while correcting the copied wrong-city bodies. Hicksville has a documented Ohio title/H1 correction in `METADATA_OVERRIDES`, while its original Indiana slug stays unchanged. Keep that draft pending coverage confirmation before production.

The city directory now links to four local city pages; the other 13 remain on the original live site. `check_location_migration.py` covers all five built location routes and guards against reintroducing wrong-city text. See `../seo/2026-09-29/CITY-CORRECTIONS-BUILD-NOTES.md` for evidence, content changes, Semrush limitations, and checks.

## Window treatment service

`/services/window-treatments/` is built from `pages/window-treatments.html`, with the original metadata archived in `pages/window-treatments-source.json`. It uses the service hero plus the shared product installation/final-action styles. The shared Services menu and homepage process link now lead to the local route. Run `python3 homepage/check_window_treatment_service.py` after the shared build, alongside the existing migration checks. The preview now contains 40 pages. See `../seo/2026-09-29/WINDOW-TREATMENT-SERVICE-NOTES.md` for SEO evidence, editorial changes, and unconfirmed business details.

## Fort Wayne and Allen County city batch

That batch brought the local review build to 44 pages. `pages/fort-wayne.html`, `pages/huntertown.html`, `pages/leo-cedarville.html`, and `pages/new-haven.html` reuse the city layout and retain original metadata and H1s. See `../seo/2026-09-29/ALLEN-COUNTY-CITY-BUILD-NOTES.md` for source comparisons and dated Semrush evidence.

## All 17 city pages built locally, October 1

The latest review build contains 53 pages. Columbia City, Bluffton, Grabill, Woodburn, Harlan, Hoagland, Angola, Kendallville, and Syracuse are now built from their corresponding `pages/*.html` templates. All 17 city directory links lead to local pages. Original URLs, titles, descriptions, H1s, and production canonicals are retained for this batch. See `../seo/2026-10-01/CITY-BUILD-NOTES.md` for fresh source verification, Semrush limitations, content comparisons, and QA.

About and `/contact-ghl` remain unresolved, alongside form delivery and the production launch checklist. Run the shared build and migration checks before publishing. Keep preview noindex protections in place.

## Reviewed 53-page release, October 2

The current review build includes all 17 city pages and the full-site copy cleanup. All 53 titles, H1s, and canonical URLs are preserved from the start of the copy pass, and all 12 imported article texts remain exact. See `../seo/2026-10-02/COPY-REVIEW.md` for the review, change record, validation, and remaining claims to verify. Netlify publishes `homepage/dist` from GitHub `main`; this release updates the review site, with noindex and the existing non-delivery form behavior retained.
