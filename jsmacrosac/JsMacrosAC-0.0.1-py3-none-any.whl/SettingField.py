from .Option import *

class SettingField(Object, ):

    type: Class = None
    option: Option = None


    def __init__(option: Option, containingClass: Object, f: Field, getter: Method, setter: Method, type: Class, ):
        pass


    def set(self, o: T, ) -> None:
        pass

    def get(self, ) -> T:
        pass

    def hasOptions(self, ) -> bool:
        pass

    def getOptions(self, ) -> list:
        pass

    def isSimple(self, ) -> bool:
        pass


    pass
