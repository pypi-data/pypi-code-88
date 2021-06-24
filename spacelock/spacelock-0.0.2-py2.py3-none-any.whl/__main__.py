"""
Author:     LanHao
Date:       2021/6/24 9:13

模块直接运行一个空间锁服务

"""
import logging
import asyncio

from sortedcontainers import SortedDict
# from tornado.tcpserver import TCPServer
# from tornado.iostream import StreamClosedError

from .core import get_lock_handler


async def main():
    loop = asyncio.get_running_loop()
    spaces = SortedDict({})
    server = await loop.create_server(
        get_lock_handler(spaces),
        '0.0.0.0', 8888)

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
