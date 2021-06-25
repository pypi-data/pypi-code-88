from __future__ import annotations

from typing import Dict, Optional, Tuple, Type, TypeVar

KT = TypeVar('KT')
VT = TypeVar('VT')


def value_type(dic: Dict[KT, VT], key: KT)\
        -> Tuple[Optional[VT], Type[VT] | Type[None]]:
    return ((val := dic[key]), type(val)) if key in dic else (None, type(None))
