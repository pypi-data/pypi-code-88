# -*- coding:utf-8 -*-
from __future__ import print_function

import time
import RPi.GPIO as GPIO
import dht11


class Temp_Hum(object):
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()

        # read data using pin 17
        self.instance = dht11.DHT11(pin=17)

    def get_temperature(self):
        i = 0
        while i < 5:
            result = self.instance.read()
            if result.is_valid():
                return "{:.2f}".format(result.temperature)
            else:
                time.sleep(1)
                i = i + 1
        return -301

    def get_humidity(self):
        i = 0
        while i < 5:
            result = self.instance.read()
            if result.is_valid():
                return "{:.2f}".format(result.humidity)
            else:
                time.sleep(1)
                i = i + 1
        return -301


if __name__ == "__main__":
    tempHum = Temp_Hum()
    print(tempHum.get_temperature())
