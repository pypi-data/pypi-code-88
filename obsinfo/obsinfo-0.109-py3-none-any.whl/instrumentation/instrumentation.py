"""
Instrumentation and Instrument classes

nomenclature:
    An "Instrument" (measurement instrument) records one physical parameter
    A "Channel" is an Instrument + an orientation code and possibly
        starttime, endtime and location code
    An "Instrumentation" combines one or more measurement Channels
"""
# Standard library modules
import warnings
import numpy

# Non-standard modules
from obspy.core.utcdatetime import UTCDateTime
import obspy.core.util.obspy_types as obspy_types
from obspy.core.inventory.response import (Response)
from obspy.core.inventory.response import InstrumentSensitivity\
                                   as obspy_Sensitivity
from obspy.core.inventory.channel import Channel\
                                   as obspy_Channel
from obspy.core.inventory.util import  (Latitude, Longitude, Comment)
# obsinfo modules
from .instrument_component import (InstrumentComponent, Datalogger, Sensor, Preamplifier,
                                   Equipment)
from .response_stages import (ResponseStages)
from ..obsMetadata.obsmetadata import (ObsMetadata)
import obspy.geodetics.base
from obspy.geodetics.base import kilometers2degrees
from numpy import cos

class Instrumentation(object):
    """
    One or more Instruments. Part of an obspy/StationXML Station
    """
    def __init__(self, attributes_dict_or_list, locations, start_date, end_date, channel_modifications={}):
        """
        Constructor
        attributes_dict may contain a configuration_selection for the instrumentation and the corresponding configs  
        for the components: datalogger, preamplifier and sensor

        :param equipment: equipment description
        :type equipment: ~class `Equipment`
        :param channels: list of channels
        :type channels: list of ~class `Channel`
        """
        
        #Syntax checking - Check whether 
        if not attributes_dict_or_list:
            raise TypeError('No instrumentation attributes')
        elif isinstance(attributes_dict_or_list, list): #It's an easy mistake to include a dash in the yaml file
            warnings.warn(f'Instrumentation should be unique, not a list. Removing list embedding.')
            if len(attributes_dict_or_list) > 0:
                attributes_dict = attributes_dict_or_list[0]
            else:
                raise TypeError('No instrumentation attributes')
        else:
            attributes_dict = attributes_dict_or_list
        
        self.operator = Operator(attributes_dict.get('operator', None))   
        self.equipment = Equipment(ObsMetadata(attributes_dict.get('equipment', None)),
                                               {}, #Equipment is not changeable either
                                               {}
                                               )
        self.equipment.obspy_equipment = self.equipment.to_obspy()
        
        das_channels = attributes_dict.get('channels', {})
        channel_default = das_channels.get('default', {})
        if channel_default:
            del das_channels['default']
        
        #v here is the attributes_dict of each das_channel
        self.channels = [Channel(k, v, locations, start_date, end_date, channel_default, channel_modifications)
                   for k, v in das_channels.items()]
        
    def __repr__(self):
        s = f'\n\nInstrumentation({len(self.channels)-1} channels)'
        return s


