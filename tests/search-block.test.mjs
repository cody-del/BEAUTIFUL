import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import searchBlock, {BLOCKED_ROBOTS, PRODUCTION_HOST, config} from '../netlify/edge-functions/search-block.js';

const page = () => new Response('<html></html>', {status: 200, headers: {'Content-Type': 'text/html'}});
const context = (make = page) => ({next: async () => make()});
const dist = new URL('../homepage/dist/', import.meta.url);

test('the real domain is served untouched', async () => {
  const response = await searchBlock(new Request(`https://${PRODUCTION_HOST}/products/blinds`), context());
  assert.equal(response.headers.get('x-robots-tag'), null);
  assert.equal(await response.text(), '<html></html>');
  const robots = await searchBlock(new Request(`https://${PRODUCTION_HOST}/robots.txt`), context(() => new Response(readFileSync(new URL('robots.txt', dist)))));
  assert.match(await robots.text(), /Sitemap: https:\/\/www\.beautifulblindsandshades\.com\/sitemap\.xml/);
});

test('every other host is noindexed and disallowed', async () => {
  for (const host of ['beautifulblindshadescom.netlify.app', 'deploy-preview-4--beautifulblindshadescom.netlify.app', 'beautifulblindsandshades.com']) {
    const response = await searchBlock(new Request(`https://${host}/contact`), context(() => new Response('x', {status: 404})));
    assert.equal(response.headers.get('x-robots-tag'), 'noindex, nofollow', host);
    assert.equal(response.status, 404, 'status is kept');
    const robots = await searchBlock(new Request(`https://${host}/robots.txt`), context(() => {throw Error('static robots.txt must not be served');}));
    assert.equal(await robots.text(), BLOCKED_ROBOTS);
  }
  assert.equal(config.path, '/*');
});

test('the committed site itself is indexable, apart from the 404 page', () => {
  const robots = readFileSync(new URL('robots.txt', dist), 'utf8');
  assert.doesNotMatch(robots, /Disallow: \/\s*$/m);
  assert.throws(() => readFileSync(new URL('_headers', dist)), /ENOENT/);
  for (const file of ['index.html', 'contact.html', 'products/blinds.html', 'privacy-policy.html']) {
    assert.doesNotMatch(readFileSync(new URL(file, dist), 'utf8'), /<meta name="robots"/, file);
  }
  assert.match(readFileSync(new URL('404.html', dist), 'utf8'), /<meta name="robots" content="noindex">/);
});
