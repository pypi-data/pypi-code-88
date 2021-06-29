# -*- coding: utf-8 -*-
"""
This file will receive and parse can-msg from can-bus with PeakCan(current only support).

In current huichuang project, the dbc protocal show below(default_huichuang_dbc.json).
TR      CAN-ID      Name                    Physical Implication
----------------------------------------------------------------------------------------
R       0x6F8       warning_id              the status of current feature 
R       0x6FA       version_id              the version of current software
R       0x500       detections_mem_id       the frame id and timestamp of detections-mem
R       0x501       detections_mem_data     the data of detections-mem 
"""

# @File  : can_process.py
# @Author: Andy.yang lan.zhang
# @Date  : 2021/02/22
# @Software: VS Code

import time
from queue import Queue

from json import load, dump
from os import mkdir
from os.path import dirname, realpath, join, exists

from can.interface import Bus
from can import CSVWriter, Printer
import pandas as pd
from pandas.api.types import is_numeric_dtype
from scipy.io import savemat

# peak can setting
try:
    peakcan_bus = Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=500000)
except:
    print("The Peak-CAN is not connected")

is_stop = True
start_push_queue_det_mem = False

detection_mem_queue = Queue(maxsize=500)

def _fillZero(bit_str):
    num_fill_zero = 8 - len(bit_str)
    if num_fill_zero == 0:
        return bit_str
    elif num_fill_zero == 1:
        return f"0{bit_str}"
    elif num_fill_zero == 2:
        return f"00{bit_str}"
    elif num_fill_zero == 3:
        return f"000{bit_str}"
    elif num_fill_zero == 4:
        return f"0000{bit_str}"
    elif num_fill_zero == 5:
        return f"00000{bit_str}"
    elif num_fill_zero == 6:
        return f"000000{bit_str}"
    elif num_fill_zero == 7:
        return f"0000000{bit_str}"
    else:
        print("Error: fill zero in _fillZeon of can_process.py")
        return f"error"


def _convHexToBits(hex_data):
    bin_0_str = _fillZero(bin(hex_data[0])[2:])
    bin_1_str = _fillZero(bin(hex_data[1])[2:])
    bin_2_str = _fillZero(bin(hex_data[2])[2:])
    bin_3_str = _fillZero(bin(hex_data[3])[2:])
    bin_4_str = _fillZero(bin(hex_data[4])[2:])
    bin_5_str = _fillZero(bin(hex_data[5])[2:])
    bin_6_str = _fillZero(bin(hex_data[6])[2:])
    bin_7_str = _fillZero(bin(hex_data[7])[2:])
    bin_str = f"{bin_0_str}{bin_1_str}{bin_2_str}{bin_3_str}{bin_4_str}{bin_5_str}{bin_6_str}{bin_7_str}"

    return bin_str


def _convBinToDec(dec_p):
    out = 0
    for index, value in enumerate(dec_p):
        if value == '1':
            out=out+2**(-index-1)
    return out

def _convBinToFloat32(bit_str):
    f_sign = bit_str[0]
    f_e = bit_str[1:9]
    f_dec = bit_str[9:]

    if f_e =='00000000':
        # M = f"0.{f_dec}"
        int_part = '0'
        dec_part = f_dec
    elif f_e =='11111111':
        if f_dec=='00000000000000000000000':
            return float('nan')
        elif f_sign == '0':
            return float('inf')
        elif f_sign == '1':
            return float('-inf')
        else:
            print("Error in function: _convBitsToFloat32")
            return None
    else:  
        E = int(f_e, 2)-127
        
        if E == 0:
            # M = f"1.{f_dec}"
            int_part = '1'
            dec_part = f_dec
        elif E > 0:
            # M = f"1{f_dec[0:E]}.{f_dec[E:]}"
            int_part = f"1{f_dec[0:E]}"
            dec_part = f_dec[E:]
        elif E < 0:
            abs_E = -E
            if abs_E ==1:
                # M = f"0.1{f_dec}"
                int_part = '0'
                dec_part = f"1{f_dec}"
            else:
                fill_zeor = (abs_E-1)*'0'
                # M = f"0.{fill_zeor}1{f_dec}"
                int_part = '0'
                dec_part = f'{fill_zeor}1{f_dec}'
        else:
            print("Error in calcuate the binary num of float in function: _convBinToFloat32")
        
    real_part_out = int(int_part, 2)
    dec_part_out = _convBinToDec(dec_part)
    
    if f_sign == '0':
        sign_out = 1
    elif f_sign == '1':
        sign_out = -1
    else:
        print("Error in Sign of function: _convBinToFloat32")
    
    return sign_out*(real_part_out + dec_part_out)


