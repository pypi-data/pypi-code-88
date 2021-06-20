import unittest
from unittest.mock import Mock

from tap_file.tap_file_writer import TapFileWriter

import io


class TestTapFile(unittest.TestCase):

    def setUp(self):
        self.fileh = io.BytesIO(b'C64-TAPE-RAW\x01\x00\x00\x00\x00\x00\x00\x00')
        self.path = Mock()
        self.path.open.return_value = self.fileh
        self.path.exists.return_value = True
        self.tf = TapFileWriter(self.path)

    def test_new_file(self):
        self.path.exists.return_value = False
        fileh = io.BytesIO()
        self.path.open.return_value = fileh
        self.tf.__enter__()
        self.assertEqual(fileh.tell(), 0)

    def test_existing_v0(self):
        fileh = io.BytesIO(b'C64-TAPE-RAW\x00\x00\x00\x00\x00\x00\x00\x00')
        self.path.open.return_value = fileh
        self.tf.__enter__()
        self.assertEqual(self.tf.version, 0)
        self.assertEqual(self.tf.platform, 0)
        self.assertEqual(self.tf.video, 0)
        self.assertEqual(fileh.tell(), 20)

    def test_existing_v1(self):
        self.tf.__enter__()
        self.assertEqual(self.tf.version, 1)
        self.assertEqual(self.tf.platform, 0)
        self.assertEqual(self.tf.video, 0)
        self.assertEqual(self.fileh.tell(), 20)

    def test_existing_content(self):
        self.fileh.seek(0, 2)
        self.fileh.write(b'\x11\x22\x33\x44')
        self.fileh.seek(0)
        self.tf.__enter__()
        self.assertEqual(self.fileh.tell(), 24)

    def test_update_len(self):
        self.fileh.seek(0, 2)
        self.fileh.write(b'\x11\x22\x33\x44\x55\x66')
        self.fileh.seek(0)
        self.tf.__enter__()
        self.fileh.close = lambda: None
        self.tf.__exit__(None, None, None)
        length = self.fileh.getvalue()[16:20]
        self.assertEqual(length, b'\x06\x00\x00\x00')

    def test_short_cycles(self):
        self.tf.__enter__()
        self.tf.add_cycles([8, 81, 159])
        data = self.fileh.getvalue()[20:]
        self.assertEqual(data, b'\x01\x0a\x14')

    def test_long_cycles(self):
        self.tf.__enter__()
        self.tf.add_cycles([0x654321])
        self.tf.version = 0
        self.tf.add_cycles([0x654321])
        data = self.fileh.getvalue()[20:]
        self.assertEqual(data, b'\x00\x21\x43\x65\x00')

    def test_leader(self):
        self.tf.__enter__()
        self.tf.add_leader(6)
        data = self.fileh.getvalue()[20:]
        self.assertEqual(data, b'\x2e'*6)

    def test_append(self):
        obj = Mock()
        obj._data = b'\xff'
        self.tf.__enter__()
        self.tf.append(obj)
        data = self.fileh.getvalue()[0x1a14:]
        # start of data stream
        self.assertEqual(data[2:6], b'\x2e\x2e\x56\x42')
        # data byte
        self.assertEqual(data[0xba:0xca], b'\x42\x2e'*8)
        # check bit
        self.assertEqual(data[0xca:0xcc], b'\x42\x2e')
        # end of data stream
        self.assertEqual(data[0xe0:0xe2], b'\x56\x2e')

    def test_bad_magic(self):
        fileh = io.BytesIO(b'x.junk.junk.\x00\x00\x00\x00\x00\x00\x00\x00')
        self.path.open.return_value = fileh
        with self.assertRaises(ValueError):
            self.tf.__enter__()

    def test_bad_version(self):
        fileh = io.BytesIO(b'C64-TAPE-RAW\x88\x00\x00\x00\x00\x00\x00\x00')
        self.path.open.return_value = fileh
        with self.assertRaises(NotImplementedError):
            self.tf.__enter__()
