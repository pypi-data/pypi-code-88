# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:09:55 2020

@author: neogi
"""

import pyvisa
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date
import nidaqmx
from nidaqmx.constants import TerminalConfiguration
from scipy.optimize import curve_fit

#%%

def PowerMeterSet(wavelength, zero, attn=True,speed=3):
    '''
    wavelength(nm)
    zero = True/False:  Make sure the detector is under ambient conditions 
        under which the experiment will be run
    attn = attenuator on(=True)/off(=False)
    for speed, 1=slow, 2=medium, 3=fast.  Fast is reccomended
        attn and speed have been set to default values and do not require input
    '''
    
    PM.write(f'W{wavelength}')
    if zero == True:
        PM.write('Z1')
    elif zero == False:
        PM.write('Z0')
    else:
        print('zero is a True/False input')
    if attn == True:
        PM.write('A1')
    elif attn == False:
        PM.write('A0')
    else:
        print('attn is a True/False input')
    PM.write(f'F{speed}')
    

        
def Power(samples):
    '''samples is the number of power measurements taken.
    This function returns a 2-tuple of which the first 
    element is the average power in Watts and the second
    is the standard deviation of the collected data.
    The 'try: except: ' is to avoid detector timeout.  Basically,
    if there is an error, that measurement is thrown out and 
    the loop continues on to the next one.
    '''
    D = []
    for i in range(0,samples,1):
        try:
            d = float(PM.query('D?')[1:-1])
            D.append(d)
        except:
            continue
    P = np.mean(D)
    Pstd = np.std(D)
    Punc = Pstd/np.sqrt(samples)## Because we are using the average, the 
                                ## uncertainty is the standard error of the 
                                ## mean, not the standard deviation
                                
    return P, Punc


def LivePlotPower():
    '''Will plot power vs time (really iteration number) until a keyboard
    interrupt (ctrl-c in console).  
    Requires QT5Agg matplotlib: activate with '%matplotlib auto' in console
    '''
    i = 1
    plt.ion()
    try:
        while i>0:
            plt.scatter(i,Power(1)[0])
            plt.pause(0.05)
            i=i+1
    except KeyboardInterrupt:
        pass
        
def LivePlotPD():
    i=1
    plt.ion()
    try:
        while i>0:
            plt.errorbar(i,PD()[0],yerr=PD()[1],fmt='o')
            plt.pause(0.05)
            i=i+1
    except KeyboardInterrupt:
        pass

def ArdInit():
    ard.write('$X')
    ard.write('$H')
def MoveArd(pos,speed):
    ard.write(f'$J =G21G90X-{pos}F{speed}')
    
def PD(nsamples=100):
    with nidaqmx.Task() as task:
        ai_channel = task.ai_channels.add_ai_voltage_chan("Dev1/ai0",terminal_config = TerminalConfiguration.RSE)
        r = task.read(number_of_samples_per_channel=nsamples)
        m = np.mean(r)
        delta = np.std(r)/np.sqrt(nsamples)
        return m, delta
def Line(x,m,b):
    return m*x+b

def LinearFit(x_data,y_data):
    params, cov = curve_fit(Line,x_data,y_data)
    m = params[0]
    m_var = cov[0,0]
    b = params[1]
    b_var = cov[1,1]
    return m, m_var, b, b_var 


#%%initialize

rm = pyvisa.ResourceManager()

ard = rm.open_resource('ASRL4::INSTR')
ard.baud_rate = 115200
PM = rm.open_resource('ASRL5::INSTR')
ArdInit()


#%% example

from time import sleep
#PowerMeterSet(405,True)
# =============================================================================
# ArdInit()
# =============================================================================
ard.write('$H')
sleep(10)
wavelength = 405
date = date.today()
#POS = []
#pwr = []
#vol = []
data = {'Position':[], 'Power':[], 'Power_Uncertainty':[], 'Voltage':[],
        'Voltage_Uncertainty':[]}
samples = 5
plt.ion()

fig, axs = plt.subplots(nrows = 2, ncols = 2)



for i in range(0,200,1):
    if i == 0:
        sleep(1)
    else:
        MoveArd(i,5000)
        sleep(.1)
        position = i
        #POS.append(position)
        data['Position'].append(position)
        power = Power(samples)
        data['Power'].append(power[0])
        data['Power_Uncertainty'].append(power[1])
        #pow_punc.append(power)
        voltage = PD(samples)
        data['Voltage'].append(voltage[0])
        data['Voltage_Uncertainty'].append(voltage[1])
        #vol.append(voltage)
        
        Marker = '.' ###Set marker for all three plots
                 
        #axs[0].plot(pow_punc,Line(pow_punc[0],m,b))
        
  
        #plt.pause(0.005)
        axs[0,0].errorbar(i,power[0],yerr=power[1],marker=Marker)
        axs[0,0].set_title(r'P vs $\theta$')
        axs[0,0].set(xlabel=r'$\theta$', ylabel= 'P (W)')
        #plt.pause(0.005)
        
        axs[0,1].errorbar(i,voltage[0],yerr=voltage[1],marker=Marker)
        axs[0,1].set_title(r'V vs $\theta$')
        axs[0,1].set(xlabel=r'$\theta$', ylabel = 'Voltage (V)')
        
        axs[1,0].errorbar(power[0],voltage[0],
                        xerr=power[1],yerr=voltage[1], 
                        marker=Marker)
        axs[1,0].set_title('V vs P')
        axs[1,0].set(xlabel='P (W)', ylabel = 'Voltage (V)') 
        
        if i >5:
            m, m_var, b, b_var = LinearFit(data['Power'],data['Voltage'])
            axs[1,1].scatter(i,m,marker=Marker)
            axs[1,1].set(xlabel='Iteration',ylabel='Slope (V/W)')
        
        

        plt.pause(0.005)
        plt.tight_layout()
        #print(pow_punc)
    
#ard.close()
#PM.close()    
# =============================================================================
# POS = np.array(POS)
# POW = np.array(pow_punc)[:,0]
# VOL = np.array(vol)[:,0]
# PUNC = np.array(pow_punc)[:,1]
# PWRPOSdata = pd.DataFrame({"position":POS, "power":POW, 'punc':PUNC})
# PWRVOLdata = pd.DataFrame({"power":POW, 'voltage':VOL})
# VOLPOSdata = pd.DataFrame({"position":POS, 'voltage':VOL})
# PWRVOLdata.to_csv(f'C:/Users/neogi/Desktop/Collins, Mercedes/PWRVOL_{wavelength}_{date}.csv')
# PWRPOSdata.to_csv(f'C:/Users/neogi/Desktop/Collins, Mercedes/PWRPOS_{wavelength}_{date}.csv')
# VOLPOSdata.to_csv(f'C:/Users/neogi/Desktop/Collins, Mercedes/VOLPOS_{wavelength}_{date}.csv')
# =============================================================================
data = pd.DataFrame(data)
data.to_csv(f'C:/Users/neogi/Desktop/Collins, Mercedes/VOLPOS_{wavelength}_{date}.csv')

# Dictionaries
#thing ={"Position":Pos, "Power": ?? ,"error":??}
#arr = np.array([thing[k] for k in ("Position","Power","error")]).T

#numpy arrays
#POS = np.array([POS])
#Pow_err = np.array(Pow_err)
#np.concatenate((Pow_err, POS.T), axis=1)

#%%
# =============================================================================
# 
# PowerMeterSet(wavelength,True)
# POS = []
# POW  []
# =============================================================================
 