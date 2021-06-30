from l0n0lnet.tcp import base_client, base_server
from l0n0lnet.tcp import session_read_size, close_tcp, client_read_size
from l0n0lnet.stream_parser import stream_parser
from l0n0lnet.utils import call_after
from l0n0lnet.confuse_tcp import confuse_client, confuse_server, confuse_session
from struct import pack, unpack
from copy import deepcopy
from enum import IntEnum
import time


class proxy_cmd(IntEnum):
    connect = 1
    close = 2
    data = 3
    start_server = 4
    regist_to_server = 5


class reverse_server_session(confuse_session):
    def set_target_port(self, port):
        self.target_port = port

    def get_target_port(self):
        if not hasattr(self, "target_port"):
            return
        return self.target_port


class reverse_server_server(base_server):
    def __init__(self, ip: bytes, port: int, contol_dession: reverse_server_session):
        super().__init__(ip, port)
        self.local_src_session_map = {}
        self.src_local_ip_map = {}
        self.local_msg_cache = {}
        self.control_session = contol_dession

    def on_session_connected(self, session_id):
        if not self.control_session:
            return
        self.control_session.send_cmd(
            proxy_cmd.connect, pack("!I", session_id))

    def on_session_disconnected(self, session_id):
        if not self.control_session:
            return
        if self.local_src_session_map.get(session_id):
            self.control_session.send_cmd(
                proxy_cmd.close, pack("!I", session_id))
        self.remove_cache(session_id)

    def on_session_read(self, session_id, data, size):
        self.send_msg_to_src(session_id, data)

    def send_msg_to_src(self, session_id, data):
        src_session: reverse_server_session = self.local_src_session_map.get(
            session_id)
        if not src_session:
            self.local_msg_cache[session_id] = self.local_msg_cache.get(session_id) or [
            ]
            self.local_msg_cache[session_id].append(data)
            return
        src_session.send_cmd(proxy_cmd.data, data)

    def regist_session_to_server(self, session_id: int, session: reverse_server_session):
        self.local_src_session_map[session_id] = session
        self.src_local_ip_map[session.tcp_id] = session_id
        cache_msgs = self.local_msg_cache.get(session_id)
        if not cache_msgs:
            return
        for msg in cache_msgs:
            session.send_cmd(proxy_cmd.data, msg)

    def on_src_session_disconnected(self, session: reverse_server_session):
        local_session_id = self.src_local_ip_map.get(session.tcp_id)
        if not local_session_id:
            return
        del self.src_local_ip_map[local_session_id]
        def cb():
            if self.src_local_ip_map.get(session.tcp_id):
                return
            close_tcp(local_session_id)
        call_after(3000, cb)

    def remove_cache(self, session_id):
        if self.local_msg_cache.get(session_id):
            del self.local_msg_cache[session_id]

        session = self.local_src_session_map.get(session_id)
        if session:
            del self.local_src_session_map[session_id]
            if self.src_local_ip_map.get(session.tcp_id):
                del self.src_local_ip_map[session.tcp_id]

    def on_get_response(self, session, data):
        local_session_id = self.src_local_ip_map.get(session.tcp_id)
        if not local_session_id:
            close_tcp(session.tcp_id)
            return
        self.send_msg(local_session_id, data)


class reverse_server(confuse_server):
    def __init__(self, ip: bytes, port: int, keys: list):
        super().__init__(ip, port, keys, reverse_server_session)
        self.servers = {}

    def on_session_disconnected(self, session_id):
        session: reverse_server_session = self.sessions[session_id]
        target_port = session.get_target_port()
        server: reverse_server_server = self.servers.get(target_port)
        if server:
            if server.control_session.tcp_id == session_id:
                print(f"Closing server on port {target_port}!")
                server.control_session = None
                server.close()
                del self.servers[target_port]
            else:
                print("Src session disconnected.", session_id)
                server.on_src_session_disconnected(session)
        super().on_session_disconnected(session_id)

    def on_cmd(self, session_id, cmd, data):
        session: reverse_server_session = self.sessions.get(session_id)
        if not session:
            return
        if cmd == proxy_cmd.start_server:
            self.start_server(session, cmd, data)
        elif cmd == proxy_cmd.regist_to_server:
            self.regist_to_server(session, cmd, data)
        elif cmd == proxy_cmd.data:
            self.on_get_response(session, data)

    def start_server(self, session, cmd, data):
        target_port = unpack("!I", data)[0]

        session.set_target_port(target_port)

        server = reverse_server_server(b'0.0.0.0', target_port, session)
        if server.id == 0:
            print(f"Open server on port {target_port} failed!")
            close_tcp(session.tcp_id)
            return

        print(f"Open server on port {target_port} success.")
        self.servers[target_port] = server

    def regist_to_server(self, session, cmd, data):
        target_session_id, server_port = unpack("!II", data)
        server: reverse_server_server = self.servers.get(server_port)
        if not server:
            close_tcp(session.tcp_id)
            return
        session.set_target_port(server_port)
        server.regist_session_to_server(target_session_id, session)

    def on_get_response(self, session, data):
        server: reverse_server_server = self.servers.get(
            session.get_target_port())
        if not server:
            close_tcp(session.tcp_id)
            return
        server.on_get_response(session, data)


