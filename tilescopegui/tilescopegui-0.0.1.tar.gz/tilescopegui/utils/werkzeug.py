import logging
import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flask import Request


def quiet_mode() -> None:
    """Remove the logging from Werkzeug."""
    logging.getLogger("werkzeug").disabled = True
    os.environ["WERKZEUG_RUN_MAIN"] = "true"


def kill_server(request: "Request") -> None:
    """Shut down the server."""
    terminate_func = request.environ.get("werkzeug.server.shutdown")
    if terminate_func:
        terminate_func()
