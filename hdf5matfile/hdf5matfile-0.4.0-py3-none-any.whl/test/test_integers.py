import numpy as np

from . import assert_array_equal, get_var_loader

load_var = get_var_loader('test_integers.mat')

neg_numbers = [[0, -1, -2, -3, -4, -5, -6, -7]]
pos_numbers = [[0, 1, 2, 3, 4, 5, 6, 7]]


def test_i8():
    i8 = load_var('i8')
    assert_array_equal(i8, np.array(neg_numbers, dtype='int8'))


def test_i16():
    i16 = load_var('i16')
    assert_array_equal(i16, np.array(neg_numbers, dtype='int16'))


def test_i32():
    i32 = load_var('i32')
    assert_array_equal(i32, np.array(neg_numbers, dtype='int32'))


def test_i64():
    i64 = load_var('i64')
    assert_array_equal(i64, np.array(neg_numbers, dtype='int64'))


def test_u8():
    u8 = load_var('u8')
    assert_array_equal(u8, np.array(pos_numbers, dtype='uint8'))


def test_u16():
    u16 = load_var('u16')
    assert_array_equal(u16, np.array(pos_numbers, dtype='uint16'))


def test_u32():
    u32 = load_var('u32')
    assert_array_equal(u32, np.array(pos_numbers, dtype='uint32'))


def test_u64():
    u64 = load_var('u64')
    assert_array_equal(u64, np.array(pos_numbers, dtype='uint64'))


def test_logical():
    b = load_var('b')
    assert_array_equal(b, np.array([[0, 1, 0, 0, 0, 1, 1]], dtype='bool8'))
