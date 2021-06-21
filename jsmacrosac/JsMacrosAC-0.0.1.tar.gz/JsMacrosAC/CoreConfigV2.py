
class CoreConfigV2(Object, ):

    defaultProfile: str = None
    profiles: list = None
    extraJsOptions: list = None


    def __init__():
        pass


    def getCurrentProfile(self, ) -> str:
        pass

    def setCurrentProfile(self, pname: str, ) -> None:
        pass

    def profileOptions(self, ) -> list:
        pass

    def fromV1(self, v1: JsonObject, ) -> None:
        pass


    pass
