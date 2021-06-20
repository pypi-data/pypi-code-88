# -*- coding: utf-8 -*-

#实验效果：读取DS18B20防水温度传感器
#接线：使用windows或linux电脑连接一块arduino主控板，dht11连接D6，dht22连接D7
import time
from pinpong.board import Board,Pin,DS18B20

Board("PinPong Board").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("PinPong Board","COM36").begin()   #windows下指定端口初始化
#Board("PinPong Board","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("PinPong Board","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

ds18b20 = DS18B20(Pin(Pin.D4))

while True:
  temp = ds18b20.temp_c()
  print("temperature = ",temp)
  time.sleep(1)














