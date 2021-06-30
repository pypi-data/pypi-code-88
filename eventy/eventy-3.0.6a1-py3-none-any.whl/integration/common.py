# coding: utf-8
# Copyright (c) Qotto, 2021

import logging
from base64 import b64encode
from datetime import datetime, timezone
from secrets import token_urlsafe
from typing import Callable

from ..context import correlation_id_ctx, request_id_ctx

logger = logging.getLogger(__name__)

__all__ = [
    'with_context',
    'merge_decorators',
    'DecoratorType',
    'generate_simple_id',
    'simple_func_id_generator',
]

DecoratorType = Callable[..., Callable]


def merge_decorators(*decorators) -> DecoratorType:
    """
    Merge multiple decorators, apply from left to right
    """

    if not decorators:
        def identity(func):
            return func

        return identity

    def decorator(func):
        def decorated_func(*args, **kwargs):
            inner_func = func
            nested_decorators = decorators
            for nested_decorator in nested_decorators:
                inner_func = nested_decorator(inner_func)

            return inner_func(*args, **kwargs)

        return decorated_func

    return decorator


def with_context(
    trace_id_generator: Callable[[Callable, tuple, dict], str] = None,
    request_id_generator: Callable[[Callable, tuple, dict], str] = None,
    reset_trace_id: bool = False,
    reset_request_id: bool = False,
) -> DecoratorType:
    """
    Create a function decorator extracting context, or generating if not in kwargs.
    """

    def decorator(func):
        def decorated_func(*args, **kwargs):
            trace_id_token = None
            request_id_token = None
            if 'trace_id' in kwargs:
                trace_id_token = correlation_id_ctx.set(kwargs.pop('trace_id'))
            elif 'correlation_id' in kwargs:
                trace_id_token = correlation_id_ctx.set(kwargs.pop('correlation_id'))
            elif trace_id_generator:
                trace_id_token = correlation_id_ctx.set(trace_id_generator(func, *args, **kwargs))
            if 'request_id' in kwargs:
                request_id_token = request_id_ctx.set(kwargs.pop('request_id'))
            elif request_id_generator:
                request_id_token = request_id_ctx.set(request_id_generator(func, *args, **kwargs))

            logger.info(f'Extracted context from function kwargs for func {func.__name__}')

            result = func(*args, **kwargs)

            if trace_id_token and reset_trace_id:
                correlation_id_ctx.reset(trace_id_token)
            if request_id_token and reset_request_id:
                request_id_ctx.reset(request_id_token)

            return result

        return decorated_func

    return decorator


def generate_simple_id(prefix, content):
    """
    Create a context is string with "prefix:content:encoded_date:random"
    """
    ts_now = datetime.now(timezone.utc).timestamp()
    ts_2k = datetime(2000, 1, 1, tzinfo=timezone.utc).timestamp()
    ts2000res65536 = int(65536 * (ts_now - ts_2k)).to_bytes(6, 'big')
    date = b64encode(ts2000res65536, b'_-').decode('ascii')
    random = token_urlsafe(3)
    id = f'{prefix}:{content}:{date}:{random}'
    logger.debug(f'Generated context id: {id}')
    return id


def simple_func_id_generator(namespace: str = 'default_namespace'):
    def id_generator(func: Callable, *args, **kwargs):
        return generate_simple_id(namespace, func.__name__)

    return id_generator