def _parseMsg(dbc_name, msg):
    msg_ts = msg.timestamp
    msg_id = hex(msg.arbitration_id)
    msg_data = msg.data

    msg_bits = _convHexToBits(msg_data)

    DIR_PATH = dirname(dirname(realpath(__file__)))
    if dbc_name == 'huichuang':
        hc_dbc_path = join(DIR_PATH, "config", "default_huichuang_dbc.json")
        with open(hc_dbc_path, 'r') as f:
            hc_dbc = load(f)
            """
            timeArray = time.localtime(msg_ts)
            dt_new = time.strftime('%Y-%m-%d %H:%M:%S.%f')
            print(dt)
            """

            if msg_id == "0x6f8":
                start = hc_dbc["0x6f8"]["warn_mode"]["start"]
                stop = hc_dbc["0x6f8"]["warn_mode"]["stop"]
                fc = hc_dbc["0x6f8"]["warn_mode"]["factor"]
                ofs = hc_dbc["0x6f8"]["warn_mode"]["offset"]
                warn_mode = int(msg_bits[start:stop], 2) * fc + ofs

                start = hc_dbc["0x6f8"]["bsd_right"]["start"]
                stop = hc_dbc["0x6f8"]["bsd_right"]["stop"]
                fc = hc_dbc["0x6f8"]["bsd_right"]["factor"]
                ofs = hc_dbc["0x6f8"]["bsd_right"]["offset"]
                rbsd = int(msg_bits[start:stop], 2) * fc + ofs

                start = hc_dbc["0x6f8"]["bsd_left"]["start"]
                stop = hc_dbc["0x6f8"]["bsd_left"]["stop"]
                fc = hc_dbc["0x6f8"]["bsd_left"]["factor"]
                ofs = hc_dbc["0x6f8"]["bsd_left"]["offset"]
                lbsd = int(msg_bits[start:stop], 2) * fc + ofs

                return ["ff", msg_ts, warn_mode, rbsd, lbsd]
            elif msg_id == "0x6fa":
                start = hc_dbc["0x6fa"]["major_ver_id"]["start"]
                stop = hc_dbc["0x6fa"]["major_ver_id"]["stop"]
                fc = hc_dbc["0x6fa"]["major_ver_id"]["factor"]
                ofs = hc_dbc["0x6fa"]["major_ver_id"]["offset"]
                maj_ver = int(msg_bits[start:stop], 2) * fc + ofs

                start = hc_dbc["0x6fa"]["minor_ver_id"]["start"]
                stop = hc_dbc["0x6fa"]["minor_ver_id"]["stop"]
                fc = hc_dbc["0x6fa"]["minor_ver_id"]["factor"]
                ofs = hc_dbc["0x6fa"]["minor_ver_id"]["offset"]
                min_ver = int(msg_bits[start:stop], 2) * fc + ofs

                start = hc_dbc["0x6fa"]["stage_ver_id"]["start"]
                stop = hc_dbc["0x6fa"]["stage_ver_id"]["stop"]
                fc = hc_dbc["0x6fa"]["stage_ver_id"]["factor"]
                ofs = hc_dbc["0x6fa"]["stage_ver_id"]["offset"]
                stg_ver = int(msg_bits[start:stop], 2) * fc + ofs

                return ["sw-ver", msg_ts, maj_ver, min_ver, stg_ver]
            elif msg_id == "0x500":
                start = hc_dbc["0x500"]["frame_id"]["start"]
                stop = hc_dbc["0x500"]["frame_id"]["stop"]
                fc = hc_dbc["0x500"]["frame_id"]["factor"]
                ofs = hc_dbc["0x500"]["frame_id"]["offset"]
                # change low-endian to big-endian
                low_endian_bits = msg_bits[start:stop]
                big_endian_bits = f"{low_endian_bits[24:32]}{low_endian_bits[16:24]}{low_endian_bits[8:16]}{low_endian_bits[0:8]}"
                frame_id = int(big_endian_bits, 2) * fc + ofs

                start = hc_dbc["0x500"]["frame_ts"]["start"]
                stop = hc_dbc["0x500"]["frame_ts"]["stop"]
                fc = hc_dbc["0x500"]["frame_ts"]["factor"]
                ofs = hc_dbc["0x500"]["frame_ts"]["offset"]
                # change low-endian to big-endian
                low_endian_bits = msg_bits[start:stop]
                big_endian_bits = f"{low_endian_bits[24:32]}{low_endian_bits[16:24]}{low_endian_bits[8:16]}{low_endian_bits[0:8]}"

                frame_ts = int(big_endian_bits, 2) * fc + ofs

                return ["detection-mem-id-ts", msg_ts, frame_id, frame_ts]
            elif msg_id == "0x501": # range(m) and doppler_vel(km/h)
                msg_bins_rng = msg_bits[0:32]
                msg_rng = _convBinToFloat32(msg_bins_rng)

                msg_bins_vel = msg_bits[32:]
                msg_vel = _convBinToFloat32(msg_bins_vel)

                return ["detection-rng-vel", msg_ts, msg_rng, msg_vel]
                """
                start = hc_dbc["0x501"]["range"]["start"]
                stop = hc_dbc["0x501"]["range"]["stop"]
                fc = hc_dbc["0x501"]["range"]["factor"]
                ofs = hc_dbc["0x501"]["range"]["offset"]
                # change low-endian to big-endian
                low_endian_bits = msg_bits[start:stop]
                big_endian_bits = f"{low_endian_bits[8:16]}{low_endian_bits[0:8]}"
                rng = int(big_endian_bits, 2) / fc + ofs

                start = hc_dbc["0x501"]["doppler_vel"]["start"]
                stop = hc_dbc["0x501"]["doppler_vel"]["stop"]
                fc = hc_dbc["0x501"]["doppler_vel"]["factor"]
                ofs = hc_dbc["0x501"]["doppler_vel"]["offset"]
                # change low-endian to big-endian
                low_endian_bits = msg_bits[start:stop]
                big_endian_bits = f"{low_endian_bits[8:16]}{low_endian_bits[0:8]}"
                doppler_vel = int(big_endian_bits, 2) / fc + ofs

                start = hc_dbc["0x501"]["angle"]["start"]
                stop = hc_dbc["0x501"]["angle"]["stop"]
                fc = hc_dbc["0x501"]["angle"]["factor"]
                ofs = hc_dbc["0x501"]["angle"]["offset"]
                # change low-endian to big-endian
                low_endian_bits = msg_bits[start:stop]
                big_endian_bits = f"{low_endian_bits[8:16]}{low_endian_bits[0:8]}"
                angle = int(big_endian_bits, 2) / fc + ofs

                start = hc_dbc["0x501"]["snr"]["start"]
                stop = hc_dbc["0x501"]["snr"]["stop"]
                fc = hc_dbc["0x501"]["snr"]["factor"]
                ofs = hc_dbc["0x501"]["snr"]["offset"]
                # change low-endian to big-endian
                low_endian_bits = msg_bits[start:stop]
                big_endian_bits = f"{low_endian_bits[8:16]}{low_endian_bits[0:8]}"
                snr = int(big_endian_bits, 2) / fc + ofs

                return [
                    "detection-mem-data", msg_ts, rng, doppler_vel, angle, snr
                ]
                """
            elif msg_id == '0x502': # angle(deg) and snr(dB)
                msg_bins_ang = msg_bits[0:32]
                msg_ang = _convBinToFloat32(msg_bins_ang)
                # print(f"Angle: {msg_data.hex()[0:8]}, {msg_bins_ang}, {msg_ang}")

                msg_bins_snr = msg_bits[32:]
                msg_snr = _convBinToFloat32(msg_bins_snr)
                # print(f"snr: {msg_data.hex()[8:]}, {msg_bins_snr}, {msg_snr}")

                return ["detection-ang-snr", msg_ts, msg_ang, msg_snr]


