# https://www.sciencedirect.com/science/article/pii/S1742287613000510
# https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjViPqBjrDxAhUGjhQKHe0SCN0QFjAAegQIAxAD&url=https%3A%2F%2Fwww.iacs.org.uk%2Fdownload%2F1871&usg=AOvVaw2AFrLs9fUAaCMTTwdPvqJq
import errno
import os
import socket
import threading
from pathlib import Path
import configparser
from .tools import *


class Vdr:

    config = configparser.ConfigParser()
    config.read('config.ini')

    def __init__(self, path="."):
        self.path = path + "/data"
        self.frame_filename = "000000"
        self.nmea_filename = "000000"
        self.voice_filename = "000000"
        self.connections = {}

        # Create tree structure of VDR if it is not already exists
        if not os.path.exists(path + "/data"):
            os.makedirs(path + "/data")
        if not os.path.exists(path + "/data/frame"):
            os.makedirs(path + "/data/frame")
        if not os.path.exists(path + "/data/nmea"):
            os.makedirs(path + "/data/nmea")
        if not os.path.exists(path + "/data/voice"):
            os.makedirs(path + "/data/voice")

    def add_connection(self, ip, port, key):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((ip, port))
        self.connections[key] = sock


class ReceivingFrame(threading.Thread):
    def __init__(self, vdr, key):
        threading.Thread.__init__(self)
        self.vdr = vdr
        self.key = key

    def run(self):
        while True:
            data = self.vdr.connections[self.key].recvfrom(1024)
            path = self.vdr.path + "/frame/" + self.vdr.frame_filename + ".bmp"
            print(self.vdr.frame_filename)
            while os.path.exists(path):
                self.vdr.frame_filename = update(self.vdr.frame_filename)
                path = self.vdr.path + "/frame/" + self.vdr.frame_filename + ".bmp.gz"
            if data[0] == b'start':
                f = open(self.vdr.path + "/frame/" + self.vdr.frame_filename + ".bmp.gz", 'wb')
                data = self.vdr.connections[self.key].recvfrom(8192)
                while data:
                    if data[0] == b'stop':
                        print("picture received")
                        f.close()
                        os.system("gunzip " + self.vdr.path + "/frame/" + self.vdr.frame_filename + ".bmp.gz")
                        break
                    else:
                        f.write(data[0])
                        data = self.vdr.connections[self.key].recvfrom(8192)


class ReceivingNmea(threading.Thread):
    def __init__(self, vdr, key):
        threading.Thread.__init__(self)
        self.key = key
        self.vdr = vdr

    def run(self):
        while True:
            data = self.vdr.connections[self.key].recvfrom(1024)
            print(self.key, ":", data)
            path = self.vdr.path + "/nmea/" + self.vdr.nmea_filename
            file = open(path, "a")
            file_size = Path(path).stat().st_size
            if file_size > int(self.vdr.config['nmea']['size']):
                self.vdr.nmea_filename = update(self.vdr.nmea_filename)
                file.close()
                file = open(path, "a")

            split_data = bytes.decode(data[0]).split(',')

            try:
                if split_data[1] == "safety_management_system":
                    safety(split_data, file)
            except IndexError:
                print(errno)
