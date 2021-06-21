import sys

import cbmcodecs

from d64 import DiskImage


with DiskImage(sys.argv[1]) as image:
    for line in image.directory('petscii-c64en-uc'):
        print(line)
