// Keeps every host except the real domain out of search: the netlify.app
// address, deploy previews and branch deploys get "X-Robots-Tag: noindex" and a
// robots.txt that disallows everything. On www.beautifulblindsandshades.com the
// site is served untouched, so pointing the domain here at launch needs no code
// change and the review copies can never compete with it in Google.
export const PRODUCTION_HOST = 'www.beautifulblindsandshades.com';
export const BLOCKED_ROBOTS = 'User-agent: *\nDisallow: /\n';

export default async function searchBlock(request, context) {
  const url = new URL(request.url);
  if (url.hostname === PRODUCTION_HOST) return context.next();
  if (url.pathname === '/robots.txt') {
    return new Response(BLOCKED_ROBOTS, {headers: {'Content-Type': 'text/plain; charset=utf-8', 'X-Robots-Tag': 'noindex, nofollow'}});
  }
  const response = await context.next();
  const blocked = new Response(response.body, response);
  blocked.headers.set('X-Robots-Tag', 'noindex, nofollow');
  return blocked;
}

export const config = {path: '/*', excludedPath: ['/assets/*', '/api/*']};
