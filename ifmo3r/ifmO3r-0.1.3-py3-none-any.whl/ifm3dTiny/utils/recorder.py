# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2021 ifm electronic gmbh
#
# THE PROGRAM IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND.
#

import argparse
import datetime
import logging
from threading import Thread
import time
from queue import Queue
from ifmO3r.ifm3dTiny.utils.Receiver import ADReceiver, ConnectionLost
from ifmO3r.ifm3dTiny.utils.ifmhdf5_format import IfmHdf5Writer

logger = logging.getLogger(__name__)

def record(filename=None, numberOfSeconds=None, cameras=[2], ip="192.168.0.69", timeout=3.0):
    """
    Record the given cameras for the given number of seconds or until CTRL-C is pressed into the given file.
    ATM, only 3D cameras are supported

    :param filename: if None, automatically create a file based on the current date and time.
    :param numberOfSeconds: if None, record for infinite time
    :param cameras: a list of the camera indices
    :param ip: IP Address of the VPU
    :param timeout: Timeout in seconds
    :return:
    """
    if filename is None:
        filename = datetime.datetime.now().strftime("O3R_AD_%Y%m%d_%H%M%S.algodebug.h5")
    stream_names = {cid: "o3r_di_%d" % idx for idx,cid in enumerate(cameras)}
    f = IfmHdf5Writer(filename, {stream_names[cid]: "imeas" for cid in cameras})
    try:
        rcv = []
        threads = []
        queue = Queue(maxsize=10)
        t0 = time.monotonic_ns()
        numFrames = 0

        def threadFunc(receiver, cid):
            try:
                while True:
                    data = receiver.get()
                    queue.put((cid, data))
            except ConnectionLost:
                logger.info("Connection to algo debug lost.")

        for idx,cid in enumerate(cameras):
            rcv.append(ADReceiver(ip=ip, port=50010+cid, stream="com.ifm.imager.i%03d"%cid, threading=False,
                                  xmlrpcTimeout=timeout))
            rcv[-1].connect()
            threads.append(Thread(target=threadFunc, args=(rcv[-1], cid)))
            threads[-1].start()

        while True:
            cid, data = queue.get(timeout=timeout)
            f.writeStreamFrame(stream_names[cid], data, "imeas", time.time_ns())
            logger.debug("%s: wrote frame (%d bytes)", cid, len(data))
            numFrames += 1
            if numberOfSeconds is not None and  time.monotonic_ns() - t0 > numberOfSeconds*1e9:
                return
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt by user.")
    finally:
        logger.info("Wrote %d frames", numFrames)
        logger.debug("closing h5 file...")
        f.close()
        logger.debug("disconnecting...")
        for r in rcv:
            r.disconnect()
        logger.debug("joining threads...")
        for t in threads:
            t.join()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="ip address of VPU", default="192.168.0.69")
    parser.add_argument("--timeout", help="timeout to be used in the get function", default=3.0, type=float)
    parser.add_argument("--numSeconds", help="number of seconds to be recorded (default: record until CTRL-C)", default=None, type=int)
    parser.add_argument("--loglevel", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    parser.add_argument("--filename", help="target filename. If not given, a file will be created in the current directory.", default=None)
    parser.add_argument("portIndices", help="VPU ports to be recorded.", default=[2], nargs="*")
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)
    record(ip=args.ip, timeout=args.timeout, numberOfSeconds=args.numSeconds, filename=args.filename, cameras=[int(cid) for cid in args.portIndices], )

if __name__ == "__main__":
    main()
