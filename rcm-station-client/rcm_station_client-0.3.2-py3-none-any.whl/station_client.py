#  Copyright (c) 2020 Pim Hazebroek
#  This program is made available under the terms of the MIT License.
#  For full details check the LICENSE file at the root of the project.

"""
This is the Station Client that reads measurements from sensors and reports them to the station monitoring service.
The station client is typically run on a raspberry-pi. One RPi represents one station.
"""
import logging
import sys
from logging import StreamHandler
from logging.handlers import RotatingFileHandler

import requests
import urllib3

import auth
import constants
import settings
import station
from sensors.bme680 import BME680
from sensors.sgp30 import SGP30
from sensors.sht31d import SHT31D
from sensors.sys import SYS
from sensors.tsl2591 import TSL2591

drivers = {
    constants.SENSOR_BME680: BME680,
    constants.SENSOR_SHT31_D: SHT31D,
    constants.SENSOR_TSL2591: TSL2591,
    constants.SENSOR_SGP30: SGP30,
    constants.SENSOR_SYS: SYS
}


def main():
    """
    Main entry point for the station client. Reads the connected sensors one by one and submits the measurements reports collected from
    these sensors to the station-monitoring-service.
    """
    try:
        _init_logger()
        logging.info('Running RCM Station Client (%s)', settings.station_name)
        # Disable warnings about unsecure connection, since HTTPS verify is set to False due to self signed certificate.
        urllib3.disable_warnings()
        sensors = station.get_sensors()
        for sensor in sensors.split(','):
            if sensor not in drivers.keys():
                raise ValueError('Unsupported sensor: ' + sensor)
            driver = drivers[sensor]()
            measurement_report = driver.read()
            _submit(measurement_report)
    except Exception as exception:
        print('Unexpected error: ', exception)
        logging.exception('Unexpected error: ', exc_info=exception)
        sys.exit(1)
    sys.exit(0)


def _init_logger():
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    rotating_file_handler = RotatingFileHandler(settings.log_file, maxBytes=settings.log_max_bytes, backupCount=settings.log_backup_count)
    rotating_file_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(rotating_file_handler)
    if settings.log_include_console_handler:
        console_handler = StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    logger.setLevel(settings.log_level)


def _submit(measurement_report):
    logging.debug('Submitting measurement report for station %s to %s', settings.station_name, settings.reports_endpoint)
    payload = {
        'stationName': settings.station_name,
        'measurements': measurement_report
    }
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {auth.get_token()}'
    }
    try:
        response = requests.post(settings.reports_endpoint, json=payload, headers=headers, verify=settings.verify, timeout=settings.timeout)
        response.raise_for_status()
    except Exception as exception:
        logging.exception('Failed to submit measurements report', exc_info=exception)
        sys.exit(1)


if __name__ == '__main__':
    main()
