# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 17:48:10 2021

@author: Vishwesh
"""
import numpy as np
from Logic_Py.basic_gates import OR, AND
from Logic_Py.plotting import plot_basic
from Logic_Py.combinational_gates import *
from Logic_Py.Logic_circuits import *
from Logic_Py.arithmatic_gates import *
w = [1,1,0,1,1,0,0,1,0,0]
x = [0,0,0,1,0,1,1,0,1,1]
y = [0,1,0,1,0,1,0,0,0,0]
z = [1,1,0,1,1,0,0,1,0,0]

#%%
s = Priority_Enc4_2(w,x,y,z)

#%%
g = full_subtractor(w,x,y)

#%%
l = Decoder4_16(w,x,y,z)
#%%
m,n,o,p = BCD2Excess3(w,x,y,z)

#%%
q,p,r,s = Excess32BCD(w,x,y,z)
#%%
plot_basic(x, y, AND)

#%%
from Logic_Py.arithmatic_gates import full_adder
from Logic_Py.plotting import plot_full_adder

sum_,carry_ = full_adder(x, y,z)
plot_full_adder(x,y,z)

#%%
Difference, Borrow = plot_half_subtractor(x,y)
#Difference, Borrow = full_subtractor(w,x,y)
print("Difference : ", Difference, "Borrow : ",Borrow)
#%%


