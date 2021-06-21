#  Copyright (c) 2020 Pim Hazebroek
#  This program is made available under the terms of the MIT License.
#  For full details check the LICENSE file at the root of the project.

"""
The BME680 sensor - Temperature, Humidity, Pressure and Gas Sensor
=========================================

See https://www.adafruit.com/product/3660
"""
import logging

import adafruit_bme680

from constants import SENSOR_BME680
from sensors.sensor import Sensor


class BME680(Sensor):
    """
    Concrete implementation of the BME680 sensor.
    """

    @property
    def name(self):
        return SENSOR_BME680

    def read(self):
        """
        Reads the temperature, humidity, air pressure and VOC gas.
        """
        logging.info('Reading BME680 sensor')
        sensor = adafruit_bme680.Adafruit_BME680_I2C(self._i2c)
        measurements = {
            'temperature': sensor.temperature,
            'humidity': sensor.humidity,
            'air-pressure': sensor.pressure,
            'voc-gas': sensor.gas
        }
        logging.info('Measurement: %s', measurements)
        return measurements