class Channel(object):
    """
    Channel Class.

    Corresponds to StationXML/obspy Channel, plus das_channel code
    """
    def __init__(self, channel_label, attributes_dict, locations, start_date, end_date, 
                 channel_template={}, channel_mods_dict={}):
        """
        :param instrument: instrument description
        :type instrument: ~class `Instrument`
        :param das_channel: the DAS channel the instrument is on
        :type das_channel: str
        :param orientation_code: orientation code of this channel/instrument
        :type orientation_code: str
        :param location_code: channel location code (if different from network)
        :type location_code: str, opt
        :param startdate: channel startdate (if different from network)
        :type startdate: str, opt
        :param enddate: channel enddate (if different from network)
        :type enddate: str, opt
        """
        if channel_label == "default":
            return
        
        if not attributes_dict:
            raise TypeError('No channel attributes')
        
        #Complete das channel fields with default fields. This will create a complete channel
        self.das_channel = ObsMetadata(self.complete_channel(attributes_dict, channel_template))
        
        #Location and orientation code should not be changed, so no channel modifications
        self.location_code = self.das_channel.get('location_code', "00") # default is always 00
        
        # This is just the one-letter string code, Although the attribute is redundant, it si needede before 
        # calling class Orientation init at the bottomo of this method
        self.orientation_code = self.get_orientation_code(attributes_dict.get('orientation_code', None))
   
        self.location = Location.get_location_from_code(locations, self.location_code, "channel",
                                                        self.channel_id_code)
                                                                             
        self.start_date = start_date
        self.end_date = end_date  
        
        selected_channel_mods = self.get_selected_channel_modifications(self.channel_id_code, channel_mods_dict)
        
        self.instrument = Instrument(self.das_channel, selected_channel_mods) 
        
        # this is the complete dictionary under key orientation code. If present, azimuth and dip can be changed in channel modifications
        orientation_dict = self.das_channel.get('orientation_code', None)
        if isinstance(orientation_dict, str):
            orientation_dict = {orientation_dict: {}} #If just a string, convert to dict to simplify code
            
        orientation_dict = ObsMetadata(orientation_dict)
        #Channel polarity is defined only while creating Instrument object. Don't change order of assignments      
        self.orientation = Orientation(orientation_dict, selected_channel_mods, self.instrument.polarity)
        
        self.comments = attributes_dict.get("comments", [])
        self.extras = [str(k) + ": " + str(v) for k, v in (attributes_dict.get('extras', {})).items()]
        self.convert_notes_and_extras_to_obspy()
        
        self.obspy_channel = self.to_obspy()
        
        
    @property
    def channel_id_code(self):
        """
        Identify channel uniquely through a combination of orientation and location code
        in that order, separated by a dash
        """
        
        if not self.orientation_code:
            raise TypeError(f'No orientation code in channel')

        # If no location, use 00 as defaul
        return self.orientation_code + "_" + (self.location_code if self.location_code else "00")
    
    def get_orientation_code(self, orientation_dict):
        """
        Get the orientation code from a dict that may include azimuth and dip
        """
        if isinstance(orientation_dict, str):
            keys = orientation_dict
        else:
            keys = list(orientation_dict.keys())
        #There should be only one key
        return keys[0]
        
    
    def get_selected_channel_modifications(self, id_code, channel_mods_dict):
        """
        Select one among several possible channel_modifications
        """

        # Get general default
        default_channel_mod = channel_mods_dict.get("*", {})
        if not default_channel_mod:
            default_channel_mod = channel_mods_dict.get("*-*", {})
        # Get defaults by location and orientation
        default_channel_loc = channel_mods_dict.get(self.orientation_code + "-*", {})
        default_channel_orient = channel_mods_dict.get("*-" + self.location_code, {})
        
        # Get modifications for this particular channel
        chmod = channel_mods_dict.get(id_code, {})
        if not chmod:
            # If id code not found, try with just the orientation part
            chmod = channel_mods_dict.get(id_code[0:1], {})
            
        # Gather all modifications in a single channel_mods
        # Do this in order: particular mods have priority over orientation-specific which has
        # priority over location-specific which has priority over general default
        for k, v in default_channel_loc.items():
            if k not in chmod:    
               chmod[k] = v
        for k, v in default_channel_orient.items():
            if k not in chmod:    
               chmod[k] = v    
        for k, v in default_channel_mod.items():
            if k not in chmod:    
               chmod[k] = v  
        
        return chmod      
           
    def complete_channel(self, das_channel, channel_default):
        """
        Take all the fields defined for each das channel and complement them with the channel_default fields
        If das_channel key exists, leave the value. If not, add channel_default key/value
        """
        #If there are no modifications, use default
        if not das_channel:
            return channel_default
        
        # First fill out allt he channel attributes 
        # Only get channel template if das_channel attribute does not exist
        for k, v in channel_default.items():
            if k not in das_channel:    
               das_channel[k] = v
        
        return das_channel
    
    def __repr__(self):
        s = f'\n\n\nChannel({self.channel_id_code}, '
        s += f'orientation code="{self.orientation.orientation_code}"'
        if self.location:
            s += f',location={self.location}'

        if self.start_date:
            s += f', startdate={self.start_date}'
 
        if self.end_date:
            s += f', enddate={self.end_date}'        
        s += ')'
        return s


    def channel_code(self, sample_rate):
        """
        Return channel code for a given sample rate

        :param sample_rate: instrumentation sampling rate (sps)i
        :kind sample_rate: float
        """
        inst_code = self.instrument.sensor.seed_instrument_code
        
        if len(inst_code) != 1:
            raise ValueError(f'Instrument code "{inst_code}" is not a single letter')
        if self.orientation.orientation_code not in ["X", "Y", "Z", "1", "2", "3", "H", "F"] :
            raise ValueError(f'Orientation code "{self.orientation_code}" is not a single letter')
        
        return (self._band_code_validation(sample_rate)
                + inst_code
                + self.orientation.orientation_code)

    def _band_code_validation(self, sample_rate):
        """
        Return the channel band code

        :param sample_rate: sample rate (sps)
        """
        bbc = self.instrument.sensor.seed_band_base_code
        if len(bbc) != 1:
            raise ValueError(f'Band base code "{bbc}" is not a single letter')
            
        if bbc in "FCHBMLVURPTQ":
            if sample_rate >= 1000:
                return "F"
            elif sample_rate >= 250:
                return "C"
            elif sample_rate >= 80:
                return "H"
            elif sample_rate >= 10:
                return "B"
            elif sample_rate > 1:
                return "M"
            elif sample_rate > 0.3:
                return "L"
            elif sample_rate > 0.03:
                return "V"
            elif sample_rate > 0.003:
                return "U"
            elif sample_rate >= 0.0001:
                return "R"
            elif sample_rate >= 0.00001:
                return "P"
            elif sample_rate >= 0.000001:
                return "T"
            else:
                return "Q"
        elif bbc in "GDES":
            if sample_rate >= 1000:
                return "G"
            elif sample_rate >= 250:
                return "D"
            elif sample_rate >= 80:
                return "E"
            elif sample_rate >= 10:
                return "S"
            else:
                warnings.warn("Short period sensor sample rate < 10 sps")
        else:
            raise TypeError(f'Unknown band base code: "{bbc}"')

    @property
    def seed_code(self):
         return self.channel_code()
     
    def to_obspy(self):
        """
         Create obspy object for channel
        """
        
        code = self.channel_code(self.instrument.sample_rate)   
        preamp = self.instrument.preamplifier.equipment.obspy_equipment if self.instrument.preamplifier else None
        comments = [Comment(s) for s in self.comments]
           
        channel = obspy_Channel(code, self.location_code, 
                        latitude=self.location.obspy_latitude, 
                        longitude=self.location.obspy_longitude,
                        elevation=self.location.elevation, 
                        depth=self.location.depth_m, 
                        azimuth=self.orientation.azimuth, 
                        dip=self.orientation.dip, 
                        types=None, 
                        external_references=None, 
                        sample_rate=self.instrument.sample_rate, 
                        sample_rate_ratio_number_samples=None, #Used for very low sample rates
                        sample_rate_ratio_number_seconds=None, 
                        storage_format=None, 
                        clock_drift_in_seconds_per_sample=None, 
                        calibration_units=None, calibration_units_description=None, 
                        sensor=self.instrument.sensor.equipment.obspy_equipment,
                        pre_amplifier=preamp, 
                        data_logger=self.instrument.datalogger.equipment.obspy_equipment, 
                        equipments=None, #This is at the instrumentation level, will be assigned there
                        response=self.instrument.obspy_response, 
                        description=self.channel_id_code, 
                        comments=comments,
                        start_date=self.start_date, #OJO: these will probably be deprecated
                        end_date=self.end_date,
                        restricted_status=None, 
                        alternate_code=None, 
                        historical_code=None, 
                        data_availability=None, 
                        identifiers=None, 
                        water_level=None, 
                        source_id=None)
         
        return channel
    
    def convert_notes_and_extras_to_obspy(self):
        """
        In StationXML comments are found at the channel level and up. Convert notes and extras to comments.
        """
        
        self.comments += self.comments + ['Extra attributes (for documentation purposes only):'] + self.extras           
        
