# -*- coding: utf-8 -*-

from ctypes import c_uint8, c_uint16, c_uint32, c_int16, c_float, Structure
from struct import pack, unpack
from os.path import getsize
from sys import argv
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import re, os
import datetime as dt
from datetime import timezone
import numpy as np
import csv
from spacepy.time import Ticktock
from spacepy.coordinates import Coords
from scipy import interpolate
import pytz
import shutil as sh

###############################################################################
#CuPID House Style

plt.rcParams['axes.grid'] = True
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Verdana']
red = '#CA054D'
blue = '#0091AD'
green = '#9CE7C8'
black = '#003049'
colormap = 'inferno'
filepath = os.getenv('DROPBOXBU')

###############################################################################
# X-RAY XRBR (X-Ray Burst) and XRFS (X-Ray Fast)
class xrbr_pkt(Structure):
    _fields_ = [('sync', c_uint32), ('time', c_uint32),
                ('channels', c_uint16 * 4)]

    def __init__(self, unpacked):
        self.sync = unpacked[0]
        self.time = unpacked[1]
        self.channels = unpacked[2:6]

ADC_Vrange = 4.5
VperC = ADC_Vrange/65536.
lo_thold = 30583.
hi_thold = 48060.
offset = 14563.
# t_cut is the limit between a science TLM packet that is not commanded, and one
# that is commanded. 1073741824 in bit form is 01000000000000000000000000000000,
# and the 1 is in the 31st spot, which makes the 1 a commanded event marker in
# the science TLM packet in bit 14 (see above). HK data would have a 1 in the
# 32nd spot, which would make the number larger than this.
t_cut = 1073741824
# XRBR packet unpacking pattern/format
# > = Big Endian
# I = Unsigned Int = Sync
# I = Unsigned Int = Time
# 4H = Unsigned Short = 4 Channels
# XRBR packet unpacking pattern/format
xrbr_unpack = '>II4H'
payld_tlm_time_t = c_uint32

class xrfs_pkt(Structure):
    _fields_ = [('sync', c_uint16), ('time', c_uint32),
                ('x', c_uint16), ('y', c_uint16)]

    def __init__(self, unpacked):
        self.sync, self.time, self.x, self.y = unpacked
# XRFS packet unpacking pattern/format
xrfs_unpack = '<HIHH'

###############################################################################
# CXDH (Combined Data and Housekeeping)
class cxdh_pkt(Structure):
    _fields_ = [('sync', c_uint32),
    ('time_payld', payld_tlm_time_t),
    ('time_adacs', c_uint32),
    ('xrbr_log_no', c_uint16),
    ('xrfs_log_no', c_uint16),
    ('dsfs_log_no', c_uint8),
    ('hkhi_log_no', c_uint8),
    ('thermistors', c_uint8 * 14),
    ('v_batt', c_uint16),
    ('v_spnl', c_uint16),
    ('i_batt', c_uint16),
    ('i_spnl', c_uint16),
    ('i_epssw1', c_uint16),
    ('i_epssw2', c_uint16),
    ('angle_to_go', c_uint16),
    ('n_xray_cull_thresh', c_uint16),
    ('mags_log_no', c_uint16),
    ('p_x', c_float),
    ('p_y', c_float),
    ('p_z', c_float),
    ('Bfield_meas1', c_int16),
    ('Bfield_meas2', c_int16),
    ('Bfield_meas3', c_int16),
    ('Qbi', c_float * 4),
    ('counts_xray', c_uint16 * 6),
    ('dosa_low', c_uint8 * 6),
    ('dosa_med', c_uint8 * 6),
    ('dosb_low', c_uint8 * 6),
    ('dosb_med', c_uint8 * 6)]

    def __init__(self,unpacked):
        (self.sync, #4
        self.time_payld, #4
        self.time_adacs, #4
        self.xrbr_log_no, #2
        self.xrfs_log_no, #2
        self.dsfs_log_no, #1
        self.hkhi_log_no #1
        ) = unpacked[0:7]
        self.thermistors = unpacked[7:21]
        (self.v_batt, #2
        self.v_spnl, #2
        self.i_batt, #2
        self.i_spnl, #2
        self.i_epssw1, #2
        self.i_epssw2, #2
        self.angle_to_go, #2
        self.n_xray_cull_thresh, #2
        self.mags_log_no, #2
        self.p_x, #4
        self.p_y, #4
        self.p_z, #4
        self.Bfield_meas1, #2
        self.Bfield_meas2, #2
        self.Bfield_meas3, #2
        ) = unpacked[21:36]
        self.Qbi = unpacked[36:40]
        self.counts_xray = unpacked[40:46]
        self.dosa_low = unpacked[46:52]
        self.dosa_med = unpacked[52:58]
        self.dosb_low = unpacked[58:64]
        self.dosb_med = unpacked[64:70]

#cxdh_unpack = 'IIIHHBB14BHHHHHHHHHfffhhhffff6H6B6B6B6B'
cxdh_unpack = '='
cxdh_unpack += '3I' #sync, time, time
cxdh_unpack += 'HHBB' #file numbers
cxdh_unpack += '14b' #thermistors
cxdh_unpack += '6H' # V, I
cxdh_unpack += '3H' # BU flags
cxdh_unpack += '3f' # Position (ECEF)
cxdh_unpack += '3H' # Bfield
cxdh_unpack += '4f' # quaternion
cxdh_unpack += '6H' # Xray counts
cxdh_unpack += '24B' # dosimetry

###############################################################################
# Dosimeter DSFS (Dosimeter Fast)
class dsfs_pkt(Structure):
    _fields_ = [('sync', c_uint32), ('pkt_count', c_uint16),
                ('model_serial', c_uint8), ('status', c_uint8),
                ('t_mon', c_uint8), ('bias_mon', c_uint8),
                ('five_mon', c_uint8), ('three_mon', c_uint8),
                ('dosa_med', c_uint8), ('dosb_med', c_uint8),
                ('dosa_low', c_uint8 * 10), ('dosb_low', c_uint8 * 10),
                ('reserved', c_uint8), ('crc', c_uint8)]

    def __init__(self, unpacked):
        (self.sync, self.pkt_count, self.model_serial, self.status, self.t_mon,
         self.bias_mon, self.five_mon, self.three_mon, self.dosa_med,
         self.dosb_med) = unpacked[0:10]
        self.dosa_low = unpacked[10:20]
        self.dosb_low = unpacked[20:30]
        self.reserved, self.crc = unpacked[30:]

dsfs_unpack = '>IHBBBBBBBB10B10BBB'

###############################################################################
# Magnetometer MAGS (Magnetometer Science)

class mags_pkt(Structure):
    _fields_ = [('sync', c_uint32), ('time_payld', payld_tlm_time_t),
                ('Bx', c_uint16 * 12), ('By', c_uint16 * 12),
                ('Bz', c_uint16 * 12)]

    def __init__(self, unpacked):
        self.sync = unpacked[0]
        self.time = unpacked[1]
        self.bx = unpacked[2:14]
        self.by = unpacked[14:26]
        self.bz = unpacked[26:38]

mags_unpack = 'II36h'

###############################################################################
# SSOH (Stored State of Health)
class ssoh_hdr(Structure):
    _fields_ = [('sync', c_uint16), ('seq_num', c_uint8), ('send_id', c_uint8),
                ('tm_secs', c_uint32), ('tm_msecs', c_uint16),
                ('len', c_uint16), ('rec_id', c_uint8)]

    def __init__(self, unpacked):
        (self.sync, self.seq_num, self.send_id, self.tm_secs, self.tm_msecs,
         self.len, self.rec_id) = unpacked

soh_unpack = '<HBBIHHB'

###############################################################################
# CHST (Channels History)
class chst_hdr(Structure):
    _fields_ = [('sync', c_uint16), ('tm_secs', c_uint32),
                ('tm_msecs', c_uint16), ('seq_num', c_uint8),
                ('sndr_id', c_uint8), ('rcvr_id', c_uint8),
                ('recd_id', c_uint8), ('len', c_uint16)]

    def __init__(self, unpacked):
        (self.sync, self.tm_secs, self.tm_msecs, self.seq_num, self.sndr_id,
         self.rcvr_id, self.recd_id, self.len) = unpacked

chst_unpack = '<HIHBBBBH'
###############################################################################
# X-RAY XRBR (X-Ray Burst) and XRFS (X-Ray Fast) READ
def read_xrbr_sci(filename, varname = []):
    """
    Function to read science data out of XRBR file into numpy array.

    ### Parameters
    * filename : str
        >Name of logfile to read
    * varname : float array-like, optional
        >XRBR sci array to append data into. Default empty.

    ### Returns
    * staging : float array-like
        >Array of XRBR sci data from logfile. Includes data from `varname`,
        if specified.
        
    """
    
    f = open(filename, 'rb')
    pkt_list = []
    contents = f.read()
    starts = [m.start() for m in re.finditer(b'\xfe\x6b', contents)]
    stops = starts[1:]
    stops.append(starts[-1]+16)
    for idx, s in enumerate(starts):
        stuff = unpack(xrbr_unpack, contents[s:s+16])
        data = xrbr_pkt(stuff)
        if (data.time < t_cut):
            pkt_list.append(data)
    f.close()
    npkts = len(pkt_list)
    staging = np.zeros([npkts,5])
    for i in range(npkts):
        pkt = pkt_list[i]
        staging[i,0] = pkt.time
        staging[i,1:5] = pkt.channels[:]
    if (len(varname) != 0):
        xrbr_sci_arr = np.concatenate((varname,staging),axis=0)
    else:
        xrbr_sci_arr = staging
    return xrbr_sci_arr

def read_xrbr_hk(filename, varname = []):
    """
    Function to read housekeeping data out of XRBR file into numpy array.

    ### Parameters
    
    * filename : str
        >Name of logfile to read
    *varname : float array-like, optional
        >XRBR HK array to append data into. Default empty.

    ### Returns
    
    * staging : float array-like
        >Array of XRBR HK data from logfile. Includes data from `varname`,
        if specified.
        
    """
    f = open(filename, 'rb')
    pkt_list = []
    contents = f.read()
    starts = [m.start() for m in re.finditer(b'\xfe\x6b', contents)]
    stops = starts[1:]
    stops.append(starts[-1]+16)
    for idx, s in enumerate(starts):
        stuff = unpack(xrbr_unpack, contents[s:s+16])
        data = xrbr_pkt(stuff)
        # 2147483648
        # This time demarkation is for HK packets from the xray that would have
        # a Telemetry Type of 1 in bit 31 of the 0-31 bit 4 byte Time Tag data
        # (bytes 4-7)
        if (data.time >= 2147483647):
            pkt_list.append(data)
    f.close()
    npkts = len(pkt_list)
    staging = np.zeros([npkts,8])
    for i in range(npkts):
        pkt = pkt_list[i]
        staging[i,0] = pkt.time
        Status = pkt.channels[0]
        StatusBit = "{0:016b}".format(Status)
        if (StatusBit[0] == '1'): #
            MCP_xHV = 1
            if (StatusBit[1] == '1'):
                MCP_xAuto = 1
            else:
                MCP_xAuto = 0
            HVData = int(StatusBit[4:],2)
            TempData = np.nan
        else:
            MCP_xHV = 0
            MCP_xAuto = np.nan
            HVData = np.nan
            TempData = int(StatusBit[4:],2)
        staging[i,1] = MCP_xHV
        staging[i,2] = MCP_xAuto
        staging[i,3] = HVData
        staging[i,4] = TempData
        staging[i,5:8] = pkt.channels[1:4]
    if (len(varname) != 0):
        xrbr_hk_arr = np.concatenate((varname,staging),axis=0)
    else:
        xrbr_hk_arr = staging
    return xrbr_hk_arr

