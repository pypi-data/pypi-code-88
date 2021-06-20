# -*- coding: utf-8 -*-

import os
import sys, getopt
import json
import time
import serial
import platform
import serial.tools.list_ports
import subprocess

from pinpong.base.avrdude import *
from pinpong.base import pymata4
from pinpong.base.comm import *

from pinpong.extension.globalvar import *

try:
  import smbus
  import spidev
except:
  pass

try:
  import RPi.GPIO as GPIO
except:
  pass

gboard = None

def get_pin(board,vpin):
  if board.boardname in ["UNO", "LEONARDO", "MEGA2560"]:
    dpin = vpin if vpin<20 else (vpin-100+14) if vpin >= 100 else -1
    apin = vpin-100 if vpin >= 100 else -1
  else:
    dpin=apin=vpin
  return dpin,apin

class DuinoPin:
  def __init__(self, board=None, pin=None, mode=None):
    self.mode = mode
    self.board = board
    self.pin,self.apin = get_pin(self.board, pin)
    
    if(mode == Pin.OUT):
      self.board.board.set_pin_mode_digital_output(self.pin)
    elif(mode == Pin.IN):
      self.board.board.set_pin_mode_digital_input(self.pin, callback=None)
    elif(mode == Pin.PWM):#为了支持面向过程的4个API而设计的此选项，尽量避免使用,使用PWM类代替
      self.board.board.set_pin_mode_pwm_output(self.pin)
    elif(mode == Pin.ANALOG):#为了支持面向过程的4个API而设计的此选项，尽量避免使用，使用ADC类代替
      if board.boardname in ["HANDPY", "MICROBIT"]:
        self.board.board.set_pin_analog_input(self.apin, None)
      else:
        self.board.board.set_pin_mode_analog_input(self.apin, None)

  def value(self, v = None):
    if v == None:  #Read
      if self.mode == Pin.OUT:
        return self.val
      else:
        if self.pin == None:
          return
        self.val = self.board.board.digital_read(self.pin)
        return self.val
    else:  #Write
      self.val = v
      if(self.pin == None):
        return
      self.board.board.digital_pin_write(self.pin, v)
      time.sleep(0.001)

  def on(self):
    self.val = 1
    if self.pin == None:
      return
    self.board.board.digital_pin_write(self.pin, 1)

  def off(self):
    self.val = 0
    if(self.pin == None):
      return
    self.board.board.digital_pin_write(self.pin, 0)

  def irq(self, trigger, handler):
    self.board.board.set_pin_mode_digital_input(self.pin, None)
    self.board.board.set_digital_pin_params(self.pin, trigger, handler)
  
  #这5个函数将打破原有的面向对象规则，请慎用
  #建议使用value方法 PWM和ADC类来替代这5个函数 
  def write_analog(self, duty):
    self.duty=duty
    self.freq=100
    if self.board.boardname in ["UNO", "LEONARDO"]:
      real_duty = int(self.duty / 255 * 100)
      real_duty = 255 if real_duty>255 else real_duty
      self.board.board.pwm_write(self.pin, self.freq, real_duty)
    else:
      self.board.board.dfrobot_pwm_write(self.pin, self.freq, self.duty)

  def write_digital(self, value):
    self.val = value
    if(self.pin == None):
      return
    self.board.board.digital_pin_write(self.pin, value)

  def read_digital(self):
    if(self.pin == None):
      return
    self.val = self.board.board.digital_read(self.pin)
    return self.val

  def read_analog(self):
    return self.board.board.analog_read(self.apin)

  def pin_mode(self, mode):
    if(mode == Pin.OUT):
      self.board.board.set_pin_mode_digital_output(self.pin)
    elif(mode == Pin.IN):
      self.board.board.set_pin_mode_digital_input(self.pin, callback=None)

class RPiPin:
  def __init__(self, board=None, pin=None, mode=None):
    self.board = board
    if(pin == None):
      self.pin = None
      return

    self.pin = pin
    self.mode = mode
    if(mode == Pin.OUT):
      GPIO.setup(self.pin, GPIO.OUT)
    elif(mode == Pin.IN):
      GPIO.setup(self.pin, GPIO.IN)
    elif(mode == Pin.PWM):#为了支持面向过程的4个API而设计的此选项，尽量避免使用,使用PWM类代替
      GPIO.setup(self.pin, GPIO.OUT)
      self.pwm=GPIO.PWM(self.pin, 1000)

  def value(self, v = None):
    if v == None:  #Read
      if self.mode == Pin.OUT:
        return self.val
      else:
        if self.pin == None:
          return
        self.val = GPIO.input(self.pin)
        return self.val
    else:  #Write
      self.val = v
      if(self.pin == None):
        return
      GPIO.output(self.pin,v)

  def on(self):
    self.val = 1
    if self.pin == None:
      return
    GPIO.output(self.pin, GPIO.HIGH)

  def off(self):
    self.val = 0
    if(self.pin == None):
      return
    GPIO.output(self.pin, GPIO.LOW)

  def irq(self, trigger, handler):
    OFFSET = 30                                   #30是偏移量
    GPIO.add_event_detect(self.pin, OFFSET+trigger)
    GPIO.add_event_callback(self.pin, handler)
    #GPIO.add_event_detect(self.pin, 30+trigger, callback=handler)
  
  #这5个函数将打破原有的面向对象规则，请慎用
  #建议使用value方法 PWM和ADC类来替代这5个函数 
  def write_analog(self, duty):
    self.duty=duty
    self.pwm.start(duty)

  def write_digital(self, value):
    self.val = value
    if(self.pin == None):
      return
    GPIO.output(self.pin, value)

  def read_digital(self):
    if(self.pin == None):
      return
    self.val = GPIO.input(self.pin)
    return self.val

  def pin_mode(self, mode):
    if(mode == Pin.OUT):
      GPIO.setup(self.pin, GPIO.OUT)
    elif(mode == Pin.IN):
      GPIO.setup(self.pin, GPIO.IN)

