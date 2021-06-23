# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 16:34:50 2020

@author: Mai Tai
"""

from pymeasure.instruments.newport import esp300
from time import sleep

'''initializes esp300 with 2 axes'''

esp = esp300.ESP300("GPIB0::2::INSTR")

esp1 = esp300.Axis(1,esp)
esp2 = esp300.Axis(2,esp)
esp3 = esp300.Axis(3,esp)

esp.enable()

esp3.home()
sleep(.1)
while esp3.motion_done==False:
    print('moving')
    sleep(.1)

print('done')





#%%

for i in range(10):
    
    try:
        print(esp3.position)
        esp3.position = i
        sleep(1)
    except:
        pass