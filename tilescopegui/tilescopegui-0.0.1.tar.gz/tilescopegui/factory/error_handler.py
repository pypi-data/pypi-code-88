import traceback
from typing import Callable

from flask import Response
from werkzeug.exceptions import HTTPException


def get_error_handler(debug: bool = False) -> Callable[[Exception], Response]:
    """Get error handler."""
    if debug:
        return _debug_handler
    return _production_handler


def _debug_handler(exc: Exception) -> Response:
    if not isinstance(exc, HTTPException):
        traceback.print_exc()
    return _production_handler(exc)


def _production_handler(exc: Exception) -> Response:
    return Response(
        status=exc.code if isinstance(exc, HTTPException) else 500,
        mimetype="application/json",
    )
