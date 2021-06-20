import logging
import sys

from tap_file import TapFileWriter, TapHeader, TapSeqData, HeaderType


logging.basicConfig(level="DEBUG")

"""
Usage: tap-append-seq.py TAPFILE SEQFILE NAME

Append the data file SEQFILE to the .tap file TAPFILE using the
name NAME. Create TAPFILE if it does not exist.
"""


with TapFileWriter(sys.argv[1]) as t:
    name = sys.argv[3].encode()

    h = TapHeader(HeaderType.SEQ, name)
    t.append(h, long_leader=True)

    with open(sys.argv[2], 'rb') as seq:
        while True:
            data = seq.read(TapSeqData.MAX_DATA)
            if len(data) < TapSeqData.MAX_DATA:
                # end of file
                d = TapSeqData(data + b'\x00')
                t.append(d)
                break
            else:
                d = TapSeqData(data)
                t.append(d)
