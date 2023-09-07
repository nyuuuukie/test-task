"""

Веб-приложение на Python, слушает на порту 8000, в API которого реализовано 3 метода:

GET /hostname - отдает имя хоста, на котором запущено приложение.
GET /author - возвращает значение переменной окружения $AUTHOR
GET /id - возвращает значение переменной окружения $UUID

"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import os
import time

hostname = 'localhost'
port = 8000

class simpleServerHandler(BaseHTTPRequestHandler):

    def req_hostname(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        hostname = socket.gethostname()
        self.wfile.write(f"Hostname: {hostname}".encode("utf-8"))

    def req_author(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        author = os.getenv("AUTHOR")
        self.wfile.write(f"Author: {author}".encode("utf-8"))

    def req_id(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        uuid = os.getenv("UUID")
        self.wfile.write(f"$UUID: {uuid}".encode("utf-8"))

    def req_unknown(self):
        self.send_response(400, "Bad request")


    def do_GET(self):

        if self.path == '/hostname':
            self.req_hostname()
        elif self.path == '/author':
            self.req_author()
        elif self.path == '/id':
            self.req_id()
        else:
            self.req_unknown()



server = HTTPServer((hostname, port), simpleServerHandler)

print(time.asctime(), "Server Starts - %s:%s" % (hostname, port))

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostname, port))