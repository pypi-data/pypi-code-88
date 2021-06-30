from typing import Any, Tuple
from collections import defaultdict
from datetime import datetime


# seasons=months mapping
seasons = [3, 3, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3]


def _prep_default(value: str) -> Tuple[bool, Any]:
    return True, value


def _prep_organic(value: str) -> Tuple[bool, Any]:
    if type(value) != bool:
        return False, value

    value = 'organic' if value else 'conventional'
    return True, value


def _prep_date(value: str) -> Tuple[bool, Any]:
    try:
        month = datetime.strptime(value, '%Y-%m-%d').month
    except ValueError as e:
        return False, value

    value = seasons[month - 1]
    return True, value


preprocess_function = defaultdict(lambda: _prep_default)
preprocess_function['organic'] = _prep_organic
preprocess_function['date'] = _prep_date
