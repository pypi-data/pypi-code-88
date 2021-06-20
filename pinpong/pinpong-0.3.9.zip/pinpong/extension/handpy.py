# -*- coding: utf-8 -*-

import time
from pinpong.extension.globalvar import *
try:
    from PIL import Image        #ESP32有显示图片功能
except:
    pass

class HPSensor:
  def __init__(self, board=None):
    if board == None:
      board = get_globalvar_value("HANDPY")
    self.board = board
    self.board.board._report_sensor()
  
  def buttonA_is_pressed(self):
    return self.board.board.handpy_buttonA_is_pressed()
  
  def buttonB_is_pressed(self):
    return self.board.board.handpy_buttonB_is_pressed()

  def buttonAB_is_pressed(self):
    return self.board.board.handpy_buttonAB_is_pressed()
    
  def touch_P(self):
    return self.board.board.handpy_touchP()
  
  def touch_Y(self):
    return self.board.board.handpy_touchY()
  
  def touch_T(self):
    return self.board.board.handpy_touchT()
  
  def touch_H(self):
    return self.board.board.handpy_touchH()
  
  def touch_O(self):
    return self.board.board.handpy_touchO()
  
  def touch_N(self):
    return self.board.board.handpy_touchN()
  
  def set_touch_threshold(self, obj="", value=30):
    if value > 80:
      value = 80
    elif value < 0:
      value = 0
    data = obj.upper()
    self.board.board.handpy_set_touch_threshold(data, value)
  
  def read_touch_P(self):
    return self.board.board.handpy_read_touch_P()
  
  def read_touch_Y(self):
    return self.board.board.handpy_read_touch_Y()
  
  def read_touch_T(self):
    return self.board.board.handpy_read_touch_T()
  
  def read_touch_H(self):
    return self.board.board.handpy_read_touch_H()
  
  def read_touch_O(self):
    return self.board.board.handpy_read_touch_O()
  
  def read_touch_N(self):
    return self.board.board.handpy_read_touch_N()
  
  def read_sound(self):
    return self.board.board.handpy_read_sound()
  
  def read_light(self):
    return self.board.board.handpy_read_light()
  
  def get_accelerometer_X(self):
    return self.board.board.handpy_get_accelerometer_X()
  
  def get_accelerometer_Y(self):
    return self.board.board.handpy_get_accelerometer_Y()
  
  def get_accelerometer_Z(self):
    return self.board.board.handpy_get_accelerometer_Z()
  
  def get_accelerometer_strength(self):
    return round(self.board.board.handpy_get_accelerometer_strength(),2)
    
