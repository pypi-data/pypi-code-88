"""
Instrumentation and Instrument classes

nomenclature:
    An "Instrument" (measurement instrument) records one physical parameter
    An "Instrumentation" combines one or more measurement instruments
"""
# Standard library modules
import warnings
# Non-standard modules
from obspy.core.inventory.network import Network as obspy_Network
import obspy.core.util.obspy_types as obspy_types
from obspy.core.inventory.util import (Person, Comment, PhoneNumber)
from obspy.core.inventory.util import Operator as obspy_Operator
from obspy.core.utcdatetime import UTCDateTime
# obsinfo modules
from ..obsMetadata.obsmetadata import (ObsMetadata)
from ..network.station import (Station, Location)
from ..instrumentation.instrumentation import (Operator)


class Network(ObsMetadata):
    """
    One or more Instruments. Part of an obspy/StationXML Station
    """
    def __init__(self, attributes_dict=None):
        """
        Constructor
        """
        
        if not attributes_dict:
            raise TypeError('No network attributes')
        
        self.campaign_ref = attributes_dict.get("campaing_ref_name", None)
        network_info = attributes_dict.get("network_info", None)
        
        self.fdsn_code = network_info.get("code", None)
        self.fdsn_name = network_info.get("name", None)        
        self.start_date = network_info.get("start_date", 0)
        self.end_date = network_info.get("end_date", 0)
        self.description = network_info.get("description", None)
        
        self.restricted_status = attributes_dict.get("restricted_status", None)
        
        self.operator = Operator(attributes_dict.get("operator", None))  
        
        stations = attributes_dict.get("stations", None)              
        self.stations = [Station(k, v) for k, v in stations.items()]
        
        self.comments = attributes_dict.get("comments", [])
        self.extras = [str(k) + ": " + str(v) for k, v in (attributes_dict.get('extras', {})).items()]
        self.convert_notes_and_extras_to_obspy() 
        
        self.obspy_network = self.to_obspy()     
          

    def __repr__(self):
        s = f'Network(Campaign: {self.campaign_ref}, FDSN Code: {self.fdsn_code}, FDSN Name: {self.fdsn_code}, '
        s += f'Start date: {self.start_date}, End date: {self.end_date}, Description: {self.description}, '
        s += f'{len(self.stations)} stations)'

        return s
    
    def to_obspy(self):
        """
         Convert network object to obspy object
        """
        if self.operator:
            
            mails = [self.operator.email] if self.operator.email else []
            phones = [PhoneNumber(0, self.operator.phone_number)] if self.operator.phone_number else []
            person = Person(names=[self.operator.contact], 
                            agencies=[self.operator.reference_name], 
                            emails=mails, 
                            phones=phones)
                   
            operator = obspy_Operator(agency=[self.operator.full_name],  contacts=[person], website=self.operator.website)
        else:
            operator = None
                      
        stations_number = len(self.stations)
        start_date = UTCDateTime(self.start_date if self.start_date else 0)
        end_date = UTCDateTime(self.end_date if self.end_date else 0)
        comments = [Comment(s) for s in self.comments]
        
        
        self.obspy_network = obspy_Network(code=self.fdsn_code, 
                                     stations=  [st.obspy_station for st in self.stations], 
                                     total_number_of_stations=stations_number, 
                                     selected_number_of_stations=stations_number, 
                                     description=self.description, 
                                     comments=comments,
                                     start_date=start_date, 
                                     end_date=end_date, 
                                     restricted_status=self.restricted_status, 
                                     alternate_code=None, 
                                     historical_code=None, 
                                     data_availability=None, 
                                     identifiers=None, 
                                     operators=[operator], 
                                     source_id=None)
        
        for st in self.stations:  #complete stations
            st.operators = [operator]
            
        print(self.obspy_network)
        
        return self.obspy_network
    
    def convert_notes_and_extras_to_obspy(self):
        """
        Convert info file notes and extras to XML comments
        """
    
        self.comments += ['EXTRA ATTRIBUTES (for documentation only): '] + self.extras
    
    
    