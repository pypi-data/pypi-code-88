# MIT License
#
# Copyright (c) 2021 Peter Goss
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from abc import ABC, abstractmethod
from typing import Any
from midb.persistent_objects import BasePersistentObject


class PersistentSequence(BasePersistentObject, ABC):
    """
        PersistentSequence is the abstract base class for list and tuple.
    """

    @property
    @abstractmethod
    def _equivalent_builtin_class(self):
        """ return the built-in class that the sub-class is emulating (tuple or list) """

    def __init__(self, iterator=(), _backend=None, _id=None):
        """
            Takes an iterator for initializing during temp state and _backend and _id for
            full disk usage state.
        """
        _init_temp = self._equivalent_builtin_class(iterator)
        BasePersistentObject.__init__(self, _backend=_backend, _id=_id, _init_temp=_init_temp)

    def in_memory(self):
        """ Returns in-memory built-in type equivelent of the persistent object. """
        if self.still_temp():
            return self._temp
        else:
            return self._equivalent_builtin_class(self._backend.get_values(self._id))

    def _init_temp(self, initial):
        """ initializes _temp attribute. """
        self._temp = self._equivalent_builtin_class(initial)

    def _move_temp_to_backend(self):
        """
            When an object has been fully initialized this is called to move what is being held in '_temp'
            into the database.
        """
        if not self.still_temp() and self._temp is not None:
            for key, value in enumerate(self._temp):
                self._set(key, value)
            self._temp = None

    def _set_temp(self, key, value):
        """
            Used by '_set' when the object is not fully initialized
            and data is still being held in the '_temp' object.
        """
        # TODO mutmut will change value to None but PTuple raises TypeError, add test after implementing PList
        self._temp[key] = value

    def _get_temp(self, key):
        """
            Used by '_get' when an object is not fully initialized
            and data is still being held in the '_temp' object.
        """
        return self._temp[key]

    def _del_temp(self, key):
        """
            Used by '_del' when the object is not fully initialized
            and data is still being held in the '_temp' object.
        """
        del(self._temp[key])

    def __getitem__(self, key: Any) -> Any:
        """ implement: obj[index] and obj[first:last:step] """
        if self.still_temp():
            return self._temp[key]
        elif type(key) is not int and type(key) is not slice:
            raise TypeError(f"{self.__class__.__name__} indices must be integers or slices not {type(key).__name__}")
        elif type(key) is int:
            if key < 0:
                key = len(self) + key
            try:
                return self._get(key)
            except KeyError:
                raise IndexError(f"{self.__class__.__name__} index out of range")
        else:  # key is slice
            return self.in_memory()[key]

    def __contains__(self, item: Any) -> bool:
        """ implement: item in self """
        if self.still_temp():
            return item in self._temp
        else:
            return item in self._backend.get_values(self._id)

    def __add__(self, other, /):
        """ implement: self + other """
        if isinstance(other, BasePersistentObject):
            other = other.in_memory()
        return self.in_memory() + other

    def __radd__(self, other, /):
        """ implement: other + self """
        # no need to convert other if BasePersistentObject because adding only makes sense with tuples and PTuples
        # so only tuple + PTuple will use __radd__().
        return other + self.in_memory()

    def __mul__(self, other):
        """ implement: self * other """
        return self.in_memory() * other

    def __rmul__(self, other):
        """ implement: other * self """
        return other * self.in_memory()