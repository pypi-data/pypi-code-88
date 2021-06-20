from importlib import import_module

from ..settings.config import Config


class Handlers:
    @staticmethod
    def get_handlers():
        handlers = []
        for key, values in Config.get_handlers().items():
            module = import_module(key.replace("/", "."))
            for handler in values:
                handlers.append(getattr(module, handler))
        return handlers
