import socket
import pyautogui
import time
import os
import configparser


class ScreenAgent:

    config = configparser.ConfigParser()
    config.read('config.ini')

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock = sock

    def send_screenshot(self):
        last_time = 0
        filename = "screenshot.bmp"
        while True:
            current_time = time.time()
            if current_time - last_time > int(self.config['frame']['frequency']):
                if not os.path.exists(filename):
                    pyautogui.screenshot(filename)
                    os.system("gzip " + filename)
                buf = 8192
                filename += ".gz"
                f = open(filename, 'rb')

                self.sock.sendto(b'start', (self.ip, self.port))
                data = f.read(buf)
                while data:
                    if self.sock.sendto(data, (self.ip, self.port)):
                        data = f.read(buf)
                        time.sleep(0.02)
                self.sock.sendto(b'stop', (self.ip, self.port))
                if os.path.exists(filename):
                    os.remove(filename)
                last_time = time.time()



