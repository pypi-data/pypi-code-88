# -*- coding: utf-8 -*-

import time
from pinpong.board import Board
from pinpong.extension.GD32V import GD32VSensor

Board("GD32V").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("GD32V","COM36").begin()   #windows下指定端口初始化
#Board("GD32V","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("GD32V","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

gd32v = GD32VSensor()

while True:
  print(gd32v.buttonA_is_pressed())                    #按键A是否按下
#  print(gd32v.buttonB_is_pressed())                    #按键B是否按下
#  print(gd32v.read_light())                            #读取环境光强度
#  print(gd32v.get_accelerometer_X())                    #读取加速度X的值
#  print(gd32v.get_accelerometer_Y())                    #读取加速度Y的值
#  print(gd32v.get_accelerometer_Z())                    #读取加速度Z的值
#
#  print(gd32v.get_Macceleration_X())                    #读取磁力计X的值
#  print(gd32v.get_Macceleration_Y())                    #读取磁力计Y的值
#  print(gd32v.get_Macceleration_Z())                    #读取磁力计Z的值
#
  print("------------------")
  time.sleep(0.3)
