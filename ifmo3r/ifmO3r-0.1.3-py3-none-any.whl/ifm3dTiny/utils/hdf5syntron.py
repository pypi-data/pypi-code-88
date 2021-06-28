# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2021 ifm electronic gmbh
#
# THE PROGRAM IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND.

# Implementation of cw format (including serialization and deserialization of different sensors)

import h5py
import numpy as np
import time
import datetime
import logging
from os import listdir, getcwd
from os.path import isfile, join

status_logger = logging.getLogger(__name__)


class _H5Writer(object):
    def __init__(self, filename, write_index, streams, formats, num_sensors, meta, desc=None):
        """"
        :param filename: filename with file extension
        :param write_index: global index for mapping global frame numbers to streams ids,
                            stream frame numbers and receive timestamps
        :param streams: description of the sensor stream - e.g o3r
        :param formats: name of data format structure
        :param num_sensors: number of sensors saved per stream (i.e number of imagers)
        :param dict meta: description string for meta information
        :param desc: optional description str containing meta data
        """

        self.f = h5py.File(filename, "w")
        self.write_index = write_index
        self.streams = streams
        self.formats = formats
        if write_index:
            self.global_index_dtype = np.dtype([(
                # receive timestamp of this frame, monotonic increasing
                'receive_timestamp', np.int64),
                # stream id providing new data
                ('current_stream_id', np.uint16),
                # pointer to last received data for the stream <current_stream_id> (in stream index domain)
                ('stream_idx', np.uint64)])

            # global index for mapping global frame numbers to streams ids, stream frame numbers and receive timestamps
            self.global_index = self.f.create_dataset("index/global_index", (0,), dtype=self.global_index_dtype,
                                                      chunks=True, maxshape=(None,))

            # TODO: check use of num_sensors var
            self.stream_ids = self.f.create_dataset("index/streams", (num_sensors,), dtype=h5py.special_dtype(vlen=str))
            self.stream_times = {}
            self.name2index = {}
            self.stream_indices = [-1] * len(streams)
        else:
            self.global_index = None
            self.stream_ids = None
            self.stream_times = None
            self.name2index = None

        self.stream_ds = {}
        self.stream_dt = {}

        # specify dtype structure
        for s_id, name in enumerate(streams):
            if write_index:
                self.name2index[name] = s_id
                self.stream_ids[s_id] = name
                self.stream_times[name] = self.f.create_dataset("index/timestamps/" + name, (0,), dtype=np.int64,
                                                                chunks=True, maxshape=(None,))

            # check that for each format str a format description exists
            self.stream_dt[name] = self.__check_format_compliance(formats[s_id])

            self.stream_ds[name] = self.f.create_dataset("streams/" + name, (0,), dtype=self.stream_dt[name],
                                                         chunks=True, maxshape=(None,))
            self.stream_ds[name].attrs["format"] = formats[s_id]

        # set creation date and time in UTC time
        self.f["/"].attrs["creation_date"] = self.__get_utc_now_time()[0]

        # set description str if supplied
        if desc is not None:
            self.f["/"].attrs["description"] = desc

        # write meta information as set at start of stream
        self.f["/"].attrs["meta"] = meta

    def __check_format_compliance(self, format):
        if format == "hdf5-compound":
            dtype = np.dtype(
                [('_data_timestamp', np.int64), ('_receive_timestamp', np.int64), ('_global_index', np.uint64),
                 ('amplitude', np.dtype('(172,224)|f4')), ('confidence', np.dtype('(172,224)|u1')),
                 ('distance', np.dtype('(172,224)|f4')), ('distance_noise', np.dtype('(172,224)|f4')),
                 ('cloud', np.dtype('(3,172,224)|f4'))])
            return dtype

        # following is just an example
        elif format == "imeas":
            dtype = np.dtype(
                [('_data_timestamp', np.int64), ('_receive_timestamp', np.int64), ('_global_index', np.uint64),
                 ('imeas', h5py.special_dtype(vlen=np.uint8))])
            return dtype
        elif format == "sensor":
            dtype = np.dtype(
                [('_data_timestamp', np.int64), ('_receive_timestamp', np.int64), ('_global_index', np.uint64),
                 ('amplitude', np.dtype('(480,640)|f4')), ('confidence', np.dtype('(480,640)|u1')),
                 ('distance', np.dtype('(480,640)|f4')), ('distance_noise', np.dtype('(480,640)|f4')),
                 ('cloud', np.dtype('(3,480,640)|f4'))])
            return dtype

        else:
            raise RuntimeError("Unsupported format")

    def __get_utc_now_time(self):
        utc_now = datetime.datetime.utcnow()
        self.ref_time = time.perf_counter()
        self.global_index_cnt = 0
        self.f["/"].attrs["name"] = "ifm_hdf5"
        self.f["/"].attrs["version"] = np.uint32(0)
        time_dt = np.dtype([('year', np.int32), ('month', np.uint8), ('day', np.uint8), ('hour', np.uint8),
                            ('minute', np.uint8), ('second', np.uint8), ('microsecond', np.uint32)])
        ts = np.zeros(1, time_dt)
        ts[0]['year'] = utc_now.year
        ts[0]['month'] = utc_now.month
        ts[0]['day'] = utc_now.day
        ts[0]['hour'] = utc_now.hour
        ts[0]['minute'] = utc_now.minute
        ts[0]['second'] = utc_now.second
        ts[0]['microsecond'] = utc_now.microsecond
        return ts

    def __enter__(self):
        return self

    def __exit__(self, exc_t, exc_v, trace):
        self.f.close()

    def close(self):
        self.f.close()
        self.f = None

    def append_data(self, name, data, timestamp):
        def append(field, item):
            l = field.len()
            field.resize((l + 1,) + field.shape[1:])
            if len(field.shape) == 1:
                field[l] = item
            elif len(field.shape) == 2:
                field[l, :] = item
            else:
                raise RuntimeError("Not implemented")

        a = np.zeros(1, self.stream_dt[name])
        a[0]['_data_timestamp'] = timestamp
        rcv_timestamp = np.int64((time.perf_counter() - self.ref_time) * 1000000)
        a[0]['_receive_timestamp'] = rcv_timestamp
        a[0]['_global_index'] = self.global_index_cnt
        self.global_index_cnt += 1
        for f in data.keys():
            a[0][f] = data[f]
        append(self.stream_ds[name], a[0])

        if self.write_index:
            t = np.zeros(1, self.global_index_dtype)
            t[0]['receive_timestamp'] = rcv_timestamp
            sid = self.name2index[name]
            t[0]['current_stream_id'] = sid
            self.stream_indices[sid] += 1
            t[0]['stream_idx'] = self.stream_indices[sid]
            append(self.global_index, t[0])
            append(self.stream_times[name], rcv_timestamp)

        # flush data after each dataset
        self.f.flush()


