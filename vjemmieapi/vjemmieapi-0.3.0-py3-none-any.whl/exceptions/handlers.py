import socket

from fastapi import Request
from fastapi.applications import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from starlette.responses import PlainTextResponse
from ..cache import cache, MockCache


async def handle_integrity_error(request: Request, exc: IntegrityError):
    if hasattr(exc.orig, "args") and exc.orig.args[0] == 1062:
        return PlainTextResponse("Resource already exists.", status_code=400)
    else:
        raise exc


async def handle_socket_gaierror(request: Request, exc: socket.gaierror):
    global cache
    cache = MockCache()
    return PlainTextResponse("Invalid cache, try again.", status_code=500)


HANDLERS = {
    IntegrityError: handle_integrity_error,
    socket.gaierror: handle_socket_gaierror,
}


def add_exception_handlers(app: FastAPI):
    for exc, handler in HANDLERS.items():
        app.add_exception_handler(exc, handler)
