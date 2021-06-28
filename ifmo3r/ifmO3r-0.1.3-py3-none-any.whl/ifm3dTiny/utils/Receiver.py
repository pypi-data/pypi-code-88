# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2021 ifm electronic gmbh
#
# THE PROGRAM IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND.
#

import ctypes as ct
import io
import logging
from queue import Queue
import select
import socket
import struct
from threading import Thread
from xmlrpc.client import ServerProxy, Transport
from http.client import HTTPConnection

IMEAS_AVAILABLE = False
MAGIC_FRAME_START = 0xffffdeda
MAGIC_FRAME_END = 0xadedffff

logger = logging.getLogger(__name__)

class BaseADReceiver(Queue):
    """
    Class for receiving data from algo debug. This class implements the data part only without
    connection logic.
    """

    class ChannelHeader(ct.Structure):
        """
        Header for transferring (parts of) channels over TCP, see AD_Impl.h for source code.
        """
        _fields_ = [
            ("id", ct.c_uint32),
            ("frameNumber", ct.c_uint32),
            ("channelIdx", ct.c_uint16),
            ("numChannels", ct.c_uint16),
            ("numSplits", ct.c_uint16),
            ("splitIdx", ct.c_uint16),
            ("totalChannelSize", ct.c_uint32),
            ("splitSize", ct.c_uint32),
            ("splitOffset", ct.c_uint32)
        ]

    def __init__(self, autoInterpret=False, maxsize=0, onceRepetitionRate=0):
        """
        Constructor

        :param maxsize: passed to the Queue constructor (0: infinite size)
        :param onceRepetitionRate: repetition rate of once channels (0: only output the once channels on demand)
        """
        super().__init__(maxsize=maxsize)
        self._frames = {}
        self._newInstance = True
        self._onceChannels = {}
        self._onceRepetitionRate = onceRepetitionRate
        self._outputOnceChannelsFrames = 0
        if autoInterpret and not IMEAS_AVAILABLE:
            raise RuntimeError("Need ifm_imeas package to interpret algo debug data.")
        self._autoInterpret = autoInterpret

    def pushChannelData(self, data):
        """
        Notifies the receiver about a new buffer from the algo debug instance.
        Eventually puts new output frames to this queue.
        This method is usually called directly from inherited classes.

        :param data: ctype structure of type SendbufArguments (see AD_cstructs.h)
        :return: None
        """
        # parse the buffer into header and payload
        if isinstance(data, ct.Array):
            hdr = ct.cast(data, ct.POINTER(self.ChannelHeader)).contents
        else:
            hdr = self.ChannelHeader.from_buffer_copy(data[:ct.sizeof(self.ChannelHeader)])
        buf = data[ct.sizeof(self.ChannelHeader):]

        if self._newInstance:
            if hdr.channelIdx == 0:
                self._newInstance = False
            else:
                # wait for clean start (this is only necessary because we get the data in async mode)
                return

        assert hdr.splitSize == len(buf)
        assert len(buf) + ct.sizeof(hdr) == len(data)

        if not hdr.frameNumber in self._frames:
            # the frame number is not yet known
            if hdr.splitIdx == 0:
                # split index is zero -> this is the start of the channel
                # add the frame and setup the channels as described in the header
                self._frames[hdr.frameNumber] = {}
                for i in range(hdr.numChannels):
                    self._frames[hdr.frameNumber][i] = [None, False]  # [buffer, completed]
            else:
                # the split idx is non-zero, this means that we do not have the beginning of the frame and therefore
                # we ignore the buffer
                logger.warning("Ignoring frame without history but non-zero split index.")
                return

        f = self._frames[hdr.frameNumber]
        if f[hdr.channelIdx][0] is None:
            # setup the buffer if not already there
            f[hdr.channelIdx][0] = bytearray(hdr.totalChannelSize)

        # fill the buffer with the given data
        f[hdr.channelIdx][0][hdr.splitOffset:hdr.splitOffset + hdr.splitSize] = buf

        if hdr.splitIdx == hdr.numSplits - 1:
            # last part of channel received
            f[hdr.channelIdx][1] = True
            assert hdr.splitOffset + hdr.splitSize == hdr.totalChannelSize
            # put completed frames to the queue
            self.output()

    def outputOnceChannelsInNextFrames(self, numFrames=1):
        self._outputOnceChannelsFrames = numFrames

    def output(self):
        """
        checks the frames for completion and put completed frames into the queue
        :return: None
        """
        magic_frame_start = struct.pack("<I", MAGIC_FRAME_START)
        magic_frame_end = struct.pack("<I", MAGIC_FRAME_END)
        for fn in sorted(self._frames.keys()):
            f = self._frames[fn]

            if all([f[c][1] for c in f.keys()]):
                # frame complete
                parts = [f[c][0] for c in f.keys()]
                if fn == 0:
                    # once channels are complete
                    self._onceChannels = parts[:]
                parts[0:0] = [magic_frame_start]
                if ((self._onceRepetitionRate > 0 and fn > 0 and fn % self._onceRepetitionRate == 0) or
                        (self._outputOnceChannelsFrames > 0)):
                    self._outputOnceChannelsFrames = max(0, self._outputOnceChannelsFrames - 1)
                    parts.extend(self._onceChannels)
                parts.append(magic_frame_end)
                r = b''.join([p for p in parts if p is not None])
                self.put(r)
                del self._frames[fn]
            else:
                logger.debug("not all channels are ready, number of frames in queue: %d, ready=%s", len(self._frames), [f[c][1] for c in f.keys()])
                return


