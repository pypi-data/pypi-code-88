# In[0] Import necessary packages 
import pandas as pd
import numpy as np
import csv

import datetime

from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
from .setting import *

import matplotlib.pyplot as plt
plt.rc('font',family='Times New Roman')
plt.rc('font',size=10)

g_number_of_plink=0
g_plink_id_dict={}
g_plink_nb_seq_dict={}
g_parameter_list=[]
g_vdf_group_list=[]


def _mkdir(path):
    import os
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
 
    if not isExists:
        os.makedirs(path) 
        print (path+' create the folder sucessfully')
        return True
    else:
        print (path+' the folder already exists')
        return False


def _convertTimeToMinute(hhmm_time_interval):
    start_time=datetime.datetime.strptime(hhmm_time_interval.split('_')[0][:2]+':'+hhmm_time_interval.split('_')[0][2:], '%H:%M')
    start_time_minute=start_time.hour*60+start_time.minute
    return start_time_minute



# In[1] input data
def _readInputData(link_performance_file, ft_list, at_list):
    data_df=pd.read_csv(link_performance_file,encoding='UTF-8') # create data frame from the input link_performance.csv
    if (ft_list != 'all') & (at_list != 'all'):
        data_df=data_df[data_df['FT'].isin(ft_list) & data_df['AT'].isin(at_list)]
    elif (ft_list == 'all') & (at_list != 'all'):
        data_df= data_df[data_df['AT'].isin(at_list)]
    elif (at_list == 'all') & (ft_list != 'all'):
        data_df= data_df[data_df['FT'].isin(ft_list)]

    data_df =data_df.drop(data_df[(data_df.volume == 0) | (data_df.speed == 0)].index) # drop all rows that have 0 volume or speed
    data_df.dropna(axis=0, how='any',inplace=True) # drop all rows that have any null value
    data_df.reset_index(drop=True, inplace=True)  # reset the index of the dataframe
    # Calculate some derived properties for each link
    data_df['volume_per_lane']=data_df['volume']/data_df['lanes'] # add an additional column volume_per_lane in the dataframe
    data_df['hourly_volume_per_lane']=data_df['volume_per_lane']*(60/TIME_INTERVAL_IN_MIN) # add an additional column hourly_volume_per_lane
    # in the link_performance.csv, the field "volume" is link volume within the time interval 
    data_df['density']=data_df['hourly_volume_per_lane']/data_df['speed'] # add an additional column density
    return data_df

# In[2] Traffic flow models and volume delay function (BPR function)
def _density_speed_function(density,free_flow_speed,critical_density,mm):# fundamental diagram model (density-speed function): 
    # More informantion the density-speed function: https://www.researchgate.net/publication/341104050_An_s-shaped_three-dimensional_S3_traffic_stream_model_with_consistent_car_following_relationship
    k_over_k_critical=density/critical_density
    denominator=np.power(1+np.power(k_over_k_critical,mm),2/mm)
    return free_flow_speed/denominator

def _volume_speed_func(x,ffs,alpha,beta,critical_density,mm): # fundamental diagram  (volume_delay fuction) 
    # 1. input: assigned volume 
    # 2. output: converted volume on S3 model 
    speed=_bpr_func(x,ffs,alpha,beta)
    kernal=np.power(np.power(ffs/speed,mm),0.5)
    return speed*critical_density*np.power(kernal-1,1/mm)

def _bpr_func(x,ffs,alpha,beta): # BPR volume delay function input: volume over capacity
    return ffs/(1+alpha*np.power(x,beta))

