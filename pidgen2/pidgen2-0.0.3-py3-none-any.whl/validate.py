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

import sys
import pprint

from jax import numpy as np
import numpy as onp
import matplotlib
import matplotlib.pyplot as plt
import uproot3 as uproot
import functools
from scipy.ndimage import gaussian_filter

import argparse

from .plotting import plot_distr1d_comparison, set_lhcb_style, plot_hist2d, plot
from .tuples import read_array_filtered, write_array, read_array
from .resampling import get_samples, get_variables

def main() : 

  parser = argparse.ArgumentParser(description = "PIDGen validation script", 
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

  parser.add_argument('--input', type=str, default = None, 
                      help="Input ROOT file")
  parser.add_argument('--intree', type=str, default = None, 
                      help="Input TTree")
  parser.add_argument('--sample', type=str, default = None, 
                      help="Calibration sample name")
  parser.add_argument('--dataset', type=str, default = None, 
                      help="Calibration dataset in the form Polarity_Year, e.g. MagUp_2018")
  parser.add_argument('--variable', type=str, default = None, 
                      help="PID variable to resample")
  parser.add_argument('--weight', type=str, default = None, 
                      help="Weigth branch name")
  parser.add_argument('--branches', type=str, default = "pt:eta:ntr", 
                      help="Input branches for Pt,Eta,Ntracks variables in the form Pt:Eta:Ntrack")
  parser.add_argument('--pidgen', type=str, default = "pidgen", 
                      help="Resampled PID branch")
  parser.add_argument('--piddata', type=str, default = "pid", 
                      help="Original PID branch")
  parser.add_argument('--output', type=str, default = None, 
                      help="Output prefix")
  parser.add_argument('--verbose', default = False, action = "store_const", const = True, 
                      help='Enable debug messages')
  parser.add_argument('--interactive', default = False, action = "store_const", const = True, 
                      help='Open interactive plot window (if False, only store the pdf file). ')

  args = parser.parse_args()

  if len(sys.argv)<2 : 
    parser.print_help()
    raise SystemExit

  input_tuple = args.input
  input_tree = args.intree
  input_branches = args.branches.split(":") + [args.pidgen, args.piddata, args.weight]

  output_tuple = args.output

  sample_name = args.sample
  dataset_name = args.dataset
  variable_name = args.variable

  pp = pprint.PrettyPrinter(indent = 4)

  config = get_samples()[sample_name][dataset_name]
  variable = get_variables()[variable_name]

  if (args.verbose) : 
    print(f"Calibration sample config: {pp.pformat(config)}")
    print(f"Variable definition: {pp.pformat(variable)}")

  f = uproot.open(input_tuple)
  t = f[input_tree]
  branches = t.keys()
  if (args.verbose) : print (f"List of all input tree branches: {pp.pformat(branches)}")
  input_data = read_array_filtered(t, input_branches, selection = "pidstat>1", sel_branches = ["pidstat"])
  if (args.verbose) : print (f"Input data array shape: {input_data.shape}")

  transform_forward = lambda x: 1.-(1.-x)**0.2

  pidgen_tr = transform_forward(input_data[:,-3])
  piddata_tr = transform_forward(input_data[:,-2])
  sw = input_data[:,-1]

  if (args.verbose) : print(f"Array of sWeights: {sw}")

  label = variable_name

  set_lhcb_style(size = 12)

  with plot("", args.output) as (fig, ax) : 
    plot_distr1d_comparison(piddata_tr, pidgen_tr, bins = 100, range = variable["data_range"], ax = ax, 
       label = "Transformed PID", 
       weights = sw, data_weights = sw, 
       title = "Transformed PID", log = False, pull = True, 
       legend = ["Original distribution", "Resampled distribution"], 
       data_alpha = 0.5)

  if (args.interactive) : plt.show()

if __name__ == "__main__" : 
  main()
