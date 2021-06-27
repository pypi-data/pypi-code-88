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
    if trace_id_ctx.is_defined():
        task_kwargs.update(trace_id=trace_id_ctx.get())
        logger.debug('Added trace_id in task')
    else:
        logger.debug('No trace_id in task')

    if request_id_ctx.is_defined():
        task_kwargs.update(request_id=request_id_ctx.get())
        logger.debug('Added request_id in task')
    else:
        logger.debug('No request_id in task')

    return send_task(task_name, task_args, task_kwargs, *args, **kwargs)


def with_namespace(celery_decorator, namespace: str) -> DecoratorType:
    """
    Wraps celery task and share_task decorators to include namespace in task name
    """

    def namespaced(*args, **kwargs) -> DecoratorType:
        def namespaced_func(func: Callable):
            full_name = f'{namespace}.tasks.{func.__name__}'
            kwargs['name'] = full_name
            return celery_decorator(*args, **kwargs)(func)

        return namespaced_func

    return namespaced
