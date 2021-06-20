from .data_stream import DataStream
from .tap_object import TapObject


class TapProgram(TapObject):
    """Program data object."""
    def __init__(self, data):
        self._data = data
        self.uncorrected_errors = False

    @classmethod
    def create_from_streams(cls, stream1, stream2, length):
        obj = cls.__new__(cls)
        obj.primary, obj.secondary = DataStream.grade_streams(stream1, stream2, length+10)
        obj._init_from_streams()
        return obj

    @property
    def data(self):
        """Program payload."""
        return self._data

    @property
    def eof(self):
        return True