# In[3] Calibrate traffic flow model 
def _calibrate_traffic_flow_model(vdf_training_set,vdf_index,subfolder):
    # 1. set the lower bound and upper bound of the free flow speed value 
    lower_bound_FFS=vdf_training_set['speed'].quantile(0.6) # Assume that the lower bound of freeflow speed should be larger than the mean value of speed
    upper_bound_FFS=np.maximum(vdf_training_set['speed'].quantile(0.95),lower_bound_FFS+0.1)  
    # Assume that the upper bound of freeflow speed should at least larger than the lower bound, and less than the maximum value of speed

    # 2. generate the outer layer of density-speed  scatters 
    vdf_training_set_after_sorting=vdf_training_set.sort_values(by = 'speed') # sort speed value from the smallest to the largest 
    vdf_training_set_after_sorting.reset_index(drop=True, inplace=True) # reset the index
    step_size=np.maximum(1,int((vdf_training_set['speed'].max()-vdf_training_set['speed'].min())/LOWER_BOUND_OF_OUTER_LAYER_SAMPLES)) # determine the step_size of each segment to generate the outer layer 
    X_data=[]
    Y_data=[]
    for k in range(0,int(np.ceil(vdf_training_set['speed'].max())),step_size):
        segment_df = vdf_training_set_after_sorting[(vdf_training_set_after_sorting.speed<k+step_size)&(vdf_training_set_after_sorting.speed>=k)]
        Y_data.append(segment_df.speed.mean())
        threshold=segment_df['density'].quantile(OUTER_LAYER_QUANTILE)
        X_data.append(segment_df[(segment_df['density']>=threshold)]['density'].mean())
    XY_data=pd.DataFrame({'X_data':X_data,'Y_data':Y_data})
    XY_data=XY_data[~XY_data.isin([np.nan, np.inf, -np.inf]).any(1)] # delete all the infinite and null values 
    if len(XY_data)==0:
        print('WARNING: No available data within all speed segments')
        exit()
    density_data =XY_data.X_data.values
    speed_data = XY_data.Y_data.values
    # 3. calibrate traffic flow model using scipy function curve_fit. More information about the function, see https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.optimize.curve_fit.html
    popt,pcov = curve_fit(_density_speed_function, density_data, speed_data,bounds=[[lower_bound_FFS,LOWER_BOUND_CRITICAL_DENSITY,0],[upper_bound_FFS,UPPER_BOUND_CRITICAL_DENSITY,15]])

    free_flow_speed=popt[0]
    critical_density=popt[1]
    mm=popt[2]
    speed_at_capacity=free_flow_speed/np.power(2,2/mm)
    ultimate_capacity=speed_at_capacity*critical_density

    xvals=np.linspace(0, UPPER_BOUND_JAM_DENSITY,100) # all the data points with density values 
    plt.plot(vdf_training_set_after_sorting['density'], vdf_training_set_after_sorting['speed'], '*', c='k', label='observations',markersize=1)
    plt.plot(xvals, _density_speed_function(xvals, *popt), '--',c='b',markersize=6,label='speed-density curve')
    plt.scatter(density_data, speed_data,edgecolors='r',color='r',label ='outer layer',zorder=30)
    plt.legend(loc='best')
    plt.grid(True)
    plt.title('Density-speed fundamental diagram, VDF: '+str(vdf_index[0]+vdf_index[1]*100))
    plt.xlabel('Density')
    plt.ylabel('Speed')
    plt.savefig(subfolder+'1_FD_speed_density_'+str(vdf_index[0]+vdf_index[1]*100)+'.png')    
    plt.close('all') 
    
    plt.plot(vdf_training_set_after_sorting['hourly_volume_per_lane'], vdf_training_set_after_sorting['speed'], '*', c='k', label='observations',markersize=1)
    plt.plot(xvals*_density_speed_function(xvals, *popt),_density_speed_function(xvals, *popt), '--',c='b',markersize=6,label='speed-volume curve')
    #plt.scatter(density_data*speed_data, speed_data,edgecolors='r',color='r',label ='outer layer',zorder=30)
    plt.legend(loc='best')
    plt.grid(True)
    plt.title('Volume-speed fundamental diagram,VDF: '+str(vdf_index[0]+vdf_index[1]*100))
    plt.xlabel('Volume')
    plt.ylabel('Speed')
    plt.savefig(subfolder+'1_FD_speed_volume_'+str(vdf_index[0]+vdf_index[1]*100)+'.png') 
    plt.close('all') 

    plt.plot(vdf_training_set_after_sorting['density'], vdf_training_set_after_sorting['hourly_volume_per_lane'], '*', c='k', label='original values',markersize=1)
    plt.plot(xvals,xvals*_density_speed_function(xvals, *popt), '--',c='b',markersize=6,label='density-volume curve')
    #plt.scatter(density_data,density_data*speed_data,edgecolors='r',color='r',label ='outer layer',zorder=30)
    plt.legend(loc='best')
    plt.grid(True)
    plt.title('Density-volume fundamental diagram,VDF: '+str(vdf_index[0]+vdf_index[1]*100))
    plt.xlabel('Density')
    plt.ylabel('Volume')
    plt.savefig(subfolder+'1_FD_volume_density_'+str(vdf_index[0]+vdf_index[1]*100)+'.png')    
    plt.close('all') 

    return speed_at_capacity,ultimate_capacity,critical_density,free_flow_speed,mm

# In[4] VDF calibration 
def _vdf_calculation(internal_period_vdf_daily_link_df, vdf_index, period_index, speed_at_capacity, ultimate_capacity, critical_density, free_flow_speed, mm):    
    p0=np.array([free_flow_speed,0.15,4])
    lowerbound_fitting=[free_flow_speed,LOWER_BOUND_ALPHA,LOWER_BOUND_BETA] # upper bound and lower bound of free flow speed, alpha and beta
    upperbound_fitting=[free_flow_speed*2,UPPER_BOUND_ALPHA,UPPER_BOUND_BETA]

    if DOC_RATIO_METHOD =='QBM':
        print('Queue based method method calibration for VDF:'+str(vdf_index)+' time period: '+period_index+'...')
        internal_period_vdf_daily_link_df['hourly_demand_over_capacity']=internal_period_vdf_daily_link_df.apply(lambda x: x.demand/ultimate_capacity,axis=1)
        X_data=[]
        Y_data=[]
        for k in range(0,len(internal_period_vdf_daily_link_df)):
            # Hourly hourly_demand_over_capacity data 
            for kk in range(WEIGHT_HOURLY_DATA):
                Y_data.append(internal_period_vdf_daily_link_df.loc[k,'congestion_period_mean_speed'])
                X_data.append(internal_period_vdf_daily_link_df.loc[k,'hourly_demand_over_capacity'])
            # Period hourly_demand_over_capacity data
            for kk in range(WEIGHT_PERIOD_DATA):
                Y_data.append(internal_period_vdf_daily_link_df['period_mean_daily_speed'].mean())
                X_data.append(internal_period_vdf_daily_link_df['period_demand_over_capacity'].mean())
            for kk in range(WEIGHT_UPPER_BOUND_DOC_RATIO):
                Y_data.append(0.001)
                X_data.append(upper_bound_doc_ratio_dict[period_index])
        x_demand_over_capacity = np.array(X_data)
        y_speed = np.array(Y_data)
        popt,pcov = curve_fit(_bpr_func, x_demand_over_capacity, y_speed,bounds=[lowerbound_fitting,upperbound_fitting])
    
        RMSE=np.power((np.sum(np.power((_bpr_func(x_demand_over_capacity, *popt)-y_speed),2))/len(x_demand_over_capacity)),0.5)
        RSE=np.sum(np.power((_bpr_func(x_demand_over_capacity, *popt)-y_speed),2))/np.sum(np.power((_bpr_func(x_demand_over_capacity, *popt)-y_speed.mean()),2))

    xvals=np.linspace(0,5,50)
    plt.plot(x_demand_over_capacity, y_speed, '*', c='k', label='DOC vs.mean_speed',markersize=3)
    plt.plot(xvals,_bpr_func(xvals, *popt), '--',c='k',markersize=6,label='BPR')
    plt.title(DOC_RATIO_METHOD+' '+str(vdf_index[0]+vdf_index[1]*100)+' '+str(period_index)+',RSE='+str(round(RSE,2))+'%,ffs='+str(round(popt[0],2))+',alpha='+str(round(popt[1],2))+',beta='+str(round(popt[2],2)))
    plt.xlabel('Hourly_demand_over_capacity')
    plt.ylabel('Speed')
    plt.legend(loc='best')
    plt.grid(True)
    plt.savefig(folder+'3_hourly_VDF_'+DOC_RATIO_METHOD+'_'+str(vdf_index[0]+vdf_index[1]*100)+'_'+str(period_index)+'.png')    
    plt.close('all') 

    internal_period_vdf_daily_link_df['period_mean_volume']=internal_period_vdf_daily_link_df['period_volume'].mean()
    internal_period_vdf_daily_link_df['period_mean_speed']=internal_period_vdf_daily_link_df['period_mean_daily_speed'].mean()

    xvals=np.linspace(0,20000,100)/internal_period_vdf_daily_link_df.period_capacity.mean()
    plt.plot(internal_period_vdf_daily_link_df.period_volume, internal_period_vdf_daily_link_df.period_mean_daily_speed  , '*', c='k', label='DOC vs.mean_speed',markersize=3)
    plt.plot(np.linspace(0,20000,100),_bpr_func(xvals, *popt), '--',c='k',markersize=6,label='BPR')
    plt.plot(internal_period_vdf_daily_link_df['period_volume'].mean(),internal_period_vdf_daily_link_df['period_mean_daily_speed'].mean(), 'o',c='r',markersize=8,label='ref_point')
    plt.title(DOC_RATIO_METHOD+' '+str(vdf_index[0]+vdf_index[1]*100)+' '+str(period_index)+',RSE='+str(round(RSE,2))+'%,ffs='+str(round(popt[0],2))+',alpha='+str(round(popt[1],2))+',beta='+str(round(popt[2],2)))
    plt.xlabel('Assigned_volume')
    plt.ylabel('Speed')
    plt.legend(loc='best')
    plt.grid(True)
    plt.savefig(folder+'3_period_VDF_'+DOC_RATIO_METHOD+'_'+str(vdf_index[0]+vdf_index[1]*100)+'_'+str(period_index)+'.png')    
    plt.close('all') 

    internal_period_vdf_daily_link_df['alpha']=round(popt[1],2)
    internal_period_vdf_daily_link_df['beta']=round(popt[2],2)   

    return internal_period_vdf_daily_link_df


