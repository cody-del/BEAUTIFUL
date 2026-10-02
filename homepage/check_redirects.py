"""Check the legacy redirects against the URL preservation plan."""
from pathlib import Path
from urllib.parse import urlsplit
import csv

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
PLAN = ROOT.parent / 'seo' / '2026-09-25' / 'url-preservation-and-redirect-plan.csv'

def path(url):
    return urlsplit(url).path.rstrip('/') or '/'

def built(route):
    # Pages are <route>.html, served at /route; older builds used <route>/index.html.
    route = route.strip('/')
    return (DIST / (route + '.html')).exists() or (DIST / route / 'index.html').exists()

rows = list(csv.DictReader(PLAN.open()))
planned = {path(r['source_url']): path(r['proposed_target']) for r in rows if r['action'] == 'Proposed 301'}
preserved = {path(r['source_url']) for r in rows if r['action'] == 'Keep URL (200)'}

rules = {}
for line in (DIST / '_redirects').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    source, target, status = line.split()
    assert status == '301', line
    assert source not in rules, f'Duplicate rule for {source}'
    rules[source] = target

assert rules == planned, 'dist/_redirects no longer matches the "Proposed 301" rows of the plan'
for source, target in rules.items():
    # Netlify serves an existing file instead of a non-forced rule.
    assert not built(source), f'{source} is a built page, so its redirect would never fire'
    assert target not in rules, f'{source} chains through {target}'
    assert target in preserved, f'{source} points at {target}, which the plan does not preserve'

waiting = sorted({t for t in rules.values() if not built(t)})
print(f'{len(rules)} legacy redirects match the plan and point at preserved routes.')
if waiting:
    print(f'{len(waiting)} destinations are not built yet and 404 in the preview until they are:')
    for target in waiting:
        print(f'  {target}')
