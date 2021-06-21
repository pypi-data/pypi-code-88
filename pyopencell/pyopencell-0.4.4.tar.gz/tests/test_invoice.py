from mock import patch
import unittest2 as unittest

from pyopencell.resources.invoice import Invoice
from pyopencell.responses.action_status import ActionStatus

from .settings import REQUIRED_ENVVARS


@patch.dict('os.environ', REQUIRED_ENVVARS)
@patch("pyopencell.resources.subscription.Client.post")
class InvoiceTests(unittest.TestCase):

    def test_sendByEmail_response(self, client_get_mock):
        expected_response_data = {
            "status": "SUCCESS",
            "errorCode": "",
            "message": ""
        }

        client_get_mock.return_value = expected_response_data

        response = Invoice.sendByEmail(0)

        self.assertIsInstance(response, ActionStatus)

    def test_sendByEmail_send_correct_data(self, client_post_mock):
        expected_response_data = {
            "status": "SUCCESS",
            "errorCode": "",
            "message": ""
        }
        invoice_id = 8

        client_post_mock.return_value = expected_response_data

        Invoice.sendByEmail(invoice_id)

        client_post_mock.assert_called_with(
            "{}/{}".format(Invoice._url_path, "sendByEmail"),
            {"invoiceId": invoice_id})
