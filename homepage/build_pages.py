"""Build static interior pages with the approved homepage's shared components.

Run: python3 homepage/build_pages.py
Check committed output: python3 homepage/build_pages.py --check
No client-side rendering or third-party Python packages are required.
"""
from pathlib import Path
import argparse
from html import escape
import json
import re
from routes import DIST as _DIST, page_file, pages, route_of

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
HOME = (DIST / 'index.html').read_text()
LIVE = 'https://www.beautifulblindsandshades.com'


def between(start, end):
    first = HOME.index(start)
    return HOME[first:HOME.index(end, first)]


def shared_paths(html):
    html = html.replace('src="assets/', 'src="/assets/')
    html = html.replace('href="./"', 'href="/"')
    html = html.replace('href="#consultation"', 'href="/contact"')
    return re.sub(r'href="#(products|meet-david|service-area|reviews)"', r'href="/#\1"', html)


def localize_service_links(html):
    # Only anchors change; production canonicals and schema keep their host.
    return re.sub(r'(<a\b[^>]*?\s)href="https://www\.beautifulblindsandshades\.com(/(?:services/window-treatments|about-beautiful-blinds-and-shades)/?(?:[?#][^"]*)?)"', r'\1href="\2"', html)


CATEGORIES = {
    'blinds': {
        'title': 'Custom Blinds Fort Wayne | Window Blinds | Beautiful Blinds & Shades',
        'description': 'Fort Wayne custom blind experts. Wood, faux wood, aluminum & vertical blinds. Precise measurement & pro installation. Free consultation. Call Beautiful Blinds!',
        'name': 'Custom Blinds', 'topic': 'Custom window blinds', 'image': 'blinds-natural-v2.jpg'},
    'shades': {
        'title': 'Custom Shades Fort Wayne | Window Shades | Beautiful Blinds & Shades',
        'description': 'Custom window shades for Fort Wayne homes. Roller shades, cellular shades, Roman shades & more. Free consultation. Professional installation. Call today!',
        'name': 'Custom Shades', 'topic': 'Custom window shades', 'image': 'roller-shades-fort-wayne-indiana.jpg'},
    'plantation-shutters': {
        'title': 'Plantation Shutters Fort Wayne | Custom Shutters | Beautiful Blinds',
        'description': 'Quality plantation shutters in Fort Wayne & Allen County. Custom wood, poly & composite options. Timeless style, lasting value. Free in-home consultation today!',
        'name': 'Custom Plantation Shutters', 'topic': 'Interior plantation shutters', 'image': 'wood-plantation-shutters-fort-wayne-indiana.jpg'},
}


SERVICES = {
    'window-treatments': {
        'title': 'Window Treatments Fort Wayne | Custom Blinds & Shades | Beautiful Blinds',
        'description': 'Custom blinds, shades & shutters for Fort Wayne homes. Roller shades, plantation shutters, cellular shades & more. Free consultation. Professional installation.',
        'name': 'Window Treatment Service', 'topic': 'Window treatment consultation, measuring and installation', 'image': 'roller-shades-fort-wayne-indiana.jpg'},
    'outdoor-shades': {
        'title': 'Outdoor Shades Fort Wayne | Patio & Deck Shades | Beautiful Blinds',
        'description': 'Custom outdoor shades for Fort Wayne patios, porches, and decks. Compare solar fabrics, manual and motorized options. Free in-home consultation.',
        'name': 'Outdoor Shades', 'topic': 'Outdoor shade installation', 'image': 'outdoor-natural-v2.jpg'},
    'blind-shade-repair': {
        'title': 'Blind Repair Fort Wayne | Shade Repair Service | Beautiful Blinds',
        'description': 'Blind and shade repair in Fort Wayne. Ask about broken cords, stuck shades, tilt controls, and motorized treatments. Call to discuss your repair.',
        'name': 'Blind & Shade Repair', 'topic': 'Blind and shade repair', 'image': 'blinds-venetian-original.jpg'},
    'blind-and-shade-cleaning': {
        'title': 'Professional Blind Cleaning Fort Wayne | Beautiful Blinds & Shades',
        'description': 'Professional blind and shade cleaning in Fort Wayne. Discuss dust, grease, fabric care, and the right cleaning method for your window treatments.',
        'name': 'Blind & Shade Cleaning', 'topic': 'Blind and shade cleaning', 'image': 'cellular-shades-fort-wayne-indiana.jpg'},
}


