# coding: utf-8
# Copyright (c) Qotto, 2021

import contextvars

from contextvars import ContextVar


class EventyContext:
    _contextvar: ContextVar

    def __init__(self, var_name: str):
        self._contextvar = contextvars.ContextVar(var_name, default="")

    def get(self) -> str:
        return self._contextvar.get()

    def set(self, value: str) -> None:
        self._contextvar.set(value)

    def is_defined(self) -> bool:
        return self.get() != ''

    def unset(self) -> None:
        self._contextvar.set('')


trace_id_ctx = EventyContext("trace_id")
request_id_ctx = EventyContext("request_id")