class SYSFSPin:
  def __init__(self, board=None, pin=None, mode=None):
    self.board = board
    if(pin == None):
      self.pin = None
      return
    
    self.pin = pin
    self.mode = mode
    self.export_path = '/sys/class/gpio/export'
    self.value_path = '/sys/class/gpio/gpio'+str(self.pin)+'/value'
    self.direction_path = '/sys/class/gpio/gpio'+str(self.pin)+'/direction'

    if not os.path.exists('/sys/class/gpio/gpio'+str(self.pin)):
      os.system('echo '+str(self.pin)+' > '+self.export_path)

    if(mode == Pin.OUT):
      os.system('echo out > ' + self.direction_path)
    elif(mode == Pin.IN):
      os.system('echo in > ' + self.direction_path)

  def value(self, v = None):
    if v is None:  #Read
      if self.mode == Pin.OUT:
        return self.val
      else:
        if self.pin is None:
          return
        with open(self.value_path) as f:
          self.val = int(f.read())  
        return self.val
    else:  #Write
      self.val = v
      if(self.pin == None):
        return
      os.system("echo "+str(v)+" > " + self.value_path)

  def on(self):
    self.val = 1
    if self.pin is None:
      return
    os.system("echo 1 > " + self.value_path)

  def off(self):
    self.val = 0
    if(self.pin == None):
      return
    os.system("echo 0 > " + self.value_path)

  def irq(self, trigger, handler):
    pass
    #GPIO.add_event_detect(self.pin, 30+trigger)
    #GPIO.add_event_callback(self.pin, handler)
    #GPIO.add_event_detect(self.pin, 30+trigger, callback=handler)
  #这5个函数将打破原有的面向对象规则，请慎用
  #建议使用value方法 PWM和ADC类来替代这5个函数 
  def write_analog(self, duty):
    self.duty=duty
    self.pwm.start(duty)

  def write_digital(self, val):
    self.val = val
    if(self.pin == None):
      return
    self.value(val)

  def read_digital(self):
    if(self.pin == None):
      return
    if self.mode == Pin.OUT:
        return self.val
    else:
      if self.pin is None:
        return
      with open(self.value_path) as f:
        self.val = int(f.read())  
      return self.val

  def pin_mode(self, mode):
    if(mode == Pin.OUT):
      os.system('echo out > ' + self.direction_path)
    elif(mode == Pin.IN):
      os.system('echo in > ' + self.direction_path)

class Pin:
  D0 = 0
  D1 = 1
  D2 = 2
  D3 = 3
  D4 = 4
  D5 = 5
  D6 = 6
  D7 = 7
  D8 = 8
  D9 = 9
  D10 = 10
  D11 = 11
  D12 = 12
  D13 = 13
  D14 = 14
  D15 = 15
  D16 = 16
  D17 = 17
  D18 = 18
  D19 = 19
  D20 = 20
  D21 = 21
  D22 = 22
  D23 = 23
  D24 = 24
  D25 = 25
  D26 = 26
  D27 = 27
  D28 = 28
  D29 = 29
  D30 = 30
  D31 = 31
  D32 = 32
  D33 = 33
  D34 = 34
  D35 = 35
  D36 = 36
  D37 = 37
  D38 = 38
  D39 = 39
  D40 = 40
  D41 = 41
  D42 = 42
  D43 = 43
  D44 = 44
  D45 = 45
  D46 = 46
  D47 = 47
  D48 = 48
  D49 = 49
  D50 = 50
  D51 = 51
  D52 = 52
  
  A0 = 100
  A1 = 101
  A2 = 102
  A3 = 103
  A4 = 104
  A5 = 105
  A6 = 106
  A7 = 107

  P0 = 0
  P1 = 1
  P2 = 2
  P3 = 3
  P4 = 4
  P5 = 5
  P6 = 6
  P7 = 7
  P8 = 8
  P9 = 9
  P10 = 10
  P11 = 11
  P12 = 12
  P13 = 13
  P14 = 14
  P15 = 15
  P16 = 16
  P17 = 17
  P18 = 18
  P19 = 19
  P20 = 20
  
  OUT = 0
  IN = 1
  IRQ_FALLING = 2
  IRQ_RISING = 1
  IRQ_DRAIN = 7
  PULL_DOWN = 1
  PULL_UP = 2
  PWM     = 0x10
  ANALOG  = 0x11
  nezha_pinmap = [None,33,32,118,40,41,2027,37,   2020,44,2021,2022,108,109,2024,107,    106,2023,110,2025,111,65,38,2026,    35,36]

  def __init__(self, board=None, pin=None, mode=None):
    if isinstance(board, int):#兼容面向过程的4个api
      mode = pin
      pin = board
      board = gboard

    if board == None:
      board = gboard

    self.board = board
    if(pin == None):
      self.pin = None
      return

    self.pin,self.apin = get_pin(self.board, pin)
    self.mode = mode
    if self.board.boardname == "RPI":#RPi
      self.obj = RPiPin(board, pin, mode)
    elif self.board.boardname == "NEZHA":#NEZHA
      if pin == 0 or pin >= len(self.nezha_pinmap):
        raise ValueError("pin must in[%d,%d]",1,len(self.nezha_pinmap)-1)
      self.obj = SYSFSPin(board,self.nezha_pinmap[pin],mode)
    else:
      self.obj = DuinoPin(board, pin,mode)

  def value(self, v = None):
    if v == None:  #Read
      return self.obj.value(v)
    else:  #Write
      self.obj.value(v)
      time.sleep(0.001)

  def on(self):
    self.val = 1
    if self.pin == None:
      return
    self.obj.on()

  def off(self):
    self.val = 0
    if(self.pin == None):
      return
    self.obj.off()

  def irq(self, trigger, handler):
    self.obj.irq(trigger, handler)

  #这5个函数将打破原有的面向对象规则，请慎用
  #建议使用value方法 PWM和ADC类来替代这5个函数
  def write_analog(self, duty):
    self.obj.write_analog(duty)

  def write_digital(self, value):
    self.obj.write_digital(value)

  def read_digital(self):
    return self.obj.read_digital()

  def read_analog(self):
    return self.obj.read_analog()

  def pin_mode(self, mode):
    self.obj.pin_mode(mode)

class DuinoADC:
  def __init__(self, board=None, pin_obj=None):
    if isinstance(board, Pin):
      pin_obj = board
      board = gboard
    elif board == None:
      board = gboard
    
    self.board = board
    self.pin_obj = pin_obj
    #MICROBIT HANDPY 使用协议 F0 xx(PIN) 02 DF私有Firamata协议
    #UNO使用标准的Firmata协议
    if board.boardname in ["HANDPY", "MICROBIT"]:
      self.board.board.set_pin_analog_input(self.pin_obj.apin, None)
    else:
      self.board.board.set_pin_mode_analog_input(self.pin_obj.apin, None)

  def read(self):
    return self.board.board.analog_read(self.pin_obj.apin)
    
class ADC:
  def __init__(self, board=None, pin_obj=None):
    if isinstance(board, Pin):
      pin_obj = board
      board = gboard
    elif board == None:
      board = gboard
    
    self.board = board
    self.pin_obj = pin_obj
    self.obj = DuinoADC(board, pin_obj)

  def read(self):
    return self.obj.read()