def read_xrfs(filename, varname = []):
    """
    Function to read data out of XRFS file into numpy array.

    ### Parameters
    
    * filename : str
        >Name of logfile to read
    * varname : float array-like, optional
        > XRFS array to append data into. Default empty.

    ### Returns
    
    * xrfs_arr : float array-like
        >Array of XRFS data from logfile. Includes data from `varname`,
        if specified.
        
    """
    f = open(filename, 'rb')
    pkt_list = []
    contents = f.read()
    starts = [m.start() for m in re.finditer(b'\x51\xfa', contents)]
    stops = starts[1:]
    stops.append(getsize(filename) - starts[0])
    length = stops[0] - starts[0]
    for idx, s in enumerate(starts):
        stuff = unpack(xrfs_unpack, contents[s:s+length])
        data = xrfs_pkt(stuff)
        pkt_list.append(data)
    f.close()
    npkts = len(pkt_list)
    staging = np.zeros([npkts,3])
    for i in range(npkts):
        pkt = pkt_list[i]
        staging[i,0] = pkt.time
        staging[i,1] = pkt.x
        staging[i,2] = pkt.y
    if (len(varname) != 0):
        xrfs_arr = np.concatenate((varname,staging),axis=0)
    else:
        xrfs_arr = staging
    return xrfs_arr

def nonlin_correction(x,y,M_inv = np.array([[1.0275, -0.14678],[-0.13380, 1.0293]]),x_offset = 0.0006,y_offset = 0.0061):
    """
    Function to apply nonlinearity correction to MCP position x/y data (as found in XRFS).

    ### Parameters
    
    * x : float, array-like
        >MCP x position array
    * y : float, array-like
        >MCP y position array
    * M_inv : float, array-like, optional
        >Array defining new "skewed" basis to transform x/y into. Default `np.array([[1.0275, -0.14678],[-0.13380, 1.0293]])`.
    * x_offset : float, optional.
        >x channel offset due to center not being exactly 0,0. Default `0.0006`.
    * y_offset : float, optional.
        >y channel offset due to center not being exactly 0,0. Default `0.0061`.

    ### Returns
    
    * x,y : float array-like
        >Arrays of corrected x and y data.
        
    """
    x_shift = x - x_offset
    y_shift = y - y_offset
    x = (x_shift * M_inv[0,0] + y_shift * M_inv[0,1])
    y = (x_shift * M_inv[1,0] + y_shift * M_inv[1,1])
    return x,y

###############################################################################
# Dosimeter DSFS (Dosimeter Fast) READ

med_rollover = 254
low_rollover = 255

dosihdr = ''
dosihdr += 'sync,pkt_count,t_mon,bias_mon,five_mon,three_mon,dosa_med,dosb_med,'
dosihdr += 'dosa_low[0],dosa_low[1],dosa_low[2],dosa_low[3],dosa_low[4],'
dosihdr += 'dosa_low[5],dosa_low[6],dosa_low[7],dosa_low[8],dosa_low[9],'
dosihdr += 'dosb_low[0],dosb_low[1],dosb_low[2],dosb_low[3],dosb_low[4],'
dosihdr += 'dosb_low[5],dosb_low[6],dosb_low[7],dosb_low[8],dosb_low[9]'


def read_dsfs(filename, varname = []):
    """
    Function to read data out of DSFS file into numpy array.

    ### Parameters
    
    * filename : str
        >Name of logfile to read
    * varname : float array-like, optional
        >DSFS array to append data into. Default empty.

    ### Returns
    
    * dsfs_arr : float array-like
        >Array of DSFS data from logfile. Includes data from `varname`,
        if specified.
        
    """
    f = open(filename, 'rb')
    pkt_list = []
    contents = f.read()
    starts = [m.start() for m in re.finditer(b'\xfa\xf3\x34\x2b', contents)]
    stops = starts[1:]
    stops.append(starts[-1]+36)
    for idx, s in enumerate(starts):
        if (s + 36 < len(contents)):
            stuff = unpack(dsfs_unpack, contents[s:s+36])
            data = dsfs_pkt(stuff)
            pkt_list.append(data)
    f.close()
    npkts = len(pkt_list)
    staging = np.zeros([npkts,28])
    for i in range(npkts):
        pkt = pkt_list[i]
        staging[i,0:8] = [pkt.sync,pkt.pkt_count,pkt.t_mon,pkt.bias_mon,
                       pkt.five_mon,pkt.three_mon, pkt.dosa_med,pkt.dosb_med]
        staging[i,8:18] = pkt.dosa_low
        staging[i,18:28] = pkt.dosb_low
    if (len(varname) != 0):
        dsfs_arr = np.concatenate((varname,staging),axis=0)
    else:
        dsfs_arr = staging
    return dsfs_arr

def dsfs_ratecalc(data):
    """
    Function to calculate DSFS countrate.

    ### Parameters
    
    * data : float array-like
        >DSFS data to calculate countrate from.

    ### Returns
    
    * ResultData : float array-like
        >Countrate data with quality flags (slowroll error, discretization error, invisible rollover warning)
        
    """
    data = np.asarray(data)
    countrate_array = np.zeros((len(data), 10))

    # #Naive medium countrate calculation
    ######################
    delta_med = np.zeros(len(data))
    for i in range(len(data)):
        if (i == 0):
            delta_med[i] = data[i+1,0] - 0
        else:
            if (i == len(data)-1):
                delta_med[i] = np.nan
            else:
                delta_med[i] = data[i+1,0] - data[i,0]
        if (delta_med[i] < -1):
            delta_med[i] += med_rollover

    hold_lo = data[0,1]
    slowroll_check = False
    rec_counter = 0
    rec_delta_med = np.zeros(len(delta_med))
    roll_count = np.zeros(len(data))
    invis_roll_flag = np.zeros(len(data), dtype = bool)
    rect_med_flag = np.zeros(len(data), dtype = bool)
    slowroll_flag_array = np.zeros((len(data), 10), dtype = bool)
    lo_disc_flag_array = np.zeros((len(data), 10), dtype = bool)
    ######################

    # #First pass countrate calculation with flags for slowroll, discretization, and invisible roll errors
    ######################
    for i in range(len(data)):
        for j in range(10):
            lo = data[i, 1 + j]
            if (lo >= hold_lo):
                countrate_array[i,j] = (lo - hold_lo) / 1
                slowroll_check = False
            if ((lo < hold_lo) & (lo - hold_lo != -1)):
                if slowroll_check:
                    slowroll_flag_array[i,j] = True
                roll_count[i] += 1
                countrate_array[i, j] = (lo + low_rollover - hold_lo) / 1
                slowroll_check = True
            if (lo - hold_lo == -1):
                countrate_array[i,j] = 0
                lo_disc_flag_array[i,j] = True
            hold_lo = lo
        rec_delta_med[i] = delta_med[i]

        if (rec_counter > 0):
            # THIS CAN MISTAKE AN INVISIBLE ROLLOVER FOR AN UNBOUNCE
            if (delta_med[i] - (roll_count[i] - np.count_nonzero(slowroll_flag_array[i, :])) == 1):
                rec_counter -= 1
                rec_delta_med[i] = roll_count[i] - np.count_nonzero(slowroll_flag_array[i, :])

        if (delta_med[i] == -1):
            rec_counter += 1
            rec_delta_med[i] = 0
        #THIS IS NOT SENSITIVE TO WHEN INVISIBLE ROLLOVERS ARE NOT COUNTED DUE TO BOUNCE DOWN
        if ((roll_count[i] - np.count_nonzero(slowroll_flag_array[i, :])) - delta_med[i] >= 1):
            # #Make some kind of test in here to distinguish uncounted low rollover from bounce down???
            rec_counter += 1
            rec_delta_med[i] = roll_count[i] - np.count_nonzero(slowroll_flag_array[i, :])

        invis_roll_flag[i] = rec_delta_med[i] > (roll_count[i] - np.count_nonzero(slowroll_flag_array[i, :]))
        rect_med_flag[i] = not (rec_delta_med[i] == delta_med[i])

    #######################

    # #SLOWROLL ERROR PASS (Medium channel assumed correct)
    ####################
    for i in range(len(data)):
        for j in range(10):
            if slowroll_flag_array[i, j]:
                if (rec_delta_med[i] < roll_count[i]):
                    if (j == 0):
                        countrate_array[i, j] = (data[i, 1+j] + low_rollover - data[i-1, 9]) / 2
                        countrate_array[i-1, -1] = (data[i, 1+j] + low_rollover - data[i-1, 9]) / 2
                    else:
                        if (j == 1):
                            countrate_array[i, j] = (data[i, 1+j] + low_rollover - data[i-1, 10]) / 2
                            countrate_array[i, 0] = (data[i, 1+j] + low_rollover - data[i-1, 10]) / 2
                        else:
                            countrate_array[i, j] = (data[i, 1+j] + low_rollover - data[i, -1+j]) / 2
                            countrate_array[i, j-1] = (data[i, 1+j] + low_rollover - data[i, -1+j]) / 2
    ####################
    #print(countrate_array.shape)
    rect_med_flag = np.transpose(rect_med_flag).reshape((len(rect_med_flag), 1))
    invis_roll_flag = np.transpose(invis_roll_flag).reshape((len(invis_roll_flag), 1))
    #print(rect_med_flag.shape)
    #print(invis_roll_flag.shape)
    #print(slowroll_flag_array.shape)
    #print(lo_disc_flag_array.shape)

    ResultData = np.concatenate((countrate_array,rect_med_flag, invis_roll_flag, slowroll_flag_array, lo_disc_flag_array), axis = 1)
    return ResultData

def lin_dsfs(ratedata):
    """
    Function to make DSFS countrate array arranged in columns instead of DSFS packet-like.

    ### Parameters
    
    * ratedata : float array-like
        >DSFS countrate data as calculated with `dsfs_ratecalc`.

    ### Returns
    
    * lin_data : float array-like
        >Countrate data nicely ironed out with quality flags (slowroll error, discretization error, invisible rollover warning)
        
    """
    time = np.linspace(0,len(ratedata), num=10*(len(ratedata))+1)[:-1]
    rate = np.ravel(ratedata[:,0:10])
    slowroll = np.ravel(ratedata[:,12:22])
    low_disc = np.ravel(ratedata[:,22:32])
    rect_med = np.repeat(ratedata[:,10], 10)
    invis_roll = np.repeat(ratedata[:,11],10)
    lin_data = np.vstack((time,rate,slowroll,low_disc,rect_med,invis_roll)).T
    return lin_data

###############################################################################
# Magnetometer (MAGS) READ AND WRITE

g_mag = [0.910,0.789,0.828] #Magnetometer gain
o_mag = [13.218,215.641,-526.711] #Magnetometer offset

mags_hdr = ''
mags_hdr += 'sync,time,'
mags_hdr += 'bx00,bx01,bx02,bx03,bx04,bx05,'
mags_hdr += 'bx06,bx07,bx08,bx09,bx10,bx11,'
mags_hdr += 'by00,by01,by02,by03,by04,by05,'
mags_hdr += 'by06,by07,by08,by09,by10,by11,'
mags_hdr += 'bz00,bz01,bz02,bz03,bz04,bz05,'
mags_hdr += 'bz06,bz07,bz08,bz09,bz10,bz11'

def read_mags(filename, varname = []):
    """
    Function to read data out of MAGS file into numpy array.

    ### Parameters
    
    * filename : str
        >Name of logfile to read
    * varname : float array-like, optional
        >MAGS array to append data into. Default empty.

    ### Returns
    
    * mags_arr : float array-like
        >Array of MAGS data from logfile. Includes data from `varname`,
        if specified.
        
    """
    f = open(filename, 'rb')
    pkt_list = []
    contents = f.read()
    starts = [m.start() for m in re.finditer(b'\x78\xfd', contents)]
    stops = starts[1:]
    stops.append(starts[-1]+80)
    for idx, s in enumerate(starts):
        stuff = unpack(mags_unpack, contents[s:s+80])
        data = mags_pkt(stuff)
        pkt_list.append(data)
    f.close()
    npkts = len(pkt_list)
    staging = np.zeros([npkts,38])
    for i in range(npkts):
        pkt = pkt_list[i]
        staging[i,0] = pkt.sync
        staging[i,1] = pkt.time
        staging[i, 2:14] = pkt.bx
        staging[i,14:26] = pkt.by
        staging[i,26:38] = pkt.bz
    if (len(varname) != 0):
        mags_arr = np.concatenate((varname,staging),axis=0)
    else:
        mags_arr = staging
    return mags_arr

