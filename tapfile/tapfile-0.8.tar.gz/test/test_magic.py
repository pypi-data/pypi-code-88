import unittest

from pathlib import Path
from unittest.mock import patch, mock_open

from tap_file.magic import is_valid_image


class TestMagic(unittest.TestCase):

    def test_good_magic(self):
        with patch.object(Path, 'open', mock_open(read_data=b'C64-TAPE-RAW')):
            self.assertTrue(is_valid_image(Path()))

    def test_bad_magic(self):
        with patch.object(Path, 'open', mock_open(read_data=b'INVALID')):
            self.assertFalse(is_valid_image(Path()))
