# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:09:17 2020

@author: Mai Tai
"""

from neogiinstruments.MaiTai import MaiTai
from time import sleep
import numpy as np
from instruments import CRotator
from neogiinstruments import Photodiode
from neogiinstruments.StellarNet import StellarNet as SN
import h5py
import datetime
import os
import matplotlib.pyplot as plt
from tqdm import tqdm

today = datetime.datetime.today()
date = str(today.date())
filepath="C://Users//Mai Tai//Desktop//Squires, Brian//WPDSHG" 
os.chdir(filepath)
filename = f'{date}.hdf5'




wavelengths = np.arange(800,902,2)
angles = np.arange(2,5,.1)
plt.ion()
fig, axs = plt.subplots(ncols=1, sharex=False, sharey=False)

for w in wavelengths:
    DATA = []
    VOLTS = []
    MaiTai.MoveWav(w)
    sleep(10)
    CRotator.C.home()
    CRotator.MoveRot(angles[0], True)
    MaiTai.Shutter(1)
    sleep(10)
    axs.clear()
    axs.set(xlabel='Wavelength(nm)',ylabel='Counts(a.u.)')
    R = tqdm(angles,desc=f'{w}nm',
             position=0, leave=True)
    for ang in R:
        CRotator.MoveRot(ang, True)
        sleep(.2)
        spec = SN.GetSpec()
        V = Photodiode.Photodiode()
        VOLTS.append(V)
        axs.plot(*spec)
        plt.pause(.01)
        axs.set(title=f'{V}V at {w}nm')
        with h5py.File(filename,'a') as hdf:
            dset = hdf.create_dataset(f'{w}nm/{V[0]}V',data=spec)
    with h5py.File(filename,'a') as hdf:
        dset = hdf.create_dataset(f'{w}nm/voltages',data=VOLTS)
        
        