###############################################################################
# Combined Data and Housekeeping (CXDH) READ

cxdh_hdr_l1 = ''
cxdh_hdr_l1 += "sync, time_payld, time_adacs, xrbr_log_no, xrfs_log_no,"
cxdh_hdr_l1 += "dsfs_log_no, hkhi_log_no,"
cxdh_hdr_l1 += "radio_temp [C], gps_temp [C], dosi_temp [C], pld_hv_bd_temp [C],"
cxdh_hdr_l1 += "pld_fpga_temp [C], pos_x_temp [C], neg_x_temp [C], pos_y_temp [C],"
cxdh_hdr_l1 += "neg_y_temp [C], pos_z_temp [C], neg_z_temp [C],"
cxdh_hdr_l1 += "cntr_temp [C], zync_temp [C], board_temp [C],"
cxdh_hdr_l1 += "v_batt [V], v_spnl [V], i_batt [A], i_spnl [A], i_epssw1 [A], i_epssw2 [A],"
cxdh_hdr_l1 += "angle_to_go, n_xray_cull_thresh, mags_log_no,"
cxdh_hdr_l1 += "p_x [Re], p_y [Re], p_z [Re], Bfield_meas1 [nT], Bfield_meas2 [nT], Bfield_meas3 [nT],"
cxdh_hdr_l1 += "Qbi_1, Qbi_2, Qbi_3, Qbi_4,"
cxdh_hdr_l1 += "counts_xray_1, counts_xray_2, counts_xray_3,"
cxdh_hdr_l1 += "counts_xray_4, counts_xray_5, counts_xray_6,"
cxdh_hdr_l1 += "dosalow_1, dosalow_2, dosalow_3,"
cxdh_hdr_l1 += "dosalow_4, dosalow_5, dosalow_6,"
cxdh_hdr_l1 += "dosamed_1, dosamed_2, dosamed_3,"
cxdh_hdr_l1 += "dosamed_4, dosamed_5, dosamed_6,"
cxdh_hdr_l1 += "dosblow_1, dosblow_2, dosblow_3,"
cxdh_hdr_l1 += "dosblow_4, dosblow_5, dosblow_6,"
cxdh_hdr_l1 += "dosbmed_1, dosbmed_2, dosbmed_3,"
cxdh_hdr_l1 += "dosbmed_4, dosbmed_5, dosbmed_6,"
cxdh_hdr_l1 += ""

cxdh_hdr_l2a = cxdh_hdr_l1[0:23]
cxdh_hdr_l2a += 'utc'
cxdh_hdr_l2a += cxdh_hdr_l1[28:]

def read_cxdh(filename,varname = []):
    """
    Function to read data out of CXDH file into numpy array.

    ### Parameters
    
    * Filename : str
        >Name of logfile to read
    * varname : float array-like, optional
        >CXDH array to append data into. Default empty.

    ### Returns
    
    * cxdh_arr : float array-like
        >Array of CXDH data from logfile. Includes data from `varname`,
        if specified.
        
    """
    f = open(filename,'rb')
    pkt_list = []
    contents = f.read()
    starts = [m.start() for m in re.finditer(b'\x51\xbb\xff\xfa', contents)]
    stops = starts[1:]
    size = stops[0] - starts[0]
    stops = stops.append(starts[-1] + size)
    for idx, s in enumerate(starts):
        #print("Size is " + str(size))
        stuff = unpack(cxdh_unpack, contents[s:s+size])
        data = cxdh_pkt(stuff)
        pkt_list.append(data)
    f.close()
    npkts = len(pkt_list)
    staging = np.zeros([npkts,70])
    for i in range(npkts):
        pkt = pkt_list[i]
        staging[i,0] = pkt.sync
        staging[i,1] = pkt.time_payld
        staging[i,2] = pkt.time_adacs
        staging[i,3] = pkt.xrbr_log_no
        staging[i,4] = pkt.xrfs_log_no
        staging[i,5] = pkt.dsfs_log_no
        staging[i,6] = pkt.hkhi_log_no
        staging[i,7:21] = pkt.thermistors
        staging[i,21] = pkt.v_batt
        staging[i,22] = pkt.v_spnl
        staging[i,23] = pkt.i_batt
        staging[i,24] = pkt.i_spnl
        staging[i,25] = pkt.i_epssw1
        staging[i,26] = pkt.i_epssw2
        staging[i,27] = pkt.angle_to_go
        staging[i,28] = pkt.n_xray_cull_thresh
        staging[i,29] = pkt.mags_log_no
        staging[i,30] = pkt.p_x
        staging[i,31] = pkt.p_y
        staging[i,32] = pkt.p_z
        staging[i,33] = pkt.Bfield_meas1
        staging[i,34] = pkt.Bfield_meas2
        staging[i,35] = pkt.Bfield_meas3
        staging[i,36] = pkt.Qbi[0]
        staging[i,37] = pkt.Qbi[1]
        staging[i,38] = pkt.Qbi[2]
        staging[i,39] = pkt.Qbi[3]
        staging[i,40:46] = pkt.counts_xray
        staging[i,46:52] = pkt.dosa_low
        staging[i,52:58] = pkt.dosa_med
        staging[i,58:64] = pkt.dosb_low
        staging[i,64:70] = pkt.dosb_med
    if (len(varname) != 0):
        cxdh_arr = np.concatenate((varname,staging),axis=0)
    else:
        cxdh_arr = staging
    return cxdh_arr

###############################################################################
# Stored State of Health AND Channels History READ
def read_ssoh(filename, hdrname, dataname):
    """
    Read SSOH datafile into list. NOTE THIS DOES NOT
    READ INTO NUMPY ARRAY.

    ### Parameters
    
    * filename : str
        >Name of SSOH logfile to read.
    * hdrname : str list
        >List of headers SSOH packets are appended to.
    * dataname : ssoh_pkt list
        >List of SSOH packets to append data into.

    ### Returns
    
    * None.

    """
    f = open(filename, 'rb')
    contents = f.read()
    starts = [m.start() for m in re.finditer(b'\xb1\xba', contents)]
    stops = starts[1:]
    stops.append(getsize(filename) - starts[0])
    for idx, s in enumerate(starts):
        stuff = unpack(soh_unpack, contents[s:s+13])
        hdr = ssoh_hdr(stuff)
        unpackstr = str(hdr.len)+'B'
        data = unpack(unpackstr, contents[s+13:s+13+hdr.len])
        hdrname.append(hdr)
        dataname.append(data)
    f.close()

def read_chls(filename, hdrname, dataname):
    """
    Read CHLS datafile into list. NOTE THIS DOES NOT
    READ INTO NUMPY ARRAY.

    ### Parameters
    
    * filename : str
        >Name of CHLS logfile to read.
    * hdrname : str list
        >List of headers CHLS packets are appended to.
    * dataname : chls_pkt list
        >List of CHLS packets to append data into.

    ### Returns
    
    * None.

    """
    
    f = open(filename, 'rb')
    contents = f.read()
    starts = [m.start() for m in re.finditer(b'\xed\xfe', contents)]
    stops = starts[1:]
    stops.append(getsize(filename) - starts[0])
    for idx, s in enumerate(starts):
        stuff = unpack(chst_unpack, contents[s:s+14])
        hdr = chst_hdr(stuff)
        unpackstr = str(hdr.len)+'B'
        data = unpack(unpackstr, contents[s+14:s+14+hdr.len])
        hdrname.append(hdr)
        dataname.append(data)
    f.close()

###############################################################################
# File Utility Functions

def makeL1(L0_data):
    """
    Function that takes array of L0 data and applies L1 conversion numbers.

    ### Parameters
    
    * L0_data : float, array-like
        >Array of logfile data (as read with `read_****` functions). Array
        shape determines what processing is applied. If shape is not
        recognized no processing occurs.

    ### Returns
    
    *data : float, array-like
        >Processed L1 data. If logfile data was not recognized, is a 
        copy of input array.
    *rate : float, array-like
        >DSFS countrate array. Only returned if logfile type is DSFS.

    """
    data = np.copy(L0_data) #Make a copy of the data so we don't overwrite L0 data
    if (data.shape[1] == 70): #CXDH
        for i in range(len(data)): #Switch the endianness of the times
            data[i,1] = (sw32(int(data[i,1]))-2**31-1)/1000
        data[:,21] *=  0.02685546875 #V_batt datanumber -> V
        data[:,22] *=  0.05126953125 #V_spnl datanumber -> V
        data[:,23] *=  0.00981201171875 #I_batt datanumber -> A
        data[:,23] -=  1.969 #I_batt offset (A)
        data[:,24] *=  0.0119677734375 #I_spnl datanumber -> A
        data[:,25] *=  0.0051953125 #I_epssw1 datanumber -> A
        data[:,26] *=  0.0051953125 #I_epssw2 datanumber -> A
        data[:,27] *=  1.0/360.0 #ATG datanumber -> degrees
        data[:,30:33] /=  6371000.0 #p_x/y/z meters -> Earth radii
        data[:,33:36] = (data[:,33:36] / 10.0 -o_mag) * g_mag * 32.0 #B_x/y/z datanumber -> nT with gain/offset
        data[:,36:40] *=  4.656612875245797e-10 #Qbi conversion factor (AMA)
        return data
    if (data.shape[1] == 38): #MAGS
        #First divide by 10.0 (representational trick), then apply offset
        #After offset subtracted, multiply by gain and convert datanumber- > nT
        data[:,2:14] = (data[:,2:14] / 10.0 - o_mag[0]) * g_mag[0] * 32.0
        data[:,14:26] = (data[:,14:26] / 10.0 - o_mag[1]) * g_mag[1] * 32.0
        data[:,26:38] = (data[:,26:38] / 10.0 - o_mag[2]) * g_mag[2] * 32.0
        return data
    if (data.shape[1] == 3): #XRFS
        for i in range(len(data)): #Switch the endianness of the times
            data[i,0] = sw32(int(data[i,0]))
        data[:,0] /= 1000.0 #milliseconds -> seconds
        data[:,1:3] /= 50000 #Undo the representation trick
        data[:,1:3] -= 0.5 #Center x and y on 0,0
        return data
    if ((data.shape[1] == 5) | (data.shape[1] == 8)): #XRBR Sci or HK
        data[:,0] /= 1000.0 #milliseconds -> seconds
        return data
    if (data.shape[1] == 28): #DSFS
        #DSFS numbers don't need converting, but the rates are calculated
        #here during L1 processing
        AData = data[:, [6,8,9,10,11,12,13,14,15,16,17]]
        BData = data[:, [7,18,19,20,21,22,23,24,25,26,27]]
        ARate = dsfs_ratecalc(AData)
        BRate = dsfs_ratecalc(BData)
        lin_ARate = lin_dsfs(ARate)
        lin_BRate = lin_dsfs(BRate)
        rate = np.concatenate((lin_ARate,lin_BRate),axis=1)
        return data,rate
    print('Warning: Datatype not recognized.')
    return data
 
