# Beautiful Blinds & Shades

Homepage rebuild for Beautiful Blinds & Shades in Fort Wayne, Indiana.

The website is plain HTML, CSS, and JavaScript. No build step is required.

## Preview locally

```sh
python3 -m http.server 4317 --bind 127.0.0.1 --directory homepage/dist
```

Open http://127.0.0.1:4317/.

Website files are in `homepage/dist/`. See `homepage/README.md` for implementation details and `homepage/SEO_NOTES.md` for the URL preservation plan and SEO launch requirements.

This is a design review build. Search indexing is disabled, and the consultation form validates locally but does not send leads. Connect and verify the client's lead-delivery endpoint and complete the SEO launch checklist before production deployment.
