import logging
import struct
import sys

from tap_file import TapFileWriter, TapHeader, TapProgram, HeaderType


logging.basicConfig(level="DEBUG")

"""
Usage: tap-append-prg.py TAPFILE PRGFILE NAME

Append the program file PRGFILE to the .tap file TAPFILE using the
name NAME. Create TAPFILE if it does not exist.
"""


with TapFileWriter(sys.argv[1]) as t:
    with open(sys.argv[2], 'rb') as prg:
        # read program start address
        start_addr, = struct.unpack('<H', prg.read(2))
        # read program data
        data = prg.read()

    # BASIC programs start at $xx01
    htype = HeaderType.PRG_RELOC if start_addr & 0xff == 1 else HeaderType.PRG
    end_addr = start_addr + len(data)
    name = sys.argv[3].encode()

    h = TapHeader(htype, name, start=start_addr, end=end_addr)
    t.append(h, long_leader=True)
    d = TapProgram(data)
    t.append(d)
