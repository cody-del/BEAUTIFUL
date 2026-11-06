"""Snapshot the live site's titles and meta descriptions into live-metadata.json.

The live Webflow site got an SEO pass on 2026-10-24 (titles, descriptions)
after this rebuild was drafted. build_pages.py applies these values to every
generated page so the launch doesn't undo that work. Rerun this, then
python3 homepage/build_pages.py, if the live metadata changes again before launch.
The build never fetches, so a live-site outage can't break it.

Run: python3 homepage/fetch_live_metadata.py
"""
from concurrent.futures import ThreadPoolExecutor
from html import unescape
from pathlib import Path
import json
import re
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
LIVE = 'https://www.beautifulblindsandshades.com'
OUT = ROOT / 'live-metadata.json'
# Kept from the rebuild on purpose: Hicksville is in Ohio, whatever the live URL says.
KEEP_REBUILD = {'/beautiful-blinds-shades-service-areas/window-treatments-hicksville-indiana': {'title'}}


def get(url):
    with urlopen(Request(url, headers={'User-Agent': 'beautiful-blinds-rebuild'}), timeout=20) as response:
        return response.read().decode('utf-8')


def metadata(route):
    html = get(LIVE + route)
    head = html[:html.index('</head>')]
    title = unescape(re.search(r'<title>(.*?)</title>', head, re.S)[1]).strip()
    description = unescape(re.search(r'<meta content="([^"]*)" name="description"|<meta name="description" content="([^"]*)"', head)[0].split('"')[1]).strip()
    return route, {'title': title, 'description': description}


if __name__ == '__main__':
    routes = sorted({re.sub(r'^' + re.escape(LIVE), '', u) or '/' for u in re.findall(r'<loc>([^<]+)</loc>', get(LIVE + '/sitemap.xml'))})
    with ThreadPoolExecutor(8) as pool:
        data = dict(pool.map(metadata, routes))
    for route, fields in KEEP_REBUILD.items():
        for field in fields:
            data[route].pop(field, None)
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    print('Wrote', OUT.name, len(data), 'routes')
