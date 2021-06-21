#  Copyright (c) 2020 Pim Hazebroek
#  This program is made available under the terms of the MIT License.
#  For full details check the LICENSE file at the root of the project.

"""
The TSL2591 sensor - High Dynamic Range Digital Light Sensor
============================================================

See https://www.adafruit.com/product/439

Gain & Timing
You can adjust the gain settings and integration time of the sensor to make it more or less sensitive to light, depending on the
environment where the sensor is being used.

Gain:
GAIN_LOW: Sets the gain to 1x (bright light)
GAIN_MEDIUM or GAIN_MED: Sets the gain to 25x (general purpose)
GAIN_HIGH: Sets the gain to 428x (low light)
GAIN_MAX: Sets the gain to 9876x (extremely low light)

The integration time can be set between 100 and 600ms, and the longer the integration time the more light the sensor is able to integrate,
making it more sensitive in low light the longer the integration time. The following values can be used:
100MS
200MS
300MS
400MS
500MS
600MS
"""
import logging

import adafruit_tsl2591

from constants import GAIN_LOW, GAIN_MEDIUM, GAIN_HIGH, GAIN_MAX
from constants import IT_TIME_100MS, IT_TIME_200MS, IT_TIME_300MS, IT_TIME_400MS, IT_TIME_500MS, IT_TIME_600MS, SENSOR_TSL2591
from sensors.sensor import Sensor
from settings import tsl2591_gain, tsl2591_integration_time

# Maximum lux the sensor can measure
_MAX_LUX = 88000

gain_values = {
    GAIN_LOW: adafruit_tsl2591.GAIN_LOW,
    GAIN_MEDIUM: adafruit_tsl2591.GAIN_MED,
    GAIN_HIGH: adafruit_tsl2591.GAIN_HIGH,
    GAIN_MAX: adafruit_tsl2591.GAIN_MAX
}

integration_times = {
    IT_TIME_100MS: adafruit_tsl2591.INTEGRATIONTIME_100MS,
    IT_TIME_200MS: adafruit_tsl2591.INTEGRATIONTIME_200MS,
    IT_TIME_300MS: adafruit_tsl2591.INTEGRATIONTIME_300MS,
    IT_TIME_400MS: adafruit_tsl2591.INTEGRATIONTIME_400MS,
    IT_TIME_500MS: adafruit_tsl2591.INTEGRATIONTIME_500MS,
    IT_TIME_600MS: adafruit_tsl2591.INTEGRATIONTIME_600MS
}


class TSL2591(Sensor):
    """Concrete implementation of the TSL2591 sensor."""

    @property
    def name(self):
        return SENSOR_TSL2591

    def read(self):
        """Reads the full spectrum light in lux, and raw human visible light plus raw IR light."""
        logging.info('Reading TSL2591 sensor')
        sensor = adafruit_tsl2591.TSL2591(self._i2c)
        # if tsl2591_gain in gain_values.keys(): #SNYK
        if tsl2591_gain in gain_values:
            sensor.gain = gain_values[tsl2591_gain]
            logging.debug('set gain to %s', tsl2591_gain)
        else:
            logging.warning('Gain %s is not supported', tsl2591_gain)

        # if tsl2591_integration_time in integration_times.keys(): #SNYK
        if tsl2591_integration_time in integration_times:
            sensor.integration_time = integration_times[tsl2591_integration_time]
            logging.debug('set integration_time to %s', tsl2591_integration_time)
        else:
            logging.warning('Integration time %s is not supported', tsl2591_integration_time)

        # Read lux property of sensor. Can raise RuntimeError in very bright circumstances.
        try:
            lux = sensor.lux
        except RuntimeError:
            logging.warning("Sensor overflow detected while reading lux")
            lux = _MAX_LUX
        measurements = {
            'lux': lux,
            'visible-light': sensor.visible,
            'IR-light': sensor.infrared
        }
        logging.info('Measurement: %s', measurements)
        return measurements
