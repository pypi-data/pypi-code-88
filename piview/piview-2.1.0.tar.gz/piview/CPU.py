# Project:    PiView
# Filename:   CPU.py
# Location:   ./piview
# Author:     Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Created:    10/04/21
#
# This file provides the following features, methods and associated supporting
# code:
# - speed
# - maximum load
# - temperature

import subprocess

import psutil

from piview.Utils import Utils


class CPU:
    @staticmethod
    def speed():
        """
        Get the CPU frequency using the vcgencmd on Linux based systems

        If frequency cannot be determined, returns -1

        :rtype: integer
        :return: The CPU frequency in MHz
        """
        try:
            output = subprocess.check_output(
                ['vcgencmd', 'get_config', 'arm_freq'])
            output = output.decode()
            lines = output.splitlines()
            line = lines[0]
            freq = line.split('=')
            freq = float(freq[1])
        except:
            freq = -1
        return freq

    @staticmethod
    def max_load(random=False):
        """
        This function returns the maximum "CPU load" across all CPU cores,
        or -1 if no value determined.

        Providing a random=True parameter value will return a random value if
        the actual CPU load can't be determined.

        :param random: boolean default False
        :rtype: float
        :return: The maximum CPU Load in range 0-100
        """
        value = -1
        if psutil is not None:
            value = max(psutil.cpu_percent(percpu=True))
        if random:
            value = Utils.random_percentage()
        return float(value)

    @staticmethod
    def temperature():
        """
        Requests the CPU temperature from the vcgencmd returning the
        result to the caller as a floating point value to 2DP

        If no value can be determined, uses -999.99 as the
        returned "error" value.

        :rtype: float
        :return: The CPU temperature in degrees Celsius
        """
        try:
            temp = subprocess.check_output(['vcgencmd', 'measure_temp'])
            temp = float(temp[5:-3])
        except:
            temp = -999.99
        temp = round(temp, 2)
        return temp


    @staticmethod
    def temperature_k():
        """Provide temperature of the CPU in degrees Kelvin

        :return: CPU Temperature in Kelvin
        """
        temp_k =  CPU.temperature()
        if temp_k == -999.99:
            return temp_k
        return temp_k - 273.16