def makeL2a(L1_data,lognumbers=[]):
    """
    Function that takes array of L1 data and applies L2a conversion functons.

    ### Parameters
    
    * L1_data : float, array-like
        >Array of L1 data (as processed with `makeL1`). Array
        shape determines what processing is applied. If shape is not
        recognized no processing occurs.
    * Lognumbers : int, array-like
        >Array of lognumbers of the files `L1_data` is pulled from. Used to sync
        XRBR/XRFS data.

    ### Returns
    
    * data : float, array-like
        >Processed L2a data. If L1 data was not recognized, is a 
        copy of input array.
    * rate : float, array-like
        >DSFS countrate array. Only returned if L1 array contains DSFS.

    """
    data = np.copy(L1_data) #Make a copy of the data so we don't overwrite L1 data
    if (data.shape[1] == 70): #CXDH
        data[:,2] = GPS2UTC(data[:,2]) #Convert GPS time to UNIX timestamp
        #Convert the positions from ECEF to GSE
        pos = Coords(data[:,30:33], 'GDZ', 'car', units = ['Re','Re','Re'], ticks = Ticktock(GPS2UTC(data[:,2]),'UNX'))
        pos_GSE = pos.convert('GSE','car')
        data[:,30] = pos_GSE.x
        data[:,31] = pos_GSE.y
        data[:,32] = pos_GSE.z
        return data
    if (data.shape[1] == 38): #MAGS
        data[:,1] = GPS2UTC(data[:,1]) #Convert GPS time to UNIX timestamp
        return data
    if (data.shape[1] == 3): #XRFS
        data = xray_sync(data,lognumbers,XRFS=True) #Sync the payld times to GPS time 
        data[:,0] = GPS2UTC(data[:,0]) #Convert GPS time to UNIX timestamp
        #Transform into centered coordinate system with x,y in (-1,1)
        x,y = nonlin_correction(data[:,1],data[:,2])
        data[:,1] = x
        data[:,2] = y
        #Convert from MCP Position to on sky RA and Dec
        data[:,1:2] = MCP2ANG(data[:,1:2], data[:,0],lognumbers,XRFS=True)
        return data
    if ((data.shape[1] == 5) | (data.shape[1] == 8)): #XRBR Sci or HK
        data = xray_sync(data,lognumbers,XRFS=False) #Sync the payld times to GPS time 
        data[:,0] = GPS2UTC(data[:,0]) #Convert GPS time to UNIX timestamp
        return data
    if (data.shape[1] == 28): #DSFS
        #Sync DSFS times to GPS time
        data = dsfs_sync(data,lognumbers)
        #Sync DSFS GPS time to UTC
        data[:,2] = GPS2UTC(data[:,2])
        #Recalculate countrate with UTC instead of payload time
        AData = data[:, [6,8,9,10,11,12,13,14,15,16,17]]
        BData = data[:, [7,18,19,20,21,22,23,24,25,26,27]]
        ARate = dsfs_ratecalc(AData)
        BRate = dsfs_ratecalc(BData)
        lin_ARate = lin_dsfs(ARate)
        lin_BRate = lin_dsfs(BRate)
        rate = np.concatenate((lin_ARate,lin_BRate),axis=1)
        return data,rate
    print('Warning: Datatype not recognized.')
    return data
   
def log_update(filetype, gp_date, lib_ver):
    '''
    Function that automatically updates L1/L2 logfile with the date of file 
    conversion and script version for specified science logfile type. 

    ### Parameters
    
    * filetype : string
        >Filetype being logged (i.e. XRFS, XRBR, DSFS, MAGS, CXDH) in string form.
        
    * gp_date : string
        >Date of ground pass in YYYYMMDDHHMM string form.

    * lib_ver : string
        >Version of cupidsat used to process data in 'x.x.x' form.

    ### Returns
    
    * None.

    '''
    date = int(dt.datetime.now().strftime('%Y%m%d%H%M'))
    gp = int(gp_date)
    try:
        logfile = np.loadtxt('Log_'+filetype+'.csv',delimiter=',',skiprows=1)
    except OSError:
        logfile = np.asarray([[0,0,0]])
    logfile = np.concatenate((logfile,[[date,gp,lib_ver]]),axis=0)
    np.savetxt('Log_'+filetype+'.csv',logfile,delimiter=',',header='Conversion Date, Ground Pass Date, Script Version')
    
def GPS2UTC(GPS_time):
    '''
    Little function that makes a UTC datetime object out of an ADACS time uint32.

    ### Parameters
    
    * GPS_time : uint32, array-like
        >Seconds since Jan 6th, 1980 as reported by ADACS.

    ### Returns
    
    * UTC_time : datetime object, array-like
        >ADACS time translated to UTC in a datetime object.

    '''
    if (np.asarray(GPS_time).size == 1):
        UTC_time = (dt.datetime(1980,1,6,tzinfo=dt.timezone.utc) + dt.timedelta(seconds=GPS_time)).timestamp()
    elif (np.asarray(GPS_time).size > 1):
        UTC_time = np.zeros(len(GPS_time))
        for i in np.arange(len(GPS_time)): 
            UTC_time[i] = (dt.datetime(1980,1,6,tzinfo=dt.timezone.utc) + dt.timedelta(seconds=GPS_time[i])).timestamp()
            
    return UTC_time
    
def xray_sync(xray_struct,xray_lognos,l2a_path='../../L2a/',XRFS=True):
    '''
    Function that syncs x-ray telescope payload time to GPS time.
    
    ### Parameters
    
    * xray_struct : float, array-like
        >Numpy array containing CuPID XRFS/XRBR data (as read with read_XR**()).
    
    * xray_lognos : int, array-like
        >CuPID XRBR/XRFS lognumbers being synced.
        
    * l2a_path : str
        >Path to level 2a data.
        
    * XRFS : bool
        >If true, assumes XRFS sync. If false, assumes XRBR.

    ### Returns
    
    * sync_struct : float, array-like
        >Numpy array containing CuPID XRFS/XRBR data with time synced to GPS time.

    '''
    if (len(xray_lognos)==1): #Is there only one logfile to sync?
        logno = xray_lognos
        cxdh_arr = np.asarray([])
        names = [f for f in os.listdir(l2a_path+'cxdh/') if ('.csv' in f)]
        names = names[::-1] #Search backward through directory for speed
        test_ind = 4 if XRFS else 3 #Which index contains the lognumbers?
        for name in names: 
            try:
                next_cxdh = np.loadtxt(l2a_path+'cxdh/'+name,delimiter=',')
            except OSError:
                print('XRay Sync Warning: L2a CXDH files not found.')
            if np.any(np.isin(next_cxdh[:,test_ind],logno)):
                if len(cxdh_arr)!=0: #Is this not the first array to be read?
                    cxdh_arr = np.concatenate((cxdh_arr, next_cxdh),axis=0)
                else: #This is the first array to be read
                    cxdh_arr = next_cxdh
        if (len(cxdh_arr)==0):
            print('XRay Sync Warning: Corresponding CXDH not found. X-ray files not synced.')
            return np.asarray([])
        payld_time = cxdh_arr[:,1]
        adacs_time = cxdh_arr[:,2]
        xray_time = xray_struct[:,0]
        sync_time = np.zeros(len(xray_time)) #Stage an array to put synced times
        delt_ind = np.asarray([0]) #Stage an array to put jump indices (treat start of file as jump)
        for i in np.arange(1,len(xray_time)): #Let's find the jumps if they exist
            if (xray_time[i]-xray_time[i-1] < 0):
                delt_ind = np.concatenate((delt_ind, [i]))
        for idx, i in enumerate(delt_ind): #Process each jump individually
            #Use insane numpy operations to find the last payld time in CXDH before the jump
            jump = np.where((payld_time - xray_time[i]) < 0, (payld_time - xray_time[i]), -np.inf).argmax()
            payld_step = payld_time[jump]
            adacs_step = adacs_time[jump]
            if (len(delt_ind)!=1): #Let's throw a reset warning in case someone wants to look
                filetype = 'XRFS' if XRFS else 'XRBR'
                log = str(logno)
                print('XRay Sync Warning: Reset detected in '+filetype+'-'+log)
            if ((len(delt_ind)==1)|(i==delt_ind[-1])): #Is this the start of file with no jumps/the last jump?
                sync_time[i:-1] = xray_time[i:-1] + (adacs_step-payld_step)
            else: #Else process the jumps individually
                sync_time[i:delt_ind[idx+1]] = xray_time[i:delt_ind[idx+1]] + (adacs_step-payld_step)
        sync_struct = np.copy(xray_struct)
        sync_struct[:,0] = sync_time
        return sync_struct
    if (len(xray_lognos)>1): #Is there more than one logfile to sync?
        logno = xray_lognos
        cxdh_arr = np.asarray([])
        names = [f for f in os.listdir(l2a_path+'cxdh') if ('.csv' in f)]
        names = names[::-1] #Search backward through directory for speed
        test_ind = 4 if XRFS else 3 #Which index contains the lognumbers?
        for name in names: 
            try:
                next_cxdh = np.loadtxt(l2a_path+'cxdh/'+name,delimiter=',')
            except OSError:
                print('XRay Sync Warning: L2a CXDH files not found.')
            if np.any(np.isin(next_cxdh[:,test_ind],logno)):
                if len(cxdh_arr)!=0: #Is this not the first array to be read?
                    cxdh_arr = np.concatenate((cxdh_arr, next_cxdh),axis=0)
                else: #This is the first array to be read
                    cxdh_arr = next_cxdh
        if (len(cxdh_arr)==0):
            print('XRay Sync Warning: Corresponding CXDH not found. X-ray files not synced.')
            return np.asarray([])
        payld_time = cxdh_arr[:,1]
        adacs_time = cxdh_arr[:,2]
        xray_time = xray_struct[:,0]
        sync_time = np.zeros(len(xray_time)) #Stage an array to put synced times
        delt_ind = np.asarray([0]) #Stage an array to put jump indices (treat start of file as jump)
        for i in np.arange(len(xray_time)): #Let's find the jumps if they exist
            if (i==0):
                continue
            else:
                if (xray_time[i]-xray_time[i-1] < 0):
                    delt_ind = np.concatenate((delt_ind, [i]))
        for idx, i in enumerate(delt_ind): #Process each jump individually
            #Use insane numpy operations to find the last payld time in CXDH before the jump    
            jump = np.where((payld_time - xray_time[i]) < 0, (payld_time - xray_time[i]), -np.inf).argmax()
            payld_step = payld_time[jump]
            adacs_step = adacs_time[jump]
            if (len(delt_ind)!=1): #Let's throw a reset warning in case someone wants to look
                filetype = 'XRFS' if XRFS else 'XRBR'
                log = ''
                for num in logno:
                    log += str(num)+'/'
                print('XRay Sync Warning: Reset detected in '+filetype+'-'+log)
            if ((len(delt_ind)==1)|(i==delt_ind[-1])): #Is this the last jump/start of file with no jumps?
                sync_time[i:-1] = xray_time[i:-1] + (adacs_step-payld_step)
            else: #Else process the jumps individually
                sync_time[i:delt_ind[idx+1]] = xray_time[i:delt_ind[idx+1]] + (adacs_step-payld_step)
        sync_struct = xray_struct
        sync_struct[:,0] = sync_time
        return sync_struct
    if (len(xray_lognos)<1):
        print('XRay Sync Warning: No lognumber specified.')
        return np.asarray([])


def dsfs_sync(dsfs_struct,dsfs_lognos,l2a_path='../../L2a/'):
    '''
    Function that syncs dosimeter payload time to GPS time.

    ### Parameters
    
    * dsfs_struct : float, array-like
        >Numpy array containing CuPID DSFS data (as read with read_dsfs()).
    
    * dsfs_lognos : int, array-like
        >Structure containing CuPID DSFS lognumbers being synced.
        
    * l2a_path : str
        >Path to level 2a data.

    ### Returns
    
    * sync_struct : float, array-like
        >Numpy array containing CuPID DSFS data with time synced to GPS time.

    '''
    cxdh_arr = np.asarray([])
    names = [f for f in os.listdir(l2a_path+'cxdh/') if ('.csv' in f)] #Get all the cxdh filenames
    names = names[::-1] #Sort them in reverse
    test_ind = 5 #What index is the dsfs lognumber?
    for name in names: #Test every file
        next_cxdh = np.loadtxt(l2a_path+'cxdh/'+name,delimiter=',') #Load the cxdh file
        if np.any(np.isin(next_cxdh[:,test_ind],dsfs_lognos)): #Is the dsfs lognumber in there?
            cxdh_arr = np.concatenate((cxdh_arr, next_cxdh),axis=0) #Add it into the blob of cxdh data
    dosa_med = np.zeros(len(cxdh_arr),6)
    dosb_med = np.zeros(len(cxdh_arr),6)
    dosa_low = np.zeros(len(cxdh_arr),6)
    dosb_low = np.zeros(len(cxdh_arr),6)
    adacs_time = np.zeros(len(cxdh_arr))
    for i in np.arange(len(cxdh_arr)):
        dosa_low[i] = cxdh_arr[i,46:52]
        dosa_med[i] = cxdh_arr[i,52:58]
        dosb_low[i] = cxdh_arr[i,58:64]
        dosb_med[i] = cxdh_arr[i,64:70]
        adacs_time[i] = cxdh_arr[i,2]
    sync_struct = np.copy(dsfs_struct) #Copy the dsfs data
    matches = pd.DataFrame(columns=['time_adacs','time_dosi']) #Make the dataframe of matches for interpolation
    ind = 0 #Make manual index for matches
    for i in range(len(adacs_time)):
        for j in range(len(sync_struct)):
            for k in range(10):
                match = (sync_struct[j,6]==dosa_med[i])&(sync_struct[j,7]==dosb_med[i])&(sync_struct[j,8+k]==dosa_low[i])&(sync_struct[j,18+k]==dosb_low[i])
                if match:
                    df = pd.DataFrame([adacs_time[i],sync_struct[j,2]],columns=['time_adacs','time_dosi'],index=[ind])
                    matches = matches.append(df)
                    index += 1
    matches = matches.drop_duplicates(subset='time_adacs')
    matches = matches.drop_duplicates(subset='time_dosi') #Make sure the interpolation is one to one
    interp_func = interpolate.interp1d(matches['time_dosi'].to_numpy(),matches['time_adacs'].to_numpy())
    sync_time = interp_func(sync_struct[:,2])
    sync_struct[:,2] = sync_time
    return sync_struct

