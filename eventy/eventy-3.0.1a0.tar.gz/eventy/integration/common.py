# coding: utf-8
# Copyright (c) Qotto, 2021
from typing import Callable

from eventy.context import trace_id_ctx, request_id_ctx


def extracting_context(
    func,
    trace_id_generator: Callable[[Callable, tuple, dict], str] = None,
    request_id_generator: Callable[[Callable, tuple, dict], str] = None,
):
    def extracting_context_func(*args, **kwargs):
        trace_id_token = None
        request_id_token = None
        if 'trace_id' in kwargs:
            trace_id_token = trace_id_ctx.set(kwargs.pop('trace_id'))
        elif 'correlation_id' in kwargs:
            trace_id_token = trace_id_ctx.set(kwargs.pop('correlation_id'))
        elif trace_id_generator:
            trace_id_token = trace_id_ctx.set(trace_id_generator(func, args, kwargs))  # noqa
        if 'request_id' in kwargs:
            request_id_token = request_id_ctx.set(kwargs.pop('request_id'))
        elif request_id_generator:
            request_id_token = request_id_ctx.set(request_id_generator(func, args, kwargs))  # noqa
        func(*args, **kwargs)
        # TODO: optionally reset context

    return extracting_context_func
