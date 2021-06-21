from .MethodWrapper import *
from .TextHelper import *
from .ItemStackHelper import *
from .EntityHelper import *

class TextBuilder(Object, ):



    def __init__():
        pass


    def append(self, text: Object, ) -> self:
        pass

    def withColor(self, color: int, ) -> self:
        pass

    def withColor(self, r: int, g: int, b: int, ) -> self:
        pass

    def withFormatting(self, underline: bool, bold: bool, italic: bool, strikethrough: bool, magic: bool, ) -> self:
        pass

    def withShowTextHover(self, text: TextHelper, ) -> self:
        pass

    def withShowItemHover(self, item: ItemStackHelper, ) -> self:
        pass

    def withShowEntityHover(self, entity: EntityHelper, ) -> self:
        pass

    def withCustomClickEvent(self, action: MethodWrapper, ) -> self:
        pass

    def withClickEvent(self, action: str, value: str, ) -> self:
        pass

    def build(self, ) -> TextHelper:
        pass


    pass
