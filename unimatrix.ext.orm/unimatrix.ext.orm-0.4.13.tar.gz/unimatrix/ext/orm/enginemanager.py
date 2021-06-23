"""Declares :class:`EngineManager`."""
import asyncio
import inspect
import threading


class EngineManager:
    """Confines the connections dictionary to the local thread scope."""

    @property
    def engines(self):
        return self.__local.engines

    @property
    def loop(self):
        if self.__loop:
            # This is for testing purposes only.
            return self.__loop
        try:
            return asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return loop

    def __init__(self, engines=None, loop=None):
        self.__local = threading.local()
        self.__local.engines = engines or {}
        self.__loop = loop
        self.keys = self.engines.keys
        self.pop = self.engines.pop

    def destroy(self, loop=None):
        """Destroys all known engines."""
        loop = loop or self.loop
        for name in list(dict.keys(self.engines)):
            engine = self.engines.pop(name)
            result = engine.dispose()
            if inspect.iscoroutine(result) and loop.is_running():
                loop.run_until_complete(result)

    def __len__(self):
        return len(self.engines)

    def __getitem__(self, key):
        return dict.get(self.engines, key)

    def __setitem__(self, key, value):
        return self.engines.__setitem__(key, value)

    def __iter__(self):
        return iter(self.engines)
