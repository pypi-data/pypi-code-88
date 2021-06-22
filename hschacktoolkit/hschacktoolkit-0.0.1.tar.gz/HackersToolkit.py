# Use this to build all sorts of hacking applications, like Webcrawlers, Webbrutes, Trojans, and more!
import requests
import socket
import os
import threading


class Web:
    def __init__(self, url: str):
        self.url = url

    def crawl(self, url_list):
        if not os.path.exists(url_list):
            raise FileNotFoundError

        for line in open(url_list).readlines():
            response = requests.get(self.url + '/' + line.strip())

            if response:
                yield f"\nURL FOUND: {self.url}/{line.strip()}\n"

    def web_ping(self) -> int:
        ip = socket.gethostbyname(self.url)
        status = os.popen(f'ping -w {ip}')
        if status == 0:
            return 1
        else:
            return 0