def csvw(data, filename, level=1):
    """
    Function that takes array of CuPID data and saves as CSV with correct header.

    ### Parameters
    
    * data : float, array-like
        >Array of logfile data (as read with `read_****` functions). Array
        shape determines what header is applied. If shape is not
        recognized no write occurs.
    * filename : str
        >string filename to save the data as.
    * level : int
        >level of data processing that has been applied to data. Default is 1.

    ### Returns
    
    * write : bool
        >Boolean of whether write occurred.
    """
    #Add '.csv' to the end of the filename if it needs it
    if (filename[-4:] != '.csv'):
        filename += '.csv'
    #Identify the type of data via its shape
    if (data.shape[1] == 70): #CXDH
        if (level == 1):
            np.savetxt(filename,data,delimiter=',',newline='\n',header=cxdh_hdr_l1, fmt='%.5f')
        if (level == 2):
            np.savetxt(filename,data,delimiter=',',newline='\n',header=cxdh_hdr_l2a, fmt='%.5f')
        return
    if (data.shape[1] == 38): #MAGS
        np.savetxt(filename,data,delimiter=',',newline='\n',header=mags_hdr, fmt='%.5f')
        return
    if (data.shape[1] == 3): #XRFS
        if (level == 1):
            np.savetxt(filename,data,delimiter=',',newline='\n',header='sync,time,x,y', fmt='%.5f')
        if (level == 2):
            np.savetxt(filename,data,delimiter=',',newline='\n',header='sync,time,RA,Dec', fmt='%.5f')
        return
    if (data.shape[1] == 5): #XRBR Sci
        np.savetxt(filename,data,delimiter=',',newline='\n',header='time,v0,v1,v2,v3', fmt='%.5f')
        return
    if (data.shape[1] == 8): #XRBR HK
        np.savetxt(filename,data,delimiter=',',newline='\n',header='time,MCP_Delta_HV,MCP_Auto/Manual,HV_Setting,Temp_Data,Delta_Event_Count,Delta_Dropped_Event_Count,Delta_Lost_Event_Count', fmt='%.5f')
        return
    if (data.shape[1] == 28): #DSFS Counts
        np.savetxt(filename,data,delimiter=',',newline='\n',header=dosihdr, fmt='%.5f')
        return
    if (data.shape[1] == 12): #DSFS Rate
        np.savetxt(filename,data,delimiter=',',newline='\n',header='time,rate_a,slowroll_a,low_disc_a,rect_med_a,invis_roll_a,time,rate_b,slowroll_b,low_disc_b,rect_med_b,invis_roll_b', fmt='%.5f')
        return
    print('Warning: Datatype not recognized.')
    return
  

