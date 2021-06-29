#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Functions to validate YAML or JSON formats versus a schema

"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA @UnusedWildImport

import os
from pathlib import Path, PurePath
import glob
import unittest
import inspect
import difflib
import re
from obspy.core.utcdatetime import UTCDateTime
# from pprint import pprint
# import xml.etree.ElementTree as ET
# from CompareXMLTree import XmlTree
from obsinfo.obsMetadata.obsmetadata import (ObsMetadata)
                                     #validate, _read_json_yaml,
                                     #ObsMetadata.read_json_yaml_ref, ObsMetadata.read_info_file)
# from obsinfo.info_dict import InfoDict
from obsinfo.instrumentation import (Instrumentation, InstrumentComponent,
                                     Datalogger, Preamplifier, Sensor,
                                     ResponseStages, Stage, Filter)
from obsinfo.instrumentation.instrumentation import (Location)
from obsinfo.network import (Station, Network)
from obsinfo.instrumentation.filter import (Filter, PolesZeros, FIR, Coefficients, ResponseList,
                     Analog, Digital, AD_Conversion)



class Validate(object):
    
    def setUp(self, verbose=True, quiet=False):
        self.path = Path("").resolve().parent
        self.testing_path = PurePath(self.path).joinpath('obsinfo', 'obsinfo', "tests", "data")
        self.infofiles_path =  PurePath(self.path).joinpath(self.path,
                                           'obsinfo', 
                                           'obsinfo',
                                           '_examples',
                                           'Information_Files')
        
        self.verbose = verbose
        self.quiet = quiet

    def validate_filters(self):
        """
        Test validate filter files
        """
        for ftype in ["PoleZeros", "FIR"]:
            for fname in glob.glob(PurePath(self.infofiles_path).joinpath(
                                                "instrumentation",
                                                "*",
                                                "responses",
                                                ftype,
                                                "*.filter.yaml")):
                self.assertTrue(validate(fname, self.quiet))

    def validate_responses(self):
        """
        Test validate sensor files
        """
        for component_dir in ["sensors", "dataloggers", "preamplifiers"]:
            glob_name = PurePath(self.infofiles_path).joinpath( "instrumentation",
                                     component_dir, "responses",
                                     "*.response.yaml")
            for fname in glob.glob(glob_name):
                self.assertTrue(validate(fname, self.quiet))

    def validate_components(self):
        """
        Test validate instrument_component files
        """
        for component in ["sensors", "dataloggers", "preamplifiers"]:
            glob_name = PurePath(self.infofiles_path).joinpath( "instrumentation",
                                     component+'s', f"*.{component}.yaml")
            for fname in glob.glob(glob_name):
                self.assertTrue(validate(fname, self.quiet))

    def validate_instrumentation(self):
        """
        Test validate instrumentation files
        """
        for fname in glob.glob(PurePath(self.infofiles_path).joinpath(
                                            "instrumentation",
                                            "*.instrumentation.yaml")):
            self.assertTrue(validate(fname, self.quiet))

    def validate_station(self):
        """
        Test validate network files
        """
        for fname in glob.glob(PurePath(self.infofiles_path).joinpath(
                                            "network",
                                            "*.station.yaml")):
            self.assertTrue(validate(fname, self.quiet))

    def validate_networks(self):
        """
        Test validate network files
        """
        for fname in glob.glob(PurePath(self.infofiles_path).joinpath(
                                            "network",
                                            "*.network.yaml")):
            self.assertTrue(validate(fname, self.quiet))

