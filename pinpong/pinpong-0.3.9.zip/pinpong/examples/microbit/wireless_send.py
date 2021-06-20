# -*- coding: utf-8 -*-

import time
from pinpong.board import Board
from pinpong.extension.microbit import MBWireless

Board("microbit").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("microbit","COM36").begin()   #windows下指定端口初始化
#Board("microbit","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("microbit","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

micro = MBWireless()

def handle(data):
  print("recve：{}".format(data))

micro.set_wireless_channel(7)           #设置无线频道为7
micro.open_wireless()                   #打开无线通信
#micro.close_wireless()                 #关闭无线通信
while True:
  micro.send_wireless("hello")         #通过无线通信发送xxx
  print("send str hello")
  time.sleep(0.1)

#micro.recv_data(handle)                 #接收数据，并执行handle
#while True:
#  time.sleep(1)



