from enum import Enum


class Http2Async(Enum):
    APPLICATION = 'http2async'
    HTTP_UNKNOWN = 'http-unknown'
    HTTP_REQUEST_HEADER = 'http-request-header'
    HTTP_REQUEST = 'http-request'
    WEB_SOCKET_HEADER = 'http-ws-header'
    WEB_SOCKET_RECEIVE = 'http-ws-receive'
    WEB_SOCKET_ACCEPT = 'http-ws-accept'
    HTTP_RESPONSE = 'http-response'
    HTTP_RESPONSE_HEADER = 'http-response-header'
    HTTP_RESPONSE_BODY = 'http-response-body'
    HTTP_REQUEST_ACCEPT = 'http-request-accept'
    HTTP_SSE_EVENT = 'http-ss-event'
    HTTP_WS_ACCEPT = 'http-ws-accept'
    HTTP_WS_SEND = 'http-ws-send'
    HTTP_WS_CLOSE = 'http-ws-close'

    def __call__(self, clazz):
        setattr(clazz, 'type', self.value)
        self.clazz = clazz
        return clazz


class Http2AsyncMessage:
    type: Http2Async
