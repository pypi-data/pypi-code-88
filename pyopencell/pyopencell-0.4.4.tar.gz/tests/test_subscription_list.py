from mock import patch
import unittest2 as unittest

from pyopencell.resources.subscription_list import SubscriptionList
from pyopencell.resources.subscription import Subscription
from pyopencell.responses.action_status import ActionStatus

from .settings import REQUIRED_ENVVARS


@patch.dict("os.environ", REQUIRED_ENVVARS)
class SubscriptionListTests(unittest.TestCase):
    @patch("pyopencell.resources.subscription.Client.get")
    def test_get_status_not_success(self, client_get_mock):
        expected_response_data = {"status": "FAIL", "errorCode": "", "message": ""}

        client_get_mock.return_value = expected_response_data

        response = SubscriptionList.get()

        self.assertIsInstance(response, ActionStatus)

    @patch("pyopencell.resources.subscription.Client.get")
    def test_get(self, client_get_mock):
        expected_response_data = {
            "paging": {
                "fullTextFilter": "...",
                "filters": {"property1": {}, "property2": {}},
                "fields": "...",
                "offset": 12345,
                "limit": 12345,
                "sortBy": "...",
                "sortOrder": "ASCENDING",
                "totalNumberOfRecords": 12345,
                "loadReferenceDepth": 12345,
            },
            "subscriptions": {
                "listSize": 12345,
                "subscription": [
                    {
                        "id": 12345,
                        "code": "...",
                        "auditable": {},
                        "auditableField": [{}, {}],
                        "description": "...",
                        "updatedCode": "...",
                        "userAccount": "...",
                        "offerTemplate": "...",
                        "subscriptionDate": 12345,
                        "terminationDate": 12345,
                        "endAgreementDate": 12345,
                        "status": "CREATED",
                        "statusDate": 12345,
                        "customFields": {},
                        "accesses": {},
                        "services": {},
                        "products": {},
                        "productInstance": [{}, {}],
                        "terminationReason": "...",
                        "orderNumber": "...",
                        "minimumAmountEl": "...",
                        "minimumAmountElSpark": "...",
                        "minimumLabelEl": "...",
                        "minimumLabelElSpark": "...",
                        "subscribedTillDate": 12345,
                        "renewed": True,
                        "renewalNotifiedDate": 12345,
                        "renewalRule": {},
                        "billingCycle": "...",
                        "seller": "...",
                        "autoEndOfEngagement": True,
                        "ratingGroup": "...",
                        "electronicBilling": True,
                        "email": "...",
                        "mailingType": "...",
                        "emailTemplate": "...",
                        "ccedEmails": "...",
                        "discountPlanForInstantiation": [{}, {}],
                        "discountPlanForTermination": ["...", "..."],
                        "discountPlanInstance": [{}, {}],
                    },
                    {
                        "id": 12345,
                        "code": "...",
                        "auditable": {},
                        "auditableField": [{}, {}],
                        "description": "...",
                        "updatedCode": "...",
                        "userAccount": "...",
                        "offerTemplate": "...",
                        "subscriptionDate": 12345,
                        "terminationDate": 12345,
                        "endAgreementDate": 12345,
                        "status": "ACTIVE",
                        "statusDate": 12345,
                        "customFields": {},
                        "accesses": {},
                        "services": {},
                        "products": {},
                        "productInstance": [{}, {}],
                        "terminationReason": "...",
                        "orderNumber": "...",
                        "minimumAmountEl": "...",
                        "minimumAmountElSpark": "...",
                        "minimumLabelEl": "...",
                        "minimumLabelElSpark": "...",
                        "subscribedTillDate": 12345,
                        "renewed": True,
                        "renewalNotifiedDate": 12345,
                        "renewalRule": {},
                        "billingCycle": "...",
                        "seller": "...",
                        "autoEndOfEngagement": True,
                        "ratingGroup": "...",
                        "electronicBilling": True,
                        "email": "...",
                        "mailingType": "...",
                        "emailTemplate": "...",
                        "ccedEmails": "...",
                        "discountPlanForInstantiation": [{}, {}],
                        "discountPlanForTermination": ["...", "..."],
                        "discountPlanInstance": [{}, {}],
                    },
                ],
            },
            "actionStatus": {
                "status": "SUCCESS",
            },
        }
        client_get_mock.return_value = expected_response_data

        response = SubscriptionList.get()

        for key, value in expected_response_data["actionStatus"].items():
            self.assertEquals(getattr(response.action_status, key), value)

        for key, value in expected_response_data["paging"].items():
            self.assertEquals(getattr(response.paging, key), value)

        for subscription in response.subscriptions:
            self.assertIsInstance(subscription, Subscription)

        client_get_mock.assert_called_with(
            "/billing/subscription/list", query=None, limit=10, offset=None
        )

    @patch("pyopencell.resources.subscription.Client.get")
    def test_get_with_offset(self, client_get_mock):
        SubscriptionList.get(limit=10, offset=2)

        client_get_mock.assert_called_with(
            "/billing/subscription/list", query=None, limit=10, offset=2
        )

    @patch("pyopencell.resources.subscription.Client.get")
    def test_query_without_matches(self, client_get_mock):
        # NOTE opencell API should return an empty array in
        # subscriptions.subscription, but life is hard!
        expected_response_data = {
            "actionStatus": {"status": "SUCCESS"},
            "paging": {
                "fullTextFilter": None,
                "filters": {"userAccount.code": "caca"},
                "fields": None,
                "offset": None,
                "limit": 10,
                "sortBy": "code",
                "sortOrder": "ASCENDING",
                "totalNumberOfRecords": 0,
                "loadReferenceDepth": 0,
            },
        }

        client_get_mock.return_value = expected_response_data

        subscription_list = SubscriptionList.get(query="userAccount.code:caca")

        self.assertEquals(len(subscription_list.subscriptions), 0)
