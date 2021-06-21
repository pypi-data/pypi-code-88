"""Receive money module."""


class Merchant:
    """Merchant class."""

    def __init__(self, till):
        """Create merchant."""
        self.till = till

    def to_json(self):
        """Return merchant as json."""
        return {
            "merchant": {
                "till": self.till,
            }
        }


class Partner:
    """Partner class."""

    def __init__(self, id, reference):
        """Create partner."""
        self.id = id
        self.ref = reference

    def to_json(self):
        """Return partner as json."""
        return {
            "partner": {
                "id": self.id,
                "ref": self.ref,
            }
        }


class Payment:
    """Payment class."""

    def __init__(self, amount, currency, reference):
        """Create payment."""
        self.amount = amount
        self.currency = currency
        self.ref = reference

    def to_json(self):
        """Return payment as json."""
        return {
            "payment": {
                "amount": self.amount,
                "currency": self.currency,
                "ref": self.ref,
            }
        }


class Bill:
    """Bill class."""

    def __init__(self, amount, currency, reference):
        """Create bill."""
        self.amount = amount
        self.currency = currency
        self.reference = reference

    def to_json(self):
        """Return bill as json."""
        return {
            "bill": {
                "amount": self.amount,
                "currency": self.currency,
                "reference": self.reference,
                "type": self.type,
            }
        }


class Transaction:
    """Transaction class."""

    def __init__(self, amount, description, reference, type="EazzyPayOnline"):
        """Create transaction."""
        self.amount = amount
        self.description = description
        self.reference = reference
        self.type = type

    def to_json(self):
        """Return transaction as json."""
        return {
            "transaction": {
                "amount": self.amount,
                "description": self.description,
                "reference": self.reference,
                "type": self.type,
            }
        }


class RefundReverseTransaction(Transaction):
    """Refund or reverse Transaction class."""

    def __init__(
        self,
        amount,
        description,
        reference,
        service="EazzyPayOnline",
        channel="EAZ",
        type="refund",
    ):
        """Create refund or reversal transaction."""
        self.amount = amount
        self.description = description
        self.reference = reference
        self.service = service
        self.channel = channel
        self.type = type

    def to_json(self):
        """Return transaction as json."""
        return {
            "transaction": {
                "amount": self.amount,
                "description": self.description,
                "reference": self.reference,
                "service": self.service,
                "channel": self.channel,
                "type": self.type,
            }
        }


class Payer:
    """Payer class."""

    def __init__(
        self,
        name,
        account,
        reference,
        mobileNumber,
    ):
        """Create payer."""
        self.mobileNumber = mobileNumber
        self.name = name
        self.account = account
        self.reference = reference

    def to_json(self):
        """Return payer as json."""
        return {
            "payer": {
                "name": self.name,
                "account": self.account,
                "mobileNumber": self.mobileNumber,
                "reference": self.reference,
            }
        }


class Customer:
    """Customer class."""

    def __init__(self, mobileNumber, countryCode="KE"):
        """Create customer."""
        self.mobileNumber = mobileNumber
        self.countryCode = countryCode

    def to_json(self):
        """Return customer as json."""
        return {
            "customer": {
                "mobileNumber": self.mobileNumber,
                "countryCode": self.countryCode,
            }
        }


class Biller:
    """Biller class."""

    def __init__(self, billerCode, countryCode="KE"):
        """Create biller."""
        self.billerCode = billerCode
        self.countryCode = countryCode

    def to_json(self):
        """Return biller as json."""
        return {
            "biller": {
                "billerCode": self.billerCode,
                "countryCode": self.countryCode,
            }
        }


class EazzypayPush:
    """Easy Pay Push."""

    def __init__(
        self,
        customer: Customer,
        transaction: Transaction,
        merchantCode,
    ):
        """Create EazzyPay Push object."""
        self.customer = customer
        self.transaction = Transaction
        self.merchantCode = merchantCode

    @property
    def body_payload(self):
        """Return body payload as json."""
        d = {}
        d.update(self.customer.to_json())
        d.update(self.transaction.to_json())
        return d

    @property
    def sigkey(self):
        """Return tuple of fields to gen signature."""
        return (
            self.transaction.reference,
            self.transaction.amount,
            self.merchantCode,
            self.customer.countryCode,
        )


class BillPayment:
    """Bill Payments."""

    def __init__(
        self,
        biller: Biller,
        bill: Bill,
        payer: Payer,
        partnerId,
        remarks,
    ):
        """Create bill payment object."""
        self.biller = biller
        self.bill = bill
        self.payer = payer
        self.partnerId = partnerId
        self.remarks = remarks

    @property
    def body_payload(self):
        """Return body payload as json."""
        d = {}
        d.update(self.biller.to_json())
        d.update(self.bill.to_json())
        d.update(self.payer.to_json())
        d.update({"partnerId": self.partnerId, "remarks": self.remarks})
        return d

    @property
    def sigkey(self):
        """Return tuple of fields to gen signature."""
        return (
            self.biller.billerCode,
            self.bill.amount,
            self.payer.reference,
            self.partnerId,
        )


class MerchantPayment:
    """Merchant Payments."""

    def __init__(
        self,
        merchant: Merchant,
        payment: Payment,
        partner: Partner,
    ):
        """Create Merchant Payment object."""
        self.merchant = merchant
        self.payment = payment
        self.partner = partner

    @property
    def body_payload(self):
        """Return body payload as json."""
        d = {}
        d.update(self.merchant.to_json())
        d.update(self.payment.to_json())
        d.update(self.partner.to_json())
        return d

    @property
    def sigkey(self):
        """Return tuple of fields to gen signature."""
        return (
            self.merchant.till,
            self.partner.id,
            self.payment.amount,
            self.payment.currency,
            self.payment.ref,
        )


class RefundReversePayment:
    """Refund Reverse Payment."""

    def __init__(
        self,
        customer: Customer,
        transaction: RefundReverseTransaction,
    ):
        """Create a refund/reverse payment object."""
        self.customer = customer
        self.transaction = transaction

    @property
    def body_payload(self):
        """Return body payload as json."""
        d = {}
        d.update(self.customer.to_json())
        d.update(self.transaction.to_json())
        return d

    @property
    def sigkey(self):
        """Return tuple of fields to gen signature."""
        return (
            self.transaction.amount,
            self.transaction.reference,
        )


class BillValidation:
    """Bill Validation."""

    def __init__(
        self,
        billerCode,
        customerRefNumber,
        amount,
        amountCurrency,
    ):
        """Create Bill Validation object."""
        self.billerCode = billerCode
        self.customerRefNumber = customerRefNumber
        self.amount = amount
        self.amountCurrency = amountCurrency

    @property
    def body_payload(self):
        """Return body payload as json."""
        return {
            "billerCode": self.billerCode,
            "customerRefNumber": self.customerRefNumber,
            "amount": self.amount,
            "amountCurrency": self.amountCurrency,
        }

    @property
    def sigkey(self):
        """Return Tuple to gen signature."""
        return None
