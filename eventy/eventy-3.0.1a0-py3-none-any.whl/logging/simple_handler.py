# coding: utf-8
# Copyright (c) Qotto, 2021

from coloredlogs import ColoredFormatter

from eventy.logging.context_filters import add_trace_id_filter, add_request_id_filter
from logging import Formatter, StreamHandler


class SimpleHandler(StreamHandler):
    def __init__(
        self,
        fmt='%(asctime)s [TID:%(trace_id)s] [RID:%(request_id)s] '
            '%(levelname)s %(name)s (%(module)s L%(lineno)d) '
            '%(message)s',
        datefmt='[%Y-%m-%d %H:%M:%S %z]',
        colored=False,
        stream=None,
        level='DEBUG',
    ):
        super().__init__(stream)
        self.addFilter(add_trace_id_filter)
        self.addFilter(add_request_id_filter)
        if colored:
            self.setFormatter(ColoredFormatter(fmt=fmt, datefmt=datefmt))
        else:
            self.setFormatter(Formatter(fmt=fmt, datefmt=datefmt))
        self.setLevel(level=level)
