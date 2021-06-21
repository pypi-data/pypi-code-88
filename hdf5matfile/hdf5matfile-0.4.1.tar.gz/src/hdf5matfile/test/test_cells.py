import numpy as np
from . import assert_array_equal, get_var_loader

load_var = get_var_loader('test_cells.mat')


def test_1d():
    c1 = load_var('c1')
    assert c1.dtype == np.dtype('O')
    assert c1.shape == (1, 3)
    a1, a2, a3 = c1.flat
    assert_array_equal(a1, np.array([[1.0]], dtype='double'))
    assert_array_equal(a2, np.array([[2.0]], dtype='double'))
    assert_array_equal(a3, np.array([[3.0]], dtype='double'))


def test_1d_arrays():
    c2 = load_var('c2')
    assert c2.dtype == np.dtype('O')
    assert c2.shape == (1, 2)
    a1 = c2.flat[0]
    a2 = c2.flat[1]
    assert_array_equal(a1, np.array([[1., 2., 3., 4.]]))
    assert_array_equal(a2, np.array([[5., 6., 7., 8.]]))


def test_2d():
    c3 = load_var('c3')
    assert c3.dtype == np.dtype('O')
    assert c3.shape == (2, 2)
    a11 = c3[0, 0]
    a12 = c3[0, 1]
    a21 = c3[1, 0]
    a22 = c3[1, 1]
    assert_array_equal(a11, np.array([[1., 2., 3., 4.]]))
    assert_array_equal(a12, np.array([[5., 6., 7., 8.]]))
    assert_array_equal(a21, np.array([[4., 3., 2., 1.]]))
    assert_array_equal(a22, np.array([[8., 7., 6., 5.]]))
