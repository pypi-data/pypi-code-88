##############################################################################
# (c) Copyright 2021 CERN for the benefit of the LHCb Collaboration           #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "COPYING".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################

"""
Functions for PID resampling of calibration data. 
"""
import importlib

from jax import numpy as np
import numpy as onp
import matplotlib
import matplotlib.pyplot as plt
import uproot
from scipy.ndimage import gaussian_filter

from .plotting import plot, plot_distr2d, plot_distr1d, set_lhcb_style, plot_hist2d
from .tuples import read_array_filtered, write_array, read_array
from . import density_estimation as de

def get_samples() :
  """
  Import all modules with calibration samples from the "samples" subdir
  and construct the dictionary of all calibration samples

  Returns: 
      Dictionary of all samples loaded from "samples/" subdirectory
  """
  from . import samples
  d = {}
  for i in samples.__all__ : 
    module = importlib.import_module("." + i, "pidgen2.samples")
    s = getattr(module, "sample")
    d[i] = s
  return d

def get_variables() : 
  """
  Import all modules with variables description from the "variables" subdir
  and construct the dictionary of all variables. 

  Returns: 
      Dictionary of all variables loaded from "variables/" subdirectory
  """
  from . import variables
  d = {}
  for i in variables.__all__ : 
    module = importlib.import_module("." + i, "pidgen2.variables")
    c = getattr(module, "variable")
    d[i] = c
  return d

def read_calib_tuple(sample, trees, branches, verbose = False) : 
  """ 
  Read calibration sample from the list of files into numpy array. 

  Args: 
    sample: tuple in the form (formatstring, numfiles) describing the calibration sample.
    trees: list of ROOT trees to read from the calibration files 
    branches: list of branches to read. 

  Returns: 
    2D numpy array, result of concatenation of all calibration samples. 
    The 1st index of 2D array corresponds to event, 2nd index to the variable from the branches list. 
  """
  datasets = []
  for i in range(sample[1]) : 
    filename = sample[0] % i
    print(f"Reading file ({i+1}/{sample[1]}) {filename}")
    for tree in trees : 
      try : 
        with uproot.open(filename + ":" + tree) as t :
          arr = t.arrays(branches, library = "pd")[branches].to_numpy()
          if verbose : print(f"Reading tree {tree}, {arr.shape[0]} events")
          datasets += [ arr ]
      except FileNotFoundError : 
        print(f"... file not found, skipping")
        break
  if len(datasets) == 0 : 
    print(f"No input calibration files found. Do you have a valid Kerberos ticket to access EOS?")
    print(f"Will not create PID template, exiting...\n\n")
    raise SystemExit
  return np.concatenate(datasets, axis = 0)

def calib_transform(x, config, variable) :
  """
  Apply variable transformation to the calibration array. 

  Args: 
    x: 2D numpy array in the format returned by read_calib_tuple function. 
    config: calibration sample configuration dictionary. 
    variable: variable definition dictionary. 
  """
  transform_forward = variable["transform_forward"]
  transform_sample = config["transform"]
  arr = [ 
    transform_forward(x[:,0]),    # PID variable
    transform_sample[0](x[:,1]),  # pT
    transform_sample[1](x[:,2]),  # eta
    transform_sample[2](x[:,3] + onp.random.uniform(size = x.shape[0]) - 0.5 ),   # Ntracks (add uniform random +-0.5)
    x[:,4]  # sWeight
  ]
  return np.stack(arr, axis = 1)

def data_transform(x, config) :
  """
  Apply variable transformation to the data array. 

  Args: 
    x: 2D numpy array in the format returned by read_array function. 
    config: calibration sample configuration dictionary. 
  """
  transform_sample = config["transform"]
  arr = [ 
    transform_sample[0](x[:,0]),  # pT
    transform_sample[1](x[:,1]),  # eta
    transform_sample[2](x[:,2])   # Ntracks
  ]
  return np.stack(arr, axis = 1)

