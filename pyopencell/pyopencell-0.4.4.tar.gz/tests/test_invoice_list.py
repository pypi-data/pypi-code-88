from datetime import datetime
from mock import patch
import unittest2 as unittest

from pyopencell.resources.invoice_list import InvoiceList
from pyopencell.resources.invoice import Invoice
from pyopencell.responses.action_status import ActionStatus

from .settings import REQUIRED_ENVVARS


@patch.dict('os.environ', REQUIRED_ENVVARS)
class InvoiceListTests(unittest.TestCase):

    @patch("pyopencell.resources.subscription.Client.get")
    def test_get_status_not_success(self, client_get_mock):
        expected_response_data = {
            "status": "FAIL",
            "errorCode": "",
            "message": ""
        }

        client_get_mock.return_value = expected_response_data

        response = InvoiceList.get()

        self.assertIsInstance(response, ActionStatus)

    @patch("pyopencell.resources.subscription.Client.get")
    def test_get(self, client_get_mock):
        expected_response_data = {
            "invoices": [
                {
                    "invoiceId": 12345,
                    "amountTax": 12345.0,
                    "categoryInvoiceAgregate": [
                        {
                            "amountTax": 12345.0,
                        }
                    ],
                    "taxAggregate": [
                        {
                            "amountTax": 12345.0,
                        }
                    ],
                }
            ],
            "actionStatus": {
                "status": "SUCCESS",
                "errorCode": "",
                "message": "",
            },
            "paging": {
                "fullTextFilter": "...",
                "filters": {
                    "property1": {},
                    "property2": {}
                },
                "fields": "...",
                "offset": 12345,
                "limit": 12345,
                "sortBy": "...",
                "sortOrder": "ASCENDING",
                "totalNumberOfRecords": 12345,
                "loadReferenceDepth": 12345
            }
        }
        client_get_mock.return_value = expected_response_data

        response = InvoiceList.get()

        for key, value in expected_response_data["actionStatus"].items():
            self.assertEquals(getattr(response.action_status, key), value)

        for key, value in expected_response_data["paging"].items():
            self.assertEquals(getattr(response.paging, key), value)

        for invoice in response.invoices:
            self.assertIsInstance(invoice, Invoice)

        client_get_mock.assert_called_with("/invoice/list", query=None, limit=10, offset=None)

    @patch("pyopencell.resources.subscription.Client.get")
    def test_get_filtering_by_date(self, client_get_mock):
        now = datetime.now()
        InvoiceList.filter_by_date(now)

        client_get_mock.assert_called_with(
            "/invoice/list",
            query="invoiceDate:{}".format(now.strftime("%Y-%m-%d")),
            limit=10,
            offset=None)

    @patch("pyopencell.resources.subscription.Client.get")
    def test_get_with_offset(self, client_get_mock):
        InvoiceList.get(limit=10, offset=2)

        client_get_mock.assert_called_with("/invoice/list", query=None, limit=10, offset=2)
