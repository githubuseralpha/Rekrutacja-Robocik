import requests
import time
import math


class Receiver:
    def __init__(self):
        self.url = 'http://localhost:5000'
        self.msg = ''
        self.start = 0
        [self.old_x, self.old_y, self.old_z] = [0, 0, 0]

    @staticmethod
    def calculate_speed(x, y, z, t):
        return math.sqrt(x * x + y * y + z * z) / t

    @staticmethod
    def read_coordinates(msg):
        [x, y, z] = msg.split(", ")
        return float(x), float(y), float(z)

    def run(self):
        while self.msg != "DISCONNECT":
            try:
                x = requests.post(self.url, '')
                if x.text == "START" and self.msg != x.text:
                    self.msg = x.text
                    self.start = time.time()
                elif self.msg != x.text:
                    stop = time.time()
                    self.msg = x.text
                    [x, y, z] = self.read_coordinates(self.msg)
                    x_change = x - self.old_x
                    y_change = y - self.old_y
                    z_change = z - self.old_z
                    t = stop - self.start
                    speed = self.calculate_speed(x_change, y_change, z_change, t)
                    print(f'v = {speed}')
                    [self.old_x, self.old_y, self.old_z] = [x, y, z]
                    self.start = time.time()
            except:
                print("Nie połączono")


rec = Receiver()
rec.run()
