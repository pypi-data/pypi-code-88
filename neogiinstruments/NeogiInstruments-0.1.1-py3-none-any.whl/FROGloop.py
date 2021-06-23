# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:40:00 2020

@author: Mai Tai
"""

from pymeasure.instruments.newport import esp300
from time import sleep
from StellarNet import StellarNet as SN
import matplotlib.pyplot as plt
import numpy as np

def find_nearest(array,value):
    array = np.asarray(array)
    idx = (np.abs(array-value)).argmin()
    return idx, array[idx]

esp = esp300.ESP300("GPIB0::2::INSTR")

esp1 = esp300.Axis(1,esp)
esp2 = esp300.Axis(2,esp)
esp3 = esp300.Axis(3,esp)
esp.clear_errors()
esp.enable()

DATA = []
POS = []
IAC = []
input('Close Shutter and press enter')

bkg = SN.GetSpec()
wl = bkg[0]
input('Open Shutter and press enter')

plt.ion()
fig, axs = plt.subplots(ncols=2, sharey=False)
esp3.home()
sleep(5)
esp3.position = -3
sleep(2)
for i in range(1000):
    while i<10000:
        try:
            pos = esp3.position
            sleep(0.1)
            data = SN.GetSpec()
            DATA.append(data[1])
            POS.append(pos)
            left = find_nearest(data[0],400)[0] - 5
            right = find_nearest(data[0],400)[0] +5
            IAC.append(data[1][left:right].sum())
            axs[0].clear()
            axs[0].plot(wl,data[1])
            axs[0].set(xlabel='Wavelength(nm)')
            axs[1].clear()
            axs[1].plot(POS,IAC)
            plt.pause(.001)
            sleep(.1)
            esp3.position = i/1000 -3
            sleep(.5)
            print(pos)
            i = i+1
        except:
            continue


    
    
    