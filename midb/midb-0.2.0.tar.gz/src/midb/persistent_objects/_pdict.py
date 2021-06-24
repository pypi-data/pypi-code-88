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
from typing import Any, Optional, Dict
from midb.persistent_objects import BasePersistentObject


class PDict(BasePersistentObject):
    """
        A persistent version of the built-in dict type.
    """
    _backend: Optional["midb.backend.SQLiteBackend"]
    _id: Optional[int]
    _temp: Optional[Dict]

    def __init__(self, initial_values={}, /, _backend=None, _id=None, **kwargs):
        _init_temp = {}
        _init_temp.update(initial_values)
        _init_temp.update(kwargs)
        BasePersistentObject.__init__(self, _backend=_backend, _id=_id, _init_temp=_init_temp)

    @classmethod
    def fromkeys(cls, iterable, value=None, /):
        """
            D.fromkeys(S[,v]) -> New PDict with keys from S and values equal to v.
            v defaults to None.
        """
        return PDict({key: value for key in iterable})

    def _init_temp(self, initial):
        """ This is called by '__init__' to initialize a temporary object. """
        self._temp = dict(initial)

    def _move_temp_to_backend(self):
        """
            When an object has been fully initialized this is called to move what is being held in '_temp'
            into the database.
        """
        if not self.still_temp() and self._temp is not None:
            for key, value in self._temp.items():
                self._set(key, value)
            self._temp = None

    def in_memory(self):
        """
            Returns an object that contains all the attributes of the persistent object but in memory
            instead of on disk.
        """
        if self.still_temp():
            return self._temp
        else:
            return dict(self.items())

    def _get_temp(self, key):
        """
            Used by '_get' when an object is not fully initialized
            and data is still being held in the '_temp' object.
        """
        return self._temp[key]

    def __getitem__(self, key: Any) -> Any:
        """
            implement: self[key]
        """
        if isinstance(key, (int, float, bool)) and int(key) == key:
            key = int(key)
        return self._get(key)


    def _set_temp(self, key, value):
        """
            Used by '_set' when the object is not fully initialized
            and data is still being held in the '_temp' object.
        """
        self._temp[key] = value

    def __setitem__(self, key: Any, value: Any):
        """ implement: self[key] = value """
        if isinstance(key, (int, float, bool)) and int(key) == key:
            key = int(key)
        self._set(key, value)

    def setdefault(self, key: Any, default=None, /):
        """
            Insert key with a value of default if key is not in the dictionary.
            Return the value for key if key is in the dictionary, else default.
        """
        try:
            return self[key]
        except KeyError:
            self[key] = default
            return default

    def update(self, E=None, **F):
        """
            If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
            If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
            In either case, this is followed by: for k in F:  D[k] = F[k]
        """
        if E is not None:
            if hasattr(E, "keys"):
                for key in E:
                    self[key] = E[key]
            else:
                for key, value in E:
                    self[key] = value
        for key in F:
            self[key] = F[key]

    def _del_temp(self, key):
        """
            Used by '_del' when the object is not fully initialized
            and data is still being held in the '_temp' object.
        """
        del(self._temp[key])

    def __delitem__(self, key: Any, /) -> None:
        """ implement: del(self[key]) """
        if isinstance(key, (int, float, bool)) and int(key) == key:
            key = int(key)
        self._del(key)

    def pop(self, key, /, *args):
        """
            D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
            If key is not found, d is returned if given, otherwise KeyError is raised
        """
        if len(args) > 1:
            raise TypeError(f'pop expected at most 2 arguments, got {len(args) + 1}')
        elif len(args) == 1:
            default = args[0]

        try:
            value = self[key]
            del self[key]
            return value
        except KeyError as e:
            try:
                return default
            except UnboundLocalError:
                raise e

    def popitem(self):
        """
            D.popitem() -> (k, v), remove and return some (key, value) pair as a
            2-tuple; but raise KeyError if D is empty.
        """
        if self.still_temp():
            return self._temp.popitem()
        else:
            last_item_key = list(self.keys())[-1]
            return_item = (last_item_key, self[last_item_key])
            del self[last_item_key]
            return return_item

    def clear(self):
        """ D.clear() -> None.  Remove all items from D. """
        if self.still_temp():
            self._temp.clear()
        else:
            self._backend.delete_all_children(self._id)

    def items(self):
        """ D.items() -> list of D's (key, value) pairs, as 2-tuples """
        if self.still_temp():
            return list(self._temp.items())
        else:
            items = self._backend.get_items(self._id)
            for k, v in items:
                if isinstance(v, BasePersistentObject):
                    v._backend = self._backend
            return items

