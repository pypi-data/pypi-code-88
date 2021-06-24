from __future__ import annotations

import json
from dataclasses import fields, is_dataclass
from typing import Any, TypeVar, Generic, Type, get_type_hints

from http2async.http import *

E = TypeVar('E')


def _recursive_merge(destination, data):
    for k, v in data.items():
        if isinstance(v, (dict,)):
            value = destination.get(k, False) or {}
            destination[k] = _recursive_merge(value, v)
        else:
            destination[k] = v
    return destination


class DataClassBuilder(Generic[E]):

    def __init__(self, data_class: Type[E], data=None):
        self.hints = get_type_hints(data_class)
        self.data_class = data_class
        self.data = data or {}

    def copy(self, extra_data=None) -> 'self':
        if extra_data is None:
            extra_data = {}
        return type(self)(data_class=self.data_class, data=_recursive_merge(dict(self.data), extra_data))

    def put(self, **kwargs) -> DataClassBuilder[E]:
        return self.copy(kwargs)

    def build(self) -> E:
        prepared_data = dict(self.data)
        for field in fields(self.data_class):
            field_type = self.hints[field.name]
            if not is_dataclass(field_type):
                continue
            value = field_type(**prepared_data.get(field.name, {}))
            prepared_data[field.name] = value
        data_class_instance = self.data_class(**prepared_data)
        return data_class_instance

    def __call__(self) -> E:
        return self.build()


class HttpResponseHeaderBuilder(DataClassBuilder[HttpResponseHeader]):

    def sse(self, encoding='utf-8') -> 'self':
        return self.copy({
            'headers': {
                'Cache-Control': 'no-cache',
                'Content-Type': 'text/event-stream;charset={}'.format(encoding),
            }
        })


class HttpResponseBuilder(DataClassBuilder[HttpResponse]):

    def status(self, status_code: int):
        return self.copy({
            'header': {
                'status': status_code
            }
        })

    def text(self, body: str, encoding: str = 'utf-8') -> 'self':
        raw_body = body.encode(encoding)
        return self.copy({
            'header': {
                'headers': {
                    'Content-Type': 'text/plan;charset={}'.format(encoding),
                    'Content-Length': '{}'.format(len(raw_body)),
                }
            },
            'body': raw_body,
        })

    def json(self, body: Any, encoding: str = 'utf-8') -> 'self':
        raw_body = json.dumps(body).encode(encoding)
        return self.copy({
            'header': {
                'headers': {
                    'Content-Type': 'application/json;charset={}'.format(encoding),
                    'Content-Length': '{}'.format(len(raw_body)),
                }
            },
            'body': raw_body,
        })


class HttpFactory:

    def response_header(self) -> HttpResponseHeaderBuilder:
        return HttpResponseHeaderBuilder(HttpResponseHeader)

    def accept(self) -> DataClassBuilder[HttpRequestAccept]:
        return DataClassBuilder(HttpRequestAccept)

    def response(self) -> HttpResponseBuilder:
        return HttpResponseBuilder(HttpResponse)

    def sse_header(self) -> HttpResponseHeaderBuilder:
        return self.response_header().sse()

    def sse_event(self) -> DataClassBuilder[HttpSseEvent]:
        return DataClassBuilder(HttpSseEvent)

    def ws_accept(self) -> DataClassBuilder[WebSocketAccept]:
        return DataClassBuilder(WebSocketAccept)

    def ws_close(self) -> DataClassBuilder[WebSocketClose]:
        return DataClassBuilder(WebSocketClose)

    def ws_send(self) -> DataClassBuilder[WebSocketSend]:
        return DataClassBuilder(WebSocketSend)

    def ws_header(self):
        pass

    def request_header(self):
        pass

    def request(self):
        pass
