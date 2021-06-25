# coding: utf-8
# Copyright (c) Qotto, 2021

import logging
from base64 import b64encode
from datetime import datetime, timezone
from secrets import token_urlsafe
from typing import Callable

from eventy.context import trace_id_ctx, request_id_ctx

logger = logging.getLogger(__name__)


def extracting_context(
    func,
    trace_id_generator: Callable[[Callable, tuple, dict], str] = None,
    request_id_generator: Callable[[Callable, tuple, dict], str] = None,
):
    """
    Transform any function into a function that extracts trace_id / request_id from kwargs and put it in context
    """

    def extracting_context_func(*args, **kwargs):
        trace_id_token = None
        request_id_token = None
        if 'trace_id' in kwargs:
            trace_id_token = trace_id_ctx.set(kwargs.pop('trace_id'))
        elif 'correlation_id' in kwargs:
            trace_id_token = trace_id_ctx.set(kwargs.pop('correlation_id'))
        elif trace_id_generator:
            trace_id_token = trace_id_ctx.set(trace_id_generator(func, *args, **kwargs))  # noqa
        if 'request_id' in kwargs:
            request_id_token = request_id_ctx.set(kwargs.pop('request_id'))
        elif request_id_generator:
            request_id_token = request_id_ctx.set(request_id_generator(func, *args, **kwargs))  # noqa
        logger.debug('Extracted context from function kwargs')
        func(*args, **kwargs)
        # TODO: optionally reset context

    return extracting_context_func


class SimpleIdGenerator:
    def __init__(self, **kwargs):
        self.prefix = '-'.join(f'{k}={v}' for k, v in kwargs.items()) or '-'

    def __call__(self, *args, **kwargs):
        content = '-'.join(f'{k}={v}' for k, v in kwargs.items()) or '-'
        ts_now = datetime.now(timezone.utc).timestamp()
        ts_2k = datetime(2000, 1, 1, tzinfo=timezone.utc).timestamp()
        ts2000res65536 = int(65536 * (ts_now - ts_2k)).to_bytes(6, 'big')
        date = b64encode(ts2000res65536, b'_-').decode('ascii')
        random = token_urlsafe(3)
        id = f'{self.prefix}:{content}:{date}:{random}'
        logger.debug(f'Generated context id: {id}')
        return id
