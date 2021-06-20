# -*- coding: utf-8 -*-
import time
from pinpong.board import Board,Pin

ip = "192.168.1.116"
port = 8081

Board(ip, port)

btn = Pin(Pin.D8, Pin.IN)

def btn_rasing_handler(pin):#中断事件回调函数
  print("\n--rising---")
  print("pin = ", pin)
  
def btn_falling_handler(pin):#中断事件回调函数
  print("\n--falling---")
  print("pin = ", pin)

def btn_both_handler(pin):#中断事件回调函数
  print("\n--both---")
  print("pin = ", pin)

btn.irq(trigger=Pin.IRQ_FALLING, handler=btn_falling_handler) #设置中断模式为下降沿触发
#btn.irq(trigger=Pin.IRQ_RISING, handler=btn_rasing_handler) #设置中断模式为上升沿触发，及回调函数
#btn.irq(trigger=Pin.IRQ_RISING+Pin.IRQ_FALLING, handler=btn_both_handler) #设置中断模式为电平变化时触发

while True:
  time.sleep(1)
