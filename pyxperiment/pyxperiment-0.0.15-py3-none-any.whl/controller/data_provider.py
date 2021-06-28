"""
    pyxperiment/controller/data_provider.py:
    Manipulates data storage to fetch specific datasets for plots

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

class SweepProvider():
    """
    Manages filtering for a single sweep
    """

    def __init__(self, sweep, measurable_ind):
        self.sweep = sweep
        self.measurable_ind = measurable_ind

    def read_data(self):
        """
        Get all the values from readed devices
        """
        data = self.sweep.read_data()
        return data[self.measurable_ind]

    def write_data(self):
        """
        Get all the values from writable devices
        """
        return self.sweep.write_data()

    def time_markers(self):
        """
        Get the time markers for this measurements
        """
        return self.sweep.time_markers()

class DataProvider():
    """
    Fetches data from DataStorage for a specific readable parameter
    """

    def __init__(self, data_storage, measurable_ind):
        """
        Creates a new DataProvider from the specified data source

        Parameters
        ----------
        data_storage : object
            Can be an instance of DataStorage, DataProvider or DataContext
            DataContext - will fetch the data from experiment,
                update accordingly when rerun
            DataStorage - will fetch the data from experiment, stored
                after the experiment is finished
            DataProvider - will apply extra filtering onto existing DataProvider

        measurable_ind : int
            Index of the measurable to be fetched
        """
        self.data_storage = data_storage
        self.filter_x = None# Take all slow x points
        self.measurable_ind = measurable_ind

    def set_filter_x(self, index):
        """
        Set filter to 0 to take odd, 1 to take even, None to take all
        """
        self.filter_x = index
        return self

    def get_data(self):
        """
        Return the set of filtered curves

        Returns
        -------
        data : list of CurveProvider
            The list of measured curves
        """
        data = self.data_storage.get_data()
        if self.filter_x is not None:
            data = data[self.filter_x::2]
        if self.measurable_ind is not None:
            data = [SweepProvider(c, self.measurable_ind) for c in data]
        return data

    def get_length(self):
        """
        Returns the total number of sweeps present

        Returns
        -------
        int
            The number of sweeps available
        """
        data = self.data_storage.get_data()
        if self.filter_x is not None:
            data = data[self.filter_x::2]
        return len(data)

    def get_sweep(self, sweep_id):
        """
        Return the dataset for a specified sweep

        Parameters
        ----------
        sweep_id : int
            The index of the sweep to fetch (-1 = the last)

        Returns
        -------
        SweepProvider
            The fetched sweep object
        """
        data = self.data_storage.get_data()
        if self.filter_x is not None:
            data = data[self.filter_x::2]
        return SweepProvider(data[sweep_id], self.measurable_ind)

    def get_sweepables(self):
        return self.data_storage.writables

    def get_measurables(self):
        return [self.data_storage.readables[self.measurable_ind]]