class DuinoPWM:
  def __init__(self, board, pin_obj):
    self.board = board
    self.pin_obj = pin_obj
    self.freq_value = 100
    self.duty_value = 50
    self.board.board.set_pin_mode_pwm_output(self.pin_obj.pin)

  def freq(self, v=None):
    if v == None:
      return self.freq_value
    else:
      self.freq_value = v
    #f4（设置引脚模式） 04（引脚） 03（设置引脚模式为PWM模式）
    #e4（设置4号引脚的信息） 10（占空比：16%） 01（频率7~9位） 7f（频率0~6位） 
    if self.board.boardname in ["UNO", "LEONARDO"]:
      real_duty = int(self.duty_value / 255 * 100)
      real_duty = 255 if real_duty>255 else real_duty
      self.board.board.pwm_write(self.pin_obj.pin, self.freq_value, real_duty)
    else:
      self.board.board.dfrobot_pwm_write(self.pin_obj.pin, self.freq_value, self.duty_value)

  def duty(self, v=None):
    if v == None:
      return self.duty_value
    else:
      self.duty_value = v
    if self.board.boardname in ["UNO", "LEONARDO"]:
      real_duty = int(self.duty_value / 255 * 100)
      real_duty = 255 if real_duty>255 else real_duty
      self.board.board.pwm_write(self.pin_obj.pin, self.freq_value, real_duty)
    else:
      self.board.board.dfrobot_pwm_write(self.pin_obj.pin, self.freq_value, self.duty_value)

  def deinit(self):
    self.board.pin_obj.pin_mode(Pin.IN)

class RPiPWM:
  def __init__(self, board, pin_obj):
    self.pin_obj = pin_obj
    self.freq_value = 100
    self.duty_value = 50

    GPIO.setup(self.pin_obj.pin, GPIO.OUT)
    self.pwm = GPIO.PWM(self.pin_obj.pin, self.freq_value)
    #self.pwm.start(duty)
    self.isStart = False

  def freq(self, v=None):
    if v == None:
      return self.freq_value
    else:
      self.freq_value = v
      if v == 0:
        self.pwm.stop()
        self.isStart = False
      else:
        self.pwm.start(self.duty_value)
        self.pwm.ChangeFrequency(self.freq_value)
        self.isStart = True

  def duty(self, v=None):
    if v == None:
      return self.duty_value
    else:
      self.duty_value = v
    self.pwm.ChangeDutyCycle(self.duty_value)

  def deinit(self):
    self.pwm.stop()


class NeZhaPWM:
  def __init__(self, board, pin_obj):
    self.pin_obj = pin_obj
    self.freq_value = 100
    self.duty_value = 50
    self.period_ns = 10000000
    if self.pin_obj.pin not in [3]:
      raise ValueError("pin must in [%d]"%3)

    self.export_path = '/sys/class/pwm/pwmchip0/export'
    self.period_path = '/sys/class/pwm/pwmchip0/pwm7/period'
    self.duty_path = '/sys/class/pwm/pwmchip0/pwm7/duty_cycle'
    self.enable_path = '/sys/class/pwm/pwmchip0/pwm7/enable'

    os.system('echo 118 > /sys/class/gpio/unexport')
    if not os.path.exists('/sys/class/pwm/pwmchip0/pwm7'):
      os.system('echo 7 > '+self.export_path)
    self.isStart = False

  def freq(self, v=None):
    if v == None:
      return self.freq_value
    else:
      if v == 0:
        os.system('echo 0 > /sys/class/pwm/pwmchip0/pwm7/enable')
        self.isStart = False
        return
      self.freq_value = v
      self.period_ns = int(1000000000/self.freq_value)
      #print('echo '+str(self.period_ns)+' > /sys/class/pwm/pwmchip0/pwm7/period')
      os.system('echo '+str(self.period_ns)+' > /sys/class/pwm/pwmchip0/pwm7/period')

      if self.isStart == False:
        #print('echo 1 > /sys/class/pwm/pwmchip0/pwm7/enable')
        os.system('echo 1 > /sys/class/pwm/pwmchip0/pwm7/enable')
        self.isStart = True

  def duty(self, v=None):
    if v == None:
      return self.duty_value
    else:
      self.duty_value = v
      duty_ns = int(self.period_ns*(100-self.duty_value)/100.0)
      #print('echo '+str(duty_ns)+' > '+self.duty_path)
      os.system('echo '+str(duty_ns)+' > '+self.duty_path)
      if self.isStart == False:
        #print('echo 1 > /sys/class/pwm/pwmchip0/pwm7/enable')
        os.system('echo 1 > /sys/class/pwm/pwmchip0/pwm7/enable')
        self.isStart = True

  def deinit(self):
    os.system('echo 0 > /sys/class/pwm/pwmchip0/pwm7/enable')
    self.isStart = False

class PWM:
  def __init__(self, board=None, pin_obj=None):
    if isinstance(board, Pin):
      pin_obj = board
      board = gboard
    elif board == None:
      board = gboard

    self.board = board
    self.pin_obj = pin_obj

    if self.board.boardname == "RPI":#RPi
      self.obj = RPiPWM(board, pin_obj)
    elif self.board.boardname == "NEZHA":#RPi
      self.obj = NeZhaPWM(board, pin_obj)
    else:
      self.obj = DuinoPWM(board, pin_obj)

  def freq(self, v=None):
    if v == None:
      return self.obj.freq(v)
    else:
      self.obj.freq(v)

  def duty(self, v=None):
    if v == None:
      return self.obj.duty(v)
    else:
      self.obj.duty(v)

  def deinit(self):
    self.obj.deinit()

class DuinoSPI:
  def __init__(self, board, device_num=0, bus_num = 0, baudrate=10000):
    self.board = board
    self.device_num = device_num
    self.board.board.set_pin_mode_spi(device_num)

  def read(self, length, default_value=0xff):
    ret = self.board.board.spi_readbytes(self.device_num, length)
    return ret

  def readinto(self, buf):
    length = len(buf)
    buf=self.board.spi_read(self.device_num, length)

  def write(self, buf): #write some bytes on MOSI
    self.board.board.xfer3(buf)

  def write_readinto(self, wbuf, rbuf): # write to MOSI and read from MISO into the buffer
    rbuf=self.board.board.xfer3(wbuf)

class SoftSPI:
  def __init__(self, board, sck, mosi, miso, baudrate=100000, polarity=0, phase=0, bits=8):
    self.board = board
    self.mosi = mosi
    self.miso = miso
    self.sck = sck
    self.phase = phase
    self.mosi.value(0)
    self.sck.value(polarity)

  def read(self, num, default_value=0xff):
    ret = bytearray(num)
    for i in range (num):
      ret[i] = self._transfer(default_value)
    return ret

  def readinto(self, buf):
    num = len(buf)
    buf=self.read(num)

  def write(self, buf): #write some bytes on MOSI
    num = len(buf)
    for i in range (num):
      self._transfer(buf[i])

  def write_readinto(self, wbuf, rbuf): # write to MOSI and read from MISO into the buffer
    num = len(wbuf)
    for i in range (num):
      rbuf[i] = self._transfer(wbuf[i])

  def _transfer(self,data):
    ret = 0
    for i in range(8):
      self.mosi.value(1 if data&0x80 else 0)
      self.sck.value(0 if self.sck.value() else 1) #这样书写兼容了MODE0 和 MODE3
      self.sck.value(0 if self.sck.value() else 1)
      if self.miso:
        ret= ret<<1 + self.miso.value()
      data <<= 1
    return ret

