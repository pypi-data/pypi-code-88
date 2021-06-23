import unittest
from ibm_watson_machine_learning.tests.utils import is_cp4d
from ibm_watson_machine_learning.tests.autoai.svt.abstract_test_iris_using_database_connection import\
    AbstractTestAutoAIDatabaseConnection


@unittest.skipIf(not is_cp4d(), "Not supported on Cloud")
class TestAutoAIMSSQLServer(AbstractTestAutoAIDatabaseConnection, unittest.TestCase):
    database_name = "sqlserver"
    schema_name = "connections"


@unittest.skipIf(not is_cp4d(), "Not supported on Cloud")
class TestAutoAIDB2(AbstractTestAutoAIDatabaseConnection, unittest.TestCase):
    database_name = "db2"
    schema_name = "CJB94327"
    table_name = "IRIS"


@unittest.skipIf(not is_cp4d(), "Not supported on Cloud")
class TestAutoAIPostgresSQL(AbstractTestAutoAIDatabaseConnection, unittest.TestCase):
    database_name = "postgresql"
    schema_name = "public"


@unittest.skipIf(not is_cp4d(), "Not supported on Cloud")
@unittest.skip("The writing of training data is broken for now.")
class TestAutoAIMySQL(AbstractTestAutoAIDatabaseConnection, unittest.TestCase):
    database_name = "mysql"
    schema_name = "mysql"


if __name__ == "__main__":
    unittest.main()