def checkConnectStatusOfPeakCAN():
    return peakcan_bus.status_is_ok()

def startPushDetMem(st):
    global start_push_queue_det_mem
    start_push_queue_det_mem = st

def switchStop(st_stop):
    global is_stop
    is_stop = st_stop


def writeCanMsg():
    global is_stop
    data_js = {
        "ff": {
            "ts": [],
            "warning_mode": [],
            "bsd_left_level": [],
            "bsd_right_level": []
        },
        "sw-ver": {
            "ts": [],
            "major": [],
            "minor": [],
            "stage": []
        },
        "det-mem-id-ts": {
            'ts': [],
            'frame-id': [],
            'frame-ts': [],
        },
        'det-mem-data': {
            'ts': [],
            'range': [],
            'doppler-vel': [],
            'angle': [],
            'snr': []
        }
    }

    st_is_frame_id_aligned = False
    for msg in peakcan_bus:
        physical_data = _parseMsg('huichuang', msg)

        if physical_data[0] == "ff":
            data_js['ff']['ts'].append(physical_data[1])
            data_js['ff']['warning_mode'].append(physical_data[2])
            data_js['ff']['bsd_left_level'].append(physical_data[3])
            data_js['ff']['bsd_right_level'].append(physical_data[4])
        elif physical_data[0] == "sw-ver":
            data_js['sw-ver']['ts'].append(physical_data[1])
            data_js['sw-ver']['major'].append(physical_data[2])
            data_js['sw-ver']['minor'].append(physical_data[3])
            data_js['sw-ver']['stage'].append(physical_data[4])
        elif physical_data[0] == 'detection-mem-id-ts':
            if not st_is_frame_id_aligned:
                st_is_frame_id_aligned = True
            data_js['det-mem-id-ts']['ts'].append(physical_data[1])
            data_js['det-mem-id-ts']['frame-id'].append(physical_data[2])
            data_js['det-mem-id-ts']['frame-ts'].append(physical_data[3])
        elif physical_data[
                0] == 'detection-mem-data' and st_is_frame_id_aligned:
            data_js['det-mem-data']['ts'].append(physical_data[1])
            data_js['det-mem-data']['range'].append(physical_data[2])
            data_js['det-mem-data']['doppler-vel'].append(physical_data[3])
            data_js['det-mem-data']['angle'].append(physical_data[4])
            data_js['det-mem-data']['snr'].append(physical_data[5])

        if is_stop:
            DIR_PATH = "C:\data_records"
            if not exists(DIR_PATH):
                mkdir(DIR_PATH)
            # DIR_PATH = dirname(dirname(realpath(__file__)))
            cur_time = time.strftime("%Y-%m-%d %Hh-%Mm-%Ss",
                                     time.localtime(time.time()))
            # data_store_path = join(DIR_PATH, "data", f"{cur_time}.json")
            data_store_path = join(DIR_PATH, f"{cur_time}.json")
            with open(data_store_path, 'w') as f:
                dump(data_js, f)

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
            break