class RPiSPI:
  def __init__(self, device_num=0, baudrate=31200000):
    self.spi = spidev.SpiDev(0, device_num)
    self.spi.open(0, device_num)
    self.spi.max_speed_hz = baudrate

  def read(self, num, default_value=0xff):
    ret = self.spi.readbytes(num)
    return ret

  def readinto(self, buf):
    num = len(buf)
    buf=self.read(num)

  def write(self, buf): #write some bytes on MOSI
    self.spi.xfer3(buf)

  def write_readinto(self, wbuf, rbuf): # write to MOSI and read from MISO into the buffer
    num = len(wbuf)

class SPI:
  # spi四种模式SPI的相位(CPHA)和极性(CPOL)分别可以为0或1，对应的4种组合构成了SPI的4种模式(mode)
  # Mode 0 CPOL=0, CPHA=0  ->  第一个跳变，即上升沿采样
  # Mode 1 CPOL=0, CPHA=1  ->  第二个跳变，即下降沿采样
  # Mode 2 CPOL=1, CPHA=0  ->  第一个跳变，即下降沿采样
  # Mode 3 CPOL=1, CPHA=1  ->  第二个跳变，即上升沿采样
  # 时钟极性CPOL: 即SPI空闲时，时钟信号SCLK的电平 (1:空闲时高电平; 0:空闲时低电平)
  # 时钟相位CPHA: 即SPI在SCLK第几个边沿开始采样 (0:第一个边沿开始; 1:第二个边沿开始)
  # 默认设置为MODE 0 因为大部分的外设使用的是MODE 0
  def __init__(self, board=None, device_num=0, bus_num=0, sck=None, mosi=None, miso=None, cs=None, baudrate=100000, polarity=0, phase=0, bits=8):
    if isinstance(board, int):
      device_num = board
      bus_num = device_num
      board = gboard
    elif board == None:
      board = gboard
    self.board = board

    if self.board.spi[device_num] == None:
      if mosi:  #SoftSPI
        self.board.spi[device_num] = SoftSPI(board, sck, mosi, miso, cs, baudrate, polarity, phase, bits)
      elif self.board.boardname == "RPI":  #RPiSPI
        self.board.spi[device_num] = RPiSPI(device_num)
      else:  #DuinoSPI
        self.board.spi[device_num] = DuinoSPI(self, device_num, bus_num)
    self.obj = self.board.spi[device_num]

  def read(self, num, default_value=0xff):
    return self.obj.read(num, default_value)

  def readinto(self, buf):
    self.obj.readinto(buf)

  def write(self, buf): #write some bytes on MOSI
    self.obj.write(buf)

  def write_readinto(self, wbuf, rbuf): # write to MOSI and read from MISO into the buffer
    self.obj.writeinto(wbuf, rbuf)

class DuinoI2C:
  def __init__(self, board, bus_num):
    self.board = board
    self.board.board.set_pin_mode_i2c()

  def scan(self):
    plist = self.board.board.i2c_scan()
    return plist

  def writeto(self, i2c_addr, value):
    self.board.board.i2c_write(i2c_addr, value)

  def readfrom(self, i2c_addr, read_byte):
    return self.board.board.i2c_addr_read(i2c_addr, read_byte)

  def readfrom_mem(self, i2c_addr, reg, read_byte):
    return self.board.board.i2c_read(i2c_addr, reg, read_byte, None)

  def readfrom_mem_restart_transmission(self, i2c_addr, reg, read_byte):
    return self.board.board.i2c_read_restart_transmission(i2c_addr, reg, read_byte, None)

  def writeto_mem(self, i2c_addr, reg, value):
    if isinstance(reg,(list)):
        self.board.board.i2c_write(i2c_addr, reg+list(value))
    else:
        self.board.board.i2c_write(i2c_addr, [reg]+list(value))

class SMBUS:
  def __init__(self, board, bus_num):
    self.bus_num = bus_num
    self.i2c = smbus.SMBus(bus_num)

  def scan(self):
    plist=[]
    for i in range(127):
      try:
        self.i2c.write_quick(i)
        plist.append(i)
      except Exception as e:
        pass
    return plist

  def writeto(self, i2c_addr, value):
    if len(value) == 1:
      self.i2c.write_byte(i2c_addr, value[0])
    else:
      self.i2c.write_i2c_block_data(i2c_addr, value[0], list(value[1:]))

  def readfrom(self, i2c_addr, read_byte):
    if read_byte == 1:
      return self.i2c.read_byte(i2c_addr)
    else:
      pass
 
  def readfrom_mem(self, i2c_addr, reg, read_byte):
    return self.i2c.read_i2c_block_data(i2c_addr, reg, read_byte)

  def readfrom_mem_restart_transmission(self, i2c_addr, reg, read_byte):
    return self.i2c.read_i2c_block_data(i2c_addr, reg, read_byte)

  def writeto_mem(self, i2c_addr, reg, value):
    self.i2c.write_i2c_block_data(i2c_addr, reg, list(value))

class I2C:
  def __init__(self, board=None, bus_num=0):
    if isinstance(board, int):
      bus_num = board
      board = gboard
    elif board == None:
      board = gboard

    if board.boardname in board.i2c_fixed:
      bus_num = board.i2c_fixed[board.boardname]

    self.board = board
    if self.board.i2c[bus_num] == None:
      self.bus_num = bus_num
      if self.board.boardname in ["RPI","NEZHA"]:
        self.board.i2c[bus_num] = SMBUS(board, bus_num)
      else:
        self.board.i2c[bus_num] = DuinoI2C(board, bus_num)
    self.obj = self.board.i2c[bus_num]

  def scan(self):
    return self.obj.scan()

  def writeto(self, i2c_addr, value):
    self.obj.writeto(i2c_addr, value)

  def readfrom(self, i2c_addr, read_byte):
    return self.obj.readfrom(i2c_addr, read_byte)

  def readfrom_mem(self, i2c_addr, reg, read_byte):
    return self.obj.readfrom_mem(i2c_addr, reg, read_byte)

  def readfrom_mem_restart_transmission(self, i2c_addr, reg, read_byte):
    return self.obj.readfrom_mem_restart_transmission(i2c_addr, reg, read_byte)

  def writeto_mem(self, i2c_addr, reg, value):
    return self.obj.writeto_mem(i2c_addr, reg, value)

