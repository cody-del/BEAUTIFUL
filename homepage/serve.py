"""Serve dist/ locally the way Netlify serves it.

Run: python3 homepage/serve.py, then open http://127.0.0.1:4317/
/products/blinds serves dist/products/blinds.html, /products/blinds/ 301s to
/products/blinds, and a missing page gets dist/404.html with a 404 status.
_redirects rules are not applied locally.
"""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote, urlsplit
import argparse
from routes import DIST, page_file


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.dispatch(super().do_GET)

    def do_HEAD(self):
        self.dispatch(super().do_HEAD)

    def dispatch(self, serve):
        url = urlsplit(self.path)
        path = unquote(url.path)
        query = '?' + url.query if url.query else ''
        if path != '/' and path.endswith('/') and page_file(path).is_file():
            self.send_response(301)
            self.send_header('Location', path.rstrip('/') + query)
            self.end_headers()
        elif (DIST / path.lstrip('/')).is_file():
            serve()
        elif page_file(path).is_file():
            self.path = '/' + page_file(path).relative_to(DIST).as_posix() + query
            serve()
        else:
            body = (DIST / '404.html').read_bytes()
            self.send_response(404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            if self.command == 'GET':
                self.wfile.write(body)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=4317)
    args = parser.parse_args()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), partial(Handler, directory=str(DIST)))
    print(f'Serving {DIST} at http://127.0.0.1:{args.port}/')
    server.serve_forever()
