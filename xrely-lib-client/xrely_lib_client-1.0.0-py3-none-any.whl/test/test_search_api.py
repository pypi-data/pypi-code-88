# coding: utf-8

"""
    XRELY

    API Documentation for XRELY platform  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@xrely.com
    
"""


#from __future__ import absolute_import
from __future__ import print_function
import unittest
from pprint import pprint
import time
import xrely_lib_client
from xrely_lib_client.rest import ApiException
import json
import ast

class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""
    api = xrely_lib_client.api.search_api.SearchApi()
    def setUp(self):
        self.api = xrely_lib_client.api.search_api.SearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_search_post(self):
        """Test case for search_post

        Provides relevant result for your query  # noqa: E501
        """
        pass

    def test_search_post_count(self):
        body = xrely_lib_client.SearchRequest()
        body.q='a'
        body.ak='c7a505fa518c566e111eb2532efc9685'
        body.size=10
        try:
            api_response = self.api.search_post(body)
            self.assertLessEqual(len(ast.literal_eval(str((api_response.data)['results']))),body.size)
        except ApiException as e:
            pprint("Exception when calling SearchApi->search_post: %s\n" % e)

    def test_search_post_code(self):
        body = xrely_lib_client.SearchRequest()
        body.q='a'
        body.ak='c7a505fa518c566e111eb2532efc9685'
        body.size=10
        try:
            api_response = self.api.search_post(body)
            self.assertEqual(0,int(api_response.code))
        except ApiException as e:
            pprint("Exception when calling SearchApi->search_post: %s\n" % e)


    def test_search_post_data(self):
        body = xrely_lib_client.SearchRequest()
        body.q='a'
        body.ak='c7a505fa518c566e111eb2532efc9685'
        body.size=10
        try:
            api_response = self.api.search_post(body)
            self.assertIsNotNone(api_response.data)
        except ApiException as e:
            pprint("Exception when calling SearchApi->search_post: %s\n" % e)

    def test_search_suggestions_get_count(self):
        q = 'a' # str | Search Term or Keyword
        ak = 'c7a505fa518c566e111eb2532efc9685' # str | Account Key
        size = 10 # int | Number Of Results Required (optional)
        try:
            api_response = self.api.search_suggestions_get(q, ak, size=size)
            self.assertLessEqual(len(ast.literal_eval(str((api_response.data)['results']))),size)
        except ApiException as e:
            pprint("Exception when calling SearchApi->search_suggestions_get: %s\n" % e)
        
    def test_search_suggestions_get_code(self):
        q = 'a' # str | Search Term or Keyword
        ak = 'c7a505fa518c566e111eb2532efc9685' # str | Account Key
        size = 10 # int | Number Of Results Required (optional)
        try:
            api_response = self.api.search_suggestions_get(q, ak, size=size)
            self.assertEqual(0,api_response.code)
        except ApiException as e:
            pprint("Exception when calling SearchApi->search_suggestions_get: %s\n" % e)


    def test_search_suggestions_get_data(self):
        q = 'a' # str | Search Term or Keyword
        ak = 'c7a505fa518c566e111eb2532efc9685' # str | Account Key
        size = 10 # int | Number Of Results Required (optional)
        try:
            api_response = self.api.search_suggestions_get(q, ak, size=size)
            self.assertIsNotNone(api_response.data)
        except ApiException as e:
            pprint("Exception when calling SearchApi->search_suggestions_get: %s\n" % e)


if __name__ == '__main__':
    unittest.main()
