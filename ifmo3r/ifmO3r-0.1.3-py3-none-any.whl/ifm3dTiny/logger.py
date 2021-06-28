# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2021 ifm electronic gmbh
#
# THE PROGRAM IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND.
#

import os
import pickle
import struct
from pathlib import Path
import h5py
import matplotlib.pyplot as plt
import numpy as np
import time
import datetime
import logging
from json import dumps
import argparse

from ifmO3r.ifm3dTiny.utils import hdf5dict, GetCallableMethods
from ifmO3r.ifm3dTiny.grabber import FrameGrabber, ImageBuffer
from ifmO3r.ifm3dTiny.utils import recorder
from ifmO3r.ifm3dTiny.utils.hdf5syntron import _H5Writer
from ifmO3r.ifm3dTiny.utils.utils import get_SW_version

# %%
DEFAULT_IMAGE_STACK_DEPTH = 10  # Arbitrary number
DEFAULT_TIMEOUT = 5  # Timeout in sec.
DEFAULT_TIMEOUT_LIVE = 30

# %%

status_logger = logging.getLogger(__name__)

class ImageLogger:
    """
    This image logger class provides helper functions for writing image data to file
    """
    def __init__(self, device, frameGrabber, imageBuffer, path=None):
        """
        :param path: std output path for all data written to file
        :param frameGrabber: frame grabber object of the grabber class
        :param imageBuffer: image buffer object of the grabber class
        :device: device object of the device class
        """

        # check for provided data output path
        if path is None:
            cwd = os.getcwd()
            self.path = os.path.join(cwd, 'data')
            if not os.path.exists(self.path):
                try:
                    os.makedirs(self.path)
                except IOError as err:
                    print('A data output folder can not be created at the current working directory: ', err)
        else:
            self.path = path
            if not os.path.exists(self.path):
                try:
                    os.makedirs(self.path)
                except IOError as err:
                    print('The output folder can not created', err)

        # set FrameGrabber and ImageBuffer, and Device
        self.frameGrabber = frameGrabber
        self.imageBuffer = imageBuffer
        self.device = device

        # get the first frame and set it inside the ImageBuffer
        self.frameGrabber.wait_for_frame(image_buffer=self.imageBuffer, timeout=DEFAULT_TIMEOUT)

    def __str__(self):
        method_list = GetCallableMethods().get_methods(self)
        return method_list

    def _set_frame(self, frame):
        """
        setter method for setting to a specific frame from the outside
        :param frame: frame object of the frameGrabber class
        :return:
        """
        self.imageBuffer._set_frame(frame=frame)

    def _get_frame(self):
        """
        returns the frame currently stored inside the ImageBuffer object
        :return: frame
        """
        return self.imageBuffer._get_frame()

    def get_current_frame(self, timeout=DEFAULT_TIMEOUT):
        """
        this method sets to frame inside the ImageBuffer to the current frame
        :return:
        """
        self.frameGrabber.wait_for_frame(self.imageBuffer, timeout)

    def write_png(self, dictToSave):
        """
        write a the data of a frame png file: provide a list of the names of the data fields
        :param dictToSave: dict of key - value pairs: of data fields and file names to be written
            (e.g. {"distance": "distance_frame1", "amplitude": "amplitude_frame1", "confidence": "confidence_frame1"})
        :return:
        :raises: IOError, Exception
        """

        try:
            for key in list(dictToSave.keys()):
                if 'distance' in key.lower():
                    distance_img = self.imageBuffer.distance_image()
                    self.__write_png(distance_img, str(dictToSave[key]))
                elif 'amplitude' in key.lower():
                    amplitude_img = self.imageBuffer.amplitude_image()
                    self.__write_png(amplitude_img, str(dictToSave[key]))
                elif 'confidence' in key.lower():
                    confidence_img = self.imageBuffer.confidence_image()
                    self.__write_png(confidence_img, str(dictToSave[key]))
                else:
                    raise NameError('The data field of the supplied key can not be written to a png file currently.')
        except OSError as e:
            print('Writing data to file failed')
            print(e)
            pass

    def write_binary(self, dictToSave):
        """
        write a the data of a frame to binary file: provide a list of the names of the data fields
        :param dictToSave: dict of key - value pairs: of data fields and file names to be written
            (e.g. {"x": "x_frame1", "y": "y_frame1", "z": "z_frame1",
            "distance": "distance_frame1", "amplitude": "amplitude_frame1", "confidence": "confidence_frame1"})

        :return:
        :raises: IOError, Exception
        """
        x, y, z = self.imageBuffer.xyz_image()

        try:
            for key in list(dictToSave.keys()):
                if 'x' in key.lower():
                    self.__write_binary(x, np.uint16, str(dictToSave[key]))
                elif 'y' in key.lower():
                    self.__write_binary(y, np.uint16, str(dictToSave[key]))
                elif 'z' in key.lower():
                    self.__write_binary(z, np.uint16, str(dictToSave[key]))

                elif 'distance' in key.lower():
                    distance_img = self.imageBuffer.distance_image()
                    self.__write_binary(distance_img, np.float32, str(dictToSave[key]))
                elif 'amplitude' in key.lower():
                    amplitude_img = self.imageBuffer.amplitude_image()
                    self.__write_binary(amplitude_img, np.uint16, str(dictToSave[key]))
                elif 'confidence' in key.lower():
                    confidence_img = self.imageBuffer.confidence_image()  # TODO: replace dummy method in ImageBuffer
                    self.__write_binary(confidence_img, np.uint16, str(dictToSave[key]))
                else:
                    raise NameError('The data field of the supplied key can not be written to a binary file currently.')
        except OSError as e:
            print('Writing data to file failed')
            print(e)
            pass

    def write_to_h5(self, dictToSave):
        """
        write a the data of a frame to hdf5 file: provide a list of the names of the data fields
        :param (e.g. {"x": "x_frame1", "y": "y_frame1", "z": "z_frame1",
            "distance": "distance_frame1", "amplitude": "amplitude_frame1", "confidence": "confidence_frame1"})
        :return:
        :raises: IOError, Exception
        """
        x, y, z = self.imageBuffer.xyz_image()

        try:
            for key in list(dictToSave.keys()):
                if 'x' in key.lower():
                    self.__write_h5(x, str(dictToSave[key]))
                elif 'y' in key.lower():
                    self.__write_h5(y,str(dictToSave[key]))
                elif 'z' in key.lower():
                    self.__write_h5(z, str(dictToSave[key]))

                elif 'distance' in key.lower():
                    distance_img = self.imageBuffer.distance_image()
                    self.__write_h5(distance_img, str(dictToSave[key]))
                elif 'amplitude' in key.lower():
                    amplitude_img = self.imageBuffer.amplitude_image()
                    self.__write_h5(amplitude_img, str(dictToSave[key]))
                elif 'confidence' in key.lower():
                    confidence_img = self.imageBuffer.confidence_image()
                    self.__write_h5(confidence_img, str(dictToSave[key]))
                else:
                    raise NameError('The data field of the supplied key can not be written to a h5 file currently.')
        except OSError as e:
            print('Writing data to file failed')
            print(e)
            pass

    def __write_h5(self, data, name, filename=None):
        """
        this method expects numpy array and writes the data to HDF5

        :param data: data to be written to file (expects: np.array)
        :param name: name of the data field inside the hdf5 object
        :param filename: output filename without file designation
        :return:
        :raise:IOError, OSError

        """
        if filename is None:
            filename = "{}.h5".format(str(name))
            filename_out = os.path.join(self.path, filename)
        else:
            filename_out = os.path.join(self.path, "{}.h5".format(filename))
        try:
            hf = h5py.File(filename_out, 'w')
            hf.create_dataset(name, data=data)
            hf.close()
        except IOError as e:
            print('The data can not be written to file. Did you check the permissions of the file directory?')
            print(e)
            pass

    def _write_frame_to_h5(self, filename):
        """
        write a complete frame to hdf5-file
        :param filename: output filename without file designation
        :return:
        """
        # set output path based on filename
        filename_out = os.path.join(self.path, "{}.h5".format(filename))

        # convert arrays in frame to np.arrays
        x, y, z = self.imageBuffer.xyz_image()
        distance = self.imageBuffer.distance_image()
        amplitude = self.imageBuffer.amplitude_image()
        confidence_img = self.imageBuffer.confidence_image()
        distance_noise_tmp = self.imageBuffer.frame['distance_noise']
        distance_noise = np.resize(distance_noise_tmp, (self.imageBuffer.height, self.imageBuffer.width))
        distance_noise = np.frombuffer(distance_noise, dtype=np.float32)

        # get the current frame for the rest of the data
        frame_current = self._get_frame()
        extrinsic = frame_current['distance_image_info'].ExtrinsicOpticToUser
        intrinsic = frame_current['distance_image_info'].IntrinsicCalibration

        # TODO: add further data fields to hdf5 export

        # create new dict
        frame = {'distance': distance,
                 'amplitude': amplitude,
                 'confidence': confidence_img,
                 'x': x,
                 'y': y,
                 'z': z,
                 }
        hdf5dict.saveDictToHdf5(frame, filename_out)

    def __write_png(self, data, filename):
        """
        this method expects a numpy array and writes the data to PNG
        :param data: data to be written to file (expects: np.array)
        :param filename: output filename without file designation
        :return:
        """
        try:
            filename_out = os.path.join(self.path, "{}.png".format(filename))
            plt.imsave(filename_out, data)
        except IOError as e:
            print('The data can not be written to file. Did you check the permissions of the file directory?')
            print(e)
            pass


    def __write_binary(self, data, d_type, name):
        """
        this method expects a numpy array and writes the data to non-structured binary output file
        :param data: data to be written to file
        :param d_type: data type (e.g. numpy.flat32)
        :param name:  output filename without file designation
        :return:
        """
        filename_out = os.path.join(self.path, str(name))
        data = np.frombuffer(data, dtype=d_type)

        # struct format based on numpy data types
        if d_type == 'float32':
            fmt = 'f' * len(data)
        elif d_type == 'float64':
            fmt = 'd' * len(data)
        elif d_type == 'uint8':
            fmt = 'H' * len(data)
        elif d_type == 'uint16':
            fmt = 'L' * len(data)
        elif d_type == 'uint32':
            fmt = 'Q' * len(data)
        else:
            fmt = 'd' * len(data)

        try:
            # pack the data and write to file
            f = open(filename_out, "wb")
            data_bin = struct.pack(fmt, *data)
            f.write(data_bin)
            f.close()
        except IOError as e:
            print('The data can not be written to file. Did you check the permissions of the file directory?')
            print(e)
            pass

    def save_frame_as_pickle(self, name=None):
        """
        saves the complete frame by serializing it and save to pickle file
        :param name: filename of the output
        :return:
        """
        if name is None:
            name = "{}.p".format('frame')
            name = os.path.join(self.path, name)
        else:
            name = os.path.join(self.path, "{}.p".format(name))

        try:
            pickle.dump(self.imageBuffer.frame, open(name, "wb"))
        except IOError as e:
            print('The data can not be written to file. Did you check the permissions of the file directory?')
            print(e)
            pass

    def load_frame_from_pickle(self, name):
        """
        load frame from pickle file
        :param name: filename
        :return:
        """
        try:
            frame_from_pickle = pickle.load(open(name, "rb"))
            self._set_frame(frame_from_pickle)
        except OSError as e:
            print('File not found')
            pass
        return frame_from_pickle

    def save_images_png(self, amount, img_type):
        """
        Save several images in a row. The while loop is used, because the
        python program might be faster than the receiving of images.

        :amount     :   How many images should be saved
        :img_type   :   List, which kind of images should be saved
        """
        self.frameGrabber.stream_on(self.imageBuffer, 30)
        time.sleep(0.5)
        i = 0
        while True:
            if i >= amount:
                break

            if next(self.imageBuffer):
                for t in img_type:
                    self.write_png({
                        t:f'frame_{t}_{i}'
                        })
                    i += 1

        self.frameGrabber.stream_on(self.imageBuffer, 30)

    def save_algo_debug_data(self, cameraID=[2], numSeconds=15, filename=None):
        """
        Save algo debug data: binary data used for post processing / scientific purposes.
        Use with caution, the data format definition is proprietary to ifm and not shared.
        Only the data streams written to file can be analyzed later on. A mode change based on recorded data in not
        possible, so only distance information as seen by the user during the recording can be evaluated.
        Previously seen data or data streams can not be saved in retrospect.

        :param cameraID: port ID of camera(s) from which to grab the data
        :param filename: filename in cwd or absolute path to file
        :param numSeconds: if None, record for infinite time
        """
        recorder.record(filename=filename, numberOfSeconds=numSeconds, cameras=cameraID, ip=self.device.ip,
                        timeout=DEFAULT_TIMEOUT)

    def save_data_stream(self, streams, num_sensors=2, write_index=True, numSeconds=5, desc=None,
                         filename=None):
        """
        Save a data stream as a h5 file. Previously seen data or data streams can not be saved in retrospect.

        :param list streams: list of description of the sensor stream - e.g ["o3r"]
        :param list formats: list of description of the sensor stream format - see list of possible formats
                            - e.g ["O3R-38k"]
        :param num_sensors: number of sensors saved per stream (i.e number of imagers)
        :param bool write_index: global index for mapping global frame numbers to streams ids,
                            stream frame numbers and receive timestamps
        :param int numSeconds: number of seconds which will be saved to file. default 5 sec
        :param str desc: optional description str
        :param str filename: filename of the created h5 file
        :return int: number of frames saved
        """
        # TODO: implement saving multiple streams simultaneously
        # TODO: implement method to check currently implemented stream formats

        if filename is None:
            filename = datetime.datetime.now().strftime("O3R_data_%Y%m%d_%H%M%S.h5")

        # get the current frame rate and calculate amount of frames from it
        params = self.device.dump()
        frame_rate = params[list(params.keys())[0]]["mode"]["modeParam"]["framerate"]
        amount = int(numSeconds*frame_rate)

        # collect meta information
        # VPU SW version, ifmO3r package version, acquisition and filter parameters,
        # calib file parameters
        # for this get a current frame
        self.frameGrabber.wait_for_frame(image_buffer=self.imageBuffer, timeout=DEFAULT_TIMEOUT)
        #vpu_sw_version = get_SW_version()
        ifmO3r_version = "0.1.3" # TODO implement dunder __version__ for ifmO3r package
        intrinsic = self.imageBuffer.frame['distance_image_info'].IntrinsicCalibration.__str__()
        #meta = {"vpu_sw_version": vpu_sw_version, "ifmO3r_version": ifmO3r_version, "intrinsic parameters": intrinsic, "configuration": dumps(params)}
        meta = {"ifmO3r_version": ifmO3r_version,
                "intrinsic parameters": intrinsic, "configuration": dumps(params)}
        meta_json = dumps(meta)
        status_logger.info("meta information: {}".format(meta_json))

        try:
            # get data
            with _H5Writer(filename=filename, write_index=write_index, streams=streams, formats=["hdf5-compound",],
                           num_sensors=num_sensors, meta=meta_json, desc=desc) as f:
                # set to stream on
                self.frameGrabber.stream_on(image_buffer=self.imageBuffer, timeout=DEFAULT_TIMEOUT)

                c = 0
                while True:
                    if c > amount:
                        # turn streaming off
                        self.frameGrabber.stream_on(image_buffer=self.imageBuffer, timeout=5)
                        return amount

                    if self.imageBuffer.__next__():
                        amp = self.imageBuffer.amplitude_image()
                        conf = self.imageBuffer.confidence_image()
                        xyz = self.imageBuffer.xyz_image()
                        dist = self.imageBuffer.distance_image()
                        dist_noise = self.imageBuffer.distance_noise_image()

                        current_data = {'amplitude': amp, 'cloud': xyz, 'confidence': conf, 'distance': dist,
                                        'distance_noise': dist_noise}
                        status_logger.debug("data written to file: {}".format(current_data.keys()))
                        for k in current_data.keys():
                            status_logger.debug("data written key, size: {}, {}".format(k, current_data[k].shape))

                        # append the data
                        f.append_data(streams[0], current_data, time.perf_counter() * 1000000)
                        c += 1

        except IOError as e:
            status_logger.error(e)
            pass


def main():
    from ifmO3r.ifm3dTiny.device import Device

    # build a FrameGrabber and ImageBuffer and Device
    cam1 = Device("192.168.0.69", 50012)
    fg = FrameGrabber(cam1)
    im = ImageBuffer()

    # specify a data dir
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        Path(os.path.join(dir_path, 'data')).mkdir(parents=True, exist_ok=True)
        data_path = os.path.join(dir_path, 'data')
    except IOError as arg:
        print('The data dir can not be accessed or written to: ' + arg)
        pass
    else:
        data_path = dir_path

    # get a ImgLogger objet with the specified frame and data dir
    img_logger = ImageLogger(device=cam1, frameGrabber=fg, imageBuffer=im, path=data_path)

    # EXAMPLE usage of the two streaming functions
    img_logger.save_data_stream(streams=['o3r',], num_sensors=1, write_index=True, numSeconds=5, desc="example data set")
    # img_logger.save_algo_debug_data(cameraID=[2,3], numSeconds=10)


#%%
if __name__ == "__main__":
    main()
