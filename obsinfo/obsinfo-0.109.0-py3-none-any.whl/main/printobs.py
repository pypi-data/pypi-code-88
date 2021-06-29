#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Functions to print obsinfo objects

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
from ..instrumentation import (Instrumentation, InstrumentComponent,
                                     Datalogger, Preamplifier, Sensor,
                                     ResponseStages, Stage, Filter)
from ..instrumentation.instrumentation import (Location)
from ..network import (Station, Network)
from ..instrumentation.filter import (Filter, PolesZeros, FIR, Coefficients, ResponseList,
                     Analog, Digital, AD_Conversion)


class PrintObs(object):
    
    @staticmethod
    def print_component(obj, level="all"):
        if not obj:
            return
        print(obj)
        if level == "channel":
            return 
        
        print(obj.equipment)
        
    @staticmethod
    def print_instrumentation(obj, level="all"):
        print(obj)
        print("Instrument:\n")
        print(obj.equipment)
        for k in obj.channels:
            print(k)
            if level != "instrumentation":
                print(k.instrument)
                PrintObs.print_component(k.instrument.sensor, level)
                PrintObs.print_component(k.instrument.preamplifier, level)
                PrintObs.print_component(k.instrument.datalogger, level)
            
            if k.instrument.sensor.response_stages.stages and level != "component":
                for s in k.instrument.sensor.response_stages.stages:
                   print(s)
                   if level == "all":
                       print(s.filter) 
            
    
    @staticmethod            
    def print_station(obj, level="all"):
        print(obj)
        print(obj.locations)
        for k, v in obj.locations.items():
            print(f'Location {k}: {v}')
        if level != "station":
            PrintObs.print_instrumentation(obj.instrumentation, level)
    
    @staticmethod        
    def print_network(obj, level="all"):
        print(obj)
        print(obj.operator)
        if level != "network":
            for v in obj.stations:
                PrintObs.print_station(v, level)
                   