class HPScreen:
  def __init__(self, board=None):
    if board == None:
      board = get_globalvar_value("HANDPY")
    self.board = board

  def display_in_line(self, data, line):
    try:
      if line < 1 or line > 4:
        raise ValueError("line must be a number greater than 0 and less than or equal to 4")
    except ValueError as e:
      print("Throw an exception:",repr(e))
    else:
      buf = []
      text = str(data)
      text = text.encode(encoding='UTF-8',errors='strict')
      for i in text:
        buf.append(i)
      length = len(buf)
      try:
        if length > 500:
          raise ValueError("Please enter less than 500")
      except ValueError as e:
        print("Throw an exception:",repr(e))
      else:
        self.board.board.handpy_display_in_line(buf, line, length)

  def display_clear_in_line(self, line):
    self.board.board.handpy_display_clear_in_line(line)
  
  def display_in_XY(self, data, x, y):
    try:
      if x < 0 or x > 127 or y < 0 or y > 63:
        raise ValueError("Please input x:0-127 y:0-63")
    except ValueError as e:
      print("Throw an exception:",repr(e))
    else:
      buf = []
      text = str(data)
      text = text.encode(encoding='UTF-8',errors='strict')
      for i in text:
        buf.append(i)
      length = len(buf)
      try:
        if length > 500:
          raise ValueError("Please input less than 500")
      except ValueError as e:
        print("Throw an exception:",repr(e))
      else:
        self.board.board.handpy_display_in_XY(x, y, buf, length)
  
  def fill_screen(self, color = "black"):
    color = str(color)
    color = color.upper()
    try:
      if color != "BLACK" and color != "WHITE":
        raise ValueError("Please input white or black")
    except ValueError as e:
      print("Throw an exception:",repr(e))
    else:
      color = 0 if color == "BLACK" else 1
      self.board.board.handpy_fill_screen(color)

  def screen_rotation(self, angle = 0):
    try:
      if angle != 0 and angle != 180:
        raise ValueError("Please input 0 or 180")
    except ValueError as e:
      print("Throw an exception:",repr(e))
    else:
      angle = 2 if angle == 180 else 0
      self.board.board.handpy_screen_rotation(angle)

  def point_drawing(self, x, y):
    try:
      if x < 0 or x > 127 or y < 0 or y > 63:
        raise ValueError("Please input x:0-127 y:0-63")
    except ValueError as e:
      print("Throw an exception:",repr(e))
    else:
      self.board.board.handpy_point_drawing(x, y)

  def set_line_width(self, lineW):
    try:
      if lineW < 1 or lineW > 128:
        raise ValueError("Please input x:0-127 y:0-63")
    except ValueError as e:
      print("Throw an exception:",repr(e))
    else:
      self.board.board.handpy_set_line_width(lineW)

  def line_drawing(self, x1, y1, x2, y2):
    try:
      if x1 < 0 or x1 > 127 or y1 < 0 or y1 > 63 or x2 < 0 or x2 > 127 or y2 < 0 or y2 > 63:
        raise ValueError("Please input x:0-127 y:0-63")
    except ValueError as e:
      print("Throw an exception:",repr(e))
    else:
      self.board.board.handpy_line_drawing(x1, y1, x2, y2)

  def circle_drawing(self, x, y, r):
    self.board.board.handpy_circle_drawing(x, y, 0 ,r)

  def circle_drawing_fill(self, x, y, r):
    self.board.board.handpy_circle_drawing_fill(x, y, 1 ,r)

  def rectangle_drawing(self, x, y, width, height):
    self.board.board.handpy_rectangle_drawing(x, y, width, height, 0)

  def rectangle_drawing_fill(self, x, y, width, height):
    self.board.board.handpy_rectangle_drawing_fill(x, y, width, height, 1)
  
  def display_image(self, x, y, width, height, path):
    try:
      if width < 0 or height < 0  or x < 0 or y < 0 or height > 64 or y >= 64 or width > 128 or x >= 128:
        raise ValueError("Please input width, x:0-127 height, y:0-63")
    except ValueError as e:
        print("Throw an exception:",repr(e))
    else:
      img_src = Image.open(path)
      im = img_src.resize((width,height))
      img_src = im.convert('L')
      aa = img_src.getdata()
      sequ0 = list(aa)
      data = []
      threshold = 130
      for i in range(height):
        j = 0; k = 0; l=0
        for j in range(width//8):
          byte = 0
          for k in range(8):
            byte <<= 1
            bit = sequ0[i*width+j*8+k]
            byte |= (1 if bit>threshold else 0)
          data .append(byte)
        byte = 0
        for l in range(width%8):
          byte <<= 1
          bit = sequ0[i*width+j*8+k + l]
          byte |= (1 if bit>threshold else 0)
        for m in range(7-l):
          byte <<= 1
        if width%8:
          data.append(byte)
      width_bytes = len(data) // height
      max_height = 128 // width_bytes
      for ii in range(height // max_height):
        time.sleep(0.1)
        self.board.board.handpy_display_image(x, y+max_height*ii, width, max_height, data[max_height * width_bytes * ii : max_height * width_bytes*(ii+1)], max_height * width_bytes)
      time.sleep(0.1)
      if height % max_height:
        self.board.board.handpy_display_image(x, y+max_height * (height // max_height), width, height % max_height, data[len(data) -((height % max_height) * width_bytes) : len(data)], (height % max_height) * width_bytes)
      time.sleep(0.1)
      self.board.board.handpy_oled12864_show(x, y, width, height)

class HPWS2812:
  def __init__(self, board=None):
    if board == None:
      board = get_globalvar_value("HANDPY")
    self.board = board
    self.board.board.handpy_report_sensor()
  
  def set_rgb_color(self, index, r, g, b):
    try:
      if index < -1 or index > 2 or r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
         raise ValueError("Please input (-1,0,1,2) rgb(0-255)")
    except ValueError as e:
      print("Throw an exception:",repr(e))
    else:
      if index == -1:
        index = 3
      color = r << 16 | g << 8 | b
      self.board.board.handpy_set_lights_color(index, color)

  def rgb_disable(self, index):
    try:
      if index < -1 or index > 2:
        raise ValueError("Please input (-1,0,1,2)")
    except ValueError as e:
      print("Throw an exception:",repr(e))
    else:
      if index == -1:
        index = 3
      self.board.board.handpy_rgb_disable(index, 0)
  
  def set_brightness(self, value):
    try:
      if value < 0 or value > 9:
        raise ValueError("Please input 0-9")
    except ValueError as e:
      print("Throw an exception:",repr(e))
    else:
      self.board.board.handpy_set_brightness(value)
  
  def get_brightness(self):
    return self.board.board.handpy_get_brightness()
