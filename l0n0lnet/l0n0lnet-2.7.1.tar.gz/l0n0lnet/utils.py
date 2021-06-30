from ctypes import *
from l0n0lnet import se
import random

_delay_funcs = {}   # 延时函数容器 id : function
_resolve_max_id = 0  # 域名解析请求ID
_resolve_cbs = {}   # 域名解析回调

se.get_address.restype = c_bool
se.call_after.restype = c_uint64

def call_after(timeout: int, fn, repeat: int = 0):
    """
    延时调用

    @timeout:int: timeout毫秒后调用fn函数\n
    @fn: function: 无参数。返回bool。表示是否停止运行。True表示停止运行\n
    @repeat: int: repeat毫秒后重复执行该函数\n

    例如：
    ```
    def test_timer():
        print("123")
        return True

    # 每秒打印一次 '123'
    call_after(1000, test_timer, 1000)
    ```
    """
    delay_id = se.call_after(timeout, _delay_cb, repeat)
    if delay_id == 0:
        return False

    _delay_funcs[delay_id] = {
        "cb": fn,
        "repeat": repeat
    }

    return True


def is_ipv6(ip: bytes):
    """
    判断某个ip地址是否时ipv6地址
    """
    return ip.find(b":") != -1


@CFUNCTYPE(c_bool, c_uint64)
def _delay_cb(id):
    """
    给c++的延时回调。用于调用python函数。（不要主动调用）
    """
    data = _delay_funcs.get(id)
    if not data:
        return False

    stop = data['cb']()

    if stop or data['repeat'] == 0:
        del _delay_funcs[id]

    return not stop


@CFUNCTYPE(c_bool, c_char_p, c_uint64, c_char_p)
def _on_resolve(name, req_id, address):
    """
    域名解析内部回调（不要主动调用）
    """
    cb = _resolve_cbs.get(req_id)
    if not cb:
        return False
    if not cb(name, address):
        del _resolve_cbs[req_id]
        return False
    return True


def get_address(name, cb):
    """
    域名解析

    @name:bytes:域名
    @cb:function:两个参数的函数bool(name:bytes, address:bytes)。
        返回True表示接收下一个IP地址(一个域名可能有多个ip)；
        返回False表示不再接收下一个ip。
        函数会被调用多次，每次一个ip地址
    例如:
    ```python
    def on_resolve(name, address):
        print(name, address)
        return True
    get_address(b'www.l0n0l.cn', on_resolve)
    ```
    """
    try:
        global _resolve_max_id
        _resolve_max_id += 1
        _resolve_cbs[_resolve_max_id] = cb
        return se.get_address(name, _resolve_max_id, _on_resolve)
    except:
        return False


def ip4_to_bytes(ip: bytes):
    """
    将IPV4地址转换为4bytes二进制序列

    #ip:bytes:ipv4地址\n
    @return:bytes:4字节二进制\n

    例如:
    ```python
    ip4_to_bytes(b'127.0.0.1')
    out: b'\\x7f\\x00\\x00\\x01'
    ```
    """
    ret = b'\x00\x00\x00\x00'
    se.ip4_to_bytes(ip, ret)
    return ret


def bytes_to_ip4(bip: bytes):
    """
    将4字节二进制序列转换为ip地址字符串

    @bip:bytes:4字节二进制ip地址
    @return:bytes:ip地址序列

    例如
    ```python
    bytes_to_ip4(b'\\x7f\\x00\\x00\\x01')
    out: b'127.0.0.1'
    ```
    """
    ret = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    se.bytes_to_ip4(bip, ret)
    return ret.decode().encode()


def ip6_to_bytes(ip: bytes):
    """
    将IPV6地址转换为16bytes二进制序列

    #ip:bytes:ipv6地址\n
    @return:bytes:16字节二进制\n

    例如:
    ```python
    ip6_to_bytes(b'fe80::dc7c:4130:fef4:ab7e')
    out: b'\\xfe\\x80\\x00\\x00\\x00\\x00\\x00\\x00\\xdc|A0\\xfe\\xf4\\xab~'
    ```
    """
    ret = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    se.ip6_to_bytes(ip, ret)
    return ret


def bytes_to_ip6(bip: bytes):
    """
    将16字节二进制序列转换为ip地址字符串

    @bip:bytes:16字节二进制ip地址
    @return:bytes:ip地址序列

    例如
    ```python
    bytes_to_ip6(b'\\xfe\\x80\\x00\\x00\\x00\\x00\\x00\\x00\\xdc|A0\\xfe\\xf4\\xab~')
    out: 'fe80::dc7c:4130:fef4:ab7e'
    ```
    """
    ret = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    se.bytes_to_ip4(bip, ret)
    return ret.decode().encode()


def ip2bytes(ip: bytes):
    """
    将ip地址转换为二进制序列，自动识别ipv4,ipv6

    @ip:bytes:ip地址
    @return:bytes:二进制序列

    例如
    ```python
    ip2bytes(b'127.0.0.1')
    out: b'\\x7f\\x00\\x00\\x01'

    ip2bytes(b'fe80::dc7c:4130:fef4:ab7e')
    out: b'\\xfe\\x80\\x00\\x00\\x00\\x00\\x00\\x00\\xdc|A0\\xfe\\xf4\\xab~'
    ```
    """
    if is_ipv6(ip):
        return ip6_to_bytes(ip)
    return ip4_to_bytes(ip)


def bytes2ip(value: bytes):
    """
    将二进制序列转换为可读ip地址

    @value:bytes:二进制序列
    @return:bytes:ip地址

    例如:
    ```python
    bytes2ip(b'\\x7f\\x00\\x00\\x01')
    out: b'127.0.0.1'

    bytes_to_ip6(b'\\xfe\\x80\\x00\\x00\\x00\\x00\\x00\\x00\\xdc|A0\\xfe\\xf4\\xab~')
    out: 'fe80::dc7c:4130:fef4:ab7e'
    ```
    """
    if len(value) > 4:
        return bytes_to_ip6(value)
    return bytes_to_ip4(value)


