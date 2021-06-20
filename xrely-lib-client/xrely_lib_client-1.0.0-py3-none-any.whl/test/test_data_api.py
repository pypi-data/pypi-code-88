# coding: utf-8

"""
    XRELY

    API Documentation for XRELY platform  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@xrely.com
    
"""


#from __future__ import absolute_import

from __future__ import print_function
import time
import xrely_lib_client
from xrely_lib_client.rest import ApiException
from pprint import pprint
import unittest

class TestDataApi(unittest.TestCase):
    """DataApi unit test stubs"""

    def setUp(self):
        self.api = xrely_lib_client.api.data_api.DataApi()  # noqa: E501
        self.body = xrely_lib_client.DataStoreRequest() # DataStoreRequest |  (optional)
        data_object = xrely_lib_client.DocStoreItem()
        data_object.keyword = "convonix kw-python"
        data_object.url = "http://www.convonix.com/convonix-python"
        map = {}
        map['type'] = "datatype"
        map['info'] = "website"
        data_object.data = map
        self.body.secret_key = "68ceece96a303ca6d4c1e9d01b674c02d4602681ebf344ef8e8b43f21cca4c03"
        arr_obj=[]
        arr_obj.append(data_object)
        self.body.docs = arr_obj

    def tearDown(self):
        pass

    def test_data_store_post(self):
        try:
            api_response = self.api.data_store_post(body=self.body)
            self.assertTrue(api_response.data.committed)
            self.assertEqual("1 documents inserted sucessfully!!",api_response.data.message)
        except ApiException as e:
            print("Exception when calling DataApi->data_store_post: %s\n" % e)

    def test_data_store_delete(self):
        try:
            api_response = self.api.data_store_delete(body=self.body)
            self.assertTrue(api_response.data.committed)
            self.assertEqual("1 documents deleted sucessfully!!",api_response.data.message)
        except ApiException as e:
            print("Exception when calling DataApi->data_store_delete: %s\n" % e)


if __name__ == '__main__':
    unittest.main()
