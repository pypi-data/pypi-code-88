"""Presto SQL utilities."""
from typing import List


def date_parse(formats: List[str], /, column: str = "{col}") -> str:
    """Return the coalesced date_parse usage string to parse a column using the given formats.

    Example:
    -------
        date_parse(['%m/%d/%Y %r', '%Y-%m-%d %H:%i:%s', '%Y-%m-%d %H:%i:%s.%f']) ->
            "coalesce(try(date_parse({col}, '%m/%d/%Y %r')), try(date_parse({col}, '%Y-%m-%d %H:%i:%s')), date_parse({col}, '%Y-%m-%d %H:%i:%s.%f'))"

    """
    assert formats

    def _parse(fmt: str, /) -> str:
        return f"date_parse({column}, '{fmt}')"

    if len(formats) == 1:
        return _parse(formats[0])

    return "coalesce(" + ", ".join(f"try({_parse(f)})" for f in formats[:-1]) + ", " + _parse(formats[-1]) + ")"
