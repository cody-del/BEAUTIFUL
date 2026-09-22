const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
menuButton.addEventListener('click', () => {
  const expanded = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(expanded));
  navigation.classList.toggle('open', expanded);
});
navigation.addEventListener('click', (event) => {
  if (event.target.closest('a')) {
    menuButton.setAttribute('aria-expanded', 'false');
    navigation.classList.remove('open');
  }
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
    menuButton.setAttribute('aria-expanded', 'false');
    navigation.classList.remove('open');
    menuButton.focus();
  }
});
document.querySelector('#play-video').addEventListener('click', (event) => {
  const player = document.querySelector('#video-player');
  const frame = document.createElement('iframe');
  frame.src = 'https://fast.wistia.net/embed/iframe/cfwf2ryb20?autoPlay=true';
  frame.title = 'Meet David Fear, owner of Beautiful Blinds and Shades';
  frame.allow = 'autoplay; fullscreen; picture-in-picture';
  frame.allowFullscreen = true;
  player.append(frame);
  player.hidden = false;
  event.currentTarget.hidden = true;
  frame.focus();
});

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
