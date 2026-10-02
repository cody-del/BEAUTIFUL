# Customer-facing copy review

Reviewed October 1, 2026 using the customer-copy-guard skill after the final nine city pages were built.

## Scope

Contextual reading of all nine new city templates: Columbia City, Bluffton, Grabill, Woodburn, Harlan, Hoagland, Angola, Kendallville, and Syracuse. Reviewed their headings, body copy, FAQs, actions, image descriptions, original titles/descriptions, and generated WebPage text. Shared navigation and footer labels were inspected in the rendered preview.

The automated checker separately scanned all 54 HTML files in `homepage/dist` (53 index pages plus the service-area map document). That wider scan is not a full manual editorial review of every existing page. The original live website and Netlify deployment were not edited.

## Findings and edits

No exposed SEO strategy, writer instructions, AI self-reference, or unfinished placeholders were found in the nine new pages. The automated scan returned zero blocking findings and zero review warnings.

Twenty small edits across the nine city pages simplify jargon and awkward phrasing. Examples:

- Columbia City: “during the in-home process” becomes “during your home visit.”
- Hoagland: “can offer grouped operation” becomes “lets you adjust several shades together.”
- Syracuse: “conditioned year-round” becomes “heat and cool the room year-round.”
- Kendallville: “compare … the control with your reach” becomes “choose controls you can reach comfortably.”
- Harlan: “outside normal call hours” becomes the direct question “Can I arrange an evening or weekend visit?” The answer still makes availability conditional.

The exact before/after record is in `customer-copy-edits.json`. These are clarity edits, not corrections to exposed internal instructions. Original URLs, titles, descriptions, H1s, link destinations, heading order, product topics, and useful qualifications are retained. Two secondary headings were made more natural. No blog article wording was changed.

## Verification

Rebuilt the static pages. Location preservation checks and all-page headings, IDs, schema, noindex, links, and assets passed. All 12 original blog texts and titles remain exact. Build-currentness and whitespace checks passed. The rendered Columbia City copy was checked in the browser.

These edits are local. No deployment or publication gate was added by this review. The skill's automated scan supplements contextual review and does not guarantee detection of every unsuitable sentence.
