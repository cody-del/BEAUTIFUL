# Contact page build

Built from the September 25 contact-page audit brief and archived live-site content. Local preview only; no production deployment or domain change.

## SEO preservation

- Existing URL/canonical target: `https://www.beautifulblindsandshades.com/contact`.
- Existing title retained exactly: Contact Us | Beautiful Blinds & Shades | Fort Wayne IN
- Existing description retained exactly: Get your free consultation! Call Beautiful Blinds & Shades in Fort Wayne at (260) 222-6467. Serving Allen County with custom blinds, shades & shutters
- One H1 retains the free in-home consultation intent. Body content explains the visit, samples, measurements, quote, and service coverage without competing for the homepage's broad blinds/Fort Wayne intent.
- Preserved public phone, email, hours, repair/cleaning links, and coverage. No showroom claim or buy-two-get-one promotion.
- ContactPage structured data references the shared business entity. Preview noindex and robots protections remain.
- Semrush `resource_organic`, US database, exact `/contact` URL, requested keyword/position/URL/timestamp: returned `ERROR 50 :: NOTHING FOUND`. The earlier audit also had no contact-page ranking rows. This is unavailable evidence, not proof of zero rankings or traffic. Refresh with Search Console and Semrush before launch.

## Design and behavior

- Shared brand colors, Manrope headings, responsive navigation, and footer.
- Desktop split layout: contact details beside the custom consultation form. Centered mobile intro with a full-width form below.
- Four required contact fields plus optional treatment and project details. Native labels, autocomplete on contact inputs, input validation, and inline errors.
- Visible preview notice before entering details. Valid submissions retain the values and explicitly state that nothing was sent; no lead endpoint or fake success message.
- Homepage and blinds consultation buttons now lead to `/contact`. Contact-page consultation controls scroll to its form and close the mobile menu.
- Plain consultation steps and the existing blue-boundary service map.

## Validation

- Generated output is reproducible; JavaScript syntax passes.
- Titles, canonicals, descriptions, one H1, unique IDs, JSON-LD, local asset paths, local routes, and same-page fragments checked on all three pages.
- Browser layout checked at 320, 390, 768, 1024, and 1440 pixels with no horizontal document overflow. Desktop and mobile screenshots visually reviewed.
- Empty-form errors and valid dummy preview submission tested locally; no live lead created. Shared navigation and homepage/blinds links to Contact verified; no browser JavaScript errors observed.

## Before launch

Connect and verify this client's lead-delivery workflow, server-side validation, abuse protection, and appropriate privacy notice. Verify current business details, tracking, production indexability, and all route behavior as part of the existing migration checklist. Do not publish this preview as a complete replacement for the live website.
