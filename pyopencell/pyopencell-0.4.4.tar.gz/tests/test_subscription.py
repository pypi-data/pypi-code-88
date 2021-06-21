import unittest2 as unittest
from mock import patch

from pyopencell.resources.subscription import Subscription
from pyopencell.responses.action_status import ActionStatus

from .settings import REQUIRED_ENVVARS


@patch.dict('os.environ', REQUIRED_ENVVARS)
class SubscriptionTests(unittest.TestCase):

    @patch("pyopencell.resources.subscription.Client.get")
    def test_get_not_subscription_returned(self, client_get_mock):
        expected_code = "some-sub-code"
        expected_response_data = {
            "status": "FAIL",
            "errorCode": "",
            "message": "",
        }
        client_get_mock.return_value = expected_response_data

        response = Subscription.get(expected_code)

        client_get_mock.assert_called_with(Subscription._url_path, subscriptionCode=expected_code)
        self.assertIsInstance(response, ActionStatus)

    @patch("pyopencell.resources.subscription.Client.get")
    def test_get(self, client_get_mock):
        expected_code = "some-sub-code"
        expected_response_data = {
            "subscription": {
                "code": expected_code
            },
            "actionStatus": {
                "status": "SUCCESS",
                "errorCode": "",
                "message": "",
            }
        }
        client_get_mock.return_value = expected_response_data

        response = Subscription.get(expected_code)

        for key, value in expected_response_data["subscription"].items():
            self.assertEquals(getattr(response.subscription, key), value)

        for key, value in expected_response_data["actionStatus"].items():
            self.assertEquals(getattr(response.action_status, key), value)

        client_get_mock.assert_called_with(Subscription._url_path, subscriptionCode=expected_code)

    @patch("pyopencell.resources.subscription.Client.post")
    def test_create(self, client_post_mock):
        attributes = {
            "code": "hola"
        }

        Subscription.create(**attributes)

        client_post_mock.assert_called_with(
            Subscription._url_path,
            attributes
        )

    @patch("pyopencell.resources.subscription.Client.post")
    def test_activate(self, client_post_mock):
        services_to_activate = [
            {
                "service": "foO",
                "quantity": 1,
                "subscriptionDate": "XX/XX/XXXX"
            }
        ]

        subscription = Subscription()
        subscription.code = 1
        subscription.activate(services_to_activate)

        client_post_mock.assert_called_with(
            "{}/{}".format(subscription._url_path, "activateServices"),
            {
                "subscription": 1,
                "servicesToActivate": {
                    "service": services_to_activate
                }
            }
        )

    @patch("pyopencell.resources.subscription.Client.post")
    def test_terminate(self, client_post_mock):
        termination_date = "2019-01-25"

        subscription = Subscription()
        subscription.code = 1
        subscription.terminate(termination_date)

        client_post_mock.assert_called_with(
            "{}/{}".format(subscription._url_path, "terminate"),
            {
                "subscriptionCode": subscription.code,
                "terminationDate": termination_date,
                "terminationReason": "CC_TERMINATION"
            }
        )

    @patch("pyopencell.resources.subscription.Client.post")
    def test_terminate_services(self, client_post_mock):
        termination_date = "2019-01-25"
        services = ["service-code-1", "service-code-2"]

        subscription = Subscription()
        subscription.code = 1
        subscription.terminateServices(termination_date, services)

        client_post_mock.assert_called_with(
            "{}/{}".format(subscription._url_path, "terminateServices"),
            {
                "subscriptionCode": subscription.code,
                "terminationDate": termination_date,
                "terminationReason": "CC_TERMINATION",
                "services": services,
            }
        )

    @patch("pyopencell.resources.subscription.Client.post")
    def test_apply_one_shot_charge(self, client_post_mock):
        one_shot_charge_code = "FoOo"

        subscription = Subscription()
        subscription.code = 1
        subscription.applyOneShotCharge(one_shot_charge_code)

        client_post_mock.assert_called_with(
            "{}/{}".format(subscription._url_path, "applyOneShotChargeInstance"),
            {
                "subscription": subscription.code,
                "oneShotCharge": one_shot_charge_code,
            }
        )

    @patch("pyopencell.resources.subscription.Client.post")
    def test_apply_one_shot_charge_with_amount(self, client_post_mock):
        one_shot_charge_code = "FoOo"
        amountWithoutTax = -123.4567

        subscription = Subscription()
        subscription.code = 1
        subscription.applyOneShotCharge(one_shot_charge_code, amountWithoutTax)

        client_post_mock.assert_called_with(
            "{}/{}".format(subscription._url_path, "applyOneShotChargeInstance"),
            {
                "subscription": subscription.code,
                "oneShotCharge": one_shot_charge_code,
                "amountWithoutTax": amountWithoutTax
            }
        )