class DuinoUART:
  def __init__(self, board, bus_num, baud_rate):
    self.bus_num = bus_num
    self.board = board
    self.board.board.set_pin_mode_uart(bus_num, baud_rate)

  def writechar(self,data):
    return self.board.board.uart_write(self.bus_num,[data])

  def write(self, data):
    self.board.board.uart_write(self.bus_num, data)

  def readchar(self):
    return self.board.board.uart_readchar(self.bus_num)

  def readall(self):
    return self.board.board.uart_readall(self.bus_num)

  def readline(self):
    return self.board.board.uart_readline(self.bus_num)

  def read(self, n):
    return self.board.board.uart_read(self.bus_num, n)

  def readinto(self, buf):
    return self.board.board.uart_readinto(self.bus_num, buf)

  def any(self):
    return self.board.board.uart_any(self.bus_num)

class UART:
  def __init__(self, board=None, bus_num=0, baud_rate=9600):
    if isinstance(board, int):
      baud_rate = bus_num
      bus_num = board
      board = gboard
    elif board == None:
      board = gboard
    
    self.board = board
    if self.board.uart[bus_num] == None:
      self.bus_num = bus_num
      if self.board.boardname == "RPI":
        self.board.uart[bus_num] = RPiUART(board, bus_num, baud_rate)
      else:
        self.board.uart[bus_num] = DuinoUART(board, bus_num, baud_rate)
    self.obj = self.board.uart[bus_num]

  def writechar(self,data):
    return self.obj.writechar(data)

  def write(self, data):
    self.obj.write(data)

  def readchar(self):
    return self.obj.readchar()

  def readall(self):
    return self.obj.readall()

  def readline(self):
    return self.obj.readline()

  def read(self, n):
    return self.obj.read(n)

  def readinto(self, buf):
    return self.obj.readinto(buf)

  def any(self):
    return self.obj.any()


class RPiIRRecv:
  def __init__(self, board, pin_obj):
    self.pin_obj = pin_obj

  def read(self):
    return None

class DuinoIRRecv:
  def __init__(self, board, pin_obj,callback):
    self.board = board
    self.pin_obj = pin_obj
    self.board.board.set_pin_mode_ir_recv(self.pin_obj.pin, callback)

  def read(self):
    return self.board.board.ir_read(self.pin_obj.pin)


class IRRecv:
  def __init__(self, board=None, pin_obj=None, callback=None):
    if isinstance(board, Pin):
      callback = pin_obj
      pin_obj = board
      board = gboard
    elif board == None:
      board = gboard
    
    self.board = board
    if self.board.boardname == "RPI":
      self.obj = RPiIRRecv(board, pin_obj, callback)
    else:
      self.obj = DuinoIRRecv(board, pin_obj, callback)

  def read(self):
    return self.obj.read()


class RPiIRRemote:
  def __init__(self, board, pin_obj):
    self.pin_obj = pin_obj

  def send(self, value):
    return None

class DuinoIRRemote:
  def __init__(self, board, pin_obj,callback=None):
    self.board = board
    self.pin_obj = pin_obj
#    self.board.board.set_pin_mode_ir_recv(self.pin_obj.pin, callback)

  def send(self, value):
    value &= 0xFFFF
    a = bin(value)[2:]
    c = str.zfill(a, 16)
#    print(c)
    head = '0b'
    tmp = ''
    for i in range(len(c)-1, -1, -1):
        tmp += c[i]
    values = head + tmp
    value = eval(values)
#    print(value)
    value |= 0x00 << 24
    value |= 0xFD << 16
    return self.board.board.ir_send(self.pin_obj.pin, value)

class IRRemote:
  def __init__(self, board=None, pin_obj=None):
    if isinstance(board, Pin):
      pin_obj = board
      board = gboard
    elif board == None:
      board = gboard
    
    self.board = board
    if self.board.boardname == "RPI":
      self.obj = RPiIRRemote(board, pin_obj)
    else:
      self.obj = DuinoIRRemote(board, pin_obj)

  def send(self, value):
    return self.obj.send(value)


class RPiTone:
  def __init__(self, board, pin_obj):
    self.board = board
    self.pwm = PWM(pin_obj = pin_obj)
    self.freq_value = 0

  def on(self):
    self.pwm.freq(self.freq_value)

  def off(self):
    self.pwm.freq(0)

  def freq(self, v=None):
    if v == None:
      return self.freq_value
    else:
      self.freq_value = v
      self.pwm.freq(v)

  def tone(self, freq, duration):
#    self.pwm.play_tone(self.pin_obj.pin, freq, duration) 
     pass

class DuinoTone:
  def __init__(self, board, pin_obj):
    self.board = board
    self.pin_obj = pin_obj
    self.board.board.set_pin_mode_tone(self.pin_obj.pin)
    self.freq_value = 100
    
  def on(self):
    self.board.board.play_tone(self.pin_obj.pin, self.freq_value, 0)

  def off(self):
    self.board.board.play_tone(self.pin_obj.pin, 0, 0)

  def freq(self, v=None):
    if v == None:
      return self.freq_value
    else:
      self.freq_value = v

  def tone(self, freq, duration):
    self.board.board.play_tone(self.pin_obj.pin, freq, duration)

class Tone:
  def __init__(self, board=None, pin_obj=None):
    if isinstance(board, Pin):
      pin_obj = board
      board = gboard
    elif board == None:
      board = gboard

    self.board = board
    if self.board.boardname == "RPI":
      self.obj = RPiTone(board, pin_obj)
    else:
      self.obj = DuinoTone(board, pin_obj)
      
  def on(self):
    self.obj.on()

  def off(self):
    self.obj.off()

  def freq(self, v=None):
    if v == None:
      return self.obj.freq(v)
    else:
     self.obj.freq(v)

  def tone(self, freq, duration):
    self.obj.tone(freq=freq,duration=duration)

class RPiServo:
  def __init__(self, board, pin_obj):
    self.board = board
    self.pin_obj = pin_obj
    GPIO.setup(self.pin_obj.pin, GPIO.OUT)
    self.pwm=GPIO.PWM(self.pin_obj.pin, 50)
    self.pwm.start(0)

  def write_angle(self, value):
    self.angle(value)
    
  def angle(self, _angle):
    duty = int(_angle*(10.0/180.0)+2.5)
    self.pwm.ChangeDutyCycle(duty)
  
  def detach(self):
    self.pwm.stop()
    self.pwm = None
    GPIO.setup(self.pin_obj.pin, GPIO.IN)

