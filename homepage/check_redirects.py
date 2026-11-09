"""Check the legacy redirects against the URL preservation plan and the old-URL inventory.

seo/2026-09-25/url-preservation-and-redirect-plan.csv holds the original "Proposed 301"
rows. seo/2026-11-09/old-url-inventory.csv lists every old URL found in the live sitemap,
a live crawl, 16 months of Search Console page data and that plan, each with outcome 200
(same URL), 301 (to new_path) or 404 (no equivalent). tests/redirects.test.mjs runs the
same checks in the Netlify build.
"""
from pathlib import Path
from urllib.parse import urlsplit
import csv

from routes import DIST, pages, route_of

ROOT = Path(__file__).resolve().parent
PLAN = ROOT.parent / 'seo' / '2026-09-25' / 'url-preservation-and-redirect-plan.csv'
INVENTORY = ROOT.parent / 'seo' / '2026-11-09' / 'old-url-inventory.csv'


def path(url):
    return urlsplit(url).path.rstrip('/') or '/'


def built(route):
    # Pages are <route>.html, served at /route; older builds used <route>/index.html.
    route = route.strip('/')
    return (DIST / (route + '.html')).exists() or (DIST / route / 'index.html').exists()


plan = {path(r['source_url']): path(r['proposed_target']) for r in csv.DictReader(PLAN.open()) if r['action'] == 'Proposed 301'}
inventory = list(csv.DictReader(INVENTORY.open()))
planned = {r['old_path']: r['new_path'] for r in inventory if r['outcome'] == '301'}
for source, target in plan.items():
    assert planned.get(source) == target, f'{source}: the inventory no longer redirects it to {target} as the plan does'

rules = {}
for line in (DIST / '_redirects').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    source, target, status = line.split()
    assert status == '301', line
    assert source not in rules, f'Duplicate rule for {source}'
    rules[source] = target

assert rules == planned, 'dist/_redirects no longer matches the 301 rows of seo/2026-11-09/old-url-inventory.csv'
indexable = {route_of(p) for p in pages()}
for source, target in rules.items():
    # Netlify serves an existing file instead of a non-forced rule.
    assert not built(source), f'{source} is a built page, so its redirect would never fire'
    assert target != '/', f'{source} redirects to the homepage (a soft 404)'
    assert target not in rules, f'{source} chains through {target}'
    assert target in indexable, f'{source} points at {target}, which is not a built, indexable page'

for row in inventory:
    if row['outcome'] == '200':
        assert built(row['old_path']) or row['old_path'] == '/', f"{row['old_path']} should be served at the same URL"
    if row['outcome'] == '404':
        assert not built(row['old_path']) and row['old_path'] not in rules, f"{row['old_path']} is listed as an intentional 404"

counts = {k: sum(r['outcome'] == k for r in inventory) for k in ('200', '301', '404')}
print(f"{len(inventory)} old URLs: {counts['200']} kept, {counts['301']} redirected in one hop to built pages, {counts['404']} intentional 404s.")
