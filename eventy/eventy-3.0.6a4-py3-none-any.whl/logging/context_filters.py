# coding: utf-8
# Copyright (c) Qotto, 2021

from logging import LogRecord

from ..context import correlation_id_ctx, request_id_ctx


def add_correlation_id_filter(log_record: LogRecord) -> bool:
    log_record.correlation_id = correlation_id_ctx.get()  # type: ignore
    return True


def add_request_id_filter(log_record: LogRecord) -> bool:
    log_record.request_id = request_id_ctx.get()  # type: ignore
    return True
