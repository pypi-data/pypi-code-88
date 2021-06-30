from l0n0lnet import se
from ctypes import *


se.stream_parser_set_password.restype = c_bool
se.stream_parser_set_password.argtypes = [c_uint64, POINTER(c_char)]

se.stream_parser_encrypt.restype = c_bool
se.stream_parser_encrypt.argtypes = [c_uint64, POINTER(c_char), c_size_t]

se.stream_parser_decrypt.restype = c_bool
se.stream_parser_decrypt.argtypes = [c_uint64, POINTER(c_char), c_size_t]


class stream_parser:
    def __init__(self):
        self.id = se.create_stream_parser()

    @staticmethod
    def gen_password():
        p = b''
        p = p.zfill(256)
        se.se_gen_password(p)
        return p

    def set_password(self, p):
        return se.stream_parser_set_password(self.id, p)

    def encrypt(self, data):
        return se.stream_parser_encrypt(self.id, data, len(data))

    def decrypt(self, data):
        return se.stream_parser_decrypt(self.id, data, len(data))
