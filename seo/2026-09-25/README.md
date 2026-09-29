# Beautiful Blinds & Shades: SEO audit and rebuild plan

Prepared September 25, 2026. Research and planning only. No live content, URLs, redirects, DNS, Netlify deployment, or Semrush settings were changed.

## Start here

1. [Findings and recommendations](AUDIT.md): what matters most, existing rankings, content defects, overlap decisions and research limits.
2. [Page-by-page writing briefs](PAGE-BRIEFS.md): a brief for each of the 55 discovered live pages, with an assigned intent, findings, outline, links and evidence needed before writing.
3. [Migration and measurement checklist](MIGRATION-CHECKLIST.md): requirements before the design replaces the current website.
4. [Page inventory and content map](page-inventory-and-content-map.csv): sortable current metadata, technical findings, ranking evidence and proposed work for every page.
5. [URL preservation and redirect plan](url-preservation-and-redirect-plan.csv): all 122 checked URLs, including 55 proposed legacy redirects. Planning only, not an executable redirect file.

## Supporting evidence

- [Current keyword/URL observations](keyword-url-evidence.csv): all 501 returned rows, including observation timestamps.
- [Semrush page metrics](semrush-page-metrics.csv): the separate page-level report; estimates, not analytics.
- [Keyword overlap review](keyword-overlap-review.csv): 15 queries with more than one URL in the returned data. Overlap does not establish harmful cannibalization.
- [Historical keyword observations](historical-keyword-evidence.csv) and [historical top-10 watchlist](historical-top10-watchlist.csv).
- [Keyword demand](keyword-demand.csv): a targeted 20-phrase request returned 12 rows; missing rows are unknown, and zero estimates do not mean no demand.
- [Backlink URL evidence](backlink-url-evidence.csv): reported link counts and last-seen dates.
- [Broken internal link](broken-internal-links.csv).
- [Claims requiring verification](claims-to-verify.csv): 111 automatically flagged passages for editorial review. These are not all proven false.

Raw source HTML, extracted text, the crawl script, the live sitemap/robots file and complete Semrush responses are saved in `homepage/research/audit-2026-09-25/`. That directory is intentionally excluded from Git. These reports live outside `homepage/dist`, so they are not published with the website.

For the next page build, read its entry in PAGE-BRIEFS.md, preserve its existing URL, and use the inventory's current title, description and ranking evidence as the baseline. Do not treat proposed titles as already approved changes.
