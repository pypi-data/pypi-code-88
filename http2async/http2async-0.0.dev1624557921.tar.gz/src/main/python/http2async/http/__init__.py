from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from aiorx import Observable, Observer, Subscription
from aiorx.subjects import Subject

from http2async.api import Http2Async, Http2AsyncMessage


class HttpIncoming(Http2AsyncMessage):

    async def write_in(self, stream: HttpIncomingOutputStream):
        raise NotImplementedError()


class HttpOutgoing(Http2AsyncMessage):

    async def write_in(self, stream: HttpOutgoingOutputStream):
        raise NotImplementedError()

    def is_final(self) -> bool:
        raise NotImplementedError()


class HttpIncomingOutputStream:

    async def write(self, message: HttpIncoming):
        await message.write_in(self)

    def write_http_request_header(self, message: HttpRequestHeader):
        raise NotImplementedError()

    def write_http_request(self, message: HttpRequest):
        raise NotImplementedError()

    def write_ws_header(self, message: WebSocketHeader):
        raise NotImplementedError()

    def write_ws_receive(self, message: WebSocketReceive):
        raise NotImplementedError()


class HttpOutgoingOutputStream:

    async def write(self, message: HttpOutgoing):
        await message.write_in(self)

    async def write_http_response_body(self, message: HttpResponseBody):
        raise NotImplementedError()

    async def write_http_response_header(self, message: HttpResponseHeader):
        raise NotImplementedError()

    async def write_http_response(self, message: HttpResponse):
        raise NotImplementedError()

    async def write_sse_event(self, message: HttpSseEvent):
        raise NotImplementedError()

    async def write_ws_accept(self, message: WebSocketAccept):
        raise NotImplementedError()

    async def write_ws_send(self, message: WebSocketSend):
        raise NotImplementedError()

    async def write_ws_close(self, message: WebSocketClose):
        raise NotImplementedError()

    async def write_http_request_accept(self, message: HttpRequestAccept):
        raise NotImplementedError()


class HttpServerConnection(Observer[HttpOutgoing], Observable[HttpIncoming], HttpOutgoingOutputStream):

    def __init__(self):
        self.subject = Subject()

    async def subscribe(self, *args, **kwargs) -> Subscription:
        return await self.subject.subscribe(*args, **kwargs)

    async def on_next(self, event: HttpOutgoing):
        await self.write(event)


class HttpServer(Observable[HttpServerConnection]):
    pass


@Http2Async.HTTP_REQUEST_HEADER
@dataclass
class HttpRequestHeader(HttpIncoming):
    method: str = None
    path: str = None
    headers: Dict[str, str] = field(default_factory=dict)

    @classmethod
    def parse(cls, data):
        return cls(**data)

    async def write_in(self, stream: HttpIncomingOutputStream):
        await stream.write_http_request_header(self)


HttpRequestBody = bytes


@Http2Async.HTTP_REQUEST_ACCEPT
@dataclass
class HttpRequestAccept(HttpOutgoing):

    @classmethod
    def parse(cls, data):
        return cls()

    async def write_in(self, stream: HttpOutgoingOutputStream):
        await stream.write_http_request_accept(self)

    def is_final(self) -> bool:
        return False


@Http2Async.HTTP_REQUEST
@dataclass
class HttpRequest(HttpIncoming):
    header: HttpRequestHeader
    body: HttpRequestBody

    @property
    def path(self) -> str:
        return self.header.path

    @classmethod
    def parse(cls, data):
        return cls(header=data['header'], body=data['body'])

    async def write_in(self, stream: HttpIncomingOutputStream):
        await stream.write_http_request(self)


@Http2Async.WEB_SOCKET_HEADER
@dataclass
class WebSocketHeader(HttpIncoming):
    path: str
    headers: Dict[str, str]

    @classmethod
    def parse(cls, data):
        return cls(**data)

    async def write_in(self, stream: HttpIncomingOutputStream):
        await stream.write_ws_header(self)


@Http2Async.WEB_SOCKET_RECEIVE
@dataclass
class WebSocketReceive(HttpIncoming):
    path: str
    headers: Dict[str, str]
    body: str

    @classmethod
    def parse(cls, data):
        return cls(**data)

    async def write_in(self, stream: HttpIncomingOutputStream):
        await stream.write_ws_receive(self)


@Http2Async.HTTP_RESPONSE_HEADER
@dataclass
class HttpResponseHeader(HttpOutgoing):
    status: int = 200
    headers: Dict[str, str] = field(default_factory=dict)

    @classmethod
    def parse(cls, data):
        return cls(**data)

    async def write_in(self, stream: HttpOutgoingOutputStream):
        await stream.write_http_response_header(self)

    def is_final(self) -> bool:
        # @todo verify 204 no content
        return False


HttpResponseBody = bytes


@Http2Async.HTTP_RESPONSE
@dataclass
class HttpResponse(HttpOutgoing):
    header: HttpResponseHeader = field(default_factory=HttpResponseHeader)
    body: bytes = b''

    @classmethod
    def parse(cls, data):
        return cls(header=HttpResponseHeader.parse(data['header']), body=data['body'])

    async def write_in(self, stream: HttpOutgoingOutputStream):
        await stream.write_http_response(self)

    def is_final(self) -> bool:
        return True


@Http2Async.HTTP_SSE_EVENT
@dataclass
class HttpSseEvent(HttpOutgoing):
    id: str = None
    event: str = None
    data: str = None
    final: bool = False

    @classmethod
    def parse(cls, data):
        return cls(**data)

    async def write_in(self, stream: HttpOutgoingOutputStream):
        await stream.write_sse_event(self)

    def is_final(self) -> bool:
        return self.final


@Http2Async.HTTP_WS_ACCEPT
@dataclass
class WebSocketAccept(HttpOutgoing):
    @classmethod
    def parse(cls, data):
        return cls()

    async def write_in(self, stream: HttpOutgoingOutputStream):
        await stream.write_ws_accept(self)

    def is_final(self) -> bool:
        return False


@Http2Async.HTTP_WS_SEND
@dataclass
class WebSocketSend(HttpOutgoing):
    bytes: bytes = None
    text: str = None

    @classmethod
    def parse(cls, data):
        return cls(**data)

    async def write_in(self, stream: HttpOutgoingOutputStream):
        await stream.write_ws_send(self)

    def is_final(self) -> bool:
        return False


@Http2Async.HTTP_WS_CLOSE
@dataclass
class WebSocketClose(HttpOutgoing):
    @classmethod
    def parse(cls, data):
        return cls()

    async def write_in(self, stream: HttpOutgoingOutputStream):
        await stream.write_ws_close(self)

    def is_final(self) -> bool:
        return True
