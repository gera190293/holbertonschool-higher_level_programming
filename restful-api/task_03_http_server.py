#!/usr/bin/python3

"""Module for RESTful API exercises"""
import http.server
import json


class Basic_server(http.server.BaseHTTPRequestHandler):
    """Class for a basic http server management"""
    def do_GET(self):
        """Method to serve a sample JSON data
        when the endpoint /data is accessed"""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
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
        else:
            self.send_error(404, 'Not Found')

def run_server():
    address = ('', 8000)
    server = http.server.HTTPServer(address, Basic_server)
    server.serve_forever()

if __name__ == '__main__':
    run_server()