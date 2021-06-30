# coding: utf-8
# Copyright (c) Qotto, 2021

from contextvars import ContextVar, Token


class EventyContext:
    _contextvar: ContextVar

    def __init__(self, var_name: str):
        self._contextvar = ContextVar(var_name, default="")

    @property
    def name(self):
        return self._contextvar.name

    def get(self) -> str:
        return self._contextvar.get()

    def set(self, value: str) -> Token:
        return self._contextvar.set(value)

    def is_defined(self) -> bool:
        return self.get() != ''

    def unset(self) -> None:
        self._contextvar.set('')

    def reset(self, token: Token) -> str:
        previous = self.get()
        self._contextvar.reset(token)
        return previous


correlation_id_ctx = EventyContext("correlation_id")
request_id_ctx = EventyContext("request_id")
