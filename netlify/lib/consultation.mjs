// Consultation requests from the website go straight to Beautiful Blinds &
// Shades' GoHighLevel location, the way the go. landing page sends its own
// (cody-del/beautifullanding, netlify/lib/consultation.mjs). The token and
// location come from this site's Netlify environment variables, never the browser.
const GHL_API = 'https://services.leadconnectorhq.com';
export const GHL_UPSERT_URL = `${GHL_API}/contacts/upsert`;
export const ghlTagsUrl = contactId => `${GHL_API}/contacts/${encodeURIComponent(contactId)}/tags`;
export const ghlNotesUrl = contactId => `${GHL_API}/contacts/${encodeURIComponent(contactId)}/notes`;
const GHL_VERSION = '2021-07-28';

// The tag GHL's "Form Submission bbs" workflow triggers on for main-site forms
// (google_landing_page is for the go. landing page only). Nothing here enrols the
// lead; renaming it detaches every new lead from that workflow without any error,
// so change the GHL trigger in the same sitting.
export const LEAD_TAG = 'website lead';
export const LEAD_SOURCE = 'Website (beautifulblindsandshades.com)';
// Added only when the visitor ticked the optional text-message box; a phone
// number alone is not consent. The same tag the landing page and Shade
// Strategy's other A2P sites use, so texting workflows can check one tag.
export const SMS_OPT_IN_TAG = 'sms-transactional-opt-in';

// Submissions sooner than this after the page loads are refused. script.js waits
// it out, so a person is never caught by it.
export const MIN_FILL_MS = 3000;

// The Contact page's optional "I'm interested in" choices.
export const TREATMENTS = ['Blinds', 'Shades', 'Plantation shutters', 'Outdoor shades', 'Cleaning or repair', 'Help choosing'];

const PHONE = '(260) 222-6467';