def _vdf_calculation_daily(all_calibration_period_vdf_daily_link_results, vdf_index, speed_at_capacity, ultimate_capacity, critical_density, free_flow_speed):
    p0=np.array([free_flow_speed,0.15,4])
    lowerbound_fitting=[free_flow_speed,0.15,1.01]
    upperbound_fitting=[free_flow_speed*1.1,10,10]
    X_data=[]
    Y_data=[]
   
    for k in range(0,len(all_calibration_period_vdf_daily_link_results)):
        # Hourly hourly_demand_over_capacity data 
        for kk in range(WEIGHT_HOURLY_DATA):
            Y_data.append(all_calibration_period_vdf_daily_link_results.loc[k,'congestion_period_mean_speed'])
            X_data.append(all_calibration_period_vdf_daily_link_results.loc[k,'hourly_demand_over_capacity'])
        # Period hourly_demand_over_capacity data
            # Period hourly_demand_over_capacity data
        for kk in range(WEIGHT_PERIOD_DATA):
            Y_data.append(all_calibration_period_vdf_daily_link_results.loc[k,'period_mean_speed'])
            X_data.append(all_calibration_period_vdf_daily_link_results.loc[k,'period_mean_volume']/all_calibration_period_vdf_daily_link_results.loc[k,'period_capacity'])
        for kk in range(WEIGHT_UPPER_BOUND_DOC_RATIO):
            Y_data.append(0.001)
            X_data.append(upper_bound_doc_ratio_dict[all_calibration_period_vdf_daily_link_results.loc[k,'assignment_period']])
        x_demand_over_capacity = np.array(X_data)
        y_speed = np.array(Y_data)

    popt_daily,pcov = curve_fit(_bpr_func, x_demand_over_capacity, y_speed,bounds=[lowerbound_fitting,upperbound_fitting])
    #daily_RMSE=np.power((np.sum(np.power((_bpr_func(x_demand_over_capacity, *popt_daily)-y_speed),2))/len(x_demand_over_capacity)),0.5)
    daily_RSE=np.sum(np.power((_bpr_func(x_demand_over_capacity, *popt_daily)-y_speed),2))/np.sum(np.power((_bpr_func(x_demand_over_capacity, *popt_daily)-y_speed.mean()),2))

    xvals=np.linspace(0,5,50)
    plt.plot(x_demand_over_capacity, y_speed, '*', c='k', label='DOC vs.mean_speed',markersize=3)
    plt.plot(xvals,_bpr_func(xvals, *popt_daily), '--',c='k',markersize=6,label='calibrated BPR function')
        
    plt.title('Daily_QBM'+str(vdf_index[0]+vdf_index[1]*100)+',RSE='+str(round(daily_RSE,2))+'%,ffs='+str(round(popt_daily[0],2))+',alpha='+str(round(popt_daily[1],2))+',beta='+str(round(popt_daily[2],2)))
    plt.xlabel('hourly_demand_over_capacity')
    plt.ylabel('speed')
    plt.legend(loc='best')
    plt.grid(True)
    plt.savefig(folder+'4_hourly_VDF_QBM_'+str(vdf_index[0]+vdf_index[1]*100)+'_day.png')    
    plt.close('all')
    
    plt.plot(all_calibration_period_vdf_daily_link_results.period_volume, all_calibration_period_vdf_daily_link_results.period_mean_daily_speed  , '*', c='k', label='derived training data',markersize=3)
    maximum_value=all_calibration_period_vdf_daily_link_results.period_volume.max()*2
    capacity_period_dict= dict(zip(all_calibration_period_vdf_daily_link_results.assignment_period,all_calibration_period_vdf_daily_link_results.period_capacity,)) 
    

    for kk in list(all_calibration_period_vdf_daily_link_results.assignment_period.unique()):
        xvals=np.linspace(0,maximum_value,100)/capacity_period_dict[kk]
        plt.plot(np.linspace(0,maximum_value,100),_bpr_func(xvals, *popt_daily), '--', label = 'BPR:'+str(kk), markersize=6)
        df= all_calibration_period_vdf_daily_link_results[all_calibration_period_vdf_daily_link_results.assignment_period == kk]
        plt.plot(df['period_mean_volume'],df['period_mean_speed'], 'o', label = 'ref_point:'+str(kk), markersize=8)
    
    plt.legend(loc='best')
    plt.grid(True)
    plt.title('Daily_QBM_'+str(vdf_index[0]+vdf_index[1]*100)+',RSE='+str(round(daily_RSE,2))+'%,ffs='+str(round(popt_daily[0],2))+',alpha='+str(round(popt_daily[1],2))+',beta='+str(round(popt_daily[2],2)))
    plt.xlabel('Assigned_volume')
    plt.ylabel('Speed')
    plt.savefig(folder+'4_period_VDF_QBM_'+str(vdf_index[0]+vdf_index[1]*100)+'_day.png') 
    plt.close('all') 

    all_calibration_period_vdf_daily_link_results['daily_alpha']=round(popt_daily[1],2)
    all_calibration_period_vdf_daily_link_results['daily_beta']=round(popt_daily[2],2) 

    return all_calibration_period_vdf_daily_link_results

