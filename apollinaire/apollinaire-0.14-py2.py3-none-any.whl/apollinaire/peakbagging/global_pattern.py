# coding: utf-8

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from scipy.optimize import minimize
from .analyse_window import sidelob_param
from .fit_tools import *
from .modified_optimize import _minimize_powell
from .regressor import gp_predict, get_min_max_teff
from pathos.multiprocessing import ProcessPool
from .save_chain import save_sampled_chain
import numdifftools as nd
import emcee
import corner
import numba
import warnings


'''
Given some known input stellar parameters (DeltaNu, Numax), this file
contains necessary functions to fit global parameters and create
initial guess to give to the MLE/MCMC peakbagging pipeline for individual
mode fitting.
'''

def first_guess_mle (Dnu, numax, Teff, Hmax, Wenv, mass=None, return_bounds=False,
                     use_gp=True) :
  '''
  Use input parameters to design a first guess to feed the global_pattern fit in the MLE
    step. 
    >>>> eps, alpha, Dnu, numax, Hmax, Wenv, w, d02, d01 (if needed) <<<<

  :param Dnu: large frequency separation. Must be given in µHz.
  :type Dnu: float

  :param numax: maximum of power in p-mode envelope. Must be given in µHz.
  :type numax: float

  :param use_gp: set to ``True`` to guess epsilon with a gaussian process prediction.
    Optional, default ``True``.
  :type use_gp: bool
  '''
  global_param = np.zeros (13)
  low_bounds = np.zeros (13)
  up_bounds = np.zeros (13)
  # epsilon
  min_t, max_t = get_min_max_teff ()
  if Teff < min_t or Teff > max_t or Dnu < 20 :
    use_gp = False
  if use_gp :
    global_param[0] = gp_predict (Teff, plot_prediction=False)
  elif Dnu > 20 :
    global_param[0] = - 6.e-4 * Teff + 5.
  else :
    global_param[0] = 0.601 + 0.632 * np.log10 (Dnu) #Corsaro et al. 2012
  low_bounds[0] = 0.8 * global_param[0]
  up_bounds[0] = 1.2 * global_param[0]
  # alpha
  if Dnu < 20 :
    global_param[1] = 0.
    low_bounds[1] = 0.
  else :
    global_param[1] = 0.25
    low_bounds[1] = 0.15
  up_bounds[1] = 0.5
  # Dnu
  global_param[2] = Dnu
  low_bounds[2] = Dnu - Dnu/100.
  up_bounds[2] = Dnu + Dnu/100.
  # numax
  global_param[3] = numax
  low_bounds[3] = numax - numax/100.
  up_bounds[3] = numax + numax/100.
  # Hmax
  global_param[4] = Hmax
  low_bounds[4] = Hmax / 10 
  up_bounds[4] = 5 * Hmax 
  # Wenv
  global_param[5] = Wenv
  low_bounds[5] = 0.8 * Wenv
  up_bounds[5] = 1.2 * Wenv 
  # w 
  if Dnu < 20 :
    w = 0.1
  else :
    w = 6.2e-3 * Teff - 33.3
  if w < 0 :
    global_param[6] = 0.2
    low_bounds[6] = 1e-9
    up_bounds[6] = 5
  else :
    global_param[6] = w 
    low_bounds[6] = 0.2 * w
    up_bounds[6] = 3 * w
  # d02
  if Dnu > 125. :
    d02 = 8.
  elif (Dnu>20) & (Dnu < 80.) :
    d02 = 0.13*Dnu - 3.5
  elif Dnu < 20 :
    d02 = 0.121 * Dnu + 0.035 #Corsaro et al. 2012
  else :
    if mass is None :
      d02 = 7.5
    elif mass < 1. :
      d02 = 5.
    else : 
      d02 = 9.
  global_param[7] = d02 
  low_bounds[7] = 0.5 * d02
  if Dnu < 20 :
    up_bounds[7] = 1.1 * d02
  else :
    up_bounds[7] = 1.5 * d02
  # b02
  if Dnu < 20 :
    global_param[8] = 0
  else :
    global_param[8] = - 0.0027 * Dnu + 0.135
  low_bounds[8] = - 0.5
  up_bounds[8] = 0.5 
  # d01 
  if Dnu < 20 :
    global_param[9] = -0.021 * Dnu - 0.063 
    low_bounds[9] = 1.5 * global_param[9]
    up_bounds[9] = 0.5 * global_param[9]
  else :
    global_param[9] = 3.25
    low_bounds[9] = 0.5 * global_param[9]
    up_bounds[9] = 1.5 * global_param[9]
  # b01 
  if Dnu < 20 :
    global_param[10] = 0
  else : 
    global_param[10] = -0.1
  low_bounds[10] = -0.5
  up_bounds[10] = 0.5
  # d13 
  global_param[11] = Dnu / 12
  low_bounds[11] = 0.8 * global_param[11]
  up_bounds[11] = 2. * global_param[11]
  # b03 
  global_param[12] = 0.
  low_bounds[12] = -0.1
  up_bounds[12] = 0.5

  if return_bounds:
    bounds = np.c_[low_bounds, up_bounds]
    return global_param, bounds
  else :
    return global_param

