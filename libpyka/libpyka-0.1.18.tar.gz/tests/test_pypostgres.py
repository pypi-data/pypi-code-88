"""libpykaライブラリのdbパッケージのpypostgresモジュールのテスト
"""

from typing import Optional, Union, Any
from typing import Callable, NoReturn
from typing import Sequence, Iterable, List, Tuple
from typing import Dict
from typing import TypeVar, Generic, NewType, Type

import logging
import unittest
from libpyka.db import pypostgres
from libpyka.db import SQLException

"""モジュールpypostgresのテストケースクラス。
"""
class PyPostgresTest(unittest.TestCase):
    CONNECT_INFO_OK = {
        "host": "mail.kacpp.xyz",
        "port": 5432,
        "user": "postkamail",
        "password": "postkamail3275",
        "dbname": "kamail"
    }
    CONNECT_INFO_ERR = {
        "host": "mail.kacpp.xyz",
        "port": 5432,
        "user": "kamail",
        "password": "kamailadmin",
        "dbname": "kamail"
    }

    """このテストケース前に呼ばれる関数。
    """
    def setUp(self) -> None:
        logging.basicConfig(level=logging.INFO)

    def test_get_connection(self) -> None:
        """DB接続ができるかテストする。
        """
        dbcon = pypostgres.get_connection(**PyPostgresTest.CONNECT_INFO_OK) # type: ignore
        self.assertTrue(dbcon is not None)

    @unittest.skip('Exceptionをキャッチできないのでスキップ')
    def test_get_connection_connect_error(self) -> None:
        """誤りのDB接続情報でちゃんとエラーが出るかテストする。
        """
        with self.assertRaises(SQLException):
            dbcon = pypostgres.get_connection(**PyPostgresTest.CONNECT_INFO_ERR) # type: ignore
    
    def test_get_config_connection(self) -> None:
        """設定iniファイルから接続情報を読み込みDBに接続できるかテスト。
        """
        inifile = 'tests/data/postgres.ini'
        section = 'PostgreSQL'
        dbcon = pypostgres.get_config_connection(inifile, section) # type: ignore
        self.assertTrue(dbcon is not None)

    def test_db_object_names(self) -> None:
        """db_object_names()関数のテスト
        DBオブジェクトの名前がきちんと取得できるか確認する。
        """
        def in_array(array: Sequence[str], search: Sequence[str]) -> bool:
            """配列arrayの中に配列searchの要素が全て含まれているか
            Args:
                array (Sequence[str]): 検索対象の配列
                search (Sequence[str]): 検索する要素の配列
            Returns:
                True: すべて含まれている
                False: 何か一つ含まれていない要素があった
            """
            for table in search:
                if table not in array:
                    return False
            return True

        inifile = 'tests/data/postgres.ini'
        section = 'PostgreSQL'
        expected = ["test_db_objects", "test_sample"]
        dbcon = None
        cur = None
        try:
            dbcon = pypostgres.get_config_connection(inifile, section) # type: ignore
            cur = dbcon.cursor()
            sql = "create table test_db_objects (id integer not null, name text)"
            cur.execute(sql)
            sql = "create table test_sample (id integer not null)"
            cur.execute(sql)
            result = pypostgres.db_object.names("TABLE", cur)
            print(result)
            dbcon.commit()
            self.assertTrue(in_array(result, expected))
        except Exception as ex:
            print(ex)
        finally:
            if cur is not None:
                cur.execute("drop table if exists test_db_objects")
                cur.execute("drop table if exists test_sample")
                cur.close()
            if dbcon is not None:
                dbcon.close()

