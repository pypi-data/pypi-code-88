"""
    pyxperiment/core/experiment.py: This module defines the class for defining
    a single data aquisition activity

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

from pyxperiment.controller.data_context import DataContext
from pyxperiment.frames.experiment_control_frame import ExperimentControlFrame

class Experiment():
    """
    Experiment defines the interface for a single data aquisition activity
    """

    def __init__(self, app, data_writer):
        """
        Create a new empty experiment.

        Parameters
        ----------
        app : PyXperimentApp
            The entity of the current application.

        data_writer : DataWriter
            To be used for saving results.
        """
        self.app = app
        self.data_writer = data_writer
        self._cumulative_view = False
        self.data_context = DataContext()
        self.data_context.set_data_writer(self.data_writer)

    def add_observable(self, parameter, values, delay):
        """
        Add the device, which reads the parameter for Х axis.
        The observable is a parameter you can not control directly
        via setpoints, but can only get the actual value of.

        Parameters
        ----------
        parameter : object
            The data type should be a descendant of Instrument or ValueDeviceOption,
            in any case with is_writable() == True.
            Should incorporate the internal logic of threshold control, which is done
            by calling a method finished().

        values : a two element array
            The first element is the start value. The second is a threshold
            used to set the experiment end condition and the view size.

        delay : float
            Delay between the experiment ticks in milliseconds.

        """
        self.data_context.add_observable(parameter, values, delay)
        return self

    def add_writable(self, writable, values, delay):
        """
        Add the device which will set some parameter
        """
        self.data_context.add_writable(writable, values, delay)
        return self

    def add_double_writable(self, writable1, writable2, values1, values2, delay):
        """
        Add two devices which will set their parameters simultaneously
        TODO: This is a workaround, until vector writable devices are not avialiable
        """
        self.data_context.add_double_writable(writable1, writable2, values1, values2, delay)
        return self

    def add_readables(self, readables):
        """
        Add the parameters to be read. The parameters will be read at each
        experiment tick. The read will be performed in the same order, as
        in supplied collection. Sequential calls of this method are possible.

        Parameters
        ----------
        readables : collection
            The data type should be a descendant of Instrument or ValueDeviceOption,
            in any case with is_readable() == True.

        Returns
        -------
        self : Experiment
            Used to stack calls
        """
        self.data_context.add_readables(readables)
        return self

    def add_curve_callback(self, callback):
        """
        Add a function to be called after a curve is finished.

        Parameters
        ----------
        callback : callable
            The unbound function to be called after each experimental
            curve is finished. No arguments are to be passed by the
            experiment logic.

        Returns
        -------
        self : Experiment
            Used to stack calls
        """
        self.data_context.add_curve_callback(callback)
        return self

    def set_curves_num(self, curves_num, delay, backsweep):
        """
        Sets the number of repeated curve measurements.

        Parameters
        ----------
        curves_num : integer
            The number of repetetive measurements to be taken
        delay : float
            The delay between iterations in seconds
        backsweep : boolean
            The behaviour on return path
            True - The measurement will be performed in reverse with the
            same points set.
            False - The measurement will return to start using the reverse
            of the points set with 10 times the measurement speed and no
            readables logging.

        Returns
        -------
        self : Experiment
            Used to stack calls
        """
        self.data_context.set_curves_num(curves_num, delay, backsweep)
        return self

    def set_cumulative_view(self, view_mode):
        """
        Sets the desired view of the measured curves.

        Parameters
        ----------
        view_mode : boolean
            True - cumulative, all the curves stay on screen
            False (default) - only the current curve is displayed

        Returns
        -------
        self : Experiment
            Used to stack calls
        """
        self._cumulative_view = view_mode
        return self

    def run(self, auto_close=False, parent_frame=None, start_now=True):
        """
        Start the experiment. If working in scripted environment, will blocks current
        execution until the experiment is complete. Shows the experiment control window.

        Parameters
        ----------
        auto_close : boolean
            True - the control window will close automatically when the measurement is
            finished.
            False - the window will persist until closed manually
        parent_frame : wx.Frame
            If specified - a frame that will be locked while the experiment is active and
            unlocked again when the ControlWindow is closed
        start_now : boolean
            True - the control window will open and the experiment will start immediately
            False - the control window will open, however the actual experiment has to be
            manually started later
        """

        # Actualize the file number
        self.data_writer.start_new_file()
        # Save experiment information
        self.data_writer.save_info_file(
            [dev.description() for dev in self.data_context.readables],
            [dev.description() for dev in self.data_context.writables],
            [
                ('Repeat each curve', str(self.data_context.curves_num)),
                ('Delay between curves', str(self.data_context.curves_delay)),
                ('Measure on backward sweep', str(self.data_context.backsweep)),
                ('Data Format', str(self.data_writer.get_format_name()))
            ]
            )

        if self.data_context.finished:
            self.data_context.rearm()
        control_frame = ExperimentControlFrame(
            parent_frame, self.data_context, self._cumulative_view, auto_close
            )
        control_frame.Show()
        if start_now:
            self.data_context.start()
        if self.app.frame is None:
            self.app.frame = control_frame
        self.app.start()
