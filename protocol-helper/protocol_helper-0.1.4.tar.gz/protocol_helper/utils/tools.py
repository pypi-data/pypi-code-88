#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LeisureMan
# email:LeisureMam@gmail.com
# datetime:2021-06-11 14:49
# software: PyCharm
import math
import re
import sys
import time


def countdown(timing_num: (int, float), remarks = '剩余休眠时间还有'):
    """
    不换行的倒计时打印，只限单线程情况下调用
    :param timing_num:
    :param remarks:
    :return:
    """
    time.sleep(0.01)  # 用于不跟日志打印行冲突
    # print('Task->sleep->{0}'.format(timing_num))
    if timing_num < 1:
        print(f'{remarks}:{timing_num}秒')
        time.sleep(timing_num)
        return

    if isinstance(timing_num, float):
        num_float, num_int = math.modf(timing_num)
        num_int = int(num_int)
    else:
        num_float, num_int = 0, timing_num

    for num in range(num_int, -1, -1):
        if num == 0 and num_float:
            sys.stdout.write(f'\r{remarks}:{round(num_float, 2)}秒')
            sleep_num = num_float
        else:
            sys.stdout.write(f'\r{remarks}:{num}秒')
            sleep_num = 1
        sys.stdout.flush()

        time.sleep(sleep_num)
    print('\n')


class Timer(object):
    """
    计时器，对于需要计时的代码进行with操作：
    with Timer() as timer:
        ...
        ...
    print(timer.cost)
    ...
    """

    def __init__(self, start = None):
        self.start = start if start is not None else time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.time()
        self.cost = round(self.stop - self.start, 2)
        return exc_type is None


def check_wb_is_fans_url(url):
    """
    检测地址是否是微博主页地址
    Args:
        url:
        https://weibo.com/u/6388382145
        https://weibo.com/p/1005057316802031/home
        https://weibo.com/p/1005055953899825/follow
        https://m.weibo.cn/u/6388382145
        https://m.weibo.cn/profile/6973695473
    Returns:

    """
    res = re.match(
            r'^http[s]?:\/\/(\w+\.)?weibo.(cn|com)(\/p\/|\/u\/|\/profile\/|\/)(?!status)(?!detail)(\w{6,'
            r'26})(\/info|\/manage|\/home|\/fans|\?|\/profile|\/follow|\/$|$)|^http[s]?:\/\/(\w+\.)?weibo.('
            r'cn|com)\/\w+|^\d{6,15}$',
            url)
    if res is None:
        return False
    else:
        return True


def check_wb_is_article_url(url):
    """
    检测地址是否是微博文章地址
    Args:
        url:

        https://m.weibo.cn/detail/4638970946257445
        https://m.weibo.cn/status/4640406149792999?
        https://weibo.com/7316802031/JtnHTvcby

    Returns:

    """
    res = re.match(r'^http[s]?:\/\/(\w+\.)?weibo.(cn|com)\/(status|profile|detail|\d+)\/(\w{6,26}).*', url)
    if res is None:
        return False
    else:
        return True
