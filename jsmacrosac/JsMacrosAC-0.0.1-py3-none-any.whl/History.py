from .SelectCursor import *

class History(Object, ):

    onChange: Consumer = None
    current: str = None


    def __init__(start: str, cursor: SelectCursor, ):
        pass


    def addChar(self, position: int, content: char, ) -> bool:
        pass

    def add(self, position: int, content: str, ) -> bool:
        pass

    def deletePos(self, position: int, length: int, ) -> bool:
        pass

    def bkspacePos(self, position: int, length: int, ) -> bool:
        pass

    def shiftLine(self, startLine: int, lines: int, shiftDown: bool, ) -> bool:
        pass

    def replace(self, position: int, length: int, content: str, ) -> None:
        pass

    def tabLines(self, startLine: int, lineCount: int, reverse: bool, ) -> None:
        pass

    def undo(self, ) -> int:
        pass

    def redo(self, ) -> int:
        pass


    pass
