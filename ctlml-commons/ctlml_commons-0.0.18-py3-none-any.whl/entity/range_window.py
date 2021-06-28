from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass(frozen=True)
class RangeWindow:
    floor: float
    ceiling: float

    def serialize(self) -> Dict[str, Any]:
        return self.__dict__

    @classmethod
    def deserialize(cls, input_data: Dict[str, Any]) -> RangeWindow:
        return RangeWindow(**input_data)
