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

from typing import Type, Any, Optional, Union, Iterable, List, cast, Callable
import midb
from midb.backend import SQLiteBackend
from midb.persistent_objects import PersistentSequence
from midb.persistent_objects._persistentsequence import Sequences


class PList(PersistentSequence):
    """ A persistent version of the built-in list type. """
    _backend: Optional["midb.backend.SQLiteBackend"]
    _id: Optional[int]
    _temp: Optional[List]

    @property
    def _equivalent_builtin_class(self) -> Type:
        """ return list, the built-in class that PList is emulating """
        return list

    def __setitem__(self, key: Any, value: Any) -> None:
        """ implement: self[key] """
        if self.still_temp():
            self._set_temp(key, value)
        elif type(key) is not int and type(key) is not slice:
            raise TypeError(f"{self.__class__.__name__} indices must be integers or slices, not {key.__class__.__name__}")
        elif type(key) is int:
            if key >= len(self):
                raise IndexError(f"{self.__class__.__name__} assignment index out of range")
            elif key < 0:
                key = len(self) + key
                if key < 0:
                    raise IndexError(f"{self.__class__.__name__} assignment index out of range")
            self._set(key, value)
        else:  # key is slice
            slice_ = key
            try:
                iter(value)
            except TypeError:
                raise TypeError("can only assign an iterable")
            start, stop, step = slice_.indices(len(self))
            if step == 1:
                del(self[slice_])
                for k, v in enumerate(value):
                    self.insert(start + k, v)
            else:  # extended slice
                indices_to_set = list(range(start, stop, step))
                if len(indices_to_set) != len(value):
                    raise ValueError(f"attempt to assign sequence of size {len(value)} to extended slice of size {len(indices_to_set)}")
                for k, v in zip(indices_to_set, value):
                    self._set(k, v)

    def __delitem__(self, key: Any) -> None:
        """ implement: del self[key] """
        if self.still_temp():
            _temp = cast(List, self._temp)
            del _temp[key]
        else:
            _backend = cast(SQLiteBackend, self._backend)
            _id = cast(int, self._id)
            if type(key) is not int and type(key) is not slice:
                raise TypeError(f"{self.__class__.__name__} indices must be integers or slices, not {key.__class__.__name__}")
            elif type(key) is int:
                if key < 0:
                    key = len(self) + key
                if not (0 <= key < len(self)):
                    raise IndexError(f"{self.__class__.__name__} assignment index out of range")
                _backend.list_del_item(_id, key)
            else:  # slice
                slice_ = key
                indices_to_delete = list(range(*slice_.indices(len(self))))
                _backend.list_del_multiple(_id, indices_to_delete)

    def append(self, value: Any) -> None:
        """ Append object to the end of the list. """
        if self.still_temp():
            _temp = cast(List, self._temp)
            _temp.append(value)
        else:
            _backend = cast(SQLiteBackend, self._backend)
            _id = cast(int, self._id)
            key = len(_backend.get_keys(_id))
            self._set(key, value)

    def insert(self, index: int, value: Any) -> None:
        """ Insert object before index. """
        if self.still_temp():
            _temp = cast(List, self._temp)
            _temp.insert(index, value)
        else:
            _backend = cast(SQLiteBackend, self._backend)
            _id = cast(int, self._id)
            _backend.list_insert(_id, index, value)

    def __iadd__(self, other: Sequences) -> Sequences:
        """ implement: self += other """
        for v in other:
            self.append(v)
        return self

    def clear(self) -> None:
        """ Remove all items from list. """
        if self.still_temp():
            _temp = cast(List, self._temp)
            _temp.clear()
        else:
            _backend = cast(SQLiteBackend, self._backend)
            _id = cast(int, self._id)
            _backend.delete_all_children(_id)

    def copy(self) -> List:
        """ Return a shallow copy of the list. """
        copy = cast(List, self.in_memory())
        return copy

    def extend(self, iterable: Iterable, /) -> None:
        """ Extend list by appending elements from the iterable. """
        if self.still_temp():
            _temp = cast(List, self._temp)
            _temp.extend(iterable)
        else:
            _backend = cast(SQLiteBackend, self._backend)
            _id = cast(int, self._id)
            start = len(self)
            for i, value in enumerate(iterable):
                _backend.list_insert(_id, start + i, value, commit=False)
                _backend.commit()

    def pop(self, index: int = -1, /) -> Any:
        """
            Remove and return item at index (default last).
            Raises IndexError if list is empty or index is out of range.
        """
        if self.still_temp():
            _temp = cast(List, self._temp)
            return _temp.pop(index)
        else:
            _backend = cast(SQLiteBackend, self._backend)
            _id = cast(int, self._id)
            if index < 0:  # pragma: no mutate # mutmut changes "<" to "<=" which both have same result so can't test
                index = len(self) + index
            value = _backend.get(_id, index)
            _backend.list_del_item(_id, index)
            return value

    def remove(self, value: Any, /) -> None:
        """
            Remove first occurrence of value.
            Raises ValueError if the value is not present.
        """
        self.pop(self.index(value))

    def sort(self, /, *, key: Optional[Callable] = None, reverse: bool = False) -> None:
        """
            Sort the list in ascending order and return None.

            The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
            order of two equal elements is maintained).

            If a key function is given, apply it once to each list item and sort them,
            ascending or descending, according to their function values.

            The reverse flag can be set to sort in descending order.
        """
        if self.still_temp():
            _temp = cast(List, self._temp)
            _temp.sort()
        else:
            _backend = cast(SQLiteBackend, self._backend)
            _id = cast(int, self._id)
            values = cast(List, self.in_memory())
            values.sort(key=key, reverse=reverse)
            for index, value in enumerate(values):
                _backend.set(_id, index, value, commit=False)
            _backend.commit()
