''' Statistical routines - statscalc
        developed by Victor Cossich (victor.cossich@gmail.com) and Conrado Torres (conradotl@gmail.com)
        for quick statistical procedures in pandas series and dataframes. Email us if you want. ;)

    	you need numpy,pandas and scipy.stats to run this module.
'''

import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from scipy import stats
    
def normality_check(data_set, alpha = 0.05, log = True, verbose = True):
    '''
    data_set = Pandas DataFrame for analisis
    alpha(optional) = critical p value for the shapiro-wilk test (scipy.stats), default is .05
    log(optional) = if True log transformation is considered, default is True
    verbose(optional) = if True prints the results for each variable, default is true
    return: list with the name of normally distributed variables, list with the name of non-normally distributed variables
    '''        
    # list for the normally and non-normally distributed vars
    normal = []
    non_normal = []    
    # iterate over each column
    for var in data_set:           
        # test if is numerical
        if is_numeric_dtype(data_set[var]):                                   
            # hold the p value of Shapiro-Wilk test
            p_val = stats.shapiro(data_set[var])[1]            
            # procedures for normally distributed vars
            if p_val > alpha:                   
                if verbose: print (var, '- NORMAL' , '- p=', round(p_val,4) )                   
                normal.append(var)                 
                # pass to the next iteration
                continue                 
            # procedures for normally distributed vars
            # tests for log transformed values if indicated
            if log :                  
                # hold the p value of Shapiro-Wilk test
                p_log = stats.shapiro(np.log10(data_set[var]))[1]                 
                if p_log > alpha:                    
                    # procedures for normally distributed transformed vars
                    if verbose: print (var, '- NORMAL (log10)' , '- p=', round(p_log,4) )                     
                    normal.append(var)                     
                    # pass for the next iteration
                    continue             
            # procedures for non normally distributed vars
            if verbose: print (var, '- Non NORMAL' , '- p=', round (p_val,4) ) 
            non_normal.append(var)                                           
    
    return (normal,non_normal) 

###############################################################################

def outliers_det (series,method = 'interquartile',lim = 1.5):
    '''
    series = a pd.series or list for analisys
    method = if "interquartile" the lim*interquartile range is used as the bundary
    if "zscore", the lim*standart deviation is used.
    lim = number of interquartile range or standart deviation used as boundaries for outliers detection.
    return: dataframe with the non-outliers values, dataframe with the outliers values
    '''    
    # cast the passed structure into a pd.series
    series = pd.Series(series)
    if method == 'interquartile':
        #defines the interquartile range
        q1 = series.quantile(0.25) 
        q3 = series.quantile(0.75)
        iqr= q3 - q1
        #calculate the boundaries
        down_lim = q1 - (lim * iqr)
        up_lim = q3 + (lim * iqr)
    if method == 'zscore':
        #defines mean and stddev
        mean = series.mean()
        std = series.std()        
        #calculate the boundaries
        down_lim = mean - (lim * std)
        up_lim = mean + (lim * std)        
    # create masks for the boundaries
    mask_up = series < up_lim
    mask_down = series > down_lim
    mask = mask_up & mask_down
    #apply yhe masks
    filtered = series[mask]
    outliers = series[~mask]

    return (filtered,outliers)

###############################################################################

def outliers_df(dataframe,method = 'interquartile',lim = 1.5):
    '''
    dataframe = a dataframe to be analyzed
    method = if "interquartile" the lim*interquartile range is used as the bundary
    if "zscore", the lim*standart deviation is used.
    lim = number of interquartile range or standart deviation used as boundaries for outliers detection.
    return: a copy of the original dataframe with NaN in the outliers positions
    '''  
    # Make a copy of the original dataframe 
    outlierless = dataframe.copy()  
    # Apply the previous function to remove outliers from each column
    for var in outlierless:
        if is_numeric_dtype(outlierless[var]):
            outlierless[var]=outliers_det(outlierless[var],method,lim)[0]
            
    return outlierless

###############################################################################
    
    
    
    
    
    
    
    
    
    
    
    
    