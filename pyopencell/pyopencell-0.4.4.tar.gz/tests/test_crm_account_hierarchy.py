import unittest2 as unittest
from mock import patch

from pyopencell.resources.crm_account_hierarchy import CRMAccountHierarchy

from .settings import REQUIRED_ENVVARS


class CRMAccountHierarchyTests(unittest.TestCase):

    @patch.dict('os.environ', REQUIRED_ENVVARS)
    @patch("pyopencell.resources.crm_account_hierarchy.Client.post")
    def test_create(self, client_post_mock):
        expected_response_data = {
            "status": "SUCCESS",
            "errorCode": "",
            "message": "",
        }
        client_post_mock.return_value = expected_response_data

        attributes = {
            "code": "hola"
        }

        response = CRMAccountHierarchy.create(**attributes)
        for key, value in expected_response_data.items():
            self.assertEquals(getattr(response, key), value)

        client_post_mock.assert_called_with(
            "{}/{}".format(CRMAccountHierarchy._url_path, 'createCRMAccountHierarchy'),
            body=attributes
        )

    @patch.dict('os.environ', REQUIRED_ENVVARS)
    @patch("pyopencell.resources.crm_account_hierarchy.Client.post")
    def test_update(self, client_post_mock):
        expected_response_data = {
            "status": "SUCCESS",
            "errorCode": "",
            "message": "",
        }
        client_post_mock.return_value = expected_response_data

        attributes = {
            "code": "hola"
        }

        response = CRMAccountHierarchy.update(**attributes)
        for key, value in expected_response_data.items():
            self.assertEquals(getattr(response, key), value)

        client_post_mock.assert_called_with(
            "{}/{}".format(CRMAccountHierarchy._url_path, 'createOrUpdateCRMAccountHierarchy'),
            body=attributes
        )
