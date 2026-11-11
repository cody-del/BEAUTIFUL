import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, readdirSync, readFileSync, rmSync, statSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { extname, join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';
import { minifyAsset, minifySite } from '../scripts/minify-site.mjs';

// Netlify publishes _site/: homepage/dist/ with every .css and .js file minified (Semrush Site
// Audit 2026-11-12: "Unminified JavaScript and CSS files", 79 warnings for script.js and
// guides.js). The minified files must behave exactly like the readable sources.
const dist = fileURLToPath(new URL('../homepage/dist/', import.meta.url));
const files = dir => readdirSync(dir).flatMap(name => {
  const path = join(dir, name);
  return statSync(path).isDirectory() ? files(path) : [path];
});

test('the minified script.js keeps its page globals, form endpoint, Turnstile and GA4 lead event', async () => {
  const source = readFileSync(join(dist, 'script.js'), 'utf8');
  const script = await minifyAsset(source, '.js');
  assert.ok(script.length < source.length * 0.8, 'script.js should shrink');
  assert.doesNotMatch(script, /\n\s|\/\/ /, 'no indentation or comments left');
  // A classic script: its top-level names are page globals and must keep their names.
  for (const name of ['menuButton', 'navigation', 'TURNSTILE_LIVE_HOSTS', 'TURNSTILE_SITE_KEY', 'consultationForm', 'CALL_US']) {
    assert.match(script, new RegExp(`\\b${name}=`), `${name} must keep its name`);
  }
  for (const text of ['"/api/consultation"', 'onTurnstileLoad', 'generate_lead', '??=']) {
    assert.ok(script.includes(text), `minified script.js lost ${text}`);
  }
});

test('the minified guides.js still drives the guide carousels', async () => {
  const guides = await minifyAsset(readFileSync(join(dist, 'guides.js'), 'utf8'), '.js');
  for (const selector of ['.guide-carousel', '.guide-track', '.guide-card', '.guide-prev']) {
    assert.ok(guides.includes(selector), `minified guides.js lost ${selector}`);
  }
});

test('every stylesheet minifies smaller', async () => {
  const sheets = files(dist).filter(path => extname(path) === '.css');
  assert.ok(sheets.length >= 8);
  for (const path of sheets) {
    const source = readFileSync(path, 'utf8');
    const css = await minifyAsset(source, '.css');
    assert.ok(css.length < source.length, `${path} should shrink`);
    assert.doesNotMatch(css, /\n(?!$)|\/\*/, `${path}: no line breaks (but the last) or comments left`);
  }
});

test('_site has exactly the files in homepage/dist, and only .css and .js files change', async () => {
  const out = mkdtempSync(join(tmpdir(), 'bbs-site-'));
  try {
    const results = await minifySite(dist, out);
    assert.deepEqual(
      results.map(r => r.file).sort(),
      files(dist).filter(path => /\.(css|js)$/.test(path)).map(path => relative(dist, path)).sort(),
    );
    for (const path of files(dist)) {
      const rel = relative(dist, path);
      const same = readFileSync(path).equals(readFileSync(join(out, rel)));
      assert.equal(same, !/\.(css|js)$/.test(rel), `${rel}: ${same ? 'should be minified' : 'should be copied unchanged'}`);
    }
    // The redirects and the IndexNow key file must still be published.
    assert.ok(readFileSync(join(out, '_redirects'), 'utf8').includes('/products/shade'));
  } finally {
    rmSync(out, { recursive: true, force: true });
  }
});
