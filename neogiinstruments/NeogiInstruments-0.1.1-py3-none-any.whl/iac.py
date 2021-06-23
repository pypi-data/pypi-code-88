from neogiinstruments.esp300 import ESP300
from time import sleep
from Photodiode import Photodiode
import matplotlib.pyplot as plt
ESP300 = ESP300()
ESP300.Home(1)
print('homing...')
sleep(10)
V = []
StDev = []
pos = []
for i in range(10):
    ESP300.moveRel(1,.1+i)
    sleep(.51)
    v = Photodiode()
    V.append(v[0])
    StDev.append(v[1])
    pos.append(i)
    print(i)

plt.plot(pos,V)