# In[5] Calculate demand and congestion period
def _calculate_congestion_duration(speed_series,volume_per_lane_series,density_series,hourly_volume_per_lane_series,speed_at_capacity,ultimate_capacity,critical_density,length, free_flow_speed):
    global PSTW # preferred service time window
    nb_time_stamp=len(speed_series)
    min_speed=min(speed_series)
    min_index=speed_series.index(min(speed_series)) # The index of speed with minimum value 
    
    # start time and ending time of prefered service time window
    PSTW_start_time=max(min_index-2,0)
    PSTW_ending_time=min(min_index+1,nb_time_stamp)
    if PSTW_ending_time - PSTW_start_time < 3:
        if PSTW_start_time==0:
            PSTW_ending_time=PSTW_ending_time+(3-(PSTW_ending_time - PSTW_start_time))
        if PSTW_ending_time==nb_time_stamp:
            PSTW_start_time=PSTW_start_time-(3-(PSTW_ending_time - PSTW_start_time))
    PSTW=(PSTW_ending_time-PSTW_start_time+1)*(TIME_INTERVAL_IN_MIN/60)
    PSTW_volume=np.array(volume_per_lane_series[PSTW_start_time:PSTW_ending_time+1]).sum()
    PSTW_speed=np.array(speed_series[PSTW_start_time:PSTW_ending_time+1]).mean()

    # Determine 
    t3=nb_time_stamp-1
    t0=0
    if min_speed<=speed_at_capacity:
        for i in range(min_index,nb_time_stamp):
            if speed_series[i]>speed_at_capacity:               
                t3=i-1
                break
        for j in range(min_index,-1,-1):
            #t0=PSTW_start_time
            if speed_series[j]>speed_at_capacity:               
                t0=j+1
                break
        congestion_duration=(t3-t0+1)*(TIME_INTERVAL_IN_MIN/60)
        #queue_demand_factor_method='SBM' # if the min_speed of the link within the assignment period is less than the speed_at_capacity, then we use SBM to calculate the peak hour factor
    
    elif min_speed >speed_at_capacity:
        t0=0
        t3=0
        congestion_duration=0
        #queue_demand_factor_method='VBM' # if the min_speed of the link within the assignment period is larger than the speed_at_capacity, then we use VBM to calculate the peak hour factor
    
    average_discharge_rate=np.mean(hourly_volume_per_lane_series[t0:t3+1]) 

    gamma=0
    max_queue_length=0
    #average_waiting_time=0
    queue_series=np.zeros(nb_time_stamp)
    congestion_period_mean_speed=np.array(speed_series[t0:t3+1]).mean()
    if congestion_duration>PSTW:
        demand=np.array(volume_per_lane_series[t0:t3+1]).sum()
        congestion_period_mean_speed=np.array(speed_series[t0:t3+1]).mean()  
    elif congestion_duration<=PSTW:
        demand=PSTW_volume
        congestion_period_mean_speed=PSTW_speed
        #queue_series_string= ';'.join(str(l) for l in queue_series)

    return t0, t3,congestion_duration,PSTW_start_time,PSTW_ending_time,PSTW,demand,average_discharge_rate,congestion_period_mean_speed,queue_demand_factor_method#,gamma,queue_series_string,max_queue_length


