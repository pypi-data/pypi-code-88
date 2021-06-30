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

from typing import Optional, Tuple, Type
import midb
from midb.persistent_objects import PersistentSequence


class PTuple(PersistentSequence):
    """ A persistent version of the built-in tuple type. """
    _backend: Optional["midb.backend.SQLiteBackend"]
    _id: Optional[int]
    _temp: Optional[Tuple]

    @property
    def _equivalent_builtin_class(self) -> Type:
        """ return tuple, the built-in class that PTuple is emulating """
        return tuple

    def __hash__(self) -> int:
        """ implement: hash(self) """
        return hash(self.in_memory())