class NeZhaServo:
  def __init__(self, board, pin_obj):
    self.board = board
    self.pin_obj = pin_obj
    self.pwm=NeZhaPWM(board, pin_obj)
    self.pwm.freq(50)

  def write_angle(self, value):
    self.angle(value)
    
  def angle(self, _angle):
    #duty_value = int(_angle*(10.0/180.0)+2.5)
    duty_value = _angle*(10.0/180.0)+2.5
    self.pwm.duty(duty_value)
  
  def detach(self):
    self.pwm.deinit()


class DuinoServo:
  def __init__(self, board, pin_obj):
    self.board = board
    self.pin_obj = pin_obj
    self.board.board.set_pin_mode_servo(self.pin_obj.pin)
    self.board.board.set_mode_servo(self.pin_obj.pin)

  def write_angle(self, value):
    self.angle(value)
  
  def angle(self, _angle):
    if self.board.boardname in ["HANDPY", "MICROBIT", "GD32V"]:
      if self.pin_obj.pin < 16:
        self.board.board.servo_write(self.pin_obj.pin, _angle)
      else:
        self.board.board.dfrobot_servo_write(self.pin_obj.pin, _angle)
    else:
      self.board.board.servo_write(self.pin_obj.pin, _angle)
  
  def detach(self):
    self.board.set_pin_mode_digital_input(self.pin_obj.pin, callback=None)

class Servo:
  def __init__(self, board=None, pin_obj=None):
    if isinstance(board, Pin):
      pin_obj = board
      board = gboard
    elif board == None:
      board = gboard
    
    self.board = board
    self.pin_obj = pin_obj
    if self.board.boardname == "RPI":
      self.obj = RPiServo(board, pin_obj)
    elif self.board.boardname == "NEZHA":
      self.obj = NeZhaServo(board,pin_obj)
    else:
      self.obj = DuinoServo(board, pin_obj)

  def write_angle(self, value):
    self.obj.write_angle(value)
  
  def angle(self, _angle):
    self.obj.angle(_angle)
  
  def detach(self):
    self.obj.detach()

class NeoPixel(object):
  def __init__(self, board=None, pin_obj=None, num=None):
    if isinstance(board, Pin):
      num = pin_obj
      pin_obj = board
      board = gboard
    elif board == None:
      board = gboard

    self.pin_obj  = pin_obj
    self.board = board
    self.num = num
    self.__data = [(0,0,0) for i in range(num)]
    #self.board.board.set_pin_mode_neo(self.pin_obj.pin)
    self.board.board.neopixel_config(self.pin_obj.pin,self.num)
    time.sleep(0.1)

  def __repr__(self):
    return 'pixel data (%s)' % self.__data
 
  def __getitem__(self, i):
    return self.__data[i]  # 返回data绑定列表中的第i个元素
 
  def __setitem__(self, i, v):
    #print(i,v)
    self.__data[i]=v
    self.write(i,v)

  def write(self , index, r, g=None, b=None):
    if isinstance(r,tuple):
      b=r[2]
      g=r[1]
      r=r[0]
    color = (r<<16) + (g<<8) + b
    self.board.board.neopixel_write(self.pin_obj.pin, index, color)

  def rainbow(self , start, end, hsv_start, hsv_end):
    self.board.board.neopixel_set_rainbow(self.pin_obj.pin, start, end, hsv_start, hsv_end)

  def shift(self , n):
    self.board.board.neopixel_shift(self.pin_obj.pin, n)

  def rotate(self , n):
    self.board.board.neopixel_rotate(self.pin_obj.pin, n)

  def range_color(self, start, end, color):
    self.board.board.neopixel_set_range_color(self.pin_obj.pin, start, end, color)
    
#  def bar_graph(self, start, end, numerator, denominator):
#    self.board.board.set_bar_graph(self.pin_obj.pin, start, end, numerator, denominator)

  def clear(self):
    self.board.board.neopixel_set_range_color(self.pin_obj.pin, 0, self.num-1, 0)

class DHT11:
  def __init__(self,board=None, pin_obj=None):
    if isinstance(board, Pin):
      pin_obj = board
      board = gboard
    elif board == None:
      board = gboard

    self.board = board
    self.pin_obj = pin_obj
    self.type = 11
    self.board.board.set_pin_mode_dht(self.pin_obj.pin, self.type, differential=.01)
    time.sleep(0.1)
    
  def measure(self):
    self.value = self.board.board.dht_read(self.pin_obj.pin)

  def temp_c(self):
    return self.board.board.dht_read(self.pin_obj.pin)[1]

  def humidity(self):
    return self.board.board.dht_read(self.pin_obj.pin)[0]

class DHT22:
  def __init__(self,board=None, pin_obj=None):
    if isinstance(board, Pin):
      pin_obj = board
      board = gboard
    elif board == None:
      board = gboard

    self.board = board
    self.pin_obj = pin_obj
    self.type = 22
    self.board.board.set_pin_mode_dht(self.pin_obj.pin, self.type, differential=.01)
    time.sleep(0.1)

  def measure(self):
    self.value = self.board.board.dht_read(self.pin_obj.pin)

  def temp_c(self):
    return self.board.board.dht_read(self.pin_obj.pin)[1]

  def humidity(self):
    return self.board.board.dht_read(self.pin_obj.pin)[0]

class SR04_URM10:
  def __init__(self,board=None, trigger_pin_obj=None, echo_pin_obj=None):
    if isinstance(board, Pin):
      echo_pin_obj = trigger_pin_obj
      trigger_pin_obj = board
      board = gboard
    elif board == None:
      board = gboard

    self.board  = board
    self.trigger_pin_obj = trigger_pin_obj
    self.echo_pin_obj = echo_pin_obj
    self.board.board.set_pin_mode_sonar(self.trigger_pin_obj.pin, self.echo_pin_obj.pin)

  def distance_cm(self):
    return self.board.board.sonar_read(self.trigger_pin_obj.pin)[0]

class DS18B20:
  def __init__(self, board=None, pin_obj=None):
    if isinstance(board, Pin):
      pin_obj = board
      board = gboard
    elif board == None:
      board = gboard
    
    self.board = board
    self.pin_obj = pin_obj
    self.board.board.set_pin_mode_DS18B20(self.pin_obj.pin)
    
  def temp_c(self):
    return self.board.board.ds18b20_read(self.pin_obj.pin)

class AudioAnalyzer :
  def __init__(self, board=None, strobe=None, RST=None, DC=None):
    if isinstance(board, int):
      strobe_pin = board
      RST_pin = strobe
      DC_pin = RST
      board = gboard
    elif board == None:
      board = gboard
    
    self.board = board
    self.strobe_pin = strobe_pin
    self.RST_pin = RST_pin
    self.DC_pin,self.DC_apin = get_pin(self.board, DC_pin)
    self.RST_pin,self.RST_apin = get_pin(self.board, RST_pin)
    self.strobe_pin,self.strobe_apin = get_pin(self.board, strobe_pin)
    self.board.board.set_audio_init(self.strobe_pin, self.RST_pin, self.DC_pin)
    
  def read_freq(self):
    return self.board.board.audio_analyzer_read_freq()