def create_template(variable, config, kernels = None, use_calib_cache = True, control_plots = False, 
                    interactive_plots = False, prefix = "", max_files = 0, verbose = False) : 
  """
  Create PID calibration template from the calibration sample (smoothed PDF). 
  
  Args: 
    variable: variable definition dictionary.
    config: calibration sample configuration dictionary.
    kernels: optional list of kernel widths (if None, taken from config and variable definition dicts). 
    use_calib_cache: if True, take calibration sample from the local cache. 
    control_plots: if True, produce control plots (1D and 2D projections of calibration and smoothed distributions). 
    interactive_plots: if True, open control plots in interactive mode, if False, only store them to files. 
    prefix: prefix for control plots (e.g. --prefix="subdir/"). 
    max_files: Maximum number of calibration files to load (0 for unlimited)
    
  Returns: 
    template structure to be used for resampling. 
  """
  sample = config['sample']
  trees = config['trees']
  calib_branches = [variable["branch"]] + config["branches"]
  ranges = [ variable["data_range"]] + config["data_ranges"]
  calib_cache_filename = config["calib_cache_filename"]
  calib_cache_branches = ["pid"] + config["calib_cache_branches"]
  normalise_bins = [variable["normalise_bins"]] + config["normalise_bins"]
  normalise_methods = [variable["normalise_method"]] + config["normalise_methods"]
  normalise_ranges = [variable["normalise_range"]] + config["normalise_ranges"]
  template_bins = [variable["template_bins"]] + config["template_bins"]
  if kernels : 
    template_sigma = kernels
  else : 
    template_sigma = [variable["template_sigma"]] + config["template_sigma"]
  max_weights = config["max_weights"]

  if use_calib_cache : 
    with uproot.open(calib_cache_filename + ":tree") as t :
      raw_data = t.arrays(calib_cache_branches, library = "pd")[calib_cache_branches].to_numpy()
    if verbose : print(f"Read {raw_data.shape[0]} calibration events from local cache.")
  else :
    if max_files == 0 : 
      raw_data = read_calib_tuple(sample, trees, calib_branches, verbose = verbose)
    else : 
      raw_data = read_calib_tuple( (sample[0], min(sample[1], max_files)), trees, calib_branches, verbose = verbose)
    if verbose : print(f"Read {raw_data.shape[0]} calibration events from remote storage.")
    write_array(calib_cache_filename, raw_data, branches = calib_cache_branches)   # Store calibration data to local cache

  data = calib_transform(raw_data, config, variable)
  if (verbose) : print(f"Transformed data array: {data}")

  data = de.filter_data(data, ranges + [ (-1000., 1000.) ] )

  weights1 = data[:,-1]

  if max_weights : 
    histograms = de.create_histograms(data[:,1:-1], ranges = ranges[1:], bins = normalise_bins[1:], weights = weights1)
    weights2 = de.reweight(data[:,1:-1], histograms, max_weights = max_weights)
    weights = weights1*weights2
  else : 
    weights = weights1

  normaliser = de.create_normaliser(data[:,:-1], ranges = ranges, bins = normalise_bins, weights = weights )
  if (verbose) : print(f"Normalizer structure: {normaliser}")

  norm_data = de.normalise(data[:,:-1], normaliser, normalise_methods)
  if (verbose) : print(f"Normalized data array: {norm_data}")

  #unnorm_data = de.unnormalise(norm_data, normaliser, normalise_methods)

  counts, edges = onp.histogramdd(norm_data, bins = template_bins, range = normalise_ranges, weights = weights)
  smooth_counts = gaussian_filter(counts, template_sigma)

  set_lhcb_style(size = 12, usetex = False)
  #fig, axes = plt.subplots(nrows = 7, ncols = 6, figsize = (12, 9) )

  labels = config["labels"]
  names = config["names"]

  log = True

  if control_plots : 
    for i in range(len(ranges)) : 
      with plot(f"{names[i]}_transformed", prefix) as (fig, ax) : 
        plot_distr1d(data[:,i], bins = 50, range = ranges[i], ax = ax, label = "Transformed " + labels[i], weights = weights1, title = "Transformed distribution")

    for i in range(len(ranges)) : 
      with plot(f"{names[i]}_weighted", prefix) as (fig, ax) : 
        plot_distr1d(data[:,i], bins = 50, range = ranges[i], ax = ax, label = "Weighted " + labels[i], weights = weights, title = "Weighted distribution")

    for i in range(len(ranges)) : 
      with plot(f"{names[i]}_normalised", prefix) as (fig, ax) : 
        plot_distr1d(norm_data[:,i], bins = 50, range = normalise_ranges[i], ax = ax, label = "Normalised " + labels[i], weights = weights, title = "Normalised distribution")

    for i,j in [ (0,1), (0,2), (1,2), (0,3), (1,3), (2,3) ] : 
      with plot(f"{names[i]}_{names[j]}_data_proj", prefix) as (fig, ax) : 
        plot_distr2d(norm_data[:,i], norm_data[:,j], bins = 2*[50], ranges = (normalise_ranges[i], normalise_ranges[j]), 
             fig = fig, ax = ax, labels = ("Normalised " + labels[i], "Normalised " + labels[j]), weights = weights, cmap = "jet", log = log, 
             title = "Data projection")

    bins = template_bins

    smooth_proj = {
      (0, 1) : [np.sum(smooth_counts, (2,3)), edges[0], edges[1]],
      (0, 2) : [np.sum(smooth_counts, (1,3)), edges[0], edges[2]],
      (1, 2) : [np.sum(smooth_counts, (0,3)), edges[1], edges[2]],
      (0, 3) : [np.sum(smooth_counts, (1,2)), edges[0], edges[3]],
      (1, 3) : [np.sum(smooth_counts, (0,2)), edges[1], edges[3]],
      (2, 3) : [np.sum(smooth_counts, (0,1)), edges[2], edges[3]],
    }

    n1,n2,n3,n4 = [int(n/2) for n in bins]

    data_slices = {
      (0, 1) : [counts[:,:,n3,n4], edges[0], edges[1]], 
      (0, 2) : [counts[:,n2,:,n4], edges[0], edges[2]], 
      (1, 2) : [counts[n1,:,:,n4], edges[1], edges[2]], 
      (0, 3) : [counts[:,n2,n3,:], edges[0], edges[3]], 
      (1, 3) : [counts[n1,:,n3,:], edges[1], edges[3]], 
      (2, 3) : [counts[n1,n2,:,:], edges[2], edges[3]], 
    }

    smooth_slices = {
      (0, 1) : [smooth_counts[:,:,n3,n4], edges[0], edges[1]], 
      (0, 2) : [smooth_counts[:,n2,:,n4], edges[0], edges[2]], 
      (1, 2) : [smooth_counts[n1,:,:,n4], edges[1], edges[2]], 
      (0, 3) : [smooth_counts[:,n2,n3,:], edges[0], edges[3]], 
      (1, 3) : [smooth_counts[n1,:,n3,:], edges[1], edges[3]], 
      (2, 3) : [smooth_counts[n1,n2,:,:], edges[2], edges[3]], 
    }

    for i,j in smooth_proj.keys() : 
      with plot(f"{names[i]}_{names[j]}_smooth_proj", prefix) as (fig, ax) : 
        plot_hist2d(smooth_proj[(i,j)], fig = fig, ax = ax, labels = ("Normalised " + labels[i], "Normalised " + labels[j]), log = log, cmap = "jet", 
                  title = "Smoothed projection")
      with plot(f"{names[i]}_{names[j]}_data_slice", prefix) as (fig, ax) : 
        plot_hist2d(data_slices[(i,j)], fig = fig, ax = ax, labels = ("Normalised " + labels[i], "Normalised " + labels[j]), log = log, cmap = "jet", 
                  title = "Data slice")
      with plot(f"{names[i]}_{names[j]}_smooth_slice", prefix) as (fig, ax) : 
        plot_hist2d(smooth_slices[(i,j)], fig = fig, ax = ax, labels = ("Normalised " + labels[i], "Normalised " + labels[j]), log = log, cmap = "jet", 
                  title = "Smoothed slice")

    #plt.tight_layout(pad=1., w_pad=1., h_pad=0.5)
    if interactive_plots : plt.show()

  return smooth_counts, edges, normaliser

