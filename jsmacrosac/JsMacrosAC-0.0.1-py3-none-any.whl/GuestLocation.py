from .SourceLocation import *

class GuestLocation(SourceLocation, ):

    file: File = None
    line: int = None
    column: int = None
    startIndex: int = None
    endIndex: int = None


    def __init__(file: File, startIndex: int, endIndex: int, line: int, column: int, ):
        pass


    def toString(self, ) -> str:
        pass


    pass