// The pattern zod's z.string().email() accepts, as on the landing page.
export const EMAIL = /^(?!\.)(?!.*\.\.)([A-Z0-9_'+\-.]*)[A-Z0-9_+-]@([A-Z0-9][A-Z0-9-]*\.)+[A-Z]{2,}$/i;

// The note keeps what the contact fields can't: the treatment, the project text,
// the page, and a dated record of the text-message choice.
export function leadNote(data, {now = new Date()} = {}) {
  const lines = [`Website consultation request, ${now.toISOString()}, from ${data.page || 'the website'}.`];
  if (data.treatment) lines.push(`Interested in: ${data.treatment}`);
  if (data.project?.trim()) lines.push(`About the project: ${data.project.trim()}`);
  lines.push(data.smsOptIn === true
    ? 'Text messages: opted in (ticked the optional box agreeing to texts about this request: consultations, appointments, estimates, scheduling, project updates and customer service).'
    : 'Text messages: not opted in.');
  return lines.join('\n');
}

export async function submitConsultation(data, {fetcher = fetch, rateLimited = () => false, env = process.env, now = () => new Date()} = {}) {
  const fail = (status, error) => ({status, body: {success: false, error}});
  if (!data || typeof data !== 'object' || Array.isArray(data)) return fail(400, 'Please check your contact details.');
  // Hidden field that people never see; bots fill it in.
  if (data.website) return fail(400, `Unable to submit this request. Please call ${PHONE}.`);
  // Time since the page loaded, measured on the visitor's own clock.
  if (!Number.isSafeInteger(data.elapsedMs) || data.elapsedMs < MIN_FILL_MS) return fail(400, `Unable to submit this request. Please call ${PHONE}.`);
  const limits = {firstName: 80, lastName: 80, phone: 30, email: 254};
  for (const [field, limit] of Object.entries(limits)) {
    if (typeof data[field] !== 'string' || !data[field].trim() || data[field].trim().length > limit) return fail(400, 'Please complete all contact fields.');
  }
  const digits = data.phone.replace(/\D/g, '');
  if (!/^\d{10}$|^1\d{10}$/.test(digits) || !EMAIL.test(data.email.trim())) return fail(400, 'Please enter a valid phone number and email address.');
  if (data.smsOptIn !== undefined && typeof data.smsOptIn !== 'boolean') return fail(400, 'Please check your contact details.');
  if (data.treatment !== undefined && data.treatment !== '' && !TREATMENTS.includes(data.treatment)) return fail(400, 'Please check your contact details.');
  if (data.project !== undefined && (typeof data.project !== 'string' || data.project.length > 2000)) return fail(400, 'Please keep your project note under 2,000 characters.');
  if (data.page !== undefined && (typeof data.page !== 'string' || !/^\/[\w\-/]{0,200}$/.test(data.page))) return fail(400, 'Please check your contact details.');
  if (rateLimited()) return fail(429, `Too many requests. Please wait a few minutes or call ${PHONE}.`);

  const token = env.GHL_PRIVATE_TOKEN;
  const locationId = env.GHL_LOCATION_ID;
  if (!token || !locationId) {
    console.error('[consultation] GHL_PRIVATE_TOKEN and GHL_LOCATION_ID are not configured');
    return fail(500, `We couldn’t send your request. Please call ${PHONE}.`);
  }
  const headers = {Authorization: `Bearer ${token}`, Version: GHL_VERSION, 'Content-Type': 'application/json', Accept: 'application/json'};
  const post = (url, body, ms) => fetcher(url, {method: 'POST', headers, body: JSON.stringify(body), signal: AbortSignal.timeout(ms)});
  // Tags are added in their own call, not sent on the upsert: GHL documents the
  // contact tags field as overwriting the existing list, which could strip a
  // returning customer's tags. The tags endpoint only adds.
  const contact = {
    locationId,
    firstName: data.firstName.trim(),
    lastName: data.lastName.trim(),
    phone: `+${digits.length === 10 ? '1' : ''}${digits}`,
    email: data.email.trim().toLowerCase(),
    source: LEAD_SOURCE,
  };
  const tags = [LEAD_TAG, ...(data.smsOptIn === true ? [SMS_OPT_IN_TAG] : [])];
  let contactId;
  try {
    // Netlify stops synchronous functions after 10 seconds, so the three calls
    // share that budget: 4.5 s for the upsert, then 4 s for tags and note together.
    const response = await post(GHL_UPSERT_URL, contact, 4500);
    const result = await response.json();
    contactId = result?.contact?.id || result?.contactId;
    if (!response.ok || typeof contactId !== 'string' || !contactId) {
      console.error(`[consultation] GHL did not confirm the contact (HTTP ${response.status})`);
      return fail(502, `We couldn’t confirm your request. Please call ${PHONE} for help.`);
    }
  } catch (error) {
    console.error(`[consultation] GHL contact request failed: ${error.name}`);
    return fail(502, `We couldn’t confirm your request. Please call ${PHONE} before submitting again.`);
  }
  const [tagged, noted] = await Promise.allSettled([
    post(ghlTagsUrl(contactId), {tags}, 4000),
    post(ghlNotesUrl(contactId), {body: leadNote(data, {now: now()})}, 4000),
  ]);
  // Without the tag, the GHL workflow never sees the lead and nobody is told
  // about it, so the visitor is asked to call. Sending again is safe: the upsert
  // finds the same contact.
  if (tagged.status !== 'fulfilled' || !tagged.value.ok) {
    console.error(`[consultation] GHL did not tag the contact (${tagged.status === 'fulfilled' ? `HTTP ${tagged.value.status}` : tagged.reason?.name})`);
    return fail(502, `We couldn’t confirm your request. Please call ${PHONE} for help.`);
  }
  // A missing note loses the project text, not the lead.
  if (noted.status !== 'fulfilled' || !noted.value.ok) {
    console.error(`[consultation] GHL did not save the note (${noted.status === 'fulfilled' ? `HTTP ${noted.value.status}` : noted.reason?.name})`);
  }
  // Only a tagged contact id confirms the lead reached the workflow. It is
  // returned so the browser reports generate_lead for real leads only.
  return {status: 200, body: {success: true, contactId}};
}
