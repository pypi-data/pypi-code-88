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
    midb.backend._db_creation_and_validation handles the creation ond validation of midb SQLite databases.
"""
from typing import Tuple, List, Optional, Sequence
import sqlite3
from midb.constants import MEMORY_DB, DEFAULT_ROOT_CLASS_ID
from midb.backend._serialization import ClassID

def _run_sql(connection: sqlite3.Connection, sql: str, sql_values: Sequence = ()) -> Tuple[int, List]:
    """
    :param connection:  a SQLite3.Connection object
    :param sql:         the SQL to run with '?' for each input data location
    :param sql_values:  a Sequence of values to place in the '?' place holders.
    :return:            returns a 2 tuple containing lastrowid and results returned from the running of the SQL statement
    """
    cursor = connection.execute(sql, sql_values)
    result = cursor.fetchall()
    new_id = cursor.lastrowid
    return new_id, result


def create_db(filename: str = MEMORY_DB, root_obj_class_id: ClassID = DEFAULT_ROOT_CLASS_ID) -> sqlite3.Connection:
    """
    :param filename:            the filename of where the SQLite database will be stored
    :param root_obj_class_id:   the class object id (as returned by midb.backend._serialization.get_class_id())
                                    of the object to be used as the root object (id=0).
    :return:                    returns a connection to the database
    """
    con = sqlite3.connect(filename)
    _run_sql(con, "PRAGMA journal_mode=WAL")
    # self._run_sql('PRAGMA foreign_keys = ON')
    _run_sql(con, "CREATE TABLE IF NOT EXISTS persistent_objects (id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT)")
    _run_sql(con, "CREATE TABLE IF NOT EXISTS  key_value ("
                      "parent_id INTEGER, "
                      "key_type TEXT, "
                      "key TEXT, "
                      "value_type TEXT, "
                      "value TEXT)")
    values = [root_obj_class_id]
    _run_sql(con, "INSERT OR REPLACE INTO persistent_objects VALUES (0, ?)", sql_values=values)
    con.commit()
    return con


def valid_db(connection: sqlite3.Connection) -> bool:
    """
    returns True if a properly constructed database is found.
    return False if necessary tables are missing (correctable).
    raises ValueError in necessary tables exist but are structured incorrectly (not correctable)
    """
    persistent_objects_table_exists = _persistent_objects_table_exists(connection)
    persistent_objects_table_valid = _persistent_objects_table_valid(connection)
    persistent_objects_table_has_root_record = _persistent_objects_table_has_root_record(connection)
    key_value_table_exists = _key_value_table_exists(connection)
    key_value_table_valid = _key_value_table_valid(connection)

    if (
            persistent_objects_table_exists
            and persistent_objects_table_valid
            and persistent_objects_table_has_root_record
            and key_value_table_exists
            and key_value_table_valid
    ):
        return True
    elif ((persistent_objects_table_exists and not persistent_objects_table_valid)
            or
            (key_value_table_exists and not key_value_table_valid)):
        raise ValueError("incompatible database.")
    else:
        return False


def _persistent_objects_table_exists(connection: sqlite3.Connection) -> bool:
    _, result = _run_sql(connection, "SELECT tbl_name FROM sqlite_master WHERE tbl_name IS 'persistent_objects'")
    if len(result) > 0:
        return True
    else:
        return False


def _persistent_objects_table_valid(connection: sqlite3.Connection) -> bool:
    _, result = _run_sql(connection, "SELECT sql FROM sqlite_master WHERE tbl_name IS 'persistent_objects'")
    try:
        if result[0][0] == "CREATE TABLE persistent_objects (id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT)":
            return True
    except IndexError:
        pass
    return False


def _persistent_objects_table_has_root_record(connection: sqlite3.Connection) -> bool:
    try:
        _, result = _run_sql(connection, "SELECT * FROM persistent_objects WHERE id = 0")
        if len(result) == 1:
            return True
    except sqlite3.OperationalError:
        pass
    return False


def _key_value_table_exists(connection: sqlite3.Connection) -> bool:
    _, result = _run_sql(connection, "SELECT tbl_name FROM sqlite_master WHERE tbl_name IS 'key_value'")
    if len(result) > 0:
        return True
    else:
        return False


def _key_value_table_valid(connection: sqlite3.Connection) -> bool:
    _, result = _run_sql(connection, "SELECT sql FROM sqlite_master WHERE tbl_name IS 'key_value'")
    try:
        if result[0][0] == ("CREATE TABLE key_value ("
                                "parent_id INTEGER, "
                                "key_type TEXT, "
                                "key TEXT, "
                                "value_type TEXT, "
                                "value TEXT)"):
            return True
    except IndexError:
        pass
    return False

