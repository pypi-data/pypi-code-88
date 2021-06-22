import requests
import logging
import json
import sys

from sap.connector import Connector, ConnectorException
from sap.settings import api_settings


logger = logging.getLogger(__name__)


class CardType():
    CREDIT = 1
    DEBIT = 2


class TBKType():
    TBK_CUOTA = 1
    TBK_DEBITO = 2
    TBK_TOTAL = 3


class SapHandler:
    """
        Handler to connect with Sap.
    """
    def __init__(self, base_url=api_settings.SAP['BASE_URL'],
                 username=api_settings.SAP['USERNAME'],
                 password=api_settings.SAP['PASSWORD'],
                 company_db=api_settings.SAP['COMPANY_DB'],
                 verify=False
                 ):
        self.base_url = base_url
        self.verify = verify
        self.username = username
        self.password = password
        self.company_db = company_db
        self.doc_entry = None
        self.connector = Connector(self._login(), verify_ssl=self.verify)

    def _login(self):
        """
            This method generate a headers for all Sap connection.
        """
        data = {
            'CompanyDB': self.company_db,
            'Password': self.password,
            'UserName': self.username
        }
        response = requests.request(
            'POST', f'{self.base_url}Login',
            data=json.dumps(data), verify=self.verify
        )

        if response.status_code not in [200, 302]:
            logger.error('Invalid credentials')
            raise UserWarning('Invalid username or password')

        headers = {
            'Cookie': f"B1SESSION={response.json()['SessionId']}; ROUTEID=.node0"
        }

        return headers

    def default_payload_invoice_reserve(self, instance):
        """
            This method try return a structure data for method send_invoice_reserve.
        """
        try:
            documents = [
                {
                    'ItemCode': detail.product.sku,
                    'Quantity': str(detail.quantity),
                    'PriceAfterVAT': str(detail.final_price),
                    'WarehouseCode': api_settings.SAP['WAREHOUSE_CODE'],
                    'TaxCode': api_settings.SAP['TAX_CODE'],
                    'CostingCode': api_settings.SAP['COSTING_CODE'],
                    'CostingCode2': api_settings.SAP['COSTING_CODE2'],
                    'CostingCode3': api_settings.SAP['COSTING_CODE3'],
                } for detail in instance.order_details.all()
            ]

            payload = {
                'CardCode': api_settings.SAP['CARD_CODE'],
                'CardName': instance.customer.full_name,
                'DocDate': instance.order_date.strftime('%Y-%m-%d'),
                'DocDueDate': instance.order_date.strftime('%Y-%m-%d'),
                'TaxDate':instance.order_date.strftime('%Y-%m-%d'),
                'Series': api_settings.SAP['SERIE'],
                'Indicator': api_settings.SAP['INDICATOR'],
                'FederalTaxID': instance.customer.rut if instance.customer.rut != '' else '1-9',
                'ReserveInvoice': api_settings.SAP['RESERVE_INVOICE'],
                'U_Ref1': str(instance.id),
                'U_TipoPedWMS': api_settings.SAP['U_TIPO_PED_WMS'],
                'U_MAIL_DTE': instance.customer.email,
                'DocumentLines': documents,
                'AddressExtension': {
                    'ShipToStreet': f'{instance.billing_address.street} {instance.billing_address.number}',
                    'ShipToCity': instance.billing_address.commune.name,
                    'ShipToCounty': instance.billing_address.commune.region.name,
                    'BillToStreet': f'{instance.billing_address.street} {instance.billing_address.number}',
                    'BillToCity': instance.billing_address.commune.name,
                    'BillToCounty': instance.billing_address.commune.region.name,
                }
            }
            logger.debug(payload)
            return payload
        except Exception as error:
            logger.error(str(error))
            return False

    def send_invoice_reserve(self, data):
        """
            This method sends a invoice reserve to Sap, receives a dictionary
            with the structure of the default_payload_invoice_reserve method.
        """
        try:
            invoice_data = self.connector.post(
                f'{self.base_url}Invoices',
                data=data, object_name='invoice reserve'
            )
            self.doc_entry = invoice_data['DocEntry']
            return invoice_data
        except ConnectorException as error:
            logger.error(str(error.message))
            raise ConnectorException(
                error.message, error.description, error.code, 'INVOICE_RESERVE'
            )
        except Exception as error:
            logger.error(str(error))
            raise ConnectorException(sys.exc_info()[0], str(error), 500, 'INVOICE_RESERVE')

    def default_payload_incoming_payment(self, instance):
        """
            This method try return a structure data for method send_incoming_payment.
        """
        try:
            order_payment_data = json.loads(instance.payment_data)
            if not isinstance(order_payment_data, dict):
                order_payment_data = json.loads(order_payment_data)
            logger.debug('payment_data: %s' % (order_payment_data))

            experation_date = '2030-12-01'
            if order_payment_data['cardDetail']['cardExpirationDate'] is not None and order_payment_data['cardDetail'][
                    'cardExpirationDate'] != 'null':
                experation_date = order_payment_data['cardDetail']['cardExpirationDate']
            payment_type_code = order_payment_data['detailOutput']['paymentTypeCode']
            is_credit_card = payment_type_code in ('VC', 'VN', 'SI', 'S2', 'NC')

            installments = order_payment_data['detailOutput']['sharesNumber']

            payment_method_code = TBKType.TBK_DEBITO
            number_of_payments = 1
            split_payments = 'tNO'

            if is_credit_card:
                payment_method_code = TBKType.TBK_CUOTA
                number_of_payments = installments
                split_payments = 'tYES'

                if installments >= 7:
                    payment_method_code = TBKType.TBK_TOTAL
                    number_of_payments = 1
                    split_payments = 'tNO'

            data = {
                'CardCode': api_settings.SAP['CARD_CODE'],
                'DocDate': instance.order_date.strftime('%Y-%m-%d'),
                'TaxDate': instance.order_date.strftime('%Y-%m-%d'),
                'U_Ref1': str(instance.external_id),
                'PaymentInvoices': [
                    {
                        'LineNum': 0,
                        'DocEntry': self.doc_entry,
                        'SumApplied': str(order_payment_data['detailOutput']['amount']),
                        'InvoiceType': 'it_Invoice',
                    }
                ],
                'PaymentCreditCards': [
                    {
                        'LineNum': 0,
                        'CreditCard': CardType.CREDIT if is_credit_card else CardType.DEBIT,
                        'CreditCardNumber': str(order_payment_data['cardDetail']['cardNumber']),
                        'CardValidUntil': experation_date,
                        'VoucherNum': str(order_payment_data['detailOutput']['authorizationCode']),
                        'PaymentMethodCode': payment_method_code,
                        'NumOfPayments': number_of_payments,
                        'CreditSum': str(order_payment_data['detailOutput']['amount']),
                        'ConfirmationNum': str(order_payment_data['detailOutput']['authorizationCode']),
                        'CreditType': 'cr_Regular',
                        'SplitPayments': split_payments,
                    }
                ]
            }
            logger.debug(data)
            return data
        except KeyError as error:
            logger.error(str(error))
            raise ConnectorException(
                f'Key Error: {str(error)}',
                f'payment_data: {order_payment_data}',
                500, 'INCOMMING_PAYMENTS'
            )
        except Exception as error:
            logger.error(str(error))
            raise ConnectorException(sys.exc_info()[0], str(error), 500, 'INVOICE_RESERVE')

    def send_incoming_payment(self, data):
        """
            This method sends a incomming payment to Sap, receives a dictionary
            with the structure of the default_payload_incoming_payment method.
        """
        try:
            payment_data = self.connector.post(
                f'{self.base_url}IncomingPayments',
                data=data, object_name='incomming payments'
            )
            return payment_data
        except ConnectorException as error:
            logger.error(str(error.message))
            raise ConnectorException(error.message, error.description, error.code, 'INCOMMING_PAYMENTS') from error
        except Exception as error:
            logger.error(str(error))
            raise ConnectorException(sys.exc_info()[0], str(error), 500, 'INVOICE_RESERVE') from error
