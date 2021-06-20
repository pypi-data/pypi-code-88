# -*- coding: utf-8 -*-

import time
from pinpong.extension.globalvar import *

class GD32VSensor:
  def __init__(self, board=None):
    if board == None:
      board = get_globalvar_value("GD32V")
    self.board = board
    self.board.board._report_sensor()
  
  def buttonA_is_pressed(self):
      return self.board.board.GD32V_buttonA_is_pressed()
  
  def buttonB_is_pressed(self):
      return self.board.board.GD32V_buttonB_is_pressed()
  
  def read_light(self):
      return self.board.board.GD32V_read_light()
      
  def get_accelerometer_X(self):
    return self.board.board.GD32V_get_accelerometer_X()
  
  def get_accelerometer_Y(self):
    return self.board.board.GD32V_get_accelerometer_Y()
  
  def get_accelerometer_Z(self):
    return self.board.board.GD32V_get_accelerometer_Z()
    
  def get_Macceleration_X(self):
    return self.board.board.GD32V_get_Macceleration_X()
  
  def get_Macceleration_Y(self):
    return self.board.board.GD32V_get_Macceleration_Y()
  
  def get_Macceleration_Z(self):
    return self.board.board.GD32V_get_Macceleration_Z()