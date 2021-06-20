import logging


log = logging.getLogger(__name__)


class DataStream:
    """Stream of bytes including sync and checksum bytes."""
    BAD_BYTE = ord('#')

    def __init__(self):
        self.data = bytearray()
        self.byte_errors = set()

    def add_byte(self, bit_list):
        """Add byte to stream.

        `bit_list` is either an array of 9 integers (1 check + 8 data bits) or None if the byte is corrupt"""
        if bit_list is None:
            # error
            self.byte_errors.add(len(self.data))
            self.data.append(self.BAD_BYTE)
        else:
            # order is reversed: check bit, b7 .. b0
            check_bit = bit_list.pop(0)
            val = 0
            for b in bit_list:
                val <<= 1
                val |= b
                check_bit ^= b
            if check_bit == 0:
                self.byte_errors.add(len(self.data))
            self.data.append(val)

    def payload(self):
        """Return payload bytes and indexes of errors."""
        errors = {e-9 for e in self.byte_errors if e >= 9 and e < len(self.data)-1}
        return self.data[9:-1], errors

    def __len__(self):
        return len(self.data)

    def valid_sync(self):
        if len(self.data) < 10:
            return False
        valid = [None if n in self.byte_errors else (d & 0x7f == 9-n) for n, d in enumerate(self.data[:9])]
        return False not in valid

    def valid_checksum(self):
        if len(self.data) < 10:
            return False
        # skip sync
        csum = 0
        for b in self.data[9:]:
            csum ^= b
        return csum == 0

    def __str__(self):
        return "<DataStream: data_len - {}, #errors - {}>".format(len(self.data), len(self.byte_errors))

    @staticmethod
    def grade_streams(stream1, stream2, expected_size):
        if len(stream1) != len(stream2):
            if len(stream1) == expected_size:
                return stream1, stream2
            elif len(stream2) == expected_size:
                return stream2, stream1
            else:
                # neither stream is the correct length
                raise ValueError("Invalid stream header lengths, expected {}, {} & {}".format(expected_size, len(stream1), len(stream2)))

        if len(stream1) != expected_size:
            # neither stream is the correct length
            raise ValueError("Invalid stream header lengths, expected {}, {} & {}".format(expected_size, len(stream1), len(stream2)))

        # both streams are the correct length
        if (not stream1.byte_errors) and stream1.valid_checksum():
            return stream1, stream2
        elif (not stream2.byte_errors) and stream2.valid_checksum():
            return stream2, stream1

        # chose stream with the least errors
        if len(stream1.byte_errors) < len(stream2.byte_errors):
            return stream1, stream2
        return stream2, stream1
