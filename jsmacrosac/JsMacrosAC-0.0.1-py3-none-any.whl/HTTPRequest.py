from .Response import *

class HTTPRequest(Object, ):

    headers: list = None
    conn: URL = None


    def __init__(url: str, ):
        pass


    def addHeader(self, key: str, value: str, ) -> self:
        pass

    def get(self, ) -> Response:
        pass

    def post(self, data: str, ) -> Response:
        pass


    pass