# In[6] Histogram
def _getCPF(speed_series,volume_per_lane_series,vdf_index,period_index,folder):
            fig, ax = plt.subplots(nrows=2, ncols=1)
            n, bins, patches = ax[0].hist(speed_series, bins=50, density=True, histtype='step',
                           cumulative=True, label='Empirical distrbution')
            sigma=speed_series.std()
            mu=speed_series.mean()
            nb_of_sample=speed_series.count()
            # # Add a line showing the expected distribution.
            y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
            y = y.cumsum()
            y /= y[-1]
            ax[0].plot(bins, y, 'k--', linewidth=1.5, label='Gauss distribution')
            ax[0].grid(True)
            ax[0].legend(loc='best')
            ax[0].set_title('speed_cpf_'+str(100*vdf_index[1]+vdf_index[0])+'_'+period_index+': mean='+str(np.round(mu,1))+'; std='+str(np.round(sigma,1))+'; count='+str(np.round(nb_of_sample,0)))
            ax[0].set_xlabel('speed (mph)')
            ax[0].set_ylabel('cumulative probablity')

            n, bins, patches = ax[1].hist(volume_per_lane_series, bins=50, density=True, histtype='step',
                           cumulative=True, label='Empirical distribution')
            sigma=volume_per_lane_series.std()
            mu=volume_per_lane_series.mean()
            nb_of_sample=volume_per_lane_series.count()
            # # Add a line showing the expected distribution.
            y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
            y = y.cumsum()
            y /= y[-1]            
            
    
            ax[1].plot(bins, y, 'k--', linewidth=1.5, label='Gauss distribution')
            ax[1].grid(True)
            ax[1].legend(loc='best')
            ax[1].set_title('volume_cpf_'+str(100*vdf_index[1]+vdf_index[0])+'_'+period_index+': mean='+str(np.round(mu,1))+'; std='+str(np.round(sigma,1))+'; count='+str(np.round(nb_of_sample,0)))           
            ax[1].set_xlabel('volume per lane (veh/15minutes)')
            ax[1].set_ylabel('cumulative probablity')
            fig.tight_layout()
            plt.savefig(folder+'2_cpf_'+str(vdf_index[0]+vdf_index[1]*100)+'_'+period_index+'.png')    
            plt.close()


def _calibrateQueueDemandFactor(internal_period_vdf_daily_link_df,vdf_index,period_index,folder,EPS):
   period_queue_demand_factor=np.mean(internal_period_vdf_daily_link_df.queue_demand_factor)
   
   return period_queue_demand_factor


def _convertIndexToTime(t0,t3,period_index,congestion_duration,PSTW):
    if ((t0==t3) and (t0==0) and (t3==0)) or (congestion_duration<=PSTW):
        t0_new='none'
        t3_new='none'
        congestion_duration='<PSTW'
    else:
        K=period_index.split('_')
        temp_time=pd.to_datetime(K[0],format='%H%M', errors='ignore')
        t0_new=temp_time+datetime.timedelta(minutes=TIME_INTERVAL_IN_MIN)*t0
        t3_new=temp_time+datetime.timedelta(minutes=TIME_INTERVAL_IN_MIN)*(t3+1)
        t0_new=str(t0_new.time())[0:5]
        t3_new=str(t3_new.time())[0:5]
    return t0_new,t3_new,t0,t3,congestion_duration


def _calculateQueueLength(t0,t3,gamma,average_discharge_rate,assignment_period,congestion_duration,assingment_demand,demand): # assingment_demand= assignment_volume/PHF
    nb_time_stamp=period_length_dict[assignment_period]*(60/TIME_INTERVAL_IN_MIN)
    queue_series=np.zeros(int(nb_time_stamp))
    gamma_1 =gamma*(assingment_demand/demand)**4
    if congestion_duration!='<PSTW':
    
        time_stamp=np.array([*range(t0,t3+1)])/ (60.0 / TIME_INTERVAL_IN_MIN)
        t0_ph=t0 / (60.0 / TIME_INTERVAL_IN_MIN)
        t3_ph=t3 / (60.0 / TIME_INTERVAL_IN_MIN)
        waiting_time_term=(1/(4*average_discharge_rate))*(time_stamp-t0_ph)*(time_stamp-t0_ph)*(time_stamp-t3_ph)*(time_stamp-t3_ph)
        queue_series[t0:t3+1]=np.round(waiting_time_term*average_discharge_rate*gamma_1,2)
        #queue_series_string=';'.join(str(l) for l in queue_series)
        #max_queue_length=np.max(queue_series)
    return queue_series

def _getTimeVaryingQueue(calibration_period_vdf_daily_link_results,free_flow_speed):
    calibration_period_vdf_daily_link_results['gamma']=calibration_period_vdf_daily_link_results['alpha']*(calibration_period_vdf_daily_link_results['length']/free_flow_speed)*120*(calibration_period_vdf_daily_link_results['average_discharge_rate']**5)/(calibration_period_vdf_daily_link_results['ultimate_capacity']**4)
    calibration_period_vdf_daily_link_results['queue_series']=calibration_period_vdf_daily_link_results.apply(lambda x:_calculateQueueLength(x.t0_index,x.t3_index,x.gamma,x.average_discharge_rate,x.assignment_period,x.congestion_duration,x.demand,x.demand),axis=1)
    #calibration_period_vdf_daily_link_results['queue_series_lf']=calibration_period_vdf_daily_link_results.apply(lambda x:_calculateQueueLength(x.t0_index,x.t3_index,x.gamma,x.average_discharge_rate,x.assignment_period,x.congestion_duration,x.demand*0.8,x.demand),axis=1)
    #calibration_period_vdf_daily_link_results['queue_series_hf']=calibration_period_vdf_daily_link_results.apply(lambda x:_calculateQueueLength(x.t0_index,x.t3_index,x.gamma,x.average_discharge_rate,x.assignment_period,x.congestion_duration,x.demand*1.2,x.demand),axis=1)
    calibration_period_vdf_daily_link_results['max_queue_length']=calibration_period_vdf_daily_link_results['queue_series'].apply(lambda x: max(x))
    calibration_period_vdf_daily_link_results['queue_series']=calibration_period_vdf_daily_link_results['queue_series'].apply(lambda x: ';'.join(str(l) for l in x))
    #calibration_period_vdf_daily_link_results['queue_series_lf']=calibration_period_vdf_daily_link_results['queue_series_lf'].apply(lambda x: ';'.join(str(l) for l in x))
    #calibration_period_vdf_daily_link_results['queue_series_hf']=calibration_period_vdf_daily_link_results['queue_series_hf'].apply(lambda x: ';'.join(str(l) for l in x))
    return calibration_period_vdf_daily_link_results


