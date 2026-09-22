/* Approximate geographic trace of the boundary in the client's Sept. 22
   reference screenshot. Keep this polygon in geographic coordinates so it
   follows the map while visitors pan, zoom, or resize the page. */
if (window.L) {
  const map = L.map('map', {
    scrollWheelZoom: false,
    zoomControl: false,
    zoomSnap: 0.1,
    minZoom: 7,
    maxZoom: 15
  });
  L.control.zoom({ position: 'bottomright' }).addTo(map);

  const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap contributors</a>'
  }).addTo(map);
  const fallback = document.querySelector('#map-fallback');
  tiles.on('tileload', () => { fallback.hidden = true; });

  const boundary = [
    [41.678, -84.995],
    [41.639, -84.971],
    [41.143, -84.836],
    [41.031, -84.839],
    [40.963, -84.859],
    [40.723, -85.148],
    [40.715, -85.205],
    [41.212, -85.883],
    [41.244, -85.895],
    [41.271, -85.888],
    [41.448, -85.760]
  ];
  // A white casing keeps the blue border visible over roads and town labels.
  L.polygon(boundary, { color: '#fff', weight: 7, opacity: 0.9, fill: false, interactive: false }).addTo(map);
  const serviceArea = L.polygon(boundary, {
    color: '#67b2e8', weight: 3.5, opacity: 1,
    fillColor: '#bfdd9f', fillOpacity: 0.10,
    lineJoin: 'round', interactive: false
  }).addTo(map);

  function showServiceArea() {
    map.invalidateSize({ pan: false });
    map.fitBounds(serviceArea.getBounds(), {
      paddingTopLeft: [24, 86], paddingBottomRight: [24, 48], animate: false
    });
  }
  const ResetControl = L.Control.extend({
    options: { position: 'bottomleft' },
    onAdd() {
      const wrapper = L.DomUtil.create('div', 'leaflet-bar');
      const button = L.DomUtil.create('button', 'map-reset', wrapper);
      button.type = 'button';
      button.textContent = 'Show service area';
      L.DomEvent.disableClickPropagation(wrapper);
      L.DomEvent.on(button, 'click', showServiceArea);
      return wrapper;
    }
  });
  new ResetControl().addTo(map);
  showServiceArea();
  new ResizeObserver(showServiceArea).observe(document.querySelector('#map'));
}
