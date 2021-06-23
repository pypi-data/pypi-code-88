"""
**Warning**
In order to execute those tests correctly please make sure data is already placed
under the specified location /schema_name/table_name.
(You can easily do this by running the `test_iris_using_database_connection.py` before those tests).
"""


import unittest

from ibm_watson_machine_learning.tests.utils import is_cp4d
from ibm_watson_machine_learning.tests.autoai.svt.abstract_test_iris_using_database_data_asset import\
    AbstractTestAutoAIConnectedAsset


@unittest.skipIf(not is_cp4d(), "Not supported on Cloud")
class TestAutoAIMSSQLServer(AbstractTestAutoAIConnectedAsset, unittest.TestCase):
    database_name = "sqlserver"
    schema_name = "connections"


@unittest.skipIf(not is_cp4d(), "Not supported on Cloud")
class TestAutoAIDB2(AbstractTestAutoAIConnectedAsset, unittest.TestCase):
    database_name = "db2"
    schema_name = "CJB94327"
    table_name = "IRIS"


@unittest.skipIf(not is_cp4d(), "Not supported on Cloud")
class TestAutoAIPostgresSQL(AbstractTestAutoAIConnectedAsset, unittest.TestCase):
    database_name = "postgresql"
    schema_name = "public"


@unittest.skipIf(not is_cp4d(), "Not supported on Cloud")
@unittest.skip("The writing of training data is broken for now.")
class TestAutoAIMySQL(AbstractTestAutoAIConnectedAsset, unittest.TestCase):
    database_name = "mysql"
    schema_name = "mysql"


if __name__ == "__main__":
    unittest.main()
