# -*- coding: utf-8 -*-

#实验效果：读取模拟量
#接线：使用windows或linux电脑连接一块arduino主控板，16位AD模数模块接到I2C口SCL SDA
import time
from pinpong.board import Board
from pinpong.libs.dfrobot_ADS1115 import ADS1115

Board("xugu").begin()  #初始化，选择板型和端口号，不输入端口号则进行自动识别

ads = ADS1115() #默认地址0x48
#ads = ADS1115(i2c_addr = 0x49)


while True:
    #channel-0的模拟输出
    print(ads.read_voltage(0))
    time.sleep(0.1)
