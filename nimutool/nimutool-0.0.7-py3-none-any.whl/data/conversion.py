import math

rad2deg = lambda x: x * (180 / math.pi)
rad2dph = lambda x: (x * (180 / math.pi)) * 3600
acc2g = lambda x: x / 9.81
acc2mg = lambda x: x / (9.81 / 1e3)
acc2ug = lambda x: x / (9.81 / 1e6)
