# -*- coding: utf-8 -*-
import time
from pinpong.board import Board
from pinpong.libs.dfrobot_bmi160 import BMI160

Board("xugu").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("xugu","COM36").begin()  #windows下指定端口初始化
#Board("xugu","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("xugu","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

bmi = BMI160()

bmi.begin(bmi.Acc)

while True:
  GyrX = bmi.getGyrX()
  AccX = bmi.getAccX()
  GyrY = bmi.getGyrY()
  AccY = bmi.getAccY()
  GyrZ = bmi.getGyrZ()
  AccZ = bmi.getAccZ()
  print("{}  {}  {}  {}  {}  {}".format(GyrX, GyrY, GyrZ, AccX, AccY, AccZ))
  time.sleep(0.5)