class ConnectionLost(Exception):
    pass


class TimeoutTransport(Transport):
    def __init__(self, timeout):
        self.timeout = timeout
        super().__init__()

    def make_connection(self, host):
        connection = HTTPConnection(host)
        connection.timeout = self.timeout
        self._connection = host, connection
        return connection


class ADReceiver(BaseADReceiver):
    """
    Usage:

    with ADReceiver("192.168.0.69", 50010, "com.ifm.imager.i000", autoInterpret=True) as rcv:
        while 1:
            frame = rcv.get()
            # process frame
    """
    def __init__(self, ip, port, stream,
                 autoInterpret=False, threading=False, recv_bufsize=4096, onceRepetitionRate=0,
                 xmlrpcTimeout=3.0, xmlrpcPort=None, workaroundForMissingOnceChannels=True):
        """
        Constructor
        :param ip: ip address of the sensor
        :param port: port of the PCIC system
        :param stream: the stream to be recorded, given as a string (e.g. "com.ifm.imager.i000")
        """
        super().__init__(autoInterpret=autoInterpret, onceRepetitionRate=onceRepetitionRate)
        self._ip = ip
        self._port = port
        self._stream = stream
        self._threading = threading
        self._thread = None
        self._finished = False
        self._recv_bufsize = recv_bufsize
        self._recvall_state = None
        self._xmlrpcTimeout = xmlrpcTimeout
        self._xmlrpcPort = xmlrpcPort
        self._timebarrier = None
        self._workaroundForMissingOnceChannels = workaroundForMissingOnceChannels

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def threading(self):
        return self._threading

    def get(self, block=True, timeout=None):
        """
        Overwritten from queue.Queue. Note that block=False and timeout parameters are properly supported if and only
        if the receiver is in threading mode. Otherwise, this function might block even if requested otherwise.
        :param args:
        :param kwargs:
        :return:
        """
        self._timebarrier = None
        res = None
        if self._threading:
            if self._finished:
                raise ConnectionLost()
            res = super().get(block=block, timeout=timeout)
        else:
            if block and timeout is not None:
                self._timebarrier = time.monotonic() + timeout
                self._socket.setblocking(False)
            elif block and timeout is None:
                self._socket.setblocking(True)
            else:
                self._socket.setblocking(False)
            while self.empty():
                self._receiveFrame()
            res = super().get(block=block, timeout=timeout)
        # workaround for missing once channels
        if len(self._onceChannels) == 0 and self._workaroundForMissingOnceChannels:
            logger.warning("apply workaround for missing once channels")
            self.disconnect()
            self.connect()
        return res

    def _recvall(self, msg_len):
        if self._recvall_state is None:
            self._recvall_state = [bytearray(msg_len), 0]
        max_msg_size = self._recv_bufsize
        view = memoryview(self._recvall_state[0])[self._recvall_state[1]:]
        while self._recvall_state[1] < msg_len:
            nbytes=[]
            try:
                if self._timebarrier is not None:
                    timeout = max(0, self._timebarrier - time.monotonic())
                    select.select([self._socket], [], [], timeout)
                nbytes = self._socket.recv_into(view, min(msg_len - self._recvall_state[1], max_msg_size))
                view = view[nbytes:]
            except (ConnectionError, OSError) as err:
                logger.error("Received exception during socket.recv.")
                pass
            if not nbytes:
                logger.debug("received 0 bytes -> connection lost")
                raise ConnectionLost()
            self._recvall_state[1] += nbytes
        ret = self._recvall_state[0]
        self._recvall_state = None
        return ret

    def _receiveFrame(self):
        answer, ticket = self._readAnswer()
        logger.debug("ticket=%s len(ans)=%d", ticket, len(answer))
        if ticket == b"0000":
            logger.debug("Ignoring ticket 0000, length=%d", len(answer))
            return
        if ticket == b"0020":
            # algo debug
            algoDebugData = None
            f = io.BytesIO(answer)
            token = f.read(4)
            if token != b"star":
                raise RuntimeError("Unexpected token, expected b'star', got %s" % repr(token))
            while True:
                data = f.read(4)
                #print("_receiveFrame(debug): nextPacket:", data, struct.unpack("I", data) if len(data) == 4 else "")
                # stop if frame finished
                if data == b"stop":
                    break
                chunkType, = struct.unpack("I", data)
                try:
                    # else read rest of image header
                    chunkSize, headerSize, headerVersion, imageWidth, imageHeight, pixelFormat, timestamp, frameCount, \
                        statusCode, timestampSeconds, timestampNano = struct.unpack("IIIIIIIIIII", f.read(44))
                except struct.error:
                    logger.warning("Unexpected error in data stream, stop with this PCIC packet.")
                    break
                assert headerVersion == 3
                # read rest of chunk header
                metaData = f.read(headerSize - 48)
                chunkData = f.read(chunkSize-headerSize)
                if chunkType == 900:
                    logger.debug("push channel data to algo debug")
                    self.pushChannelData(chunkData)
                else:
                    logger.warning("Ignoring chunkType=%d", chunkType)

    def _receive(self):
        try:
            while True:
                self._receiveFrame()
        except Exception:
            if not self._finished:
                self._finished = True
                raise

    def _readAnswer(self, reqTicket = None):
        while True:
            answer = self._recvall(16)
            ticket = answer[0:4]
            ansLen = int(answer.split(b"L")[1])
            res = self._recvall(ansLen)
            assert res[:4] == ticket and len(res) == ansLen
            if reqTicket is None or ticket == reqTicket:
                break
        # skip the repeated ticket number and the "\r\n" end
        return res[4:-2], ticket

    def _sendCommand(self, cmd):
        cmdLen = len(cmd) + 6
        self._socket.sendall(b"1000L%09d\r\n1000%s\r\n" % (cmdLen, cmd))
        answer, _ = self._readAnswer(b"1000")
        return answer

    def _enableAlgoDebug(self, enabled):
        if self._stream is not None:
            host = self._ip if self._xmlrpcPort is None else ("%s:%d" % (self._ip, self._xmlrpcPort))
            prx = ServerProxy(uri="http://%s/api/rpc/v1/%s/params" % (host, self._stream), transport=TimeoutTransport(self._xmlrpcTimeout))
            prx.setParameter("enableAlgoDebug", enabled)
            logger.debug("getParameter('enableAlgoDebug') = %s (should be %s)", prx.getParameter("enableAlgoDebug"), enabled)

    def connect(self):
        """
        Connects to the sensor, enables algo debug on the specified stream and starts the working thread.
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # before connection, turn off algo debug
        self._enableAlgoDebug(False)
        self._enableAlgoDebug(True)
        self._socket.connect((self._ip, self._port))
    #     if False:
    #         # this is not yet supported by O3R's PCIC
    #         # disable all result output
    #         ans = self._sendCommand(b"p0")
    #         if ans[-1] != "*":
    #             raise RuntimeError("error sending p0: %s" % ans)
    #         pcicConfig = b"""\
    # {
    #     "layouter": "flexible",
    #     "format": {"dataencoding": "ascii"},
    #     "elements": [
    #         {"type": "string", "value": "star", "id": "start_string"},
    #         {"type": "blob", "id": "algo_debug"},
    #         {"type": "string", "value": "stop", "id": "end_string"}
    #     ]
    # }
    # """
    #         answer = self._sendCommand(b"c%09d%s" % (len(pcicConfig), pcicConfig))
    #         if not b"*" in answer:
    #             raise RuntimeError("Unexpected answer from PCIC: %s." % answer)
    #         self._sendCommand(b"p1")
        self._finished = False
        if self._threading:
            self._thread = Thread(target=self._receive)
            self._thread.start()

    def disconnect(self):
        """
        Disconnects from the sensor and finishes the working thread.
        :return:
        """
        self._finished = True
        self._socket.close() # this is kind of a forced exit, read() functions will fail after the socket is closed
        self._enableAlgoDebug(False)
        if self._threading:
            self._thread.join()
            self._thread = None
        self._socket = None

