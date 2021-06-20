import logging
import struct

from pathlib import Path

from .magic import C64_MAGIC
from .profile import Profile

log = logging.getLogger(__name__)


class TapFileWriter:
    def __init__(self, filepath, version=1, platform=0, video=0, profile=None):
        self.filepath = Path(filepath) if isinstance(filepath, str) else filepath
        self.fileh = None
        self.version = version
        self.platform = platform
        self.video = video
        self.profile = profile if profile else Profile()

    def __enter__(self):
        if self.filepath.exists():
            # open existing file r/w
            log.debug("Opening existing file %s", self.filepath)
            self.fileh = self.filepath.open('r+b')
            # read header
            header = self.fileh.read(15)
            magic = None
            if len(header) == 15:
                magic, self.version, self.platform, self.video = struct.unpack('<12sBBB', header)

            if magic != C64_MAGIC:
                raise ValueError("Invalid file format")
            if self.version > 1:
                raise NotImplementedError("Unsupported version, "+str(self.version))

            # seek to end of file
            self.fileh.seek(0, 2)
        else:
            # open new file r/w
            log.debug("Creating new file %s", self.filepath)
            self.fileh = self.filepath.open('w+b')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.fileh:
            if exc_type is None:
                # update data length in header
                data_length = self.fileh.tell()-20
                log.debug("Updating data length, 0x%x", data_length)
                self.fileh.seek(16)
                self.fileh.write(struct.pack('<I', data_length))

            # close file
            self.fileh.close()

    def append(self, obj, long_leader=False):
        """Append a data object to the tap file."""
        if self.fileh.tell() == 0:
            # empty file, add header
            log.debug("Adding header")
            header = C64_MAGIC
            header += struct.pack('<BBBBI', self.version, self.platform, self.video, 0, 0)
            self.fileh.write(header)

        # add silence to mimic motor startup
        self.add_cycles([0x800])
        # add leader
        count = 0x6a00 if long_leader else 0x1a00
        self.add_leader(count)
        # add first copy
        self.add_data_stream(obj, 0x80)
        # add gap
        self.add_leader(0x50)
        # add second copy
        self.add_data_stream(obj, 0)
        # add trailer
        self.add_leader(0x50)

    def add_leader(self, count):
        log.debug("Adding leader, 0x%x", count)
        self.add_cycles([self.profile.ideal_s] * count)

    def add_data_stream(self, obj, top_bit):
        """Append encoded data stream to tapfile."""
        log.debug("Adding data stream, %s", obj)
        # prepend sync bytes
        sync_bytes = bytearray([n | top_bit for n in range(9, 0, -1)])
        data = sync_bytes + obj._data

        # append checksum of the data
        csum = 0
        for b in obj._data:
            csum ^= b
        data.append(csum)

        cycles = []
        for b in data:
            # start of data byte
            cycles += [self.profile.ideal_l, self.profile.ideal_m]
            check_bit = 1
            # encode each bit as a cycle pair, LSB first
            for _ in range(0, 8):
                cycles += self.bit_to_cycles(b & 1)
                check_bit ^= b & 1
                b >>= 1

            # encode check bit
            cycles += self.bit_to_cycles(check_bit)

        # end of data stream
        cycles.append(self.profile.ideal_l)
        self.add_cycles(cycles)

    def add_cycles(self, cycles):
        """Write values representing a list of cycles."""
        buffer = bytearray()
        for c in cycles:
            val = round(c / 8)
            if val < 256:
                buffer.append(val)
            else:
                buffer.append(0)
                if self.version == 1:
                    cyclesb = struct.pack('<I', c)
                    buffer += cyclesb[:3]
        self.fileh.write(buffer)

    def bit_to_cycles(self, b):
        """Return the pair of cycles to encode a single bit."""
        if b:
            return [self.profile.ideal_m, self.profile.ideal_s]
        return [self.profile.ideal_s, self.profile.ideal_m]
