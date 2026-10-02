"""Render the 13 existing product-detail URLs with the shared product design."""
from pathlib import Path
from html import escape
import json
import re
from subproducts.editorial import CONTENT
from routes import page_file

ROOT = Path(__file__).resolve().parent
LIVE = 'https://www.beautifulblindsandshades.com'
BASELINE = json.loads((ROOT/'subproducts/source-baseline.json').read_text())
GROUPS = {'blinds':'Blinds', 'shades':'Shades', 'plantation-shutters':'Plantation shutters'}


def sentence_name(name):
    """Keep Roman and Venetian capitalized within a sentence."""
    return name if name.startswith(('Roman ', 'Venetian ')) else name.lower()


PAGES = {}
for key, content in CONTENT.items():
    source = next(p for p in BASELINE if (('/custom-'+key+'-' in p['url']) if key in ('mini','panel-track','venetian','vertical','roller','wood','composite') else ('/'+key+'-' in p['url'])))
    page = {**content, 'key':key, 'url':source['url'], 'path':source['url'].removeprefix(LIVE), 'title':source['title'], 'description':source['description'], 'h1':source['headings'][0]['text']}
    if key == 'roller':
        page['h1'] = page['h1'].replace('Solar','Roller')
    if key == 'pleated':
        page['h1'] = page['h1'].replace('FOrt','Fort')
    if content['group'] == 'shades':
        # The live descriptions reused "sheer shades" for unrelated products.
        page['description'] = f"Custom {sentence_name(content['name'])} in Fort Wayne, Indiana. Compare fabrics, light control, and fitting options. Free in-home consultation with Beautiful Blinds & Shades."
    PAGES[key] = page
ROUTES = {p['path'] for p in PAGES.values()}


def localize(html):
    """Localize only migrated destinations, preserving query strings/fragments."""
    return re.sub(r'(<a\b[^>]*?\s)href="https://www\.beautifulblindsandshades\.com([^"?#]*)([?#][^"]*)?"',
                  lambda m: m[1]+'href="'+m[2]+(m[3] or '')+'"' if m[2].rstrip('/') in ROUTES else m[0], html)


def a(text):
    return escape(text, quote=True)


