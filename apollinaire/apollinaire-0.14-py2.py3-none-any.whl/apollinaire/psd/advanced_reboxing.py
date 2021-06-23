#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Advanced PSD reboxing methods developed by V. Delsanti, R.A. García
and S.N. Breton. 
'''

import numpy as np
import matplotlib.pyplot as plt
import astropy

def show_compressed_vector (freq, psd, sampleed_freq, stat_array, err_array, spectro=False,
                            numax=None, start=None, end=None) :
  '''
  Plot the compressed vector against the original vector.
  '''
  figure, ax = plt.subplots (1, 1, figsize=(12,6))
  ax.set_xscale ('log')
  ax.set_yscale ('log')
  ax.set_xlabel (r'Frequency ($\mu$Hz)')
  if spectro :
    ax.set_ylabel (r'PSD ((m/s)$^2$/$\mu$Hz)')
  else :
    ax.set_ylabel (r'PSD (ppm$^2$/$\mu$Hz)')
  ax.plot (freq, psd, '-k', alpha=0.5, linewidth=0.4)
  ax.plot (sampled_freq, stat_array+err_array, '-r', linewidth=0.6)
  ax.plot (sampled_freq, stat_array-err_array, '-b', linewidth=0.6)
  ax.plot (sampled_freq, stat_array,'-k', linewidth=1, label=method)
  ax.axvline (freq[k0], linewidth = 0.5, color='red', linestyle ='dashed')
  if numax is not None :
      ax.axvline (start, linewidth=0.5, color='green', linestyle='dashed')
      ax.axvline (end, linewidth=0.5, color='green', linestyle='dashed')
  plt.show()


def advanced_reboxing_no_numax (freq, psd, method='median', number_points=2000, show=False):
  '''
  Compress a PSD vector without taking into account the numax region. 

  :return: the resampled frequency array and the resampled PSD vector.
  :rtype: tuple of array.
  '''
  sampled_freq = np.array([])
  stat_array = np.array([])
  err_array = np.array([])
  k=0
  while freq[k+1]/freq[k] > 10**(1/number_points):
      sampled_freq = np.append(sampled_freq,freq[k])
      stat_array = np.append(stat_array, psd[k])
      k+=1
  k0 = k
  size = (freq[-1]/freq[k])**(1/number_points)
  box_begin = freq[k]
  while box_begin<freq[-1]:
      box = np.array([freq[k]])
      psd_box = np.array([psd[k]])
      while freq[k]< box_begin*size and freq[k]<freq[-1]:
          box = np.append(box,freq[k])
          psd_box = np.append(psd_box,psd[k])
          k+=1
      box_begin = freq[k]
      if psd_box.size > 0:
          f, stat, err = box_analysis (box, psd_box, method=method)
          stat_array = np.append (stat_array,stat)
          sampled_freq = np.append (sampled_freq, f)
          if show:
              err_array = np.append (err_array,err)
  f, stat, err = box_analysis (box, psd_box, method=method)
  stat_array = np.append (stat_array,stat)
  sampled_freq = np.append (sampled_freq, f)
  if show:
      err_array = np.append(err_array,err)

  if show :
    show_compressed_vector (freq, psd, sampled_freq, stat_array, err_array, spectro=spectro,
                            numax=None, start=None, end=None)

  return sampled_freq, stat_array


def advanced_reboxing_with_numax (freq, psd, method='median', number_points=2000, numax=None, points_numax=500,
                                  verbose=0, show=False, spectro=False):
  '''
  Compress a PSD vector by taking into account the numax region. 

  :return: the resampled frequency array and the resampled PSD vector.
  :rtype: tuple of array.
  '''
  sampled_freq = np.array([])
  stat_array = np.array([])
  err_array = np.array([])
  k=0
  while freq[k+1]/freq[k] > 10**(1/number_points):
      sampled_freq = np.append(sampled_freq, freq[k])
      stat_array = np.append(stat_array, psd[k])
      k+=1
  k0 = k
  division = np.array(freq[k0])
  if numax is not None :
      start = numax/1.5
      end = numax*1.5
      if end < freq[k0]:
          if verbose==1 :
            print('numax zone already fully conserved, no need to use the numax option')
          else :
            pass
      else:
          if start > freq[k0]:
              division = np.append(division, start)
          if end < freq[-1]:
              division = np.append(division,end)
          points_numax = end/(start*2.25) * points_numax

  division = np.append(division, freq[-1])
  point_numbers_list = np.array([number_points])
  if division.size > 1:
      S = np.log10(division[-1]*division[1]/(division[0]*division[-2]))
      point_numbers_list = np.array ([number_points*np.log10(division[1]/division[0])/S])
      point_numbers_list = np.append (point_numbers_list, points_numax)
      point_numbers_list = np.append (point_numbers_list, number_points*np.log10(division[-1]/division[-2])/S)

  for i in range(1, division.size):
      zone_begin = division[i-1]
      zone_end = division[i]
      number = point_numbers_list[i-1]
      size = (zone_end/zone_begin)**(1/number)
      box_begin = zone_begin
      while box_begin<zone_end:
          box = np.array([freq[k]])
          psd_box = np.array([psd[k]])
          while freq[k]< box_begin*size and freq[k]<zone_end:
              box = np.append(box,freq[k])
              psd_box = np.append(psd_box,psd[k])
              k+=1
          box_begin = freq[k]
          if psd_box.size > 1:
              f, stat, err = box_analysis (box, psd_box, method=method)
              stat_array = np.append (stat_array,stat)
              sampled_freq = np.append (sampled_freq, f)
              if show:
                  err_array = np.append (err_array, err)
      f, stat, err = box_analysis (box, psd_box, method=method)
      stat_array = np.append (stat_array, stat)
      sampled_freq = np.append (sampled_freq, f)
      if show:
          err_array = np.append (err_array,err)

  if show :
    show_compressed_vector (freq, psd, sampled_freq, stat_array, err_array, spectro=spectro,
                            numax=numax, start=start, end=end)

  return sampled_freq, stat_array

def wrapper_advanced_reboxing (freq, psd, method='median', number_points=2000, numax=None, points_numax=500,                            
                               verbose=0, show=False, spectro=False) :
  '''
  Wrap advanced_reboxing_no_numax and advanced_reboxing_with_numax.

  :return: the resampled frequency array and the resampled PSD vector.
  :rtype: tuple of array.
  '''

  if numax is None :
    sampled_freq, stat_array = advanced_reboxing_no_numax (freq, psd, method=method, number_points=number_points)

  else :
    sampled_freq, stat_array = advanced_reboxing_with_numax (freq, psd, method=method, number_points=number_points, 
                                                             numax=numax, points_numax=points_numax,
                                                             verbose=verbose, show=show, spectro=spectro)

  return sampled_freq, stat_array


def box_analysis (box, psd_box, method):
  '''
  Process statistical analysis of a given box.
  '''
  f = 10**np.mean (np.log10(box))   #set the point to the geometric mean of the freqs taken in the box
  if method=='mean' :
      stat = np.mean (psd_box)       
  if method=='median' :
      stat = np.median (psd_box)
  if method=='mean' :
    err = np.std (psd_box)
  if method=='median':
    err = astropy.stats.mad_std (psd_box)

  return f, stat, err

