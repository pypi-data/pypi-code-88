# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 13:00:03 2020

@author: neogi
"""

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

def PowerThresh(samples,threshold):
    '''
    

    Parameters
    ----------
    samples : int
        number of samples to run consecutively.
    threshold : float
        Maximum allowed uncertainty in the measurement. If the set of power 
        values returned by Power() has an uncertainty value above threshold,
        the while loop will restart and try again until the uncertainty is 
        below threshold
    .

    Returns
    -------
    power : same as the function Power()
        See docstring for Power().

    '''
    power = Power(samples)
    
    while power[1]>threshold:
        power = Power(samples)
    
    return power

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


#%% Excecute Calibration

from time import sleep
ard.write('$H')
sleep(10)
wavelength = input("Enter Wavelength: ")
input("Block the Laser beam to set the powermeter to zero, then hit enter: ")
PowerMeterSet(wavelength,True)
input("Unblock the beam and hit enter: ")
sleep(1)

date = date.today()
data = {'Position':[], 'Power':[], 'Power_Uncertainty':[], 'Voltage':[],
        'Voltage_Uncertainty':[]}


samples = 10
threshold = 1*10**-3


plt.ion()

fig, axs = plt.subplots(nrows = 2, ncols = 2)

#tic = datetime.now()

for i in range(0,200,1):
    if i == 0:
        sleep(1)
    else:
        MoveArd(i,5000)
        sleep(.1)
        position = i
        #POS.append(position)
        data['Position'].append(position)
        power = PowerThresh(samples, threshold)
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
        
        if i >2:
            m, m_var, b, b_var = LinearFit(data['Power'],data['Voltage'])
            axs[1,1].scatter(i,m_var,marker=Marker)
            axs[1,1].set(xlabel='Iteration',ylabel=r'$\delta$Slope (Variance) (V/W)')

        plt.pause(0.005)
        plt.tight_layout()
#toc = datetime.now()

#print(f'Total Time = {tic-toc}')

DATA = pd.DataFrame(data)
DATA.to_csv(f'C:/Users/neogi/Desktop/Collins, Mercedes/PWRCAL{wavelength}_{date}.csv')

#%%

from scipy.interpolate import interp1d

data = pd.read_csv('PWRCAL325_2020-07-02.csv')
data = data[:200]


def P2A(power):
    Power2Angle = interp1d(data['Power'],data['Position'])  ###Power2Angle
    angle = float(Power2Angle(power))
    return angle

def ArdPower(power, speed=5000):
    pos = P2A(power)
    MoveArd(pos,speed)
    
def MoveThroughPowerSteps(start,stop,step):
    '''
    Start, Stop, and Step are given in mW
    

    Parameters
    ----------
    start : TYPE
        DESCRIPTION.
    stop : TYPE
        DESCRIPTION.
    step : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    ard.write('$H')
    sleep(10)
    
    for i in np.arange(start,stop,step):
        ArdPower(i/1000)
        sleep(5)
        print(f'Current Power = {i}mW \n ...................')
        #print(Power(10))
        input('>>>>>Press Enter for next step')
        
        
        
    
