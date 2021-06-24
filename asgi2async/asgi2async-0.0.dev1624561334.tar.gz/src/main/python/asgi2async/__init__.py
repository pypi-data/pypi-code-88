import asyncio
import logging
from asyncio.events import AbstractEventLoop
from dataclasses import asdict
from enum import Enum
from logging import Logger
from typing import Callable

from http2async.http import *

__logger__: Logger = logging.getLogger(__name__)


def http_request_header(asgi_scope):
    return HttpRequestHeader(
        path=asgi_scope[Asgi.HTTP_PATH.value],
        method=asgi_scope[Asgi.HTTP_METHOD.value],
        headers=dict(
            (k.decode(), v.decode()) for k, v in asgi_scope[Asgi.HTTP_HEADERS.value]
        ),
    )


def web_socket_header(asgi_scope):
    return WebSocketHeader(
        path=asgi_scope[Asgi.HTTP_PATH.value],
        headers=dict(
            (k.decode(), v.decode()) for k, v in asgi_scope[Asgi.HTTP_HEADERS.value]
        ),
    )


def web_socket_receive(asgi_scope, message):
    return WebSocketReceive(
        path=asgi_scope[Asgi.HTTP_PATH.value],
        headers=dict(
            (k.decode(), v.decode()) for k, v in asgi_scope[Asgi.HTTP_HEADERS.value]
        ),
        body=message['text'] if 'text' in message
        else message['bytes'].decode('utf-8')
    )


class Asgi(Enum):
    TYPE = 'type'
    TEXT = 'text'
    BYTES = 'bytes'
    HTTP_TYPE = 'http'
    HTTP_STATUS = 'status'
    HTTP_PATH = 'path'
    HTTP_METHOD = 'method'
    HTTP_HEADERS = 'headers'
    WEB_SOCKET_TYPE = 'websocket'
    HTTP_RESPONSE_BODY = 'http.response.body'
    HTTP_RESPONSE_START = 'http.response.start'
    WEB_SOCKET_ACCEPT = 'websocket.accept'
    WEB_SOCKET_CONNECT = 'websocket.connect'
    WEB_SOCKET_RECEIVE = 'websocket.receive'
    WEB_SOCKET_SEND = 'websocket.send'
    WEB_SOCKET_CLOSE = 'websocket.close'
    WEB_SOCKET_DISCONNECT = 'websocket.disconnect'


class AsgiConnection(HttpServerConnection):
    scope: Dict
    send: Callable
    receive: Callable
    loop: AbstractEventLoop
    done: asyncio.Event

    logger: logging.Logger = __logger__

    def __init__(self, scope, send, receive, loop):
        super().__init__()
        self.scope = scope
        self.send = send
        self.receive = receive
        self.loop = loop
        self.done = asyncio.Event()

    async def start_ws(self):
        ws_header = web_socket_header(self.scope)
        await self.subject.on_next(ws_header)

    async def start_http(self):
        request_header = http_request_header(self.scope)
        await self.subject.on_next(request_header)

    async def write_http_response_body(self, message: HttpResponseBody):
        package = {
            Asgi.TYPE.value: Asgi.HTTP_RESPONSE_BODY.value,
            'body': message,
            'more_body': False,
        }
        await self.send(package)

    async def write_http_response_header(self, message: HttpResponseHeader):
        package = {
            Asgi.TYPE.value: Asgi.HTTP_RESPONSE_START.value,
            Asgi.HTTP_STATUS.value: message.status,
            Asgi.HTTP_HEADERS.value: tuple(
                (str(k).encode(), str(v).encode())
                for k, v in message.headers.items()
            ),
        }
        await self.send(package)

    async def write_http_response(self, message: HttpResponse):
        await self.write_http_response_header(message.header)
        await self.write_http_response_body(message.body)

    async def write_sse_event(self, message: HttpSseEvent):
        data = b''
        if message.id:
            data += 'id: {}\n'.format(message.id).encode()
        if message.event:
            data += 'event: {}\n'.format(message.event).encode()
        if message.data:
            data += 'data: {}\n\n'.format(message.data).encode()
        await self.send({
            Asgi.TYPE.value: Asgi.HTTP_RESPONSE_BODY.value,
            'body': data,
            'more_body': not message.final,
        })
        if message.final:
            self.done.set()

    async def write_ws_accept(self, message: WebSocketAccept):
        package = {
            Asgi.TYPE.value: Asgi.WEB_SOCKET_ACCEPT.value,
        }
        await self.send(package)

        async def read_ws():
            while not self.done.is_set():
                data = await self.receive()
                if data[Asgi.TYPE.value] == Asgi.WEB_SOCKET_DISCONNECT.value:
                    self.done.set()
                elif data[Asgi.TYPE.value] == Asgi.WEB_SOCKET_CONNECT.value:
                    pass
                elif data[Asgi.TYPE.value] == Asgi.WEB_SOCKET_RECEIVE.value:
                    ws_receive = web_socket_receive(self.scope, data)
                    await self.subject.on_next(ws_receive)

        self.loop.create_task(read_ws())

    async def write_ws_send(self, message: WebSocketSend):
        package = {
            Asgi.TYPE.value: Asgi.WEB_SOCKET_SEND.value,
            **asdict(message),
        }
        await self.send(package)

    async def write_ws_close(self, message: WebSocketClose):
        package = {
            Asgi.TYPE.value: Asgi.WEB_SOCKET_CLOSE.value,
        }
        await self.send(package)
        self.done.set()

    async def write_http_request_accept(self, message: HttpRequestAccept):
        async def read_body():
            more_body = True
            data = b''
            while more_body:
                package = await self.receive()
                data += package.get('body', b'')
                more_body = package.get('more_body', False)
            header = http_request_header(self.scope)
            await self.subject.on_next(HttpRequest(header=header, body=data))

        self.loop.create_task(read_body())

    async def on_error(self, error):
        body = str(error).encode()
        message = HttpResponse(
            header=HttpResponseHeader(
                status=500,
                headers={
                    'Content-Type': 'text/plan;charset=UTF-8',
                    'Content-Length': str(len(body)),
                }
            ),
            body=body
        )
        await message.write_in(self)
        self.done.set()

    async def on_complete(self):
        self.done.set()


class AsgiServer(HttpServer):
    logger: Logger = __logger__

    def __init__(self, loop):
        super().__init__()
        self.loop = loop
        self.subject = Subject()

    def create_connection(self, scope, receive, send) -> AsgiConnection:
        return AsgiConnection(
            scope=scope,
            receive=receive,
            send=send,
            loop=self.loop,
        )

    async def __call__(self, scope, receive, send):
        request_type = scope.get(Asgi.TYPE.value, Asgi.HTTP_TYPE.value)
        if request_type not in [Asgi.WEB_SOCKET_TYPE.value, Asgi.HTTP_TYPE.value]:
            return
        connection = self.create_connection(scope, receive, send)
        await self.subject.on_next(connection)
        if request_type == Asgi.HTTP_TYPE.value:
            await connection.start_http()
        elif request_type == Asgi.WEB_SOCKET_TYPE.value:
            await connection.start_ws()
        await connection.done.wait()
        await connection.subject.on_complete()

    async def subscribe(self, *args, **kwargs) -> Subscription:
        return await self.subject.subscribe(*args, **kwargs)
