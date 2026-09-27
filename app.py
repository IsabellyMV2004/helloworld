from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloWorld(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(b"""
        <html>
            <head>
                <title>Hello World</title>
            </head>
            <body>
                <h1>Hello World!</h1>
                <p>Servidor Web funcionando na Oracle Cloud.</p>
            </body>
        </html>
        """)

server = HTTPServer(("127.0.0.1", 8000), HelloWorld)

print("Servidor iniciado na porta 8000")

server.serve_forever()
