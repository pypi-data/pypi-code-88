#!/usr/bin/env python3

import numpy as np
from scipy.optimize import curve_fit

# Find the parameter beta (= daily contact rate) from data from a region
# Pass a numpy array 'numinfec', of number of infected people over a small 
# period (typically one or two weeks) at the onset of the infection there.
def findbeta(numinfec):
    I0 = numinfec[0]
    
    def func(t, beta):
        return I0 * np.exp(beta * t)
    
    dur = numinfec.shape[0]
    
    tdata = np.array([t for t in range(dur)])
    popt, pcov = curve_fit(func, tdata, numinfec)
    
    est_beta = popt[0]
    
    return est_beta