#!/usr/bin/env python

"""Tests for `disambigufile` package."""

# assumes make test in the root package source directory

import os
import unittest

from disambigufile import DisFile
import disambigufile


class TestDisambigufile(unittest.TestCase):
    """Tests for `disambigufile` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        os.mkdir('sandbox')
        os.mkdir('sandbox/dir1')
        os.mkdir('sandbox/dir2')
        os.mkdir('sandbox/dir2/dir3')
        with open('sandbox/dir1/findme', 'w') as f:
            f.write("token\n")
        with open('sandbox/dir2/findother', 'w') as f:
            f.write("token\n")
        with open('sandbox/dir2/dir3/data', 'w') as f:
            f.write("token\n")

    def tearDown(self):
        """Tear down test fixtures, if any."""
        os.unlink('sandbox/dir2/dir3/data')
        os.unlink('sandbox/dir2/findother')
        os.unlink('sandbox/dir1/findme')
        os.rmdir('sandbox/dir2/dir3')
        os.rmdir('sandbox/dir2')
        os.rmdir('sandbox/dir1')
        os.rmdir('sandbox')

    def test_hit(self):
        """Test hit"""
        path = 'sandbox/dir1:sandbox/dir2'
        try:
            assert str(DisFile('me', path=path)) == 'sandbox/dir1/findme'
        except Exception as e:
            print(f"exception: {e}")
            assert False

    def test_miss_ambiguous(self):
        """Test miss (ambiguous)"""
        path = 'sandbox/dir1:sandbox/dir2'
        try:
            DisFile('find', path=path).hit()
            assert False
        except disambigufile.AmbiguousMatchError:
            assert True

    def test_miss_no_match(self):
        """Test miss (no match)"""
        path = 'sandbox/dir1:sandbox/dir2'
        try:
            DisFile('46a52c91eec8b604', path=path).hit()
            assert False
        except disambigufile.NoMatchError:
            assert True

    def test_subpattern(self):
        """Test subpattern hit"""
        path = 'sandbox/dir1:sandbox/dir2'
        try:
            # pattern matches dir3 found in dir2
            # subpattern matches dir3/data
            found = DisFile('dir3', subpattern='data', path=path).hit()
            assert str(found) == 'sandbox/dir2/dir3/data'
        except Exception as e:
            print(f"exception: {e}")
            assert False
