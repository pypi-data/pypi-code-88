import unittest2 as unittest
from mock import patch

from pyopencell.resources.customer import Customer


from .settings import REQUIRED_ENVVARS


class CustomerTests(unittest.TestCase):

    @patch.dict('os.environ', REQUIRED_ENVVARS)
    @patch("pyopencell.resources.customer.Client.get")
    def test_get(self, client_get_mock):
        expected_code = "some-customer-code"
        expected_response_data = {
            "customer": {
                "code": expected_code
            },
            "actionStatus": {
                "status": "SUCCESS",
                "errorCode": "",
                "message": "",
            }
        }
        client_get_mock.return_value = expected_response_data

        response = Customer.get(expected_code)

        for key, value in expected_response_data["customer"].items():
            self.assertEquals(getattr(response.customer, key), value)

        for key, value in expected_response_data["actionStatus"].items():
            self.assertEquals(getattr(response.action_status, key), value)

        client_get_mock.assert_called_with(Customer._url_path, customerCode=expected_code)

    @patch.dict('os.environ', REQUIRED_ENVVARS)
    @patch("pyopencell.resources.customer.Client.post")
    def test_create(self, client_post_mock):
        expected_response_data = {
            "status": "SUCCESS",
            "errorCode": "",
            "message": "",
        }
        client_post_mock.return_value = expected_response_data

        expected_code = "some-customer-code"

        customer_data = {
            "code": expected_code,
            "name": {
                "title": None,
                "firstName": "Nombre",
                "lastName": "Apellido"
            },
        }

        response = Customer.create(**customer_data)

        for key, value in expected_response_data.items():
            self.assertEquals(getattr(response, key), value)

        client_post_mock.assert_called_with(Customer._url_path, customer_data)

    @patch.dict('os.environ', REQUIRED_ENVVARS)
    @patch("pyopencell.resources.customer.Client.put")
    def test_update(self, client_put_mock):
        expected_response_data = {
            "status": "SUCCESS",
            "errorCode": "",
            "message": "",
        }
        client_put_mock.return_value = expected_response_data

        expected_code = "some-customer-code"

        customer_data = {
            "code": expected_code,
            "name": {
                "title": None,
                "firstName": "Nombre",
                "lastName": "Apellido"
            },
        }

        response = Customer.update(**customer_data)

        for key, value in expected_response_data.items():
            self.assertEquals(getattr(response, key), value)

        client_put_mock.assert_called_with(Customer._url_path, customer_data)
