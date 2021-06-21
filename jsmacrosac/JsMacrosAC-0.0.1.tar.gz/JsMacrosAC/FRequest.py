from .BaseLibrary import *
from .HTTPRequest import *
from .Websocket import *
from .Response import *

class FRequest(BaseLibrary, ):



    def create(self, url: str, ) -> HTTPRequest:
        pass

    def get(self, url: str, ) -> Response:
        pass

    def get(self, url: str, headers: list, ) -> Response:
        pass

    def post(self, url: str, data: str, ) -> Response:
        pass

    def post(self, url: str, data: str, headers: list, ) -> Response:
        pass

    def createWS(self, url: str, ) -> Websocket:
        pass

    def createWS2(self, url: str, ) -> Websocket:
        pass


    pass
