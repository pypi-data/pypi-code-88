#!/usr/bin/env python

"""Tests for `gleandoc` package."""


import unittest
import os
import re
import subprocess
import sys

import gleandoc


class TestGleandoc(unittest.TestCase):
    """Tests for `gleandoc` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""
        try:
            os.unlink('test.rst')
            print('tearDown: removed test.rst')
        except Exception:
            pass

    def test_docstring_stdlib_module(self):
        """Test extracting docstring from standard library module"""
        docstring = gleandoc.docstring('re')
        line = docstring.splitlines()[0]
        assert line == 'Support for regular expressions (RE).'

    def test_docstring_cwd_basename(self):
        """Test extracting docstring based on working directory name"""
        docstring = gleandoc.docstring()
        line = docstring.splitlines()[9]
        # this test will need to be updated if the docstring changes
        assert line == 'Print the first line of a docstring:'

    def test_generate_readme(self):
        """Test interpolating the docstring into readme at command line"""
        # figure out how to test as installed
        # determine tox env (this matches definitions in tox.ini, like 'py39')
        toxenv = os.environ['TOX_ENV_NAME']
        program = f"{os.getcwd()}/.tox/{toxenv}/bin/gleandoc"
        subprocess.Popen(
            [sys.executable, program, "README.rst.fstr", "test.rst"],
        ).wait(timeout=30)
        with open('test.rst') as f:
            readme = f.read()
            # look for a line that should be interpolated into the readme
            assert bool(re.search(r'No dependencies', readme, re.MULTILINE))