class Instrument(Channel):
    """
    Instrument Class.
    """
    def __init__(self, attributes_dict, channel_modif={}):
        """
        :param datalogger: datalogger information
        :type datalogger: ~class `Datalogger`
        :param sensor: sensor information
        :type sensor: ~class `Sensor`
        :param preamplifier: preamplifier information
        :type preamplifier: ~class `Preamplifier`, opt
        """
        
        if not attributes_dict:
            raise TypeError('No instrument attributes')
        
        datalogger_config_selector = attributes_dict.get_configured_element(
                                                                      'datalogger_configuration', 
                                                                      channel_modif,
                                                                      {},
                                                                      None)
        sensor_config_selector = attributes_dict.get_configured_element(
                                                                  'sensor_configuration', 
                                                                  channel_modif,
                                                                  {},
                                                                  None)
        preamplifier_config_selector = attributes_dict.get_configured_element(
                                                                        'preamplifier_configuration', 
                                                                        channel_modif,
                                                                        {},
                                                                        None)
        
        self.datalogger = InstrumentComponent.dynamic_class_constructor('datalogger', 
                                              attributes_dict,
                                              channel_modif,
                                              None, #This is delay correction, calculated later
                                              datalogger_config_selector)
        delay_correction = self.datalogger.delay_correction

        #delay correction is a property of dataloggers, but needs to be used in sensors and preamplifiers
        self.sensor = InstrumentComponent.dynamic_class_constructor('sensor', 
                                              attributes_dict,
                                              channel_modif,
                                              delay_correction,
                                              sensor_config_selector)
        self.preamplifier = InstrumentComponent.dynamic_class_constructor('preamplifier', 
                                              attributes_dict,
                                              channel_modif,
                                              delay_correction,
                                              preamplifier_config_selector)
        
        # add the three component response stages
        self.add_and_renumber_all_response_stages()
        #Validate inputs and outputs of complete response sequence and correct delay    
        self.integrate_component_stages_into_single_list(delay_correction)
   
        self.obspy_response = self.to_obspy()
             
        #Finally, add sensitivity
        self.add_sensitivity(self.obspy_response)  
        
    def __repr__(self):
        return f'\nInstrument(Polarity="{self.polarity}", Output sample rate={self.total_output_sample_rate})'
    
    def integrate_component_stages_into_single_list(self, delay_correction):
        """
        1) Renumber stages sequentially 
        2) Verify/set units and sample rates
        3) Assure same frequency is used for consecutive PZ filters
        4) Calculate global polarity of the whole set of response stages
        5) Set global response delay correction
        6) Validate sample_rate expressed in datalogger component is equal to global response sample rate
        """
        
        # Stack response stages
        stages = self.response_stages
        
        last_stage = stages[0]
        last_frequency = last_stage.filter.normalization_frequency if last_stage.filter.type == 'PolesZeros' else None
        last_polarity = last_stage.polarity
        partial_accumulated_sample_rate = last_stage.output_sample_rate
        
        for this_stage in stages[1:]:
            
            """
            2a) Verify continuity of units
            """
            if last_stage.output_units != this_stage.input_units:
                raise ValueError(
                    f'Stage {stage.stage_sequence_number} and {this_stage.stage_sequence_number} units don\'t match')
            
            """
            2b) Verify continuity of sample rate. Calculate delay if necessary
            """
            if last_stage.input_sample_rate:
                if not this_stage.decimation_factor:
                    warnings.warn(f'No decimation factor for stage {this_stage.stage_sequence_number}, \
                                 assuming = 1 ')
                    this_stage.decimation_factor = 1
                    
                next_input_rate = last_stage.input_sample_rate / this_stage.decimation_factor
               
                if this_stage.input_sample_rate:
                    if this_stage.output_sample_rate != next_input_rate:
                        raise ValueError(
                            f'stage {this_stage.stage_sequence_number}  \
                            sample rate {this_stage.output_sample_rate} != expected {next_input_rate}')
                     
                else: # If no inpput sample rate specified (e.g. in FIR filters with decimation factor only), 
                      #store partial accumulated sample rate
                    this_stage.input_sample_rate = partial_accumulated_sample_rate
                    
                #Calculate delay, if absent, using real input sample rate
                this_stage.calculate_delay(delay_correction)
                    
            """
            3) Station XML requires that all PZ stages have the same normalization frequency.
            Check this condition
            """
            if last_frequency and last_frequency != 0 and this_stage.filter.type == 'PolesZeros':
                if last_frequency != this_stage.filter.normalization_frequency:
                    warnings.warn(
                        f'Normalization frequencies for PZ stages {stage.stage_sequence_number}\
                        and {this_stage.stage_sequence_number} don\'t match')
                last_frequency = this_stage.filter.normalization_frequency
                                 
            """
            4) Calculate global polarity
            """
            if not this_stage.polarity: #default polarity equals positive polarity
                this_stage.polarity = 1
                
            last_polarity *= this_stage.polarity
            
            last_stage = this_stage
            last_frequency = last_stage.filter.normalization_frequency if last_stage.filter.type == 'PolesZeros' else None
            partial_accumulated_sample_rate = last_stage.output_sample_rate     
            
        """
        5) Out of the loop: set global delay correction
        Apply global delay correction to the last stage (datalogger) if delay_correction = none
        All previous corrections in stages are zero in this case, so delay correcton is only applied once, at the end
        """
        stages[-1 ].correction = delay_correction \
            if delay_correction != None else last_stage.delay

        """
        6) Out of the loop: check global output sample rate
        """
        total_expected_sample_rate = partial_accumulated_sample_rate   

        if total_expected_sample_rate != self.sample_rate:
            warnings.warn(f'Datalogger declared sample rate {self.sample_rate} is different from calculated overall \
                sample rate of stages {total_expected_sample_rate}')
            
        """
        Set global response attributes
        """ 
        self.polarity = last_polarity 
        self.total_output_sample_rate = partial_accumulated_sample_rate
     
    def add_and_renumber_all_response_stages(self):
        
        """
        Adds all response stages as obsinfo and obpsy objects and renumbers the obsinfo ones
        """
 
        response_st = self.sensor.response_stages.stages
        obspy_st = self.sensor.response_stages.obspy_stages
        
        if self.preamplifier and self.preamplifier.response_stages:
            response_st += self.preamplifier.response_stages.stages
            obspy_st += self.preamplifier.response_stages.obspy_stages

        
        response_st += self.datalogger.response_stages.stages
        obspy_st += self.datalogger.response_stages.obspy_stages
        
        # Order the stage_sequence_numbers
        for i in range(len(response_st)):
            response_st[i].stage_sequence_number = i
           
        self.response_stages = response_st
        self.obspy_stages = obspy_st
                
    def to_obspy(self):
        """
        Return equivalent obspy response class
        """
        
        obspy_stages = self.obspy_stages
        
        obspy_response = Response(resource_id=None, 
                                  instrument_sensitivity=None, 
                                  instrument_polynomial=None, 
                                  response_stages=obspy_stages)
             
        return obspy_response
    
    
    def add_sensitivity(self, obspy_response):
        """
        Adds sensitivity to an obspy Response object

        Based on ..misc.obspy_routines.response_with_sensitivity
        """

        response_stg = self.response_stages
        true_input_units = input_units = response_stg[0].input_units
        output_units = response_stg[-1].output_units

        if "PA" in true_input_units.upper():
            # MAKE OBSPY THINK ITS M/S TO CORRECTLY CALCULATE SENSITIVITY
            input_units = "M/S"
        gain_prod = 1.
        for stage in response_stg:
            gain_prod *= stage.gain
              
        sensitivity = obspy_Sensitivity(
            gain_prod,
            response_stg[0].gain_frequency, #This could be provided according to StationXML but we assume it's equal to the gain frequency of first stage
            input_units=input_units,
            output_units=output_units, 
            input_units_description=response_stg[0].input_units_description,
            output_units_description=response_stg[-1].output_units_description
            )
        
        obspy_response.instrument_sensitivity = sensitivity
        #obspy_response.recalculate_overall_sensitivity(sensitivity.frequency)
        obspy_response.instrument_sensitivity.input_units = true_input_units
        obspy_response.instrument_sensitivity.output_units = output_units

       
    @property
    def equipment_datalogger(self):
        return self.datalogger.equipment
    @property
    def equipment_sensor(self):
        return self.sensor.equipment
    @property
    def equipment_preamplifier(self):
        return self.preamplifier.equipment
        
    def get_response_stage(self, num):    
    # All response stages are at the instrument_component level
        stages = self.response_stages
        assert(num <= stages[-1].stage_sequence_number), 'response stage out of range: {num}'
        
        return stages[num]
    
    @property
    def sample_rate(self):    
        return self.datalogger.sample_rate
    @property
    def delay_correction(self):  
        return self.delay_correction
    @property
    def seed_band_base_code(self):    
        return self.sensor.seed_band_base_code
    @property
    def seed_instrument_code(self): 
        return self.sensor.seed_instrument_code   
    @property
    def seed_orientation(self):    
        return self.orientation
    

