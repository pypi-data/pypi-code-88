# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 08:00:45 2021

@author: ZSL
"""
import numpy as np
import math
import pandas as pd
import datetime 
import time 
import os
import re

from vtda.analysis.vibration import vibration_level

from vtda.analysis.base import (               choose_windows,
                                               fft,
                                               octave_3,
                                               rms_time,
                                               rms_frec,
                                            )
from vtda.read_data.read_dasp import (
                                               read_dasp_data_single,
                                               read_dasp_data
                                            )
from vtda.util.util import fix_num
from tqdm import tqdm         


def handle_vibration_data(data,info,name,dir_,realtime_save=False,cdxs=0.75,num_shiyan='all',num_tongdao='all'):
    '''
    Parameters
    ----------
    data : TYPE, optional
        数据文件. The default is None.
    info : TYPE, optional
        数据信息. The default is None.
    name : TYPE, optional
        文件名，不要加试验号. The default is None.
    dir_ : TYPE, optional
        路径. The default is None.        
    realtime_save : TYPE, optional
        实时数据保存，此功能目前未启用 The default is False.
    cdxs : TYPE, optional
        重叠系数. The default is 0.75.
    num_shiyan : TYPE, optional
        要计算的试验号，默认为'all'，如果需要读取部分可输入:'3,5,6-8'.
    num_tongdao : TYPE, optional
        要计算的通道号，默认为'all'，如果需要读取部分可输入:'3,5,6-8'.        
    Returns
    -------
    None.

    '''

    if isinstance(num_shiyan, list):
        print('试验号格式输入错误，请输入str格式')
        return None,None
    elif isinstance(num_shiyan, str) and num_shiyan!='all':
        num_shiyan=fix_num(num_shiyan)
        data_={}
        for i in data:
            pass
            if i in num_shiyan:
                data_[i]=data[i]
        data=data_
    if isinstance(num_tongdao, list):
        print('通道号格式输入错误，请输入str格式')
        return None,None
    elif isinstance(num_tongdao, str) and num_tongdao!='all':
        num_tongdao=fix_num(num_tongdao)  
        data_={}
        for i in data:
            pass
            data_[i]={}
            for j in data[i]:
                if j in num_tongdao:
                    data_[i][j]=data[i][j]
        data=data_        

    # if dir_==None:
    #     print("{} 未指定文件路径，读取失败。。。".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))         
    if dir_:
        pass   
    else:  #不指定目录则执行当前工作目录
        dir_=os.getcwd()    
    res_vlz_detail={}
    res_vlz_summarize={}    
    res_octave_3={}
    res_fft={}
    window='hanning'  #汉宁窗rect
    #计算Z振级   
    t1=time.time()
    #print("{} 正在计算Z振级。。。".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))                
    for i in tqdm(data,desc='正在计算Z振级'):
        pass
        df=data[i]
        info_=info[i]
        res_vlz_detail_=[]
        columns_=[]
        res_vlz_summarize_=[['平均数','最小值','25%分位数','50%分位数','75%分位数','最大值']]       
        for j in df:
            pass
            frec,vlz=vibration_level(df[j],sample_rate=float(info_[j]['采样频率']),window=window,cdxs=cdxs)
            if len(res_vlz_detail_)==0: #第一次需要把频率加上
                res_vlz_detail_.append(frec)
            columns_.append(j)
            res_vlz_detail_.append(vlz)
            res_vlz_summarize_.append([np.array(vlz).mean(),
                                      np.array(vlz).min(),
                                      np.percentile(np.array(vlz),25),
                                      np.percentile(np.array(vlz),50),
                                      np.percentile(np.array(vlz),75),                                      
                                      np.array(vlz).max()])        
        try:  
            ls1=pd.DataFrame(res_vlz_detail_).T.set_index(0)  
            ls1.columns=columns_
            res_vlz_detail[i]=ls1
            ls2=pd.DataFrame(res_vlz_summarize_).T.set_index(0) 
            ls2.columns=columns_
            res_vlz_summarize[i]=ls2
            
        except:
            print("{} 试验号：{}，计算Z振级错误。。。".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),i))             

    res_vlz_summary=pd.DataFrame()
    ls_num=[]
    res_vlz_summarize_={}
    for i in res_vlz_summarize:
        pass           
        res_vlz_summarize_[i]=res_vlz_summarize[i]

    for i in res_vlz_summarize_:
        pass
        ls_num.append(int(i)) 
        res_vlz_summary=pd.concat([res_vlz_summary,res_vlz_summarize_[i].iloc[[-1],:]],axis=0)
    res_vlz_summary=pd.concat([res_vlz_summary,pd.DataFrame(res_vlz_summary.min()).T],axis=0)
    res_vlz_summary=pd.concat([res_vlz_summary,pd.DataFrame(res_vlz_summary.max()).T],axis=0)
    res_vlz_summary=pd.concat([res_vlz_summary,pd.DataFrame(res_vlz_summary.mean().apply(lambda x:round(x,1))).T],axis=0)

    num_shiyan_start=min(ls_num)
    num_shiyan_end=max(ls_num)    
    ls_num.append('最小值')
    ls_num.append('最大值')
    ls_num.append('平均值')
    res_vlz_summary['试验号']=ls_num
    res_vlz_summary=res_vlz_summary.set_index('试验号')

   
    with pd.ExcelWriter(dir_+'/Z振级汇总('+str(num_shiyan_start)+'-'+str(num_shiyan_end)+')-'+name+'.xlsx') as writer:
        res_vlz_summary.to_excel(writer, sheet_name='Z振级汇总')  
    with pd.ExcelWriter(dir_+'/Z振级详细('+str(num_shiyan_start)+'-'+str(num_shiyan_end)+')-'+name+'.xlsx') as writer:
        for i in res_vlz_detail:
            res_vlz_detail[i].to_excel(writer, sheet_name=str(i))        
    t2=time.time()
    #print("{} 计算Z振级完成，耗时{}秒。。".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),round((t2-t1),2)) )               


    #计算频谱
    t1=time.time()
    #print("{} 正在计算倍频程和频谱。。。".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))                    
    res_vlz_time=[]
    for i in res_vlz_detail:
        pass
        aa=res_vlz_detail[i].diff()
        a=pd.DataFrame(aa.apply(lambda x: x[x==x.min()].index.values[0])).T
        min_=a.T.apply(pd.value_counts).reset_index().sort_values(by=0,ascending=False).loc[0,'index'] 
        a=pd.DataFrame(aa.apply(lambda x: x[x==x.max()].index.values[0])).T
        max_=a.T.apply(pd.value_counts).reset_index().sort_values(by=0,ascending=False).loc[0,'index']        
        res_vlz_time.append([i,max_,min_,(min_-max_)]) #最小值的时间在后面     
    res_vlz_time=pd.DataFrame(res_vlz_time)
    res_vlz_time.columns=['实验号','开始时间','结束时间','持续时间']   
    res_vlz_time=res_vlz_time.set_index('实验号')
    res_vlz_time=res_vlz_time.sort_index()
    for i in res_vlz_time.index:
        pass
        if res_vlz_time.loc[int(i),'开始时间']>res_vlz_time.loc[int(i),'结束时间']:
           ls=res_vlz_time.loc[int(i),'开始时间'] 
           res_vlz_time.loc[int(i),'开始时间']=res_vlz_time.loc[int(i),'结束时间']
           res_vlz_time.loc[int(i),'结束时间']=ls
           res_vlz_time.loc[int(i),'持续时间']=-res_vlz_time.loc[int(i),'持续时间']
           
    res_fft={}  
    for i in tqdm(data,desc='正在计算频谱'):
        pass
        df=data[i]
        res_fft_=[] 
        columns_=[]
        for j in df:
            pass
            sample_rate=float(info[i][j]['采样频率'])
            frec,fft_=fft(df[j][int(res_vlz_time.loc[i,'开始时间']*sample_rate):int(res_vlz_time.loc[i,'结束时间']*sample_rate)], 
                          sample_rate=sample_rate,
                          fft_size=sample_rate,
                          window=window,cdxs=cdxs)
            if len(res_fft_)==0: #第一次需要把频率加上
                res_fft_.append(frec)
            res_fft_.append(fft_)
            columns_.append(j)
        try: 
            ls1=pd.DataFrame(res_fft_).T.set_index(0)  
            ls1.columns=columns_
            res_fft[i]=ls1
        except:
            print("{} 计算倍频谱错误。。。".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))             

    with pd.ExcelWriter(dir_+'/频谱详细('+str(num_shiyan_start)+'-'+str(num_shiyan_end)+')-'+name+'.xlsx') as writer:
        res_vlz_time.to_excel(writer, sheet_name='计算时间')
        for i in res_fft:
            #print(i)                       
            res_fft[i].to_excel(writer, sheet_name=str(i))
    time.sleep(1)        
    t2=time.time()
    #print("{} 计算频谱完成，耗时{}秒。。".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),round((t2-t1),2)) )               
       

            
    #计算倍频程
    t1=time.time()            
    res_octave_3={}  
    for i in tqdm(data,desc='正在计算1/3倍频程'):
        pass
        df=data[i]
        res_octave_3_=[]        
        for j in df:
            pass
            sample_rate=float(info[i][j]['采样频率'])
            frec,octave_3_=octave_3(df[j][int(res_vlz_time.loc[i,'开始时间']*sample_rate):int(res_vlz_time.loc[i,'结束时间']*sample_rate)],
                                    sample_rate=sample_rate,
                                    fft_size=sample_rate,
                window=window,cdxs=cdxs)
            if len(res_octave_3_)==0: #第一次需要把频率加上
                res_octave_3_.append(frec)
            res_octave_3_.append(octave_3_)
        try:
            ls1=pd.DataFrame(res_octave_3_).T.set_index(0)     
            ls1.columns=columns_          
            res_octave_3[i]=ls1   
        except:
            print("{} 计算倍频程错误。。。".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))             
    
     
    with pd.ExcelWriter(dir_+'/倍频程详细('+str(num_shiyan_start)+'-'+str(num_shiyan_end)+')-'+name+'.xlsx') as writer:
        res_vlz_time.to_excel(writer, sheet_name='计算时间')  
        for i in res_octave_3:
            #print(i)                       
            res_octave_3[i].to_excel(writer, sheet_name=str(i))
    time.sleep(1)   
    t2=time.time()
    #print("{} 计算倍频程完成，耗时{}秒。。".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),round((t2-t1),2)) )               

if __name__ == '__main__':
           
    dir_='E:/南宁地下数据'
    name='20210227南宁地铁2号线上行16+018啊' 
    data,info=read_dasp_data(name,dir_)    
    handle_vibration_data(data,info) 