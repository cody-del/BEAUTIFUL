/* Native scrolling keeps every guide and link available without JavaScript. */
document.querySelectorAll('.guide-carousel').forEach(carousel => {
  const track = carousel.querySelector('.guide-track');
  const cards = [...track.querySelectorAll('.guide-card')];
  const controls = carousel.querySelector('.guide-controls');
  const previous = carousel.querySelector('.guide-prev');
  const next = carousel.querySelector('.guide-next');
  const count = carousel.querySelector('.guide-count');
  if (!cards.length) return;
  carousel.classList.add('enhanced');
  controls.hidden = false;
  const step = () => cards.length > 1 ? cards[1].getBoundingClientRect().left - cards[0].getBoundingClientRect().left : track.clientWidth;
  const update = () => {
    const end = track.scrollWidth - track.clientWidth;
    previous.disabled = track.scrollLeft <= 2;
    next.disabled = track.scrollLeft >= end - 2;
    const bounds = track.getBoundingClientRect();
    const visible = cards.map((card, index) => ({index, rect:card.getBoundingClientRect()}))
      .filter(({rect}) => rect.right > bounds.left + rect.width / 2 && rect.left < bounds.right - rect.width / 2);
    const first = (visible[0]?.index ?? 0) + 1;
    const last = (visible[visible.length - 1]?.index ?? 0) + 1;
    count.textContent = first === last ? `Guide ${first} of ${cards.length}` : `Guides ${first}–${last} of ${cards.length}`;
  };
  const move = direction => {
    const index = Math.max(0, Math.min(cards.length - 1, Math.round(track.scrollLeft / step()) + direction));
    track.scrollTo({left:index * step() + 1,behavior:'instant'});
    update();
  };
  previous.addEventListener('click', () => move(-1));
  next.addEventListener('click', () => move(1));
  track.addEventListener('keydown', event => {
    if (event.target !== track || !['ArrowLeft','ArrowRight','Home','End'].includes(event.key)) return;
    event.preventDefault();
    if (event.key === 'ArrowLeft') move(-1);
    if (event.key === 'ArrowRight') move(1);
    if (event.key === 'Home') track.scrollTo({left:0,behavior:'instant'});
    if (event.key === 'End') track.scrollTo({left:track.scrollWidth,behavior:'instant'});
  });
  let frame;
  track.addEventListener('scroll', () => {cancelAnimationFrame(frame);frame = requestAnimationFrame(update);}, {passive:true});
  new ResizeObserver(update).observe(track);
  update();
});
