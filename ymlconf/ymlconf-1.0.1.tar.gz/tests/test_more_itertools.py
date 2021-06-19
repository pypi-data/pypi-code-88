#!/usr/bin/env python3

import unittest

import more_itertools


class TestMoreItertools(unittest.TestCase):
    def test_flatten_2_nested(self):
        print(list(more_itertools.collapse([1, 2, 3, [4, 5, 6], [7]])))

    def test_flatten_3_nested(self):
        print(list(more_itertools.collapse([[[1], [2, 3]], [4, 5, 6], [7]])))
