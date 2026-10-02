"""Check preserved location metadata and complete city discovery."""
from html import unescape
from urllib.parse import urlsplit
import re
from routes import page_file, pages
from build_locations import BASELINE, CITIES, LIVE, ROUTES, HUB

NEW_CITY_TOPICS = {
    'columbia-city': ['cellular', 'solar', 'roman', 'shutters', 'motorized', 'woodwork'],
    'bluffton': ['cellular', 'solar', 'roman', 'shutters', 'motorized', 'blackout'],
    'grabill': ['wood', 'faux wood', 'cellular', 'roller', 'vertical', 'motorized'],
    'woodburn': ['faux wood', 'cellular', 'roman', 'solar', 'shutters'],
    'harlan': ['double-cell', 'wood', 'solar', 'motorized', 'roman'],
    'hoagland': ['blackout', 'cellular', 'wood', 'faux wood', 'solar', 'roller', 'motorized', 'outbuilding'],
    'angola': ['cellular', 'solar', 'roller', 'roman', 'shutters', 'motorized', 'seasonal'],
    'kendallville': ['cellular', 'solar', 'roller', 'roman', 'shutters', 'motorization'],
    'syracuse': ['cellular', 'solar', 'roller', 'roman', 'shutters', 'motorization', 'seasonal'],
}

def plain(value):
    return ' '.join(unescape(re.sub('<[^>]+>', ' ', value)).split())

for key, source in BASELINE.items():
    raw = page_file(source['url'].removeprefix(LIVE)).read_text()
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
        if key in NEW_CITY_TOPICS:
            text = plain(main).lower()
            for topic in NEW_CITY_TOPICS[key] + ['measur', 'installation']:
                assert topic in text, (key, 'missing useful source topic', topic)
            assert 'href="tel:+12602226467"' in main
            for phrase in ['published contact hours', 'mid-america science park', 'bluffton university', 'southeast of fort wayne along route 24', 'southwestern allen county', 'savings often equal or exceed', 'we\'ve installed countless']:
                assert phrase not in text, (key, 'unsuitable source copy returned', phrase)
            if key == 'columbia-city':
                assert 'href="/blog-post/plantation-shutters-for-columbia-city-homes"' in main
            if key == 'bluffton':
                assert 'href="/blog-post/blackout-window-treatments-bluffton-homes"' in main
        if key in {'fort-wayne', 'huntertown', 'leo-cedarville', 'new-haven'}:
            for topic in ['cellular', 'solar', 'motorized', 'shutters', 'measur', 'installation']:
                assert topic in plain(main).lower(), (key, 'missing source topic', topic)
            if key != 'leo-cedarville':
                assert 'Roman shades' in main
            assert 'twice the insulating power' not in main
            assert not re.search(r'The original (?:Huntertown|New Haven|Fort Wayne|Leo-Cedarville) page', main), 'Editorial notes leaked into customer copy'
            if key == 'huntertown':
                assert 'href="/blog-post/best-window-blinds-new-construction-homes-huntertown-indiana"' in main
            if key == 'leo-cedarville':
                assert 'href="/blog-post/energy-efficient-blinds-leo-cedarville-indiana-homes"' in main
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

for file in pages():
    for href in re.findall(r'<a\b[^>]*\shref="([^"]+)"', file.read_text()):
        u = urlsplit(unescape(href))
        assert not (u.netloc == urlsplit(LIVE).netloc and u.path.rstrip('/') in ROUTES), (file, href)
print(f'All {len(BASELINE)} location routes and all 17 city-directory links passed.')
