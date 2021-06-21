import numpy as np

from . import assert_array_equal, get_var_loader

load_var = get_var_loader('test_chars.mat')


def test_1d():
    ch1 = load_var('ch1')
    assert ch1 == 'hello world!'


def test_2d():
    ch2 = load_var('ch2')
    assert ch2 == 'helloworld'


def test_chars_in_cells():
    ch3 = load_var('ch3')
    assert_array_equal(ch3, np.array([['hello', 'world']], dtype=object))
