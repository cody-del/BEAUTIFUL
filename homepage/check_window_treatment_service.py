"""Preserve the original service metadata and keep local service discovery intact."""
from pathlib import Path
from html import unescape
import json
import re
from routes import page_file, pages

ROOT = Path(__file__).resolve().parent
source = json.loads((ROOT / 'pages/window-treatments-source.json').read_text())
raw = page_file('/services/window-treatments').read_text()
assert unescape(re.search(r'<title>(.*?)</title>', raw)[1]) == source['title']
assert unescape(re.search(r'<meta name="description" content="([^"]+)"', raw)[1]) == source['description']
assert f'rel="canonical" href="{source["url"]}"' in raw
h1 = re.findall(r'<h1\b[^>]*>(.*?)</h1>', raw, re.S)
assert len(h1) == 1
assert ' '.join(re.sub('<[^>]+>', ' ', h1[0]).split()) == source['headings'][0]['text']
main = raw.split('<main id="main">')[1].split('</main>')[0]
assert not re.search(r'<(?:video|iframe)\b|hero-badges|renewable energy|Buy 2 Get 1|—', main, re.I)
for route in ['/contact', '/products/blinds', '/products/shades', '/products/plantation-shutters', '/services/outdoor-shades', '/services/blind-shade-repair', '/services/blind-and-shade-cleaning', '/location/beautiful-blinds-and-shades-service-area']:
    assert f'href="{route}"' in main, route
for file in pages():
    text = file.read_text()
    assert f'href="{source["url"]}"' not in re.sub(r'<link\b[^>]+>', '', text), file
home = (ROOT / 'dist/index.html').read_text()
assert 'href="/services/window-treatments">Our window treatment service</a>' in home
assert '<strong>Window treatments</strong>' in home
print('Window treatment service: original metadata, promoted H1, local discovery, and content boundaries passed.')
