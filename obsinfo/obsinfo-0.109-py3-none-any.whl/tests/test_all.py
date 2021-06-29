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
test_all_stage_types()
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


class TestObsinfo(unittest.TestCase):
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

    def test_readJSONREF_json(self):
        """
        Test JSONref using a JSON file.
        """
        fname_A =  PurePath(self.testing_path).joinpath("jsonref_A.json")
        A = ObsMetadata.read_json_yaml_ref(fname_A)
        AB = ObsMetadata.read_json_yaml_ref(PurePath(self.testing_path).joinpath(
                                              "jsonref_AB.json"))
        self.assertTrue(A == AB)

    def test_readJSONREF_yaml(self):
        """
        Test JSONref using a YAML file.
        """
        A = ObsMetadata.read_json_yaml_ref(PurePath(self.testing_path).joinpath(
                                             "jsonref_A.yaml"))
        AB = ObsMetadata.read_json_yaml_ref(PurePath(self.testing_path).joinpath(
                                              "jsonref_AB.yaml"))
        self.assertTrue(A == AB)

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
        
    def test_all_filters(self):
        """
        Test all information files in test/data/Information_Files/responses/_filters" subdirectory
        If you wish to test individual files, use test_filter(file) with file an absolute or 
        relative file name.
        """
        #files_in_test_dir = ObsMetadata.read_info_file(PurePath(self.testing_path).joinpath(
        files_in_test_dir = Path(self.testing_path).joinpath(
            "Information_Files",
            "responses",
            "_filters")
          
        if files_in_test_dir.is_dir():
            for dir in files_in_test_dir.iterdir():
               self.test_filters_in_directory(dir)
        
    def test_filters_in_directory(self, dir):
        """
        Test all information files in test filter directory.
        """
        if dir.is_dir():
            for file in dir.iterdir():
                self.test_filter(file)     

    def test_filter(self, info_file):
        """
        Test reading a filter file. All are actual examples except the info files called "test---attributes. 
        In this special cases there will also be a comparison against a dict of expected results
        """
        test_expected_result = { 
            'PolesZeros' : 
                {
                    "type": "PolesZeros",
                    "transfer_function_type": "LAPLACE (RADIANS/SECOND)",
                    "zeros": [(0.0+0.0j)],
                    "poles": [(0.546+0.191j), (4.00004e4+0.000j),],
                    "normalization_frequency" : 1.,
                    "normalization_factor" : 42833.458122775904,
                    "offset": 0,  
                },
            'FIR' : 
                {
                    "type": "FIR",
                    "symmetry": "ODD",
                    "coefficient_divisor": 8388608,
                    "coefficients": [-10944, 0, 103807, 0, -507903, 0, 2512192, 4194304,],
                    "offset": 7,  
                },
            'Coefficients' : 
                {
                    "type" : "Coefficients",
                    "transfer_function_type" : "DIGITAL", 
                    "numerator_coefficients" :   [1, 0.1, -0.3, 0.6],
                    "denominator_coefficients" : [-0.2, 0.8, 0.4, -0.3],
                    "offset": 0,
                },
            'ResponseList' : 
                {
                    "type" : "ResponseList",
                    "offset": 0,  
                    "response_list" : [[ 0.050, 0.56, 0.0], [ 0.075, 0.73, 0.0], [ 1, 1, 0.0], [10, 0.97, -179], [100, 0.96, 179], [1000, 0.96, 179], [5000, 0.82, 143], [7500, 0.69, 129]],
                },
            'AD_CONVERSION' : 
                {
                    "type" : "AD_CONVERSION",
                    "input_full_scale" : 5,
                    "output_full_scale" : 4294967292,
                    "transfer_function_type" : "DIGITAL",
                    "numerator_coefficients" :   [1.0],
                    "denominator_coefficients" : [],
                    "offset": 0,  
                },
            'ANALOG' : 
                {
                    "type" : "ANALOG",
                    "transfer_function_type" : "LAPLACE (RADIANS/SECOND)",
                    "zeros": [],
                    "poles": [],
                    "normalization_frequency" : 0.,
                    "normalization_factor" : 1.0,
                    "offset": 0,      
                },
            'DIGITAL' : 
                {
                    "type" : "DIGITAL",
                    "transfer_function_type" : "DIGITAL",
                    "numerator_coefficients" :   [1.0],
                    "denominator_coefficients" : [],
                    "offset": 0,                   
                },
             }
            
        read_stream = ObsMetadata.read_info_file(info_file)
        obj = Filter.dynamic_class_constructor(ObsMetadata(read_stream['filter']), "")
        
        if re.match("test---attributes", str(info_file.name)): # compare with expected result
            self.filter_compare(info_file, obj, test_expected_result)
            
        if self.verbose:
           print(f'Filter test for: {info_file.name}: PASSED')
        
        if self.print_output:    
           print(obj)
    
    def filter_compare(self, info_file, filter, expected_result):
        """
        Test a created filter object against an expected result to make sure all values are right
        """
        ftype = filter.type 
        read_dict = vars(filter)
        
        # Remove notes and extras
        if read_dict.get('notes', None) == []:
            read_dict.pop('notes')
        if read_dict.get('extras', None) == None:
            read_dict.pop('extras')
        
        self.assertEqual(read_dict,expected_result.get(ftype, None), f" File: '{info_file}'. Computed result: {read_dict} and expected result: {expected_result.get(ftype, None)} are different")
        
    
    def test_PZ_conditionals(self):
        """
        Test all the conditionals in the PZ filter, and the function to calculate the normalization factor.
        """
        obj = Filter.dynamic_class_constructor({'type': 'PolesZeros', 
                                         'transfer_function_type' : 'LAPLACE (RADIANS/SECOND)',
                                         'zeros': [[0.3, 0.2],],
                                         'poles': [[0.546, 0.191], [4.40e4, 0.000],],
                                         'normalization_frequency' : 1.,
                                         'normalization_factor' : None,
                                          })
        assertIn(obj.transfer_function_type, ['LAPLACE (RADIANS/SECOND)', 'LAPLACE (HERTZ)', 'DIGITAL (Z-TRANSFORM)'], 
                                              f'transfer function type wrong in test case for PZ {obj.transfer_function_type}')
        self.assertEqual(obj.normalization_factor,  44188.013594177224, 
                f'object normalization factor in test case for PZ {obj.normalization_factor} in PZ test is different from 44188.013594177224')
        
        obj = Filter.dynamic_class_constructor({'type': 'PolesZeros', 
                                         'transfer_function_type' : 'LAPLACE (HERTZ)',
                                         'zeros': [[0.3, 0.2],],
                                         'poles': [[0.546, 0.191], [4.40e4, 0.000],],
                                         'normalization_frequency' : 1.,
                                         'normalization_factor' : None,
                                          })
        assertIn(obj.transfer_function_type, ['LAPLACE (RADIANS/SECOND)', 'LAPLACE (HERTZ)', 'DIGITAL (Z-TRANSFORM)'], 
                                              f'transfer function type wrong in test case for PZ {obj.transfer_function_type}')
        self.assertEqual(obj.normalization_factor,  50262.70428857582, 
                    f'object normalization factor in test case for PZ {obj.normalization_factor} is different from 50262.70428857582')
        
        obj = Filter.dynamic_class_constructor({'type': 'PolesZeros', 
                                         'transfer_function_type' : 'LAPLACE (RADIANS/SECOND)',
                                         'zeros': [[0.3, 0.2],],
                                         'poles': [[0.546, 0.191], [4.40e4, 0.000],],
                                         'normalization_frequency' : 120.,
                                         'normalization_factor' : None,
                                          })
                                          
        self.assertEqual(obj.normalization_factor, 44006.993117493024, f'{obj.normalization_factor} in test case for PZ is different from 44006.993117493024')
        
        obj = Filter.dynamic_class_constructor({'type': 'PolesZeros', 
                                         'transfer_function_type' : 'LAPLACE (RADIANS/SECOND)',
                                         'zeros': [[0.3, 0.2],],
                                         'poles': [[0.546, 0.191], [4.40e4, 0.000],],
                                         'normalization_frequency' : None,
                                         'normalization_factor' : None,
                                          })
        
        self.assertEqual(obj.normalization_factor, None, f'{obj.normalization_factor} is different from None')
        
        obj = Filter.dynamic_class_constructor({'type': 'PolesZeros', 
                                         'transfer_function_type' : 'LAPLACE (RADIANS/SECOND)',
                                         'zeros': [],
                                         'poles': [],
                                         'normalization_frequency' : 1.,
                                         'normalization_factor' : None,
                                          })
        
        self.assertEqual(obj.normalization_factor, 1., f'{obj.normalization_factor} is different from 1.')
        
        obj = Filter.dynamic_class_constructor({'type': 'PolesZeros', 
                                         'transfer_function_type' : 'DIGITAL (Z-TRANSFORM)',
                                         'zeros': [[0.3, 0.2],],
                                         'poles': [[0.546, 0.191], [4.40e4, 0.000],],
                                         'normalization_frequency' : 1.,
                                         'normalization_factor' : None,
                                          })
        
        assertIn(obj.transfer_function_type, ['LAPLACE (RADIANS/SECOND)', 'LAPLACE (HERTZ)', 'DIGITAL (Z-TRANSFORM)'], 
                                              f'transfer function type wrong in test case for PZ {obj.transfer_function_type}')
        self.assertEqual(obj.normalization_factor,  None, 
                    f'object normalization factor {obj.normalization_factor} is different from None')
    
    def test_all_stage_types(self):
        """
        Test reading and converting to obspy a stage file with each filter type. 
        This is the first time obspy conversion occurs so make sure it's done right
        ONly one example stage for each type. If you wish to test all stage files,
        use test_all_responses(). If you wish to test individual files use test_state_with_XXX(file)
        with file as stripped file name. 
        File must exist in obsinfo/Information_files/instrumentation/YYY/responses
        """
        self.test_stage_with_FIR('TI_ADS1281_FIR1.stage.yaml')
        self.test_stage_with_PZ('SIO-LDEO_DPG_5018_calibrated.stage.yaml')
        self.test_stage_with_coefficients('test-with-coeff.stage.yaml')
        self.test_stage_with_response_list('test-with-response-list.stage.yaml')
        
    def test_all_responses(self):
        """
        Test all information files in each responses subdirectory.
        """
        #files_in_test_dir = ObsMetadata.read_info_file(PurePath(self.testing_path).joinpath(
        files_in_test_dir = Path(self.infofiles_path).joinpath("instrumentation")
        
        if files_in_test_dir.is_dir():
            for dir in files_in_test_dir.iterdir():
                if dir.is_dir():
                    self.test_responses_in_directory(dir)
        
    def test_responses_in_directory(self, dir):
        """
        Test all information files in test responses directory.
        """               
        datalogger_dir_re = re.compile(".*/dataloggers")
        sensor_dir_re = re.compile(".*/sensors")
        exception_re = re.compile(".*/test-with")
        
        if re.match(datalogger_dir_re, str(dir)):
            for file in (Path(dir).joinpath("responses")).iterdir():
                print(f'test stage with FIR "{file}"')
                if not file.is_dir() and re.match(exception_re, str(file)) == None: 
                    self.test_stage_with_FIR(file)
        elif re.match(sensor_dir_re, str(dir)):
            for file in (Path(dir).joinpath("responses")).iterdir():
                print(f'test stage with PZ "{file}"')
                if not file.is_dir() and re.match(exception_re, str(file)) == None: 
                    self.test_stage_with_PZ(file)   

        
    def test_stage_with_FIR(self, file):
        """
        Test reading and converting to obspy a stage file with FIR filter.
        """
        info_file = PurePath(self.infofiles_path).joinpath(
            'instrumentation',
            'dataloggers',
            'responses',
            file
            )
        
        info_file_dict = ObsMetadata.read_info_file(info_file)
           
        stage_from_info_file = Stage(ObsMetadata(info_file_dict['stage']))
        
        obspy_result = stage_from_info_file.to_obspy()
        self.test_common_attributes(stage_from_info_file, obspy_result)
        
        if isinstance(filter, FIR):
            self.assertEqual(stage_from_info_file.filter.symmetry, obspy_result._symmetry)
            for info_file_coeff in stage_from_info_file.filter.coefficients:
                for obspy_coeff in obspy_result.decimation_correction:
                    self.assertEqual(info_file_coeff / 512, obspy_coeff (f))
                
        if self.verbose:
            print(f'Stage test for: {info_file.name}: PASSED')
    
    def test_stage_with_PZ(self, file):
        """
        Test reading and converting to obspy a stage file with PolesZeros filter.
        """
        info_file = PurePath(self.infofiles_path).joinpath(
            'instrumentation',
            'sensors',
            'responses',
            file)
        info_file_dict = ObsMetadata.read_info_file(info_file)

        stage_from_info_file = Stage(ObsMetadata(info_file_dict['stage']))
        obspy_result = stage_from_info_file.to_obspy()
        
        self.test_common_attributes(stage_from_info_file, obspy_result)    
            
        self.assertEqual(stage_from_info_file.filter.transfer_function_type, obspy_result.pz_transfer_function_type)
        self.assertEqual(stage_from_info_file.filter.normalization_frequency, obspy_result.normalization_frequency)
        self.assertEqual(stage_from_info_file.filter.normalization_factor, obspy_result.normalization_factor)
        self.assertEqual(stage_from_info_file.filter.zeros, obspy_result.zeros)
        self.assertEqual(stage_from_info_file.filter.poles, obspy_result.poles)
                
        if self.verbose:
            print(f'Stage test for: {info_file.name}: PASSED')
            
    def test_stage_with_response_list(self, file):
        """
        Test reading and converting to obspy a stage file with Response List filter.
        """
        info_file = PurePath(self.infofiles_path).joinpath(
            'instrumentation',
            'sensors',
            'responses',
            file)
        info_file_dict = ObsMetadata.read_info_file(info_file)

        stage_from_info_file = Stage(ObsMetadata(info_file_dict['stage']))
        obspy_result = stage_from_info_file.to_obspy()
        self.test_common_attributes(stage_from_info_file, obspy_result)
        self.assertEqual(stage_from_info_file.filter.response_list, obspy_result.response_list_elements)
        
        if self.verbose:
            print(f'Stage test for: {info_file.name}: PASSED')
    
    def test_stage_with_coefficients(self, file):
        
        """
        Test reading and converting to obspy a stage file with Coeff filter.
        """
        info_file = PurePath(self.infofiles_path).joinpath(
            'instrumentation',
            'sensors',
            'responses',
            file)
        info_file_dict = ObsMetadata.read_info_file(info_file)

        stage_from_info_file = Stage(ObsMetadata(info_file_dict['stage']))
        obspy_result = stage_from_info_file.to_obspy()
        
        self.test_common_attributes(stage_from_info_file, obspy_result)
        self.assertEqual(stage_from_info_file.filter.transfer_function_type, obspy_result.cf_transfer_function_type)
        self.assertEqual(stage_from_info_file.filter.numerator_coefficients, obspy_result.numerator)
        self.assertEqual(stage_from_info_file.filter.denominator_coefficients, obspy_result.denominator)

        if self.verbose:
            print(f'Stage test for: {info_file.name}: PASSED')
    
    def test_common_attributes(self, stage_from_info_file, obspy_result):
        self.assertEqual(stage_from_info_file.name, obspy_result.name)
        self.assertEqual(stage_from_info_file.description, obspy_result.description)
        self.assertEqual(stage_from_info_file.input_units, obspy_result.input_units)
        self.assertEqual(stage_from_info_file.output_units, obspy_result.output_units)
        self.assertEqual(stage_from_info_file.input_units_description, obspy_result.input_units_description)
        self.assertEqual(stage_from_info_file.output_units_description, obspy_result.output_units_description)
        self.assertEqual(stage_from_info_file.gain, obspy_result.stage_gain)
        self.assertEqual(stage_from_info_file.gain_frequency, obspy_result.stage_gain_frequency)
        self.assertEqual(stage_from_info_file.decimation_factor, obspy_result.decimation_factor)
        self.assertEqual(stage_from_info_file.filter.offset, obspy_result.decimation_offset)
        self.assertEqual(stage_from_info_file.delay, obspy_result.decimation_delay)
        self.assertEqual(stage_from_info_file.correction, obspy_result.decimation_correction)
        #Notes and extras are not compared
           
    def test_response_stage_addition(self):
        """
        Test reading and combining response_stages.
        """
        read_info_A = ObsMetadata.read_info_file(PurePath(self.infofiles_path).joinpath( 
            'instrumentation',
            'sensors',
            'responses',
            'Trillium_T240_SN400-singlesided_theoretical.stage.yaml'))
        read_info_B = ObsMetadata.read_json_yaml_ref(PurePath(self.infofiles_path).joinpath(
            'instrumentation',
            'dataloggers',
            'responses',
            'TexasInstruments_ADS1281_100sps-linear_theoretical.response_stages.yaml'))
        stages_A = ResponseStages(read_info_A['response']['stages'])
        stages_B = ResponseStages(read_info_B['response']['stages'])
        stages = stages_A + stages_B
        #obspy_result = stages.to_obspy()
    
    def test_all_components(self):
        """
        Test all information files in each responses subdirectory.
        """
        #files_in_test_dir = ObsMetadata.read_info_file(PurePath(self.testing_path).joinpath(
        files_in_test_dir = Path(self.infofiles_path).joinpath("instrumentation")
        
        if files_in_test_dir.is_dir():
            for dir in files_in_test_dir.iterdir():
                if dir.is_dir():
                    self.test_components_in_directory(dir)
        
    def test_components_in_directory(self, dir):
        """
        Test all information files in test responses directory.
        """               
        datalogger_dir_re = re.compile(".*/dataloggers")
        preamplifier_dir_re = re.compile(".*/preamplifiers")
        sensor_dir_re = re.compile(".*/sensors")

        if re.match(datalogger_dir_re, str(dir)):
            for file in Path(dir).iterdir():
                if not file.is_dir():
                    self.test_datalogger(file)
                  
        elif re.match(preamplifier_dir_re, str(dir)):
            for file in Path(dir).iterdir():
                if not file.is_dir():
                    self.test_preamplifier(file)
                  
        elif re.match(sensor_dir_re, str(dir)):
            for file in Path(dir).iterdir():
                if not file.is_dir():
                    self.test_sensor(file)
                  
                
    def test_datalogger(self, file='LC2000.datalogger.yaml'):
        """
        Test reading datalogger instrument_compoents.
        """
        info_file_dict = ObsMetadata.read_info_file(PurePath(self.infofiles_path).joinpath(
            'instrumentation',
            'dataloggers',
            file))
        
        #OJO: no configuraton passed from above. No delay_correction either.
        obj = InstrumentComponent.dynamic_class_constructor('datalogger', info_file_dict)
        
        if self.verbose:   
           print(f'{file}: PASSED')
           
        if self.print_output:
            PrintObs.print_component(obj)

    def test_sensor(self, file='NANOMETRICS_T240_SINGLESIDED.sensor.yaml'):
        """
        Test reading sensor instrument_compoents.
        """
        info_file_dict = ObsMetadata.read_info_file(PurePath(self.infofiles_path).joinpath( 
            'instrumentation',
            'sensors',
            file))
        
        #OJO: no configuraton passed from above. No delay_correction either.
        obj = InstrumentComponent.dynamic_class_constructor('sensor', info_file_dict)
        
        if self.verbose:   
           print(f'{file}: PASSED')
           
        if self.print_output:
            PrintObs.print_component(obj)
        
    def test_preamplifier(self, file='LCHEAPO_BBOBS.preamplifier.yaml'):
        """
        Test reading sensor instrument_compoents.
        """
        info_file_dict = ObsMetadata.read_info_file(PurePath(self.infofiles_path).joinpath( 
            'instrumentation',
            'preamplifiers',
            file))
        
        if self.verbose:   
           print(f'Processing: {file}')
        
        #OJO: no configuraton passed from above. No delay_correction either.
        obj = InstrumentComponent.dynamic_class_constructor('preamplifier', info_file_dict)
        
        if self.verbose:   
           print(f'{file}: PASSED')
        
        if self.print_output:
            PrintObs.print_component(obj)
        
         
    def test_instrumentation(self, file='SPOBS2.instrumentation.yaml', level="all"):
        """
        Test reading instrumentation.
        """
        dict = ObsMetadata.read_info_file(PurePath(self.infofiles_path).joinpath(
            'instrumentation',
            file))
        
        start_date = end_date = UTCDateTime(0)
        
        location_dict = {
                           "position": {"lon": 0., "lat": 0., "elev": 0.},
                           "base":  { "depth.m": 0.,
                                "geology": "unknown",
                                "vault": "Sea floor",
                                "uncertainties.m": {"lon": 0., "lat": 0., "elev": 0.},
                                "localisation_method": "Sea surface release point"
                               }
                        }
        
        location = Location(location_dict)
        locations={"00": location}
        
        print(f'Processing "{file}"')
        obj = Instrumentation(ObsMetadata(dict['instrumentation']), locations, start_date, end_date, {})
     
        if self.verbose:   
           print(f'{file}: PASSED')
        
        if self.print_output:
            PrintObs.print_instrumentation(obj)
            
        
    def test_all_instrumentation(self, level="all"):
        """
        Test all information files in each responses subdirectory.
        """
        #files_in_test_dir = ObsMetadata.read_info_file(PurePath(self.testing_path).joinpath(
        files_in_test_dir = Path(self.infofiles_path).joinpath("instrumentation")
        
        if files_in_test_dir.is_dir():
            for file in files_in_test_dir.iterdir():
                if not file.is_dir():
                    self.test_instrumentation(file, level)
                    
                 
    def test_station(self, file_name='TEST.station.yaml', level="all"):
        """
        Test reading a station.
        """
        info_dict = ObsMetadata.read_info_file(PurePath(self.infofiles_path).joinpath( 
            'network',
            file_name))
        
        info_dict = info_dict['stations']
        key = list(info_dict.keys())[0]
        value = ObsMetadata(list(info_dict.values())[0])
        
        obj = Station(key, value)
        
        if self.verbose:
           print(f'Station test for: {file_name}: PASSED')
           
        if self.print_output:
            PrintObs.print_station(obj, level)
             
    def test_network(self, file_name='BBOBS.INSU-IPGP.network.yaml', level="all"):
        """
        Test reading a network.
        """
        info_dict = ObsMetadata.read_info_file(PurePath(self.infofiles_path).joinpath( 
            'network',
            file_name))
        
        net_dict = info_dict.get('network',None)
        if not net_dict:
            return 
        
        if self.verbose:
            print(f'Processing network file: {file_name}')
        obj = Network(ObsMetadata(net_dict))
        
        if self.verbose:
           print(f'Network test for: {file_name}: PASSED')
           
        if self.print_output:
            PrintObs.print_network(obj, level)
    
    def test_all_networks(self, level="all"):
        """
        Test all information files in each responses subdirectory.
        """
        #files_in_test_dir = ObsMetadata.read_info_file(PurePath(self.testing_path).joinpath(
        files_in_test_dir = Path(self.infofiles_path).joinpath("network")
        
        if files_in_test_dir.is_dir():
            for file in files_in_test_dir.iterdir():
                if not file.is_dir() and not file == 'TEST.station.yaml':
                    self.test_network(file, level)
                                      
    
    
def suite():
    return unittest.makeSuite(TestObsinfo, 'test')


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
