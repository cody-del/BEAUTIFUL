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

## Old URLs and redirects

`seo/2026-11-09/old-url-inventory.csv` lists every URL Google knows on the old site (live sitemap, a live crawl, 16 months of Search Console page data, and the September 25 plan) with its outcome on the new site: 200 at the same URL, a one-hop 301 in `homepage/dist/_redirects` to the closest equivalent page, or an intentional 404 where nothing equivalent exists (never a redirect to the homepage). `tests/redirects.test.mjs`, part of the Netlify build, fails the deploy if a rule chains, lands on a non-sitemap page or the homepage, or an old URL loses its outcome; it also checks self-canonicals and the sitemap. `python3 homepage/check_redirects.py` runs the same redirect checks locally. Google requests `&` and `,` in old paths as `%26` and `%2C`, and Netlify matches rules literally, so those forms have their own rules. http→https and apex→www are left to Netlify's domain settings (www primary), so those variants of an old URL take one extra hop.

## Carried over from the live site (2026-11-06)

The live Webflow site got an SEO pass on 2026-10-24 after these pages were drafted. `python3 homepage/fetch_live_metadata.py` snapshots every live title, meta description and service schema into `homepage/live-metadata.json`, which `build_pages.py` applies to all pages (Hicksville keeps the rebuild's "Ohio" title). Where a live title equals the page's H1 (the 17 town pages), the H1 keeps it and `distinct_title()` in `homepage/routes.py` gives the `<title>` the brand suffix instead (Semrush's "title duplicates the H1" warning); `tests/search-block.test.mjs` fails the build if any page's title matches its H1. Rerun it, then `python3 homepage/build_pages.py`, if the live site changes again before launch. Also carried over: Service schema on service, product and town pages; the live Auburn additions; GTM-KHJ3F2F5 and GA4 on the production host; `llms.txt`.

## Lead form

The homepage and Contact consultation forms post to `/api/consultation` (`netlify/functions/consultation.mjs`, logic in `netlify/lib/consultation.mjs`). It upserts the contact into Beautiful Blinds & Shades' GoHighLevel, then adds the tag `website lead` (the trigger of GHL's "Form Submission bbs" workflow; `google_landing_page` is for the go. landing page only), plus `sms-transactional-opt-in` when the optional, unticked text-message box was ticked, then a note with the page, treatment, project text and a dated text-message choice. The browser shows the thank-you card and sends one GA4 `generate_lead` only after the lead is confirmed and tagged. GA4 (G-TBE6JC5ZYG) loads on www.beautifulblindsandshades.com only.

Netlify environment variables (never committed): `GHL_PRIVATE_TOKEN` (a BBS private integration with contacts write access, secret) and `GHL_LOCATION_ID`. Functions read them at deploy time, so redeploy after changing them. `node --test tests/*.test.mjs` runs the tests; Netlify runs them as the build command.

### Cloudflare Turnstile

`homepage/dist/script.js` adds an invisible Cloudflare Turnstile human check to both consultation forms (home and Contact); visitors only see a checkbox if Cloudflare wants one. `netlify/lib/turnstile.mjs` checks the token in the function before anything reaches GoHighLevel, refuses the lead with a 403 when the token is missing or refused, and never passes the token on. If Cloudflare can't be reached (3-second timeout, HTTP error or a non-JSON answer), the lead goes through rather than being lost. A token older than 270 seconds (Cloudflare honours them for 300) is refreshed before sending.

- Widget: "Beautiful Blinds and Shades lead forms" in the gbp@shadestrategy.com Cloudflare account (Managed mode; also covers the go. landing page).
- Site key: `0x4AAAAAAF6P0O2EGLa-iliA` (public, in `script.js`), used only on `www.beautifulblindsandshades.com` and `beautifulblindsandshades.com`. Every other host, including `beautifulblindshadescom.netlify.app` before launch, deploy previews and localhost, uses Cloudflare's always-pass test key `1x00000000000000000000AA` and needs no secret.
- Secret: the Netlify variable `TURNSTILE_SECRET_KEY` on `beautifulblindshadescom` (Production context, Functions scope, marked secret). Without it the check is off. Functions read it at deploy time, so redeploy after setting it. Until the real domain is attached, the netlify.app production URL sends the test key's token, which the real secret refuses: set the secret only when the site moves to beautifulblindsandshades.com.
- The privacy policy's cookie paragraph mentions Turnstile. That sentence is ours, not the live site's: keep it if `fetch_legal_pages.py` is rerun.

The text-message consent links to `/privacy-policy` and `/terms-of-service`, copied from the live site by `python3 homepage/fetch_legal_pages.py` into `homepage/pages/legal/`. Rerun it, then `python3 homepage/build_pages.py`, whenever the live wording changes.