def render_category(slug, service=False):
    page = (SERVICES if service else CATEGORIES)[slug]
    url = LIVE + ('/services/' if service else '/products/') + slug
    head = between('<head>', '</head>') + '</head>'
    head = re.sub(r'<title>.*?</title>', '<title>' + escape(page['title']) + '</title>', head)
    head = re.sub(r'<meta name="description"[^>]+>', '<meta name="description" content="' + escape(page['description'], quote=True) + '">', head)
    head = head.replace('rel="canonical" href="' + LIVE + '/"', 'rel="canonical" href="' + url + '"')
    head = head.replace('href="assets/', 'href="/assets/').replace('/assets/shades-natural-v2.jpg', '/assets/' + page['image'])
    head = re.sub(r'href="styles.css[^\"]*"', 'href="/styles.css?v=20260928-cleanup"', head)
    head = re.sub(r'src="script.js[^\"]*"', 'src="/script.js?v=20260926-contact"', head)
    schema = {
        '@context': 'https://schema.org', '@graph': [
            {'@type': 'WebPage' if service else 'CollectionPage', '@id': url + '#page',
             'url': url, 'name': page['name'] + ' in Fort Wayne, Indiana',
             'about': ({'@type': 'Service', 'name': page['topic'], 'provider': {'@id': LIVE + '/#business'}, 'areaServed': {'@type': 'Place', 'name': 'Fort Wayne, Indiana'}} if service else {'@type': 'Thing', 'name': page['topic']}),
             'publisher': {'@id': LIVE + '/#business'},
             'breadcrumb': {'@id': url + '#breadcrumb'}},
            {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb',
             'itemListElement': [
                 {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': LIVE + '/'},
                 {'@type': 'ListItem', 'position': 2, 'name': page['name'], 'item': url}]}
        ]}
    head = head.replace('</head>', '<link rel="stylesheet" href="/category.css?v=20260928-cleanup">\n<script type="application/ld+json">' + json.dumps(schema) + '</script>\n</head>')
    if not service or slug in ('outdoor-shades', 'window-treatments'):
        head = head.replace('</head>', '<link rel="stylesheet" href="/product.css?v=20260928-products">\n</head>')
    if service:
        head = head.replace('</head>', '<link rel="stylesheet" href="/service.css?v=20260929-treatment-service">\n</head>')
    header = shared_paths(between('  <header class="header">', '  <main'))
    reviews = between('    <section class="testimonials"', '    <section class="section intro"')
    footer = shared_paths(HOME[HOME.index('  <footer class="footer">'):])
    if service and slug in ('blind-shade-repair', 'blind-and-shade-cleaning'):
        # Service enquiries should not imply that repair or cleaning work is free.
        header = header.replace('Get a Free Consultation', 'Contact David').replace('Free Consultation', 'Contact David')
        footer = footer.replace('Free Consultation', 'Contact David')
    product_class = 'product-page ' if not service or slug in ('outdoor-shades', 'window-treatments') else ''
    content = (ROOT / 'pages' / (slug + '.html')).read_text()
    # Google/Facebook hero badges belong on the homepage only.
    content = content.replace('{{reviews}}', reviews)
    return '<!doctype html>\n<html lang="en">\n' + head + '\n<body class="category-page ' + product_class + slug + '-page">\n  <a class="skip" href="#main">Skip to content</a>\n' + header + '<main id="main">\n' + content + '\n</main>\n' + footer


def render_contact():
    head = between('<head>', '</head>') + '</head>'
    head = re.sub(r'<title>.*?</title>', '<title>Contact Us | Beautiful Blinds &amp; Shades | Fort Wayne IN</title>', head)
    head = re.sub(r'<meta name="description"[^>]+>', '<meta name="description" content="Get your free consultation! Call Beautiful Blinds &amp; Shades in Fort Wayne at (260) 222-6467. Serving Allen County with custom blinds, shades &amp; shutters">', head)
    head = head.replace('rel="canonical" href="' + LIVE + '/"', 'rel="canonical" href="' + LIVE + '/contact"')
    head = re.sub(r'  <link rel="preload"[^>]+>\n', '', head)
    head = head.replace('href="assets/', 'href="/assets/').replace('href="styles.css', 'href="/styles.css').replace('src="script.js', 'src="/script.js')
    schema = {'@context': 'https://schema.org', '@type': 'ContactPage', '@id': LIVE + '/contact#page',
              'url': LIVE + '/contact', 'name': 'Contact Beautiful Blinds & Shades',
              'about': {'@id': LIVE + '/#business'}}
    head = head.replace('</head>', '<link rel="stylesheet" href="/contact.css?v=20260926-contact">\n<script type="application/ld+json">' + json.dumps(schema) + '</script>\n</head>')
    header = shared_paths(between('  <header class="header">', '  <main'))
    footer = shared_paths(HOME[HOME.index('  <footer class="footer">'):])
    form = between('<form class="consultation-form"', '</form>') + '</form>'
    form = form.replace('<h3 id="form-title">Request your free consultation</h3>', '<h2 id="form-title">Tell us about your windows</h2>')
    form = form.replace('Leave your details and we\'ll be in touch to find a time that works for you.', 'Choose a treatment or tell us what you need help with.')
    extra = '''<div class="form-field contact-full-field"><label for="treatment">I’m interested in <span>(optional)</span></label><select id="treatment" name="treatment"><option value="">Choose an option</option><option>Blinds</option><option>Shades</option><option>Plantation shutters</option><option>Outdoor shades</option><option>Cleaning or repair</option><option>Help choosing</option></select></div>
            <div class="form-field contact-full-field"><label for="project">About your project <span>(optional)</span></label><textarea id="project" name="project" rows="3" maxlength="2000" placeholder="Your city, the rooms you have in mind, or a question for David"></textarea></div>'''
    form = form.replace('            <button class="button form-submit"', extra + '\n            <button class="button form-submit"')
    header = header.replace('href="/contact"', 'href="#request"')
    footer = footer.replace('href="/contact"', 'href="#request"')
    content = (ROOT / 'pages' / 'contact.html').read_text().replace('{{form}}', form)
    return '<!doctype html>\n<html lang="en">\n' + head + '\n<body class="contact-page">\n<a class="skip" href="#main">Skip to content</a>\n' + header + '<main id="main">\n' + content + '\n</main>\n' + footer



ABOUT = {
    'title': 'About Beautiful Blinds & Shades | Fort Wayne Window Treatments',
    'description': 'Family-owned window treatment experts serving Fort Wayne & Allen County. Custom blinds, shades & shutters with local installation. Free consultation today!',
    'h1': 'About Beautiful Blinds & Shades', 'route': '/about-beautiful-blinds-and-shades'}


def render_about():
    url = LIVE + ABOUT['route']
    head = between('<head>', '</head>') + '</head>'
    head = re.sub(r'<title>.*?</title>', '<title>' + escape(ABOUT['title']) + '</title>', head)
    head = re.sub(r'<meta name="description"[^>]+>', '<meta name="description" content="' + escape(ABOUT['description'], quote=True) + '">', head)
    head = head.replace('rel="canonical" href="' + LIVE + '/"', 'rel="canonical" href="' + url + '"')
    head = head.replace('href="assets/', 'href="/assets/').replace('/assets/shades-natural-v2.jpg', '/assets/video-owner-frame-v2.jpg')
    head = re.sub(r'href="styles.css[^\"]*"', 'href="/styles.css?v=20260928-cleanup"', head)
    head = re.sub(r'src="script.js[^\"]*"', 'src="/script.js?v=20260926-contact"', head)
    schema = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'AboutPage', '@id': url + '#page', 'url': url, 'name': ABOUT['h1'],
         'about': {'@id': LIVE + '/#business'}, 'breadcrumb': {'@id': url + '#breadcrumb'}},
        {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': LIVE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'About', 'item': url}]}]}
    head = head.replace('</head>', '<link rel="stylesheet" href="/category.css?v=20260928-cleanup">\n<link rel="stylesheet" href="/product.css?v=20260928-products">\n<link rel="stylesheet" href="/service.css?v=20260929-treatment-service">\n<script type="application/ld+json">' + json.dumps(schema) + '</script>\n</head>')
    header = shared_paths(between('  <header class="header">', '  <main'))
    reviews = between('    <section class="testimonials"', '    <section class="section intro"')
    footer = shared_paths(HOME[HOME.index('  <footer class="footer">'):])
    content = (ROOT / 'pages' / 'about.html').read_text().replace('{{reviews}}', reviews)
    return '<!doctype html>\n<html lang="en">\n' + head + '\n<body class="category-page product-page about-page">\n  <a class="skip" href="#main">Skip to content</a>\n' + header + '<main id="main">\n' + content + '\n</main>\n' + footer


def render_not_found():
    head = between('<head>', '</head>') + '</head>'
    head = re.sub(r'<title>.*?</title>', '<title>Page not found | Beautiful Blinds &amp; Shades</title>', head)
    # Keep the error page out of search even after launch removes the preview noindex.
    head = re.sub(r'\s*<meta name="(?:description|robots)"[^>]+>', '', head)
    head = head.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n  <meta name="robots" content="noindex">', 1)
    head = re.sub(r'\s*<link rel="(?:canonical|preload)"[^>]+>', '', head)
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', '', head, flags=re.S)
    head = re.sub(r'<link rel="stylesheet" href="/blog.css[^>]*>\s*|<script src="/guides.js[^>]*></script>\s*', '', head)
    head = head.replace('href="assets/', 'href="/assets/').replace('href="styles.css', 'href="/styles.css').replace('src="script.js', 'src="/script.js')
    head = head.replace('</head>', '<link rel="stylesheet" href="/category.css?v=20260928-cleanup">\n</head>')
    header = shared_paths(between('  <header class="header">', '  <main'))
    footer = shared_paths(HOME[HOME.index('  <footer class="footer">'):])
    content = (ROOT / 'pages' / '404.html').read_text()
    return '<!doctype html>\n<html lang="en">\n' + head + '\n<body class="category-page not-found-page">\n<a class="skip" href="#main">Skip to content</a>\n' + header + '<main id="main">\n' + content + '\n</main>\n' + footer


def render_sitemap():
    # Each page's own canonical is its sitemap URL; it must match the route Netlify serves it at.
    urls = []
    for file in pages():
        canonical = re.search(r'<link rel="canonical" href="([^"]+)"', file.read_text())[1]
        if canonical.removeprefix(LIVE) != route_of(file):
            raise SystemExit(f'{file.relative_to(_DIST)} is served at {route_of(file)} but its canonical is {canonical}')
        urls.append(canonical)
    urls.sort(key=lambda u: (u != LIVE + '/', u))
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{escape(u)}</loc></url>\n' for u in urls) + '</urlset>\n'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    from build_blogs import homepage_with_guides, blog_outputs
    from build_subproducts import outputs as subproduct_outputs, localize
    from build_locations import outputs as location_outputs, localize as localize_locations
    updated_home = localize_service_links(localize_locations(localize(homepage_with_guides(HOME))))
    if args.check and updated_home != HOME:
        raise SystemExit('Homepage guides are stale. Run python3 homepage/build_pages.py')
    if not args.check:
        HOME = updated_home
        (DIST / 'index.html').write_text(HOME)
    for output, rendered in [(page_file('/products/' + slug), render_category(slug)) for slug in CATEGORIES] + [(page_file('/services/' + slug), render_category(slug, service=True)) for slug in SERVICES] + [(page_file('/contact'), render_contact()), (page_file(ABOUT['route']), render_about())] + list(blog_outputs(HOME)) + list(subproduct_outputs(HOME, shared_paths)) + list(location_outputs(HOME, shared_paths)) + [(DIST / '404.html', render_not_found())]:
        rendered = localize_service_links(localize_locations(localize(rendered)))
        if args.check:
            if not output.exists() or output.read_text() != rendered:
                raise SystemExit(f'{output} is stale. Run python3 homepage/build_pages.py')
            print('Generated page is current:', output.relative_to(DIST))
        else:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(rendered)
            print('Built', output)
    sitemap = render_sitemap()
    if args.check:
        if not (DIST / 'sitemap.xml').exists() or (DIST / 'sitemap.xml').read_text() != sitemap:
            raise SystemExit('sitemap.xml is stale. Run python3 homepage/build_pages.py')
        print('Sitemap is current:', sitemap.count('<url>'), 'URLs')
    else:
        (DIST / 'sitemap.xml').write_text(sitemap)
        print('Built', DIST / 'sitemap.xml', sitemap.count('<url>'), 'URLs')
