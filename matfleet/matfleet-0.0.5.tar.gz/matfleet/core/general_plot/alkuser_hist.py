#   Coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2021/04/17 11:10:48'

from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl


def plt_user_append(x, y):
    plt.figure(1, (12, 4))

    mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

    xdata = np.array(range(len(x)))
    ydata = np.array([sum(y[:i+1]) for i in range(len(y))])
    ydata[0] = ydata[0] + 2
    y_smo_data = ydata
    y_interp = interp1d(xdata, y_smo_data, kind='cubic')

    x_smooth = np.linspace(xdata[:-1].min(), xdata[:-1].max(), 300)
    # x_smooth = np.linspace(xdata.min(), xdata.max(), 300)
    y_smooth = y_interp(x_smooth)

    plt.plot(np.append(x_smooth, xdata[-1]), np.append(y_smooth, y_smo_data[-1]), 'k',
             linewidth=3, label="ALKEMIE总用户增长曲线")
    plt.bar(x, y, 0.4, color="lightcoral", label="ALKEMIE每月用户增长量")
    for i in range(len(xdata)):
        x = xdata[i] - 0.3 if 1 < i < 5 else xdata[i]
        y = y_smo_data[i] + 3.5 if i < 5 else y_smo_data[i] - 8.5
        if i == 0:
            ydata[i] = ydata[i] - 2
        plt.text(x, y, str(ydata[i]), fontsize=16)
    plt.legend(fontsize=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    # plt.show()
    plt.savefig("1.pdf")


if __name__ == '__main__':
    xx = ['2019-03', '2019-04', '2019-05', '2019-06', '2019-09', '2021-03', '2021-04']
    yy = [4, 4, 5, 10, 6, 33, 3]
    plt_user_append(xx, yy)