class reverse_client(confuse_client):
    def __init__(self, ip: bytes, port: int, keys: list, remote_port: int, tip: bytes, tport: int):
        self.remote_port = remote_port
        self.tip = tip
        self.tport = tport
        self.clients = {}
        super().__init__(ip, port, keys)

    def reconnect(self):
        for client in self.clients.values():
            client.close()
        super().reconnect()

    def on_connected(self):
        super().on_connected()
        self.send_cmd(proxy_cmd.start_server, pack("!I", self.remote_port))
        print("Server connected")

    def on_connect_failed(self):
        call_after(1000, self.reconnect)
        print("Connect to Server Failed! Reconnect in 1 second.")

    def on_disconnected(self):
        call_after(1000, self.reconnect)
        print("DisConnect from server! Reconnect in 1 second.")

    def on_cmd(self, tcp_id, cmd, data):
        if cmd == proxy_cmd.connect:
            print("Remote sesion connected.")
            self.remote_session_connected(data)
        elif cmd == proxy_cmd.close:
            print("Remote sesion disconnected.")
            self.remote_session_disconnected(data)

    def remote_session_connected(self, data):
        remote_session_id = unpack("!I", data)[0]
        client = reverse_client_client(self, remote_session_id)
        self.clients[remote_session_id] = client

    def remote_session_disconnected(self, data):
        remote_session_id = unpack("!I", data)[0]
        client: reverse_client_client = self.clients.get(remote_session_id)
        if not client:
            return
        client.close()
        del self.clients[remote_session_id]

    def on_server_session_disconnected(self, remote_session_id):
        self.send_cmd(proxy_cmd.close, pack("!I", remote_session_id))
        if self.clients.get(remote_session_id):
            del self.clients[remote_session_id]


class reverse_client_client(base_client):
    def __init__(self, owner: reverse_client, remote_session_id):
        self.owner = owner
        self.remote_session_id = remote_session_id
        super().__init__(owner.tip, owner.tport)

    def on_connected(self):
        self.trans_client = reverse_trans_client(self,
                                                 self.owner.ip,
                                                 self.owner.port,
                                                 self.owner.keys,
                                                 self.remote_session_id)

    def on_connect_failed(self):
        if hasattr(self, "trans_client"):
            self.trans_client.close()
        self.owner.on_server_session_disconnected(self.remote_session_id)

    def on_disconnected(self):
        if hasattr(self, "trans_client"):
            self.trans_client.close()
        self.owner.on_server_session_disconnected(self.remote_session_id)

    def on_read(self, data, size):
        self.trans_client.send_cmd(proxy_cmd.data, data)

    def on_trans_client_connected(self):
        self.trans_client.send_cmd(proxy_cmd.regist_to_server,
                                   pack("!II", self.remote_session_id, self.owner.remote_port))

    def on_trans_client_disconnected(self):
        self.close()

    def on_trans_client_request(self, data):
        self.send_msg(data)


class reverse_trans_client(confuse_client):
    def __init__(self, owner: reverse_client_client, ip, port, keys, remote_session_id):
        super().__init__(ip, port, keys)
        self.owner = owner
        self.remote_session_id = remote_session_id
        self.need_reconnect = True
        self.reconnect_count = 0

    def on_connected(self):
        print(
            f"Connected to local {self.owner.owner.tip}:{self.owner.owner.tport}", self.remote_session_id)
        super().on_connected()
        self.owner.on_trans_client_connected()

    def on_connect_failed(self):
        self.owner.on_trans_client_disconnected()

    def on_disconnected(self):
        if not self.need_reconnect:
            self.on_disconnected_real()
            return

        self.reconnect_count += 1
        if self.reconnect_count > 5:
            self.on_disconnected_real()
            return

        print("Trans client reconnecting .. ", self.remote_session_id)
        self.reconnect()

    def on_disconnected_real(self):
        self.need_reconnect = True
        print(
            f"Disconnected from local {self.owner.owner.tip}:{self.owner.owner.tport}", self.remote_session_id)
        self.owner.on_trans_client_disconnected()

    def on_cmd(self, id, cmd, data):
        if cmd == proxy_cmd.data:
            self.owner.on_trans_client_request(data)

    def close(self):
        self.need_reconnect = False
        super().close()
