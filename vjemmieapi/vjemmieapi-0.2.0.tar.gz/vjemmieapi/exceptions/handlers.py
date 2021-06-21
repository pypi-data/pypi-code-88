from fastapi.applications import FastAPI
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.responses import PlainTextResponse


async def handle_integrity_error(request: Request, exc: IntegrityError):
    if hasattr(exc.orig, "args") and exc.orig.args[0] == 1062:
        return PlainTextResponse("Resource already exists.", status_code=400)
    else:
        raise exc


HANDLERS = {
    IntegrityError: handle_integrity_error,
}


def add_exception_handlers(app: FastAPI):
    for exc, handler in HANDLERS.items():
        app.add_exception_handler(exc, handler)
