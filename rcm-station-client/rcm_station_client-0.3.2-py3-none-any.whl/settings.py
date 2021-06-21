#  Copyright (c) 2020 Pim Hazebroek
#  This program is made available under the terms of the MIT License.
#  For full details check the LICENSE file at the root of the project.
"""Application wide settings that are shared across multiple modules"""

import os
import sys
from distutils.util import strtobool

from dotenv import load_dotenv

from constants import ONE_MB, DEFAULT_GAIN, DEFAULT_IT_TIME

try:
    load_dotenv()

    # Logging
    log_file = os.getenv('log-file', '/home/pi/rcm-station-client.log')
    log_level = os.getenv('log-level', 'WARN')
    log_max_bytes = int(os.getenv('log-max-bytes', ONE_MB))
    log_backup_count = int(os.getenv('log-backup-count', '5'))
    # pylint: disable=invalid-name
    log_include_console_handler = bool(strtobool(os.getenv('log-include-console-handler', 'false')))

    # Requests
    timeout = int(os.getenv('requests-timeout', '5'))
    verify = False

    # RCM specific
    api_base_url = os.getenv('api-base-url', 'https://raspberrypi.local:8080')
    reports_endpoint = api_base_url + '/measurement-reports'
    stations_endpoint = api_base_url + '/stations'
    station_name = os.getenv('station-name')
    sensors = os.getenv('sensors')

    tsl2591_gain = os.getenv('tsl2591-gain', DEFAULT_GAIN)
    tsl2591_integration_time = os.getenv('tsl2591-integration-time', DEFAULT_IT_TIME)
    # pylint: disable=invalid-name
    sgp30_init_baseline = bool(strtobool(os.getenv('sgp30-init-baseline', 'false')))
    sgp30_baseline_file = os.getenv('sgp30-baseline-file', '/home/pi/rcm-sgp30-baseline.txt')

    # Security
    # pylint: disable=invalid-name
    auth_enabled = bool(strtobool(os.getenv('auth-enabled', 'true')))
    token_endpoint = os.getenv('auth-token-endpoint')
    client_id = os.getenv('auth-client-id', 't6N95EF5uZgXJYqYONKXmiwTMSwxpcvw')
    client_secret = os.getenv('auth-client-secret')
    audience = os.getenv('auth-audience', 'https://station-monitoring-service')
    token_file = os.getenv('token-file', 'token.txt')

    # Other
    # pylint: disable=invalid-name
    disable_I2C = bool(strtobool(os.getenv('disable-i2c', 'false')))

    # Validation
    if station_name is None:
        raise ValueError('Station name is missing. Please configure "station-name" in the .env file')
    if sensors is None:
        raise ValueError('No sensors configured. Please configure "sensors" in the .env file')
    if auth_enabled and (token_endpoint is None or client_id is None or client_secret is None or audience is None):
        raise ValueError('Auth is not configured properly, please double check settings')
except Exception as exception:
    print('Invalid configuration', exception)
    sys.exit(1)
