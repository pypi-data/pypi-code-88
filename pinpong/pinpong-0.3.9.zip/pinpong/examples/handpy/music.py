# -*- coding: utf-8 -*-

import time
from pinpong.board import Board, Music

Board("handpy").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("handpy","COM36").begin()   #windows下指定端口初始化
#Board("handpy","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("handpy","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

esp32 = Music()

esp32.music_set_tempo(4,60)                         #设置每一拍等同于4分音符，每分钟节拍数
# 音符C/C3、D/D3、E/E3、F/F3、G/G3、A/A3、B/B3、C/C4、D/D4、E/E4、F/F4、G/G4、A/A4、B/B4、C/C5、D/D5、E/E5、F/F5、G/G5、A/A5、B/B5
# C#/C#3、D#/D#3、F#/F#3、G#/G#3、A#/A#3、C#/C#4、D#/D#4、F#/F#4、G#/G#4、A#/A#4、C#/C#5、D#/D#5、F#/F#5、G#/G#5、A#/A#5
#节拍1、0.5、0.25、2/4
esp32.set_buzzer_freq("F/F3", 1)                    #播放"F/F3"音符，1节拍
time.sleep(2)
esp32.background_set_buzzer_freq("C/C3")            #后台播放音符
time.sleep(2)                 
esp32.stop_background_buzzer_freq()                 #停止后台播放











