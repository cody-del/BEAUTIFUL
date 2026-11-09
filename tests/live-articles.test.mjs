import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readdirSync, readFileSync} from 'node:fs';

const root = new URL('../homepage/', import.meta.url);
const snapshots = readdirSync(new URL('pages/live-articles/', root)).filter(f => f.endsWith('.html'));
const page = file => readFileSync(new URL('dist/' + file.replace(/__/g, '/'), root), 'utf8');
const towns = ['Harlan', 'Huntertown', 'Columbia City', 'Angola', 'Auburn', 'Bluffton', 'Grabill', 'Hicksville', 'Hoagland',
  'Kendallville', 'Leo-Cedarville', 'Monroeville', 'New Haven', 'Syracuse', 'Warsaw', 'Woodburn'];

test('every snapshot appears once, before the page closes, on the page it came from', () => {
  assert.ok(snapshots.length >= 25, `only ${snapshots.length} snapshots`);
  for (const file of snapshots) {
    const html = page(file);
    assert.equal(html.match(/class="section live-article"/g)?.length, 1, file);
    assert.ok(html.indexOf('class="section live-article"') < html.indexOf('class="section category-final'), file);
    assert.equal(html.match(/<h1\b/g).length, 1, `${file}: one H1`);
  }
});

test('the ported text carries no prices, unconfirmed claims or another town', () => {
  const banned = /\$\s?\d|buy (?:2|two)\b|family[- ]owned|\bfor (?:many |several )?years\b|\b\d+\+?\s+years\b|warrant(?:y|ies)|—/i;
  for (const file of snapshots) {
    const text = readFileSync(new URL('pages/live-articles/' + file, root), 'utf8');
    assert.doesNotMatch(text, banned, file);
    assert.doesNotMatch(text, /<(?:script|iframe|img|div|span)\b|\sclass=|\sstyle=/i, file);
    if (file.startsWith('beautiful-blinds-shades-service-areas__')) {
      const own = towns.find(t => file.includes(t.toLowerCase().replace(' ', '-')));
      for (const other of towns.filter(t => t !== own)) assert.ok(!new RegExp(`\\b${other}\\b`).test(text), `${file} names ${other}`);
    }
  }
  assert.doesNotMatch(readFileSync(new URL('pages/live-articles/beautiful-blinds-shades-service-areas__window-treatments-hicksville-indiana.html', root), 'utf8'), /Hicksville,? Indiana/);
});
