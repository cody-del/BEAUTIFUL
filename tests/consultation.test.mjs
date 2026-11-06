import {test} from 'node:test';
import assert from 'node:assert/strict';
import {submitConsultation, leadNote, ghlTagsUrl, ghlNotesUrl, GHL_UPSERT_URL, LEAD_TAG, LEAD_SOURCE, MIN_FILL_MS, SMS_OPT_IN_TAG} from '../netlify/lib/consultation.mjs';

const env = {GHL_PRIVATE_TOKEN: 'pit-test', GHL_LOCATION_ID: 'location-1'};
const valid = {firstName: 'Test', lastName: 'Person', phone: '(260) 555-0123', email: 'test@example.com', website: '', elapsedMs: 20000, page: '/contact'};
const now = () => new Date('2026-11-06T15:00:00Z');
const mustNotCall = () => {throw Error('must not call');};
const ok = body => ({ok: true, status: 201, json: async () => body});
const created = async () => ok({new: true, contact: {id: 'contact-1'}});
// Records every GHL call; answers the upsert with a contact id and the rest with 201.
const capture = (overrides = {}) => {
  const calls = [];
  const fetcher = async (url, request) => {
    calls.push({url, method: request.method, headers: request.headers, body: JSON.parse(request.body)});
    if (overrides[url]) return overrides[url]();
    return url === GHL_UPSERT_URL ? created() : ok({});
  };
  const call = url => calls.find(c => c.url === url);
  return {calls, call, fetcher};
};

test('incomplete, invalid and spam requests never reach GHL', async () => {
  for (const data of [
    null, [], {}, 'Test Person',
    {...valid, phone: '123'}, {...valid, phone: '22605550123'}, {...valid, email: 'invalid'}, {...valid, email: 'a@b.c'},
    {...valid, firstName: ' '}, {...valid, lastName: ''}, {...valid, firstName: 'x'.repeat(81)}, {...valid, lastName: 42},
    {...valid, email: `${'a'.repeat(250)}@example.com`},
    {...valid, website: 'https://spam.example'},
    {...valid, elapsedMs: undefined}, {...valid, elapsedMs: MIN_FILL_MS - 1},
    {...valid, elapsedMs: '20000'}, {...valid, elapsedMs: 20000.5},
    {...valid, smsOptIn: 'on'}, {...valid, smsOptIn: 1},
    {...valid, treatment: 'Awnings'}, {...valid, project: 'x'.repeat(2001)}, {...valid, project: 7},
    {...valid, page: 'https://example.com/'}, {...valid, page: '/<script>'},
  ]) {
    const result = await submitConsultation(data, {env, fetcher: mustNotCall, rateLimited: mustNotCall});
    assert.equal(result.status, 400, JSON.stringify(data));
    assert.equal(result.body.success, false);
  }
});

test('upserts the contact without tags, then tags it website lead and returns its id', async () => {
  const {calls, call, fetcher} = capture();
  const result = await submitConsultation({...valid, firstName: '  Test ', lastName: ' Van Person ', email: ' Test@Example.com '}, {env, fetcher, now});
  assert.deepEqual(result, {status: 200, body: {success: true, contactId: 'contact-1'}});
  assert.equal(calls[0].url, GHL_UPSERT_URL);
  for (const c of calls) {
    assert.equal(c.method, 'POST');
    assert.equal(c.headers.Authorization, 'Bearer pit-test');
    assert.equal(c.headers.Version, '2021-07-28');
  }
  assert.deepEqual(call(GHL_UPSERT_URL).body, {
    locationId: 'location-1', firstName: 'Test', lastName: 'Van Person', phone: '+12605550123', email: 'test@example.com',
    source: 'Website (beautifulblindsandshades.com)',
  });
  assert.deepEqual(call(ghlTagsUrl('contact-1')).body, {tags: ['website lead']});
  assert.equal(call(ghlTagsUrl('contact-1')).url, 'https://services.leadconnectorhq.com/contacts/contact-1/tags');
  assert.equal(calls.length, 3);
  assert.equal(LEAD_TAG, 'website lead');
  assert.equal(LEAD_SOURCE, 'Website (beautifulblindsandshades.com)');
});

test('an 11-digit number keeps its country code', async () => {
  const {call, fetcher} = capture();
  await submitConsultation({...valid, phone: '1-260-555-0123'}, {env, fetcher});
  assert.equal(call(GHL_UPSERT_URL).body.phone, '+12605550123');
});

test('adds the SMS opt-in tag only when the box was ticked', async () => {
  assert.equal(SMS_OPT_IN_TAG, 'sms-transactional-opt-in');
  for (const [consent, tags] of [
    [{}, ['website lead']],
    [{smsOptIn: false}, ['website lead']],
    [{smsOptIn: true}, ['website lead', 'sms-transactional-opt-in']],
  ]) {
    const {call, fetcher} = capture();
    await submitConsultation({...valid, ...consent}, {env, fetcher});
    assert.deepEqual(call(ghlTagsUrl('contact-1')).body.tags, tags, JSON.stringify(consent));
  }
});

