"""Guard original routes/metadata, local discovery, and detail-page boundaries."""
from html import unescape
from urllib.parse import urlsplit
import json
import re
from build_subproducts import PAGES, BASELINE, LIVE, ROUTES
from routes import page_file, pages

assert len(PAGES)==13 and len(ROUTES)==13
for page in PAGES.values():
    source=next(s for s in BASELINE if s['url']==page['url'])
    raw=page_file(page['path']).read_text()
    title=unescape(re.search(r'<title>(.*?)</title>',raw)[1])
    assert title==source['title'],(page['key'],'original title changed')
    assert f'rel="canonical" href="{source["url"]}"' in raw,(page['key'],'canonical mismatch')
    h1=unescape(re.sub('<[^>]+>','',re.search(r'<h1[^>]*>(.*?)</h1>',raw,re.S)[1]))
    assert h1==page['h1'],(page['key'],'unexpected H1')
    assert sum(1 for _ in re.finditer('<h1\\b',raw))==1
    main=raw.split('<main id="main">')[1].split('</main>')[0]
    assert not re.search(r'<(?:video|iframe)\b|hero-badges|Buy 2 Get 1',main,re.I)
    assert '—' not in main,(page['key'],'new em dash')
    parent=page_file('/products/'+page['group']).read_text()
    assert f'href="{page["path"]}"' in parent,(page['key'],'not linked from parent')
    assert 'href="/contact"' in main and 'href="/products/'+page['group']+'"' in main
    print('Preserved URL/title, H1, category discovery:',page['key'])
for file in pages():
    raw=file.read_text()
    for href in re.findall(r'<a\b[^>]*\shref="([^"]+)"',raw):
        u=urlsplit(unescape(href))
        if u.netloc=='www.beautifulblindsandshades.com' and u.path.rstrip('/') in ROUTES:
            raise AssertionError((file,href,'migrated destination still remote'))
print('All 13 detail pages and migrated internal destinations passed.')
