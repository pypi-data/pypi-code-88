import time
from pinpong.board import gboard,I2C
import math

class MCP4725():
    DACLookup_FullSine_9Bit =[
  2048, 2073, 2098, 2123, 2148, 2174, 2199, 2224,
  2249, 2274, 2299, 2324, 2349, 2373, 2398, 2423,
  2448, 2472, 2497, 2521, 2546, 2570, 2594, 2618,
  2643, 2667, 2690, 2714, 2738, 2762, 2785, 2808,
  2832, 2855, 2878, 2901, 2924, 2946, 2969, 2991,
  3013, 3036, 3057, 3079, 3101, 3122, 3144, 3165,
  3186, 3207, 3227, 3248, 3268, 3288, 3308, 3328,
  3347, 3367, 3386, 3405, 3423, 3442, 3460, 3478,
  3496, 3514, 3531, 3548, 3565, 3582, 3599, 3615,
  3631, 3647, 3663, 3678, 3693, 3708, 3722, 3737,
  3751, 3765, 3778, 3792, 3805, 3817, 3830, 3842,
  3854, 3866, 3877, 3888, 3899, 3910, 3920, 3930,
  3940, 3950, 3959, 3968, 3976, 3985, 3993, 4000,
  4008, 4015, 4022, 4028, 4035, 4041, 4046, 4052,
  4057, 4061, 4066, 4070, 4074, 4077, 4081, 4084,
  4086, 4088, 4090, 4092, 4094, 4095, 4095, 4095,
  4095, 4095, 4095, 4095, 4094, 4092, 4090, 4088,
  4086, 4084, 4081, 4077, 4074, 4070, 4066, 4061,
  4057, 4052, 4046, 4041, 4035, 4028, 4022, 4015,
  4008, 4000, 3993, 3985, 3976, 3968, 3959, 3950,
  3940, 3930, 3920, 3910, 3899, 3888, 3877, 3866,
  3854, 3842, 3830, 3817, 3805, 3792, 3778, 3765,
  3751, 3737, 3722, 3708, 3693, 3678, 3663, 3647,
  3631, 3615, 3599, 3582, 3565, 3548, 3531, 3514,
  3496, 3478, 3460, 3442, 3423, 3405, 3386, 3367,
  3347, 3328, 3308, 3288, 3268, 3248, 3227, 3207,
  3186, 3165, 3144, 3122, 3101, 3079, 3057, 3036,
  3013, 2991, 2969, 2946, 2924, 2901, 2878, 2855,
  2832, 2808, 2785, 2762, 2738, 2714, 2690, 2667,
  2643, 2618, 2594, 2570, 2546, 2521, 2497, 2472,
  2448, 2423, 2398, 2373, 2349, 2324, 2299, 2274,
  2249, 2224, 2199, 2174, 2148, 2123, 2098, 2073,
  2048, 2023, 1998, 1973, 1948, 1922, 1897, 1872,
  1847, 1822, 1797, 1772, 1747, 1723, 1698, 1673,
  1648, 1624, 1599, 1575, 1550, 1526, 1502, 1478,
  1453, 1429, 1406, 1382, 1358, 1334, 1311, 1288,
  1264, 1241, 1218, 1195, 1172, 1150, 1127, 1105,
  1083, 1060, 1039, 1017,  995,  974,  952,  931,
   910,  889,  869,  848,  828,  808,  788,  768,
   749,  729,  710,  691,  673,  654,  636,  618,
   600,  582,  565,  548,  531,  514,  497,  481,
   465,  449,  433,  418,  403,  388,  374,  359,
   345,  331,  318,  304,  291,  279,  266,  254,
   242,  230,  219,  208,  197,  186,  176,  166,
   156,  146,  137,  128,  120,  111,  103,   96,
    88,   81,   74,   68,   61,   55,   50,   44,
    39,   35,   30,   26,   22,   19,   15,   12,
    10,    8,    6,    4,    2,    1,    1,    0,
     0,    0,    1,    1,    2,    4,    6,    8,
    10,   12,   15,   19,   22,   26,   30,   35,
    39,   44,   50,   55,   61,   68,   74,   81,
    88,   96,  103,  111,  120,  128,  137,  146,
   156,  166,  176,  186,  197,  208,  219,  230,
   242,  254,  266,  279,  291,  304,  318,  331,
   345,  359,  374,  388,  403,  418,  433,  449,
   465,  481,  497,  514,  531,  548,  565,  582,
   600,  618,  636,  654,  673,  691,  710,  729,
   749,  768,  788,  808,  828,  848,  869,  889,
   910,  931,  952,  974,  995, 1017, 1039, 1060,
  1083, 1105, 1127, 1150, 1172, 1195, 1218, 1241,
  1264, 1288, 1311, 1334, 1358, 1382, 1406, 1429,
  1453, 1478, 1502, 1526, 1550, 1575, 1599, 1624,
  1648, 1673, 1698, 1723, 1747, 1772, 1797, 1822,
  1847, 1872, 1897, 1922, 1948, 1973, 1998, 2023
]
    DACLookup_FullSine_8Bit =[
  2048, 2098, 2148, 2198, 2248, 2298, 2348, 2398,
  2447, 2496, 2545, 2594, 2642, 2690, 2737, 2784,
  2831, 2877, 2923, 2968, 3013, 3057, 3100, 3143,
  3185, 3226, 3267, 3307, 3346, 3385, 3423, 3459,
  3495, 3530, 3565, 3598, 3630, 3662, 3692, 3722,
  3750, 3777, 3804, 3829, 3853, 3876, 3898, 3919,
  3939, 3958, 3975, 3992, 4007, 4021, 4034, 4045,
  4056, 4065, 4073, 4080, 4085, 4089, 4093, 4094,
  4095, 4094, 4093, 4089, 4085, 4080, 4073, 4065,
  4056, 4045, 4034, 4021, 4007, 3992, 3975, 3958,
  3939, 3919, 3898, 3876, 3853, 3829, 3804, 3777,
  3750, 3722, 3692, 3662, 3630, 3598, 3565, 3530,
  3495, 3459, 3423, 3385, 3346, 3307, 3267, 3226,
  3185, 3143, 3100, 3057, 3013, 2968, 2923, 2877,
  2831, 2784, 2737, 2690, 2642, 2594, 2545, 2496,
  2447, 2398, 2348, 2298, 2248, 2198, 2148, 2098,
  2048, 1997, 1947, 1897, 1847, 1797, 1747, 1697,
  1648, 1599, 1550, 1501, 1453, 1405, 1358, 1311,
  1264, 1218, 1172, 1127, 1082, 1038,  995,  952,
   910,  869,  828,  788,  749,  710,  672,  636,
   600,  565,  530,  497,  465,  433,  403,  373,
   345,  318,  291,  266,  242,  219,  197,  176,
   156,  137,  120,  103,   88,   74,   61,   50,
    39,   30,   22,   15,   10,    6,    2,    1,
     0,    1,    2,    6,   10,   15,   22,   30,
    39,   50,   61,   74,   88,  103,  120,  137,
   156,  176,  197,  219,  242,  266,  291,  318,
   345,  373,  403,  433,  465,  497,  530,  565,
   600,  636,  672,  710,  749,  788,  828,  869,
   910,  952,  995, 1038, 1082, 1127, 1172, 1218,
  1264, 1311, 1358, 1405, 1453, 1501, 1550, 1599,
  1648, 1697, 1747, 1797, 1847, 1897, 1947, 1997
]
    DACLookup_FullSine_7Bit =[
  2048, 2148, 2248, 2348, 2447, 2545, 2642, 2737,
  2831, 2923, 3013, 3100, 3185, 3267, 3346, 3423,
  3495, 3565, 3630, 3692, 3750, 3804, 3853, 3898,
  3939, 3975, 4007, 4034, 4056, 4073, 4085, 4093,
  4095, 4093, 4085, 4073, 4056, 4034, 4007, 3975,
  3939, 3898, 3853, 3804, 3750, 3692, 3630, 3565,
  3495, 3423, 3346, 3267, 3185, 3100, 3013, 2923,
  2831, 2737, 2642, 2545, 2447, 2348, 2248, 2148,
  2048, 1947, 1847, 1747, 1648, 1550, 1453, 1358,
  1264, 1172, 1082,  995,  910,  828,  749,  672,
   600,  530,  465,  403,  345,  291,  242,  197,
   156,  120,   88,   61,   39,   22,   10,    2,
     0,    2,   10,   22,   39,   61,   88,  120,
   156,  197,  242,  291,  345,  403,  465,  530,
   600,  672,  749,  828,  910,  995, 1082, 1172,
  1264, 1358, 1453, 1550, 1648, 1747, 1847, 1947
]
    DACLookup_FullSine_6Bit =[
  2048, 2248, 2447, 2642, 2831, 3013, 3185, 3346,
  3495, 3630, 3750, 3853, 3939, 4007, 4056, 4085,
  4095, 4085, 4056, 4007, 3939, 3853, 3750, 3630,
  3495, 3346, 3185, 3013, 2831, 2642, 2447, 2248,
  2048, 1847, 1648, 1453, 1264, 1082,  910,  749,
   600,  465,  345,  242,  156,   88,   39,   10,
     0,   10,   39,   88,  156,  242,  345,  465,
   600,  749,  910, 1082, 1264, 1453, 1648, 1847
]
    DACLookup_FullSine_5Bit =[
  2048, 2447, 2831, 3185, 3495, 3750, 3939, 4056,
  4095, 4056, 3939, 3750, 3495, 3185, 2831, 2447,
  2048, 1648, 1264,  910,  600,  345,  156,   39,
     0,   39,  156,  345,  600,  910, 1264, 1648
]


    MCP4725_Write_CMD            = 0x40   
    MCP4725_WriteEEPROM_CMD      = 0x60     
    MCP4725A0_IIC_Address0       = 0x60   
    MCP4725A0_IIC_Address1       = 0x61

    MCP4725_NORMAL_MODE          = 0
    MCP4725_POWER_DOWN_1KRES     = 1
    MCP4725_POWER_DOWN_100KRES   = 2
    MCP4725_POWER_DOWN_500KRES   = 3

    def __init__(self, board = None, i2c_addr = None, bus_num=0):
        if isinstance(board, int):
            i2c_addr = board
            board = gboard
        elif board is None:
            board = gboard
        self.i2c_addr = i2c_addr
        self._i2c = I2C(bus_num)      

    def init(self, addr, vRef):
        self.i2c_addr = addr
        self._refVoltage = vRef
        self._power_mode = self.MCP4725_NORMAL_MODE

    def output_voltage_EEPROM(self, voltage):
        _voltage = voltage
        if self._refVoltage < voltage:
            print("ERROR! The input voltage is greater than the maximum voltage!")
            return False
        else:
            data = (_voltage / self._refVoltage) *4095
            self.write_reg(self.MCP4725_WriteEEPROM_CMD | (self._power_mode << 1), data)

    def output_voltage(self, voltage):
        _voltage = voltage
        if self._refVoltage < voltage:
            print("ERROR! The input voltage is greater than the maximum voltage!")
            return False
        else:
            data = (_voltage / self._refVoltage) *4095
            self.write_reg(self.MCP4725_Write_CMD | (self._power_mode << 1), data)

    def output_triangle(self, amp, freq, offset, dutyCycle):
        num = 64
        maxV = int(amp*(4096/self._refVoltage))
        if freq > 100:
            num = 16
        elif freq >= 50 and frea <= 100:
            num = 32
        else:
            num = 64
        frame = 1000000/(freq*num*2)
        if dutyCycle > 100:
            dutyCycle = 100
        if dutyCycle < 0:
            dutyCycle = 0
        up_num = int((2*num)*(dutyCycle/100))
        down_num = ((2*num) - up_num)
        for counter in range(0, (maxV-(maxV//up_num)-1), maxV//up_num):
            starttime = time.time()*1000000
            enterV = counter+(offset*(4096/self._refVoltage))
            if enterV > 4095:
                enterV = 4095
            elif  enterV < 0:
                enterV = 0
            self.write_reg(self.MCP4725_Write_CMD | (self._power_mode << 1), enterV)
            stoptime = time.time() * 1000000
            looptime = stoptime-starttime
            while looptime <= frame:
                stoptime = time.time() * 1000000
                looptime = stoptime - starttime
        for counter in range(maxV-1, maxV//down_num, -(maxV//up_num)):
            starttime = time.time()*1000000
            enterV = counter+(offset*(4096/self._refVoltage))
            if enterV > 4095:
                enterV = 4095
            elif  enterV < 0:
                enterV = 0
            self.write_reg(self.MCP4725_Write_CMD | (self._power_mode << 1), enterV)
            stoptime = time.time() * 1000000
            looptime = stoptime-starttime
            while looptime <= frame:
                stoptime = time.time() * 1000000
                looptime = stoptime - starttime


    def output_Sin(self, amp, freq, offset):
        num = 512
        data = 0
        if freq < 8:
            num = 512
        elif freq >= 8 and freq <=16:
            num = 256
        elif freq > 16 and freq < 33:
            num = 128
        elif freq >= 33 and freq <= 68:
            num = 64
        else:
            num = 32
        if freq > 100:
            freq = 100
        frame = 1000000/(freq*num)
        for i in range(num):
            starttime = time.time() * 1000000
            if num == 512:
                data = ((self.DACLookup_FullSine_9Bit[i] - 2047) * (amp / self._refVoltage)) * 2
            elif num == 256:
                data = ((self.DACLookup_FullSine_8Bit[i] - 2047) * (amp / self._refVoltage)) * 2
            elif num == 128:
                data = ((self.DACLookup_FullSine_7Bit[i] - 2047) * (amp / self._refVoltage)) * 2
            elif num == 64:
                data = ((self.DACLookup_FullSine_6Bit[i] - 2047) * (amp / self._refVoltage)) * 2
            elif num == 32:
                data = ((self.DACLookup_FullSine_5Bit[i] - 2047) * (amp / self._refVoltage)) * 2
            else:
                data = ((self.DACLookup_FullSine_5Bit[i] - 2047) * (amp / self._refVoltage)) * 2
            data = data + (offset*(4096/self._refVoltage))
#            print(data)
            if data < 0:
                data = 0
            if data > 4095:
                data = 4095
            self.write_reg(self.MCP4725_Write_CMD, data)
            stoptime = time.time()* 1000000
            looptime = stoptime - starttime
            while looptime <= frame:
                stoptime = time.time() * 1000000
                looptime = stoptime-starttime


    def write_reg(self, reg, value):
        data = [int(value / 16), int(value % 16) << 4]
        self._i2c.writeto_mem(self.i2c_addr, reg, data)
         
    def read_reg(self, reg, len):
        data = self._i2c.readfrom_mem(self.i2c_addr, reg, len)
