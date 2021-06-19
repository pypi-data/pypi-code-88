from LibratoneZipp import LibratoneZipp
import time

zipp = LibratoneZipp('192.168.1.31')
print(zipp.voicing)
zipp.voicing_set('neutral')
print(zipp.voicing)

