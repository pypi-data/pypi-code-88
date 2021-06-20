import logging

from .data_stream import DataStream
from .header_type import HeaderType
from .tap_object import TapObject


log = logging.getLogger(__name__)


class TapSeqData(TapObject):
    """Sequential data file data object."""
    MAX_DATA = 191

    def __init__(self, data):
        if len(data) > self.MAX_DATA:
            raise ValueError("Data too long")
        self._data = bytearray([HeaderType.SEQ_DATA])
        self._data += data.ljust(self.MAX_DATA, b'\x00')
        self.uncorrected_errors = False

    @classmethod
    def create_from_streams(cls, stream1, stream2):
        obj = cls.__new__(cls)
        obj.primary, obj.secondary = DataStream.grade_streams(stream1, stream2, 202)
        obj._init_from_streams()
        return obj

    @property
    def data(self):
        """Return data before the NUL byte."""
        nul = self._data.find(b'\x00')
        if nul == -1:
            return self._data[1:]
        return self._data[1:nul]

    @property
    def eof(self):
        """True if this is the final object."""
        return self._data.find(b'\x00') != -1
