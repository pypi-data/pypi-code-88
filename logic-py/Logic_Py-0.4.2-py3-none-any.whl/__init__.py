# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 17:34:19 2021

@author: Vishwesh
"""
from Logic_Py.basic_gates import AND, OR, NOT, NAND, NOR,XNOR,XOR
from Logic_Py.secondary_gates import AND_AND, AND_OR, AND_NAND, AND_NOR, OR_AND, OR_OR 
from Logic_Py.secondary_gates import OR_NAND, OR_NOR, NAND_AND, NAND_OR, NAND_NAND, NAND_NOR 
from Logic_Py.secondary_gates import NOR_AND, NOR_OR, NOR_NAND, NOR_NOR
from Logic_Py.arithmatic_gates import half_adder,full_adder
from Logic_Py.combinational_gates import Binary2Gray, Gray2Binary,EParity_gen,EParity_check,OParity_gen,OParity_check
from Logic_Py.plotting import plot_full_adder, plot_half_adder, plot_secondary, plot_basic
#%% update 2
from Logic_Py.combinational_gates import Excess32BCD
from Logic_Py.Logic_circuits import Decoder2_4,Decoder4_16,Decoder3_8,Encoder2_1,Encoder4_2,Encoder8_3,Priority_Enc4_2
from Logic_Py.arithmatic_gates import half_subtractor,full_subtractor
from Logic_Py.plotting import plot_full_subtractor,plot_half_subtractor

#%%