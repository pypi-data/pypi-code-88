from l0n0lnet.tcp import base_server, base_client, close_tcp
from l0n0lnet.tcp import session_read_until, session_read_size
from l0n0lnet.utils import get_address
import re


class http_tunel_server(base_server):
    clients = {}

    def on_session_connected(self, session_id):
        session_read_until(session_id, b'\r\n\r\n')

    def on_session_disconnected(self, session_id):
        client: http_tunel_client = self.clients.get(session_id)
        if not client:
            return
        client.close()

    def on_session_read(self, session_id: int, data: bytes, size: int):
        print(data)
        client: http_tunel_client = self.clients.get(session_id)
        if not client:
            self.connect_remote(session_id, data)
            return
        client.on_get_request(data)

    def connect_remote(self, session_id, data):
        ms = re.findall(rb'(\w+): (.*)\r\n', data)
        values = {}
        for m in ms:
            values[m[0]] = m[1]
        host = values.get(b"Host")
        name_port = host.split(b':')
        if len(name_port) > 1:
            name = name_port[0]
            port = int(name_port[1])
        else:
            name = host
            port = 80

        def on_resolve(name, address):
            if not address:
                close_tcp(session_id)
                return
            self.clients[session_id] = http_tunel_client(
                self, session_id, address, port)

        if not get_address(name, on_resolve):
            print("xxxxxxxx")
            close_tcp(session_id)

    def on_client_connected(self, session_id):
        self.send_msg(
            session_id, b'HTTP/1.1 200 Connection Established\r\n\r\n')
        session_read_size(session_id, 0)

    def on_client_disconnected(self, session_id):
        if self.clients.get(session_id):
            del self.clients[session_id]
        close_tcp(session_id)

    def on_client_read(self, session_id, data):
        self.send_msg(session_id, data)


class http_tunel_client(base_client):
    def __init__(self, owner: http_tunel_server, session_id: int, tip: bytes, tport: int):
        self.owner = owner
        self.session_id = session_id
        super().__init__(tip, tport)
        self.connected = False
        self.send_cache = []

    def on_connected(self):
        self.connected = True
        for msg in self.send_cache:
            self.send_msg(msg)
        self.send_cache.clear()
        self.owner.on_client_connected(self.session_id)

    def on_connect_failed(self):
        self.owner.on_client_disconnected(self.session_id)

    def on_disconnected(self):
        self.owner.on_client_disconnected(self.session_id)

    def on_read(self, data, size):
        self.owner.on_client_read(self.session_id, data)

    def on_get_request(self, data):
        if not self.connected:
            self.send_cache.append(data)
            return
        self.send_msg(data)
