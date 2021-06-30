from datetime import datetime
from faker import Faker

fake = Faker()

def UserFactory(**kwargs):
    data = dict(
        id=fake.word(),
        full_name=fake.name(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        created_at=datetime.now().isoformat(),
        updated_at=datetime.now().isoformat(),
        email=fake.email(),
        mobile="",
        phone=None,
        location="AUS"
    )
    data.update(kwargs)
    return data


def CompanyFactory(**kwargs):
    data = dict(
        id=fake.word(),
        name=fake.word(),
        legal_name=fake.word(),
        tax_number=fake.word(),
        charge_tax=None,
        address_line_1=fake.word(),
        address_line_2=fake.word(),
        city=fake.word(),
        state=fake.word(),
        zip=None,
        country=fake.word(),
        phone=None,
        user_id=fake.word()
    )
    data.update(kwargs)
    return data


def WalletAccountFactory(**kwargs):
    data = dict(
        id=fake.word(),
        active=fake.boolean(),
        created_at=datetime.now().isoformat(),
        updated_at=datetime.now().isoformat(),
        balance=fake.pyint(),
        currency="AUD"
    )
    data.update(kwargs)
    return data


def NppDetailsFactory(**kwargs):
    data = dict(
        pay_id=fake.email(),
        reference=fake.word(),
        amount="$0.00",
        currency="AUD"
    )
    data.update(kwargs)
    return data


def BpayDetailsFactory(**kwargs):
    data = dict(
        biller_code="111111",
        reference=fake.word(),
        amount="$0.00",
        currency="AUD"
    )
    data.update(kwargs)
    return data


def VirtualAccountFactory(**kwargs):
    data = dict(
        id=fake.word(),
        routing_number=fake.pyint(),
        account_number=fake.pyint(),
        wallet_account_id=fake.word(),
        currency="AUD",
        active=fake.boolean(),
        created_at=datetime.now().isoformat(),
        updated_at=datetime.now().isoformat(),
    )
    data.update(kwargs)
    return data


def BankAccountFactory(**kwargs):
    data = dict(
        id=fake.word(),
        active=fake.boolean(),
        created_at=datetime.now().isoformat(),
        updated_at=datetime.now().isoformat(),
        verification_status="not_verified",
        currency="AUD",
        bank=dict(
            bank_name=fake.word(),
            country="AUS",
            account_name=fake.first_name() + " " + fake.last_name(),
            routing_number="XXXXX1",
            account_number="XXX123",
            holder_type="personal",
            account_type="checking",
            direct_debit_authority_status="approved"
        )
    )
    data.update(kwargs)
    return data


def DisbursementFactory(**kwargs):
    data = dict(
        id=fake.word(),
        amount=fake.pyint(),
        currency="AUD",
        batch_id=fake.pyint(),
        cuscal_payment_transaction_id=None,
        created_at=datetime.now().isoformat(),
        updated_at=datetime.now().isoformat(),
        state="successful"
    )
    data.update(kwargs)
    return data


def TransactionFactory(**kwargs):
    data = dict(
        description=fake.word(),
        type="payment",
        type_method="credit_card",
        state="successful",
        user_id=fake.word(),
        user_name=fake.first_name() + " " + fake.last_name(),
        account_id=fake.word(),
        item_name=fake.word(),
        dynamic_descriptor=fake.word(),
        amount=fake.pyint(),
        currency="AUD",
        debit_credit="debit",
        created_at=datetime.now().isoformat(),
        updated_at=datetime.now().isoformat(),
    )
    data.update(kwargs)
    return data


def ItemFactory(**kwargs):
    data = dict(
        id=fake.word(),
        name=fake.word(),
        description=fake.word(),
        created_at=datetime.now().isoformat(),
        updated_at=datetime.now().isoformat(),
        state="completed",
        payment_type_id=2,
        status=22500,
        amount=fake.pyint(),
        deposit_reference=fake.word(),
        buyer_name=fake.last_name(),
        buyer_country="AUS",
        buyer_email=fake.email(),
        seller_name=fake.last_name(),
        seller_country="AUS",
        seller_email=fake.email(),
        tds_check_state="NA",
        currency="AUD"
    )
    data.update(kwargs)
    return data