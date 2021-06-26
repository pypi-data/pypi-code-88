import struct

class Validate():
    def read(func):
        def wrap(*args, **kwargs):           
            length = args[-1]
            if length < 0:
                raise RuntimeError(f'Invalid length: {length}')
            data = func(*args, **kwargs)
            if len(data) != length:
                # TODO: DiscoException
                raise RuntimeError(f'Unexpected data length. Expected: {length}. Received: {len(data)}')
            return data
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
