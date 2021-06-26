import struct
from discolib.io import DiscoIO
from serialclass import SerialClass

class DiscoAttribute(SerialClass):

    def __init__(self, port: int, type: str, name: str, io_handler: DiscoIO) -> None:
        self.port = port
        self.type = type
        self.name = name
        self._setpoint = None
        self._readback = None
        self._io = io_handler

    @property
    def setpoint(self):
        return self._setpoint

    @property
    def readback(self):
        return self._readback

    @setpoint.setter
    def setpoint(self, value):
        self._setpoint = value
        data = bytes([0x42, 0x42, 0x04, 0x25, self.port, self._setpoint, 0x10])
        self._io.write(data)

    @setpoint.getter
    def setpoint(self):
        data = bytes([0x42, 0x42, 0x03, 0x05, self.port, 0x10])
        self._io.write(data)
        resp = self._io.read_response()
        self._setpoint = struct.unpack(self.type, resp)[0]
        return self._setpoint

    @readback.getter
    def readback(self):
        data = bytes([0x42, 0x42, 0x03, 0x04, self.port, 0x10])
        self._io.write(data)
        resp = self._io.read_response()
        self._readback = struct.unpack(self.type, resp)[0]
        return self._readback