class Location(object):
    """
    Location Class.
    """
    def __init__(self, attributes_dict):
        """
        Create Location object and assign attributes from attributes_dict.
        Validate required location attributes exist
        Convert to obspy longitude and latitude
        :param latitude: station latitude (degrees N)
        :type latitude: float
        :param longitude: station longitude (degrees E)
        :type longitude: float
        :param elevation: station elevation (meters above sea level)
        :type elevation: float
        :param uncertainties_m: uncertainties of [lat, lon, elev] in METERS
        :type uncertainties_m: list
        :param geology: site geology
        :type geology: str
        :param vault: vault type
        :type vault: str
        :param depth_m: depth of station beneath surface (meters)
        :type depth_m: float
        :param localisation_method: method used to determine position
        :type localisation_method: str
        """
        
        position = attributes_dict.get('position', None)
        base = attributes_dict.get('base', None)

        if not base:
            raise TypeError('No base in location')
        if not position:
            raise TypeError('No position in location')
                  
        self.latitude =  position.get('lat', None)
        self.longitude = position.get('lon', None)
        self.elevation = position.get('elev', None)
        self.uncertainties_m = base.get('uncertainties.m', None)
        self.geology = base.get('geology', None)
        self.vault = base.get('vault', None)
        self.depth_m = base.get('depth.m', None)
        self.localisation_method = base.get('localisation_method', None)
        self.obspy_latitude, self.obspy_longitude = self.get_obspy_latitude_and_longitude()
        
    def __repr__(self):
        discontinuous = False
        s = f'Location({self.latitude:g}, {self.longitude:g}, '
        s += f'{self.elevation:g}, {self.uncertainties_m}'
        if not self.geology == 'unknown':
            s += f', "{self.geology}"'
        else:
            discontinuous = True
        if self.vault:
            if discontinuous:
                s += f', vault="{self.vault}"'
            else:
                s += f', "{self.vault}"'
        else:
            discontinuous = True
        if self.depth_m:
            if discontinuous:
                s += f', depth_m={self.depth_m:g}'
            else:
                s += f', {self.depth_m}'
        else:
            discontinuous = True
        if self.localisation_method:
            if discontinuous:
                s += f', localisation_method="{self.localisation_method}"'
            else:
                s += f', "{self.localisation_method}"'
        else:
            discontinuous = True
        s += ')'
        return s
    
    @staticmethod
    def get_location_from_code(locations, code, type, label):
        """
         Obtain from the locations dictionary one location by code (key). Raise exception if not found
        """
        
        if not locations:
            raise TypeError(f'No locations specified in station {label}')
        
        loc = locations.get(code, None)

        if not loc:
            if type == 'station': #For station the location code is mandatory
                raise TypeError(f'Location "{code}" not found in station {label}')
            else:
                warnings.warn(f'Channel {label} has no location code. Assuming location code "00"')
                loc = locations.get("00", None)
                if not loc:
                    raise TypeError(f'Location "{code}" not found in channel {label}') 
                                
        return loc
        
    
    def get_obspy_latitude_and_longitude(self, location=None):
        """
        Returns obspy (latitude, longiutde) as a tupe.
        """
    
        if not location:
            location = self
            
        #Convert meters to kilometers and then to degrees.
        #This is along a meridian, so it's a great circle, Assumes 40000 km Earth diameter    
        uncertainty_lat = kilometers2degrees(
                           location.uncertainties_m.get('lat', 0) / 1000 if location.uncertainties_m else 0 )
        latitude = Latitude(value=location.latitude, 
                            lower_uncertainty=uncertainty_lat,
                            upper_uncertainty=uncertainty_lat,
                            datum=None
                            )
        
        intermediate_uncert_lon = location.uncertainties_m.get('lon', 0) / 1000 if location.uncertainties_m  else 0
        #lon is along parallel, not a great circle, so we must reduce by cosine.. Using numpy
        #Won't work for poles, make uncertainty zero in that case
        uncertainty_lon = kilometers2degrees(intermediate_uncert_lon * numpy.cos(latitude)) if latitude != 90 else 0
                           
        longitude = Longitude(value=self.longitude, 
                              lower_uncertainty=uncertainty_lon,
                              upper_uncertainty=uncertainty_lon,
                              datum=None
                              )
        return (latitude, longitude)

   
