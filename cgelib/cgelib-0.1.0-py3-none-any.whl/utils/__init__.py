# Created by Alfred Ferrer Florensa
"""Contains utils"""


class FormatFile:
    def is_gzipped(file_path):
        ''' Returns True if file is gzipped and False otherwise.
            The result is inferred from the first two bits in the file read
            from the input path.
            On unix systems this should be: 1f 8b
            Theoretically there could be exceptions to this test but it is
            unlikely and impossible if the input files are otherwise expected
            to be encoded in utf-8.
        '''
        with open(file_path, mode='rb') as fh:
            bit_start = fh.read(2)
        if(bit_start == b'\x1f\x8b'):
            return True
        else:
            return False
