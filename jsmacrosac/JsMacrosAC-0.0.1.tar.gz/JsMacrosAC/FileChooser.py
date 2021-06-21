from .IOverlayParent import *
from .fileObj import *
from .OverlayContainer import *

class FileChooser(OverlayContainer, ):

    root: File = None


    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, directory: File, selected: File, parent: IOverlayParent, setFile: Consumer, editFile: Consumer, ):
        pass


    def setDir(self, dir: File, ) -> None:
        pass

    def selectFile(self, f: File, ) -> None:
        pass

    def init(self, ) -> None:
        pass

    def addFile(self, f: File, ) -> None:
        pass

    def addFile(self, f: File, btnText: str, ) -> None:
        pass

    def updateFilePos(self, ) -> None:
        pass

    def confirmDelete(self, f: fileObj, ) -> None:
        pass

    def delete(self, f: fileObj, ) -> None:
        pass

    def onScrollbar(self, page: float, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
