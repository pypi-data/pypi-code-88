# encoding: utf-8

'''dr.who — package tests'''

import unittest


def test_suite():
    return unittest.TestSuite()


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
