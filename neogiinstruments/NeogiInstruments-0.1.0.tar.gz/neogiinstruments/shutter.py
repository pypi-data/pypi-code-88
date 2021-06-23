import pyvisa
import time
import numpy as np
rm = pyvisa.ResourceManager()

class Shutter:
    def __init__(self):
        rm = pyvisa.ResourceManager()
        self.Shut = rm.open_resource('ASRL4::INSTR')

    def mode(self,arg):
        '''writes mode={arg}
        mode=1 == Manual mode
        mode=2 == Auto mode
        mode=3 == Single mode
        mode=4 == Repeat Mode
        mode=5 == External Gate mode'''
        if 0< arg <= 5:
            self.Shut.write(f'mode={arg}')
        else:
            print('Arg out of range')

    def enable(self):
        '''Toggle enable'''
        self.Shut.write('ens')

    def open(self):
        if self.Shut.query('ens?')==0:
            self.Shut.write('ens')
        elif self.Shut.query('ens?')==1:
            pass
        else:
            print('Shutter not found')

Shutter = Shutter()
