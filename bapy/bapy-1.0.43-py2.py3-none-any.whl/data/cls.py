__all__ = (
    'MroSlotsBase',
    'MroDictBase',
    'MroSlotsSub',
    'mro_slots_sub',

    'MroAsync',
    'mro_async',

    'MroData',
    'MroDataDictMix',
    'MroDataDictSlotMix',
    'mro_test_data_dict_slot_mix',

    'MroValuesBase',
    'MroValuesSub',
    'mro_values_sub',

    'DataAnnotations',
)
from dataclasses import dataclass
from dataclasses import field
from dataclasses import InitVar
from functools import cached_property
from types import GenericAlias
from typing import Any
from typing import ClassVar
from typing import Final
from typing import Literal
from typing import Optional
from typing import Union


class MroSlotsBase:
    __slots__ = ('mro_slots_base', )

    def __init__(self):
        self.mro_slots_base = 'mro_slots_base'


class MroDictBase(MroSlotsBase):

    def __init__(self):
        super().__init__()
        self.mro_dict_base = 'mro_dict_base'


class MroSlotsSub(MroDictBase):
    __slots__ = ('mro_slots_sub', )

    def __init__(self):
        super().__init__()
        self.mro_slots_sub = 'mro_slots_sub'


mro_slots_sub = MroSlotsSub()


class MroAsync:
    _async_classmethod = '_async_classmethod'
    _classmethod = '_classmethod'
    _async_method = '_async_method'
    _method = '_method'
    _cprop = '_cprop'
    _async_prop = '_async_prop'
    _prop = '_prop'
    _async_staticmethod = '_async_staticmethod'
    _staticmethod = '_staticmethod'

    @classmethod
    async def async_classmethod(cls): return cls._async_classmethod

    @classmethod
    def classmethod(cls): return cls._classmethod

    async def async_method(self): return self._async_method

    def method(self): return self._method

    @cached_property
    def cprop(self): return self._cprop

    @property
    async def async_prop(self): return self._async_prop

    @property
    def prop(self): return self._prop

    @staticmethod
    async def async_staticmethod(): return MroAsync._async_staticmethod

    @staticmethod
    def staticmethod(): return MroAsync._staticmethod


mro_async = MroAsync()


@dataclass
class MroData:
    __data = '__data'
    __dataclass_classvar__: ClassVar[str] = '__dataclass_classvar__'
    __dataclass_classvar: ClassVar[str] = '__dataclass_classvar'
    __dataclass_default_factory: Union[dict, str] = field(default_factory=dict, init=False)
    __dataclass_default_factory_init: Union[dict, str] = field(default_factory=dict)
    dataclass_classvar: ClassVar[str] = 'dataclass_classvar'
    dataclass_default_factory: Union[dict, str] = field(default_factory=dict, init=False)
    dataclass_default_factory_init: Union[dict, str] = field(default_factory=dict)
    dataclass_default: str = field(default='dataclass_default', init=False)
    dataclass_default_init: str = field(default='dataclass_default_init')
    dataclass_initvar: InitVar[str] = 'dataclass_initvar'
    dataclass_str: str = 'dataclass_integer'

    def __post_init__(self, dataclass_initvar): pass

    __class_getitem__ = classmethod(GenericAlias)


class MroDataDictMix(MroData):
    subclass_annotated_str: str = 'subclass_annotated_str'
    subclass_classvar: ClassVar[str] = 'subclass_classvar'
    subclass_str = 'subclass_str'

    def __init__(self, dataclass_initvar='dataclass_initvar_1', subclass_dynamic='subclass_dynamic'):
        super().__init__()
        super().__post_init__(dataclass_initvar=dataclass_initvar)
        self.subclass_dynamic = subclass_dynamic


class MroDataDictSlotMix(MroDataDictMix):
    __slots__ = ('_slot_property', 'slot',)

    # Add init=True dataclass attrs if it subclassed and not @dataclass
    def __init__(self, dataclass_initvar='dataclass_initvar_2', slot_property_initvar='slot_property_initvar',
                 slot_initvar='slot_initvar'):
        super().__init__()
        super().__post_init__(dataclass_initvar=dataclass_initvar)
        self._slot_property = slot_property_initvar
        self.slot = slot_initvar

    @property
    def slot_property(self):
        return self._slot_property


mro_test_data_dict_slot_mix = MroDataDictSlotMix()


class MroValuesBase:
    __slots__ = ('_hash', '_repr', '_test', 'missing')
    __ignore_hash__ = ('_repr', )
    __ignore_init__ = ('_repr', )
    __ignore_repr__ = ('_hash', 'test', )
    __ignore_state__ = ('_hash',)

    @property
    def test(self):
        return self._test


class MroValuesSub(MroValuesBase):
    __slots__ = ('_prop', '_slot', 'attr', 'init', 'init_ignore')
    __ignore_hash__ = ('_prop',)
    __ignore_init__ = ('init_ignore', )
    __ignore_repr__ = ('attr',)
    __ignore_state__ = ('attr',)

    def __init__(self, init, init_ignore='init_ignore'):
        self.init = init
        self.init_ignore = init_ignore


mro_values_sub = MroValuesSub(1)


@dataclass
class DataAnnotations:
    any: Any = 'any'
    classvar: ClassVar[str] = 'classvar'
    classvar_optional: ClassVar[Optional[str]] = 'classvar_optional'
    classvar_optional_union: ClassVar[Optional[Union[str, int]]] = 'classvar_optional_union'
    classvar_union: ClassVar[Union[str, int]] = 'classvar_union'
    final: Final = 'final'
    final_str: Final[str] = 'final_str'
    integer: int = 1
    initvar: InitVar[str] = 'initvar'
    initvar_optional: InitVar[Optional[str]] = 'initvar_optional'
    literal: Literal['literal', 'literal2'] = 'literal2'
    literal_optional: Optional[Literal['literal_optional', 'literal_optional2']] = 'literal_optional2'
    optional: Optional[str] = 'optional'
    union: Union[str, int] = 1
    optional_union: Optional[Union[str, bool]] = True

    # noinspection PyUnusedLocal
    def __post_init__(self, initvar: int, initvar_optional: Optional[int]):
        self.a = initvar
