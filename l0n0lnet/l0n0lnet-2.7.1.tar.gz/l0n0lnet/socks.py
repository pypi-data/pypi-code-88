from l0n0lnet.tcp import base_client, base_server
from l0n0lnet.tcp import session_read_size, close_tcp, get_ip_port
from l0n0lnet.utils import get_address, is_ipv6
from l0n0lnet.utils import ip2bytes, bytes2ip
from struct import pack, unpack


class socks5_server(base_server):
    def __init__(self, ip: bytes, port: int):
        super().__init__(ip, port)
        self.clients = {}
        self.session_data = {}

    def on_session_connected(self, session_id):
        session_read_size(session_id, 2)
        self.session_data[session_id] = {
            "state": "get_version"
        }

    def on_session_disconnected(self, session_id):
        session_data = self.session_data.get(session_id)
        if not session_data:
            return
        client = session_data.get('client')
        if not client:
            return
        del self.session_data[session_id]
        client.on_session_disconnected()

    def on_session_read(self, session_id, data, size):
        session_data = self.session_data[session_id]
        if session_data["state"] == "get_version":
            session_read_size(session_id, data[1])
            session_data['state'] = "get_methods"
        elif session_data["state"] == "get_methods":
            self.send_msg(session_id, b'\x05\x00')
            session_read_size(session_id, 4)
            session_data['state'] = "get_request"
        elif session_data["state"] == "get_request":
            session_data['cmd'] = data[1]
            session_data['atyp'] = data[3]
            # 0x01 IPv4地址，DST.ADDR部分4字节长度
            if session_data['atyp'] == 0x01:
                session_read_size(session_id, 4)
                session_data['state'] = "get_addr"
            # 0x03 域名，DST.ADDR部分第一个字节为域名长度，DST.ADDR剩余的内容为域名，没有\0结尾。
            elif session_data['atyp'] == 0x03:
                session_read_size(session_id, 1)
                session_data['state'] = "get_name_size"
            # 0x04 IPv6地址，16个字节长度。
            elif session_data['atyp'] == 0x04:
                session_read_size(session_id, 16)
                session_data['state'] = "get_addr"
        elif session_data["state"] == "get_addr":
            session_data['addr'] = bytes2ip(data)
            session_read_size(session_id, 2)
            session_data['state'] = "get_port"
        elif session_data["state"] == "get_name_size":
            session_read_size(session_id, data[0])
            session_data['state'] = "get_name"
        elif session_data["state"] == "get_name":
            session_data['addr'] = data
            session_read_size(session_id, 2)
            session_data['state'] = "get_port"
        elif session_data["state"] == "get_port":
            session_data['port'] = unpack(">H", data)[0]
            # 0x01表示CONNECT请求
            if session_data['cmd'] == 0x01:
                self.cmd_connect(session_id, session_data)
            # 0x02表示BIND请求
            elif session_data['cmd'] == 0x02:
                pass
            # 0x03表示UDP转发
            elif session_data['cmd'] == 0x03:
                pass
        elif session_data["state"] == "trans_data":
            session_data['client'].on_get_request(data)

    def send_error(self, session_id, err_code):
        self.send_msg(session_id, b'\x05' + err_code +
                      b'\x00\x01\x00\x00\x00\x00\x00\x00')
        del self.session_data[session_id]
        close_tcp(session_id)

    def cmd_connect(self, session_id, session_data):
        # 解析域名
        if session_data['atyp'] == 0x03:
            def on_name_resolve(name, ip):
                if ip is None:
                    # 0x01普通SOCKS服务器连接失败
                    self.send_error(session_id, b'\x01')
                    return
                session_data['addr'] = ip
                self.connect_to(session_id, session_data)
            if not get_address(session_data['addr'], on_name_resolve):
                close_tcp(session_id)
        else:
            self.connect_to(session_id, session_data)

    def connect_to(self, session_id, session_data):
        ip = session_data['addr']
        port = session_data['port']
        session_data['client'] = sock5_target_client(
            self, session_id, ip, port)
        session_read_size(session_id, 0)
        session_data['state'] = "trans_data"

    def cmd_bind(self, session_id):
        pass

    def cmd_udptrans(self, session_id):
        pass

    def on_client_disconnected(self, session_id):
        del self.session_data[session_id]
        close_tcp(session_id)


class sock5_target_client(base_client):
    def __init__(self, owner: socks5_server, session_id: int, ip: bytes, port: int):
        super().__init__(ip, port)
        self.session_id = session_id
        self.owner = owner
        self.session_data = owner.session_data[session_id]

    def send_msg_back(self, data: bytes):
        self.owner.send_msg(self.session_id, data)

    def on_connected(self):
        msg = b'\x05\x00\x00'
        ip, port = get_ip_port(self.session_id)
        if is_ipv6(ip):
            msg += b'\x04' + ip2bytes(ip)
        else:
            msg += b'\x01' + ip2bytes(ip)
        msg += pack(">H", port)
        self.send_msg_back(msg)

    def on_connect_failed(self):
        self.owner.send_error(self.session_id, b'\x03')

    def on_disconnected(self):
        if self.owner:
            self.owner.on_client_disconnected(self.session_id)

    def on_read(self, data, size):
        self.send_msg_back(data)

    def on_get_request(self, data):
        self.send_msg(data)

    def on_session_disconnected(self):
        self.close()
        self.owner = None
        self.session_id = None
        self.session_data = None



