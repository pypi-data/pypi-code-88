from firstimpression.constants import TEMP_FOLDER
from firstimpression.constants import APIS
from firstimpression.constants import LOCAL_INTEGRATED_FOLDER
from firstimpression.file import download_install_media
from firstimpression.file import write_root_to_xml_files
from firstimpression.file import update_directories_api
from firstimpression.file import check_too_old
from firstimpression.time import parse_date_to_string
from firstimpression.time import parse_string_to_string
from firstimpression.json import lst_dict_to_root
from firstimpression.scala import variables
from firstimpression.api.request import request
import xml.etree.ElementTree as ET
import os
import json
import datetime
import glob

##################################################################################################
# CONSTANTS
##################################################################################################

NAME = APIS['schiphol']
URL_FLIGHTS = 'https://api.schiphol.nl/public-flights/flights'
URL_STATIONS = 'https://api.schiphol.nl/public-flights/destinations'

STATIONS_JSON_FILENAME = 'stations.json'
STATIONS_MAX_FILE_AGE = 60 * 60 * 24 * 7 * 4

FLIGHTS_XML_FILENAME = 'flights.xml'
FLIGHTS_XML_FILENAME_CONTENT = 'flights*.xml'
FLIGHTS_MAX_FILE_AGE = 60 * 10

PURGE_DIRECTORIES_DAYS = 7 * 4

XML_TEMP_PATH_FLIGHTS = os.path.join(TEMP_FOLDER, NAME, FLIGHTS_XML_FILENAME)
XML_LOCAL_PATH_FLIGHTS = os.path.join(LOCAL_INTEGRATED_FOLDER, NAME, FLIGHTS_XML_FILENAME_CONTENT)
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

HEADERS = {
    'Accept': 'application/json',
    'ResourceVersion': RESOURCE_VERSION
}

##################################################################################################
# MAIN FUNCTIONS API
##################################################################################################

def run_api(id, key):
    HEADERS['app_id'] = id
    HEADERS['app_key'] = key

    update_directories_api(NAME, PURGE_DIRECTORIES_DAYS)

    if check_too_old(JSON_PATH_STATIONS, STATIONS_MAX_FILE_AGE):
        page = 0
        params = dict()
        stations = dict()

        for i in range(100000):
            params['page'] = page
            response = request(URL_STATIONS, HEADERS, params)

            if response.status_code != 200:
                break
            
            stations.update(get_stations(response.json()))

            page += 1
        
        with open(JSON_PATH_STATIONS, 'w') as file:
            json.dump(stations, file)
    
    if check_too_old(XML_TEMP_PATH_FLIGHTS, FLIGHTS_MAX_FILE_AGE):
        page = 0
        params = {
            'sort': '+scheduleDateTime',
            'flightDirection': 'D',
            'searchDateTimeField': 'scheduleDateTime',
            'fromDateTime': parse_date_to_string(datetime.datetime.now(), DATETIME_FORMAT),
            'toDateTime': parse_date_to_string(datetime.datetime.now(), DATE_FORMAT) + 'T23:59:59'
        }
        flights = list()

        if os.path.isfile(JSON_PATH_STATIONS):
            destinations = json.load(open(JSON_PATH_STATIONS, 'r'))
        else:
            raise FileExistsError("The stations file does not exists. Run this first.")

        for i in range(100000):
            params['page'] = page
            response = request(URL_FLIGHTS, HEADERS, params)

            if response.status_code != 200:
                break

            flights = parse_flights(flights, destinations, response.json())

            if len(flights) == FLIGHTS_MAX:
                break

            page += 1
        
        write_root_to_xml_files(lst_dict_to_root(flights), XML_TEMP_PATH_FLIGHTS, NAME)


def check_api():
    svars = variables()

    file_path = glob.glob(XML_LOCAL_PATH_FLIGHTS)[0]

    if check_too_old(file_path, FLIGHTS_MAX_FILE_AGE):
        svars['skipscript'] = True
    else:
        svars['skipscript'] = False

##################################################################################################
# MEDIA FUNCTIONS
##################################################################################################


##################################################################################################
# GET FUNCTIONS
##################################################################################################

def get_stations(response):
    stations = dict()
    for destination in response.get('destinations', []):
        if not destination.get('iata', 'null') == 'null' and not destination.get('iata', None) is None:
            name = destination.get('publicName', None)
            if not name is None:
                full_name = name.get('english', None)
                if not full_name is None:
                    stations[destination['iata']] = full_name
    
    return stations

def get_flight_route(flight, destinations):

    route = list()

    for elem in flight.get('route',{}).get('destinations', 'null'):
        route.append(destinations.get(elem, 'Onbekend'))
    
    return ', '.join(route)

def get_departure_time(flight):
    dt = flight.get('scheduleDateTime', None)
    if dt is None:
        return ''
    else:
        dt = dt[:-6]    
        return parse_string_to_string(dt, SCHEDULE_DATETIME_FORMAT, TIME_FORMAT)

def get_flight_number(flight):
    return flight.get('flightName', 'Onbekend')

def get_flight_status(flight):
    status = flight.get('publicFlightState', {}).get('flightStates', ['null'])[0]

    return DEPARTING_STATUS.get(status, 'Unknown')

##################################################################################################
# PARSE FUNCTIONS
##################################################################################################

def parse_flights(flights, destinations, response):

    for flight_info in response.get('flights', []):
        flight = dict()
        skip = False

        flight['route'] = get_flight_route(flight_info, destinations)
        flight['departure_time'] = get_departure_time(flight_info)
        flight['flight_number'] = get_flight_number(flight_info)
        flight['status'] = get_flight_status(flight_info)

        for i in range(len(flights)):
            if flights[i]['route'] == flight['route'] and flights[i]['departure_time'] == flight['departure_time'] and flights[i]['status'] == flight['status']:
                flights[i]['flight_number'] += ', ' + flight['flight_number']
                skip = True
        
        if not skip:
            flights.append(flight)
        
        if len(flights) == FLIGHTS_MAX:
            break
    
    return flights
        

        

