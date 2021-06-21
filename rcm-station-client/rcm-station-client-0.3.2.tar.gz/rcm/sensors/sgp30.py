#  Copyright (c) 2020 Pim Hazebroek
#  This program is made available under the terms of the MIT License.
#  For full details check the LICENSE file at the root of the project.

"""
The SGP30 sensor - tVOC and eCO2 sensor
=========================================

See https://www.adafruit.com/product/3709

The first time this sensor is used, the setting `sgp30-init-baseline` should be set to true and the script should be run in the background
for approx. 12 hours. This will establish a baseline for the sensor which is then written to disk. It will store the baseline every hour.
Check the SGP30 datasheet for more details.
See https://cdn-learn.adafruit.com/assets/assets/000/050/058/original/Sensirion_Gas_Sensors_SGP30_Datasheet_EN.pdf
"""
import logging
import os
import sys
import time

import adafruit_sgp30

from constants import MODE_WRITE, MODE_READ, LINE_SEP, SENSOR_SGP30
from sensors.sensor import Sensor
from settings import sgp30_init_baseline, sgp30_baseline_file


class SGP30(Sensor):
    """
    Concrete implementation of the SGP30 sensor.
    """

    @property
    def name(self):
        return SENSOR_SGP30

    def __init__(self):
        """
        Initialize the sensor. After the sensor is initialized, it will be in an initialization phase for about 15 seconds
        and only return default values of eCO2 400 ppm and TVOC 0 ppb.
        """
        logging.debug('Initializing SGP30 sensor')
        super().__init__()
        self._sensor = adafruit_sgp30.Adafruit_SGP30(self._i2c)

    def read(self):
        """
        Reads the sensor. The sensor is optimize for a sampling rate of 1Hz so we start reading measurements once every second for about
         30 seconds to get a stable reading and be sure initialization phase is completed.
        """
        logging.info('Reading SGP30 sensor')

        if sgp30_init_baseline:
            self._init_baseline()

        self._apply_baseline()

        elapsed_sec = 0
        while elapsed_sec < 30:
            self._compile_measurement_report()
            time.sleep(1)
            elapsed_sec += 1

        report = self._compile_measurement_report()
        logging.info('Measurement: %s', report)
        return report

    def _compile_measurement_report(self):
        """
        Send a measurement command to the sensor and read the values to compile the measurement report and return it.
        """
        self._sensor.iaq_measure()
        measurements = {
            'raw-ethanol': self._sensor.Ethanol,
            'raw-H2': self._sensor.H2,
            'TVOC': self._sensor.TVOC,
            'eCO2': self._sensor.eCO2,
        }
        logging.debug('Measurement: %s', measurements)
        return measurements

    def _apply_baseline(self):
        """Read the baseline values from disk and configure the sensor with these values"""
        logging.debug('Reading IAQ baseline values from file')
        if not os.path.isfile(sgp30_baseline_file):
            logging.warning('SGP30 baseline values not stored yet, please establish baseline first!')
            return

        try:
            with open(sgp30_baseline_file, MODE_READ) as file:
                content = file.read().splitlines()
                eco2_baseline = int(content[0])
                tvoc_baseline = int(content[1])
                self._sensor.set_iaq_baseline(eco2_baseline, tvoc_baseline)
                logging.info('Applied baseline: eCO2 = 0x%x, TVOC = 0x%x', eco2_baseline, tvoc_baseline)
        except Exception as exception:
            logging.exception('Failed to read SGP30 baseline values from file', exc_info=exception)
            sys.exit(1)

    def _init_baseline(self):
        """
        Start reading the sensors continuously to establish the baseline. Best baseline is achieved after approx. 12 hours.
        """
        logging.warning('Initializing IAQ baseline, please let it run for at least 12 hours')
        elapsed_sec = 0
        while True:
            self._compile_measurement_report()
            time.sleep(1)
            elapsed_sec += 1
            if elapsed_sec > 60:
                logging.info('Baseline: eCO2 = 0x%x, TVOC = 0x%x', self._sensor.baseline_eCO2, self._sensor.baseline_TVOC)
            if elapsed_sec > 3600:
                elapsed_sec = 0
                self._store_baseline()

    def _store_baseline(self):
        """Write the baseline values to disk"""
        logging.debug('Writing IAQ baseline values to file')
        try:
            with open(sgp30_baseline_file, MODE_WRITE) as file:
                eco2_baseline = str(self._sensor.baseline_eCO2) + LINE_SEP
                tvoc_baseline = str(self._sensor.baseline_TVOC) + LINE_SEP
                timestamp = str(time.time())
                file.writelines([eco2_baseline, tvoc_baseline, timestamp])
        except Exception as exception:
            logging.exception('Failed to write SGP30 baseline values to file', exc_info=exception)
            sys.exit(1)
