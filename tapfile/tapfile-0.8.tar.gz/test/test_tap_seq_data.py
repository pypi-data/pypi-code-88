import unittest
from unittest.mock import patch

from tap_file.tap_seq_data import TapSeqData


class MockStream:
    def __init__(self):
        self.data = None
        self.errors = set()

    def payload(self):
        return self.data, self.errors


class TestTapSeqData(unittest.TestCase):

    def test_data(self):
        def dummy_grade(s1, s2, _):
            return s1, s2

        stream = MockStream()
        stream.data = b'\x02The quick brown fox jumps over the lazy dog\x00'
        with patch('tap_file.tap_seq_data.DataStream') as mock_data_stream:
            mock_data_stream.grade_streams = dummy_grade
            self.seq = TapSeqData.create_from_streams(stream, stream)
        self.assertEqual(self.seq.data, b'The quick brown fox jumps over the lazy dog')


class TestTapProgram2(unittest.TestCase):

    def test_data(self):
        data = TapSeqData(b'12345')
        self.assertFalse(data.uncorrected_errors)
        self.assertEqual(data._data, b'\x0212345' + b'\x00' * 186)
