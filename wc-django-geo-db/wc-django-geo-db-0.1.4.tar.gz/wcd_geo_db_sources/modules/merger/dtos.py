
from typing import Any, List, Optional, Tuple, TypeVar, TypedDict

from wcd_geo_db.const import DivisionLevel, DivisionType


__all__ = 'DivisionItem', 'DivisionTranslationItem',


class DivisionItem(TypedDict):
    code: Tuple[str, Any]
    codes: List[Tuple[str, Any]]
    path: List[Tuple[str, Any]]
    name: Optional[str]
    types: List[DivisionType]
    level: DivisionLevel


class DivisionTranslationItem(TypedDict):
    code: Tuple[str, Any]
    name: Optional[str]
    synonyms: Optional[str]
