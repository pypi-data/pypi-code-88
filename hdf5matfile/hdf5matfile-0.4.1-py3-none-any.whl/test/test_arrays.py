import numpy as np

from . import assert_array_equal, get_matfile

matfile = get_matfile('test_arrays.mat')


def test_scalar():
    a0 = matfile.load_variable('a0')
    assert_array_equal(a0, np.array([[1.]]))


def test_1d():
    a1 = matfile.load_variable('a1')
    assert_array_equal(a1, np.array([[1., 2., 3.]]))


def test_2d():
    a2 = matfile.load_variable('a2')
    assert_array_equal(a2, np.array([[1., 2., 3.], [4., 5., 6.]]))


def test_3d():
    a3 = matfile.load_variable('a3')
    assert_array_equal(a3, np.arange(1., 24 + 1).reshape(2, 3, 4, order='F'))


def test_index_scalar():
    a0 = matfile['a0']
    value = a0[0, 0]
    assert value == 1.


def test_index_column():
    a2 = matfile['a2']
    assert_array_equal(a2[:, 0], np.array([1., 4.]))


def test_index_3d():
    a3 = matfile['a3']
    assert_array_equal(
        a3[:, :, 0],
        np.array([
            [1., 3., 5.],
            [2., 4., 6.],
        ]),
    )
    assert_array_equal(
        a3[:, :, 1],
        np.array([
            [7., 9., 11.],
            [8., 10., 12.],
        ]),
    )
    assert_array_equal(
        a3[:, :, 2],
        np.array([
            [13., 15., 17.],
            [14., 16., 18.],
        ]),
    )
    assert_array_equal(
        a3[:, :, 3],
        np.array([
            [19., 21., 23.],
            [20., 22., 24.],
        ]),
    )
