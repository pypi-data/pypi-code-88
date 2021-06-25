# coding: utf-8
# Copyright (c) Qotto, 2021

import json
import math

import logging
from eventy.context import trace_id_ctx, request_id_ctx
from eventy.logging.context_filters import add_trace_id_filter, add_request_id_filter


class GkeHandler(logging.StreamHandler):
    def __init__(self, stream=None, level='DEBUG'):
        super().__init__(stream)
        self.addFilter(add_trace_id_filter)
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
        if trace_id_ctx.is_defined():
            payload['trace_id'] = trace_id_ctx.get()
        if request_id_ctx.is_defined():
            payload['request_id'] = request_id_ctx.get()
        return json.dumps(payload)
