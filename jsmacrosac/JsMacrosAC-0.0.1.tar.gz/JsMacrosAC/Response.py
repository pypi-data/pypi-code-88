
class Response(Object, ):

    headers: list = None
    responseCode: int = None


    def __init__(inputStream: InputStream, responseCode: int, headers: list, ):
        pass


    def text(self, ) -> str:
        pass

    def json(self, ) -> Object:
        pass

    def byteArray(self, ) -> byte:
        pass


    pass
