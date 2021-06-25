import socket
import ssl


class Socket(object):
    def __init__(self, host: str, port: int):
        if port == 443:
            self.socket = ssl.create_default_context().wrap_socket(
                socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=host
            )
        else:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.host = host
        self.port = port

    def connect(self):
        self.socket.connect((self.host, self.port))

    def send(self, data: bytes):
        self.socket.send(data)

    def receive(self, bufsize: int = 2048):
        return self.socket.recv(bufsize)

    def close(self):
        self.socket.close()
