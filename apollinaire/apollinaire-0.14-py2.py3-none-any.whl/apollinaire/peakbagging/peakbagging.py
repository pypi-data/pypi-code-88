# coding: utf-8

import pandas as pd
import numpy as np
from .likelihood import perform_mle
from .hessian import evaluate_precision
from .fit_tools import (read_a2z, plot_from_param, a2z_to_pkb, check_a2z, 
                        amp_to_height, a2z_to_cf, a2z_to_pkb, sort_pkb)
from .bayesian import wrap_explore_distribution 
from .chain_reader import cf_to_pkb_extended
from os import path

def dnu_from_df (df_a2z) :
  '''
  Compute Dnu from l=0 frequency values.
  '''

  l0_freq = df_a2z.loc[(df_a2z[1]=='0')&(df_a2z[2]=='freq'), 4].to_numpy ()
  if l0_freq.size<2:
    return None
  l0_freq = np.sort (l0_freq)
  dnu = np.median (np.diff (l0_freq))

  return dnu

def restrict_input (df) :

  '''
  Restrict input that is used to fit the model. Can increase computation performances
  and reduce the asymmetry wing effect when considering Nigam-Kosovichev implementation of 
  asymmetry. 
  '''

  cond = (df[6]==0)|(df[0]=='a')
  df_out = df.loc[cond]

  return df_out

def preprocess_df (df_a2z, restrict, remove_asymmetry_outside_window) :

  if restrict :
    df_in = restrict_input (df_a2z)
  else :
    df_in = df_a2z.copy ()
  if remove_asymmetry_outside_window :
    df_in.loc[(df_in[2]=='asym')&(df_in[6]!=0), 4] = np.zeros (((df_in[2]=='asym')&(df_in[6]!=0)).size)

  return df_in
  

def define_window (df_a2z, strategy, dnu=135., do_not_use_dnu=False, size_window=None) :
  '''
  Define frequency window that will be used for the fit.

  :param modes: if strategy is set to ``pair``, adapt the window 
    wether the code deals with a 02 or 13 pair. 
  '''

  #automatic determination of low and up bound for the window over which the 
  #fit is realised.
  frequencies = df_a2z.loc[(df_a2z[6]==0)&(df_a2z[2]=='freq'), 4].to_numpy ()
  low_freq = np.amin (frequencies)
  up_freq = np.amax (frequencies)

  if strategy=='pair' :
    center_freq = np.mean (frequencies)
    if center_freq > 2500 :
      coeff = 37.5
    elif center_freq > 2000 :
      coeff = 27.5
    elif center_freq > 1200 :
      coeff = 17.5
    if dnu is not None :
      low_bound = center_freq - coeff * dnu / 135.
      up_bound = center_freq + coeff * dnu / 135.
    if (center_freq < 1200)|(do_not_use_dnu) :
      d = 1
      gap = up_freq - low_freq
      low_bound = low_freq - gap / d
      up_bound = up_freq + gap / d

  if strategy=='order' :
    d = 3
    gap = up_freq - low_freq
    low_bound = low_freq - gap / d
    up_bound = up_freq + gap / d

  if strategy=='global' :
    d = 20
    gap = up_freq - low_freq
    low_bound = low_freq - gap / d
    up_bound = up_freq + gap / d

  if size_window is not None :
    center_freq = (up_freq + low_freq)/2 
    low_bound = center_freq - size_window/2
    up_bound = center_freq + size_window/2 


  print ('Window width: {:.1f} muHz'.format (up_bound-low_bound))

  return up_bound, low_bound

def check_leak (df, low_bound, up_bound) :
  '''
  Check if guess values of l=4 or l=5 are inside the window 
  and add the parameters for fit if needed. 
  '''
  
  cond = ((df[2]=='freq')&((df[1]=='4')|(df[1]=='5'))&(df[4]>low_bound)&(df[4]<up_bound))
  df.loc[cond, 6] = 0

  cond_l4 = (df[2]=='freq')&(df[1]=='4')&(df[4]>low_bound)&(df[4]<up_bound)
  if not df.loc[cond_l4].empty :
    print ('n=', df.loc[cond_l4, 0].values, 'l=4 will be fitted') 
  cond_l5 = (df[2]=='freq')&(df[1]=='5')&(df[4]>low_bound)&(df[4]<up_bound)
  if not df.loc[cond_l5].empty :
    print ('n=', df.loc[cond_l5, 0].values, 'l=5 will be fitted') 

  return df

