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
Definitions of LHCb PID calibration datasets (ROOT files produced by WG productions). 
The ROOT files can contain several trees corresponding to different calibration samples. 
These dictionaries are used further in the definitions of calibration samples (see samples/ subdir). 
"""

legacy_run2_pidcalib_datasets = {
  'MagDown_2018'   : ("root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision18/PIDCALIB.ROOT/00109278/0000/00109278_%8.8d_1.pidcalib.root", 436), 
  'MagUp_2018'     : ("root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision18/PIDCALIB.ROOT/00109276/0000/00109276_%8.8d_1.pidcalib.root", 437), 
  'MagDown_2017'   : ("root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision17/PIDCALIB.ROOT/00106052/0000/00106052_%8.8d_1.pidcalib.root", 249), 
  'MagUp_2017'     : ("root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision17/PIDCALIB.ROOT/00106050/0000/00106050_%8.8d_1.pidcalib.root", 189), 
  'MagDown_2016'   : ("root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision16/PIDCALIB.ROOT/00111825/0000/00111825_%8.8d_1.pidcalib.root", 182), 
  'MagUp_2016'     : ("root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision16/PIDCALIB.ROOT/00111823/0000/00111823_%8.8d_1.pidcalib.root", 185), 
  'MagDown_2015'   : ("root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision15/PIDCALIB.ROOT/00064785/0000/00064785_%8.8d_1.pidcalib.root", 87), 
  'MagUp_2015'     : ("root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/LHCb/Collision15/PIDCALIB.ROOT/00064787/0000/00064787_%8.8d_1.pidcalib.root", 48), 
}

converted_run1_pidcalib_datasets_dstar_k = {
  "MagUp_2011"   : ("root://eoslhcb.cern.ch//eos/lhcb/wg/PID/PIDCalib_Run1_conversion/Reco14_DATA/MagUp/DSt_K_MagUp_Strip21r1_%d.root", 24), 
  "MagUp_2012"   : ("root://eoslhcb.cern.ch//eos/lhcb/wg/PID/PIDCalib_Run1_conversion/Reco14_DATA/MagUp/DSt_K_MagUp_Strip21_%d.root", 72), 
  "MagDown_2011" : ("root://eoslhcb.cern.ch//eos/lhcb/wg/PID/PIDCalib_Run1_conversion/Reco14_DATA/MagUp/DSt_K_MagUp_Strip21r1_%d.root", 35), 
  "MagDown_2012" : ("root://eoslhcb.cern.ch//eos/lhcb/wg/PID/PIDCalib_Run1_conversion/Reco14_DATA/MagUp/DSt_K_MagUp_Strip21_%d.root", 71), 
}

converted_run1_pidcalib_datasets_dstar_pi = {
  "MagUp_2011"   : ("root://eoslhcb.cern.ch//eos/lhcb/wg/PID/PIDCalib_Run1_conversion/Reco14_DATA/MagUp/DSt_Pi_MagUp_Strip21r1_%d.root", 24), 
  "MagUp_2012"   : ("root://eoslhcb.cern.ch//eos/lhcb/wg/PID/PIDCalib_Run1_conversion/Reco14_DATA/MagUp/DSt_Pi_MagUp_Strip21_%d.root", 72), 
  "MagDown_2011" : ("root://eoslhcb.cern.ch//eos/lhcb/wg/PID/PIDCalib_Run1_conversion/Reco14_DATA/MagUp/DSt_Pi_MagUp_Strip21r1_%d.root", 35), 
  "MagDown_2012" : ("root://eoslhcb.cern.ch//eos/lhcb/wg/PID/PIDCalib_Run1_conversion/Reco14_DATA/MagUp/DSt_Pi_MagUp_Strip21_%d.root", 71), 
}
