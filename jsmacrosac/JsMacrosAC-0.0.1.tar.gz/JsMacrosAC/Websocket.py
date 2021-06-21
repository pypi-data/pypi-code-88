from .MethodWrapper import *

class Websocket(Object, ):

    onConnect: MethodWrapper = None
    onTextMessage: MethodWrapper = None
    onDisconnect: MethodWrapper = None
    onError: MethodWrapper = None
    onFrame: MethodWrapper = None


    def __init__(address: str, ):
        pass


    def connect(self, ) -> self:
        pass

    def getWs(self, ) -> WebSocket:
        pass

    def sendText(self, text: str, ) -> self:
        pass

    def close(self, ) -> self:
        pass

    def close(self, closeCode: int, ) -> self:
        pass


    pass
