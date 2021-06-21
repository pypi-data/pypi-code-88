from .ScriptContext import *

class ContextContainer(Object, ):



    def __init__(ctx: ScriptContext, ):
        pass


    def setLockThread(self, lockThread: Thread, ) -> None:
        pass

    def getCtx(self, ) -> ScriptContext:
        pass

    def getLockThread(self, ) -> Thread:
        pass

    def awaitLock(self, ) -> None:
        pass

    def releaseLock(self, ) -> None:
        pass


    pass
