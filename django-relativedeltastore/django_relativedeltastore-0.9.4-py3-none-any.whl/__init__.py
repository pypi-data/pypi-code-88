import re
from typing import Optional, Tuple, Union

from dateutil.relativedelta import relativedelta


RELATIVE_UNITS = ('years', 'months', 'weeks', 'days', 'hours', 'minutes', 'seconds', 'microseconds')
ABSOLUTE_UNITS = ('year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond')
SUPPORTED_UNITS = ABSOLUTE_UNITS + RELATIVE_UNITS

UNIT_PATTERN = re.compile(r'(?P<value>[+\-]?\d+)\s*(?P<unit>{units})\b'.format(units='|'.join(SUPPORTED_UNITS)))


def relativedelta_has_value_for(obj: relativedelta, attr: str) -> bool:
    value = getattr(obj, attr)
    if attr == 'weeks':  # calculated property
        return False
    if attr in RELATIVE_UNITS:
        return value != 0
    return value is not None


def extract_relativedelta_args(obj: relativedelta) -> dict:
    return dict((
        (unit, getattr(obj, unit)) for unit in SUPPORTED_UNITS if relativedelta_has_value_for(obj, unit)
    ))


# custom string (de-)serializer

def format_value(value, unit):
    format_str = '{value}{unit}' if unit in ABSOLUTE_UNITS else '{value:+d}{unit}'
    return format_str.format(value=value, unit=unit)


def create_relativedelta_string(value: Union[relativedelta, dict]) -> str:
    if isinstance(value, relativedelta):
        value = extract_relativedelta_args(value)
    sorted_units = sorted(value.keys(), key=lambda x: SUPPORTED_UNITS.index(x))
    return ' '.join([format_value(value=value[key], unit=key) for key in sorted_units])


def parse_relativedelta_string(value: str) -> Tuple[Optional[dict], Optional[str]]:
    remainder = value.strip()
    relativedelta_kwargs = dict()

    while True:
        match = UNIT_PATTERN.match(remainder)
        if not match:
            return None, remainder

        remainder = remainder[match.end('unit'):].strip()  # remove current match & strip whitespace
        relativedelta_kwargs[match.group('unit')] = int(match.group('value'))

        if not remainder:
            break

    return relativedelta_kwargs, remainder
