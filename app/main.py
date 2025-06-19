from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send 200 OK response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Prepare response data
        data = {
            "status": "OK",
            "message": "Hello from EC2 Python server, This is a test"
        }

        # Send JSON response
        self.wfile.write(json.dumps(data).encode('utf-8'))

# Start the server
def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8000):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
