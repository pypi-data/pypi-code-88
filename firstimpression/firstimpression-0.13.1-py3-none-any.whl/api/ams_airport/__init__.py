from firstimpression.constants import TEMP_FOLDER, APIS, LOCAL_INTEGRATED_FOLDER
from firstimpression.file import download_install_media
import xml.etree.ElementTree as ET
import os

NAME = APIS['schiphol']
URL_FLIGHTS = 'https://api.schiphol.nl/public-flights/flights'
URL_STATIONS = 'https://api.schiphol.nl/public-flights/destinations'

STATIONS_JSON_FILENAME = 'stations.json'
STATIONS_MAX_FILE_AGE = 60 * 60 * 24 * 7 * 4

FLIGHTS_XML_FILENAME = 'flights.xml'
FLIGHTS_MAX_FILE_AGE = 60 * 10

PURGE_DIRECTORIES_DAYS = 7 * 4

XML_TEMP_PATH_FLIGHTS = os.path.join(TEMP_FOLDER, NAME, FLIGHTS_XML_FILENAME)
JSON_PATH_STATIONS = os.path.join(LOCAL_INTEGRATED_FOLDER, NAME, STATIONS_JSON_FILENAME)

FLIGHTS_MAX = 10

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
DATE_FORMAT = '%Y-%m-%d'
SCHEDULE_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S.000'
TIME_FORMAT = '%H:%M'

RESOURCE_VERSION = 'v4'

DEPARTING_STATUS = {
    'SCH': 'Flight scheduled',
    'DEL': 'Delayed',
    'WIL': 'Wait in Lounge',
    'GTO': 'Gate Open',
    'BRD': 'Boarding',
    'GCL': 'Gate Closing',
    'GTD': 'Gate closed',
    'DEP': 'Departed',
    'CNX': 'Cancelled',
    'GCH': 'Gate Change',
    'TOM': 'Tomorrow'
}

def get_stations(response):
    stations = dict()
    for destination in response.get('destinations', []):
        if not destination.get('iata', 'null') == 'null':
            name = destination.get('publicName', None)
            if not name is None:
                full_name = name.get('english', None)
                if not full_name is None:
                    stations[destination['iata']] = full_name
    
    return stations

def parse_flights(response):



def get_flight_route(flight):
    if os.path.isfile(JSON_PATH_STATIONS):
        destinations = json.load(open(JSON_PATH_STATIONS, 'r'))
    else:
        raise FileExistsError("The destinations file does not exists. Run this first.")    