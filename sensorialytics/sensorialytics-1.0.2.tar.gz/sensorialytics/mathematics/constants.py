#  constants.py
#  Project: sensorialytics
#  Copyright (c) 2021 Sensoria Health Inc.
#  All rights reserved

import numpy as np

__all__ = ['PI', 'g', 'GYRO_CONV']

PI: float = np.pi
g: float = 9.81
GYRO_CONV: float = np.pi / 180.0
