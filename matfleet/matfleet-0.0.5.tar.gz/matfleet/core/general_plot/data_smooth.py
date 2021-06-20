#   Coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2021/04/17 12:55:47'

from scipy.interpolate import interp1d, InterpolatedUnivariateSpline, splrep, splprep, splev
import numpy as np


def smooth_data(x, y, num: int, method_type: int = 1, kind: str = 'cubic'):
    """
    数据平滑
    :param x: 横坐标
    :param y: 纵坐标
    :param num: 平滑后横坐标设置为多少个数据点
    :param method_type: 选择哪种平滑方法
                        1-2-3-4分别对应：interp1d, InterpolatedUnivariateSpline, splrep, splprep方法, 默认选择第一种
    :param kind: 如果选择第一种方法，需要设置kind，默认为cubic
    :return: np.array: 平滑后的x和y
    """
    x = np.array(x)
    y = np.array(y)
    mm = [interp1d, InterpolatedUnivariateSpline, splrep, splprep]
    method = mm[method_type-1]
    new_data = np.linspace(min(x), max(x), num=num)

    if method_type == 1:
        y_interp = method(x, y, kind=kind)
        return new_data, y_interp(new_data)
    elif method_type == 2:
        y_interp = method(x, y)
        return new_data, y_interp(new_data)
    elif method_type == 3:
        y_interp = method(x, y, s=0)
        return new_data, splev(new_data, y_interp)
    elif method_type == 4:
        y_interp, u = method([x, y], s=0)
        fdata = splev(new_data, y_interp)
        return fdata[0], fdata[1]
    else:
        raise ValueError("Don't support %d, set to 1-2-3-4" % method_type)


if __name__ == '__main__':
    xx = np.linspace(1, 10, 10)
    yy = np.arange(30, 40) + np.random.randn(10)
    # x = ['2019-03', '2019-04', '2019-05', '2019-06', '2019-09', '2021-03', '2021-04']
    # y = [4, 4, 5, 10, 6, 33, 3]
    # y = np.array([sum(y[:i+1]) for i in range(len(y))])
    # x = np.array(range(len(x)))
    newx, newy = smooth_data(xx, yy, 300, method_type=2, kind='cubic')
    print(newx, newy)
    import matplotlib.pyplot as plt
    plt.plot(xx, yy, 'r')
    plt.plot(newx, newy, 'k')
    plt.show()
