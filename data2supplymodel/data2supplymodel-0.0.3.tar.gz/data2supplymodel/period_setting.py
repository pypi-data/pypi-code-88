
import pandas as pd
import numpy as np
import os 
import time 

#In[5] Step 3: convert observations to lane performance files 
def joinDemandPeriod (period_list,performance_file_name='measurements.csv',output_folder='./'):
    data_df=pd.read_csv(performance_file_name,encoding='UTF-8')
    
    print("---Join Demand Periods---")
    print ('obtaining time_index ....')
    time_start=time.time()
    global daily_starting_time 
    daily_starting_time=1440
    period_name_list=[]
    start_time_list=[]
    end_time_list=[]
    for period_name in period_list: # parsor HHMM time, period length
        period_name_list.append(period_name)
        var=period_name.split('_')[0]
        start_time_list.append(int(var[0:2])*60+int(var[2:4]))
        var=period_name.split('_')[1]
        end_time_list.append(int(var[0:2])*60+int(var[2:4]))
    daily_starting_time=min(start_time_list)
    assignment_period_df=pd.DataFrame({'period_name':period_name_list,'start_time':start_time_list,'end_time':end_time_list})
    assignment_period_df['start_time_r']=np.mod(assignment_period_df['start_time']-daily_starting_time,1440)
    assignment_period_df['end_time_r']=np.mod(assignment_period_df['end_time']-daily_starting_time,1440)
    assignment_period_df['end_time_r']=assignment_period_df['end_time_r'].apply(lambda x: 1440 if x==0 else x)
    data_df['time_index']=data_df.apply(lambda x: np.mod(float(x.time_period.split('_')[0][0:2])*60+float(x.time_period.split('_')[0][2:4])-daily_starting_time,1440), axis=1)

    print ('joining assignment periods ....')
    time_start=time.time()
    data_df['assignment_period']=np.nan
    for ind, row in assignment_period_df.iterrows():
        period_flag=data_df.time_index.isin(range(row.start_time_r,row.end_time_r))
        data_df.loc[period_flag,'assignment_period']=row.period_name
    
    data_df.dropna(subset=['assignment_period'],inplace=True)
    # data_df.sort_values(by="time_index" , ascending=True,inplace=True)
    # data_df.reset_index(inplace=True)



    time_end=time.time()
    print()

    data_df.to_csv(os.path.join(output_folder,performance_file_name), index=False)
    
    print('attache assignment periods on link_performance.csv, DONE, using time:',time_end-time_start,'s...\n')
	