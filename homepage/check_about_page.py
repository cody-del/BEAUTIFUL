"""Preserve the original About metadata and David's own biography, and keep About links local."""
from html import unescape
import re
from build_pages import ABOUT, LIVE
from routes import page_file, pages

# David's words from the live page, split only where the original ran sentences together.
BIO = [
    'My name is David Fear, owner of Beautiful Blinds & Shades of Fort Wayne, Indiana. If you had asked me 20 years ago where my career would lead, I never would’ve guessed it would involve custom window treatments and drapery, but here I am!',
    'I spent my first five years in the industry cleaning and repairing window treatments, and the last five years building a career I’m proud of in sales and installation. I’ve found my place, and I’m here for the long haul.',
    'I see my main role as an educator, helping clients navigate the many options, styles, and price points in the world of window coverings. When I’ve done my job right, it’s incredibly rewarding to see that final install come together and watch a client smile as they enjoy the beauty and functionality of their home.',
]

raw = page_file(ABOUT['route']).read_text()
assert unescape(re.search(r'<title>(.*?)</title>', raw)[1]) == ABOUT['title']
assert unescape(re.search(r'<meta name="description" content="([^"]+)"', raw)[1]) == ABOUT['description']
assert f'rel="canonical" href="{LIVE}{ABOUT["route"]}"' in raw
h1 = re.findall(r'<h1\b[^>]*>(.*?)</h1>', raw, re.S)
assert len(h1) == 1 and unescape(re.sub('<[^>]+>', '', h1[0])) == ABOUT['h1']
main = raw.split('<main id="main">')[1].split('</main>')[0]
paragraphs = [unescape(p) for p in re.findall(r'<p>(.*?)</p>', main.split('class="about-david-copy"')[1].split('</div>')[0])]
assert paragraphs == BIO, 'David’s biography changed'
assert not re.search(r'<(?:video|iframe)\b|hero-badges|Buy 2 Get 1|—|hundreds|thousands|subcontractor', main, re.I)
for route in ['/contact', '/services/blind-shade-repair', '/services/blind-and-shade-cleaning', '/services/window-treatments', '/location/beautiful-blinds-and-shades-service-area']:
    assert f'href="{route}"' in main, route
for file in pages():
    assert f'href="{LIVE}{ABOUT["route"]}"' not in re.sub(r'<link\b[^>]+>', '', file.read_text()), file
print('About: original metadata, David’s biography, local links, and content boundaries passed.')
