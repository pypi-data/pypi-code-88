import math
from copy import deepcopy
from typing import Any, Dict, List


def percentage_format_str() -> str:
    return "{0:.4f}%"


def float_to_percentage_str(value: float, percentage_format: str = percentage_format_str()) -> str:
    return percentage_format.format(value)


def convert_floats(input_data: Dict[str, Any], keys: List[str], default_value=None) -> Dict[str, Any]:
    if any(k in input_data for k in keys):
        data = deepcopy(input_data)

        for key in keys:
            if key in input_data:
                data[key] = float(data[key]) if data[key] is not None else default_value

        return data

    return input_data


def is_zero(an_input: float) -> bool:
    return math.isclose(an_input, 0.0)


def readable_float_to_str(an_input: float, decimal_points: int = 20) -> str:
    format_str: str = '{:.' + str(decimal_points) + "f}"
    return format_str.format(an_input)
