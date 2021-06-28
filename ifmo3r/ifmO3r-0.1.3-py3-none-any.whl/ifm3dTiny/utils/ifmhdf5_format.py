# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2021 ifm electronic gmbh
#
# THE PROGRAM IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND.
#

import datetime
import time
import numpy as np
import h5py

class IfmHdf5Writer:
    """
    Class for creating hdf5 files in the format preferred by ifm syntron PCA.
    """

    def __init__(self, filename, streamdef, use_receive_timestamps=True, silent_overwrite=False):
        """
        Creates a new hdf5 file for writing.

        :param filename: the filename given as a string
        :param streamdef: the stream definition, given as a dict mapping stream names (strings) to stream types (strings)
        :param use_receive_timestamps: if true (default) store the receive timestamps in the file. Otherwise use the
                                       data timestamps as receive times.
        """
        type_content = h5py.vlen_dtype(np.dtype(np.uint8))
        type_timestamp = np.int64
        dtype = [('imeas', type_content),
                 ('_data_timestamp', type_timestamp),
                 ('_receive_timestamp', type_timestamp),
                 ('_global_index', np.uint64)
                ]
        self._name = filename
        if not (self._name.endswith(".h5") or self._name.endswith(".hdf5") or self._name.endswith(".hdf")):
            self._name += ".h5"
        self._useRcvTimestamps = use_receive_timestamps
        # interpolate the name with optionally given variables
        dt = datetime.datetime.now()
        mode = "w" if silent_overwrite else "x"
        # create a new HDF5 file / truncate an existing file containing a stream for all existing input ports
        self._currentFile = h5py.File(self._name, mode=mode)
        streams = self._currentFile.create_group("streams")
        for sname in streamdef:
            streams.create_dataset(sname, (0,), chunks=(1,), maxshape=(None,), dtype=dtype)
        # setup variables needed during processing
        self._basetime = time.perf_counter_ns()
        self._globalIndex = 0
        # write global attributes
        self._currentFile["/"].attrs["name"] = "ifm_hdf5"
        self._currentFile["/"].attrs["version"] = np.uint32(0)
        utc_now = datetime.datetime.utcnow()
        time_dt = np.dtype([ ('year', np.int32), ('month', np.uint8), ('day', np.uint8), ('hour', np.uint8), ('minute', np.uint8), ('second', np.uint8), ('microsecond', np.uint32) ])
        ts = np.zeros(1, time_dt)
        ts[0]['year'] = utc_now.year
        ts[0]['month'] = utc_now.month
        ts[0]['day'] = utc_now.day
        ts[0]['hour'] = utc_now.hour
        ts[0]['minute'] = utc_now.minute
        ts[0]['second'] = utc_now.second
        ts[0]['microsecond'] = utc_now.microsecond
        self._currentFile["/"].attrs["creation_date"] = ts[0]
        self._currentFile["/"].attrs["description"] = "Written by " + __name__

    def writeStreamFrame(self, stream_name, buffer, data_type, data_timestamp_ns):
        """
        Writes a frame to the given stream.

        :param stream_name: the name of the stream to be written to (a string instance)
        :param buffer: the buffer to be written (a bytes instance)
        :param data_type: the name of the data type (a string instance)
        :param data_timestamp_ns: the timestamp of the data in [nanoseconds]
        """
        data_timestamp_us = (data_timestamp_ns + 500)//1000
        s = self._currentFile["streams"][stream_name]
        if not "format" in s.attrs:
            s.attrs["format"] = data_type
        if s.attrs["format"] != data_type:
            raise RuntimeError("The datatype given for port %s is inconsistent. Received %s, expected %s." %
                               (stream_name, data_type, s.attrs["format"]))

        # perform timestamp calculations
        if s.shape[0] > 0:
            lastDataTimestamp = s[-1]["_data_timestamp"]
            lastRcvTimestamp = s[-1]["_receive_timestamp"]
        else:
            lastDataTimestamp = data_timestamp_us
            lastRcvTimestamp = 0
        if self._useRcvTimestamps:
            rcvTimestamp = np.int64(time.perf_counter_ns() - self._basetime)//1000
        else:
            rcvTimestamp = max(1, data_timestamp_us - lastDataTimestamp)

        # append the new data to the existing HDF5 dataset
        s.resize((s.shape[0]+1,))
        s[-1:] = (np.frombuffer(buffer, dtype=np.uint8),
                  np.int64(data_timestamp_us),
                  np.int64(rcvTimestamp),
                  self._globalIndex)
        self._globalIndex = self._globalIndex + 1
        self._currentFile.flush()

    def close(self):
        self._currentFile.close()
        self._currentFile = None
