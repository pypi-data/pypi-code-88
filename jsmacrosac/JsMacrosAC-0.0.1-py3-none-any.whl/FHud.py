from .IDraw2D import *
from .BaseLibrary import *
from .Draw3D import *
from .IScreen import *
from .Draw2D import *

class FHud(BaseLibrary, ):

    overlays: list = None
    renders: list = None


    def createScreen(self, title: str, dirtBG: bool, ) -> IScreen:
        pass

    def openScreen(self, s: IScreen, ) -> None:
        pass

    def getOpenScreen(self, ) -> IScreen:
        pass

    def getOpenScreenName(self, ) -> str:
        pass

    def isContainer(self, ) -> bool:
        pass

    def createDraw2D(self, ) -> IDraw2D:
        pass

    def registerDraw2D(self, overlay: IDraw2D, ) -> None:
        pass

    def unregisterDraw2D(self, overlay: Draw2D, ) -> None:
        pass

    def listDraw2Ds(self, ) -> list:
        pass

    def clearDraw2Ds(self, ) -> None:
        pass

    def createDraw3D(self, ) -> Draw3D:
        pass

    def registerDraw3D(self, draw: Draw3D, ) -> None:
        pass

    def unregisterDraw3D(self, draw: Draw3D, ) -> None:
        pass

    def listDraw3Ds(self, ) -> list:
        pass

    def clearDraw3Ds(self, ) -> None:
        pass

    def getMouseX(self, ) -> float:
        pass

    def getMouseY(self, ) -> float:
        pass


    pass
