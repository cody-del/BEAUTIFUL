"""Verify exact imported article text, titles, route coverage, and local links."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
POSTS = json.loads((ROOT/'blogs/content.json').read_text())
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

class Page(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.tags=[];self.stack=[];self.body=[];self.h1=[];self.cards=[];self.scripts=[];self.schema=[];self.title=[]
        self.feed(html)
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs);self.tags.append((tag,attrs))
        if tag not in VOID:self.stack.append((tag,attrs))
    def handle_endtag(self,tag):
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i][0]==tag:
                self.stack=self.stack[:i];break
    def handle_data(self,text):
        if any('article-body' in a.get('class','').split() for t,a in self.stack):self.body.append(text)
        if any(t=='h1' for t,a in self.stack):self.h1.append(text)
        if any(t=='title' for t,a in self.stack):self.title.append(text)

def norm(text):return ' '.join(text.split())
def links(doc):return {a['href'] for t,a in doc.tags if t=='a' and 'href' in a}

home=Page((DIST/'index.html').read_text());index=Page((DIST/'blogs/index.html').read_text())
for p in POSTS:
    assert hashlib.sha256(p['source_html'].encode()).hexdigest()==p['source_sha256'],p['slug']
    route='/blog-post/'+p['slug']
    assert route in links(home) and route in links(index),(route,'not discoverable')
    doc=Page((DIST/route.strip('/')/'index.html').read_text())
    assert norm(''.join(doc.body))==p['source_text'],(route,'article wording changed')
    assert norm(''.join(doc.h1))==p['title'],(route,'H1 changed')
    assert norm(''.join(doc.title))==p['title'],(route,'title mismatch')
    canonical=next(a['href'] for t,a in doc.tags if t=='link' and a.get('rel')=='canonical')
    assert canonical==p['url'],(route,'canonical changed')
    print('Exact article text and title:',p['slug'])

for file in DIST.rglob('index.html'):
    raw=file.read_text();doc=Page(raw);ids=[a['id'] for _,a in doc.tags if 'id' in a]
    assert len(ids)==len(set(ids)),(file,'duplicate IDs')
    assert sum(t=='h1' for t,a in doc.tags)==1,(file,'H1 count')
    assert '{{' not in raw,(file,'unresolved template')
    assert any(t=='meta' and a.get('name')=='robots' and 'noindex' in a.get('content','') for t,a in doc.tags),(file,'preview indexable')
    for schema in re.findall(r'<script type="application/ld\+json">(.*?)</script>',raw,re.S):json.loads(schema)
    for tag,a in doc.tags:
        key='href' if tag in ('a','link') else 'src' if tag in ('img','iframe','script') else None
        if not key or key not in a:continue
        u=urlsplit(a[key])
        if u.scheme or u.netloc:continue
        target=DIST/unquote(u.path.lstrip('/')) if u.path.startswith('/') else file.parent/unquote(u.path)
        if u.path:assert target.exists(),(file,a[key],'missing local target')
        if not u.path and u.fragment:assert u.fragment in ids,(file,a[key],'missing section')
print('All',len(list(DIST.rglob('index.html'))),'pages: headings, IDs, schema, noindex, links, and assets passed.')
