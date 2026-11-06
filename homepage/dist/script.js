const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
const navTriggers = [...navigation.querySelectorAll('.nav-trigger')];
const compactNavigation = matchMedia('(max-width: 1000px)');
let hoverCloseTimer;

function closeDropdowns() {
  navTriggers.forEach((trigger) => {
    trigger.setAttribute('aria-expanded', 'false');
    document.getElementById(trigger.getAttribute('aria-controls')).hidden = true;
  });
}
function openDropdown(trigger) {
  clearTimeout(hoverCloseTimer);
  closeDropdowns();
  trigger.setAttribute('aria-expanded', 'true');
  document.getElementById(trigger.getAttribute('aria-controls')).hidden = false;
}
function setMenuOpen(expanded) {
  clearTimeout(hoverCloseTimer);
  menuButton.setAttribute('aria-expanded', String(expanded));
  menuButton.setAttribute('aria-label', expanded ? 'Close navigation menu' : 'Open navigation menu');
  navigation.classList.toggle('open', expanded);
  if (!expanded) closeDropdowns();
}
menuButton.addEventListener('click', () => {
  setMenuOpen(menuButton.getAttribute('aria-expanded') !== 'true');
});
navTriggers.forEach((trigger) => {
  trigger.addEventListener('click', (event) => {
    // A mouse click keeps the panel opened by hover; keyboard and touch toggle it.
    if (!compactNavigation.matches && event.detail > 0) openDropdown(trigger);
    else if (trigger.getAttribute('aria-expanded') === 'true') closeDropdowns();
    else openDropdown(trigger);
  });
  trigger.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowDown') {
      event.preventDefault();
      openDropdown(trigger);
      document.getElementById(trigger.getAttribute('aria-controls')).querySelector('a').focus();
    }
  });
  const group = trigger.closest('.nav-group');
  group.addEventListener('pointerenter', (event) => {
    if (!compactNavigation.matches && event.pointerType === 'mouse') openDropdown(trigger);
  });
  group.addEventListener('pointerleave', (event) => {
    if (!compactNavigation.matches && event.pointerType === 'mouse') {
      hoverCloseTimer = setTimeout(() => {
        if (!group.contains(document.activeElement)) closeDropdowns();
      }, 180);
    }
  });
});
navigation.addEventListener('click', (event) => {
  if (event.target.closest('a')) setMenuOpen(false);
});
document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  const expanded = navTriggers.find((trigger) => trigger.getAttribute('aria-expanded') === 'true');
  if (expanded) {
    closeDropdowns();
    expanded.focus();
  } else if (menuButton.getAttribute('aria-expanded') === 'true') {
    setMenuOpen(false);
    menuButton.focus();
  }
});
document.addEventListener('click', (event) => {
  if (!event.target.closest('.header')) setMenuOpen(false);
});
document.addEventListener('focusin', (event) => {
  if (!event.target.closest('.header')) setMenuOpen(false);
  else if (!event.target.closest('.nav-group')) closeDropdowns();
  else if (!compactNavigation.matches) {
    const currentGroup = event.target.closest('.nav-group');
    const otherExpanded = navTriggers.some((trigger) => trigger.getAttribute('aria-expanded') === 'true' && trigger.closest('.nav-group') !== currentGroup);
    if (otherExpanded) closeDropdowns();
  }
});
compactNavigation.addEventListener('change', () => setMenuOpen(false));
const videoButton = document.querySelector('#play-video');
const introductionVideo = document.querySelector('#video-player');
const videoError = document.querySelector('.video-error');
videoButton?.addEventListener('click', () => {
  introductionVideo.hidden = false;
  videoButton.hidden = true;
  introductionVideo.focus({preventScroll: true});
  introductionVideo.play().catch(() => {
    // Native controls remain available if the browser pauses automatic playback.
    if (introductionVideo.error) videoError.hidden = false;
  });
});
introductionVideo?.addEventListener('error', () => { videoError.hidden = false; });
introductionVideo?.addEventListener('playing', () => { videoError.hidden = true; });

// Consultation requests go to /api/consultation (netlify/functions/consultation.mjs),
// which adds the lead to Beautiful Blinds & Shades' GoHighLevel and tags it
// "website lead". Success is shown only after GHL confirms the lead.
const consultationForm = document.querySelector('#consultation-form');
const consultationFields = [...(consultationForm?.querySelectorAll('input[required]') || [])];
const formStatus = document.querySelector('#form-status');
const consultationSuccess = document.querySelector('#consultation-success');
const CALL_US = 'We couldn’t confirm your request. Please call (260) 222-6467 before submitting again.';
// netlify/lib/consultation.mjs refuses anything sent sooner than this after the page loads.
const MIN_FILL_MS = 3000;
let consultationPending = false;

function validateConsultationField(input) {
  const value = input.value.trim();
  let message = '';
  if (!value) {
    message = `Please enter your ${input.labels[0].textContent.toLowerCase()}.`;
  } else if (input.type === 'email' && input.validity.typeMismatch) {
    message = 'Please enter a valid email address.';
  } else if (input.type === 'tel' && !/^(1)?\d{10}$/.test(value.replace(/\D/g, ''))) {
    message = 'Please enter a 10-digit phone number.';
  }
  const error = document.getElementById(input.getAttribute('aria-describedby'));
  error.textContent = message;
  error.hidden = !message;
  input.setAttribute('aria-invalid', String(Boolean(message)));
  return !message;
}

