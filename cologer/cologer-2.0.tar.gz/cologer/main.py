from cologer.level import Level

class Cologer:
    """
    formatter:
        {time}      当前时间
        {filename}  文件名
        {lineno}    行号
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst = super().__new__(cls, *args, **kwargs)
        return cls._inst

    def __init__(self) -> None:
        self._fmt = '{time} | {level} | {message}'
        self.debug = Level('debug', self._fmt)
        self.info = Level('info', self._fmt)
        self.success = Level('success', self._fmt)
        self.warning = Level('warning', self._fmt)
        self.error = Level('error', self._fmt)

    @property
    def levels(self):
        return [L for L in self.__dict__.values() if isinstance(L, Level)]
    
    def set_format(self, fmt: str):
        self._fmt = fmt
        for L in self.levels:
            setattr(self, L.name.lower(), Level(L.name, self._fmt))

    def add_level(self, name: str):
        lv = Level(name, self._fmt)
        setattr(self, name, lv)
        return lv

    def set_field_fore(self, **kwargs):
        for l in self.levels:
            for k, v in kwargs.items():
                getattr(l.fields, k).set_fore(v)

    def set_field_back(self, **kwargs):
        for l in self.levels:
            for k, v in kwargs.items():
                getattr(l.fields, k).set_back(v)

    def set_field_style(self, **kwargs):
        for l in self.levels:
            for k, v in kwargs.items():
                getattr(l.fields, k).set_style(v)

    def set_field_default(self, **kwargs):
        for l in self.levels:
            for k, v in kwargs.items():
                getattr(l.fields, k).set_default(v)

    def __call__(self, level: Level = None):
        def wrap(func):
            if isinstance(level, Level):
                level._hook = func
            elif level is None:
                for l in self.levels:
                        l._hook = func
        return wrap
