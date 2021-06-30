# coding: utf-8
# Copyright (c) Qotto, 2021

import logging
from base64 import b64encode
from datetime import datetime, timezone
from secrets import token_urlsafe
from typing import Callable

from ..context import EventyContext

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
    context: EventyContext,
    generator: Callable[[Callable, tuple, dict], str],
    reset: bool = False,
    fetch: bool = True,
) -> DecoratorType:
    def decorator(func):
        def decorated_func(*args, **kwargs):
            token = None
            if context.name in kwargs and fetch:
                token = context.set(kwargs.pop(context.name))
                logger.debug(f'Extracted {context.name} from {func.__name__} kwargs')
            elif generator:
                token = context.set(generator(func, *args, **kwargs))
                logger.debug(f'Generated {context.name} for {func.__name__}')
            else:
                logger.debug(f'No {context.name} for {func.__name__}')

            result = func(*args, **kwargs)

            if token and reset:
                prev = context.reset(token)
                logger.debug(f'Reset {context.name} for {func.__name__} (was: {prev})')

            return result

        renamed_decorated_func = decorated_func
        renamed_decorated_func.__name__ = func.__name__
        return renamed_decorated_func

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