# In[6] Main



def calibrateFundamentalDiagram(ft_list='all', at_list='all',link_performance_file='measurements.csv'):
    output_folder='output_fundametnal_diagrams'
    _mkdir(output_folder)

    subfolder = './'+output_folder+'/'
    training_set=_readInputData(link_performance_file,ft_list, at_list)

    # Step 2: For each VDF type, calibrate basic coefficients for fundamental diagrams
    # Step 2.1: Group the data frame by VDF types. Each VDF type is a combination of facility type (FT) and area type (AT)
    vdf_group=training_set.groupby(['FT','AT']) 
    for vdf_index,vdf_training_set in vdf_group: # vdf_index is a pair of facility type and area type e.g. vdf_index = (1,1) implies that FT=1 and AT=1 
       
        vdf_training_set.reset_index(drop=True, inplace=True) # reset index of the sub dataframe 
        speed_at_capacity,ultimate_capacity,critical_density,free_flow_speed,mm =_calibrate_traffic_flow_model(vdf_training_set,vdf_index,subfolder)
        print('calibrate fundamental diagram of VDF type', vdf_index)
        print ('--speed_at_capacity=',speed_at_capacity)
        print('--ultimate_capacity=',ultimate_capacity)
        print ('--critical_density=',critical_density)
        print('--free_flow_speed=',free_flow_speed)
        print('--mm=',mm)




