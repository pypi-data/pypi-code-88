from .OverlayContainer import *
from .IOverlayParent import *

class IContainerParent():



    def addButton(self, button: T, ) -> T:
        pass

    def removeButton(self, button: AbstractButtonWidget, ) -> None:
        pass

    def openOverlay(self, overlay: OverlayContainer, ) -> None:
        pass

    def openOverlay(self, overlay: OverlayContainer, disableButtons: bool, ) -> None:
        pass

    def getFirstOverlayParent(self, ) -> IOverlayParent:
        pass


    pass
