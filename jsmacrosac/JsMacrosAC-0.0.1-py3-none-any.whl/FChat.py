from .TextHelper import *
from .TextBuilder import *
from .BaseLibrary import *

class FChat(BaseLibrary, ):



    def log(self, message: Object, ) -> None:
        pass

    def log(self, message: Object, await: bool, ) -> None:
        pass

    def say(self, message: str, ) -> None:
        pass

    def say(self, message: str, await: bool, ) -> None:
        pass

    def title(self, title: Object, subtitle: Object, fadeIn: int, remain: int, fadeOut: int, ) -> None:
        pass

    def actionbar(self, text: Object, tinted: bool, ) -> None:
        pass

    def toast(self, title: Object, desc: Object, ) -> None:
        pass

    def createTextHelperFromString(self, content: str, ) -> TextHelper:
        pass

    def createTextHelperFromJSON(self, json: str, ) -> TextHelper:
        pass

    def createTextBuilder(self, ) -> TextBuilder:
        pass


    pass
