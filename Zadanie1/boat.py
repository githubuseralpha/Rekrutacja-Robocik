from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import random


class Server(BaseHTTPRequestHandler):
    def encode_msg(self, message):
        return message.encode("utf8")

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_POST(self):
        self._set_headers()
        self.wfile.write(self.encode_msg(boat.message))


class Boat:
    def __init__(self, n, t):
        self.n = n
        self.t = t
        self.message = ""
        self.isFirst = True

    @staticmethod
    def generate_coordinates():
        x = random.random()*1000 - 500
        y = random.random()*1000 - 500
        z = random.random()*1000 - 500
        return f"{x}, {y}, {z}"

    def update_message(self):
        if self.isFirst:
            self.message = "START"
            self.isFirst = False
            timer = threading.Timer(self.t, self.update_message)
            timer.start()
        elif self.n == -1:
            server.shutdown()
        elif self.n == 0:
            self.message = "DISCONNECT"
            self.n = self.n - 1
            timer = threading.Timer(10, self.update_message)
            timer.start()
        else:
            self.message = self.generate_coordinates()
            self.n = self.n - 1
            timer = threading.Timer(self.t, self.update_message)
            timer.start()


n = input("Ile razy łódź ma się przemieścić?(conajmniej 5)")
t = input("Co ile sekund losować nowe położenie łodzi? (preferowane wartości powyżej 10)")

if int(n) < 5 or int(t) <= 0:
    raise Exception("Wprowadzone dane nie spełniają warunków")

boat = Boat(int(n), int(t))
boat.update_message()

server = HTTPServer(('localhost', 5000), Server)
server.serve_forever()
