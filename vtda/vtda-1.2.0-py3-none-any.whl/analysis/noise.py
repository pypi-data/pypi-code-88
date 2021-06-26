# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 17:11:14 2021

@author: ZSL
"""

import numpy as np
import math
import pandas as pd
import datetime 
import time 
import os
import re

from vtda.util.util import weight_factor
from vtda.analysis.vibration import vibration_level

from vtda.analysis.base import (               choose_windows,
                                               fft,
                                               octave_3,
                                               rms_time,
                                               rms_frec,
                                            )
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib
#解决中文乱码问题
plt.rcParams["font.sans-serif"]='SimHei'
#解决负号无法正常显示问题
plt.rcParams["axes.unicode_minus"]= False

def sound_pressure_level(y,
                         weight='weight_noise_a_3785_2010',
                         sample_rate=4096,
                         fft_size = None,
                         fft_len=None,
                         window='hanning',
                         cdxs=0.5,
                         frec=[10,20000],
                         n=1                       
                         ):
    '''
    计算A声级函数
    Parameters
    ----------
    y : TYPE
        待计算数据，可以为np.ndarray或者 pd.Series格式
    zweight : TYPE, optional
        计权曲线，默认为 #GB/T 3785.1-2010 曲线
    sample_rate : TYPE, optional
        采样点数，默认为4096，如果待计算数据为pd.Series格式，其中有采样频率信息，则优先采用其信息。
    fft_size : TYPE, optional
        分析点数，默认为采样点数，即分析窗长为1秒
    fft_len : TYPE, optional
        分析长度，默认为1秒  其和分析点数功能相同，输入一个即可，分析长度优先级高于分析点数
    window : TYPE, optional
        加窗，默认为汉宁窗
    cdxs : TYPE, optional
        重叠系数，默认为0.5

    Returns
    -------
    返回两个结果list，一个为时间，另一个为随时间变化的Z振级

    '''
    a,b=base_level(  y=y,
                     weight=weight,
                     sample_rate=sample_rate,
                     fft_size = fft_size,
                     fft_len=fft_len,
                     window=window,
                     cdxs=cdxs,
                     frec=frec,
                     n=n
                     )
    return a,b


    
if __name__ == '__main__':
    
    import vtda 
    dir_='D:/quant/git/vtda/test_data_dasp'
    name='20210227南宁地铁2号线上行16+018啊'
    data,info=vtda.read_dasp_data(name,dir_=dir_)
    i=10
    j=5
    y=data[i][j]
    a,b2=sound_pressure_level(data[i][j],
                        sample_rate=float(info[i][j]['采样频率']),
                        window='hanning',
                        cdxs=0.75)    
    plt.figure(figsize=(15, 12))
    plt.plot(a,b2) 