def csv2cdf(data_folder, cdf_folder, warnings=True):
    '''
    Converts all CSVs in one folder into CDFs and places them in another folder.

    ### Parameters
    
    * data_folder : string
        >Folder containing csv files.
    * cdf_folder : string
        >Destination folder for CDF files.
    * warnings : bool
        >If True, displays warnings if CDF files already exist. False suppresses
        warnings. The default is True.

    ### Returns
    
    * None.

    '''
    from spacepy import pycdf
    # check if CDF data folder exists and create it if not
    cdf_folder_exists = os.path.isdir(cdf_folder)
    if (cdf_folder_exists == 0):
        os.mkdir(cdf_folder)
    
    for file in os.listdir(data_folder):
        if (file.endswith('.csv')):
    
            # create filename for CDF file
            filename = file.split('.csv')[0]
            output_file = cdf_folder + filename + '.cdf'
    
            # skip to next loop iteration if CDF file exists
            if (os.path.isfile(output_file)):
                if warnings:
                    print("Warning: '" + output_file + "' already exists; skipping to next file.'")
                continue
    
            with open(data_folder+file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                data = {}
    
                for row in csv_reader:
                    # grab the row names from the csv
                    if (line_count == 0):
                        col_names = row
                        for name in col_names:
                            if (name != ''):
                                data[name.strip()] = []
                        line_count += 1
                    # grab the row data from the csv
                    else:
                        for i in range(len(row)):
                            data[col_names[i].strip()].append(row[i])
                        line_count += 1
    
            # create CDF file
            cdf = pycdf.CDF(output_file, '')
            for key in data:
                cdf[key] = data[key]
            cdf.close()

def read_cdf(cdf_filename):
    '''
    Allows user to browse through a CDF file's variables/data through a terminal.
    User can choose to view all rows at once or select rows to view from 0 to cdf_length-1.
    
    ### Parameters
    
    * cdf_filename: string
        >A string with the name (and relative path, if needed) of the desired CDF file
    
    ### Returns
    
    * None.
    
    '''
    # open the chosen CDF file
    print("Opening chosen CDF file: ", cdf_filename)
    try:
        cdf_file = pycdf.CDF(cdf_filename)
        cdf_file.readonly(True)
    except:
        print("\nERROR: There was an error reading in the chosen CDF file.")
        print("Please make sure the path to the desired CDF file is correct.\n")
        exit()

    from spacepy import pycdf
    cdf_keys = cdf_file.keys()

    print("Welcome to the CDF File Reader.")
    cdf_length = len(cdf_file[0])
    print("Number of rows:", cdf_length, '\n')

    while True:

        print("Use the following menu to choose the variable you would like to look through.")
        print("If you would like to view all variables at once, select 'All Variables'.\n")

        menu_options = []
        for key in cdf_keys:
            menu_options.append(key)
        menu_options.append("All Variables")

        # create a terminal prompt that allows user to choose which data variables to view
        terminal_menu = TerminalMenu(menu_options, title="CDF Variables\n---------------")
        menu_entry_index = terminal_menu.show()
        var_choice = menu_options[menu_entry_index]
        print("Chosen variable: ", var_choice)

        # create another menu that allows the user to choose how to display the data
        print("Would you like to view particular rows or all of them at once?")
        terminal_menu = TerminalMenu(['Select Rows', 'All Rows'])
        menu_entry_index = terminal_menu.show()
        display_choice = 'All Rows' if menu_entry_index == 1 else 'Select Rows'
        print(display_choice, '\n')

        if (display_choice == 'Select Rows'):

            print("Enter the first and last rows you would like to view, with a hyphen('-') in between.")
            print("For exmaple, if you wanted to view rows 3 through 10, enter '3-10'.\n")

            while True:
                user_in = input("Select rows: ")
                row_selection = user_in.split('-')

                # error check user input
                if (len(row_selection) != 2):
                    print("Make sure to enter a valid start and end row selection using the correct format.\n")
                else:
                    try:
                        start_row = int(row_selection[0])
                        end_row = int(row_selection[1])
                    except:
                        print("Please enter real, non-negative numbers.\n")
                        continue

                    if (isinstance(start_row, int) == False or isinstance(end_row, int) == False):
                        print("Please enter real, non-negative numbers.\n")
                    elif (start_row < 0 or end_row > cdf_length-1 or start_row > end_row):
                        print("Make sure to enter a valid range of rows to view (between 0 and cdf_length-1).")
                        print("Number of rows:", cdf_length, '\n')
                    else:
                        break
        else:
            start_row = 0
            end_row = cdf_length-1

        # format data into tables and display in terminal
        print("Tabulating data... (this may take a while)\n")
        display_data = []
        table_headers = ['Rows']
        iter_range = range(start_row, end_row+1)

        if (var_choice == "All Variables"):
            for key in cdf_keys:
                table_headers.append(key)

            with click.progressbar(iter_range) as bar:
                for i in bar:
                    display_row = []
                    display_row.append(i)

                    for key in cdf_keys:
                        display_row.append("{:.3f}".format(float(cdf_file[key][i])))
                    display_data.append(display_row)
        else:
            table_headers.append(var_choice)
            cdf_data = cdf_file[var_choice]
            with click.progressbar(iter_range) as bar:
                for i in bar:
                    display_data.append([i, "{:.3f}".format(float(cdf_data[i]))])

        display_table = tabulate(display_data, headers=table_headers, tablefmt="psql")
        click.echo_via_pager(display_table)

        # prompt user to choose to continue or stop using script
        end_prompt = input("Would you like to view another variable (y/n)? ")
        while True:
            end_prompt = end_prompt.strip().lower()
            if (end_prompt == 'n'):
                print("Thanks for using the CDF file reader!\n")
                cdf_file.close()
                exit()
            elif (end_prompt == 'y'):
                break
            else:
                end_prompt = input('Please enter a valid response (y/n): ')

def plot_archiver(plottype, hour):
    '''
    Small utility function for 
    
    ### Parameters
    
    * cdf_filename: string
        >A string with the name (and relative path, if needed) of the desired CDF file
    
    ### Returns
    
    * None.
    
    '''
    names = [f for f in os.listdir() if (plottype in f)&(str(hour)+'hours' in f)] #Grab all the plots for given hour/type
    for name in names:
        sh.copy(name, '../../'+plottype+'/'+str(hour)+'hours/') #Copy plots into their specific directory
        os.remove(name) #Clean up the gp directory

def archiver(filename,logtype,level):
    '''
    Inserts staged data into a given data level's archives chronologically.
    * CXDH: 24 hour files
    * XRFS: 15 minute files
    * XRBR: 15 minute files
    * DSFS: 15 minute files
    * MAGS: 24 hour files

    ### Parameters
    
    * filename : string
        >Name of the pre-staged data csv
    * logtype : str
        >logfile type to be archived (e.g. cxdh, xrfs, for 2a; burst, summary for 2b)
    * level : str
        >Data level to be archived (either 2a or 2b)

    ### Returns
    
    * None.

    '''
    try:
        data = np.loadtxt(filename+'.csv',delimiter=',')
    except OSError:
        print('Data file missing')
        return
    if (logtype == 'cxdh'):
        date_list = data[:,2]
    if (logtype == 'mags'):
        date_list = data[:,1]
    if (logtype == 'xrbr'):
        date_list = data[:,0]
    if (logtype == 'xrfs'):
        date_list = data[:,0]
    if (logtype == 'dsfs'):
        date_list = data[:,2]
        try:
            rate = np.loadtxt(filename+'_Rate.csv',delimiter=',')
        except OSError:
            rate = np.zeros((1,2))
            print('Dosi rate file missing')
    day_strs = np.asarray([],dtype=str)
    hour_strs = np.asarray([],dtype=str)
    for date in date_list:
        day_strs = np.append(day_strs,[dt.datetime.fromtimestamp(date,tz=timezone.utc).strftime('%Y%m%d')])
        hour_strs = np.append(hour_strs,[dt.datetime.fromtimestamp(date,tz=timezone.utc).strftime('%Y%m%d%H')])
    day_strs = np.unique(day_strs)
    hour_strs = np.unique(hour_strs)
    home_dir = os.getcwd()
    os.chdir('../../L'+level+'/'+logtype)
    if (logtype == 'cxdh'):
        for string in day_strs:
            date_bool = (date_list > pytz.utc.localize(dt.datetime.strptime(string[0:8],'%Y%m%d')).timestamp()) & (date_list < (pytz.utc.localize(dt.datetime.strptime(string[0:8],'%Y%m%d'))+dt.timedelta(days=1)).timestamp())
            if os.path.exists(string[0:8]+'_'+logtype+'_'+level+'.csv'):
                load_data = np.loadtxt(string[0:8]+'_'+logtype+'_'+level+'.csv',delimiter=',')
                combo_data = np.concatenate((data[date_bool],load_data),axis = 0)
                combo_data = combo_data[np.argsort(combo_data[:,2])]
                combo_data = np.unique(combo_data,axis=0)
                np.savetxt(string[0:8]+'_'+logtype+'_'+level+'.csv',combo_data, delimiter=',',newline='\n', header=cxdh_hdr_l2a)
            else:
                data = data[np.argsort(data[:,2])]
                np.savetxt(string[0:8]+'_'+logtype+'_'+level+'.csv',data, delimiter=',',newline='\n', header=cxdh_hdr_l2a)
    if (logtype == 'mags'):
        for string in day_strs:
            date_bool = (date_list > pytz.utc.localize(dt.datetime.strptime(string[0:8],'%Y%m%d')).timestamp()) & (date_list < (pytz.utc.localize(dt.datetime.strptime(string[0:8],'%Y%m%d'))+dt.timedelta(days=1)).timestamp())
            if os.path.exists(string[0:8]+'_'+logtype+'_'+level+'.csv'):
                load_data = np.loadtxt(string[0:8]+'_'+logtype+'_'+level+'.csv',delimiter=',')
                combo_data = np.concatenate((data[date_bool],load_data),axis = 0)
                combo_data = combo_data[np.argsort(combo_data[:,1])]
                combo_data = np.unique(combo_data,axis=0)
                np.savetxt(string[0:8]+'_'+logtype+'_'+level+'.csv',combo_data, delimiter=',',newline='\n', header=mags_hdr)
            else:
                data = data[np.argsort(data[:,1])]
                np.savetxt(string[0:8]+'_'+logtype+'_'+level+'.csv',data, delimiter=',',newline='\n', header=mags_hdr)
    if (logtype == 'xrfs'):
        for string in hour_strs:
            for i in np.arange(4,):
                date_bool = (date_list > (pytz.utc.localize(dt.datetime.strptime(string[0:10],'%Y%m%d'))+dt.timedelta(minutes=15*(int(i)))).timestamp()) & (date_list < (pytz.utc.localize(dt.datetime.strptime(string[0:10],'%Y%m%d'))+dt.timedelta(minutes=15*(int(i)+1))).timestamp())
                minstr = '00' if i == 0 else str(15*(i))
                if os.path.exists(string[0:10]+minstr+'_'+logtype+'_'+level+'.csv'):
                    load_data = np.loadtxt(string[0:10]+minstr+'_'+logtype+'_'+level+'.csv',delimiter=',')
                    combo_data = np.concatenate((data[date_bool],load_data),axis = 0)
                    combo_data = combo_data[np.argsort(combo_data[:,1])]
                    combo_data = np.unique(combo_data,axis=0)
                    np.savetxt(string[0:10]+minstr+'_'+logtype+'_'+level+'.csv',combo_data, delimiter=',',newline='\n', header='time,x,y')
                else:
                    data = data[np.argsort(data[:,1])]
                    np.savetxt(string[0:10]+minstr+'_'+logtype+'_'+level+'.csv',data, delimiter=',',newline='\n', header='time,x,y')
    if (logtype == 'xrbr'):
        for string in hour_strs:
            for i in np.arange(4,dtype=int):
                date_bool = (date_list > (pytz.utc.localize(dt.datetime.strptime(string[0:10],'%Y%m%d'))+dt.timedelta(minutes=15*(int(i)))).timestamp()) & (date_list < (pytz.utc.localize(dt.datetime.strptime(string[0:10],'%Y%m%d'))+dt.timedelta(minutes=15*(int(i)+1))).timestamp())
                minstr = '00' if i == 0 else str(15*(i))
                if os.path.exists(string[0:10]+minstr+'_'+logtype+'_'+level+'.csv'):
                    load_data = np.loadtxt(string[0:10]+minstr+'_'+logtype+'_'+level+'.csv',delimiter=',')
                    combo_data = np.concatenate((data[date_bool],load_data),axis = 0)
                    combo_data = combo_data[np.argsort(combo_data[:,1])]
                    combo_data = np.unique(combo_data,axis=0)
                    np.savetxt(string[0:10]+minstr+'_'+logtype+'_'+level+'.csv',combo_data, delimiter=',',newline='\n', header='time,v0,v1,v2,v3')
                else:
                    data = data[np.argsort(data[:,1])]
                    np.savetxt(string[0:10]+minstr+'_'+logtype+'_'+level+'.csv',data, delimiter=',',newline='\n', header='time,v0,v1,v2,v3')     
    if (logtype == 'dsfs'):
        for string in hour_strs:
            for i in np.arange(4,dtype=int):
                date_bool = (date_list > (pytz.utc.localize(dt.datetime.strptime(string[0:10],'%Y%m%d'))+dt.timedelta(minutes=15*(int(i)))).timestamp()) & (date_list < (pytz.utc.localize(dt.datetime.strptime(string[0:10],'%Y%m%d'))+dt.timedelta(minutes=15*(int(i)+1))).timestamp())
                minstr = '00' if i == 0 else str(15*(i))
                if os.path.exists(string[0:10]+minstr+'_'+logtype+'_'+level+'.csv'):
                    load_data = np.loadtxt(string[0:10]+minstr+'_'+logtype+'_'+level+'.csv',delimiter=',')
                    combo_data = np.concatenate((data[date_bool],load_data),axis = 0)
                    combo_data = combo_data[np.argsort(combo_data[:,1])]
                    combo_data = np.unique(combo_data,axis=0)
                    np.savetxt(string[0:10]+minstr+'_'+logtype+'_'+level+'.csv',combo_data, delimiter=',',newline='\n', header=dosihdr)
                    load_rate = np.loadtxt(string[0:10]+minstr+'_'+logtype+'_rate_'+level+'.csv',delimiter=',')
                    combo_rate = np.concatenate((rate[date_bool],load_rate),axis = 0)
                    combo_rate = combo_rate[np.argsort(combo_data[:,0])]
                    combo_rate = np.unique(combo_rate,axis=0)
                    np.savetxt(string[0:10]+minstr+'_'+logtype+'_rate_'+level+'.csv',combo_rate, delimiter=',',newline='\n', header='time,rate_a,slowroll_a,low_disc_a,rect_med_a,invis_roll_a,time,rate_b,slowroll_b,low_disc_b,rect_med_b,invis_roll_b')
                else:
                    data = data[np.argsort(data[:,1])]
                    np.savetxt(string[0:10]+minstr+'_'+logtype+'_'+level+'.csv',data, delimiter=',',newline='\n',  header=dosihdr)
                    rate = rate[np.argsort(rate[:,0])]
                    np.savetxt(string[0:10]+minstr+'_'+logtype+'_rate_'+level+'.csv',rate, delimiter=',',newline='\n',  header='time,rate_a,slowroll_a,low_disc_a,rect_med_a,invis_roll_a,time,rate_b,slowroll_b,low_disc_b,rect_med_b,invis_roll_b')
    os.chdir(home_dir)

def qmult(qp,qq):
    """
    Multiples two quaternions defined as -
    qp * qq = qr  or equivalently  a(qq) * a(qp) = a(qr)
    Reproduced from Steve Fujikawa's FLIB

    """
    qr = np.zeros((4,1))
    qa1=qp[0]
    qa2=qp[1]
    qa3=qp[2]
    qa4=qp[3]
    qb1=qq[0]
    qb2=qq[1]
    qb3=qq[2]
    qb4=qq[3]
    qx1 = qa1*qb4 + qa2*qb3 - qa3*qb2 + qa4*qb1
    qx2 = -qa1*qb3 + qa2*qb4 + qa3*qb1 + qa4*qb2
    qx3 = qa1*qb2 - qa2*qb1 + qa3*qb4 + qa4*qb3
    qx4 = -qa1*qb1 - qa2*qb2 - qa3*qb3 + qa4*qb4
    if (qx4 < 0):
        qx1=-qx1
        qx2=-qx2
        qx3=-qx3
        qx4=-qx4

    qr[0]=qx1
    qr[1]=qx2
    qr[2]=qx3
    qr[3]=qx4
    return qr

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin. See [this](https://stackoverflow.com/questions/34372480/rotate-point-about-another-point-in-degrees-python)
    explanation. The angle should be given in radians.
    """
    a = np.cos(angle)
    qx = origin[0,:] + np.cos(angle) * (point[0,:] - origin[0,:]) - np.sin(angle) * (point[1,:] - origin[1,:])
    qy = origin[1,:] + np.sin(angle) * (point[0,:] - origin[0,:]) + np.cos(angle) * (point[1,:] - origin[1,:])
    return qx, qy

def QBI2ANG(QBI,QBT = [-np.sqrt(2)/2,np.sqrt(2)/2,0,0]):
    """
    Function to calculate:
    1. Telescope quaternion from QBI
    1. Rotation matrix
    1. and RA/Dec/Roll
    Developed by Emil Atz

    ### Parameters
    
    * QBI : float,array-like
        >Body-inertial quaternion.
        
    * QBT : float,array-like, optional
        >Definition of the quaternion to rotate the body CS into the telescope CS
        The actual rotation is (0,180,-90) if you follow (x,y,z)
        This quaternion was calculated from Steve Fujikawa's FLIB
        The default is `[-np.sqrt(2)/2,np.sqrt(2)/2,0,0]`

    ### Returns
    
    * ang : float,array-like
        >`[RA,Dec,Roll]` of telescope in radians

    """
    Qres = qmult(QBI,QBT); # Call to qmult to calculate Quaternion Telescope to Inertial

    q1 = Qres[0]
    q2 = Qres[1]
    q3 = Qres[2]
    q4 = Qres[3]
    # This is the calculation of the rotation matrix. This rotation matrix rotates
    # The coordinate system (like ECI) into the coordinates pointing of CuPID.
    # Therefore, multiplying the rotation matrix by [[1],[0],[0]] gives the pointing
    # of the X axis, multiply by [[0],[1],[0]] gives pointing of Y axis.... etc
    # because each row of the rotation matrix is the unit vector by which the
    # the axis points
    RX = np.zeros(3)
    RY = np.zeros(3)
    RZ = np.zeros(3)
    RX[0] = +q1*q1 - q2*q2 - q3*q3 + q4*q4
    RX[1] = 2*(q1*q2 + q3*q4)
    RX[2] = 2*(q1*q3 - q2*q4)
    RY[0] = 2*(q1*q2 - q3*q4)
    RY[1] = -q1*q1 + q2*q2 - q3*q3 + q4*q4
    RY[2] = 2*(q2*q3 + q1*q4)
    RZ[0] = 2*(q1*q3 + q2*q4)
    RZ[1] = 2*(q2*q3 - q1*q4)
    RZ[2] = -q1*q1 - q2*q2 + q3*q3 + q4*q4
    # Calculation of the pointing angles from quaternions
    # This comes from code by Fred Eckert and Aspire - specifically Quaternion.cpp
    #####
    # Aspire - High-performance, lightweight IP-based messaging middleware.
    # *   Copyright (C) 2010-2011 Ken Center, Fred Eckert & Rod Green
    #####
    #THIS IS ROLL
    denom = q1*q3 - q2*q4 #Prep denominator
    psi = np.arctan2(-(q2*q3 + q1*q4),denom) #Calculate arc tan with quadrant dependency
    psi = psi + 0
    # These if statements bring the roll into the positive rotation by wrapping 2pi
    if (psi < -np.pi):
        n = (np.ceil(-psi / (2*np.pi)))
        Roll = psi+(n*2*np.pi)
    elif (psi >= np.pi):
        n = (psi / (2*np.pi));
        Roll = psi-(n*2*np.pi)
    else:
        Roll = psi
    #####
    # THIS IS RIGHT ASCENSION
    denom = q3*q1 + q2*q4 #Prep denominator
    phi = np.arctan2(q3*q2 - q1*q4,denom) #Calculate arc tan with quadrant dependency
    # These if statements bring the RA into the positive rotation by wrapping 1pi
    if (phi < 0):
        n = (np.ceil(-phi / (2*np.pi)))
        RA = phi+(n*2*np.pi)
    elif (phi >= 2*np.pi):
        n = (phi / (2*np.pi));
        RA = phi-(n*2*np.pi)
    else:
        RA = phi
    #####
    # THIS IS DECLINATION
    acos = q3*q3 + q4*q4 - q2*q2 - q1*q1 #This is actually an element of a directional cosine matrix
    if (acos > 1):
        acos = 1
    if (acos < -1):
        acos = -1
    theta = np.arccos(acos) #get the angle
    # These if statements bring the Declination to be defined from the equator
    if (theta >=0):
        Dec = np.pi/2 - theta
    else:
        Dec = -np.pi/2 - theta
    ang = np.asarray([RA,Dec,Roll])
    return ang

def MCP2ANG(pos,times,xray_lognos,XRFS,HalfFOV = 2.2*np.pi/180,l2a_path='../../L2a/'):
    """
    Converts XRFS MCP location to on-sky RA and Dec.

    ### Parameters
    
    * pos : float, array-like
        >Array of XRFS MCP positions in the form `[x,y]`.
    * times : float, array-like
        >Array of XRFS times in UNIX UTC TIMESTAMP (NOT PAYLOAD TIME).
    * xray_lognos : int
        >CuPID XRBR/XRFS lognumber being synced.
    * XRFS : bool
        >If true, assumes XRFS sync. If false, assumes XRBR.
    * HalfFOV : float, optional
        >Half of CuPID's FOV, for calculating angle from boresight. The default is `2.2*np.pi/180`.
    * l2a_path : string, optional
        >Path to level 2a data storage. The default is `'../../L2a/'`.

    ### Returns
    
    * pos_rolled : float, array-like
        >Array of XRFS RA and Dec positions in the form `[RA,Dec]`.

    """
    #Read in the necessary processed cxdh files to get quaternions and times
    cxdh = np.asarray([])
    names = [f for f in os.listdir(l2a_path+'cxdh') if ('.csv' in f)]
    names = names[::-1] #Search backward through directory for speed
    test_ind = 4 if XRFS else 3 #Which index contains the lognumbers?
    for name in names: 
        try:
            next_cxdh = np.loadtxt(l2a_path+'cxdh/'+name,delimiter=',')
        except OSError:
            print('XRay Sync Warning: L2a CXDH files not found.')
        if np.any(np.isin(next_cxdh[:,test_ind],xray_lognos)):
            if len(cxdh)!=0: #Is this not the first array to be read?
                cxdh = np.concatenate((cxdh, next_cxdh),axis=0)
            else: #This is the first array to be read
                cxdh = next_cxdh
    if (len(cxdh)==0):
        print('XRay Sync Warning: Corresponding CXDH not found. X-ray files not synced.')
        return np.asarray([])
    qbi = cxdh[:,36:40]
    adacs_time = cxdh[:,2]
    ang = np.zeros((len(cxdh),3))
    for i in range(len(cxdh)):
        ang_temp = QBI2ANG(qbi[i,:])
        ang[i,0] = ang_temp[0] #calculate SC RA, Dec, Roll from QBI
        ang[i,1] = ang_temp[1]
        ang[i,2] = ang_temp[2]
    #interpolate SC pointing from CXDH
    RA_func = interpolate.interp1d(adacs_time, ang[:,0], kind='cubic')
    Dec_func = interpolate.interp1d(adacs_time, ang[:,1], kind='cubic')
    Roll_func = interpolate.interp1d(adacs_time, ang[:,2], kind='cubic')
    
    #The *HalfFOV is to be able to convert the X-Y points into an angle from the
    #boresight (0,0)
    pos_ang = pos * HalfFOV
    #Get interpolated pointings and add angles from boresight 
    #(yet to be rotated into correct orientation)
    origins = np.asarray([RA_func(times),Dec_func(times)])
    RA_unrotated = origins[0,:]+pos_ang[:,0]
    Dec_unrotated = origins[1,:]+pos_ang[:,1]
    roll = Roll_func(times)
    #rotate around boresight origins by roll angle
    pos_rolled = rotate(origins,np.asarray([RA_unrotated,Dec_unrotated]), roll)*180/np.pi
    return pos_rolled

def sw32(i):
    return unpack("<I", pack(">I", i))[0]

def sw16(i):
    return unpack("<H", pack(">H", i))[0]

###############################################################################
# Plot Utility Functions MOVE TO USER-FACING PART OF LIBRARY IN PRODUCTION

def summary_plot(start_date, hours, HK = False, data_path = '../../L2a', pdf=False):
    '''
    Plotting function to create a summary plot of given length and start time.
    Uses processed L2a CXDH data.
    Planned functionality: passing list of keywords to determine contents of
    plots.

    ### Parameters
    
    * start_date : str
        >YYYYMMDDHHMM string for plot start date.
    
    * hours : int
        >Duration of plot in hours.  
    
    * HK : bool, optional
        >Include housekeeping data (to make Data Acquision Plots). The default is `False`.
        
    * data_path : str, optional
        >String path to L2a data. The default is `'../../L2a'`.
        
    * pdf : bool, optional
        >If `True`, writes a pdf version of plot in addition to the png version. The default is `False`.

    ### Returns
    
    * None.

    '''

    start_time = dt.datetime.strptime(start_date, '%Y%m%d%H%M')
    stop_time = start_time + dt.timedelta(hours=hours)
    home_dir = os.getcwd()
    os.chdir(data_path+'/cxdh')
    cxdh = np.asarray([])
    try:
        cxdh = np.loadtxt(start_time.strftime('%Y%m%d')+'_cxdh_2a.csv', delimiter=',')
    except OSError:
        os.chdir(home_dir)
        return
    for i in np.arange((stop_time-start_time).days):
        try:
            cxdh = np.concatenate((cxdh,np.loadtxt((start_time+dt.timedelta(days=int(i))).strftime('%Y%m%d')+'_cxdh_2a.csv', delimiter=',')),axis=0)
        except OSError:
            os.chdir(home_dir)
            return
            
    #Initialize empty arrays to read data into
    time = np.zeros(len(cxdh),dtype=dt.datetime)
    time_exp = np.zeros(len(cxdh)*6,dtype=dt.datetime)
    xrbr_log = np.zeros(len(cxdh))
    xrfs_log = np.zeros(len(cxdh))
    dsfs_log = np.zeros(len(cxdh))
    mags_log = np.zeros(len(cxdh))
    therm = np.zeros((len(cxdh),14))
    batt_v = np.zeros(len(cxdh))
    pos_GSE = np.zeros((len(cxdh),3))
    mlat = np.zeros(len(cxdh))
    mlong = np.zeros(len(cxdh))
    b_field = np.zeros((len(cxdh),3))
    xray_cnt = np.zeros(len(cxdh)*6)
    dosi_cnt = np.zeros((len(cxdh)*6,2)) #0 is a, 1 is b on second index
    
    #Read in CXDH data
    for i in np.arange(len(cxdh)):
        time[i] = dt.datetime.utcfromtimestamp(cxdh[i,2]) #Assume it comes as UNIX time
        xrbr_log[i] = cxdh[i,3]
        xrfs_log[i] = cxdh[i,4]
        dsfs_log[i] = cxdh[i,5]
        mags_log[i] = cxdh[i,29]
        therm[i,:] = cxdh[i,7:21] #temps in degrees C
        batt_v[i] = cxdh[i,21]
        pos_GSE[i,:] = [cxdh[i,30],cxdh[i,31],cxdh[i,32]] #Position in GSE (Re)
        b_field[i,:] = [32 * g_mag[0]*(cxdh[i,33] - o_mag[0]),32 * g_mag[1]*(cxdh[i,34] - o_mag[1]),32 * g_mag[2]*(cxdh[i,35] - o_mag[2])]
        for j in np.arange(6):
            time_exp[6*i+j] = time[i]+ dt.timedelta(seconds=(j / 8640)) #Inferred 10s cadence
            xray_cnt[6*i+j] = cxdh[i,40+j]
            if (j==0):
                if (i==0):
                    dosi_cnt[0,:] = [0,0]
                else:
                    dosi_cnt[6*i+j,:] = [(cxdh[i,46+j] + 256 * cxdh[i,52+j] - cxdh[i-1,51] - 256 * cxdh[i-1,57])/10, (cxdh[i,58+j] + 256 * cxdh[i,64+j] - cxdh[i-1,63] - 256 * cxdh[i-1,69])/10]
            else:
                dosi_cnt[6*i+j,:] = [(cxdh[i,46+j] + 256 * cxdh[i,52+j] - cxdh[i,46+j-1] - 256 * cxdh[i,52+j-1])/10, (cxdh[i,58+j] + 256 * cxdh[i,64+j] - cxdh[i,58+j-1] - 256 * cxdh[i,64+j-1])/10]

        #COORDINATE CONVERSIONS
        pos = Coords(pos_GSE[i,:], 'GSE', 'car', units = ['Re','Re','Re'], ticks = Ticktock(time[i],'UTC'))
        pos_MAG = pos.convert('MAG','sph')
        mlat[i] = pos_MAG.lati
        mlong[i] = pos_MAG.long
    time_mask = ((time >= start_time)&(time <= stop_time))
    time_exp_mask = ((time_exp >= start_time)&(time_exp <= stop_time))
    time = time[time_mask]
    time_exp = time_exp[time_exp_mask]
    xrbr_log = xrbr_log[time_mask]
    xrfs_log = xrfs_log[time_mask]
    dsfs_log = dsfs_log[time_mask]
    mags_log = mags_log[time_mask]
    therm = therm[time_mask]
    batt_v = batt_v[time_mask]
    pos_GSE = pos_GSE[time_mask]
    mlat = mlat[time_mask]
    mlong = mlong[time_mask]
    b_field = b_field[time_mask]
    xray_cnt = xray_cnt[time_exp_mask]
    dosi_cnt = dosi_cnt[time_exp_mask]
    
    #INITIALIZE FIGURE
    rows = 7 if HK else 5
    fig, axes = plt.subplots(nrows=rows, ncols=1, sharex=True)
    fig.subplots_adjust(hspace=0)
    
    for i in np.arange(0,rows):
        if i == 0:
            axes[i].plot(time_exp,xray_cnt,color=black)
            axes[i].set_ylabel(r'$CR_{XRAY}$')
            #axes[i].legend(['XRBR','XRFS'],labelcolor=[red,blue],loc='center left',bbox_to_anchor=(1,0.5),frameon=False)
            title = 'DAP '+start_date+' '+str(hours)+' hours' if HK else 'Summary '+start_date+' '+str(hours)+' hours'
            axes[i].set_title(title)
            bottom,top = axes[i].get_ylim()
            y1 = (top-bottom)*0.2 + bottom
            y2 = (top-bottom)*0.8 + bottom
            axes[i].text(start_time+dt.timedelta(seconds=360),y1,int(xrbr_log[0]),color=blue)
            axes[i].text(start_time+dt.timedelta(seconds=360),y2,int(xrfs_log[0]),color=red)
            for j in np.arange(1,len(time)):
                if (xrbr_log[j]!=xrbr_log[j-1]):
                    axes[i].axvline(x=time[j],color=blue,alpha=0.5)
                    axes[i].text(time[j]+dt.timedelta(seconds=360),y1,int(xrbr_log[j]),color=blue)
                if (xrfs_log[j]!=xrfs_log[j-1]):
                    axes[i].axvline(x=time[j],color=red,alpha=0.5)
                    axes[i].text(time[j]+dt.timedelta(seconds=360),y2,int(xrfs_log[j]),color=red)
        if i == 1:
            axes[i].plot(time_exp,dosi_cnt[:,0],color=red)
            axes[i].plot(time_exp,dosi_cnt[:,1],color=blue)
            axes[i].legend(['A','B'],loc='center left',bbox_to_anchor=(1,0.5),frameon=False)
            axes[i].set_ylabel(r'$CR_{DSFS}$')
            bottom,top = axes[i].get_ylim()
            y = (top-bottom)*0.8 + bottom
            axes[i].text(start_time+dt.timedelta(seconds=360),y,int(dsfs_log[0]),color=black)
            for j in np.arange(1,len(time)):
                if (dsfs_log[j]!=dsfs_log[j-1]):
                    axes[i].axvline(x=time[j],color=black,alpha=0.5)
                    axes[i].text(time[j]+dt.timedelta(seconds=360),y,int(dsfs_log[j]),color=black)
        if i == 2:
            axes[i].plot(time,b_field[:,0],color=red)
            axes[i].plot(time,b_field[:,1],color=blue)
            axes[i].plot(time,b_field[:,2],color=green)
            axes[i].legend(['X','Y','Z'],loc='center left',bbox_to_anchor=(1,0.5),frameon=False)
            axes[i].set_ylabel('B (nT)')
            bottom,top = axes[i].get_ylim()
            y = (top-bottom)*0.8 + bottom
            axes[i].text(start_time+dt.timedelta(seconds=360),y,int(mags_log[0]),color=black)
            for j in np.arange(1,len(time)):
                if (mags_log[j]!=mags_log[j-1]):
                    axes[i].axvline(x=time[j],color=black,alpha=0.5)
                    axes[i].text(time[j]+dt.timedelta(seconds=360),y,int(mags_log[j]),color=black)
        if i == 3:
            axes[i].plot(time,mlat,color=black)
            axes[i].hlines([60,90],start_time,stop_time,colors = red, linestyles='dashed',alpha = 0.3)
            axes[i].set_ylabel('MLAT')
        if i == 4:
            axes[i].plot(time,mlong,color=black)
            axes[i].set_ylabel('MLONG')
        if i == 5:
            axes[i].plot(time,batt_v,color=black)
            axes[i].set_ylabel(r'$V_{batt}$')
        if i == 6:
            axes[i].plot(time,therm[:,13],color=black)
            axes[i].set_ylabel(r'$T_{board}$')
            axes[i].set_ylim(-150,150)
            axes[i].hlines([100,-100],start_time,stop_time,colors = red, linestyles='dashed',alpha = 0.3)
    axes[-1].set_xlabel('Time (UTC)')
    axes[-1].set_xlim(start_time,stop_time)
    tick_locs = [start_time + i * (stop_time-start_time)/8 for i in np.arange(9)]
    axes[-1].set_xticks(tick_locs)
    ticktimes = [dt.datetime.fromtimestamp(stamp, tz=dt.timezone.utc) for stamp in np.linspace(start_time.timestamp(),stop_time.timestamp(),9)]
    labels = [date.strftime('%H%M') for date in ticktimes]
    axes[-1].set_xticklabels(labels)
    
    fig = plt.gcf()
    fig.set_size_inches(8,rows+3)
    
    os.chdir(home_dir)
    plot_name = 'DAP_{date}_{hours}hours'.format(date=start_date,hours=str(hours)) if HK else 'summary_{date}_{hours}hours'.format(date=start_date,hours=str(hours))
    if pdf:
        plt.savefig(plot_name+'.pdf', bbox_inches='tight')
    plt.savefig(plot_name+'.png',dpi = 100)
    plt.close()

def burst_plot(start_date, minutes, data_path = '../../../L2a/', cr_cadence = 1, pdf = False):
    """
    Combined x-ray countrate, x-ray position, two-channel dosi countrate, mags magnetometer plot
    utility.

    ### Parameters
    
    * start_date : string
        >String start date in YYYYMMDDHHMM format.
    * minutes : int
        >Duration of plot in minutes.
    * data_path : string, optional
        >String path to L2a data directory. The default is '../../../L2a/'.
    * cr_cadence : int, optionalo
        >Seconds over which to calculate x-ray countrate. The default is 1.
    * pdf : bool, optional
        >If true, writes a pdf version of plot in addition to the png version. The default is False.

    ### Returns
    
    * None.

    """
    start_time = dt.datetime.strptime(start_date, '%Y%m%d%H%M') #Grab time range in datetime
    stop_time = start_time + dt.timedelta(minutes = minutes)
    start_time = pytz.utc.localize(start_time)
    stop_time = pytz.utc.localize(stop_time)
    #Generate the strings that will be used to reference the data files (15 minute and daily)
    if (start_date[10:12] == '00')|(start_date[10:12] == '15')|(start_date[10:12] == '30')|(start_date[10:12] == '45'):
        minstr = start_date #This happens if we only need to load one file (i.e. falls perfectly on a 15 minute time range)
    else: #And these happen if we have to load two files, i.e. if we're overlapping two time ranges
        if (int(start_date[10:12])//15 == 0):
            minstr=[start_date[:10]+'00',start_date[:10]+'15']
        if(int(start_date[10:12])//15 == 1):
            minstr=[start_date[:10]+'15',start_date[:10]+'30']
        if(int(start_date[10:12])//15 == 2):
            minstr=[start_date[:10]+'30',start_date[:10]+'45']
        if(int(start_date[10:12])//15 == 3):
            date1 = dt.datetime(start_time.year, start_time.month,start_time.day,start_time.hour,45)
            date2 = date1+dt.timedelta(minutes=15)
            minstr=[date1.strftime('%Y%m%d%H%M'),date1.strftime('%Y%m%d%H%M')]
    date1 = dt.datetime(start_time.year, start_time.month,start_time.day)
    date2 = dt.datetime(stop_time.year, stop_time.month,stop_time.day)
    daystr = np.unique([date1.strftime('%Y%m%d'),date2.strftime('%Y%m%d')]) #Same as above if statements but for days (easier)
    
    home_dir = os.getcwd()
    os.chdir(data_path) #Step into 2a directory
    os.chdir('xrfs')
    xrfs=[]
    for string in minstr:
        try:
            xrfs = np.concatenate((xrfs, np.loadtxt(string+'_xrfs_2a.csv',delimiter = ',')),axis=0) #load in all the xrfs we need
        except OSError:
            continue
    os.chdir('../dsfs')
    dsfs_ARate = []
    dsfs_BRate = []
    for string in minstr:
        try:
            dsfs_ARate = np.concatenate((dsfs_ARate, np.loadtxt(string+'_dsfs_ARate_2a.csv',delimiter = ',')),axis=0) #load in all the dsfs we need
            dsfs_BRate = np.concatenate((dsfs_BRate, np.loadtxt(string+'_dsfs_BRate_2a.csv',delimiter = ',')),axis=0)
        except OSError:
            continue
    
    os.chdir('../mags')
    mags = []
    for string in daystr:
        try:
            mags = np.concatenate((mags, np.loadtxt(string+'_mags_2a.csv',delimiter = ',')),axis=0) #load in all the mags we need
        except OSError:
            continue
    os.chdir(home_dir)
    #Calculate X-Ray Countrate
    cr_arr = np.zeros(int(stop_time.timestamp()-start_time.timestamp())//cr_cadence)
    cr_times = np.arange(start_time.timestamp(),stop_time.timestamp(),cr_cadence)
    xr_times = xrfs[:,0]
    for i in np.arange(len(cr_arr)):
        cr_arr[i] = len(xr_times[(xr_times < start_time.timestamp()+i*cr_cadence)&(xr_times > start_time.timestamp()+(i-1)*cr_cadence)])/cr_cadence
    
    cr_mask = (cr_time > start_time.timestamp())&(cr_time < stop_time.timestamp())
    dsA_mask = (dsfs_ARate[:,0] > start_time.timestamp())&(dsfs_ARate[:,0] < stop_time.timestamp())
    dsB_mask = (dsfs_BRate[:,0] > start_time.timestamp())&(dsfs_BRate[:,0] < stop_time.timestamp())
    mags_mask = (mags[:,0] > start_time.timestamp())&(mags[:,0] < stop_time.timestamp())
    
    fig_l, axes_l = plt.subplots(nrows=4, ncols=1, sharex=True)
    fig_l.subplots_adjust(hspace=0)
    
    for i in np.arange(0,4):
            if i == 0:
                axes_l[i].plot(cr_times[cr_mask],cr_arr[cr_mask],color=red)
                axes_l[i].set_ylabel(r'$CR_{XRFS}$')
                title = 'CuPID Burst '+start_time.strftime('%b %d, %Y')+' ('+str(minutes)+' minutes)'
                axes_l[i].set_title(title)
            if i == 1:
                axes_l[i].plot(cr_times[cr_mask],np.zeros(len(cr_arr))[cr_mask],color=black)
                axes_l[i].set_ylabel(r'$BG$')
                axes_l[i].set_yticks([0])
            if i == 2:
                if (len(dsfs_ARate) != 0) & (len(dsfs_BRate) != 0):
                    axes_l[i].plot(dsfs_ARate[dsA_mask,0],dsfs_ARate[dsA_mask,1],color=red)
                    axes_l[i].plot(dsfs_BRate[dsB_mask,0],dsfs_BRate[dsB_mask,1],color=blue)
                    axes_l[i].legend(['A','B'],loc='center left',bbox_to_anchor=(1,0.5),frameon=False)
                axes_l[i].set_ylabel(r'$CR_{DSFS}$')
            if i == 3:
                if (len(mags) != 0):
                    axes_l[i].plot(mags[mags_mask,0],mags[mags_mask,1],color=red)
                    axes_l[i].plot(mags[mags_mask,0],mags[mags_mask,2],color=blue)
                    axes_l[i].plot(mags[mags_mask,0],mags[mags_mask,3],color=green)
                    axes_l[i].legend(['X','Y','Z'],loc='center left',bbox_to_anchor=(1,0.5),frameon=False)
                axes_l[i].set_ylabel('B')
    axes_l[-1].set_xlabel('UTC (HH:MM:SS)')
    axes_l[-1].set_xlim(start_time.timestamp(),stop_time.timestamp())
    axes_l[-1].set_xticks(np.linspace(start_time.timestamp(),stop_time.timestamp(),4))
    ticktimes = [dt.datetime.fromtimestamp(stamp, tz=dt.timezone.utc) for stamp in np.linspace(start_time.timestamp(),stop_time.timestamp(),4)]
    labels = [date.strftime('%H:%M:%S') for date in ticktimes]
    axes_l[-1].set_xticklabels(labels)
    
    #Make a histogram to the right of the plot with the same size as the 4 bars
    h = np.sum([ax.get_position().height for ax in axes_l])
    axes_r = plt.axes([axes_l[-1].get_position().x0+1.3*axes_l[-1].get_position().width,axes_l[-1].get_position().y0,axes_l[-1].get_position().width,h])
    axes_cb = plt.axes([axes_r.get_position().x0+axes_r.get_position().width,axes_r.get_position().y0,0.02,axes_r.get_position().height])
    bin_width = 0.5 #width of bins in degrees
    RA_bins = np.arange(int(np.min(xrfs[:,1])),int(np.max(xrfs[:,1])),bin_width)
    Dec_bins = np.arange(int(np.min(xrfs[:,2])),int(np.max(xrfs[:,2])),bin_width)
    h2, RA_edges, Dec_edges, image = axes_r.hist2d(xrfs[:,1],xrfs[:,2],bins=[RA_bins,Dec_bins], cmap='inferno')
    cbar = fig_l.colorbar(image,cax=axes_cb,orientation='vertical')
    axes_r.set_xlabel('RA [deg]')
    axes_r.set_ylabel('Dec [deg]')
    cbar.set_label('Counts')
    
    fig = plt.gcf()
    fig.set_size_inches(10,5)
    
    plot_name = 'burst_{date}_{mins}mins'.format(date=start_date,mins=str(minutes))
    if pdf:
        plt.savefig(plot_name+'.pdf', bbox_inches='tight')
    plt.savefig(plot_name+'.png', dpi = 100)
    plt.close()