def calibrateVdfCurve(ft_list='all', at_list='all', doc_method='QBM',link_performance_file='link_performance.csv'):
    # Step 0: Parameter setting
    #Step 0.1. Parameters set in external setting.csv
    global DOC_RATIO_METHOD
    global folder
    global period_length_dict
    global upper_bound_doc_ratio_dict

    DOC_RATIO_METHOD=doc_method
    
    output_folder='output_calibration'
    _mkdir(output_folder)  

    folder = './'+output_folder+'/'

    # Step 1: Read input data
    print('Step 1:Read input data...')
    training_set=_readInputData(link_performance_file,ft_list, at_list) # training_set is a data frame of pandas to store the whole link_performance.csv file 
    ASSIGNMENT_PERIOD=training_set.assignment_period.unique().tolist() #array of assignment periods
    PERIOD_LENGTH=[] #list of the length of assignment periods
    NUMBER_OF_RECORDS=[] #list of the number of records of assignment periods
    UPPER_BOUND_DOC_RATIO=[] #list of the upper bound of demand over capacity ratio
    period_start_time_list=[]
    for period in ASSIGNMENT_PERIOD: # parsor HHMM time, period length
        period_start_time_list.append(int(period.split('_')[0][0:2])*60+int(period.split('_')[0][2:4]))
        time_ss = [int(var[0:2]) for var in period.split('_')]
        if time_ss[0] > time_ss[1]:
            period_length = time_ss[1] + 24 - time_ss[0] # e.g. if the assignment period is 1800_0600, then we will calculate that 6-18+24=12
            upper_bound_doc_ratio=np.minimum(5,period_length) # assume that the maximum value of D over C ratio is 6 hours and should not be larger than the length of assignment periods
            number_of_records=period_length*(60/TIME_INTERVAL_IN_MIN) # calculate the complete number of records in the time-series data of a link during an assignment period, e.g if  assignment period 0600_0900 should have 3 hours * 4 records (if time stamp is 15 minutes)
        else:
            period_length = time_ss[1] - time_ss[0]
            upper_bound_doc_ratio=np.minimum(5,period_length)
            number_of_records=period_length*(60/TIME_INTERVAL_IN_MIN)

        PERIOD_LENGTH.append(period_length)
        NUMBER_OF_RECORDS.append(number_of_records)
        UPPER_BOUND_DOC_RATIO.append(upper_bound_doc_ratio)
    daily_starting_time=min(period_start_time_list)
    training_set['time_index']=training_set['time_period'].apply(lambda x: np.mod(_convertTimeToMinute(x)-daily_starting_time,1440))

    vdf_table_dict={}
    period_id_dict={}
    vdf_table_dict['VDF']=[]

    vdf_table_index=[100*i+j for i in training_set.AT.unique() for j in training_set.FT.unique()]
    vdf_table_column=['VDF','capacity']

    iter=1
    for period in ASSIGNMENT_PERIOD:
        period_id_dict[period]=iter
        vdf_table_column.append('VDF_Cap'+str(period_id_dict[period]))
        vdf_table_column.append('VDF_alpha'+str(period_id_dict[period]))
        vdf_table_column.append('VDF_beta'+str(period_id_dict[period]))
        iter+=1

    vdf_table=pd.DataFrame(columns=vdf_table_column, index=vdf_table_index)

    # create three hash table to map assignment periods to period lenght/ upper bound of DOC/ complete number of records
    

    period_length_dict = dict(zip(ASSIGNMENT_PERIOD, PERIOD_LENGTH))
    upper_bound_doc_ratio_dict= dict(zip(ASSIGNMENT_PERIOD, UPPER_BOUND_DOC_RATIO)) 
    number_of_records_dict = dict(zip(ASSIGNMENT_PERIOD, NUMBER_OF_RECORDS)) 


    # Step 2: For each VDF type, calibrate basic coefficients for fundamental diagrams
    # Step 2.1: Group the data frame by VDF types. Each VDF type is a combination of facility type (FT) and area type (AT)
    vdf_group=training_set.groupby(['FT','AT']) 
    output_df_daily=pd.DataFrame() # Create empty dataframe

    for vdf_index,vdf_training_set in vdf_group: # vdf_index is a pair of facility type and area type e.g. vdf_index = (1,1) implies that FT=1 and AT=1 
        #_getCPF(vdf_training_set['speed'],vdf_training_set['volume_per_lane'],vdf_index,'day',folder)
        vdf_training_set.reset_index(drop=True, inplace=True) # reset index of the sub dataframe 
        print('Step 2: Calibrate key coefficients in traffic stream models in VDF type '+str(vdf_index[1]*100+vdf_index[0])+' ...')
        # For each VDF type, we have a unique index for each VDF type e.g. (1) VDF type FT = 1 and AT = 1:  AT*100+FT=100*1+1=101 (2) VDF type FT = 3 and AT = 2:  AT*200+FT=100*2+3=203
        speed_at_capacity,ultimate_capacity,critical_density,free_flow_speed,mm=_calibrate_traffic_flow_model(vdf_training_set,vdf_index,folder) # calibrate parameters of traffic flow model
        # calibrate the four key parameters : speed at capacity, ultimate capacity , critical density and free flow speed. 

        all_calibration_period_vdf_daily_link_results=pd.DataFrame() # Create empty dataframe
        # write on vdf table 
        vdf_table.loc[100*vdf_index[1]+vdf_index[0],'VDF']=100*vdf_index[1]+vdf_index[0]
        vdf_table.loc[100*vdf_index[1]+vdf_index[0],'capacity']=ultimate_capacity

        # Step 3: For each VDF and assignment period, calibrate congestion duration, demand, t0, t3, alpha and beta
        print('Step 3: Calibrate VDF function of links for VDF_type: '+str(vdf_index)+' and time period...')
        period_vdf_group=vdf_training_set.groupby(['assignment_period']) # group the vdf_trainset according to time periods
        for period_index, period_vdf_training_set in period_vdf_group: #_period_based_vdf_training_set
            _getCPF(period_vdf_training_set['speed'],period_vdf_training_set['volume_per_lane'],vdf_index,period_index,folder)
            internal_period_vdf_daily_link_df= pd.DataFrame()
            # day_period_link_based_vdf_training_set
            daily_link_group=period_vdf_training_set.groupby(['link_id','from_node_id','to_node_id','date'])
            daily_link_list=[]

            for daily_link_index,daily_link_training_set in daily_link_group:
                daily_link_training_set=daily_link_training_set.sort_values(by='time_index', ascending=True)
                daily_link_training_set.reset_index(drop=True, inplace=True) # reset index of the sub dataframe 
                link_id=daily_link_index[0]
                from_node_id=daily_link_index[1]
                to_node_id=daily_link_index[2]
                date=daily_link_index[3]
                FT=vdf_index[0]
                AT=vdf_index[1]
                period_index=period_index
                if (len(daily_link_training_set) < number_of_records_dict[period_index]) and ((1 - len(daily_link_training_set) / number_of_records_dict[period_index]) >= MIN_THRESHOLD_SAMPLING) :
                    print('WARNING:  link ', link_id, 'does not have enough time series records in assignment period', period_index,'at',daily_link_index[3], '...')
                    continue                
                period_volume=daily_link_training_set['volume_per_lane'].sum() # summation of all volume per lane within the period, +++++
                period_mean_hourly_volume_per_lane=daily_link_training_set['hourly_volume_per_lane'].mean() #  mean hourly value 
                period_mean_daily_speed=daily_link_training_set['speed'].mean()
                period_mean_density=daily_link_training_set['density'].mean()               
                volume_per_lane_series=daily_link_training_set.volume_per_lane.to_list()
                speed_series=daily_link_training_set.speed.to_list()
                density_series=daily_link_training_set.density.to_list()
                hourly_volume_per_lane_series=daily_link_training_set.hourly_volume_per_lane.to_list() # --> hourly_volume_per_lane
                link_length=daily_link_training_set.length.mean() # obtain the length of the link
                link_free_flow_speed=free_flow_speed
                geometry=daily_link_training_set.geometry[0]
                length=daily_link_training_set.length[0]
                
                # Step 3.1 Calculate Demand over capacity and congestion duration
                t0, t3,congestion_duration,PSTW_start_time,PSTW_ending_time,PSTW,demand,average_discharge_rate,congestion_period_mean_speed,queue_demand_factor_method\
                    =_calculate_congestion_duration(speed_series,volume_per_lane_series,density_series,hourly_volume_per_lane_series,speed_at_capacity,ultimate_capacity,critical_density,link_length,link_free_flow_speed)
                t0_new,t3_new,t0,t3,congestion_duration=_convertIndexToTime(t0,t3,period_index,congestion_duration,PSTW)
                # Step 3.2 Calculate peak hour factor for each link
                vol_hour_max=np.max(hourly_volume_per_lane_series)
                EPS = ultimate_capacity/7 # setting a lower bound of demand 
                if queue_demand_factor_method=='SBM':
                    queue_demand_factor=period_volume/max(demand,EPS)
                    #queue_demand_factor=max(min(period_volume/max(demand,EPS),period_length_dict[period_index]),period_length_dict[period_index]/LOWER_BOUND_OF_PHF)
                if queue_demand_factor_method=='VBM':
                    #queue_demand_factor=period_volume/vol_hour_max  # per link peak hour factor
                    queue_demand_factor=max(min(period_volume/vol_hour_max,period_length_dict[period_index]),period_length_dict[period_index]/LOWER_BOUND_OF_PHF)
                
                daily_link=[link_id,from_node_id, to_node_id,date,FT,AT,period_index,period_volume, period_mean_hourly_volume_per_lane,\
                    period_mean_daily_speed,period_mean_density,t0,t3,t0_new,t3_new,demand,average_discharge_rate,queue_demand_factor,congestion_duration,congestion_period_mean_speed,geometry,length]
                daily_link_list.append(daily_link)
            
            if len(daily_link_list) ==0: 
                print('WARNING: all the links of ' + str(vdf_index[0]+vdf_index[1]*100) + ' during assignment period ' + period_index + ' are not qualified...')
                continue 

            internal_period_vdf_daily_link_df= pd.DataFrame(daily_link_list)
            internal_period_vdf_daily_link_df.rename(columns={0:'link_id',
                                    1:'from_node_id',
                                    2:'to_node_id',
                                    3:'date',
                                    4:'FT',
                                    5:'AT',
                                    6:'assignment_period',
                                    7:'period_volume',
                                    8:'period_mean_hourly_volume_per_lane',
                                    9:'period_mean_daily_speed', 
                                    10:'period_mean_density',                                            
                                    11:'t0_index',
                                    12:'t3_index',
                                    13:'t0',
                                    14:'t3',
                                    15:'demand',
                                    16:'average_discharge_rate',
                                    17:'queue_demand_factor',
                                    18:'congestion_duration',
                                    19:'congestion_period_mean_speed',
                                    20:'geometry',
                                    21:'length'}, inplace=True)
            internal_period_vdf_daily_link_df.to_csv(folder+'2_training_set_'+str(100*vdf_index[1]+vdf_index[0])+'_'+str(period_index)+'.csv',index=False)
            # Step 3.3 calculate the peak hour factor for each period and VDF type
            period_queue_demand_factor=_calibrateQueueDemandFactor(internal_period_vdf_daily_link_df,vdf_index,period_index,folder,EPS)
            internal_period_vdf_daily_link_df['period_queue_demand_factor']=period_queue_demand_factor
            internal_period_vdf_daily_link_df['ultimate_capacity']=ultimate_capacity
            internal_period_vdf_daily_link_df['period_capacity']=ultimate_capacity*period_queue_demand_factor
            internal_period_vdf_daily_link_df['period_demand_over_capacity']=internal_period_vdf_daily_link_df['period_volume'].mean()/(ultimate_capacity*period_queue_demand_factor)

            # Step 3.4 calculate alpha and beta for each period and VDF type
            calibration_period_vdf_daily_link_results = _vdf_calculation(internal_period_vdf_daily_link_df, vdf_index, period_index, speed_at_capacity,
                                                            ultimate_capacity, critical_density, free_flow_speed, mm) 
            calibration_period_vdf_daily_link_results=_getTimeVaryingQueue(calibration_period_vdf_daily_link_results,free_flow_speed)
            
            all_calibration_period_vdf_daily_link_results = pd.concat([all_calibration_period_vdf_daily_link_results,calibration_period_vdf_daily_link_results],sort=False)
            para=[vdf_index,100*vdf_index[1]+vdf_index[0],vdf_index[0],vdf_index[1],period_index,speed_at_capacity,ultimate_capacity,critical_density,free_flow_speed,mm,period_queue_demand_factor,calibration_period_vdf_daily_link_results.alpha.mean(),calibration_period_vdf_daily_link_results.beta.mean()]
            g_parameter_list.append(para)

            vdf_table.loc[100*vdf_index[1]+vdf_index[0],'VDF_Cap'+str(period_id_dict[period_index])]=ultimate_capacity*period_queue_demand_factor
            vdf_table.loc[100*vdf_index[1]+vdf_index[0],'VDF_alpha'+str(period_id_dict[period_index])]=calibration_period_vdf_daily_link_results.alpha.mean()
            vdf_table.loc[100*vdf_index[1]+vdf_index[0],'VDF_beta'+str(period_id_dict[period_index])]=calibration_period_vdf_daily_link_results.beta.mean()


        # Step 4 Calibrate daily VDF function 
        print('Step 4: Calibrate daily VDF function for VDF_type:'+str(vdf_index)+'...\n')

        all_calibration_period_vdf_daily_link_results=all_calibration_period_vdf_daily_link_results.reset_index(drop=True)
        all_calibration_period_vdf_daily_link_results['VDF_TYPE']=100*all_calibration_period_vdf_daily_link_results.AT+all_calibration_period_vdf_daily_link_results.FT
        all_calibration_period_vdf_daily_link_results = _vdf_calculation_daily(all_calibration_period_vdf_daily_link_results, vdf_index, speed_at_capacity, ultimate_capacity,
                                                                     critical_density, free_flow_speed)
        output_df_daily = pd.concat([output_df_daily,all_calibration_period_vdf_daily_link_results],sort=False)
        para=[vdf_index,100*vdf_index[1]+vdf_index[0],vdf_index[0],vdf_index[1],'daily','--','--','--','--','--','--','--',all_calibration_period_vdf_daily_link_results.daily_alpha.mean(),all_calibration_period_vdf_daily_link_results.daily_beta.mean()]
        g_parameter_list.append(para)
    
    if len(g_parameter_list) ==0: 
        print('WARNING: No available data')
        exit() 

    # Step 6 Output results 
    print('Step 5: Output...\n')
    para_df= pd.DataFrame(g_parameter_list)
    para_df.rename(columns={0:'VDF',
                                1:'VDF_TYPE',
                                2: 'FT',
                                3: 'AT',
                                4: 'period',
                                5:'speed_at_capacity',
                                6:'ultimate_capacity',
                                7:'critical_density',
                                8:'free_flow_speed',
                                9: 'mm',
                                10:'queue_demand_factor',
                                11:'period_capacity',
                                12:'alpha',
                                13:'beta'}, inplace=True)
    para_df.to_csv(folder+'5_summary.csv',index=False) # vdf calibratio summary
    vdf_table.dropna(axis=0,how='all',inplace=True)  
    vdf_table.to_csv('updated_vdf_table.csv',index=False) # day by day 
    output_df_daily.to_csv(folder+'5_day_based_calibration.csv',index=False) # day by day 

    print('END...')



