''' Signal processing routines - Sigproc
        developed by Victor Cossich (victor.cossich@gmail.com) and Conrado Torres (conradotl@gmail.com)
	for rate of torque development calculations. Email us if you want. ;)

	you need numpy,pandas,matplotlib and scipy.signal to run this module.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal as sig

def torque_filt(torque_signal,sf=1000,cf=50):
    '''
    torque_signal = torque signal for processing (pandas series)
    sf(optional) = sample frequency (Hz), default is 1000
    cf(optional) = critical frequency for the lowpass filter, default is 50
    return: filtered torque signal(pandas series)
    '''
# cria parametros do filtro
    b,a = sig.butter(N = 2, Wn = 50/(sf/2), btype = 'lowpass', output = 'ba')
# aplica filtro bidirecional
    filt_signal = sig.filtfilt(b,a,torque_signal)

    return filt_signal

###############################################################################

def onset(torque_signal,sf=1000,method='fixed',trigger=1,passive_correction=True, plot=True):
    '''
    Zoom in and click in the middle of a baseline region. Then zoom in the onset region, press any button and then click on 
        the point were the torque signal cross the horizontal dashed line
    torque_signal = torque signal for processing (pandas series)
    sf(optional) = sample frequency (Hz), default is 1000
    method(optional) = 'fixed' ,'baseline_noise' or 'absolute', default is 'fixed'
    trigger(optional) = torque value (fixed) or standart deviations (baseline_noise) for onset detection, default is 1
    passive_correction(optional) = remove baseline constant, default is True (Mainly for torque analysis)
    plot(optional) = plot the onset point (in red), default is True
    return: onset(index)
    '''
    fig,axes=plt.subplots(figsize=(23,15))
    axes.plot(torque_signal)
    axes.plot(torque_signal.values.argmax(), torque_signal.values.max(),'ro')
    plt.title('Zoom in, Press any button and click in the middle of a baseline period')
# Wait for a button press to enable ginput
    zoom_ready=False
    while not zoom_ready:
        zoom_ready=plt.waitforbuttonpress()
# hold baseline point
    p = plt.ginput(1)
    plt.close()
# cut a 500ms epoch centrered in the x coordinate of baseline point
    p_base = int(p[0][0])
    base = torque_signal[p_base-int(sf/4):p_base+int(sf/4)]   
# make baseline correction - speccialy fitted for passive torque correction   
    if passive_correction:
        torque_signal = torque_signal - base.mean()
        base = base - base.mean()
# Plot the visual aid for torque onset manual detection
    fig,axes=plt.subplots(figsize=(23,15))
    axes.plot(torque_signal)
    axes.plot(torque_signal.values.argmax(), torque_signal.values.max(),'ro')
    plt.title('De zoom na regiao de onset, pressione uma tecla qualquer e clique no ponto de onset')
    if method == 'fixed':
        # plots the fixed value above the baseline
        axes.axhline (np.mean(base) + trigger, c= 'r', ls = 'dashed')
    elif method == 'baseline_noise':
        # plots the limit fispersion of the baseline
        axes.axhline (np.mean(base) + trigger*np.std(base) , c= 'r', ls = 'dashed')
        axes.axhline (np.mean(base) - trigger*np.std(base) , c= 'r', ls = 'dashed')
    elif method == 'absolute':
        # plots the absolute trigger value
        axes.axhline (trigger, c= 'r', ls = 'dashed')
# Wait for a button press to enable ginput
    zoom_ready=False
    while not zoom_ready:
        zoom_ready=plt.waitforbuttonpress()    
# hold the onset point and close figure
    p = plt.ginput(1)
    plt.close()   
    p_onset = int(p[0][0])
# plot figure with the onset
    if plot:
        fig,axes=plt.subplots(figsize=(15,5))
        axes.plot(torque_signal)
        axes.plot(p_onset,torque_signal[p_onset],'ro')  
    
    return p_onset

###############################################################################

def RTD(torque_signal,onset,ID='ID',membro='limb',sf=1000,instantaneous=True,sucessive=True):
    '''
    torque_signal = torque signal for processing (pandas series)
    onset = index of torque onset
    ID(optional) = subject ID, default is 'ID'
    member(optional) = member analyzed, e.g. dominant or non-dominant, default is 'limb'
    fa(optional) = sample frequency (Hz), default is 1000
    instantaneous(optional) = if true, return the peak RTD (rate of torque development), time to peak RTD and,
        MVC (maximum voluntary contraction torque) normalized peak RTD, default is True
    sucessive(optional) = if True, return the RTD in 50ms windows from 50-100 to 200-250, default is True
    return: dataframe with ID, MVC, RTD and MVC normalized RTD from 50 to 250 ms and the other variables specified
    '''
# trimm a 3s epoch from torque onset
    torque_signal=torque_signal[onset:onset+3*sf].reset_index(drop=True)
# hold MVC value
    MVC=np.max(torque_signal)
# Make list for the RTD variables
    rtd=[]
    nrtd=[]
# Calculate RTD in the addiive time windows and append to the lists
    for i in [50,100,150,200,250]:
        F = torque_signal[int(sf/1000*i)]
        RTD = F/(1/1000*i)
        nRTD=RTD/MVC
        rtd.append(RTD)
        nrtd.append(nRTD)
# Create dicts with the obtained variables
    rtd_var_names=['ID','membro','MVC','RTD50','RTD100','RTD150','RTD200','RTD250','nRTD50','nRTD100','nRTD150','nRTD200','nRTD250']
    rtd_var_val=[ID]+[membro]+[MVC]+rtd+nrtd
    rtd_data=dict(zip(rtd_var_names,rtd_var_val))
# Calculate instantaneous RTD
    if instantaneous:
        irtd = np.diff(torque_signal)*sf
#  Peak RTD(pRTD),time to pRTD(TpRTD),normalized pRTD(npRTD)
        pRTD = irtd.max()
        TpRTD = irtd.argmax()
        npRTD = pRTD/MVC
# make a dict with instantaneous RTD and update the previous variable dict 
        irtd_var_names=['pRTD','TpRTD','npRTD']
        irtd_var_val=[pRTD,TpRTD,npRTD]
        irtd_data=dict(zip(irtd_var_names,irtd_var_val))
        rtd_data.update(irtd_data)
# Calculate sucessive time windows RTD
    if sucessive:
# Make list for sucessive RTD variables
        srtd=[]
        snrtd=[]
# calcuate RTD in specified time windows
        for i in [(50,100),(100,150),(150,200),(200,250)]:
            F = torque_signal[int(sf/1000*i[1])]-torque_signal[int(sf/1000*i[0])]
            RTD = F/(1/1000*(i[1]-i[0]))
            nRTD=RTD/MVC
            srtd.append(RTD)
            snrtd.append(nRTD)
# Create dicts with the obtained variables
        srtd_var_names=['RTD50_100','RTD100_150','RTD150_200','RTD200_250','nRTD50_100','nRTD100_150','nRTD150_200','nRTD200_250']
        srtd_var_val=srtd+snrtd
        srtd_data=dict(zip(srtd_var_names,srtd_var_val))
# Updat the previous variable dict
        rtd_data.update(srtd_data)
# Make a dataframe of the dict        
    data = pd.DataFrame(rtd_data,index=[0])
    
    return data
 
###############################################################################    
    
def EMGfilt(emg_signal,sf=1000):
    '''
    Apply a series of low and highpass , in addition to notch filters according to 
    Mello, Oliveira and Nadal papper(10.1016/j.cmpb.2007.04.004)
    emg_signal = emg signal for processing (pandas series) 
    return: Filtered emg signal
    '''
    b_param=[]
    a_param=[]
# band pass Filter parameters
    b1,a1 = sig.butter(N = 2, Wn = 10, btype = 'highpass', output = 'ba', fs=sf)
    b2,a2 = sig.butter(N = 8, Wn = 400, btype = 'lowpass', output = 'ba', fs=sf)
    b_param.extend([b1,b2])
    a_param.extend([a1,a2])
# knotch filters parameters
    for freq in range(60,361,60):
        b,a=sig.butter(N = 2, Wn = (freq-1,freq+1), btype = 'bandstop', output = 'ba', fs=sf)
        b_param.append(b)
        a_param.append(a)
# Convolution over high and low parameters
    b=sig.convolve(b_param[0],b_param[1])
    a=sig.convolve(a_param[0],a_param[1])
# Convolution over harmonic parameters    
    for b_,a_ in zip(b_param[2:],a_param[2:]):
        b=sig.convolve(b,b_)
        a=sig.convolve(a,a_)
# aplly filter
    filtered=sig.filtfilt(b,a,emg_signal)
    
    return filtered

###############################################################################

def RMS(emg_signal):
    '''
    emg_signal = signal for processing
    return: Root mean square of the signal
    '''
    rms = np.sqrt(sum(emg_signal**2)/len(emg_signal))
    
    return rms

###############################################################################
    
def EMG50(emg_signal,torque_signal,torque_onset,sf=1000):
    '''
    emg_signal = emg signal for processing
    torque_signal = sincronized torque signal
    torque_onset = index of torque signal
    sf = sample frequency, assumed to be equal for both emg and torque signals
    return = rms of the 50ms preceding torque onset normalized by the rms of the 500 ms epoch centered in the
    maximum torque point, the rms 500 ms epoch centered in the maximum torque point
    '''
    # define the point of maximum torque and select a centered 500 ms epoch
    p_MVC = torque_signal.values.argmax()
    emg_mvc = emg_signal[p_MVC-(int( sf *0.250)):p_MVC+(int( sf *0.250))] 
# calculate the rms of the emg signal on that epoch
    emg_max = RMS(emg_mvc)
# select the 50ms epoch preceding torque onset and alculate the rms of the emg signal
    emg50_array = emg_signal[torque_onset-(int( sf *0.050)):torque_onset]
    emg50 = RMS(emg50_array)/emg_max
    
    return emg50, emg_max

###############################################################################
    
    
    
    
    
    
    
    
    
    
    
    
    
    