#  Copyright (c) 2020 Pim Hazebroek
#  This program is made available under the terms of the MIT License.
#  For full details check the LICENSE file at the root of the project.
"""The abstract base class (ABC) for every sensor."""

import logging
from abc import ABCMeta, abstractmethod

from settings import disable_I2C
from station import get_sensor_settings

if not disable_I2C:
    import busio
    from board import SCL, SDA


class Sensor(metaclass=ABCMeta):
    """
    A base class for sensors connected to the station via I2C.
    """

    @property
    @abstractmethod
    def name(self):
        """The name of the sensor, as known by the server"""
        raise NotImplementedError

    def __init__(self):
        """Initialize the I2C bus to communicate with the sensors. When in simulation mode, I2C is not initialized."""
        if not disable_I2C:
            self._i2c = busio.I2C(SCL, SDA)
        self._settings = get_sensor_settings(self.name)
        logging.debug('Sensor settings: %s', self._settings)

    @abstractmethod
    def read(self):
        """
        Connect to the sensor over I2C and perform a measurement and return the value(s) that were measured.
        May return multiple values if the sensor measures multiple metrics.

        :rtype dict
        """
        raise NotImplementedError
