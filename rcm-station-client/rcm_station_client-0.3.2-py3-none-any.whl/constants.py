#  Copyright (c) 2020 Pim Hazebroek
#  This program is made available under the terms of the MIT License.
#  For full details check the LICENSE file at the root of the project.
"""Application wide constants that are shared across multiple modules"""


ONE_MB = '1048576'
LINE_SEP = '\n'
SIXTY_SECONDS = 60
MODE_READ = 'r'
MODE_WRITE = 'w'

# Supported sensors
SENSOR_BME680 = 'BME680'
SENSOR_SHT31_D = 'SHT31-D'
SENSOR_TSL2591 = 'TSL2591'
SENSOR_SGP30 = 'SGP30'
SENSOR_SYS = 'SYS'

# Supported gain modes for TSL2591
GAIN_LOW = 'GAIN_LOW'
GAIN_MEDIUM = 'GAIN_MEDIUM'
GAIN_HIGH = 'GAIN_HIGH'
GAIN_MAX = 'GAIN_MAX'
DEFAULT_GAIN = GAIN_MEDIUM

# Supported integration times for TSL2591
IT_TIME_100MS = '100ms'
IT_TIME_200MS = '200ms'
IT_TIME_300MS = '300ms'
IT_TIME_400MS = '400ms'
IT_TIME_500MS = '500ms'
IT_TIME_600MS = '600ms'
DEFAULT_IT_TIME = IT_TIME_100MS
