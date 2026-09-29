# Beautiful Blinds & Shades

Website rebuild for Beautiful Blinds & Shades in Fort Wayne, Indiana.

Full-site SEO research and page-writing plan: [September 25 audit](seo/2026-09-25/README.md). Read the relevant page brief before building additional pages.

The website is plain HTML, CSS, and JavaScript. The committed output can be served directly. After editing interior-page templates or shared homepage components, regenerate them with `python3 homepage/build_pages.py`.

## Preview locally

```sh
python3 -m http.server 4317 --bind 127.0.0.1 --directory homepage/dist
```

Open http://127.0.0.1:4317/.

Website files are in `homepage/dist/`. See `homepage/README.md` for implementation details and `homepage/SEO_NOTES.md` for the URL preservation plan and SEO launch requirements.

## Netlify preview

The `beautifulblindshadescom` Netlify project deploys from this repository's `main` branch. `netlify.toml` sets the publish directory to `homepage/dist`; no build command is needed.

Preview URL: https://beautifulblindshadescom.netlify.app/

This is a design review build. Search indexing is disabled, and the consultation form validates locally but does not send leads. Connect and verify the client's lead-delivery endpoint and complete the SEO launch checklist before production deployment.
