import pandas as pd
import numpy as np
from jh_utils.time_series.covariables import year_sincos_array, hour_sincos_array, hours_by_day
from jh_utils.pandas.preprocessing import make_dummies

def date_range_dataframe(start_date,end_date,freq='1H', column_name='hours'):
    df = pd.DataFrame({column_name: pd.date_range(start_date, end_date, freq=freq, closed='left')})
    return df

def time_series_dataframe(start_date,end_date,freq='1H',datetime_column_name='hours',
                          weekday_dummies=True,
                          month_dummies=True,
                          hour_dummies=True,
                          year_sin_cos=True,
                          hour_sin_cos=True):
    df = date_range_dataframe(start_date,end_date,freq=freq,column_name=datetime_column_name)
    shape = df.shape
    if weekday_dummies:
        df = pd.concat([df,make_dummies(pd.Series(df.iloc[:,0].dt.weekday, name = 'weekday_dummie'))],axis=1)
    if month_dummies:
        df = pd.concat([df,make_dummies(pd.Series(df.iloc[:,0].dt.month, name = 'month_dummie'))],axis=1)
    if hour_dummies:
        df = pd.concat([df,make_dummies(pd.Series(df.iloc[:,0].dt.hour, name = 'hour_dummie'))],axis=1)
    if year_sin_cos:
        df = pd.concat([df,year_sincos_array(shape[0],start_date,end_date)],axis=1)
    if hour_sin_cos:
        df = pd.concat([df,hour_sincos_array(hours_by_day(freq),start_date,pd.to_datetime(end_date))],axis=1)
    
    df.index =  df[datetime_column_name]
    df = df.iloc[:,1:]
    return df