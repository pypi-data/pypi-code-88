"""This module contains colour related utility functions."""
from typing import Any, Dict, Union

from misty2py.utils.utils import query_dict_with_fallback


def parse_rgb_value(value: Union[int, str, None]) -> int:
    """Parses and validates an RGB value.

    Args:
        value (Union[int, str, None]): an RGB value.

    Raises:
        TypeError: If the value is not int or str parseable to int.
        ValueError: If the value is int or a str parseable to int but is not a valid RGB value.

    Returns:
        int: the RGB value as an int if parseable and valid.
    """
    try:
        value = int(value)
    except Exception:
        raise TypeError("An rgb value must be int or string parseable to int.")

    if not (value >= 0 and value <= 255):
        raise ValueError("An rgb value must be \
            between 0 and 255 (bounds including)")

    return value


def rgb_values_to_dict(
    red: Union[int, str], green: Union[int, str], blue: Union[int, str]
) -> Dict:
    """Returns RGB dictionary in the form required by Misty's REST API from RGB values supplied as str or int."""
    return {
        "red": parse_rgb_value(red),
        "green": parse_rgb_value(green),
        "blue": parse_rgb_value(blue),
    }


def validate_rgb_dict(potential_rgb: Dict) -> Dict:
    """Validates a potentially RGB dictionary. Returns the RGB dictionary if successful."""
    return {
        "red": parse_rgb_value(potential_rgb.get("red")),
        "green": parse_rgb_value(potential_rgb.get("green")),
        "blue": parse_rgb_value(potential_rgb.get("blue")),
    }


def get_rgb_from_unknown(potential_rgb: Any, allowed_data: Dict = {}) -> Dict:
    """Attempts to parse an RGB dictionary as required by Misty's REST API from potential_rgb.

    Args:
        potential_rgb (Any): any data that might be an rgb dict.
        allowed_data (Dict, optional): the dictionary of allowed data shortcuts (string keys, dict values). Defaults to `{}`.

    Raises:
        TypeError: If the type of potential_rgb is not dict or parseable to dict.

    Returns:
        Dict: RGB dictionary as required by Misty's REST API.
    """
    if isinstance(potential_rgb, str):
        potential_rgb = allowed_data.get(potential_rgb)

    if isinstance(potential_rgb, Dict):
        return validate_rgb_dict(potential_rgb)

    else:
        raise TypeError(
            "Incorrect type: `%s`, expecting Dict." % type(potential_rgb))


def construct_transition_dict(
    data: Dict,
    allowed_data: Dict,
    fallback_time: int = 500,
    fallback_trans: str = "Breathe",
) -> Dict:
    """Constructs a transition dictionary in the form required by Misty's REST API.

    Args:
        data (Dict): The dictionary to transform, must have keys `"col1"` and `"col2"` that contain a string (a data shortcut for a colour) or a dict (an rgb dictionary) and should have thr keys `"transition"` and `"time"`.
        allowed_data (Dict): The dictionary of allowed data shortcuts (string keys, dict values).
        fallback_time (int, optional): The time between colours switching in ms. Defaults to `500`.
        fallback_trans (str, optional): The default transition type, can be one of `"Blink"`, `"Breathe"` or `"TransitOnce"`. Defaults to `"Breathe"`.

    Returns:
        Dict: The input dictionary in the form required by Misty API's endpoint `/api/led/transition`.
    """
    col1 = get_rgb_from_unknown(data.get("col1"), allowed_data=allowed_data)
    col2 = get_rgb_from_unknown(data.get("col2"), allowed_data=allowed_data)

    return {
        "Red": col1.get("red"),
        "Green": col1.get("green"),
        "Blue": col1.get("blue"),
        "Red2": col2.get("red"),
        "Green2": col2.get("green"),
        "Blue2": col2.get("blue"),
        "TransitionType": query_dict_with_fallback(
            data, "transition", fallback_trans, required_type=str
        ),
        "TimeMS": query_dict_with_fallback(
            data, "time", fallback_time, required_type=int
        ),
    }
