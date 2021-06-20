# -*- coding: utf-8 -*-

import time
from pinpong.extension.globalvar import *

class MBMusic:
  sound = {
    "DADADADUM": 0,
    "ENTERTAINER": 1,
    "PRELUDE": 2,
    "ODE": 3,
    "NYAN": 4,
    "RINGTONE": 5,
    "FUNK": 6,
    "BLUES": 7,
    "BIRTHDAY": 8,
    "WEDDING": 9,
    "FUNERAL": 10,
    "PUNCHLINE": 11,
    "BADDY": 12,
    "CHASE": 13,
    "BA_DING": 14,
    "WAWAWAWAA": 15,
    "JUMP_UP": 16,
    "JUMP_DOWN": 17,
    "POWER_UP": 18,
    "POWER_DOWN": 19
  }
  music_map = {
    "C/C3":131,
    "D/D3":147,
    "E/E3":165,
    "F/F3":175,
    "G/G3":196,
    "A/A3":220,
    "B/B3":247,
    "C/C4":262,
    "D/D4":294,
    "E/E4":330,
    "F/F4":349,
    "G/G4":392,
    "A/A4":440,
    "B/B4":494,
    "C/C5":523,
    "D/D5":587,
    "E/E5":659,
    "F/F5":698,
    "G/G5":784,
    "A/A5":880,
    "B/B5":988,
    "C#/C#3":139,
    "D#/D#3":156,
    "F#/F#3":185,
    "G#/G#3":208,
    "A#/A#3":233,
    "C#/C#4":277,
    "D#/D#4":311,
    "F#/F#4":370,
    "G#/G#4":415,
    "A#/A#4":466,
    "C#/C#5":554,
    "D#/D#5":622,
    "F#/F#5":740,
    "G#/G#5":831,
    "A#/A#5":932
  }
  beats_map = {
    1/4: 1,
    1/2: 2,
    3/4: 3,
    1: 4,
    1.5: 6,
    2: 8,
    3: 12,
    4: 16
  }
  microbit_map = {
    1: 1,
    1/2: 2,
    1/4: 4,
    1/8: 8,
    1/16: 16,
    2: 32,
    4: 64
  }
  def __init__(self, board=None):
    if board == None:
      board = get_globalvar_value("MICROBIT")
    self.board = board
    self.speed = 120
  
  def music_set_tempo(self, ticks, tempo):
    self.board.board.esp32_music_set_tempo(0x7f, ticks, tempo)
  
  def set_buzzer_freq(self, note, beat):
    note = note.upper()
    _note = self.music_map[note]
    if self.beats_map[beat]:
      _beat = self.beats_map[beat]
    else:
      if beat > 0.125 and beat <= 0.25:
        _beat = 1
      elif beat > 0.25 and beat <= 0.5:
        _beat = 2
      elif beat > 0.5 and beat <=0.75:
        _beat = 3
      elif beat > 0.75 and beat <= 1:
        _beat = 4
      elif beat > 1 and beat <= 1.5:
        _beat = 6
      elif beat > 1.5 and beat <= 2:
        _beat = 8
      elif beat > 2 and beat <= 3:
        _beat = 12
      elif beat > 3 and beat <= 4:
        _beat = 16
      else:
        _beat = 4
    self.board.board.esp32_set_buzzer_freq(0x7f, _note, _beat)
  
  def background_set_buzzer_freq(self, note):
    _note = self.music_map[note]
    self.board.board.esp32_set_buzzer_freq(0x7f, _note, 0)

  def stop_background_buzzer_freq(self):
    self.board.board.esp32_stop_background_buzzer_freq()
  
  def play_music_background(self, pin, music):
    try:
      val = self.sound[music]
    except:
      print("please input correct music")
    else:
      self.board.board.set_pin_mode_digital_output(pin)
      time.sleep(0.1)
      self.board.board.microbit_play_music_background(pin, val, 0)
  
  def play_music_until_end(self, pin, music):
    try:
      val = self.sound[music]
    except:
      print("please input correct music")
    else:
      self.board.board.set_pin_mode_digital_output(pin)
      time.sleep(0.1)
      self.board.board.microbit_play_music_background(pin, val, 1)
  
  def play_buzzer_freq(self, pin, note, beat):
    try:
      note = note.upper()
      _note = self.music_map[note]
      if self.microbit_map[beat]:
        _beat = self.microbit_map[beat]
      else:
        if (num > 0 and num <= 0.0625): _beat = 16
        elif (num > 0.0625 and num <= 0.125): _beat = 8
        elif (num > 0.125 and num <= 0.25): _beat = 4
        elif (num > 0.25 and num <= 0.5): _beat = 2
        elif (num > 0.5 and num <= 1): _beat = 1
        elif (num > 1 and num <= 2): _beat = 32
        elif (num > 2 and num <= 4): _beat = 64
        else: _beat = 1
    except:
      print("please input correct param")
    else:
      self.board.board.microbit_play_buzzer_freq(pin, _note, _beat)
  
  def change_speed(self, val):
    self.speed += val
    if self.speed < 4:
      self.speed = 4
    if self.speed > 400:
      self.speed = 400
    self.board.board.microbit_set_speed(self.speed)

  def set_speed(self, val):
    self.speed = val
    if self.speed < 4:
      self.speed = 4
    if self.speed > 400:
      self.speed = 400
    self.board.board.microbit_set_speed(self.speed)
  
  def get_speed(self):
    return self.speed

