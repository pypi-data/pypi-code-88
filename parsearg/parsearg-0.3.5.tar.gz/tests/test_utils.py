import pytest
from parsearg.utils import (
    is_list_of,
    underline,
)

def test_is_list_of():
    assert is_list_of([ 'A', 'B', 'C' ], str)
    assert is_list_of([ (None, []) ], tuple)
    assert is_list_of([ [] ], list)

def test_underline():
    s = 'hello, world!'

    assert underline(s) == 'hello, world!:\n--------------'