// One GA4 generate_lead per lead GHL confirmed, sent to GA4 only. gtag exists on
// the production host alone (see the head of index.html). No name, email or phone
// goes to Google Analytics. Tracking must never hold up or break the form.
function reportLead() {
  try {
    if (typeof window.gtag === 'function') window.gtag('event', 'generate_lead', {send_to: 'G-TBE6JC5ZYG', form_name: 'website_consultation_form', page_path: location.pathname});
  } catch {
    // A blocked or broken tag skips the event; the lead is already in GHL.
  }
}

consultationFields.forEach((input) => {
  input.addEventListener('blur', () => {
    if (input.value || input.hasAttribute('aria-invalid')) validateConsultationField(input);
  });
  input.addEventListener('input', () => {
    formStatus.hidden = true;
    if (input.getAttribute('aria-invalid') === 'true') validateConsultationField(input);
  });
});

consultationForm?.addEventListener('submit', async (event) => {
  event.preventDefault();
  if (consultationPending) return;
  formStatus.hidden = true;
  const valid = consultationFields.map(validateConsultationField).every(Boolean);
  if (!valid) {
    consultationFields.find((input) => input.getAttribute('aria-invalid') === 'true').focus();
    return;
  }
  const button = consultationForm.querySelector('button[type="submit"]');
  const label = button.textContent;
  consultationPending = true;
  button.disabled = true;
  button.textContent = 'Sending your request…';
  consultationForm.setAttribute('aria-busy', 'true');
  try {
    // Autofill can be faster than the minimum; wait it out rather than have the lead refused.
    const wait = MIN_FILL_MS + 100 - performance.now();
    if (wait > 0) await new Promise((resolve) => setTimeout(resolve, wait));
    const payload = Object.fromEntries(new FormData(consultationForm));
    // FormData leaves an unticked box out and sends a ticked one as "on"; send a boolean.
    payload.smsOptIn = consultationForm.elements.smsOptIn?.checked === true;
    payload.elapsedMs = Math.round(performance.now());
    payload.page = location.pathname;
    const response = await fetch('/api/consultation', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(payload),
      // AbortSignal.timeout is missing before Safari 16; send without a timeout there rather than fail.
      signal: AbortSignal.timeout?.(20000),
    });
    const result = await response.json();
    if (!response.ok || result.success !== true) throw new Error(result.error || CALL_US);
    reportLead();
    consultationForm.hidden = true;
    consultationForm.reset();
    consultationSuccess.hidden = false;
    consultationSuccess.focus();
  } catch (error) {
    formStatus.textContent = error.name === 'TimeoutError' || error instanceof TypeError || error instanceof SyntaxError ? CALL_US : error.message;
    formStatus.hidden = false;
    formStatus.focus?.();
  } finally {
    consultationPending = false;
    button.disabled = false;
    button.textContent = label;
    consultationForm.removeAttribute('aria-busy');
  }
});
if (consultationForm) consultationForm.querySelector('button[type="submit"]').disabled = false;

// Static review text remains readable without JavaScript. Enhance with compact
// excerpts and manual navigation; reviews never advance while someone is reading.
const testimonials = document.querySelector('.testimonials');
const reviewTrack = document.querySelector('.testimonial-track');
if (testimonials && reviewTrack) {
const reviewCards = [...reviewTrack.children];
const previousReviews = document.querySelector('.testimonial-prev');
const nextReviews = document.querySelector('.testimonial-next');
testimonials.classList.add('enhanced');
previousReviews.hidden = false;
nextReviews.hidden = false;

function updateReviewControls() {
  previousReviews.disabled = reviewTrack.scrollLeft < 2;
  nextReviews.disabled = reviewTrack.scrollLeft >= reviewTrack.scrollWidth - reviewTrack.clientWidth - 2;
  reviewCards.forEach((card) => {
    const quote = card.querySelector('.testimonial-quote');
    const button = card.querySelector('.testimonial-more');
    button.hidden = !quote.classList.contains('is-expanded') && quote.scrollHeight <= quote.clientHeight + 1;
  });
}

function moveReviews(direction) {
  const step = reviewCards[1].offsetLeft - reviewCards[0].offsetLeft;
  const current = Math.round(reviewTrack.scrollLeft / step);
  const visibleCount = Math.max(1, Math.round((reviewTrack.clientWidth + 24) / step));
  const next = Math.max(0, Math.min(reviewCards.length - visibleCount, current + direction));
  reviewTrack.scrollTo({left: next * step, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth'});
  document.querySelector('.testimonial-status').textContent = `Reviews ${next + 1} to ${Math.min(next + visibleCount, reviewCards.length)} of ${reviewCards.length}`;
}

previousReviews.addEventListener('click', () => moveReviews(-1));
nextReviews.addEventListener('click', () => moveReviews(1));
reviewTrack.addEventListener('scroll', updateReviewControls, {passive: true});
reviewTrack.addEventListener('keydown', (event) => {
  if (event.target === reviewTrack && ['ArrowLeft', 'ArrowRight'].includes(event.key)) {
    event.preventDefault();
    moveReviews(event.key === 'ArrowRight' ? 1 : -1);
  }
});
reviewCards.forEach((card) => {
  const button = card.querySelector('.testimonial-more');
  button.addEventListener('click', () => {
    const expanded = card.querySelector('.testimonial-quote').classList.toggle('is-expanded');
    button.setAttribute('aria-expanded', String(expanded));
    button.textContent = expanded ? 'Read less' : 'Read more';
    button.setAttribute('aria-label', `${expanded ? 'Read less' : 'Read more'} of ${card.querySelector('.testimonial-name').textContent}'s review`);
  });
});
new ResizeObserver(updateReviewControls).observe(reviewTrack);
updateReviewControls();

}
