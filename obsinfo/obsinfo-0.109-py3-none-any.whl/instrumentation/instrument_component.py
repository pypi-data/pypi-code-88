"""
InstrumentComponent class and subclasses.

No StationXML equivalent.
"""
# Standard library modules
# import math as m
import warnings
import re
# Non-standard modules
from obspy.core.inventory.util import Equipment as obspy_Equipment
import obspy.core.util.obspy_types as obspy_types
from obspy.core.utcdatetime import UTCDateTime

from .response_stages import ResponseStages

from ..obsMetadata.obsmetadata import (ObsMetadata)

class InstrumentComponent(object):
    """
    InstrumentComponent superclass.  No obspy equivalent
    """
    def __init__(self, equipment, response_stages=[],
                 config_description=''):
        """
        Constructor
        """
        self.equipment = equipment
        self.config_description = config_description
             
        if not response_stages or not response_stages.stages:
            raise TypeError(f'No response stages in {type(self)}')
            
        self.response_stages = response_stages
        
        self.obspy_equipment = self.equipment.to_obspy() 
        
    def retrieve_configuration(comp_type, attributes_dict, configuration_selection=None):
        """
        Completes the component configuration.
        A configuration selector can be defined in the instrumentation class, otherwise a config default is used
        They may be used to select a configuration in the list of configuration definitions
        If a configuration matches the selector configuration its attributes will override or
        add to existing attributes.          
        """
        
        if not attributes_dict:
            return None
        
        configuration_default = attributes_dict.get('configuration_default', None)
        # If there is a selected configuration at the instrumentation level) use it, else use default
        # configuration at component level
        # If no default configuration selected_configuration will be None
        selected_configuration_key = configuration_selection \
                                    if configuration_selection else configuration_default

        if not selected_configuration_key:
            warnings.warn(f'No configuration key or default found in {comp_type}. \
            Configurations, if present, will not be applied')
            return {}
        
        all_configurations = attributes_dict.get('configuration_definitions', None)
        if not all_configurations:
            return {}
        
        selected_configuration = all_configurations.get(selected_configuration_key, {})
        
        if selected_configuration == {}:
            warnings.warn(f'Configuration selected "{selected_configuration_key}" \
             in {comp_type} not found in configuration definitions, using default configuration')
         
        return selected_configuration
            
    @staticmethod
    def dynamic_class_constructor(component_type, 
                                  attributes_dict, 
                                  channel_modif={},
                                  delay_correction=None, 
                                  config_selector=''):
        """
        Creates an appropriate Instrument_component subclass from an attributes_dict
        """
        if not attributes_dict.get(component_type, None):
            if component_type == 'preamplifier': #Only preamps are optional
               return None
            else:
                raise TypeError(f'No {component_type}')     
    
        selected_config = InstrumentComponent.retrieve_configuration(component_type, attributes_dict[component_type], 
                                                                     config_selector)
        
        if component_type == 'datalogger':
            obj = Datalogger.dynamic_class_constructor(ObsMetadata(attributes_dict['datalogger']), 
                                                       channel_modif.get('datalogger', {}),
                                                       selected_config, 
                                                       delay_correction)
        elif component_type == 'sensor':
            obj = Sensor.dynamic_class_constructor(ObsMetadata(attributes_dict['sensor']), 
                                                   channel_modif.get('sensor', {}),
                                                   selected_config, 
                                                   delay_correction) 
        elif component_type == 'preamplifier':
            obj = Preamplifier.dynamic_class_constructor(ObsMetadata(attributes_dict['preamplifier']), 
                                                         channel_modif.get('preamplifier', {}),
                                                         selected_config, 
                                                         delay_correction)  
        else:
            raise TypeError('Unknown InstrumentComponent ')
        
        if not obj.config_description:
            obj.config_description = config_selector if config_selector else ''
            
        obj.equipment.description += ('[config: ' + obj.config_description + ']') 
        
        return obj
    
    def __repr__(self):
        
        s = ''
        if self.equipment.description:
            s += f', description="{self.equipment.description}"'
            
        return s


