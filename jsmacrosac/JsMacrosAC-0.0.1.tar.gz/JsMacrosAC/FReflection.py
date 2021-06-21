from .BaseLibrary import *
from .Mappings import *

class FReflection(BaseLibrary, ):



    def getClass(self, name: str, ) -> Class:
        pass

    def getClass(self, name: str, name2: str, ) -> Class:
        pass

    def getDeclaredMethod(self, c: Class, name: str, parameterTypes: Class, ) -> Method:
        pass

    def getDeclaredMethod(self, c: Class, name: str, name2: str, parameterTypes: Class, ) -> Method:
        pass

    def getDeclaredField(self, c: Class, name: str, ) -> Field:
        pass

    def getDeclaredField(self, c: Class, name: str, name2: str, ) -> Field:
        pass

    def invokeMethod(self, m: Method, c: Object, objects: Object, ) -> Object:
        pass

    def newInstance(self, c: Class, objects: Object, ) -> T:
        pass

    def loadJarFile(self, file: str, ) -> bool:
        pass

    def loadCurrentMappingHelper(self, ) -> Mappings:
        pass

    def getClassName(self, o: Object, ) -> str:
        pass

    def loadMappingHelper(self, urlorfile: str, ) -> Mappings:
        pass


    pass