def first_guess_mcmc (Dnu, numax, Teff, Hmax, Wenv, mass=None, return_bounds=False,
                      use_gp=True) :
  '''
  Use input parameters to design a first guess to feed the global_pattern fit in the MCMC step. 
    >>>> eps, alpha, Dnu, numax, Hmax, Wenv, w, d02, b02, d01, b01 (if needed) <<<<

  :param Dnu: large frequency separation. Must be given in µHz.
  :type Dnu: float

  :param numax: maximum of power in p-mode envelope. Must be given in µHz.
  :type numax: float

  :param use_gp: set to ``True`` to guess epsilon with a gaussian process prediction.
    Optional, default ``True``.
  :type use_gp: bool
  '''
  global_param = np.zeros (13)
  low_bounds = np.zeros (13)
  up_bounds = np.zeros (13)
  # epsilon
  min_t, max_t = get_min_max_teff ()
  if Teff < min_t or Teff > max_t or Dnu < 20 :
    use_gp = False
  if use_gp :
    global_param[0] = gp_predict (Teff, plot_prediction=False)
  elif Dnu > 20 :
    global_param[0] = - 6.e-4 * Teff + 4.8
  else :
    global_param[0] = 0.601 + 0.632 * np.log10 (Dnu) #Corsaro et al. 2012
  low_bounds[0] = 0.2 * global_param[0]
  up_bounds[0] = 2. * global_param[0]
  # alpha
  if Dnu < 20 :
    global_param[1] = 0.
  else :
    global_param[1] = 0.25
  low_bounds[1] = 0.
  up_bounds[1] = 1.
  # Dnu
  global_param[2] = Dnu
  low_bounds[2] = 0.9 * Dnu
  up_bounds[2] = 1.1 * Dnu
  # numax
  global_param[3] = numax
  low_bounds[3] = 0.9 * numax 
  up_bounds[3] = 1.1 * numax 
  # Hmax
  global_param[4] = Hmax
  low_bounds[4] = 0.1 * Hmax 
  up_bounds[4] = 5 * Hmax 
  # Wenv
  global_param[5] = Wenv
  low_bounds[5] = 0.2 * Wenv
  up_bounds[5] = 2. * Wenv 
  # w 
  if Dnu < 20 :
    w = 0.1
  else :
    w = 6.2e-3 * Teff - 33.3
  if w < 0 :
    global_param[6] = 0.2
    low_bounds[6] = 1e-9
    up_bounds[6] = 12
  else :
    global_param[6] = w 
    low_bounds[6] = min (1e-9, 0.1*w)
    up_bounds[6] = 20 * w
  # d02
  if Dnu > 125. :
    d02 = 8.
  elif (Dnu>20) & (Dnu < 80.) :
    d02 = 0.13*Dnu - 3.5
  elif Dnu < 20 :
    d02 = 0.121 * Dnu + 0.035 #Corsaro et al. 2012
  else :
    if mass is None :
      d02 = 7.5
    elif mass < 1. :
      d02 = 5.
    else : 
      d02 = 9.
  global_param[7] = d02 
  low_bounds[7] = 0.2 * d02
  up_bounds[7] = 2. * d02
  # b02
  if Dnu < 20 :
    global_param[8] = 0
  else :
    global_param[8] = - 0.0027 * Dnu + 0.135
  low_bounds[8] = - 1.5
  up_bounds[8] = 1.5 
  # d01 
  if Dnu < 20 :
    global_param[9] = -0.021 * Dnu - 0.063  
    low_bounds[9] = 2. * global_param[9]
    up_bounds[9] = 0.2 * global_param[9]
  else :
    global_param[9] = 3.25
    low_bounds[9] = 0.2 * global_param[9]
    up_bounds[9] = 2. * global_param[9]
  # b01 
  if Dnu < 20 :
    global_param[10] = 0
  else : 
    global_param[10] = -0.1
  low_bounds[10] = -1.5
  up_bounds[10] = 1.5
  # d13 
  global_param[11] = Dnu / 12 
  low_bounds[11] = 0.5 * global_param[11]
  up_bounds[11] = 4. * global_param[11]
  # b03 
  global_param[12] = 0.
  low_bounds[12] = -1.5
  up_bounds[12] = 1.5

  if return_bounds:
    bounds = np.c_[low_bounds, up_bounds]
    return global_param, bounds
  else :
    return global_param

