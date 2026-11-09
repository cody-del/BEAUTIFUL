"""Snapshot the live site's long-form page text into pages/live-articles/.

The live Webflow product-detail and town pages carry 1,000-2,500 words of
article text (the detail articles were written on 2026-10-24); the rebuild's
templates carry about 600-1,100. Launching without that text would cut what
Google ranks those pages on, so build_pages.py adds each snapshot to its page
as an "A closer look" section.

What is kept is the live wording, cleaned up:
- sentences shared word for word with another page (templated boilerplate) are dropped,
- so are "What <town> Customers Say" sections (no real reviews, only claims), prices, unconfirmed business claims (family-owned, years in business,
  warranties, Buy 2 Get 1) and the factual slips the location checks already ban,
- town pages drop any paragraph naming a different town (Fort Wayne aside), and Hicksville is Ohio,
- headings start at H2 and never repeat one the page already has, links point at this site's
  own routes, em dashes become commas.

Rerun this, then python3 homepage/build_pages.py, only if the live text changes.
The build never fetches, so a live-site outage can't break it.

Run: python3 homepage/fetch_live_articles.py
"""
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from html import escape, unescape
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

from routes import serves

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'pages' / 'live-articles'
LIVE = 'https://www.beautifulblindsandshades.com'
PREFIXES = ('/custom-blinds-fort-wayne-indiana/', '/custom-shades-fort-wayne-indiana/',
            '/custom-interior-plantation-shutters-fort-wayne-indiana/', '/beautiful-blinds-shades-service-areas/')
EXTRA = ['/products/plantation-shutters']
TOWNS = ['Harlan', 'Huntertown', 'Columbia City', 'Angola', 'Auburn', 'Bluffton', 'Grabill', 'Hicksville', 'Hoagland',
         'Kendallville', 'Leo-Cedarville', 'Monroeville', 'New Haven', 'Syracuse', 'Warsaw', 'Woodburn']
# Prices, unconfirmed claims, and the slips check_location_migration.py already bans.
BANNED = re.compile(r'\$\s?\d|\bbuy (?:2|two)\b|family[- ]owned|\bfor (?:many |several )?years\b|\b\d+\+?\s+years\b|years of experience|decades? of|warrant(?:y|ies)'
                    r'|published contact hours|mid-america science park|bluffton university|southeast of fort wayne along route 24'
                    r'|southwestern allen county|savings often equal or exceed|exceeds? the initial cost|we.ve installed countless|twice the insulating power', re.I)
