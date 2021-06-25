from .sockets import Socket

from urllib.parse import urlparse


class SocketRequests(object):
    def __init__(self, url: str, headers: list = None):
        self.url = urlparse(url)
        self.headers = headers

        self.host = self.url.netloc
        self.port = 443 if self.url.scheme == "https" else 80
        self.path = self.url.path

        self.socket = Socket(self.host, self.port)
        self.socket.connect()

        self.text = None
        self.content = None
        self.status_code = None

    def get(self):
        return self.send_request("GET")

    def put(self):
        return self.send_request("PUT")

    def send_request(self, method: str):
        data = [
            f"{method} {self.path} HTTP/1.1",
            f"Host: {self.host}"
        ]

        if self.headers is not None:
            data += self.headers

        data.append("\r\n")

        data = "\r\n".join(data)

        self.socket.send(bytes(data, encoding="utf-8"))

        content = self.socket.receive()

        self.text = content.decode()
        self.content = content
        self.status_code = int(content[9:12])

        self.socket.close()
