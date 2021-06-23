#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:38:26 2020

@author: briansquires
"""

from StellarNet import StellarNet
import Photodiode
#from MaiTai import MaiTai
from instruments import CRotator
import matplotlib.pyplot as plt
import time
import numpy as np
import os



def PDSHG(anglestart, anglestop, anglestep, inttime, filename):

        

    CRotator.MoveRot(anglestart, True)
    StellarNet.IntTime(inttime)
    filepath = os.getcwd()
    #MaiTai.Shutter(0)
    input('Close Shutter and press enter')
    time.sleep(2)
    bkg = StellarNet.GetSpec()
    #MaiTai.Shutter(1)
    input('Open Shutter and press enter')
    spectra = []
    pdvoltages = []
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for i in np.arange(anglestart, anglestop, anglestep):
        CRotator.MoveRot(i, True)
        time.sleep(1)
        p = Photodiode.Photodiode()
        pdvoltages.append(p)
        S = StellarNet.GetSpec()
        spectra.append(S)
        ax.plot(*S)
        plt.pause(.001)
    
    DATA = np.asarray([bkg,spectra,pdvoltages])
    
    np.save('Data\\'+ filename,DATA)
        
   
    return bkg, spectra, pdvoltages


            
            
            