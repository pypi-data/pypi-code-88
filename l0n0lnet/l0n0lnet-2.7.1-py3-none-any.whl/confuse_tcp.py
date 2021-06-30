from l0n0lnet.tcp import base_client, base_server, close_tcp
from l0n0lnet.tcp import client_read_size, session_read_size, send_message
from l0n0lnet.stream_parser import stream_parser
from l0n0lnet.utils import call_after
from enum import IntEnum
from struct import pack, unpack
from random import randint

#   数据包定义
#   数据大小    命令    参数数据
#   4           4      数据大小


def pack_msg(cmd: int, data: bytes):
    data_len = len(data)
    return pack(f"!II{data_len}s", data_len, cmd, data)


def unpack_header(data: bytes):
    return unpack("!II", data)


_heart_msg = b'\x00\x00\x00\x00\x00\x00\x00\x00'


class confuse_state(IntEnum):
    read_key_index = 0
    read_header = 1
    read_data = 2
    read_max = 3


class confuse_session:
    def __init__(self, tcp_id: int, parsers: list, max_heart: int, on_cmd_cb, read_size_func, start_state):
        self.tcp_id = tcp_id
        self.parsers = parsers
        self.on_cmd = on_cmd_cb
        self.set_read_size = read_size_func
        self.heart = 0
        self.max_heart = max_heart
        self.set_start_state(start_state)
        self.send_cache = []

    def __del__(self):
        self.close()

    def set_start_state(self, start_state):
        self.state = start_state
        if start_state == confuse_state.read_key_index:
            self.set_read_size(self.tcp_id, 4)
        if start_state == confuse_state.read_header:
            self.set_read_size(self.tcp_id, 8)

    def parse(self, data):
        self.heart = 0
        if self.state == confuse_state.read_key_index:
            # 读取index
            index = unpack('!I', data)[0]
            if index < 0 or index >= len(self.parsers):
                close_tcp(self.tcp_id)
                return
            # 缓存parser
            self.parser: stream_parser = self.parsers[index]
            # 发送缓存数据
            self.send_cache_data()
            # 读取header
            self.set_read_size(self.tcp_id, 8)
            self.state = confuse_state.read_header
        elif self.state == confuse_state.read_header:
            # 解析包头
            data_len, cmd = unpack_header(data)
            # 无效指令
            if data_len == 0 and cmd == 0:
                return
            # 缓存指令
            self.cmd = cmd
            # 读取数据
            self.set_read_size(self.tcp_id, data_len)
            self.state = confuse_state.read_data
        elif self.state == confuse_state.read_data:
            # 解密数据
            self.parser.decrypt(data)
            # 调用回调
            self.on_cmd(self.tcp_id, self.cmd, data)
            # 继续读取header
            self.set_read_size(self.tcp_id, 8)
            self.state = confuse_state.read_header

    def send_parser_index(self):
        index = randint(0, len(self.parsers) - 1)
        self.parser = self.parsers[index]
        send_message(self.tcp_id, pack("!I", index))

    def on_heart(self):
        self.heart += 1
        if self.heart >= self.max_heart:
            close_tcp(self.tcp_id)
            return
        send_message(self.tcp_id, _heart_msg)

    def send_cmd(self, cmd, data):
        if hasattr(self, "parser"):
            self.parser.encrypt(data)
            return send_message(self.tcp_id, pack_msg(cmd, data))
        self.send_cache.append([cmd, data])

    def send_cache_data(self):
        for cache_data in self.send_cache:
            self.send_cmd(cache_data[0], cache_data[1])
        self.send_cache = []

    def close(self):
        close_tcp(self.tcp_id)


class confuse_server(base_server):
    def __init__(self, ip: bytes, port: int, keys: list, session_type=confuse_session):
        super().__init__(ip, port)
        self.keys = keys
        self.parsers = []
        self.sessions = {}
        self.max_heart = 5
        self.session_type = session_type
        for key in keys:
            parser = stream_parser()
            parser.set_password(key)
            self.parsers.append(parser)

        call_after(1000, self.update_heart, 1000)

    def update_heart(self):
        for session_data in self.sessions.values():
            session_data.on_heart()

    def send_cmd(self, session_id, cmd, data):
        self.sessions[session_id].send_cmd(cmd, data)

    def on_session_connected(self, session_id):
        self.sessions[session_id] = self.session_type(session_id,
                                                      self.parsers,
                                                      self.max_heart,
                                                      self.on_cmd,
                                                      session_read_size,
                                                      confuse_state.read_key_index)

    def on_session_disconnected(self, session_id):
        del self.sessions[session_id]

    def on_session_read(self, session_id, data, size):
        self.sessions[session_id].parse(data)

    def on_cmd(self, session_id, cmd, data):
        print(cmd, data)


class confuse_client(base_client):
    def __init__(self, ip: bytes, port: int, keys: list, session_type=confuse_session):
        self.ip = ip
        self.port = port
        self.keys = keys
        self.parsers = []
        self.max_heart = 5
        self.session_type = session_type
        for key in keys:
            parser = stream_parser()
            parser.set_password(key)
            self.parsers.append(parser)

        # 连接目标
        self.reconnect()

        # 开启心跳
        call_after(1000, self.update_heart, 1000)

    def _reconnect(self):
        super().__init__(self.ip, self.port)
        self.session = self.session_type(self.id,
                                         self.parsers,
                                         self.max_heart,
                                         self.on_cmd,
                                         client_read_size,
                                         confuse_state.read_header)

    def reconnect(self, delay=0):
        if delay == 0:
            self._reconnect()
            return
        call_after(delay, self._reconnect)

    def update_heart(self):
        if not hasattr(self, "session"):
            return
        self.session.on_heart()

    def on_connected(self):
        self.session.send_parser_index()

    def on_connect_failed(self):
        pass

    def on_read(self, data, size):
        self.session.parse(data)

    def on_cmd(self, id, cmd, data):
        print("client", cmd, data)

    def send_cmd(self, cmd, data):
        self.session.send_cmd(cmd, data)
