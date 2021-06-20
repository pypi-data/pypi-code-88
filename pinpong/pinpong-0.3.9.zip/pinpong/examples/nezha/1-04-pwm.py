# -*- coding: utf-8 -*-

#Nezha
#实验效果：使用按钮控制LED模块亮度

import time
from pinpong.board import Board,Pin,PWM

Board("nezha").begin()

pwm0 = PWM(Pin(3)) #将Pin传入PWM中实现模拟输出

pwm0.freq(1000)

while True:
  for i in range(0,100): #占空比从0%到100%循环
    pwm0.duty(i)  #设置模拟输出值
    print(i)
    time.sleep(0.1)
