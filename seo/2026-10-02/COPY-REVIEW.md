# Full-site copy review

Reviewed October 2, 2026 using copy-editing, copywriting, and customer-copy-guard.

The rebuilt service, product, and city copy is clearer and more useful after this pass. The largest unresolved editorial concerns are in the imported articles. Those articles remain exact under the client's preservation instruction. This review does not establish that the site is ready for production or predict ranking changes.

## Scope and method

Read the rendered main content of all 53 local pages: the homepage, Contact, Guides, three product categories, 13 product-detail pages, four service pages, 17 city pages, the service-area directory, and 12 imported articles. Also reviewed the shared navigation and footer, forms and validation messages, video fallback copy, carousel labels, metadata, image descriptions, accessible labels, structured-data output, and the separate service-area map document.

Applied the seven editing sweeps: clarity, voice, customer benefit, proof, specificity, emotional relevance, and next-step clarity. Read the modified passages again after editing. Repeated shared reviews/components were reviewed once, rather than counted as independent new copy on each page. Customer quotations were preserved, including the grammar in the supplied originals.

This was a review of the local rebuild. It did not refresh Semrush rankings, re-verify every business or product claim with the client, test external websites, or change the original live site or Netlify deployment.

## Changes made

60 targeted edit entries across 23 source files, including one shared capitalization fix. The exact record is in `copy-edits.json`. Generated pages were rebuilt from their source templates.

Examples:

| Before | After / reason |
| --- | --- |
| “We keep them together here so you can compare…” on Layered Shades | Directly explains that zebra and layered shades are two names for the same style. Removes commentary about organizing the website. |
| “fabric opacity,” “grouped operation,” and “raised stack height” | Uses explanations of light blocking, moving shades together, and folded fabric covering the glass where those terms were unexplained. |
| “A replacement blind … needs a different conversation” | Describes replacing one blind or covering all the windows before move-in. |
| “These are planning considerations…” | Explains the frame, handles, and mounting space the installer checks. |
| “Give your window treatments some attention” | “Ask about cleaning your blinds and shades.” |
| Homepage question about installation followed by a two-to-three-week order estimate | Question now covers ordering and installation. Answer explains product-dependent timing, confirmed before ordering. No unverified numerical lead time. |
| Lowercase “roman” and “venetian” in generated headings and links | Keeps Roman and Venetian capitalization consistent. |
| Warsaw copy telling the visitor to measure the recess | Clearly says the business takes those measurements. |

Also simplified the window-treatment-service introduction, removed passive wording from the repair process, clarified the service-area repair/cleaning answer, and removed wording that could imply a consultation includes an after-dark visit.

The seven-sweep review was followed by a single-editor review using four perspectives, not separate reviewers or customer testing. For the revised primary page copy: conversion clarity 8/10, UX wording 9/10, brand consistency 8/10, skeptical-buyer clarity 7/10. These subjective scores apply to the revised copy only. They exclude the protected articles and do not mean delivery integrations or business claims have been verified.

## Preservation and checks

- All 53 existing local page titles, H1s, and canonical URLs are unchanged from the start of this pass. The homepage H1 remains “Beautiful Window Treatments Fort Wayne Indiana.”
- All 12 article bodies and article titles pass exact-text preservation checks. Their original prose, testimonials, and historical wording were not rewritten.
- Product and city routes, product topics, internal destinations, qualifications, and heading order remain in place.
- Two meta descriptions changed only to capitalize Roman: the shade category and Roman shade detail page.
- All 52 generated interior outputs are current.
- Existing blog, product, location, and service migration checks pass. The all-page check covers headings, duplicate IDs, JSON schema, preview noindex, local links, and assets.
- An additional pass found no broken local cross-page fragments. 105 structured-data blocks parse successfully.
- Customer-copy-guard scanned 54 HTML files: 53 pages plus the map document. It returned zero blocking findings and zero review warnings. This automated result does not replace the contextual review or verify factual claims.
- Desktop browser verification confirmed the revised layered-shades answer. Mobile checks at 390px confirmed the service introduction, New Haven intro, homepage H1 and timing FAQ, and navigation. No horizontal overflow in those views. The contact form's empty-field messages are natural and accurate.
- No design, image, submission endpoint, or production deployment changes were made. The prior audit's reference to a 404 page was corrected: the extra HTML file is the service-area map.