class HX711:
  def __init__(self, board, dout_pin, sck_pin = 2121, scale = None):
    if isinstance(board, int):
      scale = sck_pin
      sck_pin = dout_pin
      dout_pin = board
      board = gboard
    elif board == None:
      board = gboard
    
    self.board = board
    self.dout_pin = dout_pin
    self.sck_pin = sck_pin
    self.dout_pin,self.dout_apin = get_pin(self.board, dout_pin)
    self.sck_pin,self.sck_apin = get_pin(self.board, sck_pin)
    self.scale = scale
    self.board.board.set_hx711_init(self.dout_pin, self.sck_pin, self.scale)
  
  def read_weight(self):
    return self.board.board.hx711_read_weight(self.dout_pin)

class WIFI:
  def __init__(self, board = None):
    board = gboard
    self.board = board
    
  def set_ssid(self, ssid):
    self.ssid = ssid
    self.board.board._set_ssid(self.ssid)
  
  def set_password(self, password):
    self.password = password
    self.board.board._set_password(self.password)
    
  def connect_wifi(self):
    self.board.board._connect_wifi()
  
  def get_ip_port(self):
    ip,port = self.board.board._get_ip_port()
    return ip,port

class Board:
  def __init__(self, boardname="", port=None):
    global gboard
    globalvar_init()                              #初始化全局变量管理模块
    wifi_port = 8081
    self.boardname = boardname.upper()
    self.port = port
    self._i2c_init = [False,False,False,False,False]
    self.i2c = [None, None, None, None, None]
    self.uart = [None, None, None, None, None]
    self._spi_init = [[False,False], [False,False]]
    self.spi = [[None, None], [None, None]]
    self.i2c_fixed = {"RPI":1,"NEZHA":2}

    if gboard == None:
      gboard = self
      set_globalvar_value(self.boardname, gboard)
    
    if port == wifi_port:
      printlogo()
      self.ip = boardname
      self.port = port
      self.boardname = "UNO"
      self.board = pymata4.Pymata4(ip_address=self.ip, ip_port=self.port)

    name = platform.platform()
    self.connected = False
    self.spi_wifi_uno = False
    if self.boardname == "RPI":#本地资源
      GPIO.setmode(GPIO.BCM)
      GPIO.setwarnings(False)
      self.connected = True
    elif self.boardname == "NEZHA":
      self.connected = True
    elif self.boardname == "XUGU":
      self.boardname = "UNO"
      self.port = "/dev/ttyS1"
    elif self.boardname == "PINPONG BOARD":
      self.boardname = "UNO"
      self.spi_wifi_uno = True
    #  self.begin()
    #else:#外部资源
    #  self.begin()
  
  def begin(self):
    printlogo()
    version = sys.version.split(' ')[0]
    plat = platform.platform()
    if self.spi_wifi_uno:
      print("[01] Python"+version+" "+plat+" Board: "+ "PinPong Board")
    else:
      print("[01] Python"+version+" "+plat+" Board: "+ self.boardname)
    if self.boardname in ["RPI","NEZHA"]:
      self.connected = True
      return self
    if self.connected:
      return
    major,minor = self.detect_firmata()
    print("[32] Firmata ID: %d.%d"%(major,minor))
    if major != FIRMATA_MAJOR or minor != FIRMATA_MINOR:
      print("[35] Burning firmware...")
      cwdpath,_ = os.path.split(os.path.realpath(__file__))
      pgm = Burner(self.boardname,self.port)
      if(self.boardname == "UNO"):
        name = platform.platform()
        if self.spi_wifi_uno:
          pgm.burn(cwdpath + "/base/FirmataExpress.UNO_PB."+str(FIRMATA_MAJOR)+"."+str(FIRMATA_MINOR)+".hex")
        else:
          if name.find("Linux_vvBoard_OS")>=0 or name.find("Linux-4.4.159-aarch64-with-Ubuntu-16.04-xenial")>=0:
            cmd = "/home/scope/software/avrdude-6.3/avrdude -C/home/scope/software/avrdude-6.3/avrdude.conf -v -patmega328p -carduino -P"+self.port+" -b115200 -D -Uflash:w:"+cwdpath + "/base/FirmataExpress.UNO."+str(FIRMATA_MAJOR)+"."+str(FIRMATA_MINOR)+".hex"+":i"
            os.system(cmd)
          else:
            pgm.burn(cwdpath + "/base/FirmataExpress.UNO."+str(FIRMATA_MAJOR)+"."+str(FIRMATA_MINOR)+".hex")
      elif(self.boardname == "LEONARDO"):
#        port_list_0 = list(serial.tools.list_ports.comports())  #leonardo在linux下无法烧录固件 bug wsq
#        port_list_0 = [list(x) for x in port_list_0]
#        port_list_0 = [x[0:2] for x in port_list_0]
        port_list_0 = list(serial.tools.list_ports.comports())
        port_list_2 = port_list_0 = [list(x) for x in port_list_0]
        ser = serial.Serial(self.port,1200,timeout=1) #复位
        ser.close()
        time.sleep(0.2)
        retry = 5
        port = None
        while retry:
          retry = retry - 1
