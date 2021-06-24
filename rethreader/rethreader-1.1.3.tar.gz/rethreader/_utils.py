from collections import namedtuple

Key = namedtuple("Key", ["id", "target", "args", "kwargs"])
missing = object()


def is_collection(self) -> bool:
    return isinstance(self, list) or isinstance(self, tuple)


def is_partial(self: tuple) -> bool:
    return isinstance(self, tuple) and len(self) == 3 and \
           callable(self[0]) and type(self[1]) == tuple and type(self[2]) == dict


def is_unpacked(self: tuple) -> bool:
    if type(self) == Key:
        return True
    return isinstance(self, tuple) and isinstance(self[0], (int, type(None))) and is_partial(self[1:])


class FakeSet:
    def __bool__(self):
        return False

    def add(self, other):
        pass

    def clear(self):
        pass


class Description:
    def __init__(self, string: str):
        super().__init__()
        self.string = str(string)

    def __eq__(self, other):
        return type(self) == type(other) and str.__eq__(self.string, other.string)

    def __str__(self):
        return self.string

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.string}')"


thread_info_descriptor = Description("Thread Info")


class ThreadInfo(Description):
    def __init__(self, k, sep=None):
        _sep = sep or '; '
        _, a, b, c = k
        tup = str(a), str(b), str(c)

        def cond():
            return any(map(lambda x: _sep in x, tup))

        if sep and cond():
            raise ValueError('An argument contains the separator')
        while cond():
            _sep = ';' + _sep
        string = _sep.join(str(i) for i in tup)
        super(ThreadInfo, self).__init__(string)
        self.sep = _sep

    def key(self):
        return Key(thread_info_descriptor, *self.string.split(self.sep))

    @classmethod
    def of(cls, self):
        if hasattr(self, 'info'):
            return self.info
        elif is_unpacked(self):
            return cls(self)


def null(*args, **kwargs): pass
