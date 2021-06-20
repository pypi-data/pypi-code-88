# -*- coding: utf-8 -*-

import time
from pinpong.board import Board
from pinpong.extension.handpy import HPSensor

Board("handpy").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("handpy","COM36").begin()   #windows下指定端口初始化
#Board("handpy","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("handpy","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

esp = HPSensor()

while True:
#  print(esp.buttonA_is_pressed())                    #按键A是否按下
#  print(esp.buttonB_is_pressed())                    #按键B是否按下
#  print(esp.buttonAB_is_pressed())                   #按键AB是否按下
#  print(esp.touch_P())                               #是否触摸P
#  print(esp.touch_Y())                               #是否触摸Y
#  print(esp.touch_T())                               #是否触摸T
#  print(esp.touch_H())                               #是否触摸H
#  print(esp.touch_O())                               #是否触摸O
#  print(esp.touch_N())                               #是否触摸N
#  esp.set_touch_threshold("all",60)                  #设置按键P/Y/T/H/O/N的触摸阈值，all代表全部，范围为0-80
#  print(esp.read_touch_P())                          #读取按键P的触摸值
#  print(esp.read_touch_Y())                          #读取按键Y的触摸值
#  print(esp.read_touch_T())                          #读取按键T的触摸值
#  print(esp.read_touch_H())                          #读取按键H的触摸值
#  print(esp.read_touch_O())                          #读取按键O的触摸值
#  print(esp.read_touch_N())                          #读取按键N的触摸值
#  print(esp.read_sound())                            #读取麦克风强度
#  print(esp.read_light())                            #读取环境光强度
  print(esp.get_accelerometer_X())                    #读取加速度X的值
  print(esp.get_accelerometer_Y())                    #读取加速度Y的值
  print(esp.get_accelerometer_Z())                    #读取加速度Z的值
  print(esp.get_accelerometer_strength())             #读取加速度的强度
  print("------------------")
  time.sleep(0.2)
