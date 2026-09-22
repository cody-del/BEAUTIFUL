# Beautiful Blinds & Shades homepage

Static HTML/CSS/JavaScript homepage review. The visual reference is Naples Shutter's Bahama & Colonial page, using Beautiful Blinds & Shades branding.

Serve `dist/` locally with `python3 -m http.server 4317 --bind 127.0.0.1 --directory dist` from this folder. The homepage intentionally includes a noindex directive and a canonical to the client's existing domain. Do not replace the whole live website with this one-page review folder.

Source files:

- `dist/index.html`: homepage and metadata
- `dist/styles.css`: responsive styling
- `dist/script.js`: responsive dropdown navigation, click-to-play video, review carousel, and native form validation
- `dist/assets/`: original client assets and locally hosted Manrope heading font
- `SEO_NOTES.md`: ranking baseline, keyword ownership, and launch requirements
- `research/`: local source evidence and the Semrush baseline, excluded from the hosted artifact

The consultation card is a native four-field form modeled on the Naples project. It validates names, phone, and email locally, but this review build does not transmit or store contact details. Valid submissions show an explicit preview notice, never a success confirmation. Before launch, connect a server-side endpoint to Beautiful Blinds & Shades’ own CRM, add server validation and abuse protection, confirm the appropriate privacy policy, and verify delivery and the existing follow-up workflow. Never reuse another client’s credentials or expose a private CRM key in browser JavaScript. The former embedded form ID was zJjnT8CYHC8I93TcxC76. No live test leads have been sent.

## Service-area map

`dist/service-area-map.html` and `dist/service-area-map.js` render a lazy-loaded Leaflet map with OpenStreetMap tiles and visible attribution. The geographic polygon is an approximate trace of the client-supplied September 22 screenshot, not an administrative boundary. Its solid 3.5px brand-blue (#67b2e8) stroke has a white casing for contrast. Fit-to-boundary behavior preserves the full outline on desktop and mobile; scrolling the page does not zoom the map. The Google business listing remains linked below. Leaflet 1.9.4 is pinned with integrity hashes. Provider references: https://leafletjs.com/examples/quick-start/ and https://operations.osmfoundation.org/policies/tiles/.

## Review and media updates

The Google carousel contains five client-supplied reviews and shows four cards on desktop, with responsive layouts and manual navigation. Long reviews expand in place.

The video thumbnail is an authentic frame from the opening second (00:00.500) of David’s Wistia introduction, media ID `cfwf2ryb20`. The name and role appear below the video as a small black caption. The process-section background and the four product-category images are generated illustrations, not documented client installations.

## Responsive navigation and video playback

The full-width header contains custom Window Treatments and Services dropdowns on desktop. At 1000px and below it switches to a call button and expandable navigation menu. Mobile menu sections have large touch targets, close on selection or Escape, and scroll independently on short screens. Centered mobile content uses shared widths and alignment. Layout checks cover widths from 320px to 1920px.

The introduction uses native HTML video controls with inline mobile playback and `preload="none"`. It streams the original 720px-wide MP4 from the client’s Wistia delivery CDN after a user clicks Play, avoiding the blank third-party iframe. The existing video thumbnail and caption remain in place. A direct video link appears if playback fails.
