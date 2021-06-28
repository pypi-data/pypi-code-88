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

variable = {
    "branch" : "probe_MC15TuneV1_ProbNNp", 
    "data_range" : (0., 1.), 
    "transform_forward" : lambda x : 1.-(1.-x**0.25)**0.5, 
    "transform_backward" : lambda x : (1.-(1.-x)**2)**4, 
    "normalise_bins" : 1000, 
    "normalise_method" : "gauss", 
    "normalise_range" : (-2.5, 2.5), 
    "template_bins" : 200, 
    "template_sigma" : 2., 
    "resample_bins" : 200, 
}
