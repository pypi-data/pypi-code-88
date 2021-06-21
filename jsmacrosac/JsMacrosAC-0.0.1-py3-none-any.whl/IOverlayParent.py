from .OverlayContainer import *

class IOverlayParent():



    def closeOverlay(self, overlay: OverlayContainer, ) -> None:
        pass

    def setFocused(self, focused: Element, ) -> None:
        pass

    def getChildOverlay(self, ) -> OverlayContainer:
        pass


    pass
