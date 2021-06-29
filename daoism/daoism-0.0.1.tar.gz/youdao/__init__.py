from .auth import Auth
from .requester import TranslateConnector, TextOcrConnector


class YouDao:
    def __init__(self, key, secret) -> None:
        # self.auth = Auth(key=key, secret=secret)
        self.key = key
        self.secret = secret

    def translator(self):
        auth = Auth(key=self.key, secret=self.secret)
        return TranslateConnector(auth)

    def ocr(self):
        auth = Auth(key=self.key, secret=self.secret)
        return TextOcrConnector(auth)
