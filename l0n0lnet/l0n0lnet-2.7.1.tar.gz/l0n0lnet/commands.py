from l0n0lnet.socks import socks5_server
from l0n0lnet.transform import trans_server
from l0n0lnet import run, add_quit_func
from l0n0lnet.stream_parser import stream_parser
from l0n0lnet.reverse import reverse_client, reverse_server
from base64 import b64encode, b64decode
import sys
import argparse


def get_keys(filename):
    keys = []
    with open(filename, 'rb') as fp:
        for line in fp.readlines():
            key = b64decode(line[:-1])
            keys.append(key)
    return keys


def run_transform_socks5_client():
    parser = argparse.ArgumentParser(description="链接混淆服务器")
    parser.add_argument("listenip", type=str, help="本地监听IP")
    parser.add_argument("listenport", type=int, help="本地监听端口")
    parser.add_argument("ip", type=str, help="服务器IP")
    parser.add_argument("port", type=int, help="服务器端口")
    parser.add_argument("passfile", type=str, help="密码文件")
    args = parser.parse_args()

    keys = get_keys(args.passfile)
    tc = trans_server(args.listenip.encode(), args.listenport,
                      args.ip.encode(), args.port, keys, 'client')

    print(f"Open transform service on {args.listenip}:{args.listenport}.")
    print(f"Connected to  {args.ip}:{args.port}.")

    def on_close():
        tc.close()
        print("closing")

    add_quit_func(on_close)

    run()


def run_transform_socks5_server():
    parser = argparse.ArgumentParser(description="创建数据混淆socks5服务器")
    parser.add_argument("listenip", type=str, help="本地监听IP")
    parser.add_argument("listenport", type=int, help="监听端口")
    parser.add_argument("sockport", type=int, help="sock5s服务器端口")
    parser.add_argument("passfile", type=str, help="密码文件")
    args = parser.parse_args()

    keys = get_keys(args.passfile)
    socks5 = socks5_server(b'127.0.0.1', args.sockport)
    ts = trans_server(args.listenip.encode(), args.listenport, b'127.0.0.1',
                      args.sockport, keys, 'server')

    print(f"Open sock5 service on 127.0.0.1:{args.sockport}.")
    print(f"Open transform service on {args.listenip}:{args.listenport}.")

    def on_close():
        ts.close()
        socks5.close()
        print("closing")

    add_quit_func(on_close)

    run()


def generate_pass_file():
    parser = argparse.ArgumentParser(description="创建混淆文件")
    parser.add_argument("filename", type=str, help="文件名")
    parser.add_argument("count", type=int, help="文件行数")
    args = parser.parse_args()
    with open(args.filename, 'wb') as fp:
        for i in range(args.count):
            fp.write(b64encode(stream_parser.gen_password()))
            fp.write(b"\n")


def run_reverse_server():
    parser = argparse.ArgumentParser(description="创建反向代理服务器")
    parser.add_argument("listenip", type=str, help="监听ip")
    parser.add_argument("listenport", type=int, help="监听端口")
    parser.add_argument("passfile", type=str, help="混淆文件")
    args = parser.parse_args()
    keys = get_keys(args.passfile)
    server = reverse_server(args.listenip.encode(), args.listenport, keys)

    print(f"Open reverse service on {args.listenip}:{args.listenport}.")

    def on_close():
        server.close()
        print("closing")

    add_quit_func(on_close)
    run()


def run_reverse_client():
    parser = argparse.ArgumentParser(description="创建反向代理客户端")
    parser.add_argument("serverip", type=str, help="服务器IP")
    parser.add_argument("serverport", type=int, help="服务器端口")
    parser.add_argument("remoteport", type=int, help="服务器代理端口")
    parser.add_argument("localip", type=str, help="本地服务器IP")
    parser.add_argument("localport", type=int, help="本地服务端口")
    parser.add_argument("passfile", type=str, help="本地服务端口")
    args = parser.parse_args()
    keys = get_keys(args.passfile)
    client = reverse_client(args.serverip.encode(),
                            args.serverport,
                            keys,
                            args.remoteport,
                            args.localip.encode(),
                            args.localport)

    print(f"Connect to {args.serverip}:{args.serverport} and open remote port {args.remoteport} for local {args.localip}:{args.localport} service.")

    def on_close():
        client.close()
        print("closing")

    add_quit_func(on_close)
    run()


def run_tcp_proxy_server():
    parser = argparse.ArgumentParser(description="创建正向tcp混淆代理服务器")
    parser.add_argument("listenip", type=str, help="监听IP")
    parser.add_argument("listenport", type=int, help="监听端口")
    parser.add_argument("targetip", type=str, help="目标IP")
    parser.add_argument("targetport", type=int, help="目标端口")
    parser.add_argument("passfile", type=str, help="密码文件")
    parser.add_argument("role", type=str, help="(client | server)作为服务器还是客户端")
    args = parser.parse_args()

    keys = get_keys(args.passfile)

    ts = trans_server(args.listenip.encode(), args.listenport, args.targetip.encode(),
                      args.targetport, keys, args.role)

    print(f"Open transform service on {args.listenip}:{args.listenport}.")

    def on_close():
        ts.close()
        print("closing")

    add_quit_func(on_close)

    run()


def run_socks5_server():
    parser = argparse.ArgumentParser(description="创建socks5服务器")
    parser.add_argument("listenip", type=str, help="监听IP")
    parser.add_argument("listenport", type=int, help="监听端口")
    args = parser.parse_args()

    socks5 = socks5_server(args.listenip.encode(), args.listenport)

    print(f"Open socks5 service on {args.listenip}:{args.listenport}.")

    def on_close():
        socks5.close()
        print("closing")

    add_quit_func(on_close)

    run()
