# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 14:09:16 2021

@author: ZSL
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math
import pandas as pd
from scipy import signal
from mpl_toolkits.mplot3d import Axes3D
import os #os.path.abspath('.')#获得当前工作目录 #os.path.abspath('..')#获得当前工作目录的父目录
from sys import path
import glob
import datetime 
import time
import struct
import re
#https://matplotlib.org/users/index.html
#解决中文乱码问题
plt.rcParams["font.sans-serif"]='SimHei'
#解决负号无法正常显示问题
plt.rcParams["axes.unicode_minus"]= False

work_path=os.getcwd()
dir_=r"/".join(work_path.split("\\")) #"D:\\ANSYS\\20190718jietou" 
name_=os.listdir() #列出所有文件

def read_dasp_data(name,dir_=None):
    '''
    读取dasp文件（文件夹内所有文件）
    文件名仅需要指定到实验名即可，不需要到试验号和通道号,
    比如：  name='20210227南宁地铁2号线上行16+018啊'
    而不是：name='20210227南宁地铁2号线上行16+018啊10#3'
    返回为：通道数值dict格式，通道信息dict格式
    ''' 
    #name='20210227南宁地铁2号线上行16+018啊'
    # if dir_==None:
    #     print("{} 未指定文件路径，读取失败。。。".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))         

    os.chdir(dir_) #切换到指定目录 
    name_=os.listdir() #列出所有文件 
    re_obj = re.compile(r"\d+")		#创建正则表达式对象   
    shiyanhao= list(set([int(re_obj.findall(s)[-2]) for s in name_ if name in s])) #选出试验号    
    cedianhao= list(set([int(re_obj.findall(s)[-1]) for s in name_ if name in s])) #选出测点号   

    res_sts={}         
    res_tsp={}
        
    for i in shiyanhao:
        pass
        res_sts[i]={}
        res_tsp[i]={}        
        for j in cedianhao:
            pass
            data_sts,data_tsp=read_dasp_data_single(name+str(i)+'#'+str(j),dir_=dir_)            
            res_sts[i][j]=np.array(data_sts)/float(data_tsp['灵敏度'])
            res_tsp[i][j]=data_tsp
    
    return res_sts,res_tsp
                       
        #     data=pd.DataFrame(np.array(data_sts)/float(data_tsp['灵敏度']),columns=[j])
        #     res=pd.concat([res,data],axis=1)
        #     res=res.sort_index(axis=1, ascending=True) 
            
        # res_time=pd.DataFrame({'time':
               
        #         np.arange(0,len(data_sts)/float(data_tsp['采样频率']),1/float(data_tsp['采样频率'])),
        #          })
        # res=pd.concat([res_time,res],axis=1)  
        # res=res.set_index('time')
        # res_sts[name+str(i)]=res

def read_dasp_data_single(name,dir_=None):
    '''
    读取单个dasp文件（单通道数据），需要给定路径和文件名
    文件名需要指定到试验号及通道号,比如：name='20210227南宁地铁2号线上行16+018啊10#3'
    返回为：通道数值list格式，通道信息dict格式
    '''
    tsp=read_dasp_tsp_data(name=name,dir_=dir_)    
    sts=read_dasp_sts_data(name=name,dir_=dir_)
    return sts,tsp        

def read_dasp_sts_data(name,dir_=None):
    '''
    读取单个sts文件（单通道数据），需要给定路径和文件名
    返回为通道数值list格式
    '''
    #name='人民路至紫金山减振垫10#1'
    data_file = open(dir_+'/'+name+'.sts', 'rb')
    data_temp = data_file.read()
    #a=struct.pack('<f', 0.000000019)
    res=[]
    for i in range(int(len(data_temp)/4)):
        s=data_temp[i*4:i*4+4]
        data_short, = struct.unpack('<f', s)
        res.append(data_short)
    return res

# data_file = open(dir_+'/人民路至紫金山减振垫10#1Waveform.TXT', 'rb')
# data_temp2 = data_file.readlines()
# res2=[]
# for i in data_temp2:
#     pass
#     res2.append(float(i.split()[-1]))

# np.array(res[:1000])/np.array(res2[:1000])

def read_dasp_tsp_data(name,dir_=None):
    '''
    读取单个tsp文件（单通道数据），需要给定路径和文件名
    返回为通道信息dict格式
    '''    
    #name=name_tsp[2]
    data_file = open(dir_+'/'+name+'.tsp', 'r')
    data_temp = data_file.read() #readlines()
    line1=data_temp.split('[')[0].split(',')
    line2=line1[-1].split('\n') 
    res={
        '采样频率':line1[0],
        '样本点数':int(line1[2])*512,
        '总通道数':line1[6],
        '灵敏度':line1[7],
        '工程单位':line2[0].split('"')[1],
        '测点描述': data_temp[1][:-2] if len(data_temp[1])>1 else None,
        '试验工况描述': data_temp[2][:-2] if len(data_temp[2])>1 else None, 
        '试验对象描述': data_temp[3][:-2] if len(data_temp[2])>1 else None,        
        }    
    data_=data_temp.split('[')
    for i in data_:
        pass
        if i[:6]=='Source':
            pass
        elif i[:9]=='Reference':
            pass 
        elif i[:7]=='GpsInfo':
            pass 
        elif i[:17]=='SampleChannelPara':
            pass 
        elif i[:15]=='SampleStartPara':
            pass  
        elif i[:6]=='AppVer':
            pass        

    return res

if __name__ == '__main__':
    dir_='D:/quant/git/vtda/vtda/test/test_data_dasp'
    name='20210227南宁地铁2号线上行16+018啊10#3'
    tsp=read_dasp_tsp_data(name=name,dir_=dir_)
    
    name='20210227南宁地铁2号线上行16+018啊10#3'
    sts=read_dasp_sts_data(name=name,dir_=dir_)

    a,b=read_dasp_data_single(name=name,dir_=dir_)
    
    name='20210227南宁地铁2号线上行16+018啊10#3'
    a,b=read_dasp_data(name,dir_=dir_)

    
