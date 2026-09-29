# Shades and Plantation Shutters category build

Built September 27, 2026 as local design previews. No push, Netlify deployment, production-domain change, or redirect was made.

## Sources and ranking evidence

- September 25 archived live-page content and page briefs, cross-checked with the existing `/products/shades` and `/products/plantation-shutters` pages.
- Refreshed Semrush US `resource_organic` reports requested up to 50 rows per exact category URL. Raw responses and report links: `shades-rankings.json` and `plantation-shutters-rankings.json`.
- Shades returned 8 rows, observed August 11–September 15. Shutters returned 39 rows, observed August 5–September 26. Retrieval date is not observation date. These are database positions, not a live GPS-specific Fort Wayne search or Search Console performance report.

| Evidence | Implementation decision |
| --- | --- |
| Shades: window treatments fort wayne indiana #62; blinds fort wayne #77; window treatments fort wayne #85 | Preserve URL and local shade intent. Do not reposition it as another broad blinds/homepage landing page. |
| Shutters: plantation shutters nearby #31; plantations shutters near me #33; interior shutters near me #36 | Retain plantation/interior shutter coverage, selection guidance, and installation. |
| Shutters: custom plantation shutters near me #38; wood interior shutters near me #39 | Preserve material options and both existing wood/composite child links. |

Some report rows contain geographically unrelated terms. They are not evidence that the business serves those locations and were not used as content targets. Repeated query rows are retained in the raw report without averaging or inventing a single precise rank. No improvement or loss-free migration is promised.

## What is preserved

- Existing `/products/shades` and `/products/plantation-shutters` URLs as canonical targets.
- Exact original title tags and meta descriptions, checked against the archive.
- The existing local category heading topics. Shades now has an actual H1; its source page had none. One H1 per rebuilt page.
- All seven shade-detail links: roller, cellular, Roman, natural, solar, layered, and pleated. Additional sheer-shade coverage is retained as an enquiry option.
- Both shutter-detail links: wood and composite. Poly, faux wood, and vinyl choices remain discussed without universal material guarantees.
- Light filtering, room darkening, liners, cell construction, fabric choice, manual/motorized controls, measuring, mounting, budgets, and local coverage.
- Shutter louver sizes, finishes, visible/hidden tilt, divider rails, specialty shapes, room suitability, installation, and care.
- Shared navigation, genuine supplied reviews, brand colors, Manrope headings, mobile call controls, and smaller 48px-tall hero buttons.

## Targeted improvements

Repeated local-keyword phrases were rewritten into readable product guidance. No keyword-frequency or word-count quota was used. The pages retain purchase intent and topic coverage while leaving detailed product advice to the existing child URLs.

- Shade privacy guidance distinguishes fabric opacity from light gaps and explicitly addresses solar-screen privacy after dark. The old blanket no-gap claim was removed.
- Cellular construction is explained without guaranteed utility savings. Pleated and cellular styles are distinguished.
- Motorization and unusual window solutions are qualified by product and size instead of universal compatibility.
- Shutters no longer promise automatic resale-value increases, universal moisture resistance, specific lifespan, or guaranteed energy savings in body copy.
- Fixed lead times and broad unsupported installation-volume claims were omitted. Timing is confirmed for the actual order.
- Product link labels name the product instead of all saying “View Shades.”
- Native FAQ disclosures answer relevant selection and installation questions. No fabricated FAQ rich-result, review, price, or stock claims were added to structured data.
- CollectionPage and BreadcrumbList data identify each category and link to the shared business entity.

## Assets and navigation

`category-image-sources.json` records nine existing live-site product images. They were copied locally and sized to a maximum 1400px edge, without new image generation. They illustrate products; no image is identified as a documented client installation. Asset authenticity and permission for final use should be confirmed with the client if replacing these with project/manufacturer photography.

Homepage navigation, product cards, and footer now link to the two rebuilt local routes. The blinds page's shade-comparison link also uses the local route. Unbuilt product detail and service pages continue to use their existing live URLs. No video or owner video still is placed on product pages.

The generator now renders all three product categories from separate templates using a shared shell. Edit `homepage/pages/shades.html` or `homepage/pages/plantation-shutters.html`, then run `python3 homepage/build_pages.py`. The Contact page remains a separately rendered template with its honest preview-only form.

## Validation

- All five built pages: title and meta-description equality against the archived source; canonical targets; one H1; unique IDs; parsable JSON-LD; existing local routes and assets; same-page fragments; no unresolved template tokens.
- Both new categories: original child links retained; no em dashes, removed promotion, owner image, or video.
- Browser layout checks at 320, 390, 768, 1024, and 1440px: no document horizontal overflow. Desktop selection layouts and mobile hero/content visually reviewed.
- Mobile menu and treatment submenu navigation into Shutters, review expansion/collapse, category FAQ expansion, and installation-to-Contact navigation checked. No captured JavaScript errors.
- Generator `--check`, JavaScript syntax, and Git whitespace checks passed.

Preview noindex/robots protections remain. Lead delivery and the full URL migration checklist still need completion before a production launch. Next build batch: Outdoor Shades and the core service pages, followed by the preserved product-detail pages.
