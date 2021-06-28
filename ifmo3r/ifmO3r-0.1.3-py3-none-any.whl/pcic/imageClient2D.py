import socket
import ctypes as ct


class ImageClient2D:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(5)
        self.socket.connect((self.ip, self.port))
        self._recv_bufsize = 4096
        self._recvall_state = None         

    def _recvall(self, msg_len):
        if self._recvall_state is None:
            self._recvall_state = [bytearray(msg_len), 0]
        max_msg_size = self._recv_bufsize
        view = memoryview(self._recvall_state[0])[self._recvall_state[1]:]
        while self._recvall_state[1] < msg_len:
            try:
                nbytes = self.socket.recv_into(view, min(msg_len-self._recvall_state[1], max_msg_size))
                view = view[nbytes:]
            except:
                raise ConnectionAbortedError()
            if nbytes == 0:
                raise ConnectionLost()
            self._recvall_state[1] += nbytes
        ret = self._recvall_state[0]
        self._recvall_state = None
        return ret
    
    @staticmethod
    def _unpackChunkHeader(data):
        class Header(ct.Structure):
            _fields_ = [
                ("chunkType", ct.c_uint32),
                ("chunkSize", ct.c_uint32),
                ("headerSize", ct.c_uint32),
                ("headerVersion", ct.c_uint32),
                ("imageWidth", ct.c_uint32),
                ("imageHeight", ct.c_uint32),
                ("pixelformat", ct.c_uint32),
                ("timestamp", ct.c_uint32),
                ("frameCount", ct.c_uint32),
                ("statusCode", ct.c_uint32),
                ("timestampSec", ct.c_uint32),
                ("timestampNsec", ct.c_uint32)
            ]
        header = Header.from_buffer_copy(data[4:])
        return header

    def _recvChunk(self):
        data = self._recvall(4+48) # BeginMarker + ChunkHeader

        import struct
        beginMarker = struct.unpack("<I", data[0:4])[0]
        if beginMarker == 0xABCDDCBA:
            chunkHeader = self._unpackChunkHeader(data)
            chunkSize = chunkHeader.chunkSize
            chunkData = self._recvall(chunkSize - len(data))
            return chunkHeader, chunkData
        else:
            return None

    def readNextFrame(self):
            res = self._recvChunk()
            while res is None:
                res = self._recvChunk()
            chunkHeader, chunkData = res
            result = {}
            result["image_width"] = chunkHeader.imageWidth
            result["image_height"] = chunkHeader.imageHeight
            result["time_stamp_sec"] = chunkHeader.timestampSec
            result["time_stamp_nsec"] = chunkHeader.timestampNsec
            result["img_jpeg"] = chunkData
            return result

    def close(self):
        self.socket.close()