class MBScreen:
  value = {   
  "HEART":         "0101010101100010101000100",
  "HEART_SMALL":   "0000001010011100010000000",
  "ARROW_N":       "0010001110101010010000100",
  "ARROW_S":       "0010000100101010111000100",
  "ARROW_W":       "0010001000111110100000100",
  "ARROW_E":       "0010000010111110001000100",
  "ARROW_NE":      "0011100011001010100010000",
  "ARROW_NW":      "1110011000101000001000001",
  "ARROW_SE":      "1000001000001010001100111",
  "ARROW_SW":      "0000100010101001100011100",
  "YES":           "0000000001000101010001000",
  "NO":            "1000101010001000101010001",
  "HAPPY":         "0000001010000001000101110",
  "SAD":           "0000001010000000111010001",
  "ANGRY":         "1000101010000001111110101",
  "SILLY":         "1000100000111110010100111",
  "SMILE":         "0000000000000001000101110",
  "ASLEEP":        "0000011111000000111000000",
  "SQUARE":        "1111110001100011000111111",
  "SQUARE_SMALL":  "0000001110010100111000000",
  "TRIANGLE":      "0000000100010101111100000",
  "TRIANGLE_LEFT": "1000011000101001001011111",
  "DIAMOND_SMALL": "0000000100010100010000000",
  "MUSIC_CROTCHET":"0010000100001001110011100",
  "MUSIC_QUAVER":  "0010000111001011110011100",
  "MUSIC_QUAVERS": "0111101001010011101111011",
  "CLOCK1":        "0001000010001000000000000",
  "CLOCK2":        "0000000011001000000000000",
  "CLOCK3":        "0000000000001110000000000",
  "CLOCK4":        "0000000000001000001100000",
  "CLOCK5":        "0000000000001000001000010",
  "CLOCK6":        "0000000000001000010000100",
  "CLOCK7":        "0000000000001000100001000",
  "CLOCK8":        "0000000000001001100000000",
  "CLOCK9":        "0000000000111000000000000",
  "CLOCK10":       "0000011000001000000000000",
  "CLOCK11":       "0100001000001000000000000",
  "CLOCK12":       "0010000100001000000000000",
  "SKULL":         "0111010101111110111001110",
  "BUTTERFLY":     "1101111111001001111111011",
  "CHESSBOARD":    "0101010101010101010101010",
  "CONFUSED":      "0000001010000000101010101",
  "COW":           "1000110001111110111000100",
  "DIAMOND":       "0010001010100010101000100",
  "DUCK":          "0110011100011110111000000",
  "FABULOUS":      "1111111011000000101001110",
  "GHOST":         "1111110101111111111110101",
  "GIRAFFE":       "1100001000010000111001010",
  "HOUSE":         "0010001110111110111001010",
  "MEH":           "0101000000000100010001000",
  "PACMAN":        "0111111010111001111001111",
  "PITCHFORK":     "1010110101111110010000100",
  "RABBIT":        "1010010100111101101011110",
  "ROLLERSKATE":   "0001100011111111111101010",
  "SNAKE":         "1100011011010100111000000",
  "STICKFIGURE":   "0010011111001000101010001",
  "SURPRISED":     "0101000000001000101000100",
  "SWORD":         "0010000100001000111000100",
  "TARGET":        "0010001110110110111000100",
  "TORTOISE":      "0000001110111110101000000",
  "TSHIRT":        "1101111111011100111001110",
  "UMBRELLA":      "0111011111001001010001100",
  "XMAS":          "0010001110001000111011111"
  }
  def __init__(self, board=None):
    if board == None:
      board = get_globalvar_value("MICROBIT")
    self.board = board
  
  def show_shape(self, shape):
    shape = shape.upper()
    data = self.value[shape]
    buf = []
    for i in range(0, 21, 5):
      buf.append(data[i:i+5])
    data = []
    for i in buf:
      data.append(int(i,2))
    self.board.board.microbit_show_shape(data)
  
  def show_font(self, data):
    data = str(data)
    if len(data) > 20:
      data = data[0:20]
    buf = []
    for i in data:
      buf.append(ord(i))
    buf.append(0)
    self.board.board.microbit_show_font(buf)
  
  def control_light_on(self, x, y):
    try:
      if x < 0 or y < 0 or x > 4 or y > 4:
        raise ValueError("Please input 0-4")
    except ValueError as e:
      print("Throw an exception:",repr(e))
    else:
      self.board.board.microbit_control_light_on(x, y, 1)
  
  def control_light_off(self, x, y):
    try:
      if x < 0 or y < 0 or x > 4 or y > 4:
        raise ValueError("Please input 0-4")
    except ValueError as e:
      print("Throw an exception:",repr(e))
    else:
      self.board.board.microbit_control_light_on(x, y, 0)

  def set_light_brightness(self, brightness):
    try:
      if brightness < 0 or brightness > 9 :
        raise ValueError("Please input 0-9")
    except ValueError as e:
      print("Throw an exception:",repr(e))
    else:
      if brightness == 0:
        val = 0
      elif brightness == 9:
        val = 255
      else:
        val = brightness * 28
      self.board.board.microbit_set_light_brightness(val)
  
  def hide_all_lights(self):
    self.board.board.microbit_hide_all_lights()

