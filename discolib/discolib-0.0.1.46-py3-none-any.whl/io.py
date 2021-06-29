#
# DISCo Python interface library
# Copyright (c) 2021 Greg Van Aken
#
"""I/O Classes interfacing with DISCo devices directly.

Contains the base class DiscoIO which must be re-implemented using user-specific read() and write() functions,
dependent on the interface (USB, Serial, Network, etc.).
"""

import struct

class Validate():
    def read(func):
        def wrap(*args, **kwargs):           
            length = args[-1]
            if length < 0:
                # TODO: DiscoException (https://gavansystems.atlassian.net/browse/DIS-6)
                raise RuntimeError(f'Invalid length: {length}.')
            data = func(*args, **kwargs)
            if len(data) != length:
                # TODO: DiscoException (https://gavansystems.atlassian.net/browse/DIS-6)
                raise RuntimeError(f'Unexpected data length. Expected: {length}. Received: {len(data)}.')
            return data
        return wrap
    
    def write(func):
        def wrap(*args, **kwargs):
            data = args[-1]
            if type(data) is not bytes:
                # TODO: DiscoException (https://gavansystems.atlassian.net/browse/DIS-6)
                raise RuntimeError(f'Cannot write binary data of invalid type: {type(data)}.')
            if len(data) == 0:
                # TODO: DiscoException (https://gavansystems.atlassian.net/browse/DIS-6)
                raise RuntimeError(f'Cannot write empty bytes.')
            return func(*args, **kwargs)
        return wrap
    


class DiscoIO:

    def read(self, length: int, *args, **kwargs) -> bytes:
        raise NotImplementedError('Define your own DiscoIO class that implements read(length)!')
    
    def write(self, data: bytes, *args, **kwargs) -> None:
        raise NotImplementedError('Define your own DiscoIO class that implements write(data)!')

    def read_response(self):
        response = bytes()
        h1, h2, len = struct.unpack('BBB', self.read(3))
        if (h1 == h2 == 0x42):
            response = self.read(len-1) # TODO: CS
        return response
