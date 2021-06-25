import unittest
import numpy as np
import datetime as dt

from Alexandria.constructs import type_safety
from Alexandria.constructs import array
from Alexandria.constructs import datetime
from Alexandria.constructs import list
from Alexandria.constructs import string


x = np.array([1, 2, 5, 7])
y = np.array([[1, 2], [2, 3], [3, 3]])


class TypeSafetyTests(unittest.TestCase):

    def test_ensure_ndarray(self):
        assert isinstance(type_safety.ensure_ndarray([1, 2, 3]), np.ndarray)


class ArrayTests(unittest.TestCase):

    def test_nearest_entry(self):
        assert array.find_nearest_entry(x, 4)[0] == 2

    def test_span(self):
        assert array.span(x) == 7-1

    def test_internal_array_shape(self):
        assert np.all(array.internal_array_shape(x) == np.ones(x.shape))
        assert np.all(array.internal_array_shape(y) == 2*np.ones(len(y)))

    def test_dx_v(self):
        assert array.dx_v(x)[0] == 1
        assert array.dx_v(x)[-1] == 2

    def test_pretty(self):
        print(array.pretty_array(x))

    def test_list_to_ndarrays(self):
        z = [1, 2, 3, 4]
        zz = array.lists_to_ndarrays(z)
        assert type(zz) == np.ndarray
        assert type(zz[0]) == np.ndarray


class DatetimeTests(unittest.TestCase):

    def test_str_dt(self):
        print(datetime.string_to_datetime(["1999-02-3"]))

    def test_dt_str(self):
        print(datetime.datetime_to_string([dt.datetime(1999, 2, 3)], fmt="%m-%d-%Y"))

    def test_dt_n(self):
        d = datetime.datetime_to_days([dt.datetime(1999, 2, 3), dt.datetime(1999, 2, 4)])
        assert d[1] - d[0] == 1


class ListTests(unittest.TestCase):

    def test_chain_words(self):
        assert list.chain_words(["a", "b"], sep="-") == "a-b"


class StringTests(unittest.TestCase):

    def test_find_bt_q(self):
        assert string.find_between_quotations('A wild "q"') == "q"
        assert string.find_between_quotations("A wilder 'q'", q="'") == "q"

