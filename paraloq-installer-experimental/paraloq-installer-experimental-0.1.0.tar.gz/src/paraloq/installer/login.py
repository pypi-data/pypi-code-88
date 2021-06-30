import time

from fastapi import FastAPI, Query
from starlette.responses import RedirectResponse
from uvicorn import Config

from paraloq.companion.server import Server


login_app = FastAPI(title="paraloq Companion Login Server", version="0.1.0")


class LoginServer(Server):
    auth_code: str = None

    def __init__(self):
        config = Config(login_app, host="127.0.0.1", port=8085, log_level="critical")
        super(LoginServer, self).__init__(config=config)

    def serve_once(self):
        super(LoginServer, self).run_in_thread()
        old_code = self.auth_code
        while self.auth_code is old_code:
            time.sleep(0.1)
        self.stop()
        return self.auth_code


@login_app.get("/")
def _receive_auth_code(code: str = Query(None)):
    LoginServer.auth_code = code
    return RedirectResponse(url="https://www.paraloq.at")
