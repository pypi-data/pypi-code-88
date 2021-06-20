import logging
import struct

from .data_stream import DataStream
from .dipole import Dipole
from .header_type import HeaderType
from .magic import is_valid_image
from .tap_header import TapHeader
from .tap_program import TapProgram
from .tap_seq_data import TapSeqData

log = logging.getLogger(__name__)


class TapFileReader:
    def __init__(self, file_path, profile=None):
        if not is_valid_image(file_path):
            raise ValueError("Invalid file format")

        self.fileh = file_path.open('rb')
        header = self.fileh.read(0x14)
        self.version = header[12]
        if self.version > 1:
            raise NotImplementedError("Unsupported version, "+str(self.version))
        self.platform = header[13]
        self.video = header[14]
        self.length, = struct.unpack('<L', header[0x10:0x14])
        self.dipole = Dipole(profile)

    def next_dipole(self):
        data = self.fileh.read(1)
        if not data:
            self.fileh.close()
            return None

        if ord(data) == 0:
            if self.version == 0:
                val = None
            else:
                data = self.fileh.read(3)+b'\x00'
                val, = struct.unpack('<L', data)
        else:
            val = ord(data)*8

        d = self.dipole.classify(val)
        return d

    def consume_leader(self, d):
        if d == 'S':
            self.leader += 1
        elif d == 'L' and self.leader >= 16:
            # end of leader
            self.in_leader = False
            self.queued = d
            self.stream = DataStream()
        else:
            self.leader -= 1

    def consume_byte_stream(self, d):
        self.queued += d

        if self.queued.endswith('SSSS') and len(self.stream) == 0:
            # still in leader
            self.in_leader = True
            return None

        eod = self.queued.endswith('LSSS')
        if eod:
            self.queued = self.queued[:-2]
        if self.queued.endswith('LM') or eod:
            if self.queued == 'LM':
                # initial start of data
                self.queued = ''
            elif len(self.queued) >= 20:
                # may have a complete, good byte
                to_process = []
                for i in range(len(self.queued)-4, len(self.queued)-22, -2):
                    if self.queued[i:i+2] in ('SM', 'MS'):
                        # valid data bit
                        to_process.append(int(self.queued[i:i+2] == 'MS'))
                    else:
                        # invalid, continue queuing
                        break

                if len(to_process) == 9:
                    # good byte

                    self.queued = self.queued[:-20]
                    if self.queued:
                        # one or more bad bytes before this good one
                        errors = (len(self.queued)-1)//20+1
                        for _ in range(0, errors):
                            self.stream.add_byte(None)
                        self.queued = ''

                    self.stream.add_byte(to_process)

        if eod and len(self.queued) == 0:
            self.in_leader = True
            self.leader = 0
            if len(self.stream) > 10:
                return self.stream
        return None

    def byte_stream(self, is_header=True):
        self.leader = 0
        self.in_leader = True

        while True:
            d = self.next_dipole()
            if d is None:
                return None
            if self.in_leader:
                self.consume_leader(d)
            else:
                ret = self.consume_byte_stream(d)
                if ret:
                    # if a header is expected ignore obviously short streams
                    if not is_header or len(ret) >= 200:
                        return ret

    def contents(self):
        """Return the next data object in the file."""
        while True:
            # consume first header
            header1 = self.byte_stream()
            log.debug("header1: %s", header1)
            if not header1:
                return

            # consume second header
            header2 = self.byte_stream()
            log.debug("header2: %s", header2)
            if not header2:
                return

            # choose best header (yield)
            header = TapHeader.create_from_streams(header1, header2)
            log.debug("Header: %s", header)
            yield header

            if header.htype in (HeaderType.PRG_RELOC, HeaderType.PRG):
                # consume first PRG payload
                data1 = self.byte_stream(is_header=False)
                log.debug("data1: %s", data1)
                if not data1:
                    return

                # consume second PRG payload
                data2 = self.byte_stream(is_header=False)
                log.debug("data2: %s", data2)
                if not data2:
                    return

                # choose best PRG payload (yield)
                data = TapProgram.create_from_streams(data1, data2, header.end-header.start)
                log.debug("Data: %s", data)
                yield data
            elif header.htype == HeaderType.SEQ:
                while True:
                    # consume first SEQ payload
                    seq1 = self.byte_stream()
                    log.debug("seq1: %s", seq1)
                    if not seq1:
                        return

                    # consume second SEQ payload
                    seq2 = self.byte_stream()
                    log.debug("seq2: %s", seq2)
                    if not seq2:
                        return

                    # choose best SEQ payload (yield)
                    data = TapSeqData.create_from_streams(seq1, seq2)
                    log.debug("Data: %s", data)
                    yield data

                    if data.eof:
                        break
