import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync, existsSync} from 'node:fs';

const dist = new URL('../homepage/dist/', import.meta.url);
const read = path => readFileSync(new URL(path, dist), 'utf8');
const forms = {'index.html': read('index.html'), 'contact.html': read('contact.html')};

test('both consultation forms carry the spam trap, optional SMS consent, policy links and thank-you card', () => {
  for (const [page, html] of Object.entries(forms)) {
    const form = html.slice(html.indexOf('<form class="consultation-form"'), html.indexOf('</form>'));
    assert.match(form, /<input id="website" name="website" type="text" tabindex="-1" autocomplete="off">/, page);
    const box = form.match(/<input id="sms-opt-in"[^>]*>/)?.[0];
    assert.ok(box, `${page}: SMS checkbox`);
    // Carriers reject consent that is pre-ticked or required.
    assert.doesNotMatch(box, /checked|required/, page);
    assert.match(form, /<legend>Text messages \(optional\)<\/legend>/, page);
    for (const phrase of ['Beautiful Blinds &amp; Shades', 'Message frequency varies', 'Message &amp; data rates may apply', '<strong>STOP</strong>', '<strong>HELP</strong>', 'Consent is not a condition of purchase']) {
      assert.ok(form.includes(phrase), `${page}: ${phrase}`);
    }
    assert.match(form, /href="\/privacy-policy"/, page);
    assert.match(form, /href="\/terms-of-service"/, page);
    assert.match(html, /<div class="consultation-success" id="consultation-success" role="status" tabindex="-1" hidden>/, page);
    assert.match(html, /<p class="form-status" id="form-status" role="status" tabindex="-1" hidden>/, page);
  }
  // The Contact page's optional fields sit above the consent box.
  const contact = forms['contact.html'];
  assert.ok(contact.indexOf('id="project"') < contact.indexOf('class="sms-consent"'));
});

test('the policies the form links to are served, with the A2P no-sharing clause', () => {
  for (const page of ['privacy-policy.html', 'terms-of-service.html']) assert.ok(existsSync(new URL(page, dist)), page);
  assert.match(read('privacy-policy.html'), /Mobile information will not be shared with third parties or affiliates for marketing or promotional purposes/);
  assert.match(read('terms-of-service.html'), /<h2>SMS Terms<\/h2>/);
  assert.match(read('privacy-policy.html'), /<link rel="canonical" href="https:\/\/www\.beautifulblindsandshades\.com\/privacy-policy">/);
});

test('script.js posts to the function and reports one generate_lead, only after a confirmed lead', () => {
  const script = read('script.js');
  assert.ok(script.includes("fetch('/api/consultation'"));
  assert.equal(script.match(/'generate_lead'/g).length, 1);
  const handler = script.slice(script.indexOf("consultationForm?.addEventListener('submit'"));
  assert.ok(handler.indexOf("result.success !== true") < handler.indexOf('reportLead()'));
  assert.doesNotMatch(script, /This preview does not send requests/);
});

test('GA4 loads on the production host only', () => {
  const head = forms['index.html'].slice(0, forms['index.html'].indexOf('</head>'));
  assert.match(head, /if \(location\.hostname === 'www\.beautifulblindsandshades\.com'\) \{[^<]*gtag\('config', 'G-TBE6JC5ZYG'\)/);
  assert.doesNotMatch(head, /<script async src="https:\/\/www\.googletagmanager\.com/);
});

test('GTM loads the live container on the production host only', () => {
  const head = read('index.html').slice(0, read('index.html').indexOf('</head>'));
  assert.match(head, /if \(location\.hostname === 'www\.beautifulblindsandshades\.com'\) \{\(function\(w,d,s,l,i\)[^<]*'GTM-KHJ3F2F5'\);\}<\/script>/);
  for (const page of ['contact.html', 'products/blinds.html', 'blog-post/motorized-blinds-and-shades-in-fort-wayne.html']) assert.ok(read(page).includes("'GTM-KHJ3F2F5'"), page);
});
