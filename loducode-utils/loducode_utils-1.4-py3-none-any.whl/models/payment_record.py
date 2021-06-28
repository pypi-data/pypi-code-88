from django.db.models import CharField

from loducode_utils.models.audit import Audit


class PaymentRecord(Audit):
    x_cust_id_cliente = CharField(max_length=250, blank=True, null=True)
    x_description = CharField(max_length=250, blank=True, null=True)
    x_amount_ok = CharField(max_length=250, blank=True, null=True)
    x_id_invoice = CharField(max_length=250, blank=True, null=True)
    x_amount_base = CharField(max_length=250, blank=True, null=True)
    x_tax = CharField(max_length=250, blank=True, null=True)
    x_currency_code = CharField(max_length=250, blank=True, null=True)
    x_franchise = CharField(max_length=250, blank=True, null=True)
    x_transaction_date = CharField(max_length=250, blank=True,
                                          null=True)
    x_approval_code = CharField(max_length=250, blank=True, null=True)
    x_transaction_id = CharField(max_length=250, blank=True, null=True)
    x_ref_payco = CharField(max_length=250, blank=True, null=True)
    x_cod_response = CharField(max_length=250, blank=True, null=True)
    x_cod_transaction_state = CharField(max_length=250, blank=True,
                                               null=True)
    x_transaction_state = CharField(max_length=250, blank=True,
                                           null=True)
    x_signature = CharField(max_length=250, blank=True, null=True)
    x_response = CharField(max_length=250, blank=True, null=True)
    x_response_reason_text = CharField(max_length=250, blank=True,
                                              null=True)
    x_extra1 = CharField(max_length=250, blank=True, null=True)
    x_extra2 = CharField(max_length=250, blank=True, null=True)
    x_extra3 = CharField(max_length=250, blank=True, null=True)
    x_amount = CharField(max_length=250, blank=True, null=True)
    x_amount_country = CharField(max_length=250, blank=True, null=True)
    x_bank_name = CharField(max_length=250, blank=True, null=True)
    x_cardnumber = CharField(max_length=250, blank=True, null=True)
    x_quotas = CharField(max_length=250, blank=True, null=True)
    x_fecha_transaccion = CharField(max_length=250, blank=True,
                                           null=True)
    x_errorcode = CharField(max_length=250, blank=True, null=True)
    x_customer_doctype = CharField(max_length=250, blank=True,
                                          null=True)
    x_customer_lastname = CharField(max_length=250, blank=True,
                                           null=True)
    x_customer_name = CharField(max_length=250, blank=True, null=True)
    x_customer_email = CharField(max_length=250, blank=True, null=True)
    x_customer_phone = CharField(max_length=250, blank=True, null=True)
    x_customer_country = CharField(max_length=250, blank=True,
                                          null=True)
    x_customer_city = CharField(max_length=250, blank=True, null=True)
    x_customer_address = CharField(max_length=250, blank=True,
                                          null=True)
    x_customer_ip = CharField(max_length=250, blank=True, null=True)
    x_test_request = CharField(max_length=250, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s'%self.id