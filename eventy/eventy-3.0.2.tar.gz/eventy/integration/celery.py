# coding: utf-8
# Copyright (c) Qotto, 2021

import logging
from typing import Callable

from celery.execute import send_task
from celery.result import AsyncResult

from eventy.context import trace_id_ctx, request_id_ctx
from eventy.integration.common import DecoratorType

logger = logging.getLogger(__name__)


def traced_send_task(task_name: str, task_args: list, task_kwargs: dict, *args, **kwargs) -> AsyncResult:
    """
    Modified version of celery.execute.send_task adding context in task kwargs
    """
    if trace_id_ctx.is_defined():
        task_kwargs.update(trace_id=trace_id_ctx.get())
        logger.debug('Added trace_id in task')
    else:
        logger.debug('No trace_id in context to add in task')

    if request_id_ctx.is_defined():
        task_kwargs.update(request_id=request_id_ctx.get())
        logger.debug('Added request_id in task')
    else:
        logger.debug('No request_id in context to add in task')

    return send_task(task_name, task_args, task_kwargs, *args, **kwargs)


def namespaced(namespace: str, celery_decorator) -> DecoratorType:
    """
    Wraps celery task and share_task decorators to include namespace in task name
    """

    def auto_decorator(*decorator_args, **decorator_kwargs) -> DecoratorType:
        logger.info(f'auto_decorator decorator_args={decorator_args} - decorator_kwargs={decorator_kwargs}')

        def decorator(func: Callable):
            def decorated_func(*func_args, **func_kwargs):
                full_name = f'{namespace}.tasks.{func.__name__}'
                decorator_kwargs.update(name=full_name)
                return celery_decorator(**decorator_kwargs)(func)(*func_args, **func_kwargs)

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
