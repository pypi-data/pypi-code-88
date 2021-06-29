"""
Response Stage class
"""
# Standard library modules
import warnings
import re

# Non-standard modules
from obspy.core.inventory.response import (PolesZerosResponseStage,
                                           FIRResponseStage,
                                           CoefficientsTypeResponseStage,
                                           ResponseListResponseStage,
                                           Response)
from obspy.core.inventory.response import Response as obspy_Response

import obspy.core.util.obspy_types as obspy_types

# Local modules
from ..obsMetadata.obsmetadata import (ObsMetadata)
from .filter import (Filter, PolesZeros, FIR, Coefficients, ResponseList,
                     Analog, Digital, AD_Conversion)


class ResponseStages():
    """
    ReponseStages class

    An ordered list of Stages. Method can be invoked with attribute_list as a single element of class 
    Stage or as a list of them. 
    """
    def __init__(self, attribute_list, channel_modif={}, selected_config={}, delay_correction=None):
        
        if attribute_list == None:
            raise TypeError(f'No stages found in information file')
        elif not isinstance(attribute_list, list): #Not a list, single element
            self.stages = Stage(ObsMetadata(attribute_list), 
                                 channel_modif,
                                 selected_config, 
                                 delay_correction, 
                                 0) #last argument is position in list

        else:
            self.stages = [Stage(ObsMetadata(s), 
                                 channel_modif,
                                 selected_config, 
                                 delay_correction, 
                                 i) for s, i in zip(attribute_list, range(0, len(attribute_list)))] #last argument is position in list

        self.obspy_stages = self.to_obspy()

        #delay, delay corrections and sample rates (if not present for digital stages)  will be calculated for the whole instrumentation
           
        
    def to_obspy(self):
        """
        Return equivalent obspy response class
        """
        if not self.stages:
            return None
        
        obspy_stages = [s.to_obspy() for s in self.stages]
        
        return obspy_stages
                                   
        
    def __repr__(self):

        if self.stages != None:
            return f' Number of response stages: {len(self.stages):d}' 
        else:
            return f'Response_Stages: (empty)'
        

