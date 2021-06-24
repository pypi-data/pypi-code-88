#!/usr/bin/env python
# coding: utf-8

# Author : Rahul Bhadani
# Initial Date: April 25, 2021
# About: strymplot for visualization dashboard
# Read associated README for full description
# License: MIT License

#   Permission is hereby granted, free of charge, to any person obtaining
#   a copy of this software and associated documentation files
#   (the "Software"), to deal in the Software without restriction, including
#   without limitation the rights to use, copy, modify, merge, publish,
#   distribute, sublicense, and/or sell copies of the Software, and to
#   permit persons to whom the Software is furnished to do so, subject
#   to the following conditions:

#   The above copyright notice and this permission notice shall be
#   included in all copies or substantial portions of the Software.

#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF
#   ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
#   TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
#   PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
#   SHALL THE AUTHORS, COPYRIGHT HOLDERS OR ARIZONA BOARD OF REGENTS
#   BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN
#   AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#   OR OTHER DEALINGS IN THE SOFTWARE.

__author__ = 'Rahul Bhadani'
__email__  = 'rahulbhadani@email.arizona.edu'
import sys

from ..strymread import strymread

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import seaborn as sea
import IPython
import time


class strymviz:
    """
    Real Time visualization of a Timeseries

    Parameters
    -------------
    x_col: `str`
        X Axis data

    y_col: `str`
        Y Axis data

    z_col: `str`
        Optional. Z Axis, in Case of 3D Plot


    """

    def __init__(self, ts, x_col ='Time', y_col='Message', **kwargs):
        self.ts = ts
        self.x_col = x_col
        self.y_col = y_col
        self.z_col = kwargs.get("z_col", None)

        self.shell_type = IPython.get_ipython().__class__.__name__

    def animate2D(self, **kwargs):
        '''
        `animate2D` will animate a 2D plot. Time and Message pandas series are expected


        Parameters
        ----------

        title: `str`
            Title of the plot. By Default, it is `Timeseries Plot`

        rate: int
            Animation Rate, by default, it is 1x, 2 = 2x, 3 =3x, and so on.
        '''
        self.plot_title = kwargs.get("title", 'Timeseries Plot')
        rate = kwargs.get("rate", 1)

        ts = self.ts
        if isinstance(self.ts, pd.DataFrame):
            ts = [self.ts]
        else:
            ts= self.ts

        ts1, ts2 = strymread.ts_sync(ts[0], ts[1], rate = 20, method='nearest')
        fig, ax = strymread.create_fig(len(ts))

        Index = ts1.index.strftime('%m/%d/%Y, %H:%M:%S.%f')
        cb_indices = np.linspace(0, ts1.shape[0]-1, len(ts1['Time'].values), dtype=int)
        cb =Index[cb_indices]
        cbtime = ts1.Time[cb_indices].values

        xvals1 = ts1[self.x_col]
        yvals1 = ts1[self.y_col]

        xvals2 = ts2[self.x_col]
        yvals2 = ts2[self.y_col]

        # if self.shell_type in ['ZMQInteractiveShell', 'TerminalInteractiveShell']:
        #     if self.shell_type == 'ZMQInteractiveShell':
        #         IPython.get_ipython().run_line_magic('matplotlib', 'inline')
        #     print('Warning: Animation is being executed in IPython/Jupyter Notebook. Animation may not be real-time.')
        #     l, = ax.plot(xvals.iloc[0],yvals.iloc[0], marker='o', markersize=5, linewidth=0, markerfacecolor='#275E56')
        #     def animate(i):
        #         l.set_data(xvals[:i], yvals[:i])

        #         ax.set_xlabel(self.x_col, fontsize=15)
        #         ax.set_ylabel(self.y_col, fontsize=15)
        #         ax.set_title(self.plot_title, fontsize=16)

        #     for index in range(len(yvals)-1):
        #         animate(index)
        #         IPython.display.clear_output(wait=True)
        #         display(fig)
        #         plt.pause( (xvals[index + 1] - xvals[index])/rate)
        # else:
        # index = 1
        # ax[0].scatter(x = xvals1[:index], y =yvals1[:index],  s=20, c="#275E56")
        # ax[1].scatter(x = xvals2[:index], y =yvals2[:index],  s=20, c="#E56275")

        # ax[0].set_title('{}'.format(cbtime[index]))
        # ax[0].set_xlabel('Time')
        # ax[0].set_ylabel('Speed')
        # ax[1].set_xlabel('Time')
        # ax[1].set_ylabel('Acceleration')
        # plt.draw()
        # plt.pause( (xvals1[index + 1] - xvals1[index])/rate)
        # time.sleep(20)
        for index in range(0, len(yvals1)-1):
            ax[0].clear()
            ax[1].clear()
            if index < 20:
                #ax[0].scatter(x = xvals1[:index], y =yvals1[:index],  s=20, c="#275E56")
                #ax[1].scatter(x = xvals2[:index], y =yvals2[:index],  s=20, c="#E56275")
                ax[0].plot(xvals1[:index], yvals1[:index],  markersize=12, marker='.', linewidth=2, color="#275E56")
                ax[1].plot(xvals2[:index], yvals2[:index],  markersize=12, marker='.', linewidth=2, color="#E56275")
            else:
                #ax[0].scatter(x = xvals1[index - 500:index], y= yvals1[index - 500:index],  s=20, c="#275E56")
                #ax[1].scatter(x = xvals2[index - 500:index], y= yvals2[index - 500:index],  s=20, c="#E56275")
                ax[0].plot(xvals1[index - 20:index], yvals1[index - 20:index], linewidth=2, marker='.', markersize=12, color="#275E56")
                ax[1].plot(xvals2[index - 20:index], yvals2[index - 20:index], linewidth=2, marker='.', markersize=12, color="#E56275")

            ax[0].set_title('{}'.format(cb[index]))
            ax[0].set_ylim([0, 70]);
            ax[1].set_ylim([-2, 2]);
            ax[1].set_title('{}'.format(cb[index]))
            ax[0].set_xlabel('Time [s]')
            ax[0].set_ylabel('Speed [km/h]')
            ax[1].set_xlabel('Time [s]')
            ax[1].set_ylabel('Acceleration [m/s^2]')
            plt.draw()
            plt.pause( (xvals1[index + 1] - xvals1[index])/rate)