def update_with_centiles (df_a2z, input_centiles, fit_amp=False, cf=None, extended=False) :
  '''
  Update df_a2z with fitted parameter.
  '''

  if extended :
    df_a2z = df_a2z.copy ()

  centiles = np.copy (input_centiles)
  centiles = centiles [:, :centiles[1,:].size-1]
  aux = df_a2z.loc[df_a2z[6]==0]
  cond_exp = (aux[2]=='height')|(aux[2]=='width')
  a_cond_exp = cond_exp.to_numpy ()
  #retransform width and height (the explored distribution is the distribution of the logarithm)
  for ii in range (centiles.shape[0]) :
    centiles[ii,a_cond_exp] = np.exp (centiles[ii,a_cond_exp])

  if fit_amp :

    # Update df_a2z a first time so the code get the good medians of the gamma values
    df_a2z.loc[df_a2z[6]==0, 4] = centiles [1,:]

    orders = aux[0].to_numpy ()
    degrees = aux[1].to_numpy ()
    param_type = aux[2].to_numpy ()
    for ii, (p_type, o, d) in enumerate (zip (param_type, orders, degrees)) :
      if p_type=='height' :
         if np.any ( (df_a2z[0]==o) & (df_a2z[1]==d) & (df_a2z[2]=='width') ) :
           gamma = df_a2z.loc[(df_a2z[0]==o) & (df_a2z[1]==d) & (df_a2z[2]=='width'), 4].to_numpy () [0]
         elif np.any ( (df_a2z[0]==o) & (df_a2z[1]=='a') & (df_a2z[2]=='width') ) :
           gamma = df_a2z.loc[(df_a2z[0]==o) & (df_a2z[1]=='a') & (df_a2z[2]=='width'), 4].to_numpy () [0]
         elif np.any ( (df_a2z[0]=='a') & (df_a2z[1]=='a') & (df_a2z[2]=='width') ) :
           gamma = df_a2z.loc[(df[0]=='a') & (df_a2z[1]=='a') & (df_a2z[2]=='width'), 4].to_numpy () [0]
         centiles[:,ii] = amp_to_height (centiles[:, ii], gamma)

  # Update df_a2z with the parameters extracted from the sampled posterior probability
  sigma_1 = centiles[1,:] - centiles[0,:]
  sigma_2 = centiles[2,:] - centiles[1,:]
  if extended :
    cf.loc[df_a2z[6]==0, 4] = centiles [1,:]
    cf.loc[df_a2z[6]==0, 5] = sigma_1
    cf.loc[df_a2z[6]==0, 6] = sigma_2
    return cf
  else :
    df_a2z.loc[df_a2z[6]==0, 4] = centiles [1,:]
    sigma = np.maximum (sigma_1, sigma_2) 
    df_a2z.loc[df_a2z[6]==0, 5] = sigma
    return df_a2z

def get_list_order (df_a2z) :
  '''
  Get the list of orders to fit.
  '''

  list_order = df_a2z.loc[(df_a2z[0]!='a')&((df_a2z[1]=='0')|(df_a2z[1]=='1')), 0].to_numpy ()
  list_order = list_order.astype (np.int_)
  order = np.unique (list_order)

  return order

