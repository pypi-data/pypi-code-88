# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 14:05:42 2021

@author: nkdi
"""

def trapezoidal_sum_2d(f,x,y):
    import numpy as np
    xa = x[:-1]
    xb = x[1:]
    ya = y[:-1]
    yb = y[1:]
    dx = np.dot(np.atleast_2d(xb - xa).T,np.ones((1,np.size(ya))))    
    dy = np.dot(np.ones((np.size(xa),1)),np.atleast_2d(yb - ya))
    darea = dx*dy
    fa = f[:-1,:-1]
    fb = f[:-1,1:]
    fc = f[1:,:-1]
    fd = f[1:,1:]    
    return sum( sum( darea*(fa + fb + fc + fd)/4 ) )