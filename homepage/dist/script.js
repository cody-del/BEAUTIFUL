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
videoButton.addEventListener('click', () => {
  introductionVideo.hidden = false;
  videoButton.hidden = true;
  introductionVideo.focus({preventScroll: true});
  introductionVideo.play().catch(() => {
    // Native controls remain available if the browser pauses automatic playback.
    if (introductionVideo.error) videoError.hidden = false;
  });
});
introductionVideo.addEventListener('error', () => { videoError.hidden = false; });
introductionVideo.addEventListener('playing', () => { videoError.hidden = true; });

// The review build intentionally has no lead-delivery endpoint. Connect a
// server-side handler for this client's CRM before enabling production delivery.
const consultationForm = document.querySelector('#consultation-form');
const consultationFields = [...consultationForm.querySelectorAll('input[required]')];
const formStatus = document.querySelector('#form-status');

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

consultationFields.forEach((input) => {
  input.addEventListener('blur', () => {
    if (input.value || input.hasAttribute('aria-invalid')) validateConsultationField(input);
  });
  input.addEventListener('input', () => {
    formStatus.hidden = true;
    if (input.getAttribute('aria-invalid') === 'true') validateConsultationField(input);
  });
});

consultationForm.addEventListener('submit', (event) => {
  event.preventDefault();
  formStatus.hidden = true;
  const valid = consultationFields.map(validateConsultationField).every(Boolean);
  if (!valid) {
    consultationFields.find((input) => input.getAttribute('aria-invalid') === 'true').focus();
    return;
  }
  // Never show a success message or discard details without confirmed delivery.
  formStatus.innerHTML = 'This preview does not send requests yet. Your details have not been sent. To book a consultation, call <a href="tel:+12602226467">(260) 222-6467</a>.';
  formStatus.hidden = false;
});
consultationForm.querySelector('button[type="submit"]').disabled = false;

// Static review text remains readable without JavaScript. Enhance with compact
// excerpts and manual navigation; reviews never advance while someone is reading.
const testimonials = document.querySelector('.testimonials');
const reviewTrack = document.querySelector('.testimonial-track');
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
