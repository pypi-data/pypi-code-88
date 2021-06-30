# coding: utf-8
# Copyright (c) Qotto, 2021

import logging
from typing import Callable, Any

from .common import DecoratorType, merge_decorators
from ..context import correlation_id_ctx

logger = logging.getLogger(__name__)

try:
    from celery.result import AsyncResult

    logger.debug("Celery support enabled")
except ImportError:
    AsyncResult = Any
    logger.debug("Celery support disabled")

__all__ = [
    'traced',
    'namespaced',
]


def traced(celery_send_task: Callable) -> Callable[[str, list, dict, ], AsyncResult]:
    """
    Wraps a celery send_task method, adding context to task_kwargs
    """

    def traced_send_task(task_name: str, task_args: list, task_kwargs: dict, *args, **kwargs) -> AsyncResult:
        """
        Modified version of celery.execute.send_task adding context in task kwargs
        """
        if correlation_id_ctx.is_defined():
            task_kwargs.update(trace_id=correlation_id_ctx.get())
            logger.debug('Added correlation_id in task kwargs')
        else:
            logger.debug('No correlation_id in context to add in task kwargs')

        return celery_send_task(task_name, task_args, task_kwargs, *args, **kwargs)

    return traced_send_task


def namespaced(namespace: str, celery_decorator, *other_decorators) -> DecoratorType:
    """
    Wraps celery task and share_task decorators to include namespace in task name
    """

    def auto_decorator(*decorator_args, **decorator_kwargs) -> DecoratorType:
        logger.debug(f'namespaced {celery_decorator.__name__} decorator_args={decorator_args} - decorator_kwargs={decorator_kwargs}')

        def decorator(func: Callable):
            def decorated_func(*func_args, **func_kwargs):
                full_name = f'{namespace}.tasks.{func.__name__}'
                decorator_kwargs.update(name=full_name)
                inner_func = merge_decorators(*other_decorators)(func)
                return celery_decorator(**decorator_kwargs)(inner_func)(*func_args, **func_kwargs)

            return decorated_func

        if len(decorator_args) == 1 and callable(decorator_args[0]):
            # @decorator
            # def f():
            return decorator(decorator_args[0])
        else:
            # @decorator(param=value)
            # def f():
            return decorator

    return auto_decorator