#          port_list_2 = list(serial.tools.list_ports.comports())
#          port_list_2 = [list(x) for x in port_list_2]
#          port_list_2 = [x[0:2] for x in port_list_2]
          port_list_2 = list(serial.tools.list_ports.comports())
          port_list_2 = [list(x) for x in port_list_2]
          for p in port_list_2:
            if p not in port_list_0:
              port = p
              break
          if port == None:
            time.sleep(0.5)
          if port: #找到了BootLoader串口
            break
        if port == None:
          print("[99] can NOT find ",self.boardname)
          sys.exit(0)
        pgm = Burner(self.boardname, port[0])
        pgm.burn(cwdpath + "/base/FirmataExpress.LEONARDO."+str(FIRMATA_MAJOR)+"."+str(FIRMATA_MINOR)+".hex")
      elif(self.boardname == 'MEGA2560'):
        pgm.burn(cwdpath + "/base/FirmataExpress.MEGA2560."+str(FIRMATA_MAJOR)+"."+str(FIRMATA_MINOR)+".hex")
      elif(self.boardname == 'HANDPY'):
        pgm.burn(cwdpath + "/base/FirmataExpress.HANDPY."+str(FIRMATA_MAJOR)+"."+str(FIRMATA_MINOR)+".bin")
        time.sleep(1)
        ser=serial.Serial(self.port, 115200, timeout=3)
        ser.read(ser.in_waiting)
        ser.close()
      elif(self.boardname == 'MICROBIT'):
        pgm.burn(cwdpath + "/base/FirmataExpress.MICROBIT."+str(FIRMATA_MAJOR)+"."+str(FIRMATA_MINOR)+".hex")
      elif(self.boardname == 'GD32V'):
        pgm.burn(cwdpath + "/base/FirmataExpress.GD32V."+str(FIRMATA_MAJOR)+"."+str(FIRMATA_MINOR)+".bin")
      print("[37] Burn done")
      self.detect_firmata()
    if self.boardname == "GD32V": #Degug 后期需要删除
      time.sleep(2)
    self.board = pymata4.Pymata4(com_port=self.port, arduino_wait=2, baud_rate=115200)
    
    self.connected = True
    return self
  '''
  Uno:
  ['COM99', 'Arduino Uno (COM99)', 'USB VID:PID=2341:0043 SER=5573932393735151F0C1 LOCATION=1-10']
  ['/dev/ttyACM0', 'ttyACM0', 'USB VID:PID=2341:0043 SER=5573932393735151F0C1 LOCATION=1-2:1.0']
  Leonardo:
  ['COM18', 'Arduino Leonardo (COM18)', 'USB VID:PID=2341:8036 SER=6 LOCATION=1-10.10:x.0']
  ['/dev/ttyACM1', 'Arduino Leonardo', 'USB VID:PID=2341:8036 LOCATION=1-10:1.0']
  MEGA2560:
  ['COM7', 'Arduino Mega 2560 (COM7)', 'USB VID:PID=2341:0042 SER=556393132333512141A2 LOCATION=1-10']
  ['/dev/ttyACM0', 'ttyACM0', 'USB VID:PID=2341:0042 SER=556393132333512141A2 LOCATION=1-2:1.0']
  Microbit:
  ['COM12', 'mbed Serial Port (COM12)', 'USB VID:PID=0D28:0204 SER=6 LOCATION=1-1:x.1']
  Handpy:
  ['COM29', 'Silicon Labs CP210x USB to UART Bridge (COM29)', 'USB VID:PID=10C4:EA60 SER=01CEDB2F LOCATION=1-9']
  '''
  def detect_firmata(self):
    vidpid={
    "UNO":"2341:0043",
    "LEONARDO":"3343:8036",
    "LEONARDO":"2341:8036",
    "MEGA2560":"2341:0042",
    "MICROBIT":"0D28:0204",
    "HANDPY":"10C4:EA60",
    "GD32V":"3343:3240"
    }
    portlist=[]
    localportlist=[]
    if self.boardname == "RPI":
      print("Using local resources")
      return (-1,-1)
    elif self.port == None:
      plist = list(serial.tools.list_ports.comports())
      for port in plist:
        msg = list(port)
        if msg[2].find(vidpid[self.boardname]) >= 0:
          portlist.insert(0,msg)
          break
        elif msg[2].find("USB") >= 0:
          portlist.insert(0,msg)
        else:
          localportlist.append(msg)
        portlist += localportlist
      if len(portlist) > 0:
        self.port = portlist[0][0]
        print("Automatically selected -> ",self.port)
    if self.port == None:
      return 0,0
    print("[10] Opening "+self.port)
    name = platform.platform()
    if name.find("Linux_vvBoard_OS")>=0 or name.find("Linux-4.4.159-aarch64-with-Ubuntu-16.04-xenial") >= 0:
      os.system("echo scope | sudo -S /home/scope/software/scripts/arduino_burn_setup.sh Arduino_Reset")
    if self.boardname == "GD32V" and name.find("rockchip")>0:
      if not os.path.exists("/sys/class/gpio/gpio71"):
         os.system("echo 71 > /sys/class/gpio/export")#RST
      if not os.path.exists("/sys/class/gpio/gpio70"):
         os.system("echo 70 > /sys/class/gpio/export")#BOOT1
      if not os.path.exists("/sys/class/gpio/gpio69"):
        os.system("echo 69 > /sys/class/gpio/export")#BOOT0

      os.system("echo out > /sys/class/gpio/gpio69/direction")
      os.system("echo out > /sys/class/gpio/gpio70/direction")
      os.system("echo out > /sys/class/gpio/gpio71/direction")
      os.system("echo 0 > /sys/class/gpio/gpio69/value")
      os.system("echo 0 > /sys/class/gpio/gpio70/value")
      os.system("echo 1 > /sys/class/gpio/gpio71/value")
      time.sleep(0.3)
      os.system("echo 0 > /sys/class/gpio/gpio71/value")
      time.sleep(0.3)
      os.system("echo 1 > /sys/class/gpio/gpio71/value")
      time.sleep(1)
    if self.boardname == "LEONARDO":
        time.sleep(1)
    ser=serial.Serial(self.port, 115200, timeout=0.5)
    if self.boardname in ["HANDPY","MICROBIT"]:
      time.sleep(1)
    if self.boardname in ["UNO" , "MEGA2560"]:
      time.sleep(3)
    ser.read(ser.in_waiting)
    buf=bytearray(b"\xf0\x79\xf7")
    ser.write(buf)
    res = ser.read(4)
    if len(res) < 3:
      major=0
      minor=0
    elif res[0] == 0xF0 and res[1] == 0x79:
      major = res[2]
      minor = res[3]
    else:
      major=0
      minor=0
    if (major,minor) == (2,6):
      if self.boardname in ["HANDPY" , "MICROBIT"]:
        ser.read(ser.in_waiting)
        reset_buf=bytearray(b"\xf0\x0d\x55\xf7")
        ser.write(reset_buf)
        reset = ser.read(10)
    ser.close()
    print("[15] Close "+self.port)
    return major,minor

  def get_i2c_master(self, bus_num=0):
    if bus_num == -1:#如果用户填写-1，自动分配device_num
      for i in range(len(self.i2c)):
        if self.i2c[i] == None:
          bus_num = i
          break

    if bus_num == -1: #分配满了，不再分配
      return None

    if self.i2c[bus_num] == None:
      self._i2c_init[bus_num] = True
      self.i2c[bus_num] = IIC(self,bus_num)
    return self.i2c[bus_num]

  def get_spi_master(self, device_num=0, sck=None, mosi=None, miso=None, cs=None, baudrate=100000, polarity=0, phase=0, bits=8):
    if device_num == -1:#如果用户填写-1，自动分配device_num
      for i in range(len(self.spi)):
        if self.spi[i] == None:
          device_num = i
          break

    if device_num == -1: #分配满了，不再分配
      return None

    if self.spi[device_num] == None:
      self._spi_init[device_num] = True
      self.spi[device_num] = SPI(self, device_num, sck, mosi, miso, cs, baudrate, polarity, phase, bits)
    return self.spi[device_num]
  
  @staticmethod
  def set_default_board(board):
    global gboard
    gboard = board
