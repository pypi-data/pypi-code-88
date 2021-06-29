""" Module containing a generic input stream
"""

from typing import Union, TextIO
import sys
from pathlib import Path

import serial

__author__ = "Brendan Kristiansen"
__copyright__ = "Copyright 2021, Brendan Kristiansen"
__credits__ = ["Brendan Kristiansen"]
__license__ = "MPL 2.0"
__maintainer__ = "Brendan Kristiansen"
__email__ = "b@bek.sh"


class SerialParity:
    """ Contains constants to specify serial parity bit
    """

    parity_none = serial.PARITY_NONE
    parity_even = serial.PARITY_EVEN
    parity_odd = serial.PARITY_ODD


class SerialDataBits:
    """ Contains constants to specify number of data bits
    """

    bits_five = serial.FIVEBITS
    bits_six = serial.SIXBITS
    bits_seven = serial.SEVENBITS
    bits_eight = serial.EIGHTBITS


class SerialStopBits:
    """ Contains constants to specify serial stop bits
    """

    stopbits_one = serial.STOPBITS_ONE
    stopbits_two = serial.STOPBITS_TWO


class SerialFlowControl:
    """ Contains constants to set up serial flow control
    """

    off = serial.XOFF
    on = serial.XON


class GenericInputStream:
    """ Generic input stream
    """

    _raw_log_path: Union[Path, None]

    def __init__(self):
        """ Constructor
        """

        self._raw_log_path = None

    @staticmethod
    def open_stream(path: Union[str, Path], **kwargs):
        """ Input stream factory

        :param path: Path to stream (file or serial port)
        :param baud: Baud rate of serial port. Ignored if file

        :return: Input stream instance

        """

        if not isinstance(path, str) and not isinstance(path, Path):
            raise TypeError("Path must be a string or pathlib.Path")

        path = Path(path)

        if not path.exists():
            raise FileNotFoundError("Specified GNSS source does not exist.")

        if path.is_char_device():
            return SerialPort(path, **kwargs)

        return InputFileStream(path)

    def __del__(self):
        self.ensure_closed()

    def __enter__(self):
        self.ensure_open()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ensure_closed()

    def enable_raw_recording(self, logpath: Union[Path, str]):
        """

        :param logpath:
        :return:
        """

        if not isinstance(logpath, Path) and not isinstance(logpath, str):
            raise TypeError('Log path must be a string or pathlib.Path')

        self._raw_log_path = Path(logpath)
        if not self._raw_log_path.parent.exists():
            raise FileNotFoundError('Log path parent directory does not exist.')

    def disable_raw_recording(self):
        """ Stop recording raw input
        """

        self._raw_log_path = None

    def _record_raw_stmt(self, stmt: bytes):
        """ Record a raw NMEA Message

        :param stmt: Raw NMEA Message

        """

        if self._raw_log_path is not None:
            with open(self._raw_log_path, 'ab') as fout:
                fout.write(stmt)

    def get_line(self) -> bytes:
        """ Receive a single line from the input stream

        :return: Encoded line (bytes)

        """

        raise NotImplementedError

    def ensure_open(self):
        """ Ensure stream is open
        """

        raise NotImplementedError

    def ensure_closed(self):
        """ Ensure stream is closed
        """

        raise NotImplementedError

    @staticmethod
    def verify_checksum(message: bytes) -> bool:
        """ Verify a NMEA message via checksum

        :param message: Bytes from NMEA stream

        :return: Boolean. True if valid

        TODO: Incorporate this function after the raw NMEA dump functionality has been completed

        """

        assert isinstance(message, bytes)

        xor = 0x00

        try:
            start = message.find(ord('$')) + 1
            end = message.find(ord('*'))
            for char in message[start:end]:
                xor = char ^ xor
            exp = str(message[end + 1:end + 3].decode()).upper()
            res = str(hex(xor))[2:].upper().zfill(2)
            return exp == res
        except Exception as e:
            print('Error calculating checksum of NMEA sentence: %s. Please file a bug report.' % str(e),
                  file=sys.stderr)
            return False


class InputFileStream (GenericInputStream):
    """ Read GPS data from a file
    """

    _fp = Union[TextIO, None]

    _path: Path

    def __init__(self, path: Union[Path, str]):
        """ Constructor

        :param path: Path to input file

        """

        if not isinstance(path, str) and not isinstance(path, Path):
            raise TypeError("Path must be a string or pathlib.Path")

        self._path = Path(path)
        if not self._path.exists():
            raise FileNotFoundError("Specified file %s does not exist." % str(self._path))

        self._fp = None

        GenericInputStream.__init__(self)

    def get_line(self) -> bytes:

        self.ensure_open()

        while True:
            line = self._fp.readline()
            self._record_raw_stmt(line)
            if self.verify_checksum(line):
                return line

    def ensure_open(self):
        if self._fp is None:
            self._fp = open(self._path, "rb")

    def ensure_closed(self):
        if self._fp is not None:
            self._fp.close()
        self._fp = None


class SerialPort (GenericInputStream):
    """ Read NMEA stream from a serial port
    """

    _stream: Union[serial.Serial, None]

    _port: Path
    _baud: int

    def __init__(self, path: Union[str, Path], baud: int = 4800, **kwargs):

        self._stream = None

        if not isinstance(path, str) and not isinstance(path, Path):
            raise TypeError("Path must be a string or pathlib.Path")
        if not isinstance(baud, int):
            raise TypeError("Baud rate must be an integer")

        self._port = Path(path)
        self._baud = baud

        self._stream = serial.Serial(port=str(self._port), baudrate=self._baud, **kwargs)
        self._stream.close()

        GenericInputStream.__init__(self)

    def get_line(self) -> bytes:
        self.ensure_open()
        while True:
            line = self._stream.readline()
            self._record_raw_stmt(line)
            if self.verify_checksum(line):
                return line

    def ensure_open(self):
        if not self._stream.is_open:
            self._stream.open()

    def ensure_closed(self):
        if self._stream is None:
            return

        if self._stream.is_open:
            self._stream.close()