class Datalogger(InstrumentComponent):
    """
    Datalogger Instrument Component. No obspy equivalent
    """
    def __init__(self, equipment, sample_rate, delay_correction=None, response_stages=[],
                 config_description=''):
        
        self.sample_rate = sample_rate
        self.delay_correction = delay_correction
                   
        super().__init__(equipment, response_stages, config_description)

    @classmethod
    def dynamic_class_constructor(cls, attributes_dict, channel_modif={}, selected_config={}, delay_correction=None):
        """
        Create Datalogger instance from an attributes_dict
        """
        if not attributes_dict:
            return None
        if not selected_config:
            selected_config = {} #A syntax error in the yaml file, two consecutive labels with no response stages, is avoided here
        
        # response_stages = reconfigure_component('response_stages', attributes_dict, selected_config, None)
        sample_rate = attributes_dict.get_configured_element('sample_rate', channel_modif, selected_config, None)
        delay_correction = attributes_dict.get_configured_element('delay_correction', channel_modif, selected_config, None)
        config_description = attributes_dict.get_configured_element('configuration_description', channel_modif, selected_config, '')
               
        #What the next line of code will do is to totally override response states in attribute_dict IF there is a selected_config with response_stages
        response_stages_list = attributes_dict.get_configured_element('response_stages', 
                                                                {}, 
                                                                selected_config,
                                                                 None)
        
        response_stages = ResponseStages(response_stages_list,
                                 channel_modif.get('response_modifications', {}), 
                                 selected_config.get('response_modifications', {}), 
                                 delay_correction)
                                  
        obj = cls(Equipment(ObsMetadata(attributes_dict.get('equipment', None)), channel_modif.get('equipment', {}), selected_config.get('equipment', {})),
                  sample_rate,
                  delay_correction,
                  response_stages,
                  config_description)
        
        
        return obj

    def __repr__(self):
        s = f'Datalogger(Sample Rate={self.sample_rate})'
        s += super().__repr__()
        
        return s


class Sensor(InstrumentComponent):
    """
    Sensor Instrument Component. No obspy equivalent
    """
    def __init__(self, equipment, seed_band_base_code, seed_instrument_code,
                 response_stages=[],
                 config_description=''):
        """
        Constructor

        :param equipment: Equipment information
        :type equipment: ~class `obsinfo.instrumnetation.Equipment`
        :param seed_band_base_code: SEED base code ("B" or "S") indicating
                                    instrument band.  Must be modified by
                                    obsinfo to correspond to output sample
                                    rate
        :type seed_band_base_code: str (len 1)
        :param seed_instrument code: SEED instrument code
        :type seed_instrument_code: str (len 1)
        :param seed_orientations: SEED orientation codes and corresponding
                                      azimuths and dips
        :type seed_orientations: dict

        """
       
        self.seed_band_base_code = seed_band_base_code
        self.seed_instrument_code = seed_instrument_code# dictionary
        
        super().__init__(equipment, response_stages, config_description)


    @classmethod
    def dynamic_class_constructor(cls, attributes_dict, channel_modif={}, selected_config={}, delay_correction=None):
        """
        Create Sensor instance from an attributes_dict
        """
        if not attributes_dict:
            return None
        if not selected_config:
            selected_config = {} #A syntax error in the yaml file, two consecutive labels with no response stages, is avoided here
        
        seed_dict = ObsMetadata(attributes_dict).get_configured_element('seed_codes', 
                                                                  channel_modif, 
                                                                  selected_config, {})
        
        #What the next line of code will do is to totally override response states in attribute_dict IF there is a selected_config with response_stages
        response_stages_list = attributes_dict.get_configured_element('response_stages', 
                                                                {}, 
                                                                selected_config,
                                                                 None)
        
        response_stages = ResponseStages(response_stages_list,
                                 channel_modif.get('response_modifications', {}), 
                                 selected_config.get('response_modifications', {}), 
                                 delay_correction)
                        
        obj = cls(Equipment(ObsMetadata(attributes_dict.get('equipment', None)), 
                            channel_modif.get('equipment', {}), 
                            selected_config.get('equipment', {})),
                            ObsMetadata(seed_dict).get_configured_element('band_base', 
                                                                          channel_modif, 
                                                                          selected_config, 
                                                                          None),
                            ObsMetadata(seed_dict).get_configured_element('instrument', 
                                                                          channel_modif, 
                                                                          selected_config,
                                                                          None),
                            response_stages,
                            attributes_dict.get_configured_element('configuration_description', 
                                                                   channel_modif, 
                                                                   selected_config, '')
                    )

        return obj

    def __repr__(self):
        
        s = ''
        if self.response_stages:
            s += f'{self.response_stages}'
    
        s += f'\nSensor( "band code={self.seed_band_base_code}", "instrument code={self.seed_instrument_code}")'
        
        s += super().__repr__()
        
        return s


