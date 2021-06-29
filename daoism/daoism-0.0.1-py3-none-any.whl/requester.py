from .model import BaseAPIModel, TransModel, OcrModel
from .auth import Auth
import httpx


class OnlyOneQueryException(Exception):
    pass


class Connector:

    model: BaseAPIModel

    def __init__(self, auth: Auth) -> None:
        self.auth = auth
        self.data = {}
        self.data.update(self.model.config)

    def _build_data(self, **kwargs):
        # Very stupid way to check whether q or img exist
        keys = kwargs.keys()
        if len(keys) > 1:
            raise OnlyOneQueryException("No! Only one query")
        # q = list(kwargs.items())[0][1]
        q = list(kwargs.values())[0]
        self.data.update(kwargs)
        self.data.update(self.auth.get_auth(q))

        print(self.data)

    def sync_connect(self, **kwargs):
        self._build_data(**kwargs)
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        result = httpx.post(self.model.API, data=self.data, headers=headers)
        return result.json()

    async def async_connect(self):
        pass


class TranslateConnector(Connector):
    model = TransModel()

    def search(self, q):
        result = self.sync_connect(q=q)
        return result

    async def async_search(self, q):
        pass


class TextOcrConnector(Connector):
    model = OcrModel()

    def upload(self, q):
        result = self.sync_connect(img=q)
        return result
