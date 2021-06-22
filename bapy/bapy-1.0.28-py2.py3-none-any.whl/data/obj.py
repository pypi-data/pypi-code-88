__all__ = (
    'Environs',
    'PathLike',
    'ObjDictA',
    'ObjDictB',
    'ObjDictC',
    'ObjDataA',
    'ObjDataB',
    'ObjDataC',

)
from collections import OrderedDict
from dataclasses import dataclass
from dataclasses import field
from logging import getLogger
from logging import Logger
from pathlib import Path as PathLike
from typing import Any
from typing import NamedTuple

from environs import Env as Environs

Named = NamedTuple('Named', a=Any)
logger = getLogger(__name__)


class ObjDictA:
    _a = 'a'
    clsvar = 3
    logger = logger

    __ignore_attr__ = ['b', ]
    __ignore_copy__ = [OrderedDict, ]

    def __init__(self):
        super(ObjDictA, self).__init__()
        # self.env = Environs()
        self._b = 2
        self._d = 4

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return 'b'


class ObjDictB:
    _b = 'b'
    dict_a = ObjDictA()
    env = Environs()
    path = PathLike()


class ObjDictC:
    _a = 'a'
    clsvar = None
    f = None
    logger = getLogger()

    __ignore_attr__ = ['b', ]
    __ignore_copy__ = [OrderedDict, ]

    def __init__(self):
        super(ObjDictC, self).__init__()  # self.env = Environs()
        self._b = [None, None]
        self._d = {None, self.f}
        self._e = OrderedDict()
        self.f = 2

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return 'b'


@dataclass
class ObjDataA:
    a: str = 'a'
    dict_a: ObjDictA = ObjDictA()
    dictionary: dict = field(default_factory=dict)
    env: Environs = Environs()
    integer: int = field(default=int(), init=False)
    logger: Logger = logger
    path: PathLike = PathLike()


def factory():
    return [logger, ObjDataA(), PathLike(), Environs()]


@dataclass
class ObjDataB:
    b: str = 'b'
    data_a: ObjDataA = ObjDataA()
    dict_a: ObjDictA = ObjDictA()
    dictionary: dict = field(default_factory=dict)
    env: Environs = field(default_factory=Environs)
    integer: int = field(default=int(), init=False)
    logger: Logger = logger
    lst: list = field(default_factory=factory)
    named: Named = Named(ObjDataA)
    named_data_a: Named = Named(ObjDataA())
    path: PathLike = PathLike()

    def __post_init__(self):
        self.env.read_env()


@dataclass
class ObjDataC:
    _cprop: str = 'cprop'
    data_b: ObjDataB = ObjDataB()
    dict_a: ObjDictA = ObjDictA()
    dictionary: dict = field(default_factory=dict)
    env: Environs = field(default_factory=Environs)
    integer: int = field(default=int(), init=False)
    logger: Logger = logger
    path: PathLike = PathLike()

    __ignore_kwarg__ = ['path', ]

    def __post_init__(self):
        self.dictionary = dict(a=dict(__a='_a', _a='__a', a='__a'))

    @property
    def cprop(self):
        return self._cprop