def list_order_to_fit (numax, Dnu, n_order=3) :
  '''
  Create the list of order for which the pattern will be fitted.
  '''
  # the first step is to compute order closest to Numax. 
  ref_order = int (numax / Dnu) - 1 
  
  #dataframe is build order by order and then concatenated
  orders = list (range (max (1, ref_order - n_order//2), 
                        ref_order+n_order//2+1))
  orders = np.array (orders)

  return orders

def hide_modes (freq, psd, pkb, back, l=1, n_width=4, 
                remove_left=True, remove_zero_bin=True) :
  '''
  Hide PSD region around modes of given l.

  :param freq: frequency vector
  :type freq: ndarray

  :param psd: power vector
  :type psd: ndarray

  :param back: background power vector
  :type back: ndarray

  :param pkb: pkb array with modes parameters.
  :type pkb: ndarray

  :param l: mode degrees to remove. Optional, default ``1``.
  :type l: int

  :param n_width: frequency bins will be removed ``n_width`` from 
    the central frequency of the remaining modes. Optional, default ``4``.
  :type n_width: float

  :param remove_left: if set to ``True``, remove a region Dnu/2 wide
    before the first mode given in the pkb. Optional, default ``True``. 
  :type remove_left" bool

  :param remove_zero_bin: if set to ``True``, bins with zero values will be removed from
    returned vector. Optional, default ``True``.
  :type remove_zero_bin: bool 
  '''

  psd = np.copy (psd)
  dnu = np.mean (np.diff (pkb[pkb[:,1]==0, 2]))
  if pkb.shape[1]==20 :
    i_width = 8
  else :
    i_width = 6

  if remove_left : 
    w = pkb[0,i_width]
    f = pkb[0,2]
    cond = (freq>f-dnu/2)&(freq<f-n_width*w) 
    psd[cond] = 0 

  for ii, elt in enumerate (pkb) :
    if elt[1]==l :
      w = elt[i_width]
      if ii > 0 :
        f1 = pkb[ii-1, 2]
      else :
        f1 = elt[2] - dnu/2
      if ii+1 < pkb.shape[0] :
        f2 = pkb[ii+1, 2]
      else :
        f2 = elt[2] + dnu/2
      cond = (freq>f1+n_width*w)&(freq<f2-n_width*w) 
      psd[cond] = 0

  if remove_zero_bin :
    freq = freq[psd!=0]  
    back = back[psd!=0]  
    psd = psd[psd!=0]  
  
  return freq, psd, back

def remove_pattern (freq, psd, back, pkb, l=[0,2]) :
  '''
  Remove 

  :param freq: frequency vector
  :type freq: ndarray

  :param psd: power vector
  :type psd: ndarray

  :param back: background power vector
  :type back: ndarray

  :param pkb: pkb array with modes parameters.
  :type pkb: ndarray

  :param l: mode degrees to remove. Optional, default ``[0,2]``.
  :type l: int or array-like
  '''

  if pkb.shape[1]==20 :
    raise Exception ('This function cannot be used with an extended pkb array.' //
                     'Use a classical pkb instead.')

  pkb = pkb[np.isin (pkb[:,1], l),:]

  model = compute_model (freq, pkb)
  model = model + back
  psd = psd / model

  return psd

def override_epsilon (epsilon, param, bounds, mcmc=True) :
  ''' 
  Override epsilon value from what was computed by ``first_guess_mle`` and 
  ``first_guess_mcmc``.
  '''

  param[0] = epsilon
  if mcmc :
    bounds[0,0] = 0.2 * epsilon 
    bounds[0,1] = 2. * epsilon
  else :
    bounds[0,0] = 0.8 * epsilon
    bounds[0,1] = 1.2 * epsilon
    
  return param, bounds

def override_alpha (alpha, param, bounds, mcmc=True) :
  ''' 
  Override epsilon value from what was computed by ``first_guess_mle`` and 
  ``first_guess_mcmc``.
  '''

  param[1] = alpha
  if mcmc :
    bounds[1,0] = 0.2 * epsilon 
    bounds[1,1] = 2. * epsilon
  else :
    bounds[1,0] = 0.8 * epsilon
    bounds[1,1] = 1.2 * epsilon
    
  return param, bounds

def override_d02 (d02, param, bounds, mcmc=True) :
  ''' 
  Override d02 value from what was computed by ``first_guess_mle`` and 
  ``first_guess_mcmc``. Set curvature term to zero.
  '''

  param[7] = d02
  param[8] = 0
  if mcmc :
    bounds[7,0] = 0.2 * d02 
    bounds[7,1] = 2. * d02
  else :
    bounds[7,0] = 0.8 * d02
    bounds[7,1] = 1.2 * d02
    
  return param, bounds

def override_d01 (d01, param, bounds, mcmc=True) :
  ''' 
  Override d01 value from what was computed by ``first_guess_mle`` and 
  ``first_guess_mcmc``. Set curvature term to zero.
  '''

  param[9] = d01
  param[10] = 0
  if mcmc :
    bounds[9,0] = min (0.2*d01, 2*d01) 
    bounds[9,1] = max (0.2*d01, 2*d01)
  else :
    bounds[9,0] = min (0.8*d01, 1.2*d01)
    bounds[9,1] = max (0.8*d01, 1.2*d01)
    
  return param, bounds

def override_d13 (d13, param, bounds, mcmc=True) :
  ''' 
  Override epsilon value from what was computed by ``first_guess_mle`` and 
  ``first_guess_mcmc``. Set curvature term to zero.
  '''

  param[11] = d13
  param[12] = 0
  if mcmc :
    bounds[11,0] = min (0.2*d13, 2*d13) 
    bounds[12,1] = max (0.2*d13, 2*d13)
  else :
    bounds[11,0] = min (0.8*d13, 1.2*d13)
    bounds[12,1] = max (0.8*d13, 1.2*d13)
    
  return param, bounds

def override_width (w, param, bounds, mcmc=True) :
  ''' 
  Override width value from what was computed by ``first_guess_mle`` and 
  ``first_guess_mcmc``.
  '''

  param[6] = w
  if mcmc :
    bounds[6,0] = 1e-6 * w
    bounds[6,1] = 12 * w
  else :
    bounds[6,0] = 1e-9 * w
    bounds[6,1] = 5 * w
    
  return param, bounds


def pattern_to_a2z (eps, alpha, Dnu, numax, Hmax, Wenv, w, d02, b02=0., d01=None, b01=0., 
                    d13=None, b03=0., split=0, angle=90, orders=None, splitting_order=False,
                    angle_order=False, common_width=False) :
  '''
  Compute param_a2z that will be used to feed a2z_to_pkb function and then compute_model
  function.
  Lorentzian parameters are inferred from global_parameters given as input. 

  :param eps: phase term epsilon
  :type eps: float

  :param alpha: second order curvature term alpha
  :type alpha: float

  :param Dnu: large frequency separation. Must be given in µHz.
  :type Dnu: float

  :param numax: maximum of power in p-mode envelope. Must be given in µHz.
  :type numax: float

  :param Hmax: amplitude of p-mode envelope
  :type Hmax: float

  :param Wenv: width of p-mode envelope
  :type Wenv: float

  :param w: width of indiviudal p-modes
  :type w: float

  :param d02: small separation between l=0 and l=2 peaks.
  :type d02: float

  :param b02: derivative over n of d02.
  :type b02: float

  :param d01: separation between l=0 and l=1 terms. If an input is given, the function will
  compute guess for l=1 modes. Optional, default None.
  :type d01: float

  :param b01: derivative over n of d01.
  :type b01: float

  :param d13: separation between l=1 and l=3 terms. If an input is given, the function will
  compute guess for l=1 modes. Optional, default None.
  :type d13: float

  :param b03: derivative over n of d03.
  :type b03: float

  :param orders: list of orders on which the pattern will be fitted. 
    If ``None``, the function will create its own list of 3 orders using ``numax`` and ``Dnu``
    given as input. Optional, default ``None``.
  :type orders: list

  :param common_width: if set to ``True``, only a global width parameter will be set in the a2z
    DataFrame. Optional, default ``False``.
  :type common_width: bool

  :return: a2z guess as a pandas DataFrame
  :rtype: pandas DataFrame
  '''

  if orders is None :
    orders = list_order_to_fit (numax, Dnu)

  nmax = numax / Dnu - eps 

  for counter, n in enumerate (orders) :
    if d01 is None :
      k = 4
      index_l = np.array (['2', '0', 'a', 'a'])
      index_n = np.array ([str(n-1), str(n), str(n), str(n)])
      param = np.array (['freq', 'freq', 'height', 'width'])
      extent = np.array (['mode', 'mode', 'order', 'order'])
    if (d01 is not None) and (d13 is None) :
      k = 5
      index_l = np.array (['1', '2', '0', 'a', 'a'])
      index_n = np.array ([n, n-1, n, n, n])
      param = np.array (['freq', 'freq', 'freq', 'height', 'width'])
      extent = np.array (['mode', 'mode', 'mode', 'order', 'order'])
    if (d01 is not None) and (d13 is not None) :
      k = 6
      index_l = np.array (['3', '1', '2', '0', 'a', 'a'])
      index_n = np.array ([n-1, n, n-1, n, n, n])
      param = np.array (['freq', 'freq', 'freq', 'freq', 'height', 'width'])
      extent = np.array (['mode', 'mode', 'mode', 'mode', 'order', 'order'])
    value = np.zeros (k)
    err = np.zeros (k)
    fixed = np.zeros (k)
    l_bound = np.zeros (k)
    h_bound = np.zeros (k)
    data = np.c_[index_n, index_l, param, extent, value, err, fixed, l_bound, h_bound]
    if counter==0 :
      df = pd.DataFrame (data=data)
      df = df.astype (dtype={0:np.int_, 4:np.float_, 5:np.float_, 6:np.float_, 7:np.float_, 8:np.float_})
    else :
      aux_df = pd.DataFrame (data=data)
      aux_df = aux_df.astype (dtype={0:np.int_, 4:np.float_, 5:np.float_, 6:np.float_, 7:np.float_, 8:np.float_})
      df = pd.concat ([df, aux_df])

  # compute values and bounds
  df.loc [df[1]=='0', 4] = (df.loc[df[1]=='0', 0] + eps) * Dnu + alpha / 2. * np.power (df.loc[df[1]=='0', 0] - nmax, 2)
  nu0 = df.loc [df[1]=='0', 4].to_numpy ()
  df.loc [df[1]=='2', 4] = nu0 - d02 - b02 * (df.loc[df[1]=='2', 0] - nmax)
  if d01 is not None :
    df.loc [df[1]=='1', 4] = nu0 + Dnu/2 - d01 - b01 * (df.loc[df[1]=='1', 0] - nmax)
  if d13 is not None :
    nu1_aux = df.loc [df[1]=='1', 4].to_numpy () + b01 * (df.loc[df[1]=='1', 0].to_numpy () - nmax)
    df.loc [df[1]=='3', 4] = nu1_aux - d13 - b03 * (df.loc[df[1]=='3', 0] - nmax) 
  df.loc [df[2]=='height', 4] = Hmax * np.exp (-0.5 * np.power ((nu0 - numax)/Wenv, 2))
  df.loc [df[2]=='width', 4] = w
  #bounds for freq
  df.loc[df[2]=='freq',7] = df.loc[df[2]=='freq',4] - 3.e-3 * numax #this parameter is arbitrary and maybe will
  df.loc[df[2]=='freq',8] = df.loc[df[2]=='freq',4] + 3.e-3 * numax #have to be modified in the future
  if d13 is not None :
    df.loc[df[1]=='3', 8] = df.loc[df[1]=='3', 4] + d13 / 2 #setting bounds to avoid fitting l=3 over l=1 
    df.loc[df[1]=='1', 7] = df.loc[df[1]=='1', 4] - d13 / 2 
  # bounds for width and height
  df.loc[df[2]=='width',7] = 0.01 * df.loc[df[2]=='width',4]
  df.loc[df[2]=='width',8] = 10. * df.loc[df[2]=='width',4]
  df.loc[df[2]=='height',7] = 0.01 * df.loc[df[2]=='height',4]
  df.loc[df[2]=='height',8] = 10. * df.loc[df[2]=='height',4]

  if splitting_order :
    df_split = pd.DataFrame (data=orders)
    df_split[1] = 'a'
    df_split[2] = 'split'
    df_split[3] = 'order'
    df_split[4] = split
    df_split[5] = 0
    df_split[6] = 0
    df_split[7] = 0
    df_split[8] = 3.

    df = pd.concat ([df, df_split])

  if angle_order :
    df_angle = pd.DataFrame (data=orders)
    df_angle[1] = 'a'
    df_angle[2] = 'angle'
    df_angle[3] = 'order'
    df_angle[4] = angle
    df_angle[5] = 0
    df_angle[6] = 0
    df_angle[7] = 0
    df_angle[8] = 90.

    df = pd.concat ([df, df_angle])

  # creating global part of the dataframe
  index_n = np.array (['a', 'a', 'a', 'a', 'a', 'a']) 
  index_l = np.array (['a', 'a', '3', '1', '2', '0']) 
  param = np.array (['split', 'angle', 'amp_l', 'amp_l', 'amp_l', 'amp_l'])
  extent = np.array (['global', 'global', 'global', 'global', 'global', 'global'])
  value = np.array ([split, angle, 0.2, 1.5, 0.7, 1.])
  err = np.zeros (6)
  fixed = np.zeros (6)
  l_bound = np.zeros (6)
  h_bound = np.array ([max (1., 0.5*split), 90., 0., 0., 0., 0.])
  data = np.c_[index_n, index_l, param, extent, value, err, fixed, l_bound, h_bound]
  df_glob = pd.DataFrame (data=data) 
  df_glob = df_glob.astype (dtype={4:np.float_, 5:np.float_, 6:np.float_, 7:np.float_, 8:np.float_})

  # concatenate 
  df = pd.concat ([df, df_glob])

  # if needed, make slight modifications (for common_width for example)
  if common_width :
    df = df.loc[df[2]!='width']
    new_row_width = pd.DataFrame (data=[['a', 'a', 'width', 'global', w, 0, 0, 0.01*w, 10*w]])
    df = pd.concat ([df, new_row_width])

  return df

@numba.jit (nopython=True)
def wrapped_pattern_to_pkb_fast (eps, alpha, Dnu, numax, Hmax, Wenv, w, d02, b02=0, d01=None, b01=0,
                    d13=None, b03=0, split=0, angle=90, orders=None) :
  '''
  Directly compute a pkb file from the pattern parameters. 
  '''

  nmax = numax / Dnu - eps
  ratio_h = np.array ([1., 1.5, 0.7, 0.2])
  
  degrees = np.array ([0, 2])
  if d01 != -9999 :
    degrees = np.append (degrees, 1)
  if d13 != -9999 :
    degrees = np.append (degrees, 3)
  nmode = orders.size * degrees.size

  pkb = np.zeros ((nmode, 14))

  ii = 0
  for n in orders :
    for l in degrees :
      nu0 = (n+eps) * Dnu + alpha / 2. * np.power (n-nmax, 2)
      if l==0 :
        f = nu0
      elif l==1 :
        f = nu0 + Dnu/2 - d01 - b01 * (n-nmax)
      elif l==2 :
        f = nu0 - d02 - b02 * (n-nmax)
      elif l==3 :
        f = nu0 + Dnu/2 - d01 - d13 - b03 * (n-nmax) 

      h = Hmax * np.exp (-0.5 * np.power ((nu0 - numax)/Wenv, 2)) * ratio_h[l]
      if l>=2 :
        pkb[ii, 0] = n-1
      else :
        pkb[ii, 0] = n
      pkb[ii, 1] = l
      pkb[ii, 2] = f
      pkb[ii, 4] = h
      pkb[ii, 6] = w

      ii += 1

  return pkb

def pattern_to_pkb_fast (eps, alpha, Dnu, numax, Hmax, Wenv, w, d02, b02=0, d01=None, b01=0,
                    d13=None, b03=0, split=0, angle=90, orders=None) :
  '''
  Directly compute a pkb file from the pattern parameters. 
  '''
  if d13 is None :
    d13 = - 9999
  if d01 is None :
    d01 = - 9999
  
  pkb = wrapped_pattern_to_pkb_fast (eps, alpha, Dnu, numax, Hmax, Wenv, w, d02, b02=b02, d01=d01, b01=b01,
                    d13=d13, b03=b03, split=split, angle=angle, orders=orders)
  return pkb

def pattern_to_pkb (eps, alpha, Dnu, numax, Hmax, Wenv, w, d02, b02=0, d01=None, b01=0,
                    d13=None, b03=0, split=0, angle=90, orders=None, fast=True) :

  '''
  Use pkb parameters to generate a pkb array.

  This function is just a wrapper of pattern_to_a2z and a2z_to_pkb if ``fast`` is set to ``False``.
  '''

  if fast :
    param_pkb = pattern_to_pkb_fast (eps, alpha, Dnu, numax, Hmax, Wenv, w, d02, b02=b02, d01=d01, b01=b01,
                                     d13=d13, b03=b03, split=split, angle=angle, orders=orders)

  else :
    df = pattern_to_a2z (eps, alpha, Dnu, numax, Hmax, Wenv, w, d02, b02=b02, d01=d01, b01=b01,
                         d13=d13, b03=b03, split=split, angle=angle, orders=orders)
    param_pkb = a2z_to_pkb (df)

  return param_pkb


def log_prior (param, bounds) :
  '''
  Compute positive log_prior probability for MCMC framework. Uninformative priors are used.  

  :param param: parameters to fit. Optional, default None.
  :type param: 1d ndarray

  :param bounds: for parameters with assumed prior uniform distribution, bounds of 
  the uniform distribution.
  :type bounds: ndarray

  :return: prior value for the given parameters.
  :rtype: float 
  '''

  cond = (param<bounds[:,0])|(param>bounds[:,1])
  if np.any (cond) :
    return - np.inf

  extent = bounds[:,1] - bounds[:,0]
  individual_prior = 1. / extent #assuming uniform law for all given parameters.
  prior = np.prod (individual_prior)
  l_prior = np.log (prior)

  return l_prior

def log_likelihood_pattern (param_pattern, freq, psd, back, orders, split=0, angle=90, param_wdw=None, 
                            ) :
  '''
  Compute logarithmic likelihood for a given power spectrum, with a model built only with a global
  pattern (no fit of individual mode).

  :param param_pattern: param of the global pattern to adjust. They must be given in the following order:
  >>>> eps, alpha, Dnu, numax, Hmax, Wenv, w, d02, b02, d01, b01 (if needed) <<<<
  :type param_pattern: ndarray

  :param freq: frequency vector
  :type freq: ndarray

  :param psd: real power vector
  :type freq: ndarray

  :param orders: list of orders on which the pattern will be fitted. 
  :type orders: list

  :return: logarithmic likelihood of the model
  :rtype: ndarray
  '''

  # Retrieve the width parameter from its logarithm
  param_pattern[6] = np.exp (param_pattern[6])

  param_pkb = pattern_to_pkb (*param_pattern, split=split, angle=angle, orders=orders)

  model = compute_model (freq, param_pkb, param_wdw=param_wdw)
  model = model / back
  model += 1. #we fit on SNR

  aux = psd / model + np.log (model)
  log_l = np.sum (aux)

  return log_l

def log_probability_pattern (param_to_fit, freq, psd, bounds, back, orders, split=0, angle=90, param_wdw=None,
                             norm=None) : 
  '''
  Compute the positive posterior log probability (unnormalised) of the parameters to fit. 

  :param_to_fit: backgrounds parameters to fit.
  :type param_to_fit: 1d ndarray
 
  :param param: param to fit passed by perform_mle_back. Param are given in 
  the following order: Harvey law parameters, power law parameters, Gaussian p-mode 
  envelope parameters, noise constant. 

  :param freq: frequency vector in µHz.
  :type freq: ndarray

  :param psd: power density vector in ppm^2/µHz or (m/s)^2/µHz.
  :type psd: ndarray

  :param orders: list of orders on which the pattern will be fitted. 
  :type orders: list

  :param norm: if given, the param_to_fit and bounds input vectors will be multiplied by this vector. 
  Optional, default None.
  :type norm: ndarray

  :return: posterior probability value
  :rtype: float
  '''

  param_to_fit = np.copy (param_to_fit) #make a copy to not modify the reference array
  bounds = np.copy (bounds)

  if norm is not None :
    param_to_fit = param_to_fit * norm
    bounds[:,0] = bounds[:,0] * norm
    bounds[:,1] = bounds[:,1] * norm

  l_prior = log_prior (param_to_fit, bounds)

  if not np.isfinite (l_prior) :
    return - np.inf

  l_likelihood = - log_likelihood_pattern (param_to_fit, freq, psd, back, orders, split, angle, param_wdw, 
                                           )

  l_proba = l_prior + l_likelihood

  return l_proba

def visualise (param_pattern, freq, psd, back, param_pattern_2=None, filename=None, 
               orders=None, split=0, angle=90, snr=True, param_wdw=None, show=False) :
  '''
  Allow to visualise the considered global_model. May take an optional argument 
  param_pattern_2 to compare two patterns (for example guess and model fitted). 

  :param param_pattern: param of the global pattern. They must be given in the following order:
  >>>> eps, alpha, Dnu, numax, Hmax, Wenv, w, d02, d01 (if needed) <<<<
  :type param_pattern: ndarray

  :param freq: frequency vector
  :type freq: ndarray

  :param psd: real power vector
  :type freq: ndarray

  :param back: activity background vector that will be used to complete the model to fit. 
  Must have the same length than freq and psd. 
  :type back: ndarray

  :param param_pattern_2: param of an additionnal global pattern. They must be given in the following order:
  >>>> eps, alpha, Dnu, numax, Hmax, Wenv, w, d02, d01 (if needed) <<<<
  Optional, default None. 
  :type param_pattern: ndarray

  :param filename: if given, will save the shown figure at the following destination. 'show'
  argument must have been set to ``True``. Optional, default None.  
  :type filename: str

  :param orders: list of orders on which the pattern will be fitted. 
  :type orders: list

  :param snr: whether to plot or not on signal to noise data representation. Optional, default ``True``.
  :type snr: bool
  '''

  fig = plt.figure (figsize=(12,6))
  ax = fig.add_subplot (111)

  param_pkb = pattern_to_pkb (*param_pattern, split=split, angle=angle, orders=orders)
  model = compute_model (freq, param_pkb, param_wdw=param_wdw)
  if snr :
    model = model / back + 1.
    psd = psd/back
  else : 
    model += back
  
  psd_s = smooth (psd, 50) #smoothing of psd

  ax.plot (freq, psd, color='darkgrey')
  ax.plot (freq, psd_s, color='black')

  if param_pattern_2 is not None :
    param_pkb_2 = pattern_to_pkb (*param_pattern_2, split=split, angle=angle, orders=orders)
    model_2 = compute_model (freq, param_pkb_2, param_wdw=param_wdw)
    if snr :
      model_2 = model_2 / back + 1.
    else : 
      model_2 += back
    ax.plot (freq, model_2, '--', color='green')

  ax.plot (freq, model, color='red')

  ax.set_xlabel (r'Frequency ($\mu$Hz)')

  if snr :
    ax.set_ylabel ('PSD (signal to noise ratio)')
  else :
    ax.set_ylabel ('PSD')

  if filename is not None :
    plt.savefig (filename)

  if show :
    plt.show ()

  plt.close ()

  return

def perform_mle_pattern (Dnu, numax, Hmax, Wenv, Teff, freq, psd, 
                         back=None, wdw=None, method=_minimize_powell,
                         n_order=3, split=0, angle=90, fit_l1=False, fit_l3=False, 
                         mass=None, guess=None, show=True, filename=None,
                         epsilon=None, width=None, alpha=None, d02=None,
                         d01=None, d13=None) :
                        
  '''
  Perform minimization of the log likelihood function according to the parameters set to vary.

  :param Dnu: large frequency separation. Must be given in µHz.
  :type Dnu: float

  :param numax: maximum of power in p-mode envelope. Must be given in µHz.
  :type numax: float

  :param freq: frequency vector
  :type freq: ndarray

  :param psd: real power vector
  :type freq: ndarray

  :param back: activity background vector that will be used to complete the model to fit. Optional default None.
  Must have the same length than freq and psd. 
  :type back: ndarray.

  :n_order: number of orders for which to create the guess frame. Optional, default 3. 
  :type n_order: int

  :param fit_l1: set to ``True`` to fit the d01 and b01 param and create guess for l=1 modes. Optional, default ``False``.
  :type fit_l1: bool

  :param fit_l3: set to ``True`` to fit the d13 and b03 param and create guess for l=3 modes. Optional, default ``False``.
    ``fit_l1`` must be set to ``True``. 
  :type fit_l3: bool

  :param mass: mass of the star, in solar mass. Optional, default None.
  :type mass: float

  :param guess: MLE will take it as first guess of param if given. Optional, default None.
  Parameters must be given in the following order:
  >>>> eps, alpha, Dnu, numax, Hmax, Wenv, w, d02, d01 (if fit_l1 is set to ``True``) <<<<
  :type guess: array-like

  :param show: if set to ``True``, will plot a summary plot of guess (blue) and fitted (red) 
  pattern.
  :type show: bool

  :param filename: if given, will save the shown figure at the following destination. 'show'
  argument must have been set to ``True``. Optional, default None.  
  :type filename: str

  :param epsilon: epsilon value for global pattern guess. If specified, this value will override epsilon guess value
    computed by the function ``first_guess_mle``. Optional, default ``None``. 
  :type epsilon: float

  :param width: mode width value for global pattern guess. If specified, this value will override width guess value
    computed by the function ``first_guess_mle``. Optional, default ``None``. 
  :type width: float

  :param alpha: alpha value for global pattern guess. If specified, this value will override guess value
    computed by the function ``first_guess_mle``. Optional, default ``None``. 
  :type alpha: float

  :param d02: d02 value for global pattern guess. If specified, this value will override guess value
    computed by the function ``first_guess_mle``. Optional, default ``None``. 
  :type d02: float

  :param d01: d01 value for global pattern guess. If specified, this value will override guess value
    computed by the function ``first_guess_mle``. Optional, default ``None``. 
  :type d01: float

  :param d13: d13 value for global pattern guess. If specified, this value will override guess value
    computed by the function ``first_guess_mle``. Optional, default ``None``. 
  :type d13: float

  :return: updated df_a2z
  :rtype: pandas DataFrame
  '''

  if guess is None :
    guess, bounds = first_guess_mle (Dnu, numax, Teff, Hmax, Wenv, mass=mass, return_bounds=True)

  if epsilon is not None :
    guess, bounds = override_epsilon (epsilon, guess, bounds, mcmc=False)
  if alpha is not None :
    guess, bounds = override_alpha (alpha, guess, bounds, mcmc=False)
  if d02 is not None :
    guess, bounds = override_d02 (d02, guess, bounds, mcmc=False)
  if d01 is not None :
    guess, bounds = override_d01 (d01, guess, bounds, mcmc=False)
  if d13 is not None :
    guess, bounds = override_d13 (d13, guess, bounds, mcmc=False)
  if width is not None :
    guess, bounds = override_width (width, guess, bounds, mcmc=False)

  param = np.copy (guess)

  labels = np.array (['eps', 'alpha', 'Dnu', 'numax', 'Hmax', 'Wenv', 'w', 'd02', 
                      'b02', 'd01', 'b01', 'd13', 'b03'])

  orders = list_order_to_fit (numax, Dnu, n_order=n_order)

  if not fit_l1 :
    fit_l3 = False

  if not fit_l3 :
    guess = guess[:len(labels)-2]
    param = param[:len(labels)-2]
    bounds = bounds[:len(labels)-2,:]
    labels = labels[:len (labels)-2]

  if not fit_l1 :
    guess = guess[:len(labels)-2]
    param = param[:len(labels)-2]
    bounds = bounds[:len(labels)-2,:]
    labels = labels[:len (labels)-2]

  check_bounds (guess, bounds[:,0], bounds[:,1], labels=labels)

  cp_guess = np.reshape (guess, (1,guess.size))
  summary_guess = pd.DataFrame (data=cp_guess, columns=labels)
  df_guess = pattern_to_a2z (*param, split=split, angle=angle, orders=orders)

  # Transform width parameter to fit its logarithm
  param[6] = np.log (param[6])
  bounds[6,:] = np.log (bounds[6,:])

  if method is _minimize_powell :
    lb = bounds[:,0]
    ub = bounds[:,1]
    bounds = (lb, ub)

  if back is None :
    back = np.full (psd.size, 1.)

  jac=None
  options=None
  tol=None

  if (method=='TNC') :
    options = {'disp':True, 'maxiter':30, 'ftol':10.}
    jac = nd.Jacobian (log_likelihood_pattern)   
    print ('Jacobian computed')

  if wdw is not None :
    dt = 1 / (2*freq[-1])
    param_wdw = sidelob_param (wdw, dt=dt)
  else :
    param_wdw = None

  low_bound_freq = np.amin (df_guess.loc[df_guess[2]=='freq',4].to_numpy ()) - 0.2*Dnu
  up_bound_freq = np.amax (df_guess.loc[df_guess[2]=='freq',4].to_numpy ()) + 0.2*Dnu

  aux_freq = freq[(freq>low_bound_freq)&(freq<up_bound_freq)]
  aux_psd = (psd/back)[(freq>low_bound_freq)&(freq<up_bound_freq)]
  aux_back = back[(freq>low_bound_freq)&(freq<up_bound_freq)]

  
  print ('Global pattern likelihood minimisation:')
  with warnings.catch_warnings () :
    warnings.filterwarnings('ignore')
    result = minimize (log_likelihood_pattern, param, 
              args=(aux_freq, aux_psd, aux_back, orders, split, angle, param_wdw),
              bounds=bounds, method=method, jac=jac, options=options, tol=tol)

  print (result.message)

  param_fitted = result.x
  # Make the inverse transformation for width 
  param_fitted[6] = np.exp (param_fitted[6])

  summary_result = pd.DataFrame (data=np.reshape (param_fitted, (1,len(labels))), columns=labels)

  df_a2z = pattern_to_a2z (*param_fitted, split=split, angle=angle, orders=orders)

  visualise (param_fitted, aux_freq, aux_psd*aux_back, aux_back, param_pattern_2=guess, filename=filename,
               orders=orders, split=split, angle=angle, snr=True, param_wdw=param_wdw, show=show) 

  return df_a2z, param_fitted

def explore_distribution_pattern (Dnu, numax, Hmax, Wenv, Teff, freq, 
                                  psd, back=None, wdw=None,
                                  n_order=3, split=0, angle=90, fit_l1=False, 
                                  fit_l3=False, mass=None, guess=None, show=True,
                                  show_corner=True, nsteps=1000, filename=None, 
                                  parallelise=False, progress=False, 
                                  nwalkers=64, filemcmc=None, coeff_discard=50, 
                                  thin=1, save_only_after_sampling=False,
                                  epsilon=None, width=None, alpha=None, d02=None,
                                  d01=None, d13=None,
                                  bins=100, existing_chains='read') :
                        
  '''
  Perform minimization of the log likelihood function according to the parameters set to vary.

  :param Dnu: large frequency separation. Must be given in µHz.
  :type Dnu: float

  :param numax: maximum of power in p-mode envelope. Must be given in µHz.
  :type numax: float

  :param freq: frequency vector
  :type freq: ndarray

  :param psd: real power vector
  :type freq: ndarray

  :param back: activity background vector that will be used to complete the model to fit. Optional default None.
    Must have the same length than freq and psd. 
  :type back: ndarray.

  :n_order: number of orders for which to create the guess frame. Optional, default 3. 
  :type n_order: int

  :param fit_l1: set to ``True`` to fit the d01 and b03 param and create guess for l=1 modes. Optional, default ``False``.
  :type fit_l1: bool

  :param fit_l3: set to ``True`` to fit the d13 and b03 param and create guess for l=3 modes. Optional, default ``False``.
    ``fit_l1`` must be set to ``True``. 
  :type fit_l3: bool

  :param mass: mass of the star, in solar mass. Optional, default None.
  :type mass: float

  :param guess: MCMC will take it as first guess of param if given. Optional, default None.
    Parameters must be given in the following order:
    >>>> eps, alpha, Dnu, numax, Hmax, Wenv, w, d02, d01 (if fit_l1 is set to ``True``) <<<<
  :type guess: array-like

  :param show: if set to ``True``, will plot a summary plot of guess (blue) and fitted (red) 
    pattern.
  :type show: bool

  :param filename: if given, will save the shown figure at the following destination. 'show'
    argument must have been set to ``True``. Optional, default None.  
  :type filename: str

  :param filemcmc: name of the hdf5 where to store the chain. If filename is None, the name will not
    be stored. Optional, default None.
  :type filename: string

  :param parallelise: If set to ``True``, use Python multiprocessing tool to parallelise process.
    Optional, default ``False``.
  :type parallelise: bool

  :param show: if set to ``True``, will show at the end a plot summarising the fit. Optional, default ``True``.
  :type show: bool

  :param show: if set to ``True``, will show the corner plot summarising the MCMC process. 
    If ``filemcmc`` is specified, the plot will also be saved as a pdf file. Optional, default ``True``.
  :type show: bool

  :param coeff_discard: coeff used to compute the number of values to discard: total amount of
    sampled values will be divided by coeff_discard. Optional, default 50.
  :type coeff_discard: int

  :param thin: take only every ``thin`` steps from the chain. Optional, default 1. 
  :type thin: int

  :param save_only_after_sampling: if set to True, hdf5 file with chains information will only be saved at the end of the sampling
    process. If set to False, the file will be saved step by step (see ``emcee`` documentation).
  :type saveon_only_after_sampling: bool

  :param epsilon: epsilon value for global pattern guess. If specified, this value will override epsilon guess value
    computed by the function ``first_guess_mcmc``. Optional, default ``None``. 
  :type epsilon: float

  :param width: mode width value for global pattern guess. If specified, this value will override width guess value
    computed by the function ``first_guess_mcmc``. Optional, default ``None``. 
  :type width: float

  :param alpha: alpha value for global pattern guess. If specified, this value will override guess value
    computed by the function ``first_guess_mcmc``. Optional, default ``None``. 
  :type alpha: float

  :param d02: d02 value for global pattern guess. If specified, this value will override guess value
    computed by the function ``first_guess_mcmc``. Optional, default ``None``. 
  :type d02: float

  :param d01: d01 value for global pattern guess. If specified, this value will override guess value
    computed by the function ``first_guess_mcmc``. Optional, default ``None``. 
  :type d01: float

  :param d13: d13 value for global pattern guess. If specified, this value will override guess value
    computed by the function ``first_guess_mcmc``. Optional, default ``None``. 
  :type d13: float

  :param bins: number of bins for each cornerplot panel. Optional, default 100.
  :type bins: int

  :param existing_chains: controls the behaviour of the function concerning existing hdf5 files. If, ``read``, existing files will be read
    without sampling and function output will be updated consequently, if ``reset``, the backend will be cleared and the chain will 
    be sampled from scratch, if ``sample`` the function will sample the chain from where the previous exploration was stopped.
    Optional, default ``read``.
  :type existing_chains: str

  :return: updated df_a2z with relevant sigmas as determined by the MCMC walks.
  :rtype: pandas DataFrame
  '''

  if existing_chains=='ignore' :
    existing_chains = 'read'

  if existing_chains not in ['read', 'reset', 'sample'] :
    raise Exception ("Unknown value for existing_chains, must be 'read', 'reset' or 'sample'")

  if save_only_after_sampling and existing_chains=='sample' :
    raise Exception ("save_only_after_sampling=True and existing_chains='sample' are incompatible options.")

  if guess is None :
    guess, bounds = first_guess_mcmc (Dnu, numax, Teff, Hmax, Wenv, mass=mass, return_bounds=True)
  else :
    xxx, bounds = first_guess_mcmc (Dnu, numax, Teff, Hmax, Wenv, mass=mass, return_bounds=True)

  if epsilon is not None :
    guess, bounds = override_epsilon (epsilon, guess, bounds, mcmc=True)
  if alpha is not None :
    guess, bounds = override_alpha (alpha, guess, bounds, mcmc=True)
  if d02 is not None :
    guess, bounds = override_d02 (d02, guess, bounds, mcmc=True)
  if d01 is not None :
    guess, bounds = override_d01 (d01, guess, bounds, mcmc=True)
  if d13 is not None :
    guess, bounds = override_d13 (d13, guess, bounds, mcmc=True)
  if width is not None :
    guess, bounds = override_width (width, guess, bounds, mcmc=True)

  param = np.copy (guess)

  labels = np.array (['eps', 'alpha', 'Dnu', 'numax', 'Hmax', 'Wenv', 'w', 'd02', 
                      'b02', 'd01', 'b01', 'd13', 'b03'])
  orders = list_order_to_fit (numax, Dnu, n_order=n_order)

  if not fit_l1 :
    fit_l3 = False

  if not fit_l3 :
    guess = guess[:len(labels)-2]
    param = param[:len(labels)-2]
    bounds = bounds[:len(labels)-2,:]
    labels = labels[:len (labels)-2]

  if not fit_l1 :
    guess = guess[:len(labels)-2]
    param = param[:len(labels)-2]
    bounds = bounds[:len(labels)-2,:]
    labels = labels[:len (labels)-2]

  check_bounds (guess, bounds[:,0], bounds[:,1], labels=labels)

  cp_guess = np.reshape (guess, (1,guess.size))
  summary_guess = pd.DataFrame (data=cp_guess, columns=labels) 
  df_guess = pattern_to_a2z (*param, split=split, angle=angle, orders=orders)

  if back is None :
    back = np.full (psd.size, 1.)

  if wdw is not None :
    dt = 1 / (2*freq[-1])
    param_wdw = sidelob_param (wdw, dt=dt)
  else :
    param_wdw = None

  # Transform width parameter to fit its logarithm
  param[6] = np.log (param[6])
  bounds[6,:] = np.log (bounds[6,:])

  low_bound_freq = np.amin (df_guess.loc[df_guess[2]=='freq',4].to_numpy ()) - 0.2*Dnu
  up_bound_freq = np.amax (df_guess.loc[df_guess[2]=='freq',4].to_numpy ()) + 0.2*Dnu

  aux_freq = freq[(freq>low_bound_freq)&(freq<up_bound_freq)]
  aux_psd = (psd/back)[(freq>low_bound_freq)&(freq<up_bound_freq)]
  aux_back = back[(freq>low_bound_freq)&(freq<up_bound_freq)]

  norm = np.abs (param)
  norm[norm==0] = 1

  if parallelise :
    pool = ProcessPool ()
  else :
    pool = None

  param_to_pass = np.copy (param)
  bounds_to_pass = np.copy (bounds)

  #normalisation step
  param_to_pass = param_to_pass / norm
  bounds_to_pass[:,0] = bounds_to_pass[:,0] / norm
  bounds_to_pass[:,1] = bounds_to_pass[:,1] / norm

  pos = param_to_pass + 1e-4 * np.random.randn(nwalkers, param_to_pass.size)
  nwalkers, ndim = pos.shape
  pos[:,1] = np.abs (pos[:,1]) #alpha may be initialised near zero

  run_sampler = True
  if filemcmc is not None :
    if path.exists (filemcmc) :
      if existing_chains=='read' :
        print (filemcmc + " already exists, existing chains set to 'read', no sampling has been performed, proceeding to next step.")
        sampler = emcee.backends.HDFBackend(filemcmc, read_only=True)
        run_sampler = False
      elif existing_chains=='reset' :
        os.remove (filemcmc)
        backend = emcee.backends.HDFBackend(filemcmc)
        backend.reset(nwalkers, ndim)
        print (filemcmc + " already exists, existing chains set to 'reset', file has been deleted and a new file has been created instead.")
      elif existing_chains=='sample' :
        backend = emcee.backends.HDFBackend(filemcmc)
        pos = None
        print (filemcmc + " already exists, existing chains set to 'sample', sampling will restart from where it stopped.")
    else :
      backend = emcee.backends.HDFBackend(filemcmc)
      backend.reset(nwalkers, ndim) 

    #saving parameters name and normalisation information
    filemcmc_info = filemcmc[:len(filemcmc)-3] + '.dat'
    np.savetxt (filemcmc_info, np.c_[norm], fmt='%-s') 

    if save_only_after_sampling :
      # I have deliberately created the file to signal to other process that this chain is being
      # sampled
      backend = None
  else :
    backend = None

  if run_sampler :
    print ('Beginning fit')
    sampler = emcee.EnsembleSampler(nwalkers, ndim, log_probability_pattern, 
                                    args=(aux_freq, aux_psd, bounds_to_pass, aux_back, orders, split, angle, param_wdw, 
                                    norm), 
                                    backend=backend, pool=pool)
    sampler.run_mcmc(pos, nsteps, progress=progress)

    if filemcmc is not None :
      if save_only_after_sampling :
        save_sampled_chain (filemcmc, sampler, ndim, nwalkers, nsteps)

  discard = nsteps // coeff_discard

  if show_corner :
    make_cornerplot (sampler, ndim, discard, thin, labels, norm, filemcmc=filemcmc, bins=bins)

  flat_samples = sampler.get_chain(discard=discard, thin=thin, flat=True)
  centiles = np.percentile(flat_samples, [16, 50, 84], axis=0) * norm 

  # Transform back width distribution
  centiles[:,6] = np.exp (centiles[:,6])

  param_fitted = centiles[1,:]
  sigma_fitted = np.maximum (centiles[1,:] - centiles[0,:], centiles[2,:] - centiles[1,:])


  summary_result = pd.DataFrame (data=np.reshape (param_fitted, (1,len(labels))), columns=labels)

  df_a2z = pattern_to_a2z (*param_fitted, split=split, angle=angle, orders=orders)

  visualise (param_fitted, aux_freq, aux_psd*aux_back, aux_back, param_pattern_2=guess, filename=filename,
               orders=orders, split=split, angle=angle, snr=True, param_wdw=param_wdw, show=show) 

  return df_a2z, param_fitted, sigma_fitted


