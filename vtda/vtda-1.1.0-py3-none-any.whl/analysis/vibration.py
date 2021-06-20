# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 16:59:57 2021

@author: ZSL
"""
import numpy as np
import math
import pandas as pd

def choose_windows(name='hanning', N=512,fix_meth='幅值修正'):
    '''
    本函数用来生成窗函数和修正系数
    修正方式分为能量修正和幅值修正   

    Parameters
    ----------
    name : TYPE, optional
        穿函数名. The default is 'hanning'.
    N : TYPE, optional
        生成数据的长度. The default is 512.
    fix_meth : TYPE, optional
        修正方式. The default is '幅值修正'.

    Returns
    -------
    np格式的窗函数
    '''

# Rect/Hanning/Hamming
    if name == 'hamming':
        window =np.hamming(N) 
        xishu_fuzhi=1.85
        xishu_nengliang=1.59
        if fix_meth=='幅值修正':
            res_xishu=xishu_fuzhi
        elif fix_meth=='能量修正':
            res_xishu=xishu_nengliang   
        #np.array([0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1)) for n in range(N)])
    elif name == 'hanning':
        window=np.hanning(N)
        xishu_fuzhi=2
        xishu_nengliang=1.63
        if fix_meth=='幅值修正':
            res_xishu=xishu_fuzhi
        elif fix_meth=='能量修正':
            res_xishu=xishu_nengliang        
        #window = np.array([0.5 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) for n in range(N)])
    elif name == 'rect':
        window = np.ones(N)
        xishu_fuzhi=1
        xishu_nengliang=1
        if fix_meth=='幅值修正':
            res_xishu=xishu_fuzhi
        elif fix_meth=='能量修正':
            res_xishu=xishu_nengliang
    return window*res_xishu

def fft(y,sample_rate =4096,fft_size = 4096,window='hanning',cdxs=0.75,fix_meth='幅值修正',meth='线性平均'):
    '''
    傅里叶变换函数
    :param x: 为输入数据
    :param sample_rate: 数据采样率
    :param fft_size: 分析点数，默认为512Hz    
    :param cdxs: 重叠系数,默认为0.75 
    单独运算fft采用幅值修正，计算倍频程及振级采用能量修正
    '''
    #fft_size=len(y)
    try:
        y=y.dropna()
        y=y.fillna(0) 
        y=np.array(y)        
    except:
        pass
    n_zong=max(math.ceil((len(y)-fft_size)/((1-cdxs)*fft_size))+1,1)#上取整
    res=np.zeros(int(fft_size/2))
    #fix_meth='能量修正'
    #del res_y
    y=y-y.mean()
    res=[]
    for i in np.arange(n_zong):
        pass

        y_=y[int(i*(1-cdxs)*fft_size):int(i*(1-cdxs)*fft_size+fft_size)][:int(fft_size)]   
        if len(y_)>0:        
            N=fft_size
            fft_y=np.abs(np.fft.fft(y_*choose_windows(name=window,N=len(y_),fix_meth=fix_meth)))/(0.5*len(y_))
            res.append(fft_y)
    
            # try:
            #     res_y=(fft_y+res_y)/2
            # except:
            #     #第一次没有平均值 
            #     res_y=fft_y
            try:  #经测试先计算最后统一平均的方式和dasp频率特性一致，所以
                res_y+=fft_y[range(int(N/2))]
            except:
                #第一次没有平均值 
                res_y=fft_y[range(int(N/2))]
    # aa=pd.DataFrame(res).T
    # with pd.ExcelWriter(dir_+'/test_fft.xlsx') as writer:
    #     aa.to_excel(writer, sheet_name='计算时间')  
    res_y=res_y/n_zong
    # pd.DataFrame(asd).plot()        
    res_y[0]=res_y[0]/2
    # if n_zong>1:
    #     rms_z=np.sqrt(np.sum([ i*i for i in y])/(len(y)+1))
    #     rms_av=rms_z
    #     rms_1=np.sqrt(sum(res_y[range(int(N/2))]*res_y[range(int(N/2))])/2)
    #     xishu=rms_av/rms_1
    #     res_y=res_y*xishu
    #     # np.sqrt(sum(res_y1*res_y1)/2)
    #     # np.sqrt(np.sum([ i*i for i in res_y1])/2)
    #     #res_y=np.sqrt(res_y[range(int(N/2))]/n_zong)#/((n_zong-1)*(cdxs))#n_zong/np.sqrt(2)
    # else:
    #     res_y=res_y[range(int(N/2))]
    res_x=np.linspace(0,sample_rate/2,int(fft_size/2) )
    return list(res_x),list(res_y)#pd.DataFrame({'frac':res_x,'fft':res_y}).set_index('frac')


def octave_3(y, sample_rate=4096,fft_size = 4096, window='hanning',cdxs=0.75,meth='线性平均',base=0.000001,res_type='db'):
    #x=aaaa[28]
    fl=1 #默认起始频谱
    fh=sample_rate/2 #默认截止频率
    #倍频程中心频率计算有两种方法：以2或者10为基底计算 但是两种方法各有利弊，在个别频段均不是整数
    #iso266对中心频率进行了取整规定，故不在进行计算，直接引用标准
    fc_base = [1,1.25,1.6,2,2.5,3.15,4,5,6.3,8] #1/3倍频程中心频率 基础频率值  其余在此基础上乘10扩展即可
    cf=fc_base+[i*10 for i in fc_base]+[i*100 for i in fc_base]+[i*1000 for i in fc_base]+[i*10000 for i in fc_base]
    cf=[i for i in cf if i<fh ]
    lf=[i/(2**(1/6)) for i in cf]        
    rf=[i*2**(1/6) for i in cf]    
    
    res_x,res_y_=fft(y,
                     sample_rate=sample_rate,
                     fft_size =fft_size,
                     cdxs=cdxs,
                     fix_meth='能量修正',
                     window=window,
                     meth=meth)
    res_y=[]
    res_x=np.array(res_x)
    res_y_=np.array(res_y_)
    for i in range(len(cf)):
        pass
        ibf= np.where((res_x >= lf[i]) & (res_x < rf[i])) 
        rms=np.sqrt(np.sum([ i*i for i in res_y_[ibf]])/2)
        if res_type=='db':
            if rms>0:
                res_y.append(20*math.log10(rms/base))
            else:
                res_y.append(0)
        elif res_type=='线性':
            res_y.append(rms)
    return cf,res_y

zweight_13341_1992_=[-6,-5,-4,-3,-2,-1,-0,0,0,0,
         -2,-4,-6,-8,-10,-12,-14,-16,-18,-20]  #ISO2631/1-1985  / GB/T13341-1992

def vl_z(y, zweight=zweight_13341_1992_,sample_rate=4096,fft_size = None,fft_len=None, window='hanning',cdxs=0.5):
    '''
    计算Z振级函数
    Parameters
    ----------
    y : TYPE
        待计算数据，可以为np.ndarray或者 pd.Series格式
    zweight : TYPE, optional
        计权曲线，默认为 #ISO2631/1-1985  / GB/T13341-1992 曲线
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
    
    #y=aa[1]  res_tigui_acce_21_24['que_dan'][21][300:2000]['que0']
    if isinstance(y, pd.DataFrame) or isinstance(y, pd.Series):
        sample_rate=1/(y.index[1]-y.index[0])
        y=y.fillna(0)
        y=np.array(y)        
    elif isinstance(y, np.ndarray):
        pass
    else:
        print("{} vl_z函数：错误数据输入格式。。。".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))             
    if fft_size == None :  #不输入分析点数默认
       fft_size= sample_rate
    n_zong=max(math.ceil((len(y)-fft_size)/((1-cdxs)*fft_size))+1,1)#上取整
    res=np.zeros(int(fft_size/2))
    vl_z=[]
    vl_zonethirds2=[]
    y_z=[]

    for i in np.arange(n_zong):
        pass
        y_=y[int(i*(1-cdxs)*fft_size):int(i*(1-cdxs)*fft_size+fft_size)][:int(fft_size)] 
        if len(y_)>0:
            res_x,onethird=octave_3(y_,
                                    sample_rate =sample_rate,
                                    fft_size = fft_size,
                                    cdxs=cdxs,
                                    window=window,
                                    res_type='db'
                                    )
            # if len(res_x)>=len(zweight):
            #     zweight=zweight+[0]*(len(res_x)-len(zweight))
            # else:
            #     zweight=zweight[:len(res_x)]
            if len(res_x)>=len(zweight):
                onethird=onethird[:len(zweight)]#zweight+[0]*(len(res_x)-len(zweight))
            else:
                onethird=onethird+[0]*(len(zweight)-len(res_x))
                    
            vl_zonethird=10**((np.array(zweight)+np.array(onethird))*0.1)          
            vl_z_=10*math.log10(sum(vl_zonethird)) 
            vl_z.append(vl_z_)
            deta_x=(fft_size/sample_rate)*(cdxs)
    res_x=np.linspace(0,deta_x*n_zong,n_zong)              
    return list(res_x),vl_z




if __name__ == '__main__':

    import matplotlib.pyplot as plt
    import matplotlib    
    sample_rate=200
    t_s = 1/sample_rate
    t_start = 0
    t_end = 5
    t = np.arange(t_start, t_end, t_s)
    
    f0 = 5
    f1 = 20
    
    # generate the orignal signal
    y = 1.5*np.sin(2*np.pi*f0*t) + 3*np.sin(2*np.pi*f1*t) #+ np.random.randn(t.size)
    
    # fft
    res1=np.fft.fft(y_*choose_windows(name=window,N=len(y_),fix_meth=fix_meth))
    res1=np.abs(res1)
    res2=res1[range(int(len(res1)/2))]
    res3=res2/len(res2)
    res_x=np.linspace(0,sample_rate/2,int(len(res1)/2))
    
    a,b=fft(y,sample_rate =sample_rate,fft_size = sample_rate,window='rect',cdxs=0.75,fix_meth='幅值修正',meth='线性平均')
        
    
    plt.figure(figsize=(15, 12))
    plt.subplot(511)
    plt.plot(t,y)
    plt.subplot(512)
    plt.plot(res_x,res2)    
    plt.subplot(513)
    plt.plot(res_x,res3) 
    plt.subplot(514)
    plt.plot(a,fft_y[range(int(N/2))]) 
    plt.subplot(515)
    plt.plot(a,b)       
    
    import vtda
    dir_='D:/quant/git/vtda/vtda/test/test_data_dasp'
    name='20210227南宁地铁2号线上行16+018啊'
    data,info=vtda.read_dasp_data(name,dir_=dir_)
    i=10
    j=4
    a,b=fft(data[i][j],sample_rate =float(info[i][j]['采样频率']),fft_size = float(info[i][j]['采样频率']),window='rect',cdxs=0.75,fix_meth='幅值修正',meth='线性平均')
    plt.plot(a,b)  
    a,b=octave_3(data[i][j],sample_rate =float(info[i][j]['采样频率']),fft_size = float(info[i][j]['采样频率']),window='rect',cdxs=0.75,meth='线性平均')

    plt.figure(figsize=(15, 12))
    plt.plot(a,b) 
    plt.semilogx()
    
    vl_zonethird=10**(np.array(b)[:20]*0.1)          
    vl_z_=10*math.log10(sum(vl_zonethird)) 
    y=data[i][j]
    a,b=vl_z(data[i][j],sample_rate=float(info[i][j]['采样频率']),window='hanning',cdxs=0.75)    
    plt.figure(figsize=(15, 12))
    plt.plot(a,b)    