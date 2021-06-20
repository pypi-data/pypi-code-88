import logging
import sys

from tap_file import TapFileReader, HeaderType


logging.basicConfig(level="DEBUG")

t = TapFileReader(sys.argv[1])

header = None

for obj in t.contents():
    if header is None:
        print("header", obj.htype, obj.start, obj.end, obj.name, obj.uncorrected_errors)
        if obj.htype in (HeaderType.PRG_RELOC, HeaderType.PRG, HeaderType.SEQ):
            header = obj
    else:
        print("data", obj.data)
        if obj.eof:
            print("End of file")
            header = None
