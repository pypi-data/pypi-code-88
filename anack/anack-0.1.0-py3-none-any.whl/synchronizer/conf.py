#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 3:30 下午
# @Author  : similarface
# @Site    : 
# @File    : conf.py
# @Software: PyCharm
from ratelimiter import RateLimiter

# ratelimiter 这个包提供ratelimiter模块，它确保 操作在 给定的时间段。在使用第三方api时，这可能会证明是有用的 这需要例如每秒最多10个请求。
ts_rate_limiter = RateLimiter(max_calls=1, period=1)

DATA_SAVE_BASE_DIR = "/tmp/anack/stocks"
