"""
    pyxperiment/controller/device_options.py:
    The base classes for options - device specific data entities

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

from abc import ABCMeta, abstractmethod
from copy import copy
from pyxperiment.core.utils import bidict
from .validation import EmptyValidator

class DeviceOption(metaclass=ABCMeta):
    """
    Device option, that generally can not be used for a sweep,
    only in editor, abstract base class
    """

    def __init__(self, name, get_func=None, set_func=None, enabled=None):
        self._name = name
        self._fget = get_func
        self._fset = set_func
        self._enabled = enabled
        self.device = None

    @property
    def name(self):
        """The name of the current option"""
        return self._name

    @abstractmethod
    def get_value(self):
        """
        Retrieve the option value
        """

    @abstractmethod
    def set_value(self, value):
        """
        Set the option value
        """

    def is_enabled(self):
        """
        Is the option modification allowed
        """
        if self._enabled is None:
            return True
        return self._enabled(self.device)

    def is_readable(self):
        """
        Readable option can be only read
        """
        return self._fset is None

    def is_writable(self):
        """
        Writable option can be set
        """
        return self._fset is not None

    def with_instance(self, device):
        """
        Used to instantiate options when a specific device is created
        """
        #pylint: disable=W0212
        ret = copy(self)
        ret.device = device
        if self._fset is not None:
            ret._fset = self._fset.__get__(device, device.__class__)
        if self._fget is not None:
            ret._fget = self._fget.__get__(device, device.__class__)
        return ret

    def description(self):
        """
        Get the description tuple array
        """
        ret = self.device.description()
        ret.append(('Property', self._name))
        return ret

    def driver_name(self):
        return self.device.driver_name()

    def device_name(self):
        return self.device.device_name()

    def device_id(self):
        return self.device.device_id()

    def is_sweep_based(self):
        # TODO: remove
        return False

    @property
    def location(self):
        return self.device.location

    def to_remote(self):
        self.device.to_remote()

    def to_local(self):
        self.device.to_local()

class ListControl(DeviceOption):
    """
    List control has only a certain set of values, which may also
    have a separate human-readable interpretation.
    """

    def __init__(self, name, values_list, get_func=None, set_func=None, enabled=None):
        super().__init__(name, get_func, set_func, enabled)
        # Convert dict to bidict to have a faster backward conversion
        if isinstance(values_list, dict) and not isinstance(values_list, bidict):
            values_list = bidict(values_list)
        self._values_list = values_list

    def values_list(self):
        """return the list of the valid values"""
        return self._values_list

    def get_value(self):
        """
        Get the value, converted to the readable form
        """
        value = self._fget()
        if isinstance(self._values_list, bidict):
            if not value in self._values_list.inverse:
                raise ValueError('Invalid value for ' + self.name + ': ' + value)
            return self._values_list.inverse[value]
        # No conversion is required
        return value

    def set_value(self, value):
        """
        Set the value, accepts argument in readable form
        """
        if not value in self._values_list:
            raise ValueError('Invalid value for ' + self.name + ': ' + value)
        if isinstance(self._values_list, bidict):
            self._fset(self._values_list[value])
        else:# No conversion is required
            self._fset(value)

class BooleanControl(DeviceOption):
    """
    Device control, that takes two values:
    true or false, and does data conversion internally
    """

    def __init__(
            self, name, get_func=None, set_func=None, enabled=None,
            true_str='1', false_str='0'
        ):
        super().__init__(name, get_func, set_func, enabled)
        self.true_str = true_str
        self.false_str = false_str

    def get_value(self):
        value = self._fget()
        int_value = int(value)
        if int_value == 1:
            return True
        if int_value == 0:
            return False
        raise ValueError('Bad value for ' + self.name + ': "' + str(value) + '"')

    def set_value(self, value):
        self._fset(self.true_str if value else self.false_str)

class ValueDeviceOption(DeviceOption):
    """
    Device option, that repesents a numerical value of physical
    quantity (a valid x for a sweep).
    """

    def __init__(
            self, name, phys_q, get_func=None, set_func=None, channels=1,
            validator=EmptyValidator, enabled=None, sweepable=True
        ):
        super().__init__(name, get_func, set_func, enabled)
        self._phys_q = phys_q
        self._validator = validator
        self._channels = channels
        self._sweepable = sweepable

    def phys_quantity(self):
        """
        Get physical quantity (if applicable)
        """
        return self._phys_q

    def get_value(self):
        return self._fget()

    def set_value(self, value):
        self._fset(value)

    def with_instance(self, device):
        #pylint: disable=W0212
        ret = super().with_instance(device)
        if callable(self._channels):
            ret._channels = self._channels.__get__(device, device.__class__)
        return ret

    def is_sweepable(self):
        return self._sweepable

    def check_value(self, value):
        """
        Check the ability to set a single value
        """
        return self._validator.check_value(value)

    def check_values(self, values):
        """
        Check the ability to set all the values present in collection
        """
        return self._validator.check_values(values)

    @property
    def channels_num(self):
        """
        Return the length of the output data vector
        """
        return self._channels

class SweepControl(DeviceOption):
    """
    Sweep control represent a capability of making sweep measurement of
    one parameter against the other
    """

    def get_sweep_range(self):
        """
        This routine shall return the range of control paramter. This
        range is to be immutable in a single experiment.
        """

    def get_sweep_physq(self):
        """
        Return the physical quantity, associated with control parameter
        """

    def get_value(self):
        """
        Measure a new trace and return it
        """

    def phys_quantity(self):
        """
        Get physical quantity (if applicable)
        """
        return self._phys_q

class StateControl(DeviceOption):
    """
    Device control, that can only be read, and represents
    a status string
    """

    def __init__(self, name, get_func, enabled=None):
        super().__init__(name, get_func, None, enabled)

    def get_value(self):
        return self._fget()

    def set_value(self, value):
        del value
        raise NotImplementedError('set_value not valid for StateControl')

class ActionControl(DeviceOption):
    """
    Instrument control, that can only be set (activated), and
    represents a certain action/state transition
    """

    def __init__(self, name, set_func, enabled=None):
        super().__init__(name, None, set_func, enabled)

    def get_value(self):
        raise NotImplementedError('get_value not valid for ActionControl')

    def set_value(self, value=None):
        self._fset()

class TimeoutControl(ValueDeviceOption):
    """
    A special control, representing a timeout for another control
    """

    def __init__(self, option):
        super().__init__(
            'Timeout', 'ms', None, None, sweepable=False
        )
        # Value is set externally by ControlField
        self.value = None
        self.option = option
        option.read_timeout = self

    def get_value(self):
        if not self.value:
            return ''
        return str(round((self.value)*1000, 2))
