import ctypes
from threading import Thread
from typing import Union, Optional
from ._utils import Key, Description, ThreadInfo, thread_info_descriptor, null

no_id = Description("No Id")
not_returned = Description("Not Returned")


class KeyThread(Thread):
    def __init__(self, k: Union[int, Description] = None, target: callable = null, args: tuple = (),
                 kwargs: Optional[dict] = None, daemon: Optional[bool] = None):
        assert k != thread_info_descriptor
        if k is None:
            k = no_id
        if kwargs is None:
            kwargs = {}
        self.id, self._target, self._args, self._kwargs = k, target, args, kwargs
        self._result = not_returned
        super(KeyThread, self).__init__(target=target, args=args, kwargs=kwargs, daemon=daemon)

    def __bool__(self):
        return self._target != null

    @classmethod
    def of(cls, k: Key, d=None):
        return cls(*k, d)

    @property
    def key(self):
        return Key(self.id, self._target, self._args, self._kwargs)

    @property
    def info(self):
        return ThreadInfo(self.key)

    def kill(self):
        if self.is_alive():
            res = ctypes.pythonapi.PyThreadState_SetAsyncExc(self.ident, ctypes.py_object(SystemExit))
            if res > 1:
                ctypes.pythonapi.PyThreadState_SetAsyncExc(self.ident, 0)
        self.join(0)
        return self

    @property
    def returned(self):
        return self._result != not_returned

    @property
    def result(self):
        if self.returned:
            return self._result

    def run(self):
        self._result = self._target(*self._args, **self._kwargs)
        return self

    def start(self):
        super(KeyThread, self).start()
        return self
