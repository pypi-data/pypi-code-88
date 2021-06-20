import struct
import sys

from d64 import DiskImage
from tap_file import TapFileReader, TapHeader, HeaderType


tape_image = TapFileReader(sys.argv[1])
with DiskImage(sys.argv[2], 'w') as disk_image:
    for obj in tape_image.contents():
        if isinstance(obj, TapHeader):
            if obj.htype in (HeaderType.PRG_RELOC, HeaderType.PRG):
                print("Copying PRG file", obj.name)
                out_file = disk_image.path(obj.name).open('w', ftype='PRG')
                out_file.write(struct.pack('<H', obj.start))
            elif obj.htype == HeaderType.SEQ:
                print("Copying SEQ file", obj.name)
                out_file = disk_image.path(obj.name).open('w', ftype='SEQ')
        else:
            # PRG or SEQ data
            out_file.write(obj.data)
            if obj.eof:
                out_file.close()
