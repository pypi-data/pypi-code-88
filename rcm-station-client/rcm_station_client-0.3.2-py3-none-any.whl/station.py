#  Copyright (c) 2020 Pim Hazebroek
#  This program is made available under the terms of the MIT License.
#  For full details check the LICENSE file at the root of the project.

"""
Utility to interact with the /stations endpoint
"""
import logging

import requests

from settings import timeout, verify, station_name, stations_endpoint, sensors


def get_sensors():
    """Retrieve the names of the sensors as comma separated string for the station"""
    logging.debug('Retrieving sensors for this station')
    try:
        uri = f'{stations_endpoint}/{station_name}'
        response = requests.get(uri, verify=verify, timeout=timeout)
        data = response.json()['sensors']
        logging.debug('Response body: %s', response.json())
        # _sensors = ','.join(map(lambda sensor: sensor['name'], data)) # SNYK
        _sensors = ','.join(sensor['name'] for sensor in data)
    except Exception as exception:
        logging.exception('Failed to retrieve sensors for station from server', exc_info=exception)
        logging.warning('Falling back to locally configured sensors')
        _sensors = sensors

    logging.debug('Sensors: %s', _sensors)
    return _sensors


def get_sensor_settings(sensor_name):
    """Retrieve the settings of a single sensor for this station"""
    logging.debug('Retrieving sensor settings for %s', sensor_name)
    try:
        uri = f'{stations_endpoint}/{station_name}/sensors/{sensor_name}/settings'
        response = requests.get(uri, verify=verify, timeout=timeout)
        logging.debug('Response body: %s', response.json())
        return response.json()['settings']
    except Exception as exception:
        logging.exception('Failed to retrieve sensor settings', exc_info=exception)
        return {}
