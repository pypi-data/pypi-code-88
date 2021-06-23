import requests

from typing import Union


class UnsupportedGitServer(Exception):
    """Unsupported git server"""

    pass


class HttpException(Exception):
    """An HTTP error occured"""

    pass


class Session:
    def __init__(
        self,
        servertype: str,
        url: str,
        username: Union[None, str],
        secret: Union[None, str],
    ):
        self.servertype = servertype.lower()
        self.url = url
        self.username = username
        self.secret = secret
        if self.servertype.lower() not in self.supported_servers:
            raise UnsupportedGitServer(f"Unsupported git server: {self.servertype}")

    @staticmethod
    def join_url(url, path):
        return "/".join((url.rstrip("/"), path.lstrip("/")))

    def httpaction(self, http_verb: str, path: str, xstatus: int = 200, **kwargs: str):
        http_verb = getattr(requests, http_verb.lower())
        auth = None
        if not self.auth_headers:
            auth = (self.username, self.secret)
        response = http_verb(
            Session.join_url(self.url, path),
            headers={**(self.auth_headers or {}), **kwargs.get("headers", {})},
            data=kwargs.get("data"),
            auth=auth,
        )
        if response.status_code == xstatus:
            return response
        else:
            raise requests.exceptions.HTTPError(
                {
                    "msg": f"Unsuccesful GET operation. response = {response.text}",
                    "code": response.status_code,
                    "response": response,
                }
            )

    @property
    def supported_servers(self) -> str:
        return ["gitlab", "github", "gitea", "stash"]

    @property
    def auth_headers(self):
        if self.servertype == "gitlab":
            return {"Private-Token": self.secret}
        elif self.servertype in ("github", "gitea"):
            return {"Authorization": f"token {self.secret}"}
        return None
