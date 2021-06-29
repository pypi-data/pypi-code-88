from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Dict

from ctlml_commons.entity.state import State


@dataclass
class StatusState:
    status: str
    order_status: State

    @classmethod
    def deserialize(cls, input_data: Dict[str, Any]) -> StatusState:
        data = deepcopy(input_data)

        data["order_status"] = State.to_enum(data["order_status"])

        return cls(**data)
