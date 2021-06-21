from .LibraryRegistry import *
from .ConfigManager import *
from .BaseWrappedException import *
from .BaseEventRegistry import *
from .ScriptTrigger import *
from .BaseEvent import *
from .BaseLanguage import *
from .BaseProfile import *
from .ContextContainer import *

class Core(Object, ):

    instance: self = None
    eventRegistry: BaseEventRegistry = None
    profile: BaseProfile = None
    config: ConfigManager = None
    libraryRegistry: LibraryRegistry = None
    contexts: list = None
    threadContext: list = None
    languages: list = None
    defaultLang: BaseLanguage = None


    def createInstance(self, eventRegistryFunction: Function, profileFunction: Function, configFolder: File, macroFolder: File, logger: Logger, ) -> self:
        pass

    def addLanguage(self, l: BaseLanguage, ) -> None:
        pass

    def sortLanguages(self, ) -> None:
        pass

    def exec(self, macro: ScriptTrigger, event: BaseEvent, ) -> ContextContainer:
        pass

    def exec(self, macro: ScriptTrigger, event: BaseEvent, then: Runnable, catcher: Consumer, ) -> ContextContainer:
        pass

    def wrapException(self, ex: Throwable, ) -> BaseWrappedException:
        pass


    pass
