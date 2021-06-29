from enum import Enum
from typing import Dict, Optional

from pydantic import BaseModel


class FliptBasicUnit(BaseModel):
    ...


class Flag(FliptBasicUnit):
    key: str
    name: str
    description: Optional[str]
    enabled: bool


class Rule(FliptBasicUnit):
    flag_key: str
    segment_key: str
    rank: int
    id: Optional[str]


class MatchType(str, Enum):
    ALL = "ALL_MATCH_TYPE"
    ANY = "ANY_MATCH_TYPE"


class Segment(FliptBasicUnit):
    key: str
    name: str
    description: Optional[str]
    match_type: MatchType = MatchType.ALL.value


class ComparisonType(str, Enum):
    UNKNOWN = "UNKNOWN_COMPARISON_TYPE"
    STRING = "STRING_COMPARISON_TYPE"
    NUMBER = "NUMBER_COMPARISON_TYPE"
    BOOLEAN = "BOOLEAN_COMPARISON_TYPE"


class OperatorType(str, Enum):
    EQ = "=="
    NEQ = "!="
    IS_EMPTY = "IS EMPTY"
    IS_NOT_EMPTY = "IS NOT EMPTY"
    HAS_SUFFIX = "HAS SUFFIX"
    HAS_PREFIX = "HAS PREFIX"


class Constraint(FliptBasicUnit):
    segment_key: str
    type: ComparisonType = ComparisonType.UNKNOWN.value
    property: str
    operator: OperatorType
    value: Optional[str]


class EvaluateResponse(BaseModel):
    request_context: Dict[str, str]
    match: bool
    flag_key: str
    segment_key: str
    value: str
