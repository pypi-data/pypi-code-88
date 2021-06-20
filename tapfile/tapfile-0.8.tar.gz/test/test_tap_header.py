import unittest
from unittest.mock import patch

from tap_file.header_type import HeaderType
from tap_file.tap_header import TapHeader


class MockStream:
    def __init__(self):
        self.data = None
        self.errors = set()

    def payload(self):
        return self.data, self.errors


class TestTapHeader(unittest.TestCase):

    def setUp(self):
        def dummy_grade(s1, s2, _):
            return s1, s2

        stream = MockStream()
        stream.data = b'\x03\x01\x10\x47\x32TEST            321'
        with patch('tap_file.tap_header.DataStream') as mock_data_stream:
            mock_data_stream.grade_streams = dummy_grade
            self.header = TapHeader.create_from_streams(stream, stream)

    def test_htype(self):
        self.assertEqual(self.header.htype, HeaderType(3))

    def test_start(self):
        self.assertEqual(self.header.start, 0x1001)

    def test_end(self):
        self.assertEqual(self.header.end, 0x3247)

    def test_name(self):
        self.assertEqual(self.header.name, b'TEST')

    def test_data(self):
        self.assertEqual(self.header.data, b'321')


class TestTapHeader2(unittest.TestCase):

    def test_base(self):
        header = TapHeader(HeaderType.SEQ, b'TEST')
        self.assertFalse(header.uncorrected_errors)
        self.assertEqual(header._data[0], 4)
        self.assertEqual(header._data[5:], b'TEST'+b' '*183)

    def test_prg(self):
        header = TapHeader(HeaderType.PRG, b'TEST', start=111, end=222)
        self.assertEqual(header._data[0], 3)
        self.assertEqual(header._data[1:3], b'\x6f\x00')
        self.assertEqual(header._data[3:5], b'\xde\x00')

    def test_prg_missing_start(self):
        with self.assertRaises(ValueError):
            _ = TapHeader(HeaderType.PRG, b'TEST', end=222)

    def test_prg_missing_end(self):
        with self.assertRaises(ValueError):
            _ = TapHeader(HeaderType.PRG, b'TEST', start=111)


class TestTapSeq(unittest.TestCase):

    def setUp(self):
        def dummy_grade(s1, s2, _):
            return s1, s2

        stream = MockStream()
        stream.data = b'\x02The quick brown fox jumps over the lazy dog\x00'
        with patch('tap_file.tap_header.DataStream') as mock_data_stream:
            mock_data_stream.grade_streams = dummy_grade
            self.header = TapHeader.create_from_streams(stream, stream)

    def test_data(self):
        self.assertTrue(self.header.seq_eof)
        self.assertEqual(self.header.data, b'The quick brown fox jumps over the lazy dog')
