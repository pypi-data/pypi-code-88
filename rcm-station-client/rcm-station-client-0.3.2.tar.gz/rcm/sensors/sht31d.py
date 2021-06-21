#  Copyright (c) 2020 Pim Hazebroek
#  This program is made available under the terms of the MIT License.
#  For full details check the LICENSE file at the root of the project.

"""
The SHT31-D sensor - High precision Temperature & Humidity sensor
=================================================================

See https://www.adafruit.com/product/2857
"""
import logging
from distutils.util import strtobool

import adafruit_sht31d

from constants import SENSOR_SHT31_D
from sensors.sensor import Sensor

_PRIMARY_ADDRESS = 0x44
_SECONDARY_ADDRESS = 0x45


class SHT31D(Sensor):
    """Concrete implementation of SHT31-D sensor."""

    @property
    def name(self):
        return SENSOR_SHT31_D

    def read(self):
        """
        Reads the temperature and relative humidity.
        """
        logging.info('Reading SHT31-D sensor')
        address = self._get_address()
        sensor = adafruit_sht31d.SHT31D(self._i2c, address)
        measurements = {
            'temperature': sensor.temperature,
            'humidity': sensor.relative_humidity
        }
        logging.info('Measurement: %s', measurements)
        return measurements

    def _get_address(self):
        """Determine the I2C address to use"""
        if 'secondary_address' not in self._settings.keys():
            address = _PRIMARY_ADDRESS
        else:
            address = _SECONDARY_ADDRESS if strtobool(self._settings['secondary_address']) else _PRIMARY_ADDRESS

        return address
