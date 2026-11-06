"""Copy the live site's Privacy Policy and Terms of Service into pages/legal/.

The consultation form's text-message consent links to both, so the rebuild
serves them on its own pages. The wording is owned by the live site: run this
whenever it changes there, then python3 homepage/build_pages.py, and commit.
The build never fetches, so a live-site outage can't break it.

Run: python3 homepage/fetch_legal_pages.py
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
LIVE = 'https://www.beautifulblindsandshades.com'
PAGES = ['privacy-policy', 'terms-of-service']
# Everything the live legal pages use. Anything else (a script, a form, an
# image) stops the copy rather than being carried over blind.
KEEP = {'a', 'br', 'h1', 'h2', 'h3', 'li', 'p', 'section', 'strong', 'ul'}
DROP = {'div', 'span', 'main'}


class Legal(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.depth = 0  # inside <main>
        self.out = []

    def handle_starttag(self, tag, attrs):
        if tag == 'main':
            self.depth += 1
            return
        if not self.depth or tag in DROP:
            return
        if tag not in KEEP:
            raise SystemExit(f'Unexpected <{tag}> in the live legal page')
        if tag == 'br':
            self.out.append('<br>')
        elif tag == 'a':
            href = dict(attrs).get('href')
            if not href:
                raise SystemExit('Link without an address')
            extra = ' target="_blank" rel="noopener"' if href.startswith('http') else ''
            self.out.append(f'<a href="{href}"{extra}>')
        else:
            self.out.append(f'<{tag}>')

    def handle_endtag(self, tag):
        if tag == 'main':
            self.depth -= 1
        elif self.depth and tag in KEEP and tag != 'br':
            self.out.append(f'</{tag}>' + ('\n' if tag in {'h1', 'h2', 'h3', 'p', 'section', 'ul'} else ''))

    def handle_data(self, data):
        if self.depth:
            self.out.append(data)

    def handle_entityref(self, name):
        if self.depth:
            self.out.append(f'&{name};')

    def handle_charref(self, name):
        if self.depth:
            self.out.append(f'&#{name};')


def legal_content(html):
    parser = Legal()
    parser.feed(html)
    content = ''.join(parser.out).replace('<!-- -->', '').strip() + '\n'
    if '<h1>' not in content:
        raise SystemExit('No <h1> found in the live legal page')
    return content


if __name__ == '__main__':
    (ROOT / 'pages' / 'legal').mkdir(exist_ok=True)
    for slug in PAGES:
        with urlopen(Request(f'{LIVE}/{slug}', headers={'User-Agent': 'beautiful-blinds-rebuild'}), timeout=20) as response:
            html = response.read().decode('utf-8')
        out = ROOT / 'pages' / 'legal' / f'{slug}.html'
        out.write_text(legal_content(html))
        print('Wrote', out.relative_to(ROOT), 'from', f'{LIVE}/{slug}')
