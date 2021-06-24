import re

from constants import *

__all__ = ["apply_regexp", "maximum",
           "minimum", "letters", "digits",
           "uppercase", "lowercase", "symbols",
           "spaces", "not_common"]


def _process(password: str, positive: bool, regexp: str, min_: int = 0,
             max_: int = 0) -> bool:
    if min_ and max_:
        return bool(min_ <= len(re.findall(regexp, password)) <= max_) == bool(
            positive)
    elif min_:
        return bool(len(re.findall(regexp, password)) >= min_) == bool(
            positive)
    elif max_:
        return bool(len(re.findall(regexp, password)) <= max_) == bool(
            positive)
    else:
        return bool(re.search(regexp, password)) == bool(positive)


def apply_regexp(password: str, positive: bool, symbol: str) -> bool:
    return _process(password, positive, re.compile(symbol))


def minimum(password: str, positive: bool, length: int) -> bool:
    return len(password) >= length


def maximum(password: str, positive: bool, length: int) -> bool:
    return len(password) <= length


def letters(password: str, positive: bool, min_: int = 0,
            max_: int = 0) -> bool:
    if not max_: max_: int = len(password)
    return _process(password, positive, regex['letters'], min_=min_, max_=max_)


def digits(password: str, positive: bool, min_: int = 0,
           max_: int = 0) -> bool:
    if not max_: max_: int = len(password)
    return _process(password, positive, regex['digits'], min_=min_, max_=max_)


def symbols(password: str, positive: bool, min_: int = 0,
            max_: int = 0) -> bool:
    if not max_: max_: int = len(password)
    return _process(password, positive, regex['symbols'], min_=min_, max_=max_)


def spaces(password: str, positive: bool, min_: int = 0,
           max_: int = 0) -> bool:
    if not max_: max_: int = len(password)
    return _process(password, positive, regex['spaces'], min_=min_, max_=max_)


def uppercase(password: str, positive: bool) -> bool:
    return (password != password.lower()) == positive


def lowercase(password: str, positive: bool) -> bool:
    return (password != password.upper()) == positive


def not_common(password: str, positive: bool) -> bool:
    return password not in most_used_password
