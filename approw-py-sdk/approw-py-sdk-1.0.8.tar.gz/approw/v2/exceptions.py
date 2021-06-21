# coding: utf-8
import sys


class ApprowException(Exception):
    def __init__(self, code, errmsg):
        self.code = code
        self.message = errmsg

    def __str__(self):
        message = self.message.encode(
            'utf-8') if sys.version_info[0] == 2 else self.message
        return 'Approw Request Error: {} {}'.format(self.code, message)


class ApprowWrongArgumentException(Exception):
    pass
