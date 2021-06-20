import unittest

from tap_file.data_stream import DataStream


class TestDataStream(unittest.TestCase):

    def setUp(self):
        self.stream = DataStream()

    def test_add_bad_byte(self):
        self.stream.data = bytearray(6)
        self.stream.add_byte(None)
        self.assertEqual(self.stream.data, b'\x00\x00\x00\x00\x00\x00#')
        self.assertEqual(self.stream.byte_errors, {6})

    def test_add_byte(self):
        self.stream.add_byte([1, 0, 0, 1, 0, 1, 1, 1, 0])
        self.assertEqual(self.stream.data, b'.')
        self.assertNotIn(0, self.stream.byte_errors)
        self.stream.add_byte([0, 0, 0, 1, 0, 1, 1, 1, 0])
        self.assertEqual(self.stream.data, b'..')
        self.assertIn(1, self.stream.byte_errors)
        self.assertEqual(len(self.stream), 2)

    def test_sync(self):
        self.stream.data = b'\x09\x08\x07\x06\x05\x04\x03\x02\x01ABC\xCA'
        self.assertTrue(self.stream.valid_sync)
        self.stream.data = b'\x09\x08\x07\x06\x50\x04\x03\x02\x01ABC\xCA'
        self.assertFalse(self.stream.valid_sync())
        self.stream.byte_errors = {4}
        self.assertTrue(self.stream.valid_sync())

    def test_checksum(self):
        self.stream.data = b'\x11'
        self.assertFalse(self.stream.valid_checksum())
        self.stream.data = b'\x09\x08\x07\x06\x05\x04\x03\x02\x01ABC\x40'
        self.assertTrue(self.stream.valid_checksum())

    def payload(self):
        self.stream.data = b'\x09\x08\x07\x06\x05\x04\x03\x02\x01ABC\x40'
        data, _ = self.stream.payload()
        self.assertEqual(data, b'ABC')
        self.stream.data = b'\x09\x08\x07\x06\x50\x04\x03\x02\x01ABC\xCA'
        self.stream.byte_errors = {4, 10}
        _, errors = self.stream.payload()
        self.assertIn(errors, 4)


class TestGradeStreams(unittest.TestCase):

    def setUp(self):
        self.stream1 = DataStream()
        self.stream2 = DataStream()

    def test_same_length(self):
        self.stream1.data = b'\x09\x08\x07\x06\x50\x04\x03\x02\x01ABC\x40'
        self.stream2.data = b'\x09\x08\x07\x06\x50\x04\x03\x02\x01ABC\x40'
        s1, s2 = DataStream.grade_streams(self.stream1, self.stream2, len(self.stream1.data))
        self.assertIs(s1, self.stream1)
        self.stream1.byte_errors = {6}
        s1, s2 = DataStream.grade_streams(self.stream1, self.stream2, len(self.stream1.data))
        self.assertIs(s1, self.stream2)

    def test_same_length_bad_crc(self):
        self.stream1.data = b'ABCDEF'
        self.stream2.data = b'ABCDEF'
        self.stream2.byte_errors = {3}
        s1, s2 = DataStream.grade_streams(self.stream1, self.stream2, 6)
        self.assertIs(s1, self.stream1)
        self.stream1.byte_errors = {2, 3}
        s1, s2 = DataStream.grade_streams(self.stream1, self.stream2, 6)
        self.assertIs(s1, self.stream2)

    def test_diff_length(self):
        self.stream1.data = b'\x09\x08\x07\x06\x50\x04\x03\x02\x01ABC\x40'
        self.stream2.data = b'\x09\x08\x07\x06\x50\x04\x03\x02\x01ABCDE\x40'
        s1, s2 = DataStream.grade_streams(self.stream1, self.stream2, len(self.stream1.data))
        self.assertIs(s1, self.stream1)
        self.stream1.data = b'\x09\x08\x07\x06\x50\x04\x03\x02\x01ABCDE\x40'
        self.stream2.data = b'\x09\x08\x07\x06\x50\x04\x03\x02\x01ABC\x40'
        s1, s2 = DataStream.grade_streams(self.stream1, self.stream2, len(self.stream2.data))
        self.assertIs(s1, self.stream2)

    def test_invalid_length(self):
        self.stream1.data = b'\x09\x08\x07\x06\x50\x04\x03\x02\x01ABC\x40'
        self.stream2.data = b'\x09\x08\x07\x06\x50\x04\x03\x02\x01ABC\x40'
        with self.assertRaises(ValueError):
            _, __ = DataStream.grade_streams(self.stream1, self.stream2, 4)
        self.stream2.data = b'\x09\x08\x07\x06\x50\x04\x03\x02\x01ABCDE\x40'
        with self.assertRaises(ValueError):
            _, __ = DataStream.grade_streams(self.stream1, self.stream2, 4)
