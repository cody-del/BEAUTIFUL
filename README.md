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

This is a design review build with search indexing disabled. Complete the SEO launch checklist before production deployment.

## Lead form

The homepage and Contact consultation forms post to `/api/consultation` (`netlify/functions/consultation.mjs`, logic in `netlify/lib/consultation.mjs`). It upserts the contact into Beautiful Blinds & Shades' GoHighLevel, then adds the tag `website lead` (the trigger of GHL's "Form Submission bbs" workflow; `google_landing_page` is for the go. landing page only), plus `sms-transactional-opt-in` when the optional, unticked text-message box was ticked, then a note with the page, treatment, project text and a dated text-message choice. The browser shows the thank-you card and sends one GA4 `generate_lead` only after the lead is confirmed and tagged. GA4 (G-TBE6JC5ZYG) loads on www.beautifulblindsandshades.com only.

Netlify environment variables (never committed): `GHL_PRIVATE_TOKEN` (a BBS private integration with contacts write access, secret) and `GHL_LOCATION_ID`. Functions read them at deploy time, so redeploy after changing them. `node --test tests/*.test.mjs` runs the tests; Netlify runs them as the build command.

The text-message consent links to `/privacy-policy` and `/terms-of-service`, copied from the live site by `python3 homepage/fetch_legal_pages.py` into `homepage/pages/legal/`. Rerun it, then `python3 homepage/build_pages.py`, whenever the live wording changes.
