import unittest
from test.test_utils import make_test_atlas


class TestLimit(unittest.TestCase):

    def setUp(self):
        atlas = make_test_atlas()
        test_provider = atlas.sys_connection()
        self.test_query = test_provider.select('*')

    def test_setup_view_sql(self):
        expected_sql = """@x = 
use Sys.Admin.SetupView
--provider=Test.Provider_Name
--------------

select
  [Name], [Value] 
from
  Sys.Connection

enduse;

select * from @x;"""
        setup_sql = self.test_query.setup_view("Test.Provider_Name").get_sql()
        self.assertEqual(expected_sql, setup_sql)