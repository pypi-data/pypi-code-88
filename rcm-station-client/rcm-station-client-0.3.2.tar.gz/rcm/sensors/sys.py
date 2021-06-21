#  Copyright (c) 2020 Pim Hazebroek
#  This program is made available under the terms of the MIT License.
#  For full details check the LICENSE file at the root of the project.

"""
System sensor that reports data of the system itself.
"""
import logging

import psutil

from constants import SENSOR_SYS
from sensors.sensor import Sensor


class SYS(Sensor):
    """Concrete implementation of the system sensor."""

    @property
    def name(self):
        return SENSOR_SYS

    @staticmethod
    def _get_temps():
        """Returns a dict with temperature sensors and their current value"""
        if not hasattr(psutil, "sensors_temperatures"):
            logging.warning('Platform does not support temperature sensors')
            return {}
        temps = psutil.sensors_temperatures()
        if not temps:
            logging.warning('Could not read temperature sensors')
            return {}
        data = {}
        for name, entries in temps.items():
            for entry in entries:
                data[entry.label or name] = entry.current
        return data

    def _get_cpu_temp(self):
        temps = self._get_temps()
        if 'cpu_thermal' in temps:
            return temps['cpu_thermal']
        return None

    def read(self):
        """Read system metrics"""
        logging.info('Reading system sensor')

        disk = psutil.disk_usage('/')
        mem = psutil.virtual_memory()
        load = psutil.getloadavg()
        net = psutil.net_io_counters()
        cpu_count = psutil.cpu_count()
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_freq = psutil.cpu_freq()

        measurements = {
            'disk-total': disk.total,
            'disk-free': disk.free,
            'disk-used': disk.used,
            'mem-total': mem.total,
            'mem-available': mem.available,
            'mem-used': mem.used,
            'load-avg-1': load[0],
            'load-avg-5': load[1],
            'load-avg-15': load[2],
            'net-bytes-sent': net.bytes_sent,
            'net-bytes-recv': net.bytes_recv,
            'net-packets-sent': net.packets_sent,
            'net-packets-recv': net.packets_recv,
            'net-errin': net.errin,
            'net-errout': net.errout,
            'net-dropin': net.dropin,
            'net-dropout': net.dropout,
            'cpu-count': cpu_count,
            'cpu-percent': cpu_percent,
            'cpu-frequency': cpu_freq.current,
            'sys-boot-time': psutil.boot_time()
        }

        cpu_temps = self._get_cpu_temp()
        if cpu_temps:
            measurements['cpu-temp'] = cpu_temps

        logging.info('Measurement: %s', measurements)
        return measurements
