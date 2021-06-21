from .IOverlayParent import *
from .OverlayContainer import *

class EventChooser(OverlayContainer, ):



    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, selected: str, parent: IOverlayParent, setEvent: Consumer, ):
        pass


    def selectEvent(self, event: str, ) -> None:
        pass

    def init(self, ) -> None:
        pass

    def addEvent(self, eventName: str, ) -> None:
        pass

    def updateEventPos(self, ) -> None:
        pass

    def onScrollbar(self, page: float, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
