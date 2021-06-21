import numpy as np

from . import assert_array_equal, get_var_loader

load_var = get_var_loader('test_structs.mat')


def test_simple():
    s1 = load_var('s1')
    assert s1.shape == (1, 1)

    d = s1[0, 0]
    assert_array_equal(d['a'], np.array([[3]], dtype='double'))
    assert d['b'] == 'foobar'


def test_non_scalar():
    s2 = load_var('s2')
    assert s2.shape == (1, 2)

    d1 = s2[0, 0]
    assert_array_equal(d1['a'], np.array([[1]], dtype='double'))
    assert d1['b'] == 'foo'

    d2 = s2[0, 1]
    assert_array_equal(d2['a'], np.array([[2]], dtype='double'))
    assert d2['b'] == 'bar'


def test_nested():
    s3 = load_var('s3')
    assert s3.shape == (1, 1)

    # s1
    s1 = s3[0, 0]['s1']
    assert s1.shape == (1, 1)

    d = s1[0, 0]
    assert_array_equal(d['a'], np.array([[3]], dtype='double'))
    assert d['b'] == 'foobar'

    # s2
    s2 = s3[0, 0]['s2']
    assert s2.shape == (1, 2)

    d1 = s2[0, 0]
    assert_array_equal(d1['a'], np.array([[1]], dtype='double'))
    assert d1['b'] == 'foo'

    d2 = s2[0, 1]
    assert_array_equal(d2['a'], np.array([[2]], dtype='double'))
    assert d2['b'] == 'bar'
