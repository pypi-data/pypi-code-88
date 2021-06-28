"""
    pyxperiment/frames/plots/line_plot.py: The module defining line plot panel
    for data representation

    This file is part of the PyXperiment project.

    Copyright (c) 2021 PyXperiment Developers

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""

from enum import Enum
from math import isinf, isnan
import itertools
import wx
import numpy as np
import pylab
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import \
    FigureCanvasWxAgg as FigCanvas, \
    NavigationToolbar2WxAgg
from pyxperiment.controller.device_control import SweepReadableControl
from pyxperiment.controller.device_options import ValueDeviceOption

class NavigationToolbar(NavigationToolbar2WxAgg):
    """
    A custom NavigationToolbar replacement to fix the rubberband glitches
    """

    def __init__(self, canvas):
        NavigationToolbar2WxAgg.__init__(self, canvas)
        self.last_rubberband = None

    def _init_toolbar(self):
        pass

    def draw_rubberband(self, event, x0, y0, x1, y1):
        self.last_rubberband = (x0, y0, x1, y1)
        NavigationToolbar2WxAgg.draw_rubberband(self, event, x0, y0, x1, y1)

    def remove_rubberband(self):
        self.last_rubberband = None
        NavigationToolbar2WxAgg.remove_rubberband(self)

    def redraw_rubberband(self):
        if self.last_rubberband != None:
            NavigationToolbar2WxAgg.draw_rubberband(self, None, *self.lastRubberband)

    def is_nav_at_home(self):
        return self._nav_stack.empty() or self._nav_stack[0] == self._nav_stack[-1]

class DataViewMode(Enum):
    SIMPLE = 1
    CUMULATIVE = 2

class MyScalarFormatter(matplotlib.ticker.ScalarFormatter):
    """
    Minor tweaks to display the exponent along the value
    """

    def __init__(self):
        super().__init__(False, True, None)
        self.set_powerlimits((-3, 4))

    def get_offset(self):
        return ''

    def _set_format(self, *arg):
        super()._set_format(*arg)
        offset = super().get_offset().lstrip('$')
        if offset:
            self.format = self.format.rstrip('$') + offset

class DataViewAxis(wx.Panel):
    """
    The Panel, showing a line plot of a single physical quantity
    """

    # 14 standard colors for the plots
    PLOT_COLORS = [
        (1, 1, 0), (1, 0, 0), (0, 1, 0),
        (0, 0, 1), (0, 1, 1), (1, 0, 1),
        (1, 1, 1),
        (0.5, 0.5, 0), (0.5, 0, 0), (0, 0.5, 0),
        (0, 0, 0.5), (0, 0.5, 0.5), (0.5, 0, 0.5),
        (0.5, 0.5, 0.5),
        ]

    def __init__(self, parent, data_provider, mode=DataViewMode.SIMPLE):
        super().__init__(parent, wx.ID_ANY, size=(500,400))

        self.data_provider = data_provider
        self.mode = mode

        # Will effectively set the minimal figure size
        self.fig = Figure((1, 1), dpi=100, facecolor='lightgray')
        self.canvas = FigCanvas(self, -1, self.fig)
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.set_cursor = lambda cursor: None

        self.axes = self.fig.add_subplot(111)
        if callable(getattr(self.axes, 'set_facecolor', None)):
            self.axes.set_facecolor('black')
        else:
            self.axes.set_axis_bgcolor('black')
        self.axes.grid(True, color='gray')

        pylab.setp(self.axes.get_xticklabels(), fontsize=9)
        pylab.setp(self.axes.get_yticklabels(), fontsize=9)
        self.axes.get_xaxis().set_major_formatter(MyScalarFormatter())
        self.axes.get_yaxis().set_major_formatter(MyScalarFormatter())

        self.cb_autox = wx.CheckBox(
            self, -1, "Auto scale X", style=wx.ALIGN_RIGHT)
        self.Bind(wx.EVT_CHECKBOX, self._on_cb_xlab, self.cb_autox)
        self.cb_autox.SetValue(False)

        self.sweepable = self.data_provider.get_sweepables()[0]
        self.measurable = self.data_provider.get_measurables()[0]
        self.axes.set_title(
            'Reading from: ' + self.measurable.device_name +
            ' at ' + self.measurable.location,
            size=10
            )
        if isinstance(self.measurable.device, ValueDeviceOption):
            if self.measurable.device.phys_quantity() is not None:
                self.axes.set_ylabel(
                    self.measurable.device.name + ', ' + self.measurable.device.phys_quantity()
                    )
            else:
                self.axes.set_ylabel(self.measurable.device.name)
        if isinstance(self.sweepable.device, ValueDeviceOption):
            if self.sweepable.device.phys_quantity() is not None:
                self.axes.set_xlabel(
                    self.sweepable.device.name + ', ' + self.sweepable.device.phys_quantity()
                    )
            else:
                self.axes.set_xlabel(self.sweepable.device.name)

        if self.measurable.num_channels() > len(self.PLOT_COLORS):
            self.PLOT_COLORS = [self.PLOT_COLORS[1]] * self.measurable.num_channels()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer_controls = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_controls.Add(self.toolbar, 0, wx.ALIGN_LEFT)
        self.sizer_controls.Add(self.cb_autox, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        self.sizer.Add(self.canvas, 1, flag=wx.ALL | wx.GROW)
        self.sizer.Add(self.sizer_controls, 0, flag=wx.ALIGN_LEFT | wx.TOP)
        self.SetSizer(self.sizer)
        self.sizer.Fit(self)
        self.Bind(wx.EVT_SIZE, self._on_resize, self)

        # Create initial curves
        self.plot_curves = [
            self.axes.plot(
                [], linewidth=1, color=self.PLOT_COLORS[i], scalex=False, scaley=False
                )[0]
            for i in range(self.measurable.num_channels())
            ]
        self.current_curve = 0
        self.ylimits = [None, None]
        self._set_xscale()

    def _on_resize(self, event):
        event.Skip()
        size = self.GetSize()
        if size.x > 250 and size.y > 250:
            self.fig.subplots_adjust(
                left=80.0/size.x, right=1-30.0/size.x, top=1-30.0/size.y, bottom=55.0/size.y
                )

    def _set_xscale(self):
        if isinstance(self.measurable, SweepReadableControl):
            xdata = list(map(float, self.measurable.get_sweep_x()))
        else:
            xdata = self.sweepable.values
        if xdata:
            self.axes.set_xbound(lower=min(xdata), upper=max(xdata))

    def _on_cb_xlab(self, event):
        del event
        if not self.cb_autox.Value:
            self._set_xscale()
        self.draw_plot()

    def _plot_sweep_data(self, sweep):
        # get x axis data
        if isinstance(self.measurable, SweepReadableControl):
            self._set_xscale()
            xdata = self.measurable.get_sweep_x()
        else:
            xdata = sweep.write_data()
        # if sweep is not finished yet, cut it
        ydata = sweep.read_data()
        xdata = np.fromiter(itertools.islice(xdata, len(ydata)), float, len(ydata))
        # Get the actual new data and convert it to floats
        for i, curve in enumerate(self.plot_curves):
            if len(self.plot_curves) > 1:
                ydata_ch = np.fromiter(
                    itertools.islice((float(x[i]) for x in ydata), xdata.size), float, xdata.size
                    )
            else:
                ydata_ch = np.fromiter(
                    itertools.islice((float(x) for x in ydata), xdata.size), float, xdata.size
                    )
            # Update the y axis limits
            if ydata_ch.size > 0:
                self.ylimits[0] = min(self.ylimits[0], ydata_ch.min()) if self.ylimits[0] else ydata_ch.min()
                self.ylimits[1] = max(self.ylimits[1], ydata_ch.max()) if self.ylimits[1] else ydata_ch.max()
            # Update data
            curve.set_xdata(xdata)
            curve.set_ydata(ydata_ch)
        # Update x axis limits if required
        if self.cb_autox.Value and xdata.size:
            self.axes.set_xbound(lower=xdata.min(), upper=xdata.max())

    def draw_plot(self):
        """
        Redraws the plot
        """
        sweeps_ready = self.data_provider.get_length()
        if not sweeps_ready:
            return

        if self.mode == DataViewMode.CUMULATIVE:
            # If new curves appeared
            while sweeps_ready-1 > self.current_curve:
                self._plot_sweep_data(
                    self.data_provider.get_sweep(self.current_curve)
                    )
                for curve in self.plot_curves:
                    # Make previous curves faint
                    curve.set_color([col / 3 for col in curve.get_color()])
                # Create new curves
                self.plot_curves = [
                    self.axes.plot(
                        [], linewidth=1, color=self.PLOT_COLORS[i], scalex=False, scaley=False
                        )[0]
                    for i in range(self.measurable.num_channels())
                ]
                self.current_curve += 1
        else:
            self.ylimits = [None, None]

        sweep = self.data_provider.get_sweep(-1)
        # TODO: check that data actually changed
        self._plot_sweep_data(sweep)

        if not any(map(lambda x: x is None or isinf(x) or isnan(x), self.ylimits)):
            margin = (self.ylimits[1] - self.ylimits[0]) / 10
            if margin == 0:
                margin = 0.1
            if self.toolbar.is_nav_at_home():
                self.axes.set_ybound(lower=self.ylimits[0] - margin, upper=self.ylimits[1] + margin)

        self.canvas.draw()
        self.toolbar.redraw_rubberband()
