import os
import random
import string


def chunks(lst, size):
    """Yield successive sized chunks from lst."""
    for i in range(0, len(lst), size):
        yield lst[i : i + size]


# old: get_swagger_spec_path
def swagger_spec_path() -> str:
    """returns the path to the current esi swagger spec file"""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "swagger.json")


def random_string(char_count: int) -> str:
    """returns a random string of given length"""
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(char_count)
    )


class AttrDict(dict):
    """Enhanced dict that allows property access to its keys.

    Example:

    .. code-block:: python

        >> my_dict = AttrDict({"color": "red", "size": "medium"})
        >> my_dict["color"]
        "red"
        >> my_dict.color
        "red"

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self


def humanize_number(value, magnitude: str = None, precision: int = 1) -> str:
    """Return the value in humanized format, e.g. `1234` becomes `1.2k`

    Args:
    - magnitude: fix the magnitude to format the number, e.g. `"b"`
    - precision: number of digits to round for
    """
    value = float(value)
    power_map = {"t": 12, "b": 9, "m": 6, "k": 3, "": 0}
    if magnitude not in power_map:
        if value >= 10 ** 12:
            magnitude = "t"
        elif value >= 10 ** 9:
            magnitude = "b"
        elif value >= 10 ** 6:
            magnitude = "m"
        elif value >= 10 ** 3:
            magnitude = "k"
        else:
            magnitude = ""
    return f"{value / 10 ** power_map[magnitude]:,.{precision}f}{magnitude}"
