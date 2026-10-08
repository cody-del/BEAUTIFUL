# Homepage quality and SEO review

Reviewed October 7, 2026. Skills: copy-editing, customer-copy-guard, and SearchFit SEO.

## Verdict

The homepage has a sound structure and mostly useful, direct copy. It does not need another wholesale redesign or more sections for their own sake. Its largest artificial-looking element is the staged room photography. Its clearest source of clutter is repeated consultation reassurance. The strongest way to improve trust is to show the actual installations already supplied for the separate landing-page project.

This is an editorial and design judgment, not an AI-authorship detector or a prediction of ranking gains. Current Google guidance emphasizes original, accurate, useful content and a satisfying page experience, rather than a preferred word count or deleting older content to appear fresh. See [Google's content-quality guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) and [generative AI guidance](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content).

## Completed in this update

- Removed the “View Beautiful Blinds & Shades on Google Maps” link bar beneath the homepage and Contact maps.
- Removed the CSS used only by that bar. The blue service-area boundary, map controls, attribution, and failure fallback remain available. The Google review links remain elsewhere on the site.
- Preserved every existing title, H1, canonical, route, and imported blog body. No broader copy, image, or page-layout recommendations below were implemented in this update.
- Synced the newer GitHub main before applying the change, preserving its About page, slashless URLs, legacy redirects, sitemap, local schema logo, and image/font optimizations. The main website now has 54 pages, plus the 404 page and map document.

## What to improve, in order

### 1. Replace the staged room photography with relevant client work

**Where:** homepage hero, product cards, shared navigation photos, consultation background, and matching category pages.

The current blinds, shades, and shutter imagery shares a polished, neutral-room aesthetic. That repetition feels less specific to David's business than his real work. Asset provenance in the homepage notes identifies these as staged imagery rather than documented installations.

Ten client-supplied installation photographs are now recorded in `landing-page/content/installation-photos.json`, with originals under `client-photos/2026-10-07/originals/0921/`. They include roller shades, cellular shades, and plantation shutters. Use suitable existing exports to replace relevant image slots. Do not relabel a cellular-shade photo as blinds, invent the customer's city, or infer motorization from a still photograph. Keep a suitable licensed/approved product image where no matching installation photo exists. A new gallery section is not necessary to benefit from these photos.

### 2. Simplify the final consultation section

**Where:** `/#consultation`, using `homepage/dist/index.html` as its source; shared form also appears on `/contact`.

The section heading, benefit list, form heading, submit button, and reassurance row repeat the free-consultation offer five times. “No-pressure quote” appears in both the paragraph and reassurance row. Two separate sentences explain that the visitor will be contacted. On mobile this becomes a long sequence before and around a short form.

Recommended next edit: keep the section's free-consultation heading, one specific explanation of the visit, the phone/hours, and the form. Change the form heading to “Tell us about your windows.” Remove the duplicate reassurance row and the extra contact-expectation sentence; retain one accurate next-step statement. Keep useful CTAs at decision points instead of removing buttons throughout the page. These are proposed edits, not changes made during this audit.

### 3. Make repeated sections do different jobs

**Where:** homepage hero, David introduction, consultation/installation steps, FAQ, and final form; shared product and city templates.

Samples at home, measuring, installation, and a no-pressure quote recur throughout the homepage. Repetition near an action is useful, but whole sections should add something new. Keep the hero focused on the offer; use David's introduction for his personal involvement; use the process to explain order review and installation; let FAQs answer genuine questions about choice, timing, and one-window projects.

The sampled Shades and Repair pages provide useful distinctions such as solar-shade privacy at night and identifying a faulty mechanism. Preserve those details. The Columbia City page is more repetitive: its product cards and longer product explanations overlap, and several sections restate the home consultation. A future tightening pass should remove duplicate setup sentences while retaining unique trim, mounting, privacy, and renovation advice. Do not merge city pages or retarget their headings from this review alone.

### 4. Review inherited blog claims separately

**Where:** all 12 imported articles; especially `/blog-post/blackout-window-treatments-bluffton-homes`, `/blog-post/custom-roller-shades-fort-wayne-open-concept-homes`, and `/blog-post/cellular-shades-fort-wayne-energy-savings`.

The original articles contain the remaining strongest examples of formulaic prose and broad claims. Examples include complete light/heat elimination, unqualified evening privacy, numerical energy savings, and accounts of specific local projects. The blackout and roller-shade claims can conflict with the more careful fabric-and-edge-gap explanations on the current product pages. Energy/project anecdotes need business records or an appropriate product-specific source before being treated as established facts.

The client's exact-blog preservation instruction still applies. Keep their URLs, titles, article text, and homepage guide links unchanged until a separate, narrowly scoped factual-correction pass is approved. Start with verifiable inaccuracies and unsupported promises rather than rewriting every article for style. See the article-by-article evidence list in `../2026-10-02/COPY-REVIEW.md`.

### 5. Verify review claims

**Where:** homepage hero and consultation form.

The five written Google reviews are transcribed from client-supplied screenshots and are valuable proof. Preserve them. The Facebook 5.0 badge still lacks verification in this project's evidence, and the form's Google review count is hard-coded to 36. Verify those current figures before production, or remove unsupported numeric claims. This audit did not log into Facebook or establish a new Google review total; the approved badge design was not changed.

### 6. Resolve practical launch issues before adding more SEO copy

- **Lead delivery:** `homepage/dist/script.js` still prevents submission and shows the truthful unsent preview message. The form's introductory promise assumes a working endpoint. Connect and verify delivery before sending customers or paid traffic to the form. No test lead was sent in this review.
- **Map consistency:** the existing approximate blue outline follows the September screenshot. A comparison with the saved Census place coordinates puts Hicksville's center outside it, although Hicksville has a service page. Confirm coverage and reconcile the map/directory before the production migration. This is a geographic consistency finding, not an assertion about any individual address. See `map-coverage-check.json`.
- **Indexing:** Netlify remains intentionally noindex/nofollow. This audit does not remove that protection or move the original production domain. The rebuild itself cannot earn search visibility while excluded from indexing; production cutover needs its own launch checks.

## What should stay

- Homepage H1: “Beautiful Window Treatments Fort Wayne Indiana.”
- Useful blinds, shades, shutters, outdoor-shade, repair, and cleaning coverage with direct internal links.
- The real David video and customer-supplied review text.
- The restrained blue/green palette, consistent headings, compact buttons, and phone/menu navigation on mobile.
- The collapsed city directory and guide carousel. These keep links available without stacking every city or article into the page.
- Helpful qualifications about nighttime privacy, blackout fabrics versus edge gaps, motor compatibility, repair parts, and order timing.

## Semrush evidence and limits

Retrieved US Organic Research on October 7 for `beautifulblindsandshades.com`, 50 rows sorted by position. These are observations of the original domain, not rankings earned by the noindex Netlify rebuild.

| Keyword | Homepage position | Observation date, UTC |
| --- | ---: | --- |
| blinds fort wayne indiana | 3 | August 21, 2026 |
| window treatments fort wayne | 5 | August 20, 2026 |
| window treatments fort wayne indiana | 5 | September 5, 2026 |
| window blinds fort wayne | 9 | September 15, 2026 |
| blinds fort wayne | 10 | August 14, 2026 |

The report also shows the motorized guide at 15 for “blinds fort wayne indiana,” while the homepage is at 3 in the same dated observation. That overlap alone is not evidence of harmful cannibalization. It does not justify deleting or redirecting the guide. Repair and outdoor-shade pages also appear prominently in the returned rows, supporting retention of their homepage links.

Project discovery found Beautiful Blinds & Shades project `30275556`. Its campaigns response returned `targets: null`, despite tracking being listed as enabled. No usable location/device campaign was available through this report. These results are not fresh October local tracking or Search Console data. Do not interpret unchanged previous-position columns as proof rankings have remained stable through today.

Raw evidence: `semrush-project.json`, `semrush-campaigns.json`, and `semrush-organic.json`.

## Review scope and verification

- Read the homepage's rendered content, including shared navigation/footer, form wording, FAQs, reviews, guide titles, and map. Visually checked desktop products and consultation, plus homepage/Contact map layouts and mobile layout.
- Contextually sampled Shades, Repair, Columbia City, and the newly merged About content. Rechecked flagged passages in the three named inherited articles. This is not a new sentence-by-sentence manual review of all 54 pages.
- Automated content guard scanned all 56 HTML documents: no blocking findings or review warnings. This check detects recognizable internal prose/placeholders; it does not certify naturalness, accuracy, or authorship.
- Build-currentness, exact article preservation, product/city/service/About migration checks, legacy redirects, local links/assets, headings, IDs, JSON parsing, and preview indexation checks passed.
- All 56 documents retain their pre-edit titles, H1s, and canonicals. See `preservation.json`.
- No horizontal overflow in the inspected 1280px desktop and 390px mobile views. The removed link bar is absent from both map containers. No form endpoint, original-domain deployment, or DNS change was made.

Recommended next implementation: relevant real photos first, then the redundant form/section copy, followed by evidence-based article corrections under a separate approval. More headings, more city mentions, and more content length are not the objective.
