"""Snapshot the live site's titles, meta descriptions and service schema into live-metadata.json.

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


def absolute(url):
    return LIVE + url if isinstance(url, str) and url.startswith('/') else url


def service(blocks):
    """The live page's Service name, type and offer catalog, wherever its JSON-LD keeps them."""
    for block in blocks:
        for node in (block, block.get('about')):
            if not isinstance(node, dict):
                continue
            if node.get('@type') != 'Service' and 'hasOfferCatalog' not in node:
                continue
            found = {}
            if node.get('@type') == 'Service':
                found['name'] = node['name'].strip()
                kind = node.get('serviceType')
                found['serviceType'] = kind if isinstance(kind, str) else found['name']
            catalog = node.get('hasOfferCatalog')
            if catalog:
                items = []
                for offer in catalog.get('itemListElement', []):
                    item = offer.get('itemOffered', {})
                    entry = {'name': item['name'].strip(), 'description': item.get('description', '').strip()}
                    if item.get('url'):
                        entry['url'] = absolute(item['url'])
                    items.append(entry)
                found['catalog'] = {'name': catalog.get('name', 'Services'), 'items': items}
            return found
    return None


def metadata(route):
    html = get(LIVE + route)
    head = html[:html.index('</head>')]
    title = unescape(re.search(r'<title>(.*?)</title>', head, re.S)[1]).strip()
    description = unescape(re.search(r'<meta content="([^"]*)" name="description"|<meta name="description" content="([^"]*)"', head)[0].split('"')[1]).strip()
    data = {'title': title, 'description': description}
    blocks = []
    for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            blocks.append(json.loads(raw))
        except json.JSONDecodeError:
            pass
    # Blog posts all say they are "about" Outdoor Shades (a live template slip), so none is kept.
    if not route.startswith('/blog-post/') and (found := service(blocks)):
        data['service'] = found
    return route, data


if __name__ == '__main__':
    routes = sorted({re.sub(r'^' + re.escape(LIVE), '', u) or '/' for u in re.findall(r'<loc>([^<]+)</loc>', get(LIVE + '/sitemap.xml'))})
    with ThreadPoolExecutor(8) as pool:
        data = dict(pool.map(metadata, routes))
    for route, fields in KEEP_REBUILD.items():
        for field in fields:
            data[route].pop(field, None)
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    print('Wrote', OUT.name, len(data), 'routes')
