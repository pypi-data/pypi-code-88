# coding: utf-8
# Copyright (c) Qotto, 2021

import json
import logging
import math

from .context_filters import add_correlation_id_filter, add_request_id_filter
from ..context import correlation_id_ctx, request_id_ctx


class GkeHandler(logging.StreamHandler):
    def __init__(self, stream=None, level='DEBUG'):
        super().__init__(stream)
        self.addFilter(add_correlation_id_filter)
        self.addFilter(add_request_id_filter)
        self.setLevel(level=level)

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)

        subsecond, second = math.modf(record.created)
        payload = {
            'timestamp': {'seconds': int(second), 'nanos': int(subsecond * 1e9)},
            'severity': record.levelname,
            'message': message,
            'file': record.pathname,
            'line': record.lineno,
            'module': record.module,
            'function': record.funcName,
            'logger_name': record.name,
            'thread': record.thread,
        }
        if correlation_id_ctx.is_defined():
            payload['correlation_id'] = correlation_id_ctx.get()
        if request_id_ctx.is_defined():
            payload['request_id'] = request_id_ctx.get()
        return json.dumps(payload)