class MBSensor:
  _gesture = {
    1 :'Logo up',
    2 :'Logo down',
    3 :'Tilt left',
    4 :'Tilt right',
    5 :'Face up',
    6 :'Face down',
    7 :'Freefall',
    8 :'3g',
    9 :'6g',
    10:'8g',
    11:'shake' 
  }
  def __init__(self, board=None):
    if board == None:
      board = get_globalvar_value("MICROBIT")
    self.board = board
    self.board.board.microbit_report_sensor()

  def buttonA_is_pressed(self):
    return self.board.board.microbit_buttonA_is_pressed()
  
  def buttonB_is_pressed(self):
    return self.board.board.microbit_buttonB_is_pressed()

  def buttonAB_is_pressed(self):
    return self.board.board.microbit_buttonAB_is_pressed()
  
  def touch0(self):
    return self.board.board.microbit_touch0()
  
  def touch1(self):
    return self.board.board.microbit_touch1()
  
  def touch2(self):
    return self.board.board.microbit_touch2()
  
  def get_gesture(self):
    val = self.board.board.microbit_get_gesture()
    if val:
      return self._gesture[val]
    else:
      return "Failure to recognize gesture"
  
  def get_brightness(self):
    return self.board.board.microbit_get_brightness()

  def get_compass(self):
    return self.board.board.microbit_get_compass()
  
  def cal_compass(self):
    self.board.board.microbit_cal_compass()
  
  def get_temp(self):
    return self.board.board.microbit_get_temp()
  
  def get_accelerometer_X(self):
    return self.board.board.microbit_get_accelerometer_X()
  
  def get_accelerometer_Y(self):
    return self.board.board.microbit_get_accelerometer_Y()
  
  def get_accelerometer_Z(self):
    return self.board.board.microbit_get_accelerometer_Z()
  
  def get_accelerometer_strength(self):
    return self.board.board.microbit_get_accelerometer_strength()
  
class MBWireless:
  def __init__(self, board=None):
    if board == None:
      board = get_globalvar_value("MICROBIT")
    self.board = board
  
  def set_wireless_channel(self, channel):
    self.board.board.microbit_set_wireless_channel(channel)
  
  def open_wireless(self):
    self.board.board.microbit_open_wireless(1)
  
  def close_wireless(self):
    self.board.board.microbit_open_wireless(0)
  
  def send_wireless(self, data):
    data = str(data)
    val = []
    for i in data:
      val.append(ord(i))
    self.board.board.microbit_send_wireless(val)
  
  def recv_data(self, callback = None):
    self.board.board.microbbit_recv_data(callback)