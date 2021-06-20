import logging
import struct

from .data_stream import DataStream
from .header_type import HeaderType
from .tap_object import TapObject


log = logging.getLogger(__name__)


class TapHeader(TapObject):
    """All objects except program data."""
    def __init__(self, htype, name, start=None, end=None):
        if htype in (HeaderType.PRG_RELOC, HeaderType.PRG):
            if start is None:
                raise ValueError("Missing start address")
            if end is None:
                raise ValueError("Missing end address")

        if start is None:
            start = 32768
        if end is None:
            end = 0
        self._data = struct.pack('<BHH', htype, start, end)
        self._data += name.ljust(192-5, b' ')
        self.uncorrected_errors = False

    @classmethod
    def create_from_streams(cls, stream1, stream2):
        obj = cls.__new__(cls)
        obj.primary, obj.secondary = DataStream.grade_streams(stream1, stream2, 202)
        obj._init_from_streams()
        return obj

    @property
    def htype(self):
        """Header type."""
        return HeaderType(self._data[0])

    @property
    def start(self):
        """Start address, only valid for program headers."""
        return struct.unpack('<H', self._data[1:3])[0]

    @property
    def end(self):
        """End address, only valid for program headers."""
        return struct.unpack('<H', self._data[3:5])[0]

    @property
    def name(self):
        """File name."""
        return bytes(self._data[5:21].rstrip(b' '))

    @property
    def data(self):
        """For SEQ objects the payload, rest of header after file name for others."""
        if self.htype == HeaderType.SEQ_DATA:
            nul = self._data.find(b'\x00')
            if nul == -1:
                return self._data[1:]
            return self._data[1:nul]
        return self._data[21:]

    @property
    def seq_eof(self):
        """True if payload contains NUL."""
        return self._data.find(b'\x00') != -1
