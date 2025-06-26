from http.server import SimpleHTTPRequestHandler, HTTPServer

def run_server(port=8000):
    """Run a simple HTTP server with directory listing."""
    server_address = ('', port)
    handler = SimpleHTTPRequestHandler
    httpd = HTTPServer(server_address, handler)
    print(f"Serving on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
