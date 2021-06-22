"""Low-level programming interface example using databuffers
Copyright (C) Nanosurf AG - All Rights Reserved (2021)
License - MIT"""

import nanosurf
import numpy as np
import matplotlib.pyplot as plt


def setup_input_switch():
    """Set up the analog input path of the C3000.

    - do not block DC signals,
    - connect User In B (= User2) to the second fast input
    """
    system_infra = ll.SystemInfra()
    system_infra.main_in_2_input.value = system_infra.MainIn2Input.User2
    system_infra.main_in_2_coupling.value = system_infra.FastInputCoupling.DCCoupling


# We parse the  LogicalUnit_Shard file to have access to all the constants.
# Here we use the default version on the Q: server.
# make sure that the .h file is for the software version that you are currently
# using.
print("Connecting to Nanosurf Control software...")
spm = nanosurf.USPM("LogicalUnit_InterfaceShared.h")
spm.application.Visible = True
ll = spm.lowlevel

hi_res_buffer = ll.DataBuffer()
fast_buffer = ll.DataBuffer()

# Prepare Analog signal input configuration (only for CoreAFM/C3000 controllers):
setup_input_switch()


lu_daq = ll.DataAcquisition()


# disable hi res capture

lu_daq.number_of_capture_sets.value = 1
lu_daq.active_capture_set.value = 0

hi_res_points = 40
hi_res_rate = 1e6

hi_res_channel = 0
lu_daq.capture_hi_res_ch_0_input.value = lu_daq.CaptureHiResInSignal.InDeflection
lu_daq.capture_hi_res_group_id.value = hi_res_buffer.group_id
lu_daq.capture_hi_res_channel_mask.value = 2**hi_res_channel
lu_daq.capture_hi_res_datapoints.value = hi_res_points

fast_channel = 0
lu_daq.capture_fast_ch_0_input.value = lu_daq.CaptureFastInSignal.InDeflection
lu_daq.capture_fast_group_id.value = fast_buffer.group_id
lu_daq.capture_fast_channel_mask.value = 2**fast_channel
lu_daq.capture_fast_datapoints.value = hi_res_points * lu_daq.capture_fast_sampling_rate.value / hi_res_rate

# print("Start capturing")
lu_daq.capture_start()

# wait until the ramp is done
fast_buffer.synchronize_data_group()
# fast_buffer.synchronize_data_group()
print("is_synchronizing = " + str(fast_buffer.is_synchronizing))
while fast_buffer.is_synchronizing:
    # print("Synchronizing buffer")
    pass

# wait until data are measured and transferred to the DataBuffer
print("is_data_valid = " + str(fast_buffer.is_valid))
while not fast_buffer.is_valid:
    # print("Data is not yet valid")
    pass

fast_data = np.array(fast_buffer.channel(fast_channel).data)
fast_data = fast_data / (pow(2, 31) - 1) * 10.0

hi_res_data = np.array(hi_res_buffer.channel(hi_res_channel).data)
hi_res_data = hi_res_data / (pow(2, 31) - 1) * 10.0

print("Fast amplitude:", max(fast_data) - min(fast_data))
print("HiRes amplitude:", max(hi_res_data) - min(hi_res_data))

plt.plot(fast_data, 'r')
plt.plot(hi_res_data, 'b')
