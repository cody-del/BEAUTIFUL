"""Map clean URLs to files in dist/ the way Netlify serves them.

Netlify serves dist/products/blinds.html at /products/blinds with a 200 and
301s /products/blinds/ to it. A dist/products/blinds/index.html page does the
opposite: /products/blinds 301s to /products/blinds/. The live site, the
canonicals and the internal links have no trailing slash, so every page is
written as <route>.html.
"""
from pathlib import Path
import re

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


BRAND_SUFFIXES = (' | Beautiful Blinds & Shades', ' | Beautiful Blinds')
TITLE_MAX = 60


def _plain(text):
    return ' '.join(text.split())


def distinct_title(title, h1):
    """The page's <title>, made distinct from its H1 when the two are the same.

    Semrush flags a title that duplicates the H1 (the live town pages use the
    H1 as their title, and live-metadata.json carries that over). The H1
    stays; the title becomes the H1 with ", IN"/", OH" and the site's brand
    suffix, falling back to the shorter brand and then dropping a leading
    "Custom" to stay within TITLE_MAX characters.
    """
    if _plain(title).casefold() != _plain(h1).casefold():
        return title
    short = re.sub(r'(?<=\S) In (?=\S)', ' in ', _plain(h1))
    short = re.sub(r', Indiana$', ', IN', re.sub(r', Ohio$', ', OH', short))
    if 'beautiful blinds' in short.casefold():
        return short + ' | Fort Wayne, IN'
    candidates = [base + brand for base in dict.fromkeys((short, short.removeprefix('Custom '))) for brand in BRAND_SUFFIXES]
    return next((c for c in candidates if len(c) <= TITLE_MAX), short + BRAND_SUFFIXES[-1])


_LIVE_METADATA = None


def live_meta(route, field, fallback):
    """The live site's current title or description for a route (live-metadata.json), else fallback."""
    global _LIVE_METADATA
    if _LIVE_METADATA is None:
        import json
        _LIVE_METADATA = json.loads((Path(__file__).resolve().parent / 'live-metadata.json').read_text())
    return _LIVE_METADATA.get(route, {}).get(field, fallback)
