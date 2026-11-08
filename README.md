# Beautiful Blinds & Shades

Website rebuild for Beautiful Blinds & Shades in Fort Wayne, Indiana.

Full-site SEO research and page-writing plan: [September 25 audit](seo/2026-09-25/README.md). Read the relevant page brief before building additional pages.

The website is plain HTML, CSS, and JavaScript. The committed output can be served directly. After editing interior-page templates or shared homepage components, regenerate them with `python3 homepage/build_pages.py`.

## Preview locally

```sh
python3 homepage/serve.py
```

Open http://127.0.0.1:4317/.

Website files are in `homepage/dist/`. See `homepage/README.md` for implementation details and `homepage/SEO_NOTES.md` for the URL preservation plan and SEO launch requirements.

## Netlify preview

The `beautifulblindshadescom` Netlify project deploys from this repository's `main` branch. `netlify.toml` sets the publish directory to `homepage/dist`; no build command is needed.

Preview URL: https://beautifulblindshadescom.netlify.app/

## Search indexing

The committed pages are indexable. `netlify/edge-functions/search-block.js` sends `X-Robots-Tag: noindex, nofollow` and a disallow-all `robots.txt` on every host except `www.beautifulblindsandshades.com`, so the netlify.app address and deploy previews stay out of Google, and attaching the real domain at launch needs no code change. The 404 page keeps its own `noindex`.

## Carried over from the live site (2026-11-06)

The live Webflow site got an SEO pass on 2026-10-24 after these pages were drafted. `python3 homepage/fetch_live_metadata.py` snapshots every live title, meta description and service schema into `homepage/live-metadata.json`, which `build_pages.py` applies to all pages (Hicksville keeps the rebuild's "Ohio" title). Where a live title equals the page's H1 (the 17 town pages), the H1 keeps it and `distinct_title()` in `homepage/routes.py` gives the `<title>` the brand suffix instead (Semrush's "title duplicates the H1" warning); `tests/search-block.test.mjs` fails the build if any page's title matches its H1. Rerun it, then `python3 homepage/build_pages.py`, if the live site changes again before launch. Also carried over: Service schema on service, product and town pages; the live Auburn additions; GTM-KHJ3F2F5 and GA4 on the production host; `llms.txt`.

## Lead form

The homepage and Contact consultation forms post to `/api/consultation` (`netlify/functions/consultation.mjs`, logic in `netlify/lib/consultation.mjs`). It upserts the contact into Beautiful Blinds & Shades' GoHighLevel, then adds the tag `website lead` (the trigger of GHL's "Form Submission bbs" workflow; `google_landing_page` is for the go. landing page only), plus `sms-transactional-opt-in` when the optional, unticked text-message box was ticked, then a note with the page, treatment, project text and a dated text-message choice. The browser shows the thank-you card and sends one GA4 `generate_lead` only after the lead is confirmed and tagged. GA4 (G-TBE6JC5ZYG) loads on www.beautifulblindsandshades.com only.

Netlify environment variables (never committed): `GHL_PRIVATE_TOKEN` (a BBS private integration with contacts write access, secret) and `GHL_LOCATION_ID`. Functions read them at deploy time, so redeploy after changing them. `node --test tests/*.test.mjs` runs the tests; Netlify runs them as the build command.

The text-message consent links to `/privacy-policy` and `/terms-of-service`, copied from the live site by `python3 homepage/fetch_legal_pages.py` into `homepage/pages/legal/`. Rerun it, then `python3 homepage/build_pages.py`, whenever the live wording changes.
