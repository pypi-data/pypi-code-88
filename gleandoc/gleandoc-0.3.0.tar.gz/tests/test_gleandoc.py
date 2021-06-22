#!/usr/bin/env python

"""Tests for `gleandoc` package."""


import unittest
import os
import re
import subprocess
import sys

import gleandoc

sample_init_py = '''"""
657dafc3af
"""

__author__ = """Some Author"""
__email__ = 'author@example.com'
__version__ = '1.2.3'
'''


class TestGleandoc(unittest.TestCase):
    """Tests for `gleandoc` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        try:
            os.mkdir('astparse')
            open('astparse/__init__.py', 'w').write(sample_init_py)
            os.sync()
        except Exception as e:
            print(f"exception details: {e}")

    def tearDown(self):
        """Tear down test fixtures, if any."""
        try:
            os.unlink('test.rst')
        except Exception as e:
            print(f"exception details: {e}")
        try:
            os.unlink('astparse/__init__.py')
            os.rmdir('astparse')
        except Exception as e:
            print(f"exception details: {e}")

    def test_docstring_stdlib_module(self):
        """Test extracting docstring from standard library module"""
        docstring = gleandoc.docstring('re')
        line = docstring.splitlines()[0]
        assert line == 'Support for regular expressions (RE).'

    def test_ast_parse(self):
        """Test interpolating the docstring into readme at command line"""
        toxenv = os.environ['TOX_ENV_NAME']
        program = f"{os.getcwd()}/.tox/{toxenv}/bin/gleandoc"
        output = subprocess.check_output(
            [sys.executable, program, 'astparse'],
            text=True,
        )
        assert bool(re.search(r'657dafc3af', output, re.MULTILINE))

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
