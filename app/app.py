"""

Порт 8000, реализовано 3 метода:

GET /hostname - отдает имя хоста, на котором запущено приложение.
GET /author - возвращает значение переменной окружения $AUTHOR
GET /id - возвращает значение переменной окружения $UUID

"""


from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import os
import time

host = '0.0.0.0'
port = int(os.getenv("PORT"))

hostname = socket.gethostname()
author = os.getenv("AUTHOR")
uuid = os.getenv("UUID")

class simpleServerHandler(BaseHTTPRequestHandler):

    # Метод отдает имя хоста, на котором запущено приложение
    def req_hostname(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(f"Hostname: {hostname}\n".encode("utf-8"))


    # Метод отдает значение переменной окружения $AUTHOR
    def req_author(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(f"Author: {author}\n".encode("utf-8"))


    # Метод отдает значение переменной окружения $UUID
    def req_id(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(f"$UUID: {uuid}\n".encode("utf-8"))


    # Метод нужен для реализации readiness пробы.
    def req_health(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("\n\n".encode("utf-8"))

    
    # Дефолтный ответ на любой другой запрос 
    def req_root(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("\n\n".encode("utf-8"))


    def do_GET(self):

        if self.path == '/hostname':
            self.req_hostname()
        elif self.path == '/author':
            self.req_author()
        elif self.path == '/id':
            self.req_id()
        elif self.path == '/health':
            self.req_health()
        else:
            self.req_root()



print(time.asctime(), "Server Starting - %s:%s" % (host, port))

server = HTTPServer((host, port), simpleServerHandler)

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()

print(time.asctime(), "Server Stops - %s:%s" % (host, port))