class Operator(Channel):
    """  
    Operator Class.
    """
   
    def __init__(self, attributes_dict):
        """
        :param attributes_dict: datalogger information
        :type attributes_dict: ~class `Datalogger`
        """
       
        if not attributes_dict:
            return None 
        
        self.reference_name = attributes_dict.get('reference_name', None)
        self.full_name = attributes_dict.get('full_name', None)
        contact_name = attributes_dict.get('contact', None)
        
        if contact_name:
           self.contact = contact_name.get('first_name', '') \
                          + " " + contact_name.get('last_name', '')
        
        self.email = attributes_dict.get('email', None)
        self.phone_number = attributes_dict.get('phone_number', None)
        self.website = attributes_dict.get('website', None)
        
    def __repr__(self):
        s = f'\nOperator(Reference Name={self.reference_name}, Full Name = {self.full_name}, '
        if self.contact_name:
            s += f'Contact Name={self.contact_name.first_name} {self.contact_name.last_name}, '
        s += f'Email={self.email}, phone_number={self.phone_number}, website={self.website})'
        
        return s
        
class Orientation(object):
    """
    Class for sensor orientations. No channel modifs. Cannot change orientation as it is part of the channel identifiers. Azimuth and dip can be changed
    """
    def __init__(self, attributes_dict, channel_modifs, polarity):
        """
        Constructor
        Seismometer: 90º dip is down, positive voltage. Negative voltage  inverts to -90º (up)
        Hydrophone:  90º dip is down, positive pressure. Negative pressure  inverts to -90º (up)
        Seismometer vertical voltage positive = mouvement vers le haut
        Hydrophone voltage positive = augmentation de pression
        :param azimuth: azimuth (clockwise from north, degrees)
        :param azimuth_uncertainty: degrees
        :param dip: dip (degrees, -90 to 90: positive=down, negative=up)
        :param dip_uncertainty: degrees
        """
        if not attributes_dict:
            raise ValueError('No orientation')
        
        #if a dictionary attributes_dict contains azimuth and/of dip info else it's a simple string and is included in a list for generality
        keys = list(attributes_dict.keys() if isinstance(attributes_dict, dict) else attributes_dict) 
        if "1" in keys:
            self.orientation_code = "1" 
            value = ObsMetadata(attributes_dict.get("1", None))
            if not value:
                raise ValueError('Type "1" channel has no azimuth')  
            azimuth, azimuth_uncertainty = self.get_value_with_uncertainty(
                                               value.get_configured_element(
                                                   'azimuth.deg', 
                                                   channel_modifs,
                                                   {}, 
                                                   None))
            if azimuth == None:
                raise ValueError('Type "1" channel has no azimuth')
            dip, dip_uncertainty = [0, 0]
            
        elif "2" in keys:
            self.orientation_code = "2"  
            value = ObsMetadata(attributes_dict.get("2", None))
            if not value:
                raise ValueError('Type "2" channel has no azimuth')  
            azimuth, azimuth_uncertainty = self.get_value_with_uncertainty(
                                               value.get_configured_element(
                                                   'azimuth.deg', 
                                                   channel_modifs,
                                                   {}, 
                                                   None))
            if azimuth == None:
                raise ValueError('Type "2" channel has no azimuth')
            dip, dip_uncertainty = [0, 0] 
                                                            
        elif "3" in keys:
            self.orientation_code = "3"  
            value = ObsMetadata(attributes_dict.get("3", None))
            if not value:
                raise ValueError('Type "3" channel has no dip')  
            azimuth, azimuth_uncertainty = [0, 0]
            dip, dip_uncertainty = self.get_value_with_uncertainty(
                                        value.get_configured_element(
                                                 'dip.deg', 
                                                 channel_modifs,
                                                 {}, 
                                                 None))
            if dip == None:
                raise ValueError('Type "3" channel has no dip')
            
        elif "H" in keys:
            self.orientation_code = "H"  
            azimuth, azimuth_uncertainty = [0, 0]
            dip, dip_uncertainty = [90 * polarity, 0]
            
        elif "X" in keys:
            self.orientation_code = "X"  
            azimuth, azimuth_uncertainty = [0, 5] #Uncertainty defined by FDSN
            dip, dip_uncertainty = [0.0]
            
        elif "Y" in keys:
            self.orientation_code = "Y"  
            azimuth, azimuth_uncertainty = [90, 5] #Uncertainty defined by FDSN
            dip, dip_uncertainty = [0.0]
        
        elif "Z" in keys:
            self.orientation_code = "Z"  
            azimuth, azimuth_uncertainty = [0, 0] #Uncertainty defined by FDSN
            dip, dip_uncertainty = [90 * polarity, 5]
            
        else:
            raise ValueError('Type(s) "{keys}" orientation subcode(s) not implemented')
        
        self.azimuth = obspy_types.FloatWithUncertaintiesAndUnit(
            azimuth, lower_uncertainty=azimuth_uncertainty,
            upper_uncertainty=azimuth_uncertainty, unit='degrees')
        self.dip = obspy_types.FloatWithUncertaintiesAndUnit(
            dip, lower_uncertainty=dip_uncertainty,
            upper_uncertainty=dip_uncertainty, unit='degrees')
        
    
    def __repr__(self):
        s = f'\nOrientation('
        if self.azimuth:
            s += f', Azimuth={self.azimuth}'
        if self.dip:    
            s += f', Dip={self.dip}'
        
        return s

        
    def get_value_with_uncertainty(self, info_list):
        """
        Validate that info_list is a 2 member list, return the two members as a list, otherwise  [None, None]
        """
        
        if not info_list or not isinstance(info_list, list) or len(info_list) != 2:
            return [None, None]
        
        return [info_list[0], info_list[1]]
        