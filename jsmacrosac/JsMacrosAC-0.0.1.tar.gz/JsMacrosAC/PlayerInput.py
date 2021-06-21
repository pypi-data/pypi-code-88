
class PlayerInput(Object, ):

    movementForward: float = None
    movementSideways: float = None
    yaw: float = None
    pitch: float = None
    jumping: bool = None
    sneaking: bool = None
    sprinting: bool = None


    def __init__(movementForward: float, movementSideways: float, yaw: float, ):
        pass


    def fromCsv(self, csv: str, ) -> list:
        pass

    def fromJson(self, json: str, ) -> self:
        pass

    def toString(self, varNames: bool, ) -> str:
        pass

    def toString(self, ) -> str:
        pass

    def clone(self, ) -> self:
        pass


    pass
