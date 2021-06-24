# coding: utf-8
# Copyright (c) Qotto, 2021

import contextvars

from contextvars import ContextVar


class EventyContext:
    def __init__(self, contextvar: ContextVar):
        self._contextvar = contextvar

    def get(self) -> str:
        return self._contextvar.get()

    def set(self, value: str) -> None:
        self._contextvar.set(value)

    def is_defined(self) -> bool:
        return self.get() != ''

    def unset(self) -> None:
        self._contextvar.set('')


_trace_id = contextvars.ContextVar("trace_id", default="")
trace_id = EventyContext(_trace_id)

_request_id = contextvars.ContextVar("request_id", default="")
request_id = EventyContext(_request_id)
