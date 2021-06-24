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
"""
midb.backend is where all the interaction with the SQLite database takes place.
"""
from typing import Sequence, List, Tuple, Any, Union
from abc import ABCMeta
import sqlite3

from midb.constants import MEMORY_DB, DEFAULT_ROOT_CLASS_ID
from midb.backend._serialization import SerializationPair, register_new_serialization_pair, get_class_id
from midb.backend._serialization import serialize, deserialize
from midb.backend._db_creation_and_validation import valid_db, create_db, _run_sql


class SQLiteBackend:
    """
    An SQLiteBackend object maintains a connection to the database in use together with other information
    related to the state. It is used as the way to interact with the database.
    """
    def __init__(self, filename: str = MEMORY_DB,
                 root_class: Union[str,type] = DEFAULT_ROOT_CLASS_ID,
                 auto_commit: bool = True, custom_persistent_object_types=[]):
        self.filename = filename
        if type(root_class) == type or type(root_class) is ABCMeta:
            root_class_id = get_class_id(root_class)
        else:
            root_class_id = root_class
        self.auto_commit = auto_commit
        self.connection = sqlite3.connect(self.filename)
        if not valid_db(connection=self.connection):
            self.connection = create_db(filename, root_class_id)
        from midb import PDict, PTuple
        for cls in custom_persistent_object_types + [PDict, PTuple]:
            sp = SerializationPair(cls, cls._string_serializer, cls._string_deserializer)
            register_new_serialization_pair(sp)

    def __repr__(self):
        """
        Return repr(self).
        """
        return f'{self.__class__.__name__}(filename="{self.filename}")'

    def __str__(self):
        """
        Return str(self).
        """
        return self.__repr__()

    def commit(self) -> None:
        """ performs a commit on the SQL connection. """
        self.connection.commit()

    def commit_if_auto(self) -> None:
        """ Performs a commit if the database is setup to perform auto-commits (default) """
        if self.auto_commit:
            self.commit()

    # PERSISTENT OBJECT METHODS #
    def add_new_persistent_object(self, class_id:str, commit=True) -> int:
        """ creates a new record for a new Persistent Object and returns it's id. """
        new_id, _ = _run_sql(self.connection, "INSERT INTO persistent_objects (type) VALUES (?)", [class_id])
        if commit:
            self.commit_if_auto()
        return new_id

    @property
    def root(self) -> "midb.persistent_objects.BasePersistentObject":
        """ returns the root object for the database. """
        sql = "SELECT type from persistent_objects WHERE id = 0"
        _, result = _run_sql(self.connection, sql)
        if len(result) >= 1:
            return_root = deserialize(result[0][0], "0")
            return_root._backend = self
            return return_root

    # KEY_VALUE METHODS #
    def get(self, parent_id: int, key: Any) -> Any:
        """ from the parent object id and the key object return the value held there. """
        sql = "SELECT value_type, value FROM key_value where parent_id IS ? AND key_type IS ? AND key IS ?"
        sql_values = [parent_id, *serialize(key)]
        _, result = _run_sql(self.connection, sql, sql_values)
        if len(result) > 0:
            return_value = deserialize(*result[0])
            return return_value

        else:
            raise KeyError(str(key))

    #def get_multiple(self, parent_id, keys: list) -> List:
    #    """ Returns a list of objects from the parent object's id and a list of keys. """
    #    return_list = []
    #    for key in keys:
    #        return_list.append(self.get(parent_id, key))
    #    return return_list

    def key_exists(self, parent_id: int, key: Any) -> bool:
        """ returns True if a key exists in the parent object and False otherwise. """
        try:
            self.get(parent_id, key)
        except KeyError:
            return False
        return True

    def set(self, parent_id: int, key: Any, value: Any, commit: bool = True) -> None:
        """ sets a parent objects key to the value provided. """
        if self.key_exists(parent_id, key):
            sql = "UPDATE key_value SET value_type = ?, value = ? where parent_id IS ? AND key_type IS ? AND key IS ?"
            sql_values = [*serialize(value), parent_id, *serialize(key)]
            _run_sql(self.connection, sql, sql_values)
        else:
            sql = "INSERT INTO key_value VALUES (?, ?, ?, ?, ?)"
            sql_values = [parent_id, *serialize(key), *serialize(value)]
            _run_sql(self.connection, sql, sql_values)
        if commit:
            self.commit_if_auto()

    def delete(self, parent_id: int, key: Any, commit: bool = True) -> None:
        """ deletes the provided key from the parent """
        current_value = self.get(parent_id, key)
        from midb.persistent_objects import BasePersistentObject
        if isinstance(current_value, BasePersistentObject):
            sql = "SELECT * FROM key_value WHERE value_type IS ? and value IS ?"
            sql_values = [*serialize(current_value)]
            _, results = _run_sql(self.connection, sql, sql_values)
            number_of_copies = len(results)
            if number_of_copies == 1:
                sql = "DELETE FROM key_value WHERE parent_id IS ?"
                sql_values = [current_value._id]
                _run_sql(self.connection, sql, sql_values)
                sql = "DELETE FROM persistent_objects WHERE id IS ?"
                _run_sql(self.connection, sql, sql_values)
        sql = "DELETE FROM key_value WHERE parent_id IS ? AND key_type IS ? AND key IS ?"
        sql_values = [parent_id, *serialize(key)]
        _run_sql(self.connection, sql, sql_values)
        if commit:
            self.commit_if_auto()

    def delete_all_children(self, parent_id: int, commit: bool = True):
        """ deletes all keys from a parent. """
        keys = self.get_keys(parent_id)
        for key in keys:
            self.delete(parent_id, key, commit=False)
        if commit:
            self.commit_if_auto()

    def get_keys(self, parent_id: int) -> List:
        """ returns a list of all the keys contained in the parent """
        sql = "SELECT key_type, key FROM key_value WHERE parent_id IS ?"
        sql_values = [parent_id]
        _, results = _run_sql(self.connection, sql, sql_values)
        return_keys = []
        for row in results:
            return_keys.append(deserialize(*row))
        return return_keys

    def get_values(self, parent_id: int) -> List:
        """ returns all the values held in they keys of the parent """
        sql = "SELECT value_type, value FROM key_value WHERE parent_id IS ?"
        sql_values = [parent_id]
        _, results = _run_sql(self.connection, sql, sql_values)
        return_values = []
        for row in results:
            return_values.append(deserialize(*row))
        return return_values

    def get_items(self, parent_id: int) -> Any:
        """ returns a tuple of 2 tuples containing all the key-value pairs in the parent """
        sql = "SELECT key_type, key, value_type, value FROM key_value WHERE parent_id IS ?"
        sql_values = [parent_id]
        _, results = _run_sql(self.connection, sql, sql_values)
        return_values = []
        for row in results:
            key_type_id = row[0]
            key_serialization_str = row[1]
            value_type_id = row[2]
            value_serialization_str = row[3]
            key = deserialize(key_type_id, key_serialization_str)
            value = deserialize(value_type_id, value_serialization_str)
            return_values.append((key, value))
        return tuple(return_values)