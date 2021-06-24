"""
Author:     LanHao
Date:       2021/6/24 10:52

"""

import asyncio
import json
from spacelock.core import ResultMessage


class EchoClientProtocol(asyncio.Protocol):
    space_key = None
    lock = False

    def __init__(self, message, on_con_lost):
        self.message = message
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):
        self.transport = transport
        space_key = json.dumps({"handle_status": 0, "message": {"key": "test"}}).encode("utf8")
        transport.write(space_key)
        print('Data sent: {!r}'.format(space_key))

    def data_received(self, data):
        result = ResultMessage(**json.loads(data.decode("utf8")))

        if self.space_key is None:
            if result.status == 200:
                self.space_key = True  # 空间占领成功
            print("space 抢占成功")
            if not self.lock:
                print(f"发送抢占锁信息")
                # TODO 此处box 应该是何种形式创建? 服务端现在只弄了3维空间锁
                self.transport.write(
                    json.dumps(
                        {"handle_status": 1, "message": {"box": [5, 5, 5, 15, 15, 15], "release": False}}).encode(
                        "utf8"))
            else:
                print("逻辑紊乱2")
        else:
            if not self.lock:
                self.lock = True
                print("枷锁成功")
            else:
                print("逻辑紊乱")

        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.on_con_lost.set_result(True)


async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()
    message = 'Hello World!'

    transport, protocol = await loop.create_connection(
        lambda: EchoClientProtocol(message, on_con_lost),
        '127.0.0.1', 8888)

    # Wait until the protocol signals that the connection
    # is lost and close the transport.
    try:
        await on_con_lost
    finally:
        transport.close()


asyncio.run(main())
