import struct
import sys

from tap_file import TapFileReader, HeaderType


t = TapFileReader(sys.argv[1])
name = sys.argv[2].encode()

expect_header = True
data = b''
start_addr = None
matches = False

for obj in t.contents():
    if expect_header:
        if obj.htype == HeaderType.SEQ_DATA:
            if matches:
                data += obj.data
                if obj.seq_eof:
                    # last block
                    break
        else:
            if name == obj.name:
                matches = True
            if obj.htype in (HeaderType.PRG_RELOC, HeaderType.PRG):
                expect_header = False
                start_addr = obj.start
    else:
        expect_header = True
        if matches:
            data = obj.data
            break

if data:
    print("Writing", sys.argv[2])
    with open(sys.argv[2], 'wb') as fileh:
        if start_addr is not None:
            fileh.write(struct.pack('<H', start_addr))
        fileh.write(data)