def peakbagging (a2z_file, freq, psd, back=None, wdw=None, dnu=None, spectro=True,
                 nsteps_mcmc=1000, show_corner=False,
                 store_chains=False, mcmcDir='.', order_to_fit=None, parallelise=False, progress=False,
                 strategy='order', fit_02=True, fit_13=True, nwalkers=64, normalise=False, instr='geometric', show_summary=False,
                 filename_summary=None, show_prior=False, coeff_discard=50, use_sinc=False, asym_profile='nigam-kosovichev',
                 restrict=False, remove_asymmetry_outside_window=True, do_not_use_dnu=False, save_only_after_sampling=False,
                 size_window=None, fit_amp=False, extended=False, projected_splittings=False, bins=100, existing_chains='read',
                 fit_splittings=True, fit_angle=True) :
  '''
  Read an a2z input file with a prior guess of the modes to fit and return the result 
  of the peakbagging protocol processed over those modes. 
  Fitting strategy is the following: pair 1-3 and 2-0 of same order are successively fitted from low frequencies
  to high frequencies following a pseudo-global strategy. This protocol is repeted n_process times. 

  :param a2z_file: name of the file to read the parameters.
  :type a2z_file: string

  :param freq: frequency vector
  :type freq: ndarray

  :param psd: real power vector
  :type psd: ndarray

  :param back: activity background vector that will be used to complete the model to fit. Optional default ``None``.
    Must have the same length than freq and psd. 
  :type back: ndarray.

  :param wdw: observation window (0 and 1 array of the same lenght as the original timeseries)
    to analyse in order to predict the sidelob pattern. Optional, default ``None``. 
  :type wdw: ndarray.

  :param dnu: large separation of the modes. In this function, it will only be used to adapt the fitting window for 
    fitted modes above 1200 muHz. If not given and if at least two l=0 modes are specified in the a2z file, dnu will be automatically computed. 
  :type dnu: float.

  :param nsteps_mcmc: number of steps to process into each MCMC exploration.
  :type nsteps_mcmc: int

  :param show_corner: if set to ``True``, show and save the corner plot for the posterior distribution sampling.
  :type show_corner: bool

  :param store_chains: if set to ``True``, each MCMC sampler will be stored as an hdf5 files. Filename will be autogenerated
    with modes parameters. Optional, default ``False``
  :type store_chains: bool

  :param mcmcDir: directory where to save the MCMC sampler. Optional, default ``.``.
  :type mcmcDir: string
 
  :param order_to_fit: list of order to fit if the input a2z file contains order that are supposed not to be fitted.
    Optional, default ``None``.
  :type order_to_fit: array-like

  :param parallelise: If set to ``True``, use Python multiprocessing tool to parallelise process.
    Optional, default ``False``.
  :type parallelise: bool

  :param strategy: strategy to use for the fit, ``order``, ``pair``, ``global``. Optional, default ``order``. If 'pair' is used, a2z input must contain
    individual heights, widths and splittings for each degree. The ``global`` behaviour is experimental. 
  :type strategy: str

  :param fit_02: if strategy is set to ``pair``, l=0 and 2 modes will only be fitted if this parameter is set to ``True``.
    Optional, default ``True``.
  :type fit_02: bool

  :param fit_13: if strategy is set to ``pair``, l=1 and 3 modes will only be fitted if this parameter is set to ``True``.
    Optional, default ``True``.
  :type fit_13: bool

  :param nwalkers: number of wlakers in the MMCM process.
  :type nwalkers: int

  :param instr: instrument to consider (amplitude ratio inside degrees depend on geometry 
    AND instrument and should be adaptated). Possible argument : ``geometric``, ``kepler``, ``golf``, ``virgo``.
    Optional, default ``geometric``. 
  :type instr: str

  :param show_summary: show summary plot at the end of the fit. Optional, default ``False``.
  :type show_summary: bool

  :param coeff_discard: coeff used to compute the number of values to discard at the beginning
    of each MCMC : total amount of sampled values will be divided by coeff_discard. Optional, default 50.
  :type coeff_discard: int

  :param use_sinc: if set to ``True``, mode profiles will be computed using cardinal sinus and not Lorentzians.
    No asymmetry term will be used if it is the case. Optional, default ``False``.
  :type use_sinc: bool

  :param asym_profile: depending on the chosen argument, asymmetric profiles will be computed following Korzennik 2005 (``korzennik``)
    or Nigam & Kosovichev 1998 (``nigam-kosovichev``). Default ``nigam-kosovichev``. 
  :type asym_profile: str

  :param restrict: if set to True, will only use the modes with unfrozen parameters in the model.
  :type restrict: bool

  :param remove_asymmetry_outside_window: if set to True, asymmetry of modes outside of the fitting window will be set to 0. 
    Optional, default ``True``. 
  :type remove_asymmetry_outside_window: bool 

  :param do_not_use_dnu: if set to ``True``, fitting window will be computed without using dnu value.
  :type do_not_use_dnu: bool

  :param save_only_after_sampling: if set to True, hdf5 file with chains information will only be saved at the end of the sampling
    process. If set to False, the file will be saved step by step (see ``emcee`` documentation).
  :type saveon_only_after_sampling: bool

  :param size_window: size of the fitting window, in muHz. If not given, the size of the fitting window will be automatically set,
    using dnu or the input frequencies of the parameter to fit. Optional, default ``None``.
  :type size_window: float

  :param fit_amp: if set to ``True``, amplitude of the modes will be fitted instead of heights (input heights will be transformed inside
    the code and retransformed as outputs).
  :type fit_amp: bool

  :param extended: if set to ``True``, the returned pkb array will be extended to contain asymmetric uncertainties over each parameter.
  :type extended: bool

  :param projected_splittings: if set to ``True``, the function will consider that the ``split`` parameters of the input are projected 
    splittings and will build the model consequently. Optional, default ``False``. 
  :type projected_splittings: bool

  :param bins: number of bins for each cornerplot panel. Optional, default 100.
  :type bins: int

  :param existing_chains: controls the behaviour of the function concerning existing hdf5 files. If, ``read``, existing files will be read
    without sampling and function output will be updated consequently, if ``reset``, the backend will be cleared and the chain will 
    be sampled from scratch, if ``sample`` the function will sample the chain from where the previous exploration was stopped,
    if ``ignore``, the chain is not read. Optional, default ``read``.
  :type existing_chains: str

  :param fit_splittings: if the selected strategy is ``global``, the global ``split`` parameter will be fitted only
    if this parameter is set to ``True``. Optional, default ``True``. 
  :type fit_splittings: bool

  :param fit_angle: if the selected strategy is ``global``, the global ``angle`` parameter will be fitted only 
    if this parameter is set to ``True``. Optional, default ``True``. 
  :type fit_angle: bool

  :return: a2z fitted modes parameters as a DataFrame, and corresponding pkb array (extended pkb array if extended is set to ``True``)
  :rtype: tuple of objects
  '''

  if existing_chains not in ['read', 'reset', 'sample', 'ignore'] :
    raise Exception ("Unknown value for existing_chains, must be 'read', 'reset', 'sample' or 'ignore'")

  if (asym_profile!='korzennik')&(asym_profile!='nigam-kosovichev') :
    raise Exception ('Unknown asym_profile.')

  df_a2z = read_a2z (a2z_file)
  check_a2z (df_a2z)
  if dnu is None :
    dnu = dnu_from_df (df_a2z)
  if dnu is None :
    do_not_use_dnu = True

  # by default fix all parameters
  df_a2z.loc[:,6] = 1

  if extended :
    cf = a2z_to_cf (df_a2z)

  if strategy=='global' :
    print ('Global fitting')
    df_a2z.loc[df_a2z[2]!='amp_l', 6] = 0
    if not fit_splittings :
      df_a2z.loc[(df_a2z[2]=='split')&(df_a2z[0]=='a'), 6] = 1
    if not fit_angle :
      df_a2z.loc[(df_a2z[2]=='angle')&(df_a2z[0]=='a'), 6] = 1

    up_bound, low_bound = define_window (df_a2z, strategy, dnu=dnu, 
                                         do_not_use_dnu=do_not_use_dnu,
                                         size_window=size_window)
    df_a2z = check_leak (df_a2z, low_bound, up_bound)
    df_in = preprocess_df (df_a2z, restrict, remove_asymmetry_outside_window)

    if store_chains :
      #designing the filename of the hdf5 file that will be used to store the mcmc chain. 
      filename = 'mcmc_sampler_global.h5'
      filename = path.join (mcmcDir, filename)
      print ('Chain will be saved at:', filename)
    else :
      filename = None

    # show prior
    if show_prior :
      param_prior = a2z_to_pkb (df_in)
      plot_from_param (param_prior, freq[(freq>low_bound)&(freq<up_bound)], psd[(freq>low_bound)&(freq<up_bound)], 
                       back=back[(freq>low_bound)&(freq<up_bound)], wdw=wdw, smoothing=10, spectro=spectro, correct_width=1.,
                       show=show_prior, instr=instr, asym_profile=asym_profile, projected_splittings=projected_splittings)

    centiles = wrap_explore_distribution (df_in, freq, psd, back, 
                               low_bound_freq=low_bound, up_bound_freq=up_bound, wdw=wdw, nsteps=nsteps_mcmc,
                               show_corner=show_corner, filename=filename, parallelise=parallelise,
                               progress=progress, nwalkers=nwalkers, normalise=normalise, instr=instr,
                               coeff_discard=coeff_discard, use_sinc=use_sinc, asym_profile=asym_profile,
                               save_only_after_sampling=save_only_after_sampling, fit_amp=fit_amp,
                               projected_splittings=projected_splittings, bins=bins, existing_chains=existing_chains)
    if centiles is not None :
      df_a2z = update_with_centiles (df_a2z, centiles, fit_amp=fit_amp)
      if extended :
        cf = update_with_centiles (df_a2z, centiles, fit_amp=fit_amp, cf=cf, extended=True)
      print ('Ensemble sampling achieved')
    # --------------------------------------------------------------------------------------------
  
    df_a2z.loc[:,6] = 1

  else :

    #extract a list of order
    order = get_list_order (df_a2z)

    if order_to_fit is None :
      order_to_fit = order

    print ('Orders to fit')
    print (np.intersect1d (order, order_to_fit))

    for n in np.intersect1d (order, order_to_fit) :
      if strategy=='order' :
        print ('Fitting on order', n)
        df_a2z.loc[(df_a2z[0]==str(n))&(df_a2z[1]=='0'), 6] = 0
        df_a2z.loc[(df_a2z[0]==str(n))&(df_a2z[1]=='1'), 6] = 0
        df_a2z.loc[(df_a2z[0]==str(n-1))&(df_a2z[1]=='2'), 6] = 0
        df_a2z.loc[(df_a2z[0]==str(n-1))&(df_a2z[1]=='3'), 6] = 0
        df_a2z.loc[(df_a2z[0]==str(n-1))&(df_a2z[1]=='4'), 6] = 0
        df_a2z.loc[(df_a2z[0]==str(n))&(df_a2z[1]=='a'), 6] = 0

        up_bound, low_bound = define_window (df_a2z, strategy, dnu=dnu, 
                                             do_not_use_dnu=do_not_use_dnu,
                                             size_window=size_window)
        df_a2z = check_leak (df_a2z, low_bound, up_bound)

        df_in = preprocess_df (df_a2z, restrict, remove_asymmetry_outside_window)

        if store_chains :
          #designing the filename of the hdf5 file that will be used to store the mcmc chain. 
          filename = 'mcmc_sampler_order_' + str(n).rjust (2, '0') + '.h5'
          filename = path.join (mcmcDir, filename)
          print ('Chain will be saved at:', filename)
        else :
          filename = None

        # show prior
        if show_prior :
          param_prior = a2z_to_pkb (df_in)
          plot_from_param (param_prior, freq[(freq>low_bound)&(freq<up_bound)], psd[(freq>low_bound)&(freq<up_bound)], 
                           back=back[(freq>low_bound)&(freq<up_bound)], wdw=wdw, smoothing=10, spectro=spectro, correct_width=1.,
                           show=show_prior, instr=instr, asym_profile=asym_profile, projected_splittings=projected_splittings)

        centiles = wrap_explore_distribution (df_in, freq, psd, back, 
                                   low_bound_freq=low_bound, up_bound_freq=up_bound, wdw=wdw, nsteps=nsteps_mcmc,
                                   show_corner=show_corner, filename=filename, parallelise=parallelise,
                                   progress=progress, nwalkers=nwalkers, normalise=normalise, instr=instr,
                                   coeff_discard=coeff_discard, use_sinc=use_sinc, asym_profile=asym_profile,
                                   save_only_after_sampling=save_only_after_sampling, fit_amp=fit_amp,
                                   projected_splittings=projected_splittings, bins=bins, existing_chains=existing_chains)
        if centiles is not None :
          df_a2z = update_with_centiles (df_a2z, centiles, fit_amp=fit_amp)
          if extended :
            cf = update_with_centiles (df_a2z, centiles, fit_amp=fit_amp, cf=cf, extended=True)
          print ('Ensemble sampling achieved')
        # --------------------------------------------------------------------------------------------
    
        df_a2z.loc[:,6] = 1

      if strategy=='pair' : 
        print ('Fitting on order', n)

        if fit_02 :

          print ('Fitting degrees 0 and 2')

          df_a2z.loc[(df_a2z[0]==str(n))&(df_a2z[1]=='0'), 6] = 0
          df_a2z.loc[(df_a2z[0]==str(n-1))&(df_a2z[1]=='2'), 6] = 0

          up_bound, low_bound = define_window (df_a2z, strategy, dnu=dnu, do_not_use_dnu=do_not_use_dnu, size_window=size_window)
          df_a2z = check_leak (df_a2z, low_bound, up_bound)

          df_in = preprocess_df (df_a2z, restrict, remove_asymmetry_outside_window)

          if store_chains :
            #designing the filename of the hdf5 file that will be used to store the mcmc chain. 
            filename = 'mcmc_sampler_order_' + str(n).rjust (2, '0') + '_degrees_02.h5'
            filename = path.join (mcmcDir, filename)
            print ('Chain will be saved at:', filename)
          else :
            filename = None

          # show prior
          if show_prior :
            param_prior = a2z_to_pkb (restrict_input (df_a2z))
            plot_from_param (param_prior, freq[(freq>low_bound)&(freq<up_bound)], psd[(freq>low_bound)&(freq<up_bound)], 
                             back=back[(freq>low_bound)&(freq<up_bound)], wdw=wdw, smoothing=10, spectro=spectro, correct_width=1.,
                             show=show_prior, instr=instr, asym_profile=asym_profile, projected_splittings=projected_splittings)

          centiles = wrap_explore_distribution (df_in, freq, psd, back, 
                                     low_bound_freq=low_bound, up_bound_freq=up_bound, wdw=wdw, nsteps=nsteps_mcmc,
                                     show_corner=show_corner, filename=filename, parallelise=parallelise,
                                     progress=progress, nwalkers=nwalkers, normalise=normalise, instr=instr, 
                                     coeff_discard=coeff_discard, use_sinc=use_sinc, asym_profile=asym_profile,
                                     save_only_after_sampling=save_only_after_sampling, fit_amp=fit_amp,
                                     projected_splittings=projected_splittings, bins=bins, existing_chains=existing_chains)
          if centiles is not None :
            df_a2z = update_with_centiles (df_a2z, centiles, fit_amp=fit_amp)
            if extended :
              cf = update_with_centiles (df_a2z, centiles, fit_amp=fit_amp, cf=cf, extended=True)
            print ('Ensemble sampling achieved')
          # --------------------------------------------------------------------------------------------

          # Fixing again all parameters
          df_a2z.loc[:,6] = 1

        if fit_13 :

          print ('Fitting degrees 1 and 3')
          df_a2z.loc[(df_a2z[0]==str(n))&(df_a2z[1]=='1'), 6] = 0
          df_a2z.loc[(df_a2z[0]==str(n-1))&(df_a2z[1]=='3'), 6] = 0

          up_bound, low_bound = define_window (df_a2z, strategy, dnu=dnu, do_not_use_dnu=do_not_use_dnu, size_window=size_window)
          df_a2z = check_leak (df_a2z, low_bound, up_bound)

          df_in = preprocess_df (df_a2z, restrict, remove_asymmetry_outside_window)

          if store_chains :
            #designing the filename of the hdf5 file that will be used to store the mcmc chain. 
            filename = 'mcmc_sampler_order_' + str(n).rjust (2, '0') + '_degrees_13.h5'
            filename = path.join (mcmcDir, filename)
            print ('Chain will be saved at:', filename)
          else :
            filename = None

          # show prior
          if show_prior :
            param_prior = a2z_to_pkb (restrict_input (df_a2z))
            plot_from_param (param_prior, freq[(freq>low_bound)&(freq<up_bound)], psd[(freq>low_bound)&(freq<up_bound)], 
                             back=back[(freq>low_bound)&(freq<up_bound)], wdw=wdw, smoothing=10, spectro=spectro, correct_width=1.,
                             show=show_prior, instr=instr, asym_profile=asym_profile, projected_splittings=projected_splittings)

          centiles = wrap_explore_distribution (df_in, freq, psd, back, 
                                     low_bound_freq=low_bound, up_bound_freq=up_bound, wdw=wdw, nsteps=nsteps_mcmc,
                                     show_corner=show_corner, filename=filename, parallelise=parallelise,
                                     progress=progress, nwalkers=nwalkers, normalise=normalise, instr=instr,
                                     coeff_discard=coeff_discard, use_sinc=use_sinc, asym_profile=asym_profile,
                                     save_only_after_sampling=save_only_after_sampling, fit_amp=fit_amp,
                                     projected_splittings=projected_splittings, bins=bins, existing_chains=existing_chains)
          if centiles is not None :
            df_a2z = update_with_centiles (df_a2z, centiles, fit_amp=fit_amp)
            if extended :
              cf = update_with_centiles (df_a2z, centiles, fit_amp=fit_amp, cf=cf, extended=True)
            print ('Ensemble sampling achieved')
          # --------------------------------------------------------------------------------------------
    
          df_a2z.loc[:,6] = 1

  df_a2z.loc[:,6] = 0

  # generate pkb array to return
  if extended :
    pkb = cf_to_pkb_extended (cf)
  else :
    pkb = a2z_to_pkb (df_a2z)

  pkb = sort_pkb (pkb)

  # show result
  plot_from_param (pkb, freq, psd, back=back, wdw=wdw, smoothing=10, spectro=spectro, correct_width=1.,
                   show=show_summary, filename=filename_summary, instr=instr, asym_profile=asym_profile,
                   projected_splittings=projected_splittings)

  return df_a2z, pkb