KEEP = {'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'strong', 'em', 'a', 'br', 'blockquote'}
RENAME = {'h1': 'h2', 'h5': 'h4', 'h6': 'h4', 'b': 'strong', 'i': 'em'}


def get(url):
    with urlopen(Request(url, headers={'User-Agent': 'beautiful-blinds-rebuild'}), timeout=25) as response:
        return response.read().decode('utf-8')


class RichText(HTMLParser):
    """Rebuild the page's w-richtext blocks with only the allowed tags and no attributes but href."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.stack = []
        self.out = []

    def handle_starttag(self, tag, attrs):
        if not self.depth:
            if 'w-richtext' in (dict(attrs).get('class') or ''):
                self.depth = 1
            return
        if tag in {'br', 'img', 'hr', 'input'}:
            if tag == 'br':
                self.out.append('<br>')
            return
        self.depth += 1
        tag = RENAME.get(tag, tag)
        self.stack.append(tag if tag in KEEP else None)
        if tag == 'a':
            href = link(dict(attrs).get('href') or '')
            self.stack[-1] = 'a' if href else None
            if href:
                extra = ' rel="noopener"' if href.startswith('http') else ''
                self.out.append(f'<a href="{escape(href, quote=True)}"{extra}>')
        elif tag in KEEP:
            self.out.append(f'<{tag}>')

    def handle_endtag(self, tag):
        if not self.depth or tag in {'br', 'img', 'hr', 'input'}:
            return
        self.depth -= 1
        if self.depth == 0:
            return
        kept = self.stack.pop() if self.stack else None
        if kept:
            self.out.append(f'</{kept}>')

    def handle_data(self, data):
        if self.depth:
            self.out.append(escape(data, quote=False))


def link(href):
    """Live links become this site's own routes; anything that would not resolve is unlinked."""
    if href.startswith(('mailto:', 'tel:')):
        return href.replace('tel:(260)222-6467', 'tel:+12602226467')
    url = urlsplit(href)
    if url.netloc and url.netloc not in {'www.beautifulblindsandshades.com', 'beautifulblindsandshades.com'}:
        return href if url.scheme == 'https' else None
    path = url.path.rstrip('/') or '/'
    return path if serves(path) else None


def text(html):
    return ' '.join(unescape(re.sub(r'<[^>]+>', ' ', html)).split())


TOWN_NAMES = re.compile(r'\b(?:' + '|'.join(re.escape(t.lower().replace('-', ' ')) for t in TOWNS + ['Fort Wayne']) + r')\b')


def key(fragment, town=None):
    """Compare text with every town name masked, so templated copy counts as shared whichever town it names."""
    t = re.sub(r'\W+', ' ', text(fragment).lower())
    return TOWN_NAMES.sub('TOWN', t).strip()


def built_text(route):
    """The rebuild page's own text, so the live article never repeats it."""
    from routes import page_file
    page = page_file(route)
    if not page.exists():
        return ''
    html = page.read_text()
    main = html.split('<main id="main">')[1].split('</main>')[0] if '<main id="main">' in html else html
    main = re.sub(r'<section class="section live-article".*?</section>', '', main, flags=re.S)
    return TOWN_NAMES.sub('TOWN', re.sub(r'\W+', ' ', text(main).lower()))


def built_headings(route):
    """Headings the rebuild page already shows, so the live article never repeats one."""
    from routes import page_file
    page = page_file(route)
    if not page.exists():
        return set()
    html = re.sub(r'<section class="section live-article".*?</section>', '', page.read_text(), flags=re.S)
    return {re.sub(r'\W+', ' ', text(h).lower()).strip() for h in re.findall(r'<h[1-6]\b[^>]*>(.*?)</h[1-6]>', html, re.S)}


def blocks(html):
    return re.findall(r'<(h2|h3|h4|p|ul|ol|blockquote)>(.*?)</\1>', html, re.S)


def town_of(route):
    for town in TOWNS + ['Fort Wayne']:
        if town.lower().replace(' ', '-') in route:
            return town
    return None


def clean(route, html, shared):
    town = town_of(route) if route.startswith('/beautiful-blinds-shades-service-areas/') else None
    others = [t for t in TOWNS if t != town]
    already = built_text(route)
    headings = built_headings(route)

    def keep(fragment):
        plain = text(fragment)
        if len(plain.split()) < 4 or BANNED.search(plain):
            return False
        if shared[key(fragment)] > 1 or key(fragment) in already:
            return False
        # Naming a neighbouring town is how copied town pages show; keep each page about its own town.
        if town and any(re.search(rf'\b{re.escape(o)}\b', plain) for o in others):
            return False
        return True

    out = []
    for tag, inner in blocks(html):
        if tag in {'ul', 'ol'}:
            items = [i for i in re.findall(r'<li>(.*?)</li>', inner, re.S) if keep(i)]
            if items:
                out.append((tag, ''.join(f'<li>{i}</li>' for i in items)))
        elif tag.startswith('h'):
            heading = text(inner)
            repeated = re.sub(r'\W+', ' ', heading.lower()).strip() in headings
            if not repeated and not BANNED.search(heading) and not (town and any(re.search(rf'\b{re.escape(o)}\b', heading) for o in others)):
                out.append((tag, inner))
        elif keep(inner):
            out.append((tag, inner))
    # Drop "What <town> Customers Say" sections: no real reviews, only unverifiable claims
    # about the business. Everything under the heading goes, up to the next heading of its level.
    level = {'h2': 2, 'h3': 3, 'h4': 4}
    trimmed, skip_to = [], None
    for tag, inner in out:
        if skip_to is not None:
            if tag in level and level[tag] <= skip_to:
                skip_to = None
            else:
                continue
        if tag in level and re.search(r'customers say|testimonial', text(inner), re.I):
            skip_to = level[tag]
            continue
        trimmed.append((tag, inner))
    # A heading the article already used once is dropped; its text stays under the earlier one.
    seen, out = set(), []
    for tag, inner in trimmed:
        if tag in level:
            norm = re.sub(r'\W+', ' ', text(inner).lower()).strip()
            if norm in seen:
                continue
            seen.add(norm)
        out.append((tag, inner))
    # Drop headings left without any text under them.
    kept = []
    for i, (tag, inner) in enumerate(out):
        if tag in level:
            nxt = out[i + 1][0] if i + 1 < len(out) else None
            if nxt is None or (nxt in level and level[nxt] <= level[tag]):
                continue
        kept.append((tag, inner))
    html = '\n'.join(f'<{t}>{inner.strip()}</{t}>' for t, inner in kept)
    html = re.sub(r'\s*—\s*', ', ', html)
    if town == 'Hicksville':
        html = re.sub(r'Hicksville,? Indiana', 'Hicksville, Ohio', html)
    return html + '\n' if kept else ''


if __name__ == '__main__':
    routes = sorted(set(re.sub(r'^' + re.escape(LIVE), '', u) for u in re.findall(r'<loc>([^<]+)</loc>', get(LIVE + '/sitemap.xml'))))
    routes = [r for r in routes if r.startswith(PREFIXES)] + EXTRA

    def fetch(route):
        parser = RichText()
        parser.feed(get(LIVE + route))
        return route, ''.join(parser.out)

    with ThreadPoolExecutor(8) as pool:
        raw = dict(pool.map(fetch, routes))
    shared = Counter()
    for route, html in raw.items():
        town = town_of(route) if route.startswith('/beautiful-blinds-shades-service-areas/') else None
        fragments = [inner for tag, inner in blocks(html) if tag not in {'ul', 'ol'}]
        fragments += [li for tag, inner in blocks(html) if tag in {'ul', 'ol'} for li in re.findall(r'<li>(.*?)</li>', inner, re.S)]
        for k in {key(f) for f in fragments}:
            shared[k] += 1
    OUT.mkdir(parents=True, exist_ok=True)
    for route, html in raw.items():
        article = clean(route, html, shared)
        target = OUT / (route.strip('/').replace('/', '__') + '.html')
        # A few leftover sentences are not worth a section of their own.
        if len(text(article).split()) >= 150:
            target.write_text(article)
        elif target.exists():
            target.unlink()
        print(f'{len(text(article).split()):5} words  {route}')
