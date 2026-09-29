"""Check preserved location metadata and complete city discovery."""
from pathlib import Path
from html import unescape
from urllib.parse import urlsplit
import re
from build_locations import BASELINE, CITIES, LIVE, ROUTES, HUB

DIST = Path(__file__).resolve().parent / 'dist'

def plain(value):
    return ' '.join(unescape(re.sub('<[^>]+>', ' ', value)).split())

for key, source in BASELINE.items():
    raw = (DIST / source['url'].removeprefix(LIVE).strip('/') / 'index.html').read_text()
    expected_title = source['title'].replace('Indiana', 'Ohio') if key == 'hicksville' else source['title']
    assert unescape(re.search(r'<title>(.*?)</title>', raw)[1]) == expected_title
    assert unescape(re.search(r'<meta name="description" content="([^"]*)"', raw)[1]) == source['description']
    assert f'rel="canonical" href="{source["url"]}"' in raw
    headings = re.findall(r'<h1\b[^>]*>(.*?)</h1>', raw, re.S)
    expected = 'Serving Fort Wayne & Northeast Indiana' if key == 'service-area' else expected_title
    assert len(headings) == 1 and plain(headings[0]) == expected
    main = raw.split('<main id="main">')[1].split('</main>')[0]
    assert not re.search(r'<video\b|hero-badges|Buy 2 Get 1|—', main, re.I)
    assert 'href="/contact"' in main
    if key != 'service-area':
        assert '<iframe' not in main
        assert f'href="{HUB}"' in main
        if key == 'monroeville':
            assert 'Woodburn' not in plain(main), 'Copied Woodburn content returned'
        if key == 'warsaw':
            assert 'Bluffton' not in plain(main), 'Copied Bluffton content returned'
        if key == 'hicksville':
            assert 'Hicksville, Indiana' not in plain(main), 'Incorrect state in visible text'
            assert 'Hicksville, Ohio' in plain(main)
    else:
        groups = re.findall(r'<details class="coverage-group"[^>]*>.*?</details>', main, re.S)
        assert len(groups) == 3 and all(' open' not in g.split('>')[0] for g in groups)
        actual = [urlsplit(unescape(u)).path.rstrip('/') for u in re.findall(r'href="([^"]+)"', ''.join(groups))]
        expected_paths = [urlsplit(c['url']).path.rstrip('/') for c in CITIES]
        assert len(actual) == 17 and sorted(actual) == sorted(expected_paths)
    print('Preserved location metadata and content boundaries:', key)

for file in DIST.rglob('index.html'):
    for href in re.findall(r'<a\b[^>]*\shref="([^"]+)"', file.read_text()):
        u = urlsplit(unescape(href))
        assert not (u.netloc == urlsplit(LIVE).netloc and u.path.rstrip('/') in ROUTES), (file, href)
print(f'All {len(BASELINE)} location routes and all 17 city-directory links passed.')