class H5Load:
    def __init__(self, files):
        self.files = files

    def check_simple_stream(self, index):
        from ifmO3r.ifm3dTiny.utils.hdf5dict import loadDictFromHdf5
        """
        checks if the h5 is simple data stream (multidimensional numpy array) in h5 without subgroups

        :param int index: index of files list of self.files
        """

        data = loadDictFromHdf5(self.files[index])
        status_logger.info("{} - arbitrary format".format(self.files[index]))

        for k in list(data.keys()):
            status_logger.info("file: {}, key: {}, shape: {}".format(self.files[index], k, data[k].shape))

    def check_syntron_format(self, index):
        """
        check if the files is a syntron internal data stream format

        :param int index: index of files list of self.files
        :return boolean: TRUE if possible match with syntron format definition, FALSE if not
        """

        file = self.files[index]
        f = h5py.File(file, 'r')

        try:
            list(f.keys()).index("streams")
        except ValueError:
            status_logger.info("{} - syntron format (?)".format(self.files[index]))
            return False
        else:
            data = []
            status_logger.info("filename: {}".format(file))
            for idx, stream in enumerate(list(f["streams"].keys())):
                data.append(np.array(f["streams"][stream]))

                # print some meta info
                fields = data[idx].dtype
                status_logger.info("{}: {}".format(stream, fields.descr))
            return True
        # TODO: implement a h5 check based on meta information (and existing format definitions) instead of content

    def load_h5_syntron(self, index):
        """
        load h5 file if the files is a syntron internal data stream format

        :param int index: index of files list of self.files
        :return boolean: np array data if format conform
        """

        file = self.files[index]
        f = h5py.File(file, 'r')

        try:
            list(f.keys()).index("streams")
        except ValueError:
            status_logger.info("{} - syntron format (?)".format(self.files[index]))
            return False
        else:
            status_logger.info("filename: {}".format(file))
            data = []
            for idx, stream in enumerate(list(f["streams"].keys())):
                data.append(np.array(f["streams"][stream]))

                # print some meta info
                fields = data[idx].dtype
                status_logger.debug("data shape num frame: {}".format((np.array(f["streams"][stream])).shape))
                status_logger.debug("data keys per frame: {}".format(fields))

            return data


def _create_example_dataset():
    # Example usage
    sensors = [("o3d3xx", "imeas"), ("o3d3xx_structured", 'hdf5-compound')]

    with _H5Writer(filename="tmp.h5", write_index=True, streams=[s[0] for s in sensors],
                   formats=[s[1] for s in sensors], num_sensors=2, desc=None) as f2:
        for idx in range(10):
            if np.random.rand(1) > 0.5:
                name = sensors[0][0]
            else:
                name = sensors[1][0]
            data = {}
            if name == "o3d3xx":
                l = int(np.random.rand() * 300)
                data['imeas'] = (np.random.rand(l) * 255).astype(np.uint8)
            elif name == "o3d3xx_structured":
                data['amplitude'] = np.random.rand(4, 6) * 65535
                data['cloud'] = np.random.rand(4, 6, 3)
            f2.append_data(name, data, time.perf_counter() * 1000000)

            # TODO: add example for O3R_38K and O3R_VGA


if __name__ == "__main__":
    #_create_example_dataset()

    from ifmO3r.ifm3dTiny import FrameGrabber, ImageBuffer, Device

    IP = '192.168.0.69'
    PORT = 50012
    cam = Device(IP, PORT)
    fg = FrameGrabber(cam)
    im = ImageBuffer()

    sensors = [("o3r"), ("hdf5-compound")]
    with _H5Writer(filename="test.h5", write_index=True, streams=['o3r'], formats=["hdf5-compound",],
                   num_sensors=2, desc="test dataset recording", meta="test") as f:
        # get some data
        fg.stream_on(image_buffer=im, timeout=5)

        num_img = 50
        c = 0
        while True:
            if c > num_img:
                fg.stream_on(image_buffer=im, timeout=5)
                break

            if im.__next__():
                amp = im.amplitude_image()
                conf = im.confidence_image()
                xyz = im.xyz_image()
                dist = im.distance_image()
                dist_noise = im.distance_noise_image()
                data = im.all_images()  # [x, y, z, distance, amplitude]

                tmp = {'amplitude': amp, 'cloud': xyz, 'confidence': conf, 'distance': dist,
                       'distance_noise': dist_noise}
                f.append_data("o3r", tmp, time.perf_counter() * 1000000)
                c += 1