class Preamplifier(InstrumentComponent):
    """
    Preamplifier Instrument Component. No obspy equivalent
    """
    
    def __init__(self, equipment,  response_stages=[],
                 config_description=''):
        """
        Constructor

        :param equipment: Equipment information
        :type equipment: ~class `obsinfo.instrumnetation.Equipment`

        """
        
        super().__init__(equipment, response_stages, config_description)

    @classmethod    
    def dynamic_class_constructor(cls, attributes_dict, channel_modif={}, selected_config={}, delay_correction=None):
        """
        Create Preamplifier instance from an attributes_dict
        """
        if not attributes_dict:
            return None
        if not selected_config:
            selected_config = {} #A syntax error in the yaml file, two consecutive labels with no response stages, is avoided here
                
        #What the next line of code will do is to totally override response states in attribute_dict IF there is a selected_config with response_stages
        response_stages_list = attributes_dict.get_configured_element('response_stages', 
                                                                {}, 
                                                                selected_config, 
                                                                None)
        
        response_stages = ResponseStages(response_stages_list,
                                 channel_modif.get('response_modifications', {}), 
                                 selected_config.get('response_modifications', {}), 
                                 delay_correction)    
               
        obj = cls(Equipment(ObsMetadata(attributes_dict.get('equipment', None)), 
                            channel_modif.get('equipment', {}), 
                            selected_config.get('equipment', {})),
                            response_stages,
                            attributes_dict.get_configured_element('configuration_description', 
                                                                   channel_modif, 
                                                                   selected_config, 
                                                                   '')
                  )
        
        return obj
        
        
    def __repr__(self):
        s = f'Preamplifier()'
        s += super().__repr__()
        
        return s


class Equipment(obspy_Equipment):
    """
    Equipment class.

    Equivalent to obspy.core.inventory.util.Equipment
    """
    def __init__(self, attributes_dict, channel_modif={}, selected_config={}):
    
        self.type = attributes_dict.get_configured_element('type', 
                                                     channel_modif, 
                                                     selected_config, 
                                                     None)
        self.description = attributes_dict.get_configured_element('description', 
                                                            channel_modif, 
                                                            selected_config,
                                                             None)
        self.manufacturer = attributes_dict.get_configured_element('manufacturer', 
                                                             channel_modif, 
                                                             selected_config,
                                                              None)
        self.model = attributes_dict.get_configured_element('model', 
                                                      channel_modif, 
                                                      selected_config, 
                                                      None)
        self.vendor = attributes_dict.get_configured_element('vendor', 
                                                       channel_modif, 
                                                       selected_config, 
                                                       None)
        self.serial_number = attributes_dict.get_configured_element('serial_number', 
                                                              channel_modif, 
                                                              selected_config,
                                                              None)
        self.installation_date = ObsMetadata.validate_date(attributes_dict.get_configured_element('installation_date', 
                                                                  channel_modif, 
                                                                  selected_config,
                                                                  None)) 
        self.removal_date = ObsMetadata.validate_date(attributes_dict.get_configured_element('removal_date', 
                                                             channel_modif, 
                                                             selected_config, 
                                                             None))
        calibration_dates = ObsMetadata.validate_dates(attributes_dict.get_configured_element('calibration_dates', 
                                                                  channel_modif, 
                                                                  selected_config, 
                                                                  [])) 
        
        self.calibration_dates = calibration_dates
        self.resource_id = None
        
        equip = self.to_obspy()
        self.obspy_equipment = equip[0] if isinstance(equip, tuple) else equip
            
    
    def __repr__(self):
        s = f'Equipment('
        if self.type:
            s += f', Type={self.type}'
        if self.description:    
            s += f', Description={self.description}'
        if self.manufacturer:
            s += f', Manufacturer={self.manufacturer}'
        if self.model:
            s += f', Model={self.model}'
        if self.vendor:
            s += f', Vendor={self.vendor}'
        if self.serial_number:
            s += f', Serial Number={self.serial_number}'
        if self.installation_date:
            s += f', Installation Date={self.installation_date}'
        if self.removal_date:
            s += f', Removal Date={self.removal_date}'
        if self.calibration_dates:
            s += f', Calibration Date={self.calibration_dates}'
        s += ')'
        
        return s
    
    def to_obspy(self):
        """
        Convert an equipment (including the equipment description in components) to its obspy object
        """
        
        resource_id = None
        
        installation_date = UTCDateTime(self.installation_date if self.installation_date else 0)
        removal_date = UTCDateTime(self.removal_date if self.removal_date else 0)
        
        if isinstance(self.calibration_dates, list) and len(self.calibration_dates) > 0:
            calibration_dates = [UTCDateTime(dt) for dt in self.calibration_dates]
        else:
            calibration_dates = []
        #else:
        #    last_calibration_date = UTCDateTime(0) #Use last calibration date
        
        equip = obspy_Equipment(self.type, self.description, self.manufacturer, self.vendor,
                self.model, self.serial_number, installation_date, removal_date, 
                calibration_dates, resource_id)
        
        return equip        
         

    
