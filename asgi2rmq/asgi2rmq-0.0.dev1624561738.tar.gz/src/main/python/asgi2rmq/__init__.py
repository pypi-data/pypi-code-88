import asyncio
import os

from asgi2async import AsgiServer
from http2rmq import ServerSideAdapter


def app():
    loop = asyncio.get_running_loop()
    server = AsgiServer(loop, )

    rmq = ServerSideAdapter(
        loop,
    )

    loop.create_task(rmq.connect(uri=os.environ.get('RABBITMQ_URL')))
    loop.create_task(server.subscribe(rmq))
    return server
