"""
Station class
"""
# Standard library modules
import warnings
# Non-standard modules
from obspy.core.inventory.station import Station as obspy_Station

import obspy.core.util.obspy_types as obspy_types
from obspy.core.inventory.util import  (Latitude, Longitude, Site, Comment)
from obspy.core.utcdatetime import UTCDateTime
from obspy.taup.seismic_phase import self_tokenizer
# obsinfo modules
from ..instrumentation.instrumentation import (Instrumentation, Location)
from ..obsMetadata.obsmetadata import (ObsMetadata)

class Station(object):
    """
    Station. Equivalent to obspy/StationXML Station
    """
    def __init__(self, label, attributes_dict):
        """
        Constructor

        :param site: site description
        :kind site: str
        :param start_date: station start date
        :kind start_date: str
        :param end_date: station start date
        :kind end_date: str
        :param location_code: station location code (2 digits)
        :kind location_code: str
        :param locations: locations (names and positions)
        :kind locations: ~class `obsinfo.network.Locations`
        :param instruments: list of Instrumentation
        :kind instruments: list
        :param processing: processing steps
        :kind processing: dict (maybe should have class?)
        :param restricted_status: "open", "closed", "partial", or "unknown"
        :kind restricted_status: str
        """
         
        if not attributes_dict:
            raise TypeError('No station attributes')
        
        self.label = label
        
        self.site = attributes_dict.get("site", None)
        
        start_date = ObsMetadata.validate_date(attributes_dict.get("start_date", 0))
        self.start_date = UTCDateTime(start_date)
        
        end_date = ObsMetadata.validate_date(attributes_dict.get("end_date", 0))
        self.end_date = UTCDateTime(end_date)
        
        self.location_code = attributes_dict.get("location_code", None)
        
        self.restricted_status = attributes_dict.get("restricted_status", 'unknown')
        
        self.locations = {c: Location(v) for c, v in \
                          attributes_dict.get('locations', None).items()}
        self.location = Location.get_location_from_code(self.locations, self.location_code, "station", self.label)
      
        instr_list = attributes_dict.get('instrumentations', None)
        if instr_list and isinstance(instr_list, list):
            channel_mods = attributes_dict.get('channel_modifications', {})     
            self.instrumentation = [Instrumentation(inst, self.locations, start_date, end_date, channel_mods) 
                                    for inst in instr_list]
        else:
            instr_dict = attributes_dict.get('instrumentation', None)
            channel_mods = attributes_dict.get('channel_modifications', {})

            if instr_dict:
                self.instrumentation = Instrumentation(instr_dict, self.locations, start_date, end_date, channel_mods) 
            else:
                raise ValueError(f'No instrumentation in station {self.site}')
        #Locations, start_date and end_date are used to creat obspy Channel
              
        self.processing = attributes_dict.get("processing", None)
        
        self.comments = attributes_dict.get("commnents", [])
        self.extras = [str(k) + ": " + str(v) for k, v in (attributes_dict.get('extras', {})).items()]
        self.convert_notes_and_extras_to_obspy() 
        
        self.obspy_station = self.to_obspy()
        
        """
        Processing.from_attributes_dict(attributes_dict.get('processing',
                                                          None)),
        """

    def __repr__(self):
        s = f'\nStation(Label={self.label}, Site={self.site}, Start Date={self.start_date}, End Date={self.end_date}, '
        s += f'Location Code={self.location_code}, '
        s += f'{len(self.locations)} Locations, '
        if self.processing:
            s += f'{len(self.processing)} processing-steps'
        #if not self.restricted_stations == "unknown":
        #    s += f', {self.restricted_status}'
        s += ')'
        return s

    def to_obspy(self):
        """
         Convert station to obspy object
        """
        """
        Don't know what to do with 
         
        self.location.depth_m 
        self.location.localisation_method
        self.processing 
        """
            

        channels_number = len(self.instrumentation.channels)
        latitude, longitude = Location.get_obspy_latitude_and_longitude(self.location) 
        
        start_date = UTCDateTime(self.start_date if self.start_date else 0)
        end_date = UTCDateTime(self.end_date if self.end_date else 0)
        site = Site(name=self.site, description=None, town=None, county=None, region=None, country=None)
        comments = [Comment(s) for s in self.comments]
        
        obspy_station = obspy_Station( code = self.label, 
                                       latitude = latitude, 
                                       longitude = longitude, 
                                       elevation = self.location.elevation,
                                       channels=[ch.obspy_channel for ch in self.instrumentation.channels], 
                                       site=site, 
                                       vault=self.location.vault, 
                                       geology=self.location.geology, 
                                       equipments=[self.instrumentation.equipment], 
                                       operators=None,  #Will be assigned in class Network, where it is specified.
                                       creation_date=start_date, 
                                       termination_date=end_date, 
                                       total_number_of_channels=channels_number, 
                                       selected_number_of_channels=channels_number, 
                                       description=None, 
                                       comments=comments,
                                       start_date=start_date, 
                                       end_date= end_date, 
                                       restricted_status=self.restricted_status, 
                                       alternate_code=None, 
                                       historical_code=None, 
                                       data_availability=None, 
                                       identifiers=None, 
                                       water_level=None, 
                                       source_id=None)
            
        return obspy_station
    
    def convert_notes_and_extras_to_obspy(self):
        """
        Convert info file notes and extras to XML comments
        """
    
        self.comments += ['EXTRA ATTRIBUTES (for documentation only):'] + self.extras
    
    

class Processing(object):
    """
    Processing Class.

    Saves a list of Processing steps
    For now, just stores the list
    """
    def __init__(self, the_list):
        """
        :param the_list: list of processing steps
        :type list: list
        """
        self.list = the_list

    def __repr__(self):
        s = f'Processing({self.list})'
        return s