def readCanMsg():
    global is_stop
    global detection_mem_queue

    data_js = {
            'id': [],
            'range': [],
            'doppler-vel': [],
            'angle': [],
            'snr': []
    }

    # the data in cur_detection_mem_info will be:frame-id, range, doppler-vel, angle, snr, range, doppler-vel, angle, snr, range,...
    cur_detection_mem_info = []
    st_is_frame_id_aligned = False

    for msg in peakcan_bus:
        physical_data = _parseMsg('huichuang', msg)

        # print(physical_data)
        if start_push_queue_det_mem:
            if physical_data[0] == 'detection-mem-id-ts':
                if not st_is_frame_id_aligned:
                    st_is_frame_id_aligned = True
                if len(cur_detection_mem_info) != 0:
                    if not detection_mem_queue.full():
                        detection_mem_queue.put(cur_detection_mem_info)
                    else:
                        print("Error: Detection-Mem-Queue is Full")
                        raise IOError(
                            "Detection-Mem-Queue is full in function of can_process!"
                        )
                cur_detection_mem_info = []
                cur_detection_mem_info.append(physical_data[2])
                # print('id')
                if not is_stop:
                    data_js['id'].append(physical_data[2])
            elif st_is_frame_id_aligned:
                if physical_data[0] == 'detection-rng-vel':
                    cur_detection_mem_info.append((physical_data[2], physical_data[3]))
                    # print('rng-vel')
                    if not is_stop:
                        data_js['range'].append(physical_data[2])
                        data_js['doppler-vel'].append(physical_data[3])
                elif physical_data[0] == 'detection-ang-snr':
                    cur_detection_mem_info.append((physical_data[2], physical_data[3]))
                    # print('ang-snr')
                    if not is_stop:
                        data_js['angle'].append(physical_data[2])
                        data_js['snr'].append(physical_data[3])
        """
        if is_stop and len(data_js['id'])!=0:
            DIR_PATH = "C:\data_records"
            if not exists(DIR_PATH):
                mkdir(DIR_PATH)
            # DIR_PATH = dirname(dirname(realpath(__file__)))
            cur_time = time.strftime("%Y-%m-%d %Hh-%Mm-%Ss",
                                     time.localtime(time.time()))
            # data_store_path = join(DIR_PATH, "data", f"{cur_time}.json")
            data_store_path = join(DIR_PATH, f"{cur_time}.json")
            with open(data_store_path, 'w') as f:
                dump(data_js, f)

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

            data_js = {
            'id': [],
            'range': [],
            'doppler-vel': [],
            'angle': [],
            'snr': []
            }
        """

def printOneCanMsg():
    msg = peakcan_bus.recv()
    cmd_listener = Printer()
    cmd_listener.on_message_received(msg)
    _parseMsg('huichuang', msg)
    cmd_listener.stop()


def filterCanID():
    peakcan_bus.set_filters([
        # receive warning-message
        {
            "can_id": 0x6F8,
            "can_mask": 0xFFFFFFFF,
            "extended": False
        },
        # receive deftech sw version id message
        {
            "can_id": 0x6FA,
            "can_mask": 0xFFFFFFFF,
            "extended": False
        },
        # receive detections-mem-id-timestamp message
        {
            "can_id": 0x500,
            "can_mask": 0xFFFFFFFF,
            "extended": False
        },
        # receive detections-range-vel message
        {
            "can_id": 0x501,
            "can_mask": 0xFFFFFFFF,
            "extended": False
        },
        # receive detections-angle-snr message
        {
            "can_id": 0x502,
            "can_mask": 0xFFFFFFFF,
            "extended": False
        },
    ])
