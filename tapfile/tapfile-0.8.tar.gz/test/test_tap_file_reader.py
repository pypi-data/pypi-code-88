import unittest

from io import BytesIO
from pathlib import Path
from unittest.mock import patch, mock_open

from tap_file.data_stream import DataStream
from tap_file.tap_file_reader import TapFileReader


class TestTapFile(unittest.TestCase):

    def setUp(self):
        with patch.object(Path, 'open', mock_open(read_data=b'C64-TAPE-RAW\x00\x01\x02\x00\x12\x34\x56\x78')):
            self.tf = TapFileReader(Path())

    def test_header(self):
        self.assertEqual(self.tf.version, 0)
        self.assertEqual(self.tf.platform, 1)
        self.assertEqual(self.tf.video, 2)
        self.assertEqual(self.tf.length, 2018915346)

    def test_dipole(self):
        self.tf.fileh = BytesIO(b'\x42')
        self.assertEqual(self.tf.next_dipole(), 'M')
        self.tf.fileh = BytesIO(b'\x00\x11\x22\x33')
        self.assertEqual(self.tf.next_dipole(), 'X')

    def test_leader(self):
        self.tf.leader = 0
        self.tf.in_leader = True
        self.tf.consume_leader('S')
        self.tf.consume_leader('M')
        self.assertEqual(self.tf.leader, 0)
        self.assertTrue(self.tf.in_leader)
        self.tf.leader = 16
        self.tf.consume_leader('L')
        self.assertFalse(self.tf.in_leader)
        self.assertEqual(self.tf.queued, 'L')

    def test_byte_stream(self):
        self.tf.stream = DataStream()
        self.tf.queued = ''
        for d in 'LMSM':
            self.tf.consume_byte_stream(d)
        self.assertEqual(self.tf.queued, 'SM')
        for d in 'SMMSSMMSMSMSSMMSLM':
            self.tf.consume_byte_stream(d)
        self.assertEqual(self.tf.queued, '')
        self.assertEqual(len(self.tf.stream), 1)
        for d in 'SMSMMSSMMSMSMSSMMSLSSS':
            self.tf.consume_byte_stream(d)
        self.assertEqual(self.tf.queued, '')
        self.assertEqual(len(self.tf.stream), 2)
        self.assertTrue(self.tf.in_leader)

    def test_byte_stream_corrupt(self):
        self.tf.stream = DataStream()
        self.tf.queued = ''
        for d in 'SMSMMSSMMSMSMSMMMSLM':
            self.tf.consume_byte_stream(d)
        self.assertEqual(self.tf.queued, 'SMSMMSSMMSMSMSMMMSLM')
        self.assertEqual(len(self.tf.stream), 0)
        for d in 'SMSMMSSMMSMSMSSMMSLM':
            self.tf.consume_byte_stream(d)
        self.assertEqual(self.tf.queued, '')
        self.assertEqual(len(self.tf.stream), 2)


class TestTapFileInvalid(unittest.TestCase):

    def test_invalid_header(self):
        with self.assertRaises(ValueError):
            with patch.object(Path, 'open', mock_open(read_data=b'junk.junk.junk')):
                _ = TapFileReader(Path())

    def test_invalid_version(self):
        with self.assertRaises(NotImplementedError):
            with patch.object(Path, 'open', mock_open(read_data=b'C64-TAPE-RAW**')):
                _ = TapFileReader(Path())
