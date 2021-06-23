import numpy as np
from .quality_assurance import test_h0
from .fit_tools import *

def assess_detectability (h0_result, threshold) :
  '''
  Consider results yielded by test_h0 function to assess detectability of a given 
  mode.
  ''' 
 
  if h0_result > threshold :
    detected = True
  else : 
    detected = False
  return detected

def clean_df (df) :
  '''
  Clean DataFrame of width, heights, split and angle lines when they do not correspond
  anymore to a mode to fit. 
  '''

  orders = np.unique (np.copy (df[0].to_numpy ().astype (np.str)))
  orders = orders[orders!='a']
  for o in orders :
    cond_mode = ((df[0].astype(np.str)==str(o))&((df[1].astype(np.str)=='0')|(df[1].astype(np.str)=='1'))) 
    if df.loc[cond_mode].empty :
      df = df.drop (labels=df.loc[(df[0].astype(np.str)==str(o))&(df[1].astype(np.str)=='a')].index)

  return df

def select_mode_to_fit (freq, psd, back, df, tmax=99) :
  '''
  Filter an input a2z DataFrame by considering frequentist H0 quick test on
  each l=0 or l=1 mode. 
  '''

  df.index = np.arange (df.index.size)
  pkb = a2z_to_pkb (df)
  test = test_h0 (freq, psd, back, pkb, tmax=tmax, only_tmax=False)
  test = np.c_[test[:,:3], np.sum (test[:,4:], axis=1)]

  for elt in test :
    if (int (elt[1])==0) | (int (elt[1])==1) :
      if int (elt[1])==0 :
        lweak = '2'
      else :
        lweak = '3'
      considered_modes = ((df[0].astype(np.str)==str (int (elt[0]))) & (df[1].astype(np.str)==str(int (elt[1])))) | \
                         ((df[0].astype(np.str)==str (int (elt[0])-1)) & (df[1].astype(np.str)==lweak))
      ind = df.loc[considered_modes].index
      detected = assess_detectability (elt[3], tmax//3)
      if not detected :
         df = df.drop (labels=ind, axis=0)

  df = clean_df (df)

  df = sort_a2z (df)

  return df
