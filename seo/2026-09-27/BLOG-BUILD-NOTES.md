# Exact-content blog migration and homepage guide carousel

September 27, 2026. Local preview only. No production deployment or redirects.

## Inventory and preservation

Fetched the live homepage, `/blogs`, sitemap, and every discovered `/blog-post/` URL. These sources agree on 12 articles. No pagination or additional article URLs were present in this inventory. Full fetched pages are in the ignored research directory `homepage/research/blog-import-2026-09-27/`; the committed migration source is `homepage/blogs/content.json`.

All 12 article bodies retain their exact published text, including original punctuation, spelling, claims, headings, lists, and existing reading-time statements. The user's request for exact article content takes precedence over the site's general preference against em dashes. No keywords, rewritten paragraphs, invented dates, testimonials, or new claims were inserted into article bodies. Original H1s, card titles, and article URL paths are preserved. The homepage keeps its approved original H1.

The content file records source HTML, normalized source text, original metadata, image information, original structured data, and a SHA-256 fingerprint of each source body. The builder asserts text equality during rendering. `python3 homepage/check_blog_migration.py` independently checks the rendered article bodies, original H1s, canonicals, discovery links, and source fingerprints. Whitespace normalization allows layout changes, but words and punctuation must match.

## Semrush cross-check

Fresh US Organic Research request for `www.beautifulblindsandshades.com/blog-post/`, up to 50 rows sorted by position, returned 25 rows across five article URLs. Raw response and report URL: `blog-rankings.json`. Observations date from August 11 through September 15, 2026, not the retrieval date.

- Motorized blinds/shades: “blinds fort wayne indiana” #15; “fort wayne window treatments” #15; “window blinds fort wayne” #20; “blinds fort wayne” #21.
- Open-concept roller shades: “window treatments fort wayne” #28; “fort wayne window treatments” #31; “blinds fort wayne indiana” #34.
- Complete Fort Wayne guide: “window treatments fort wayne indiana” #43.
- Fall transformation and energy-efficiency articles also have returned rows at lower positions.

No returned rows for the other articles does not establish zero traffic or zero rankings. Unrelated geographic terms were not added to the site. These observations demonstrate article visibility, but cannot establish that the old homepage placement caused rankings or that the redesign will improve them. The conservative approach is to retain every original article destination and title link.

## Technical SEO corrections, without article rewriting

1. All 12 live article title tags were raw URL slugs. Their new HTML title tags use their existing visible H1 text verbatim. Visible titles were not rewritten or shortened.
2. The Columbia City shutter article had an additional H1 inside the body. Its text is preserved, with that heading changed to H2. There is now one H1 per page.
3. The missing Columbia City meta description and raw-slug Zebra Shades description were replaced with accurate article summaries. All other article descriptions and the blog index title/description are preserved.
4. A confirmed 404 link, `/shades/cellular-shades`, now points to the verified 200 URL `/custom-shades-fort-wayne-indiana/cellular-shades-fort-wayne-indiana`. Its anchor text is unchanged. `/contact-ghl` was checked and returns 200, so it remains a live-site link until separately migrated.
5. Existing links to rebuilt pages now use local routes. Unbuilt product/location/service destinations continue to use the original production domain, avoiding preview 404s.
6. Added appropriate BlogPosting and breadcrumb data. Removed unrelated copied Outdoor Shades schema from articles on other subjects. Source modification dates sometimes predate publication; unverified dates are omitted rather than invented. The organization byline and author entity are visible/consistent.
7. Added related guides and contextual product/service links outside the original article body. Original content and links remain readable HTML.
8. The index removes old duplicated placeholder/lorem-ipsum cards; it lists the 12 actual articles once. Article words are unaffected.

References checked: [Google crawlable links](https://developers.google.com/search/docs/crawling-indexing/links-crawlable), [Google Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article).

## Design and images

- `/blogs/`: branded, responsive library with a three-column desktop grid, two-column tablet layout, and single-column phone layout.
- Homepage: “Window treatment guides” above the final consultation section. All 12 exact original titles, in the original homepage order, are present as static anchor links. Desktop shows three full cards and a partial next card; phones show one and a preview. Previous/next buttons, touch scrolling, keyboard arrows, Home/End, and a position status provide navigation. No autoplay or JavaScript-only article loading.
- New “Guides” navigation link and existing footer advice link lead to `/blogs`.
- Articles: original H1, product image, expandable contents list, readable text width, consultation panel, and related guides. No owner video or hero review badges.
- Copied 12 original image files (10 hero images and two inline images). Source URL mapping: `homepage/blogs/assets.json`. Two live articles had generic placeholder hero images; those now use the existing roller-shade and wood-shutter product images already in the project. No newly generated imagery or invented installation attribution.

## Validation

- All 12 rendered article bodies match the imported text; original H1s and canonical URLs match; all 12 homepage and index title links exist.
- All 21 built pages: one H1, unique IDs, valid JSON-LD, existing local link/asset targets, same-page fragments, no unresolved template tokens, preview noindex retained.
- All 12 articles checked at 320px with no horizontal overflow. Representative article and library checked at 320, 390, 768, 1024, and 1440px. Desktop and mobile screenshots inspected.
- Desktop carousel traversed to the final card with the next control correctly disabled. Previous/next, keyboard Home/End/arrow navigation, mobile next, article links, contents links, and mobile menu were exercised.
- The import leaves original energy-saving percentages, warranty/durability promises, local claims, and timing statements unchanged. These remain candidates for a separately approved factual review, not silent migration edits.
- Native Contact form remains preview-only. No live forms were submitted.

## Updating

Run `python3 homepage/build_pages.py` to regenerate the blog index, articles, homepage carousel, and other interior pages. It reads the preserved blog source and uses `homepage/build_blogs.py` for layout. Check with `python3 homepage/build_pages.py --check`, `python3 homepage/check_blog_migration.py`, and `node --check homepage/dist/guides.js`.

Keep all preview noindex and robots protections until the actual production migration is ready. No claim of guaranteed rankings or causal ranking improvement is made.