def resample_data(data, config, variable, template, chunk_size = 50000, verbose = False) : 
  """
  Perform resampling of data sample using the template created by create_template function.

  Args: 
    data: numpy 2D array with input data 
    config: calibration sample configuration dictionary.
    variable: variable definition dictionary.
    template: PID template structure.
    chunk_size: Size of data chunk for vectorised processing.

  Returns: 
    Tuple of (pid_arr, pid_stat), where
      pid_arr: numpy 1D array of resampled PID data. 
      pid_stat: numpy 1D array of effective template statistics per each event.
  """

  counts, edges, normaliser = template

  normalise_methods = [variable["normalise_method"]] + config["normalise_methods"]
  normalise_ranges = [variable["normalise_range"]] + config["normalise_ranges"]
  resample_bins = variable["resample_bins"]
  transform_backward = variable["transform_backward"]

  norm_data = de.normalise(data, normaliser[1:], normalise_methods[1:])

  if (verbose) : 
    print(f"Normalised data: {norm_data}")

  start_index = 0
  chunk = 0
  resampled_pid_arrs = []
  pid_calib_stats = []
  stop = False
  chunks = (len(norm_data)-1)//chunk_size+1

  while not stop : 
    print(f"Resampling chunk {chunk+1}/{chunks}, index={start_index}/{len(norm_data)}")
    end_index = start_index + chunk_size
    if end_index >= len(norm_data) :
      end_index = len(norm_data)
      stop = True

    rnd = onp.random.uniform(size = (end_index-start_index, ))
    norm_pid, stats = de.resample(counts, edges, norm_data[start_index:end_index,], 
                          rnd = rnd, range = normalise_ranges[0], 
                          bins = resample_bins)
    unnorm_pid = de.unnormalise(norm_pid, normaliser[0:1], normalise_methods)
    resampled_pid = transform_backward(unnorm_pid)

    resampled_pid_arrs += [ resampled_pid ]
    pid_calib_stats += [ stats ]

    start_index += chunk_size
    chunk += 1

  resampled_pid_arr = np.concatenate(resampled_pid_arrs, axis = 0)
  pid_calib_stat = np.concatenate(pid_calib_stats, axis = 0)
  return resampled_pid_arr, pid_calib_stat

  #output_data = np.concatenate([data[start_index:end_index,:], norm_data[start_index:end_index,:], unnorm_data[:nev,:], 
  #                              norm_pid, unnorm_pid, resampled_pid], axis = 1)
  #write_array("output.root", output_data, branches = 
  #            ["pid", "pt", "eta", "ntr", "sw", 
  #             "normpid", "normpt", "normeta", "normntr", 
  #             "unnormpid", "unnormpt", "unnormeta", "unnormntr", 
  #             "normpidgen", "pidgen", "respidgen"])
