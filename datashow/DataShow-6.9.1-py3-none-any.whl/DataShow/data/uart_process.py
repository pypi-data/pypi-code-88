# -*- coding: utf-8 -*-
"""
requirements: pip install pyserial

"""

import time
from json import load, dump
from os import mkdir
from os.path import dirname, realpath, join, exists
import copy
from scipy.io import savemat

import serial
from serial.tools import list_ports


class RadarPort():
    def __init__(self, bps=231200, parity='N', stopbits=1, timeout=2.0):
        self.bps = bps
        self.parity = parity
        self.stopbits = stopbits
        self.timeout = timeout

        # store the read data
        self.read_data = ""
        # read the uart symbol bit
        self.st_store_msg = False
        # define a bool para to align frame
        # self.st_new_frame = False
        # define a dict to store cur data of frame
        self.cur_frame_data_js = {}
        # define a bool para to set bk
        self.st_bk = False
        # define a bool para to set ak
        self.st_ak = False
        # define a mem to store parsed msg
        self.msg_mem = []
        # define a para to filter
        self.st_filter = False
        self.filter_threshold_range = 4

        self.openUart()

    def setFilter(self, st):
        self.st_filter = st

    def openUart(self):
        port_list = list(list_ports.comports())
        if len(port_list) == 0:
            raise Exception("Error: no uart-com port is connected!")
        else:
            for port in port_list:
                print(f"PortID: {port[0]}  PortName: {port[1]}")
            try:
                self.radar_port = serial.Serial(port=port[0],
                                                baudrate=self.bps,
                                                stopbits=self.stopbits,
                                                timeout=self.timeout)
            except Exception as e:
                print(f"Error: open usrt fail: {e}")

            if not self.radar_port.isOpen():
                print("The status of port is not open!")
            else:
                print("Open Uart success!")
                time.sleep(0.1)
                self.radar_port.reset_input_buffer()

    def showStatus(self):
        return self.radar_port.isOpen()

    def closeUart(self):
        self.st_store_msg = False
        self.radar_port.close()

    def writeFrameToUart(self, num):
        self.radar_port.write(f"scan start {num}\n".encode("ascii"))
        self.radar_port.flush()

    def getMsg(self):
        line = self.radar_port.readline().decode("ascii")

        # parse cur-line
        split_line = line.split()
        # print(split_line)
        if len(split_line) != 0:
            if split_line[0] == "FT":
                # self.st_new_frame = True
                self.cur_frame_data_js = {}
                
                frame_interval = split_line[2]
                frame_type = split_line[4]
                self.cur_frame_data_js["frame_interval"] = frame_interval
                self.cur_frame_data_js["frame_type"] = frame_type
                self.cur_frame_data_js["det_bk"] = []
                self.cur_frame_data_js["det_ak"] = []
                # print(f"frame-int:{frame_interval}")
                # print(f"frame-type:{frame_type}")
            elif split_line[0] == "---":
                # self.st_new_frame = False

                frame_id = split_line[2]
                tmp = split_line[4].split("/")
                cdi_number = tmp[0]
                track_output_number = tmp[1]
                raw_number = tmp[2][:-1]
                self.cur_frame_data_js["frame_id"] = frame_id
                self.cur_frame_data_js["cdi_number"] = cdi_number
                self.cur_frame_data_js[
                    "track_output_number"] = track_output_number
                self.cur_frame_data_js["raw_number"] = raw_number

                # print(f"frame-id:{frame_id}")
                #print(f"cdi-num:{cdi_number}")
                #print(f"out-{track_output_number}")
                #print(f"raw-num:{raw_number}")
            elif split_line[0] == "BK":
                # self.st_new_frame = False

                self.st_bk = True
                self.st_ak = False
            elif split_line[0] == "AK":
                self.st_new_frame = False

                self.st_bk = False
                self.st_ak = True
            elif split_line[0][:-1].isdecimal():
                # self.st_new_frame = False
                cur_data = split_line
                num_data = len(cur_data)
                # print(cur_data)
                cur_det_rng_m = float(cur_data[4][:-1])
                if self.st_filter and cur_det_rng_m<self.filter_threshold_range:
                    if num_data > 12 and self.st_ak:
                        # det-id, snr, range, vel, ang, track_level, 0.0, 0
                        self.cur_frame_data_js["det_ak"].append(
                            (cur_data[0][:-1], cur_data[2][:-1], cur_data[4][:-1], cur_data[6][:-1],
                             cur_data[8][:-1], cur_data[10][:-1]))
                    elif num_data == 11 and self.st_bk:
                        self.cur_frame_data_js["det_bk"].append(
                            (cur_data[0][:-1], cur_data[2][:-1], cur_data[4][:-1], cur_data[6][:-1],
                             cur_data[8][:-1],  cur_data[10][:-1]))
                else:
                    if num_data > 12 and self.st_ak:
                        # det-id, snr, range, vel, ang, track_level, 0.0, 0
                        self.cur_frame_data_js["det_ak"].append(
                            (cur_data[0][:-1], cur_data[2][:-1], cur_data[4][:-1], cur_data[6][:-1],
                             cur_data[8][:-1], cur_data[10][:-1]))
                    elif num_data == 11 and self.st_bk:
                        self.cur_frame_data_js["det_bk"].append(
                            (cur_data[0][:-1], cur_data[2][:-1], cur_data[4][:-1], cur_data[6][:-1],
                             cur_data[8][:-1],  cur_data[10][:-1]))
                # print(f"data-{cur_data}")
            elif split_line[0]=="#":
                if self.st_store_msg:
                    self.msg_mem.append(self.cur_frame_data_js)
                return self.cur_frame_data_js
            else:
                # print(split_line)
                pass

            return None
        else:
            return None

    def getData(self):
        return self.read_data

    def startStoreMsg(self):
        self.st_store_msg = True
        self.msg_mem = []

    def stopStoreMsg(self):
        self.st_store_msg = False

        DIR_PATH = "C:\\data_records"
        if not exists(DIR_PATH):
            mkdir(DIR_PATH)
        # DIR_PATH = dirname(dirname(realpath(__file__)))
        cur_time = time.strftime("%Y-%m-%d %Hh-%Mm-%Ss",
                                 time.localtime(time.time()))
        # data_store_path = join(DIR_PATH, "data", f"{cur_time}.json")
        data_store_path = join(DIR_PATH, f"{cur_time}.json")
        with open(data_store_path, 'w') as f:
            dump(self.msg_mem, f)
        """
        # write mat file
        mat_dict = {
            "frame_id": data_js['det-mem-id-ts']['frame-id'],
            "range": data_js['det-mem-data']['range'],
            "doppler_vel": data_js['det-mem-data']['doppler-vel'],
            "angle": data_js['det-mem-data']['angle'],
            "snr": data_js['det-mem-data']['snr']
        }
        # mat_path = join(DIR_PATH, "data", f"{cur_time}.mat")
        mat_path = join(DIR_PATH, f"{cur_time}.mat")
        savemat(mat_path, mat_dict)
        """
