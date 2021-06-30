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
from typing import Optional, Any, Union, Iterable, Iterator, Sequence, Type, Tuple, List, cast
import midb
from midb.backend import SQLiteBackend
from midb.persistent_objects import BasePersistentObject

Sequences = Union[Sequence, "PersistentSequence"]  # pragma: no mutate

class PersistentSequence(BasePersistentObject, ABC):
    """
        PersistentSequence is the abstract base class for list and tuple.
    """
    _backend: Optional["midb.backend.SQLiteBackend"]
    _id: Optional[int]
    _temp: Optional[Union[List, Tuple]]

    @property
    @abstractmethod
    def _equivalent_builtin_class(self) -> Type:
        """ return the built-in class that the sub-class is emulating (tuple or list) """

    def __init__(self, iterator: Iterable = (), _backend: "midb.backend.SQLiteBackend" = None, _id: Optional[int] = None):
        """
            Takes an iterator for initializing during temp state and _backend and _id for
            full disk usage state.
        """
        _init_temp = self._equivalent_builtin_class(iterator)
        BasePersistentObject.__init__(self, _backend=_backend, _id=_id, _init_temp=_init_temp)

    def in_memory(self) -> Sequences:
        """ Returns in-memory built-in type equivelent of the persistent object. """
        if self.still_temp():
            _temp = cast(Sequence, self._temp)
            return _temp
        else:
            _backend = cast(SQLiteBackend, self._backend)
            _id = cast(int, self._id)
            items = list(_backend.get_items(_id))
            items.sort()
            values = [value for key, value in items]
            return self._equivalent_builtin_class(values)

    def _init_temp(self, initial: Iterator) -> None:
        """ initializes _temp attribute. """
        self._temp = self._equivalent_builtin_class(initial)

    def _move_temp_to_backend(self) -> None:
        """
            When an object has been fully initialized this is called to move what is being held in '_temp'
            into the database.
        """
        if not self.still_temp() and self._temp is not None:
            for key, value in enumerate(self._temp):
                self._set(key, value)
            self._temp = None

    def _set_temp(self, key: int, value: Any) -> None:
        """
            Used by '_set' when the object is not fully initialized
            and data is still being held in the '_temp' object.
        """
        try:
            self._temp[key] = value # type: ignore[index]
        except IndexError as e:
            raise IndexError(f"{self.__class__.__name__} assignment index out of range")

    def _get_temp(self, key: int) -> Any:
        """
            Used by '_get' when an object is not fully initialized
            and data is still being held in the '_temp' object.
        """
        _temp = cast(Sequence, self._temp)
        return _temp[key]

    def _del_temp(self, key: int) -> None:
        """
            Used by '_del' when the object is not fully initialized
            and data is still being held in the '_temp' object.
        """
        del(self._temp[key])  # type: ignore

    def __getitem__(self, key: int) -> Any:
        """ implement: obj[index] and obj[first:last:step] """
        if self.still_temp():
            _temp = cast(Sequence, self._temp)
            return _temp[key]
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
            _temp = cast(Sequence, self._temp)
            return item in _temp
        else:
            _backend = cast(SQLiteBackend, self._backend)
            _id = cast(int, self._id)
            return item in _backend.get_values(_id)

    def __add__(self, other: Sequences, /) -> Sequences:
        """ implement: self + other """
        if isinstance(other, BasePersistentObject):
            other = other.in_memory()
        return self.in_memory() + other  # type: ignore # intentionally raising exception when types are wrong

    def __radd__(self, other: Sequences, /) -> Sequences:
        """ implement: other + self """
        # no need to convert other if BasePersistentObject because adding only makes sense with tuples and PTuples
        # so only tuple + PTuple will use __radd__().
        return other + self.in_memory()   # type: ignore # intentionally raising exception when types are wrong

    def __mul__(self, other: int) -> Union[Tuple, List]:
        """ implement: self * other """
        return self.in_memory() * other  # type: ignore # intentionally raising exception when types are wrong

    def __rmul__(self, other: int) -> Union[Tuple, List]:
        """ implement: other * self """
        return other * self.in_memory()  # type: ignore # intentionally raising exception when types are wrong
