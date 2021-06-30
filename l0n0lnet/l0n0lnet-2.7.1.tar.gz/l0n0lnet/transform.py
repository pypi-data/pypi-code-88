from l0n0lnet.tcp import base_client, base_server
from l0n0lnet.tcp import session_read_size, close_tcp, get_ip_port
from l0n0lnet.stream_parser import stream_parser
from struct import pack, unpack
from copy import deepcopy
from random import randint


class trans_server(base_server):
    def __init__(self, ip: bytes, port: int, tip: bytes, tport: int, keys: list, role: str):
        super().__init__(ip, port)
        self.tip = tip
        self.tport = tport
        self.clients = {}
        self.role = role
        self.parsers = []
        for key in keys:
            parser = stream_parser()
            parser.set_password(key)
            self.parsers.append(parser)

    def on_session_connected(self, session_id):
        if self.role == "client":
            self.client_role_session_connected(session_id)
        elif self.role == "server":
            self.server_role_session_connected(session_id)

    def on_session_disconnected(self, session_id):
        if self.role == "client":
            self.client_role_session_disconnected(session_id)
        elif self.role == "server":
            self.server_role_session_disconnected(session_id)

    def on_session_read(self, session_id, data, size):
        if self.role == "client":
            self.client_role_session_read(session_id, data)
        elif self.role == "server":
            self.server_role_session_read(session_id, data)

    def on_response(self, session_id, data):
        if self.role == "client":
            self.client_role_session_response(session_id, data)
        elif self.role == "server":
            self.server_role_session_response(session_id, data)

    def on_client_disconnected(self, session_id):
        del self.clients[session_id]
        close_tcp(session_id)

    def on_client_connect_failed(self, session_id):
        del self.clients[session_id]
        close_tcp(session_id)

    def server_role_session_connected(self, session_id):
        self.clients[session_id] = {"state": "send_pass"}
        session_read_size(session_id, 2)

    def client_role_session_connected(self, session_id):
        index = randint(0, len(self.parsers) - 1)
        session_data = {
            "state": "send_pass",
            "parser": self.parsers[index],
            "client": trans_server_client(self, self.tip, self.tport, session_id)
        }
        self.clients[session_id] = session_data
        session_data["client"].on_request(pack("!H", index))

    def server_role_session_disconnected(self, session_id):
        session_data = self.clients.get(session_id)
        if not session_data:
            return
        client = session_data.get("client")
        if not client:
            return
        client.on_session_disconnected()

    def client_role_session_disconnected(self, session_id):
        session_data = self.clients.get(session_id)
        if not session_data:
            return
        client = session_data.get("client")
        if not client:
            return
        client.on_session_disconnected()

    def server_role_session_read(self, session_id, data):
        session_data = self.clients.get(session_id)
        if not session_data:
            return
        if session_data["state"] == "send_pass":
            index = unpack("!H", data)[0]
            session_data['parser'] = self.parsers[index]
            session_data["client"] = trans_server_client(
                self, self.tip, self.tport, session_id)
            session_read_size(session_id, 0)
            session_data["state"] = "trans_data"
        elif session_data["state"] == "trans_data":
            session_data["parser"].decrypt(data)
            session_data["client"].on_request(data)

    def client_role_session_read(self, session_id, data):
        session_data = self.clients.get(session_id)
        if not session_data:
            return
        session_data["parser"].encrypt(data)
        session_data["client"].on_request(data)

    def server_role_session_response(self, session_id, data):
        session_data = self.clients.get(session_id)
        if not session_data:
            return
        session_data["parser"].encrypt(data)
        self.send_msg(session_id, data)

    def client_role_session_response(self, session_id, data):
        session_data = self.clients.get(session_id)
        if not session_data:
            return
        session_data["parser"].decrypt(data)
        self.send_msg(session_id, data)


class trans_server_client(base_client):
    def __init__(self, owner: trans_server, ip: bytes, port: int, session_id: int):
        super().__init__(ip, port)
        self.owner = owner
        self.session_id = session_id
        self.connected = False
        self.cache = b''

    def on_connected(self):
        self.connected = True
        if len(self.cache) > 0:
            self.send_msg(self.cache)
            self.cache = b''

    def on_connect_failed(self):
        if not self.owner:
            return
        self.owner.on_client_connect_failed(self.session_id)

    def on_disconnected(self):
        if not self.owner:
            return
        self.owner.on_client_disconnected(self.session_id)

    def on_read(self, data, size):
        if not self.owner:
            return
        self.owner.on_response(self.session_id, data)

    def on_request(self, data):
        if not self.connected:
            self.cache += data
            return
        self.send_msg(data)

    def on_session_disconnected(self):
        self.close()
        self.owner = None
        self.session_id = None
