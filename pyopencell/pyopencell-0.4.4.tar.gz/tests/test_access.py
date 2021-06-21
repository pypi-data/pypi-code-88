import unittest2 as unittest
from mock import patch

from pyopencell.resources.access import Access

from .settings import REQUIRED_ENVVARS


class AccessTests(unittest.TestCase):

    @patch.dict('os.environ', REQUIRED_ENVVARS)
    @patch("pyopencell.resources.customer.Client.get")
    def test_get(self, client_get_mock):
        expected_code = "some-access-code"
        expected_subscription_code = "some-subscription-code"

        Access.get(
            accessCode=expected_code,
            subscriptionCode=expected_subscription_code)

        client_get_mock.assert_called_with(
            Access._url_path,
            accessCode=expected_code,
            subscriptionCode=expected_subscription_code)

    @patch.dict('os.environ', REQUIRED_ENVVARS)
    @patch("pyopencell.resources.access.Client.post")
    def test_create(self, client_post_mock):
        expected_code = "some-access-code"

        access_data = {
            "code": expected_code,
            "subscriotion": "subs1",
            "startDate": None,
            "endDate": None,
            "disabled": False
        }

        Access.create(**access_data)

        client_post_mock.assert_called_with(Access._url_path, access_data)