def render(page, home, shared_paths):
    key=page['key']; group=page['group']; url=page['url']
    head=home[home.index('<head>'):home.index('</head>')+7]
    head=re.sub(r'<title>.*?</title>', '<title>'+a(page['title'])+'</title>',head)
    head=re.sub(r'<meta name="description"[^>]+>', '<meta name="description" content="'+a(page['description'])+'">',head)
    head=re.sub(r'<link rel="canonical"[^>]+>', '<link rel="canonical" href="'+url+'">',head)
    head=head.replace('href="assets/','href="/assets/').replace('/assets/shades-natural-v2.jpg','/assets/'+page['image'])
    head=head.replace('href="styles.css','href="/styles.css').replace('src="script.js','src="/script.js')
    # This page has no homepage guide carousel; keep shared nav and button styles.
    head=re.sub(r'<link rel="stylesheet" href="/blog.css[^>]*>\s*','',head)
    head=re.sub(r'<script src="/guides.js[^>]*></script>\s*','',head)
    crumbs=[('Home',LIVE+'/'),(GROUPS[group],LIVE+'/products/'+group),(page['name'],url)]
    schema={'@context':'https://schema.org','@graph':[
        {'@type':'WebPage','@id':url+'#page','url':url,'name':page['h1'],'description':page['description'],'about':{'@type':'Thing','name':page['name']},'publisher':{'@id':LIVE+'/#business'},'breadcrumb':{'@id':url+'#breadcrumb'}},
        {'@type':'BreadcrumbList','@id':url+'#breadcrumb','itemListElement':[{'@type':'ListItem','position':i+1,'name':n,'item':u} for i,(n,u) in enumerate(crumbs)]}]}
    head=head.replace('</head>','<link rel="stylesheet" href="/category.css?v=20260928-cleanup">\n<link rel="stylesheet" href="/product.css?v=20260928-products">\n<link rel="stylesheet" href="/subproduct.css?v=20260928-detail">\n<script type="application/ld+json">'+json.dumps(schema)+'</script>\n</head>')
    header=shared_paths(home[home.index('  <header class="header">'):home.index('  <main')])
    footer=shared_paths(home[home.index('  <footer class="footer">'):])
    choices=''.join('<article><h3>'+a(t)+'</h3><p>'+a(p)+'</p></article>' for t,p in page['choices'])
    faq=''.join('<details><summary>'+a(q)+'</summary><p>'+a(answer)+'</p></details>' for q,answer in page['faq'])
    cards=''
    for related in page['related']:
        other=PAGES[related]
        cards+=f'<a class="detail-related-item" href="{other["path"]}"><img src="/assets/{other["image"]}" alt="{a(other["alt"])}" width="600" height="400" loading="lazy"><span><strong>{a(other["name"])}</strong><span class="text-link">Explore {a(sentence_name(other["name"]))}</span></span></a>'
    guide=''
    if page['guide']:
        posts=json.loads((ROOT/'blogs/content.json').read_text())
        post=next(p for p in posts if p['slug']==page['guide'])
        guide='<p class="detail-guide">From our guides: <a class="text-link" href="/blog-post/'+post['slug']+'">'+a(post['title'])+'</a></p>'
    # Preserve the source H1 words except the documented roller/pleated errors.
    h1=a(page['h1'])
    h1=re.sub(r' (In |in )?Fort Wayne(,)? Indiana$', lambda m:' <span>'+m[0].strip()+'</span>',h1)
    care_links = '<a class="text-link" href="/contact">Ask about shutter care</a>' if group == 'plantation-shutters' else '<a class="text-link" href="/services/blind-and-shade-cleaning">Cleaning services</a><a class="text-link" href="/services/blind-shade-repair">Repair services</a>'
    content=f'''
<section class="hero category-hero detail-hero" aria-labelledby="hero-title">
<img class="hero-photo" src="/assets/{page['image']}" alt="{a(page['alt'])}" width="1400" height="933" fetchpriority="high">
<div class="container hero-inner"><div class="hero-copy">
<nav class="category-breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/products/{group}">{GROUPS[group]}</a><span aria-hidden="true">/</span><span aria-current="page">{a(page['name'])}</span></nav>
<h1 id="hero-title">{h1}</h1><p class="hero-description">{a(page['intro'])}</p>
<div class="actions"><a class="button" href="tel:+12602226467">Call (260) 222-6467</a><a class="button button-outline" href="/contact">Get a Free Consultation</a></div>
<p class="hero-note">Serving Fort Wayne, Allen County &amp; Northeast Indiana</p>
</div></div></section>
<nav class="detail-jump" aria-label="On this page"><div class="container"><a href="#options">Options &amp; materials</a><a href="#fitting">Fitting &amp; installation</a><a href="#care">Care</a><a href="#questions">Questions</a></div></nav>
<section class="section detail-options" id="options" aria-labelledby="options-title"><div class="container">
<div class="detail-intro"><h2 id="options-title">{a(page['heading'])}</h2><p>{a(page['overview'])}</p></div>
<div class="detail-choice-list">{choices}</div>
</div></section>
<section class="section product-installation detail-fitting" id="fitting" aria-labelledby="fitting-title"><div class="container installation-layout">
<div class="installation-copy"><p class="eyebrow">Measured and installed for you</p><h2 id="fitting-title">{a(page['name'])} installation in Fort Wayne</h2><p class="installation-intro">{a(page['fitting'])}</p><div class="installation-cta"><a class="button" href="/contact">Get a Free Consultation</a></div></div>
<div class="detail-practical"><h3>Before you choose</h3><p>{a(page['limits'])}</p><h3>From samples to installation</h3><p>David brings samples to your home and measures the opening. Once you have chosen the material and controls, we confirm the quote and expected timing. We return to install the treatment, check its operation, and show you how to use it.</p><a class="text-link" href="/products/{group}">Compare all {GROUPS[group].lower()}</a></div>
</div></section>
<section class="section detail-care" id="care" aria-labelledby="care-title"><div class="container detail-intro"><h2 id="care-title">Caring for your {a(sentence_name(page['name']))}</h2><div><p>{a(page['care'])}</p><div class="detail-care-links">{care_links}</div></div></div></section>
<section class="section faq detail-faq" id="questions" aria-labelledby="questions-title"><div class="container faq-grid"><div><h2 id="questions-title">Questions about {a(sentence_name(page['name']))}</h2><p>Talk through your windows, the room, and the options before ordering.</p><a class="text-link" href="tel:+12602226467">Call David at (260) 222-6467</a></div><div>{faq}</div></div></section>
<section class="section detail-related" aria-labelledby="related-title"><div class="container"><div class="detail-related-heading"><h2 id="related-title">Also worth comparing</h2><a class="text-link" href="/products/{group}">View all {GROUPS[group].lower()}</a></div><div class="detail-related-grid">{cards}</div>{guide}</div></section>
<section class="section category-final product-final" aria-labelledby="ready-title"><div class="container"><h2 id="ready-title">See {a(sentence_name(page['name']))} in your home</h2><p>Book a free in-home consultation to compare samples and have your windows measured.</p><div class="actions"><a class="button" href="/contact">Get a Free Consultation</a><a class="button button-outline" href="tel:+12602226467">Call (260) 222-6467</a></div><span class="final-hours">Monday to Friday · 9 am to 5 pm</span></div></section>
'''
    return localize('<!doctype html>\n<html lang="en">\n'+head+'\n<body class="category-page product-page subproduct-page '+key+'-detail-page">\n<a class="skip" href="#main">Skip to content</a>\n'+header+'<main id="main">'+content+'</main>\n'+footer)


def outputs(home, shared_paths):
    for page in PAGES.values():
        yield page_file(page['path']), render(page,home,shared_paths)
