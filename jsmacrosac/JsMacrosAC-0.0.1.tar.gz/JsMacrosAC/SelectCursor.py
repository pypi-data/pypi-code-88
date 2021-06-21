
class SelectCursor(Object, ):

    onChange: Consumer = None
    defaultStyle: Style = None
    startLine: int = None
    endLine: int = None
    startIndex: int = None
    endIndex: int = None
    startLineIndex: int = None
    endLineIndex: int = None
    dragStartIndex: int = None
    arrowLineIndex: int = None
    arrowEnd: bool = None
    startCol: int = None
    endCol: int = None


    def __init__(defaultStyle: Style, ):
        pass


    def updateStartIndex(self, startIndex: int, current: str, ) -> None:
        pass

    def updateEndIndex(self, endIndex: int, current: str, ) -> None:
        pass


    pass
