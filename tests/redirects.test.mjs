// Every URL Google knows on the old site must, on the new one, either return 200
// at the same URL, 301 in one hop to an indexable page (never the homepage), or
// be an intentional 404. The list is seo/2026-11-09/old-url-inventory.csv
// (live sitemap + live crawl + 16 months of Search Console pages + the
// 2026-09-25 plan); homepage/check_redirects.py runs the same checks locally.
import {test} from 'node:test';
import assert from 'node:assert/strict';
import {existsSync, readFileSync, readdirSync} from 'node:fs';

const dist = new URL('../homepage/dist/', import.meta.url);
const LIVE = 'https://www.beautifulblindsandshades.com';
const UTILITY = new Set(['404.html', 'service-area-map.html']);

const inventory = (() => {
  const [header, ...lines] = readFileSync(new URL('../seo/2026-11-09/old-url-inventory.csv', import.meta.url), 'utf8').trim().split(/\r?\n/);
  const keys = header.split(',');
  // The evidence column is last and may be quoted with commas; the others never contain commas.
  return lines.map((line) => {
    const cells = line.split(',');
    const row = Object.fromEntries(keys.slice(0, -1).map((key, i) => [key, cells[i]]));
    row.evidence = cells.slice(keys.length - 1).join(',');
    return row;
  });
})();

const rules = new Map();
for (const line of readFileSync(new URL('_redirects', dist), 'utf8').split('\n')) {
  if (!line.trim() || line.startsWith('#')) continue;
  const [source, target, status, ...rest] = line.trim().split(/\s+/);
  assert.equal(rest.length, 0, line);
  assert.ok(!rules.has(source), `duplicate rule for ${source}`);
  rules.set(source, {target, status});
}

// Netlify serves dist/<route>.html at /route (and 301s /route/ to it), and an
// existing file shadows a non-forced rule.
const pageFile = (route) => (route === '/' ? 'index.html' : `${route.slice(1)}.html`);
const served = (route) => existsSync(new URL(pageFile(route), dist));
const pages = readdirSync(dist, {recursive: true})
  .filter((file) => file.endsWith('.html') && !UTILITY.has(file))
  .map((file) => (file === 'index.html' ? '/' : `/${file.slice(0, -'.html'.length)}`));
const sitemap = [...readFileSync(new URL('sitemap.xml', dist), 'utf8').matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
const canonicalUrl = (route) => LIVE + (route === '/' ? '/' : route);

// What Netlify answers for an old path on the production host (after its own
// trailing-slash normalization): [status, location].
function resolve(path) {
  const route = path.replace(/\/+$/, '') || '/';
  if (served(route)) return [200, null];
  const rule = rules.get(route);
  return rule ? [Number(rule.status), rule.target] : [404, null];
}

test('the inventory covers the live sitemap and the planned redirects', () => {
  const paths = new Set(inventory.map((row) => row.old_path));
  assert.ok(inventory.length >= 128, `found ${inventory.length} old URLs`);
  for (const route of pages) assert.ok(paths.has(route), `${route} is missing from the inventory`);
  for (const source of rules.keys()) assert.ok(paths.has(source), `${source} has a rule but is not in the inventory`);
});

test('every old URL is kept, redirected in one hop, or an intentional 404', () => {
  for (const row of inventory) {
    for (const variant of [row.old_path, row.old_path === '/' ? '/' : `${row.old_path}/`]) {
      const [status, location] = resolve(variant);
      if (row.outcome === '200') {
        assert.equal(status, 200, `${variant} should be served at the same URL`);
      } else if (row.outcome === '301') {
        assert.equal(status, 301, `${variant} should redirect`);
        assert.equal(location, row.new_path, `${variant} should land on ${row.new_path}`);
        assert.notEqual(location, '/', `${variant} redirects to the homepage (a soft 404)`);
        assert.deepEqual(resolve(location), [200, null], `${variant} -> ${location} is not a single hop to a page`);
        assert.ok(sitemap.includes(canonicalUrl(location)), `${location} is not an indexable sitemap URL`);
      } else {
        assert.equal(row.outcome, '404', `${row.old_path}: unknown outcome ${row.outcome}`);
        assert.equal(status, 404, `${variant} is listed as an intentional 404`);
        assert.ok(row.evidence.length > 10, `${row.old_path}: say why it has no equivalent`);
      }
    }
  }
});

test('redirect rules are plain, permanent and relative to the canonical host', () => {
  for (const [source, {target, status}] of rules) {
    assert.equal(status, '301', source);
    assert.match(source, /^\/[^*:]+$/, `${source}: no splats or placeholders, so missing URLs keep their 404`);
    assert.match(target, /^\/[^/].*[^/]$/, `${source}: target ${target} is a relative path without a trailing slash`);
    assert.ok(!served(source), `${source} is a built page, so its rule never fires`);
  }
});

test('every indexable page has one absolute, self-referencing production canonical and no robots meta', () => {
  for (const route of pages) {
    const html = readFileSync(new URL(pageFile(route), dist), 'utf8');
    const canonicals = [...html.matchAll(/<link rel="canonical" href="([^"]+)"/g)].map((m) => m[1]);
    assert.deepEqual(canonicals, [canonicalUrl(route)], route);
    assert.doesNotMatch(html, /<meta name="robots"/, route);
  }
});

test('the sitemap lists exactly the indexable pages, none of them redirected', () => {
  assert.deepEqual([...sitemap].sort(), pages.map(canonicalUrl).sort());
  for (const url of sitemap) {
    assert.ok(url.startsWith(`${LIVE}/`), url);
    assert.ok(!rules.has(url.slice(LIVE.length)), `${url} is in the sitemap but redirects`);
  }
  assert.match(readFileSync(new URL('robots.txt', dist), 'utf8'), new RegExp(`^Sitemap: ${LIVE}/sitemap\\.xml$`, 'm'));
});

test('internal links never point at a redirecting old URL', () => {
  for (const route of pages) {
    const html = readFileSync(new URL(pageFile(route), dist), 'utf8');
    for (const [, href] of html.matchAll(/href="([^"#?]+)/g)) {
      const path = href.startsWith(LIVE) ? href.slice(LIVE.length) || '/' : href;
      if (!path.startsWith('/') || path.startsWith('//')) continue;
      assert.ok(!rules.has(path.replace(/\/+$/, '')), `${route} links to ${href}, which redirects`);
    }
  }
});
