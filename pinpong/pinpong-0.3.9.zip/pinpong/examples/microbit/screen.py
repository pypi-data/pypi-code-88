# -*- coding: utf-8 -*-

import time
from pinpong.board import Board
from pinpong.extension.microbit import MBScreen

Board("microbit").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("microbit","COM36").begin()   #windows下指定端口初始化
#Board("microbit","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("microbit","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

microbit = MBScreen()
#heart,heart_small,arrow_n,arrow_s,arrow_w,arrow_e,arrow_ne,arrow_nw,arrow_se,arrow_sw,yes,no
#happy,sad,angry,silly,smile,asleep,square,square_small,triangle,triangle_left,diamond_small
#music_crotchet,music_quaver,music_quavers,clock1,clock2,clock3,clock4,clock5,clock6,clock7
#clock8,clock9,clock10,clock11,clock12,skull,butterfly,chessboard,confused,cow,diamond,duck,
#fabulous,chost,giraffe,house,meh,pacman,pitchfork,rabbit,rollerskate,snake,stickfigure
#surprised,sword,tagget,tortoise,tshirt,umbrella,xmas
microbit.show_shape("heart")                 #显示图案
#microbit.show_font("hello world")           #显示字符串
#microbit.control_light_on(0,0)              #点亮坐标x,y的灯
#microbit.control_light_off(0,0)             #熄灭坐标x,y的灯
#microbit.set_light_brightness(1)            #设置灯的亮度
#microbit.hide_all_lights()                  #关闭所有点阵
while True:
    pass



