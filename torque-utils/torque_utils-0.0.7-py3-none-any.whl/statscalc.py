''' Statistical routines - statscalc
        developed by Victor Cossich (victor.cossich@gmail.com) and Conrado Torres (conradotl@gmail.com)
        for quick statistical procedures in pandas series and dataframes. Email us if you want. ;)

    	you need numpy,pandas and scipy.stats to run this module.
'''

import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
import scipy as sp
import pingouin as pg
 
###############################################################################   
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
            p_val = sp.stats.shapiro(data_set[var])[1]            
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
                p_log = sp.stats.shapiro(np.log10(data_set[var]))[1]                 
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

############################################################################### 0.0.5
def interday_reliability(list_of_trial_values,ICC=None):
    '''Provide intraclass correlation (ICC) in the ICC3 modality and standard error of the measure (SEM)
    according to Weir (2005) - DOI: 10.1519/15184.1
    list_of_trials: list with each measurement session data
    ICC=None: alternative ICC value to calculate the SEM
    '''
    ### create a long_format dataframe with the values
    # create a list of default values for subjects id
    subject=[str(item) for item in range(len(list_of_trial_values[0]))]* len(list_of_trial_values)
    # create a list with values seriated
    seriated_trial_values=[]
    [seriated_trial_values.extend(trial_values) for trial_values in list_of_trial_values]
    # create a list with the days id 
    day_id=[]
    for day in range(len(list_of_trial_values)):
        day_id.extend([str(day)]*len(list_of_trial_values[0]))
    # create the longformat dataframe
    long_format=pd.DataFrame({'subject':subject, 'values': seriated_trial_values, 'day':day_id})
    # compute anovas to obtain the variances itens from each source
    aov=pg.anova(data=long_format, dv='values',between='subject',detailed=1)
    between=aov.iloc[0]
    within=aov.iloc[1]
    rm_aov=pg.rm_anova(data=long_format, dv='values',within='day',subject='subject',detailed=1)
    trials=rm_aov.iloc[0]
    error=rm_aov.iloc[1]
    # if no ICC is passed, calculate the ICC3
    if ICC == None:
        ICC=((between['MS'] - error['MS']) / (between['MS'] + (trials['DF'] * error['MS'])))
    # calculate the SEM
    SEM = np.sqrt((between['SS'] + within['SS'])/(len(long_format)-1))*np.sqrt(1-ICC)
   
    return ICC,SEM
    
###############################################################################
def reliability_sample_size(p0,p1,n=2,beta=.2,alpha=.05):
    '''The sample size required to test if a given ICC value (p1) is greather than a specific value (p0)
    in n (=2) tests design with beta = .8 and alpha=.05
    p0: estimated value
    p1:reference value
    beta=.2: chance of false negatives
    beta=.05: chance of false positives
    '''
    teta0=p0/(1-p0)
    teta=p1/(1-p1)
    C0=(1+n*teta0)/(1+n*teta)
    U_alpha=sp.stats.norm.ppf(1-alpha)
    U_beta=sp.stats.norm.ppf(1-beta)
    k=1+((2*(U_alpha+U_beta)**2*n)/((np.log(C0))**2*(n-1)))
    
    return k  

###############################################################################
def pearson_r(sample1,sample2):
    ''' return the pearson product-moment correlation r
    '''
    x,y=pd.Series(sample1),pd.Series(sample2)
    n=len(x)
    nominator=n*sum(x*y)-sum(x)*sum(y)
    denominator=np.sqrt((n*sum(x**2)-sum(x)**2)*(n*sum(y**2)-sum(y)**2))
    r=nominator/denominator
   
    return r

###############################################################################
def CCC(sample1,sample2):
    ''' Calculate the concordance correlation coefficient according to Lin et al (2002)
    doi:10.1198/016214502753479392
    '''
    Mx,My=np.mean(sample1),np.mean(sample2)
    Sx,Sy=np.std(sample1),np.std(sample2)
    S2x,S2y=np.var(sample1),np.var(sample2)
    r=pearson_r(sample1,sample2)
    CCC=(2*r*Sx*Sy)/(S2x+S2y+(My-Mx)**2)
    return CCC
###############################################################################
def bland_altman_metrics(sample1,sample2,interval=0.95):
    '''provide Altman-Bland metric according to Carkeet (2015)
    doi:10.1097/OPX.0000000000000513
    sample1,sample2:observations to be analyzed
    interval=0.95: interval used to define confidence interval for the limits of agreement
    return: dataframe with mean error, upper and lower limits og agreament (LoA) and confidence intervals lenght
    for mean error and LoA 
    '''
    # obtain the cumulative chance of T for the given interval 
    half_interval=(1-interval)/2+interval
    n=len(sample1)
    Tci=sp.stats.t(df=n-1).ppf(half_interval)
    # build the result dataframe
    result=pd.DataFrame(index=[0])
    error=pd.Series(sample1)-pd.Series(sample2)
    result['mean error']=error.mean()
    result['mean CI']=Tci*(error.std()/np.sqrt(n))
    result['lower LoA']=error.mean() - 1.96*error.std()
    result['upper LoA']=error.mean() + 1.96*error.std()
    result['LoA CI']=Tci*np.sqrt(2.92)*(error.std()/np.sqrt(n))
  
    return result

    
    
    
    
    
    
    
    