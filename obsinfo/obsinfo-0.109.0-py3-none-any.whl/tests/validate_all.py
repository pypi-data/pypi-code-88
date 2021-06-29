#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Functions to test the lcheapo functions
There are two types of testing functionalities.
a) If the file name includes "test--attributes" the output of the corresonding obsinfo test function
will be checked against data contained in this class.
b) If the fine name is "normal", it will simply run through to make sure there are no errors
Testing for filters uses data from obsinfo/tests/data/Information_Files/responses/_filters. 
Testing for all other classes uses data from obsinfo/_examples/Information_Files 
WARNING: many tests are crtically dependent on file hierarchy, including names. Do not change names
in tests or _examples hierarchy, or else change the names here.
Also, the following methods use four specific filen names:
validate_all_stage_types()
test_senso()
test_preamplifier()
test_datalogger()
test_station()
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
from obsinfo.main.printobs import  (PrintObs)


class ValidateObsinfo(unittest.TestCase):
    """
    Test suite for obsinfo operations.
    """
    def setUp(self, verbose=True, print_output=True):
        self.path = Path("").resolve().parent
        self.testing_path = PurePath(self.path).joinpath('obsinfo', 'obsinfo', "tests", "data")
        self.infofiles_path =  PurePath(self.path).joinpath(self.path,
                                           'obsinfo', 
                                           'obsinfo',
                                           '_examples',
                                           'Information_Files')
        
        self.verbose = verbose
        self.print_output = print_output

    def assertTextFilesEqual(self, first, second, msg=None):
        with open(first) as f:
            str_a = f.read()
        with open(second) as f:
            str_b = f.read()

        if str_a != str_b:
            first_lines = str_a.splitlines(True)
            second_lines = str_b.splitlines(True)
            delta = difflib.unified_diff(
                first_lines, second_lines,
                fromfile=first, tofile=second)
            message = ''.join(delta)

            if msg:
                message += " : " + msg

            self.fail("Multi-line strings are unequal:\n" + message)

    def test_validate_json(self):
        """
        Test validation on a YAML file.

        The test file as an $ref to a file that doesn't exist, a field that
        is not specified in the the schema, and lacks a field required in
        the schema
        """
        test_file = PurePath(self.testing_path).joinpath( 'json_testschema.json')
        test_schema = PurePath(self.testing_path).joinpath(
                                   'json_testschema.schema.json')
        # self.assertFalse(validate(test_file, schema_file=test_schema,
        #                           quiet=True))

        # Run the code
        cmd = f'obsinfo-validate -s {test_schema} {test_file} > temp'
        os.system(cmd)

        # Compare text files
        self.assertTextFilesEqual(
            'temp',
            PurePath(self.testing_path).joinpath( 'json_testschema.out.txt')
            )
        os.remove('temp')
        
    def validate_all_filters(self):
        """
        Test all information files in test/data/Information_Files/responses/_filters" subdirectory
        If you wish to test individual files, use test_filter(file) with file an absolute or 
        relative file name.
        """
        #files_in_validate_dir = ObsMetadata.read_info_file(PurePath(self.testing_path).joinpath(
        files_in_validate_dir = Path(self.testing_path).joinpath(
            "Information_Files",
            "responses",
            "_filters")
          
        if files_in_validate_dir.is_dir():
            for dir in files_in_validate_dir.iterdir():
               self.validate_filters_in_directory(dir)
        
    def validate_filters_in_directory(self, dir):
        """
        Test all information files in test filter directory.
        """
        if dir.is_dir():
            for file in dir.iterdir():
                self.validate_filter(file)     

    def validate_filter(self, info_file):
        """
        Test reading a filter file. All are actual examples except the info files called "test---attributes. 
        In this special cases there will also be a comparison against a dict of expected results
        """
        ret = ObsMetadata().validate(info_file, "yaml", "filter", self.verbose, "filter", False)
            
        if ret and self.verbose:
           print(f'Filter test for: {info_file.name}: PASSED')
        
    def validate_all_responses(self):
        """
        Test all information files in each responses subdirectory.
        """
        #files_in_validate_dir = ObsMetadata.read_info_file(PurePath(self.testing_path).joinpath(
        files_in_validate_dir = Path(self.infofiles_path).joinpath("instrumentation")
        
        if files_in_validate_dir.is_dir():
            for dir in files_in_validate_dir.iterdir():
                if dir.is_dir():
                    self.validate_responses_in_directory(dir)
        
    def validate_responses_in_directory(self, dir):
        """
        Test all information files in test responses directory.
        """               
        datalogger_dir_re = re.compile(".*/dataloggers")
        sensor_dir_re = re.compile(".*/sensors")
        exception_re = re.compile(".*/test-with")
        
        if re.match(datalogger_dir_re, str(dir)) or re.match(sensor_dir_re, str(dir)):
            for file in (Path(dir).joinpath("responses")).iterdir():
                print(f'test stage with FIR "{file}"')
                if not file.is_dir() and re.match(exception_re, str(file)) == None: 
                    self.validate_stage(file)        
        
    def validate_stage(self, file):
        """
        Test reading and converting to obspy a stage file with FIR filter.
        """
        info_file = PurePath(self.infofiles_path).joinpath(
            'instrumentation',
            'dataloggers',
            'responses',
            file
            )
        
        ret = ObsMetadata().validate(info_file, "yaml", "stage", self.verbose, "stage", False)
                
        if ret and self.verbose:
            print(f'Stage test for: {info_file.name}: PASSED')
    
            
        
    def validate_all_components(self):
        """
        Test all information files in each responses subdirectory.
        """
        #files_in_validate_dir = ObsMetadata.read_info_file(PurePath(self.testing_path).joinpath(
        files_in_validate_dir = Path(self.infofiles_path).joinpath("instrumentation")
        
        if files_in_validate_dir.is_dir():
            for dir in files_in_validate_dir.iterdir():
                if dir.is_dir():
                    self.validate_components_in_directory(dir)
        
    def validate_components_in_directory(self, dir):
        """
        Test all information files in test responses directory.
        """               
        datalogger_dir_re = re.compile(".*/dataloggers")
        preamplifier_dir_re = re.compile(".*/preamplifiers")
        sensor_dir_re = re.compile(".*/sensors")

        if re.match(datalogger_dir_re, str(dir)):
            for file in Path(dir).iterdir():
                if not file.is_dir():
                    self.validate_datalogger(file)
                  
        elif re.match(preamplifier_dir_re, str(dir)):
            for file in Path(dir).iterdir():
                if not file.is_dir():
                    self.validate_preamplifier(file)
                  
        elif re.match(sensor_dir_re, str(dir)):
            for file in Path(dir).iterdir():
                if not file.is_dir():
                    self.validate_sensor(file)
                  
                
    def validate_datalogger(self, info_file='LC2000.datalogger.yaml'):
        """
        Test reading datalogger instrument_compoents.
        """
        
        #OJO: no configuraton passed from above. No delay_correction either.
        ret = ObsMetadata().validate(info_file, "yaml", "datalogger", self.verbose, "datalogger", False)
        
        if ret and self.verbose:   
           print(f'{info_file}: PASSED')
           
    def validate_sensor(self, info_file='NANOMETRICS_T240_SINGLESIDED.sensor.yaml'):
        """
        Test reading sensor instrument_compoents.
        """
        
        #OJO: no configuraton passed from above. No delay_correction either.
        ret = ObsMetadata().validate(info_file, "yaml", "sensor", self.verbose, "sensor", False)
        
        if ret and self.verbose:   
           print(f'{info_file}: PASSED')
        
    def validate_preamplifier(self, info_file='LCHEAPO_BBOBS.preamplifier.yaml'):
        """
        Test reading sensor instrument_compoents.
        """
        
        #OJO: no configuraton passed from above. No delay_correction either.
        ret = ObsMetadata().validate(info_file, "yaml", "preamplifier", self.verbose, "preamplifier", False)
        
        if ret and self.verbose:   
           print(f'{info_file}: PASSED')
         
    def validate_instrumentation(self, info_file='SPOBS2.instrumentation.yaml', level="all"):
        """
        Test reading instrumentation.
        """
        
        ret = ObsMetadata().validate(info_file, "yaml", "instrumentation", self.verbose, "instrumentation", False)
     
        if ret and self.verbose:   
           print(f'{info_file}: PASSED')
        
        
    def validate_all_instrumentation(self, level="all"):
        """
        Test all information files in each responses subdirectory.
        """
        #files_in_validate_dir = ObsMetadata.read_info_file(PurePath(self.testing_path).joinpath(
        files_in_validate_dir = Path(self.infofiles_path).joinpath("instrumentation")
        
        if files_in_validate_dir.is_dir():
            for file in files_in_validate_dir.iterdir():
                if not file.is_dir():
                    self.validate_instrumentation(file, level)
                    
                 
    def validate_station(self, info_file='TEST.station.yaml', level="all"):
        """
        Test reading a station.
        """
        ret = ObsMetadata().validate(info_file, "yaml", "station", self.verbose, "station", False)
                
        if ret and self.verbose:
           print(f'Station test for: {info_file}: PASSED')

             
    def validate_network(self, info_file='BBOBS.INSU-IPGP.network.yaml', level="all"):
        """
        Test reading a network.
        """
        
        ret = ObsMetadata().validate(info_file, "yaml", "network", self.verbose, "network", False)
        
        if ret and self.verbose:
           print(f'Network test for: {info_file}: PASSED')
           
    
    def validate_all_networks(self, level="all"):
        """
        Test all information files in each responses subdirectory.
        """
        #files_in_validate_dir = ObsMetadata.read_info_file(PurePath(self.testing_path).joinpath(
        files_in_validate_dir = Path(self.infofiles_path).joinpath("network")
        
        if files_in_validate_dir.is_dir():
            for file in files_in_validate_dir.iterdir():
                if not file.is_dir() and not file == 'TEST.station.yaml':
                    self.validate_network(file, level)
                                      
    
