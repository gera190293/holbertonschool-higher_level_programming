#!/usr/bin/python3

"""Module for RESTful API exercises"""
import http.server
import json

class BasicServer(http.server.BaseHTTPRequestHandler):
    """Class for a basic HTTP server management"""

    def do_GET(self):
        """Method to serve a sample JSON data
        when the endpoint /data is accessed"""

        if self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        else:
            self.send_error(404, 'Endpoint not found')

def run_server():
    """Function to run the server"""
    address = ('', 8000)
    server = http.server.HTTPServer(address, BasicServer)
    print('Server running on localhost:8000')
    server.serve_forever()

if __name__ == '__main__':
    run_server()
