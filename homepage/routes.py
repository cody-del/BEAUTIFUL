"""Map clean URLs to files in dist/ the way Netlify serves them.

Netlify serves dist/products/blinds.html at /products/blinds with a 200 and
301s /products/blinds/ to it. A dist/products/blinds/index.html page does the
opposite: /products/blinds 301s to /products/blinds/. The live site, the
canonicals and the internal links have no trailing slash, so every page is
written as <route>.html.
"""
from pathlib import Path

DIST = Path(__file__).resolve().parent / 'dist'
LIVE = 'https://www.beautifulblindsandshades.com'
# Served, but not pages to index or list in the sitemap.
UTILITY = {'404.html', 'service-area-map.html'}


def page_file(route):
    route = route.strip('/')
    return DIST / (route + '.html' if route else 'index.html')


def route_of(file):
    route = '/' + file.relative_to(DIST).as_posix().removesuffix('.html')
    return '/' if route == '/index' else route


def pages():
    return sorted(p for p in DIST.rglob('*.html') if p.relative_to(DIST).as_posix() not in UTILITY)


def serves(path):
    """True when Netlify answers this URL path with a file from dist/."""
    target = DIST / path.strip('/')
    return target.is_file() or page_file(path).is_file()
