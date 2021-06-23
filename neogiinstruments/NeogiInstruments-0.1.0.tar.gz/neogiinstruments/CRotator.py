# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:32:01 2020

@author: Mai Tai
"""

from instrumental import instrument, u, list_instruments
import time
import numpy as np
from PowerMeter import PowerMeter
from Photodiode import Photodiode


try:
        C = instrument('C')
except:
        C = instrument('C')
        
def Position():
    return C.position()
        
def MoveRot(position, Wait):
    """Helper function for instrumental to avoid clutter and make code 
    more readable
    >>>returns null"""
    C.move_to(position*u.degree, wait = Wait)
    
def PowerRotLoop(pstart, pstop, pstep, pwait):
    """Main acquisition code to collect power as a function of 
    rotation stage angle. This can be run separately, but is embedded in 
    WavLoop for wavelength dependent calibration
    ************
    pstart = Initial angular position in degrees
    pstop = Final angular position in degrees
    pstep = Angular step size in degrees
    pwait = wait time between steps in seconds
    >>>>>returns P = 2D Array"""
    #wavelength = input("Shutter The Laser and Enter Wavelength: ")
    #filename = f"C:\\Users\\Mai Tai\\Desktop\\Python Code\\PowerDependentSHG\\Calibration\\Data{wavelength}.npy"
    #Shutter(0)
    print("Homing")
    C.home(wait = True)
    time.sleep(5)
    print('Homing finished')
    #input("Unshutter the laser then hit Enter: ")
    Pwr = []
    Pwrstd = []
    Pos = []
    Vol = []
    Volstd = []
    #Shutter(1)
    for i in np.arange(pstart-pstep,pstop + pstep,pstep):
        if i>=pstart:
            MoveRot(i,True)
            time.sleep(pwait)
            p=PowerMeter.PowAvg()
            print(str(C.position) + '>>>>>> ' + str(p[0]) +' mW')
            Pos.append(float(str(C.position).split(' ')[0]))
            Pwr.append(p[0])
            Pwrstd.append(p[1])
            V, Vstd = Photodiode()
            Vol.append(float(str(V).split(' ')[0]))
            Volstd.append(float(str(Vstd).split(' ')[0]))
        else:
            MoveRot(i,True)
            time.sleep(pwait)
    P = np.asarray([Pos,Pwr,Pwrstd,Vol, Volstd])
    #Shutter(0)
    #np.save(f"{filename}",P)
    #input("Shutter the laser then hit Enter: ")
    return P
    