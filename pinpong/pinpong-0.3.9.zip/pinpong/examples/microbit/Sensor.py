# -*- coding: utf-8 -*-

import time
from pinpong.board import Board
from pinpong.extension.microbit import MBSensor

Board("microbit").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("microbit","COM36").begin()   #windows下指定端口初始化
#Board("microbit","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("microbit","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

micro = MBSensor()

#micro.cal_compass()                                     #校准电子罗盘

while True:
  print(micro.buttonA_is_pressed())                    #按键A是否按下
#  print(micro.buttonB_is_pressed())                    #按键B是否按下
#  print(micro.buttonAB_is_pressed())                   #按键AB是否按下
#  print(micro.touch0())                                #接口0是否被接通
#  print(micro.touch1())                                #接口1是否被接通
#  print(micro.touch2())                                #接口2是否被接通
#  print(micro.get_gesture())                            #获取当前姿态,返回字符串
#  print(micro.get_brightness())                        #读取环境光
#  print(micro.get_compass())                           #读取指南针
#  print(micro.get_temp())                               #获取温度
#  print(micro.get_accelerometer_X())                    #读取加速度X的值
#  print(micro.get_accelerometer_Y())                    #读取加速度Y的值
#  print(micro.get_accelerometer_Z())                    #读取加速度Z的值
#  print(micro.get_accelerometer_strength())             #读取加速度的强度
  print("------------------")
  time.sleep(0.2)
