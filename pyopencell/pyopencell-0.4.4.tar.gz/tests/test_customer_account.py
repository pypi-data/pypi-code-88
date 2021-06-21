# -*- coding: utf-8 -*-
import unittest2 as unittest
from mock import patch

from pyopencell.resources.customer_account import CustomerAccount

from .settings import REQUIRED_ENVVARS


class CustomerAccountTests(unittest.TestCase):
    @patch.dict('os.environ', REQUIRED_ENVVARS)
    @patch("pyopencell.resources.customer_account.Client.get")
    def test_get(self, client_get_mock):
        expected_code = "some-customer-code"
        expected_response_data = {
            "customerAccount": {
                "code": expected_code
            },
            "actionStatus": {
                "status": "SUCCESS",
                "errorCode": "",
                "message": "",
            }
        }
        client_get_mock.return_value = expected_response_data

        response = CustomerAccount.get(expected_code)

        for key, value in expected_response_data["customerAccount"].items():
            self.assertEquals(getattr(response.customerAccount, key), value)

        for key, value in expected_response_data["actionStatus"].items():
            self.assertEquals(getattr(response.action_status, key), value)

        client_get_mock.assert_called_with(
            CustomerAccount._url_path,
            customerAccountCode=expected_code
        )