class Stage(object):
    """
    Stage class
    """
    def __init__(self, attributes_dict, channel_modif_list={}, selected_config={}, 
                 delay_correction=None, sequence_number=-1):
        
        if attributes_dict == None:
            return None
        
        channel_modif = self.get_selected_modifications(channel_modif_list, str(sequence_number))
        
        name = attributes_dict.get_configured_element('name', channel_modif, selected_config, '')
            
        self.name = name if name else sequence_number #stage id is either the name or a sequence number

        self.description = attributes_dict.get_configured_element('description', 
                                                            channel_modif, 
                                                            selected_config,
                                                            '')
        self.input_units = attributes_dict.get_configured_element('input_units', 
                                                            channel_modif, 
                                                            selected_config, None).get('name', None)
        
        self.output_units = attributes_dict.get_configured_element('output_units', 
                                                             channel_modif, 
                                                             selected_config, None).get('name', None)
        
        gain_dict = ObsMetadata(attributes_dict.get('gain', {}))
        if gain_dict:
            modif_gain_dict = channel_modif.get('gain', {})
            self.gain = gain_dict.get_configured_element('value', 
                                                         modif_gain_dict, 
                                                         selected_config,
                                                          1.0)             
            self.gain_frequency = gain_dict.get_configured_element('frequency', 
                                                                   modif_gain_dict, 
                                                                   selected_config, 
                                                                   0.0)
        else:
            raise TypeError(f'No gain specified in stage {self.name}')
        
        #In this version filter cannot be changed by configuration
        self.filter = Filter.dynamic_class_constructor(ObsMetadata(attributes_dict.get('filter', None)),
                                                       channel_modif.get('filter', None),
                                                       selected_config, 
                                                       self.name)
        if not self.filter:
            raise TypeError(f'No filter in stage {self.name}')
        
        self.stage_sequence_number = -1
        
        input_dict = input_units_description=attributes_dict.get_configured_element('input_units', 
                                                                                    channel_modif, 
                                                                                    selected_config, 
                                                                                    None)
        if input_dict:
            self.input_units_description = input_dict.get('description', None)
        output_dict = output_units_description=attributes_dict.get_configured_element('output_units', 
                                                                                      channel_modif, 
                                                                                      selected_config, 
                                                                                      None)
        if output_dict:  
            self.output_units_description = output_dict.get('description', None)
        self.input_sample_rate = attributes_dict.get_configured_element('input_sample_rate', 
                                                                  channel_modif, 
                                                                  selected_config, 
                                                                  None) 
        
        
        
        self.delay = attributes_dict.get_configured_element('delay', channel_modif, selected_config, None)
        self.decimation_factor = attributes_dict.get_configured_element('decimation_factor', 
                                                                  channel_modif, 
                                                                  selected_config,
                                                                  1)
        self.correction = delay_correction
        
        #default polarity is positive
        self.polarity = attributes_dict.get_configured_element('polarity', channel_modif, selected_config, 1)
                
        #self.calculate_delay(delay_correction)
        
        self.calibration_date = attributes_dict.get_configured_element('calibration_date', selected_config, None)
        
        self.instrument_sensitivity = None #Overall sensitivity will be calculated using obspy and stored in first stage
        
                  
    @property
    def output_sample_rate(self):
        if self.input_sample_rate and self.decimation_factor:
            return self.input_sample_rate / self.decimation_factor
        else:
            return None

    def calculate_delay(self, delay_correct):
        """
        Calculates delay as a function of object for digital filters if delay not specified
        Otherwise, uses delay as passed in the arguments
        Also applies delay_correction in the following way:
            - If delay_correct == None, correction is not applied and self.correction values are made equal to delay values
            - Otherwise, self.correction will be 0 except for the last stage, which will be correct.value
              but is set elsewhere (in datalogger _init_). 
        """
        
        delay = self.delay
        offset = self.filter.offset
        input_sample_rate = self.input_sample_rate
        
        if delay == None:
            if offset:
                if not input_sample_rate:
                    #Delay is already none, leave it like that
                    warnings.warn(
                        f'Stage delay is impossible to calculate \
                        out of filter offset with an Unspecified input sample rate in stage {self.name}. Setting to "None"')
                else: 
                    self.delay = offset / input_sample_rate
            else:    
                self.delay = None
                       
        else:
            self.delay = delay
               
        self.correction = self.delay if delay_correct == None else 0
    
    def get_selected_modifications(self, modif_dict, key_code):
        """
        Select which modifications apply to a given stage, with the stage number (WITHIN an instrument component) as key cide
        """
        
        default_dict = range_dict = {}
        modif = modif_dict.get(key_code, {})
        
        overlap = False
        for k, v in modif_dict.items():
            if k[0] == "*":
                default_dict = v
            elif k[0][0] == "[":             
                if re.match(k, key_code):
                    if overlap:
                        warnings.warn("There is an overlap in response stage modifications. Taking the first applicable pattern.")
                        break # Will only use first match to avoid conflicts
                    range_dict = v
                    overlap = True                  
                                    
        # Gather all modifications in a single dict
        # Do this in order: particular mods have priority over range specific which has
        # priority over default
        for k, v in range_dict.items():
            if k not in modif:    
               modif[k] = v  
           
        for k, v in default_dict.items():
            if k not in modif:    
               modif[k] = v
        
        return modif


    def __repr__(self):
        s = f'\n     Stage("{self.name}", "{self.description}", '
        s += f'"{self.input_units}", "{self.output_units}", '
        s += f'{self.gain}, {self.gain_frequency:g}, '
        s += f'{type(self.filter)}'
        if not self.stage_sequence_number == -1:
            s += f', stage_sequence_number="{self.stage_sequence_number}"'
        if self.input_units_description:
            s += f', input_units_description="{self.input_units_description}"'
        if self.output_units_description:
            s += f', output_units_description='
            s += f'"{self.output_units_description}"'
        if self.input_sample_rate:
            s += f', input_sample_rate={self.input_sample_rate}'
        
        s += f', decimation_factor={self.decimation_factor}'
        s += f', delay={self.delay}'
        s += f', correction={self.correction}'
        
        if self.calibration_date:
            s += f', calibration_dates={self.calibration_date}'
        s += ')'
        return s

    def to_obspy(self):
        """
        Return equivalent obspy response stage
        Don't change parameter assignment in called meethods, as they are used so
        parameter order is irrelevant- Very handy
        """

        filt = self.filter
        args = (self.stage_sequence_number, self.gain, self.gain_frequency,
                self.input_units, self.output_units) # Invariable position arguments for all
        
        if (isinstance(filt, PolesZeros) 
                or isinstance(filt, Analog)):
            if not filt.normalization_frequency:
                filt.normalization_frequency = self.gain_frequency
                
            if filt.type == "PolesZeros": #Only iterate if zeros and poles exist
                PZ_zeros=[obspy_types.ComplexWithUncertainties(
                    t, lower_uncertainty=0.0, upper_uncertainty=0.0)\
                    for t in filt.zeros]
                PZ_poles=[obspy_types.ComplexWithUncertainties(
                    t, lower_uncertainty=0.0, upper_uncertainty=0.0)\
                    for t in filt.poles]
            else:
                PZ_zeros = filt.zeros
                PZ_poles = filt.poles
                
            obspy_stage = PolesZerosResponseStage(
                *args,
                name=self.name,
                input_units_description=self.input_units_description,
                output_units_description=self.output_units_description,
                description=self.description,
                decimation_input_sample_rate=self.input_sample_rate,
                decimation_factor=self.decimation_factor,
                decimation_offset=filt.offset,
                decimation_delay=self.delay,
                decimation_correction=self.correction,                #OJO: check if correction and delay should be modified
                resource_id="",
                # PolesZeros-specific
                pz_transfer_function_type=filt.transfer_function_type,
                normalization_frequency=filt.normalization_frequency,
                zeros=PZ_zeros,
                poles=PZ_poles,
                normalization_factor=filt.normalization_factor
                )
            
        elif isinstance(filt, FIR):
            
            obspy_stage = FIRResponseStage(
                *args,
                name=self.name,
                input_units_description=self.input_units_description,
                output_units_description=self.output_units_description,
                description=self.description,
                decimation_input_sample_rate=self.input_sample_rate,
                decimation_factor=self.decimation_factor,
                decimation_offset=filt.offset,
                decimation_delay=self.delay,
                decimation_correction=self.correction,
                resource_id="",                
                # FIR-specific
                symmetry=filt.symmetry,
                coefficients=[obspy_types.FloatWithUncertaintiesAndUnit(
                    c / filt.coefficient_divisor) for c in filt.coefficients])
        
        elif (isinstance(filt, Coefficients)
                or isinstance(filt, Digital)
                or isinstance(filt, AD_Conversion)):                
            
            if filt.type == "Coefficients": #Only iterate if zeros and poles exist
                c_numerator=[obspy_types.FloatWithUncertaintiesAndUnit(
                    n, lower_uncertainty=0.0, upper_uncertainty=0.0)\
                    for n in filt.numerator_coefficients]
                c_denominator=[obspy_types.FloatWithUncertaintiesAndUnit(
                    n, lower_uncertainty=0.0, upper_uncertainty=0.0)\
                    for n in filt.denominator_coefficients]
            else:
                c_numerator=filt.numerator_coefficients
                c_denominator=filt.denominator_coefficients
                           
            obspy_stage = CoefficientsTypeResponseStage(
                *args,
                name=self.name,
                input_units_description=self.input_units_description,
                output_units_description=self.output_units_description,
                description=self.description,
                decimation_input_sample_rate=self.input_sample_rate,
                decimation_factor=self.decimation_factor,
                decimation_offset=filt.offset,
                decimation_delay=self.delay,
                decimation_correction=self.correction,
                resource_id="",
                # CF-specific
                cf_transfer_function_type=filt.transfer_function_type,
                numerator=c_numerator,
                denominator=c_denominator
                )

        elif isinstance(filt, ResponseList):
            
            obspy_stage = ResponseListResponseStage(
                *args,
                name=self.name,
                input_units_description=self.input_units_description,
                output_units_description=self.output_units_description,
                description=self.description,
                decimation_input_sample_rate=self.input_sample_rate,
                decimation_factor=self.decimation_factor,
                decimation_offset=filt.offset,
                decimation_delay=self.delay,
                decimation_correction=self.correction,
                resource_id="",
                # ResponeList-specific
                response_list_elements=filt.response_list)
            
        else:
            raise TypeError(f'Unhandled response stage type in stage #{self.stage_sequence_number}: "{filt.type}"')
        
        return obspy_stage