## Imported articles: preserve now, review evidence separately

These are passages needing client confirmation or product-specific sourcing, not a finding that every statement is false. They also account for much of the remaining formulaic tone, including repeated “perfect,” “transform,” “seamless,” broad superlatives, and long geographic lists. Do not bulk rewrite, retitle, consolidate, or redirect these ranking articles without a separately approved plan.

| Article slug | Main review items |
| --- | --- |
| `5-ways-custom-blinds-and-shades-can-transform-your-fort-wayne-home` | Customer-volume and local-project anecdotes; 20% heat-loss claim; resale-value statements. |
| `best-window-blinds-new-construction-homes-huntertown-indiana` | Complete-darkness language; universal smart-home integration; warranty/DIY claims. |
| `blackout-window-treatments-bluffton-homes` | Complete darkness, 95–98% room-darkening numbers, health/sleep promises, 10–15% savings, lifetime support, no subcontractors, and blanket cleaning directions. |
| `cellular-shades-fort-wayne-energy-savings` | Named-town project stories, 10–20% bills/$25–30 savings, payback example, top-down/bottom-up description, comparative performance and window-replacement advice. The inherited meta description also contains “sourounding.” |
| `custom-roller-shades-fort-wayne-open-concept-homes` | Complete elimination of glare/heat, reliable evening privacy, perfect matching, and hundreds-of-projects claim. |
| `energy-efficient-blinds-leo-cedarville-indiana-homes` | 40% heat-loss context, insulation comparisons, openness-to-heat relationship, product availability, and pays-for-itself language. |
| `fort-wayne-window-treatments-guide` | 10–20% savings, resale value, 20-year experience claim, top-down/bottom-up explanation, broad warranties and perfect-fit claims. |
| `motorized-blinds-and-shades-in-fort-wayne` | Customer anecdotes, personal-family statements, 90% repair figure, 10+ year motors, battery life, universal outage/compatibility claims, blackout and cord-safety wording. |
| `motorized-zebra-shades-fort-wayne-light-control` | Full-blackout privacy, universal integration, promised preserved views/privacy, performance claims, and hundreds-of-installations statement. |
| `outdoor-patio-shades-guild-fort-wayne` | Year-round comfort, 98% UV and health-protection claims, pest-free wording, wind/weather protection, waterproof motor generalizations, and climate statistics. |
| `plantation-shutters-for-columbia-city-homes` | Population figure, 45% solar heat, 10–15% utility savings, property value, 30+ year life, near-blackout/noise claims, fixed manufacturing timing, and no-subcontractor/lifetime-support promises. |
| `save-energy-window-treatments-fort-wayne` | 10–20% bill reductions, payback illustration, air-gap elimination, source context for 40% heat-loss claim, and property-value claims. |

## Remaining customer-facing launch work

1. **Connect and test form delivery.** The forms still deliberately prevent submission and report that details were not sent. Empty-field validation works, but no successful lead-delivery path exists. The repair/cleaning selection should also get request-specific confirmation wording when the real delivery flow is implemented.
2. **Verify displayed review numbers.** Preserve the approved badge design, but confirm the Facebook 5.0 rating and refresh the Google rating/count before launch. This pass did not verify a Facebook profile; the Google 36-review count remains in form reassurance, not the hero.
3. **Finish remaining destinations.** About and the original `/contact-ghl` route still point to the original domain. About needs its rebuild, and the legacy contact destination needs a verified form/redirect plan before replacing that site.
4. **Confirm business details and outlying coverage.** Keep the established phone, email, weekday hours, free consultation offer, and Fort Wayne base. Confirm current details, especially visits farther from Fort Wayne. No offices or completed projects were invented for the city pages.
5. **Keep proof factual.** Use real installation photos and confirmed project details when available. The illustrative images should not be represented as David's completed installations.

The local preview includes these edits. Neither GitHub nor Netlify was updated in this pass.
