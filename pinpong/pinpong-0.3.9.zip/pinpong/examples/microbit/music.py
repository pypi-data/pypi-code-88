# -*- coding: utf-8 -*-

import time
from pinpong.board import Board,Pin
from pinpong.extension.microbit import MBMusic

Board("microbit").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("microbit","COM36").begin()   #windows下指定端口初始化
#Board("microbit","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("microbit","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

microbit = MBMusic()
#接口播放音乐：DADADADUM、ENTERTAINER、PRELUDE、ODE、NYAN、RINGTONE、FUNK、BLUES、BIRTHDAY、WEDDING、FUNERAL、PUNCHLINE、BADDY
#CHASE、BA_DING、WAWAWAWAA、JUMP_UP、JUMP_DOWN、POWER_UP、POWER_DOWN
microbit.play_music_background(Pin.P0, "DADADADUM")   #后台播放音乐
#microbit.play_music_until_end(Pin.P0, "DADADADUM")    #播放音乐直到结束
# 音符C/C3、D/D3、E/E3、F/F3、G/G3、A/A3、B/B3、C/C4、D/D4、E/E4、F/F4、G/G4、A/A4、B/B4、C/C5、D/D5、E/E5、F/F5、G/G5、A/A5、B/B5
# C#/C#3、D#/D#3、F#/F#3、G#/G#3、A#/A#3、C#/C#4、D#/D#4、F#/F#4、G#/G#4、A#/A#4、C#/C#5、D#/D#5、F#/F#5、G#/G#5、A#/A#5
#节拍1、0.5、0.25、2、4
#microbit.play_buzzer_freq(Pin.P0, "F/F3", 2)
#microbit.change_speed(100)                                #将声音速度增加 x
#microbit.set_speed(220)                                   #设置声音速度为 x
#print(microbit.get_speed())                               #获取声音速度
