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
from midb.persistent_objects import PDict
import midb.backend
from midb.constants import MEMORY_DB
from midb.persistent_objects import PDict
from midb.persistent_objects import PTuple

DEFAULT_ROOT_CLASS = PDict


def get_root(filename=midb.backend.MEMORY_DB,
             root_type=DEFAULT_ROOT_CLASS,
             custom_persistent_object_types=[]):
    """
    Primary access into using midb as a backend. Accesses a backend file and creates it if it
    does not exist. Then it returns the root object. The 'root_type' argument is ignored if a
    database file already exists and has a root object defined. The type of the root object in
    that case will be what is defined in the database.

    :param filename: filename of the backend database
    :param root_type: the class of the root of the database
    :param custom_persistent_object_types: any additional custom types that will be used.
    :return: a persistent object class that is the root object of the database
    """
    backend = midb.backend.SQLiteBackend(filename=filename,
                                         root_class=root_type,
                                         custom_persistent_object_types=custom_persistent_object_types)
    return backend.root


def get_backend(filename=MEMORY_DB,
                root_type=DEFAULT_ROOT_CLASS,
                custom_persistent_object_types=[]):
    """
    Similar to get_root() above but returns the backend instead of the root object. This is for use when
    more hands on control of the process is needed.

    :param filename: filename of the backend database
    :param root_type: the class of the root of the database
    :param custom_persistent_object_types: any additional custom types that will be used.
    :return: an SQLiteBackend
    """
    return midb.backend.SQLiteBackend(filename=filename,
                                      root_class=root_type,
                                      custom_persistent_object_types=custom_persistent_object_types)



