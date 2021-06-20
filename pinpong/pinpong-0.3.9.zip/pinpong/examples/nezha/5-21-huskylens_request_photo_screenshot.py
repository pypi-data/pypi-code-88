# -*- coding: utf-8 -*-

#NeZha
#实验效果：触发拍照/截图保存至SD卡

import time
from pinpong.board import Board
from pinpong.libs.dfrobot_huskylens import Huskylens

Board("nezha").begin()  #初始化，选择板型和端口号，不输入端口号则进行自动识别

husky = Huskylens()


#husky.command_request_knock()
#       Header	Header 2	Address	  Data Length	Command	 Checksum
#return 0x55	0xAA	    0x11	      0x00	    0x2E	 0x3E

husky.command_request_photo() #保存照片
time.sleep(2)


husky.command_request_screenshot() #保存截图
time.sleep(2)




