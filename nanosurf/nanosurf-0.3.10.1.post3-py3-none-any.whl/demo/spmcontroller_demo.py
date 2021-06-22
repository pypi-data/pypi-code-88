#%%
""" Implements support for CX Controller Hardware features

Copyright (C) Nanosurf AG - All Rights Reserved (2021)
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
https://www.nanosurf.com
"""

import nanosurf.spmcontroller as spmcontroller
import matplotlib.pyplot as plt

# connect to running application
spm = spmcontroller.connect()

# write a dc level to an output
tipdac = spm.get_dac(spmcontroller.Converter.HiResOut_TIPVOLTAGE)
tipdac.dc = 5
del tipdac

# reading an analog input
userin = spm.get_adc(spmcontroller.Converter.HiResIn_USER1)
print(f"User input: {userin.dc:g}{userin.unit}")
del userin

# read amplitude of current dynamic mode  
lockin1 = spm.get_lock_in(spmcontroller.Module.SigAnalyzer_1)
print(f"Lockin 1 input amp: {lockin1.input_amp:g}")
lockin1.input_amp
del lockin1

# setup secondary lock-in for custom ac measurement  
reference_out = spm.get_dac(spmcontroller.Converter.FastOut_USER)
signal_in = spm.get_adc(spmcontroller.Converter.FastIn_USER)
lockin2 = spm.get_lock_in(spmcontroller.Module.SigAnalyzer_2)
reference_out.source = lockin2  # excitation gos out at Userr Fast Output
lockin2.source = signal_in      # return signal comes from Fast DeflectionIn
lockin2.freq = 10000 # [Hz]
lockin2.amp_v = 0.5 # [V]
print(f"Lockin 2 input amp: {lockin2.input_amp:g}")
del lockin2

# measure some data and plot
daq = spm.get_data_sampler()
daq.channels = ['InUser1', 'InUser2']
daq.samples = 1000
daq.sample_rate = 10000 #[Hz]
daq.measure()

print(f"Sample rate ={daq.sample_rate}Hz")
for ch in daq.channels:
    plt.plot(daq.timeline, daq.data[ch], label=f"{ch}, range={daq.data_max[ch]}, unit={daq.data_unit[ch]}")
plt.legend()
plt.show()
del daq
# %%
