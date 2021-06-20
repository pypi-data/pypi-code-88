# -*- coding: utf-8 -*-

import time
from pinpong.board import Board
from pinpong.extension.handpy import HPWS2812

Board("handpy").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("handpy","COM36").begin()   #windows下指定端口初始化
#Board("handpy","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("handpy","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

esp32 = HPWS2812()

esp32.set_rgb_color(-1, 255, 0, 0)                       #设置LED灯的颜色，-1代表3个灯(可以填灯号0,1,2)，255,0,0代表rgb
time.sleep(1)
esp32.rgb_disable(-1)                                       #关闭LED灯，-1代表3个灯(可以填灯号0,1,2)
#time.sleep(1)
#esp32.set_brightness(7)                                     #设置LED灯的亮度，范围0-9
#time.sleep(1)
#esp32.get_brightness()                                      #返回LED灯的亮度值
while True:
  pass