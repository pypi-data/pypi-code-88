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
import argparse
import pprint

from jax import numpy as np
import uproot3 as uproot

from .tuples import write_array, read_array
from .resampling import read_calib_tuple, calib_transform, data_transform, create_template, resample_data
from .resampling import get_samples, get_variables

def main() : 

  parser = argparse.ArgumentParser(description = "PIDGen resampling script", 
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)

  parser.add_argument('--seed', type=int, default = 1, 
                      help="Initial random seed")
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
  parser.add_argument('--branches', type=str, default = "pt:eta:ntr", 
                      help="Input branches for Pt,Eta,Ntracks variables in the form Pt:Eta:Ntrack")
  parser.add_argument('--pidgen', type=str, default = "pidgen", 
                      help="Resampled PID branch")
  parser.add_argument('--stat', type=str, default = "pidstat", 
                      help="PID calibration statistics branch")
  parser.add_argument('--maxfiles', type=int, default = 0, 
                      help="Maximum number of calibration files to read (0-unlimited)")
  parser.add_argument('--output', type=str, default = None, 
                      help="Output ROOT file")
  parser.add_argument('--outtree', type=str, default = "tree", 
                      help="Output TTree")
  parser.add_argument('--start', type=int, default = 0, 
                      help="Start event")
  parser.add_argument('--stop', type=int, default = -1, 
                      help="Stop event")
  parser.add_argument('--usecache', default = False, action = "store_const", const = True, 
                      help='Use calibration cache')
  parser.add_argument('--plot', default = False, action = "store_const", const = True, 
                      help='Produce control plots')
  parser.add_argument('--interactive', default = False, action = "store_const", const = True, 
                      help='Show interactive control plots')
  parser.add_argument('--kernels', type=str, default = None, 
                      help='Kernel widths (e.g. --kernels="2,3,3,4"), if None, use the default ones')
  parser.add_argument('--verbose', default = False, action = "store_const", const = True, 
                      help='Enable debug messages')

  args = parser.parse_args()

  if len(sys.argv)<2 : 
    parser.print_help()
    raise SystemExit

  kernels = args.kernels
  if kernels : kernels = eval(kernels)

  input_tuple = args.input
  input_tree = args.intree
  input_branches = args.branches.split(":")
  start_event = args.start
  stop_event = args.stop

  output_tuple = args.output
  output_branch = args.pidgen
  stat_branch = args.stat

  sample_name = args.sample
  dataset_name = args.dataset
  variable_name = args.variable

  config = get_samples()[sample_name][dataset_name]
  variable = get_variables()[variable_name]

  pp = pprint.PrettyPrinter(indent = 4)

  if (args.verbose) : 
    print(f"Calibration sample config: {pp.pformat(config)}")
    print(f"Variable definition: {pp.pformat(variable)}")

  print(f"Starting to make the template")

  # Create PID resampling template based on calibration sample
  template = create_template(variable, config, 
                             use_calib_cache = args.usecache, max_files = args.maxfiles, 
                             interactive_plots = args.interactive, 
                             control_plots = args.plot, verbose = args.verbose)

  print(f"Template done, starting resampling")

  f = uproot.open(input_tuple)
  t = f[input_tree]
  all_branches = t.keys()
  if (args.verbose) : print (f"List of all input tree branches: {pp.pformat(all_branches)}")
  input_data = read_array(t, input_branches)    # Array with input data for PID resampling
  if stop_event > len(input_data) : stop_event = len(input_data)
  else : input_data = input_data[start_event:stop_event]
  if (args.verbose) : print (f"Shape of the array for resampling: {input_data.shape}")
  all_data = read_array(t, all_branches)[start_event:stop_event]  # Array with all input tree branches
  if (args.verbose) : print (f"Shape of all input data array: {all_data.shape}")

  data = data_transform(input_data, config)
  pid_arr, calib_stat = resample_data(data, config, variable, template, verbose = args.verbose)

  if (args.verbose) : 
    print(f"Data array after variable transformation: {data}")
    print(f"Resampled PID array: {pid_arr}")
    print(f"Resampling statistics array: {calib_stat}")

  write_array(output_tuple, np.concatenate([all_data, pid_arr, calib_stat], axis = 1), 
            branches = all_branches + [output_branch, stat_branch] )

if __name__ == "__main__" : 
  main()
