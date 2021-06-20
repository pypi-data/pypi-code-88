#   coding: utf-8
#   This file is part of potentialmind.

#   potentialmind is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2020/11/15"

import numpy as np
import matplotlib.pyplot as plt


def read_data_and_plt_for_subplt(fn):
    data = np.loadtxt(fname=fn, dtype=np.float, comments='#', skiprows=1, usecols=None)
    num = data.shape[-1] - 1
    x, y = data[:, 0], data[:, 1:]
    fig, axes = plt.subplots(num, 1, figsize=(12, 7))
    y_label = ['E_potential', 'E_kin', 'T', 'E_tot']
    y_limlist = [[-3.3, -3.4], [0.031, 0.039], [240, 300], [-3.2, -3.4]]
    x_lim = [0, 10001]

    for n in range(len(axes)):
        ax = axes[n]
        ax.plot(x, y[:, n], label=y_label[n])
        ax.set_ylim(y_limlist[n])
        ax.set_ylabel(y_label[n], fontsize=12)
        ax.set_xlim(x_lim)
        if n == len(axes) - 1:
            ax.set_xlabel("Timesteps (fs)", fontsize=12)
        ax.legend(fontsize=12)

    plt.subplots_adjust(left=0.09, bottom=0.08, right=0.98, top=0.98, hspace=0.33)


    plt.show()


if __name__ == '__main__':
    read_data_and_plt_for_subplt(fn='111')