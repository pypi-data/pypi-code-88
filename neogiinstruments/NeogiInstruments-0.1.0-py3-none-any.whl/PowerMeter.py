# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 21:55:20 2020

@author: Mai Tai
"""

import pyvisa
import time
import numpy as np
rm = pyvisa.ResourceManager()

class PowerMeter:
    def __init__(self):

        self.Pmeter = rm.open_resource('ASRL/dev/ttyUSB1::INSTR')

    def Power(self):
        """Reads power from Gentec TPM300 via VISA commands
        The while loop avoids outputting invalid token
        >>>returns float

        to-do: incorporate different power ranges (itteratively check all avaliable
        ranges and chose the best fit. Log this choice)"""


        while True:
            try:
                Pread = self.Pmeter.query("*READPOWER:")
                PowerPM = float(Pread.split('e')[0].split('+')[1])
                return PowerPM
            except:
                 continue

    def PowAvg(self):
        P = []
        for i in range(0,5,1):
            p = self.Power()
            P.append(p)
            time.sleep(1)
        PowerAvg = np.mean(P)
        PowerStd = np.std(P)
        return PowerAvg, PowerStd

PowerMeter = PowerMeter()
