#!/usr/bin/env python

"""Tests for `gleandoc` package."""


import unittest

import gleandoc


class TestGleandoc(unittest.TestCase):
    """Tests for `gleandoc` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_docstring_stdlib_module(self):
        """Test extracting docstring from standard library module"""
        docstring = gleandoc.docstring('re')
        first = docstring.splitlines()[0]
        assert first == 'Support for regular expressions (RE).'

    def test_docstring_cwd_basename(self):
        """Test extracting docstring based on working directory name"""
        docstring = gleandoc.docstring()
        second = docstring.splitlines()[1]
        assert second == 'Simple convenience function to extract docstring'