test('the note records the page, treatment, project and a dated text-message choice', async () => {
  const {call, fetcher} = capture();
  await submitConsultation({...valid, treatment: 'Shades', project: '  Three bedroom windows in Auburn ', smsOptIn: true}, {env, fetcher, now});
  assert.deepEqual(call(ghlNotesUrl('contact-1')).body, {body: [
    'Website consultation request, 2026-11-06T15:00:00.000Z, from /contact.',
    'Interested in: Shades',
    'About the project: Three bedroom windows in Auburn',
    'Text messages: opted in (ticked the optional box agreeing to texts about this request: consultations, appointments, estimates, scheduling, project updates and customer service).',
  ].join('\n')});
  assert.equal(leadNote({}, {now: now()}), 'Website consultation request, 2026-11-06T15:00:00.000Z, from the website.\nText messages: not opted in.');
});

test('refuses to send without credentials', async t => {
  t.mock.method(console, 'error', () => {});
  for (const missing of [{}, {GHL_PRIVATE_TOKEN: 'pit-test'}, {GHL_LOCATION_ID: 'location-1'}, {GHL_API_KEY: 'pit-other', GHL_LOCATION_ID: 'location-1'}]) {
    const result = await submitConsultation(valid, {env: missing, fetcher: mustNotCall});
    assert.equal(result.status, 500);
    assert.match(result.body.error, /\(260\) 222-6467/);
  }
});

test('exactly the minimum fill time is accepted', async () => {
  const {fetcher} = capture();
  const result = await submitConsultation({...valid, elapsedMs: MIN_FILL_MS}, {env, fetcher});
  assert.equal(result.status, 200);
});

test('never reports success unless GHL returns a contact id', async t => {
  t.mock.method(console, 'error', () => {});
  for (const upsert of [
    async () => ({ok: false, status: 401, json: async () => ({message: 'Invalid JWT'})}),
    async () => ({ok: false, status: 422, json: async () => ({message: 'Unprocessable'})}),
    async () => ok({contact: {}}),
    async () => ok({}),
    async () => ({ok: true, status: 200, json: async () => {throw new SyntaxError('Unexpected token <');}}),
    async () => {throw new TypeError('fetch failed');},
  ]) {
    const {calls, fetcher} = capture({[GHL_UPSERT_URL]: upsert});
    const result = await submitConsultation(valid, {env, fetcher});
    assert.equal(result.status, 502);
    assert.equal(result.body.success, false);
    assert.match(result.body.error, /\(260\) 222-6467/);
    assert.equal(calls.length, 1, 'no tag or note without a contact');
  }
});

test('a lead the workflow tag never reached is reported as a failure', async t => {
  t.mock.method(console, 'error', () => {});
  for (const tags of [
    async () => ({ok: false, status: 401, json: async () => ({})}),
    async () => {throw new DOMException('timed out', 'TimeoutError');},
  ]) {
    const {fetcher} = capture({[ghlTagsUrl('contact-1')]: tags});
    const result = await submitConsultation(valid, {env, fetcher});
    assert.equal(result.status, 502);
    assert.match(result.body.error, /\(260\) 222-6467/);
  }
});

test('a failed note is logged but the tagged lead still succeeds', async t => {
  const logged = [];
  t.mock.method(console, 'error', (...args) => logged.push(args.join(' ')));
  for (const note of [async () => ({ok: false, status: 403, json: async () => ({})}), async () => {throw new TypeError('fetch failed');}]) {
    const {fetcher} = capture({[ghlNotesUrl('contact-1')]: note});
    const result = await submitConsultation(valid, {env, fetcher});
    assert.deepEqual(result, {status: 200, body: {success: true, contactId: 'contact-1'}});
  }
  assert.equal(logged.length, 2);
});

test('logs never contain the token or the lead’s details', async t => {
  const logged = [];
  t.mock.method(console, 'error', (...args) => logged.push(args.join(' ')));
  t.mock.method(console, 'log', (...args) => logged.push(args.join(' ')));
  await submitConsultation(valid, {env, fetcher: async () => ({ok: false, status: 400, json: async () => ({message: valid.email})})});
  await submitConsultation(valid, {env, fetcher: async () => {throw new TypeError(`fetch failed for ${valid.email}`);}});
  await submitConsultation(valid, {env: {}, fetcher: mustNotCall});
  const {fetcher} = capture({[ghlTagsUrl('contact-1')]: async () => {throw new TypeError(`bad ${valid.phone}`);}});
  await submitConsultation(valid, {env, fetcher});
  assert.equal(logged.length, 4);
  for (const line of logged) {
    for (const secret of ['pit-test', 'test@example.com', '555-0123', '5550123', 'Person']) assert.equal(line.includes(secret), false, line);
  }
});

test('rate-limited visitors are told to wait, and only valid leads count toward the limit', async () => {
  const limited = await submitConsultation(valid, {env, fetcher: mustNotCall, rateLimited: () => true});
  assert.equal(limited.status, 429);
  assert.equal(limited.body.success, false);
  let checks = 0;
  await submitConsultation({...valid, phone: '1'}, {env, fetcher: mustNotCall, rateLimited: () => {checks++; return false;}});
  assert.equal(checks, 0);
});
