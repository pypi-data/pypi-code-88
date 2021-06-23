# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:14:23 2020

@author: Mai Tai
"""

from instruments.MaiTai import MaiTai
import time
import numpy as np
from instruments import CRotator
from scipy.optimize import curve_fit

wavelengths = np.arange(860,902,2)
CALIB = []
for w in wavelengths:
    MaiTai.MoveWav(w)
    print(f'moving to {w}')
    time.sleep(30)
    MaiTai.Shutter(1)
    print(f'starting loop at {w}')
    d = CRotator.PowerRotLoop(0, 10, .5, 1)
    CALIB.append(d)
    filename = f'{w}'
    np.save(filename,d,allow_pickle=True)

MaiTai.MaiTai.write('OFF')

def Line(x,m,b):
    return m*x +b

#%%
FIT = []
for i in range(len(Files)):
    v = Files[i][3]
    p = Files[i][1]
    fit, cov = curve_fit(Line,v,p)
    FIT.append(fit)
