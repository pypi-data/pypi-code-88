from .SourceLocation import *

class BaseWrappedException(Object, ):

    stackFrame: T = None
    location: SourceLocation = None
    message: str = None
    next: self = None


    def __init__(exception: T, message: str, location: SourceLocation, next: self, ):
        pass


    def wrapHostElement(self, t: StackTraceElement, next: self, ) -> self:
        pass


    pass
