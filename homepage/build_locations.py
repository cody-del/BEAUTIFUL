"""Build service coverage pages at their existing production paths."""
from pathlib import Path
from html import escape
import json
import re

ROOT=Path(__file__).resolve().parent
LIVE='https://www.beautifulblindsandshades.com'
BASELINE=json.loads((ROOT/'locations/source-baseline.json').read_text())
CITIES=json.loads((ROOT/'locations/city-routes.json').read_text())
ROUTES={p['url'].removeprefix(LIVE) for p in BASELINE.values()}
HUB=BASELINE['service-area']['url'].removeprefix(LIVE)
CITY_PAGES={
    'auburn': {'name':'Auburn, Indiana','image':'blinds-venetian-original.jpg'},
    'monroeville': {'name':'Monroeville, Indiana','image':'blinds-venetian-original.jpg'},
    'warsaw': {'name':'Warsaw, Indiana','image':'roller-shades-fort-wayne-indiana.jpg'},
    'hicksville': {'name':'Hicksville, Ohio','image':'roman-shades-fort-wayne-indiana.jpg'},
}
# The source body and directory identify Ohio. Keep the legacy Indiana URL;
# this factual correction is a preview draft pending service-coverage confirmation.
METADATA_OVERRIDES={'hicksville': {'title':'Custom Window Treatments in Hicksville, Ohio'}}
GROUPS=[('Fort Wayne & Allen County',['Fort Wayne','New Haven','Leo-Cedarville','Huntertown','Grabill','Woodburn','Monroeville','Harlan','Hoagland']),('Nearby Indiana communities',['Auburn','Angola','Kendallville','Bluffton','Warsaw','Syracuse','Columbia City']),('Hicksville, Ohio',['Hicksville'])]


def localize(html):
    # Only anchor destinations change. Canonicals must keep the production host.
    html=re.sub(r'(<a\b[^>]*?\s)href="https://www\.beautifulblindsandshades\.com([^"?#]*)([?#][^"]*)?"',lambda m:m[1]+'href="'+m[2]+(m[3] or '')+'"' if m[2].rstrip('/') in ROUTES else m[0],html)
    # The shared navigation can now lead to the complete directory.
    for name in ('Service Area','Explore our service area'):
        html=re.sub(r'href="(?:/)?#service-area">'+name, 'href="'+HUB+'">'+name,html)
    return html


def city_groups():
    groups=[]
    for title,names in GROUPS:
        links=[]
        for name in names:
            slug=name.lower().replace(' ','-')
            city=next(p for p in CITIES if '-'+slug+'-' in p['url'])
            label=name+(', Ohio' if name=='Hicksville' else ', Indiana')
            links.append('<li><a href="'+city['url']+'">'+escape(label)+'</a></li>')
        groups.append('<details class="coverage-group"><summary>'+escape(title)+'<span class="coverage-count">'+str(len(names))+(' community' if len(names)==1 else ' communities')+'</span></summary><ul>'+''.join(links)+'</ul></details>')
    return ''.join(groups)


def outputs(home,shared_paths):
    for key,source in BASELINE.items():
        page={**source,**METADATA_OVERRIDES.get(key,{})}
        url=page['url'];path=url.removeprefix(LIVE)
        head=home[home.index('<head>'):home.index('</head>')+7]
        head=re.sub(r'<title>.*?</title>','<title>'+escape(page['title'])+'</title>',head)
        head=re.sub(r'<meta name="description"[^>]+>','<meta name="description" content="'+escape(page['description'],quote=True)+'">',head)
        head=re.sub(r'<link rel="canonical"[^>]+>','<link rel="canonical" href="'+url+'">',head)
        head=head.replace('href="assets/','href="/assets/').replace('href="styles.css','href="/styles.css').replace('src="script.js','src="/script.js')
        if key in CITY_PAGES:head=head.replace('/assets/shades-natural-v2.jpg','/assets/'+CITY_PAGES[key]['image'])
        else:head=re.sub(r'\s*<link rel="preload"[^>]+>','',head)
        head=re.sub(r'<link rel="stylesheet" href="/blog.css[^>]*>\s*','',head)
        head=re.sub(r'<script src="/guides.js[^>]*></script>\s*','',head)
        crumbs=[('Home',LIVE+'/'),('Service area',LIVE+HUB)]
        if key in CITY_PAGES:crumbs.append((CITY_PAGES[key]['name'],url))
        schema={'@context':'https://schema.org','@graph':[
            {'@type':'WebPage' if key in CITY_PAGES else 'CollectionPage','@id':url+'#page','url':url,'name':page['title'],'description':page['description'],'publisher':{'@id':LIVE+'/#business'},'breadcrumb':{'@id':url+'#breadcrumb'}},
            {'@type':'BreadcrumbList','@id':url+'#breadcrumb','itemListElement':[{'@type':'ListItem','position':i+1,'name':n,'item':u} for i,(n,u) in enumerate(crumbs)]}]}
        head=head.replace('</head>','<link rel="stylesheet" href="/category.css?v=20260928-cleanup">\n<link rel="stylesheet" href="/product.css?v=20260928-products">\n<link rel="stylesheet" href="/location.css?v=20260929-locations">\n<script type="application/ld+json">'+json.dumps(schema)+'</script>\n</head>')
        header=shared_paths(home[home.index('  <header class="header">'):home.index('  <main')])
        footer=shared_paths(home[home.index('  <footer class="footer">'):])
        content=(ROOT/'pages'/(key+'.html')).read_text().replace('{{city_groups}}',city_groups())
        rendered='<!doctype html>\n<html lang="en">\n'+head+'\n<body class="category-page product-page location-page '+key+'-page">\n<a class="skip" href="#main">Skip to content</a>\n'+header+'<main id="main">\n'+content+'\n</main>\n'+footer
        yield ROOT/'dist'/path.strip('/')/'index.html',localize(rendered)