if __name__ == "__main__":
    import argparse
    import time

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="ip address of VPU", default="192.168.0.69")
    parser.add_argument("--port", help="port of PCIC interface", default=50012, type=int)
    parser.add_argument("--stream", help="xmlrpc object of camera", default="com.ifm.imager.i002")
    parser.add_argument("--threading", help="use threaded mode of ADReceiver", default=False, action="store_true")
    parser.add_argument("--timeout", help="timeout to be used in the get function", default=3.0, type=float)
    parser.add_argument("--frames", help="number of frames to be grabbed (-1 to grab forever)", default=-1, type=int)
    parser.add_argument("--interpret", help="interpret data (needs ifm_imeas package).", action="store_true")
    parser.add_argument("--loglevel", default="INFO")
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    with ADReceiver(args.ip, args.port, args.stream if args.stream != "" else None,
                    autoInterpret=args.interpret, threading=args.threading, xmlrpcTimeout=args.timeout) as rcv:
        cnt = 0
        t0 = time.time()
        while True:
            try:
                logger.debug("receiving frame ...")
                data = rcv.get(timeout=args.timeout)
            except socket.timeout:
                logger.debug("timeout")
                continue
            if args.interpret:
                logger.info("received imeas channels: %s", data.keys())
            else:
                logger.info("received %d bytes", len(data))
            cnt += 1
            if cnt > args.frames and args.frames >= 0:
                logger.info("Received %d frames in %.3f seconds.", cnt, time.time() - t0)
                break
