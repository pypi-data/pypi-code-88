import unittest
from unittest.mock import patch

from tap_file.tap_program import TapProgram


class MockStream:
    def __init__(self):
        self.data = None
        self.errors = set()

    def payload(self):
        return self.data, self.errors


class TestTapProgram(unittest.TestCase):

    def setUp(self):
        def dummy_grade(s1, s2, _):
            return s1, s2

        stream = MockStream()
        stream.data = b'The quick brown fox jumps over the lazy dog\x00'
        with patch('tap_file.tap_program.DataStream') as mock_data_stream:
            mock_data_stream.grade_streams = dummy_grade
            self.header = TapProgram.create_from_streams(stream, stream, len(stream.data))

    def test_data(self):
        self.assertEqual(self.header.data, b'The quick brown fox jumps over the lazy dog\x00')


class TestTapProgram2(unittest.TestCase):

    def test_data(self):
        data = TapProgram(b'12345')
        self.assertFalse(data.uncorrected_errors)
        self.assertEqual(data._data, b'12345')
