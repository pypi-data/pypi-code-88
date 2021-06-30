from typing import Union, Optional

from pydantic.main import BaseModel


class TokenRequest(BaseModel):
    grant_type: Union[None, str]
    client_id: Union[None, str]
    client_secret: Union[None, str]
    scope: Union[None, str]


class Token(BaseModel):
    access_token: str
    expires_in: int
    token_type: str
    expires_at: int


class UserBase(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str


class UserRequest(UserBase):
    country: str


class User(UserBase):
    full_name: Union[None, str]
    created_at: Optional[Union[None, str]]
    updated_at: Optional[Union[None, str]]
    location: Union[None, str]


class CompanyBase(BaseModel):
    name: str
    legal_name: str
    tax_number: str


class CompanyRequest(CompanyBase):
    user_id: str
    country: str


class Company(CompanyBase):
    id: str
    charge_tax: Union[None, str]
    address_line_1: Union[None, str]
    address_line_2: Union[None, str]
    city: Union[None, str]
    state: Union[None, str]
    zip: Union[None, str]
    phone: Union[None, str]


class WalletAccount(BaseModel):
    id: str
    active: bool
    created_at: Optional[Union[None, str]]
    updated_at: Optional[Union[None, str]]
    balance: int
    currency: str


class NppDetails(BaseModel):
    pay_id: str
    reference: str
    amount: str
    currency: str


class BpayDetails(BaseModel):
    biller_code: str
    reference: str
    amount: str
    currency: str


class VirtualAccountBase(BaseModel):
    id: str
    wallet_account_id: str


class VirtualAccountRequest(VirtualAccountBase):
    pass


class VirtualAccount(VirtualAccountBase):
    routing_number: int
    account_number: int
    currency: str
    active: bool
    created_at: Optional[Union[None, str]]
    updated_at: Optional[Union[None, str]]


class BankAccountBase(BaseModel):
    bank_name: str
    country: str
    account_name: str
    routing_number: str
    account_number: str
    holder_type: str
    account_type: str


class BankDetails(BankAccountBase):
    direct_debit_authority_status: Optional[str]


class BankAccountRequest(BankAccountBase):
    user_id: str


class BankAccount(BaseModel):
    id: str
    active: bool
    verification_status: str
    currency: str
    created_at: Optional[Union[None, str]]
    updated_at: Optional[Union[None, str]]
    bank: Optional[BankDetails]


class SetDisbursementRequest(BaseModel):
    account_id: str


class Disbursement(BaseModel):
    id: str
    amount: int
    currency: str
    batch_id: int
    cuscal_payment_transaction_id: Optional[Union[None, str]]
    created_at: Optional[Union[None, str]]
    updated_at: Optional[Union[None, str]]
    state: str


class Transaction(BaseModel):
    description: str
    type: str
    type_method: str
    state: str
    user_id: str
    user_name: str
    account_id: str
    item_name: str
    dynamic_descriptor: str
    amount: int
    currency: str
    debit_credit: str
    created_at: Optional[Union[None, str]]
    updated_at: Optional[Union[None, str]]


class ItemBase(BaseModel):
    id: str
    name: str
    amount: int


class ItemRequest(ItemBase):
    payment_type: int
    buyer_id: str
    seller_id: str


class Item(ItemBase):
    description: str
    created_at: Optional[Union[None, str]]
    updated_at: Optional[Union[None, str]]
    state: str
    payment_type_id: int
    status: int
    deposit_reference: str
    buyer_name: str
    buyer_country: str
    buyer_email: str
    seller_name: str
    seller_country: str
    seller_email: str
    tds_check_state: str
    currency: str


class MakePaymentRequest(BaseModel):
    account_id: str


class RefundPaymentRequest(BaseModel):
    refund_amount: Optional[int]
    refund_message: Optional[str]
    account_id: Optional[str]


class AuthorizePaymentRequest(BaseModel):
    account_id: str
    cvv: Optional[str]
