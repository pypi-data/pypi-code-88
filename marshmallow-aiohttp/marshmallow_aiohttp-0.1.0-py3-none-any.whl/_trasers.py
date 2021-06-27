import asyncio
import logging
import os
import types
from typing import Sequence

import aiohttp
import attr

__all__ = (
    "make_http_trace_config",
    "make_default_trace_configs",
)

MISSING = "-"

HTTP_LOGGER_NAME = os.getenv("MARSHMALLOW_AIOHTTP_HTTP_LOGGER_NAME", "http")


@attr.s(auto_attribs=True, slots=True, frozen=True)
class ClientLogger:
    _logger: logging.Logger
    _missing: str

    async def log(
        self,
        response: aiohttp.ClientResponse,
        request_time: float,
    ) -> None:
        extra = {
            "protocol": "HTTP/1.1",
            "method": response.method.upper(),
            "url": response.url,
            "content_type": response.content_type or self._missing,
            "content_length": response.content_length or self._missing,
            "charset": response.charset or self._missing,
            "reason": str(response.reason).title(),
            "response_code": response.status,
            "request_time": request_time,
        }
        self._logger.info("Received HTTP response", extra=extra)


def make_http_trace_config() -> aiohttp.TraceConfig:
    tracer = aiohttp.TraceConfig()
    logger = ClientLogger(logging.getLogger(HTTP_LOGGER_NAME), MISSING)

    async def start_request_timer(
        _: aiohttp.ClientSession,
        ctx: types.SimpleNamespace,
        __: aiohttp.TraceRequestStartParams,
    ) -> None:
        ctx.started_at = asyncio.get_event_loop().time()

    async def stop_request_timer(
        _: aiohttp.ClientSession,
        ctx: types.SimpleNamespace,
        params: aiohttp.TraceRequestEndParams,
    ) -> None:
        finished_at = asyncio.get_event_loop().time()
        request_time = finished_at - ctx.started_at
        await logger.log(params.response, request_time)

    tracer.on_request_start.append(start_request_timer)
    tracer.on_request_end.append(stop_request_timer)

    return tracer


def make_default_trace_configs() -> Sequence[aiohttp.TraceConfig]:
    return (
        make_http_trace_config(),
    )
