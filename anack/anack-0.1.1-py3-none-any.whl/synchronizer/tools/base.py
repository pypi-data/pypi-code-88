#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 5:43 下午
# @Author  : similarface
# @Site    : 
# @File    : base.py
# @Software: PyCharm
from typing import Union

import pandas as pd
import numpy as np
from datetime import datetime, date


def to_datetime64(x: Union[str, pd.Timestamp, date]) -> Union[np.datetime64, None]:
    if x is None:
        return None
    if x is date:
        return x
    if x is pd.Timestamp:
        return pd.to_datetime(datetime(x.year, x.month, x.day))

    if len(x) == 6:
        return pd.to_datetime(x, format='%Y%m')
    elif len(x) == 8:
        return pd.to_datetime(x, format='%Y%m%d')
    elif len(x) == 10:
        return pd.to_datetime(x, format='%Y-%m-%d')
    elif len(x) == 10:
        return pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S')
    else:
        return None
