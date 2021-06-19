"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
from datetime import datetime
if TYPE_CHECKING:
    from ...tl.types import TypeBankCardOpenUrl, TypeDataJSON, TypeInvoice, TypePaymentRequestedInfo, TypePaymentSavedCredentials, TypeShippingOption, TypeUpdates, TypeUser, TypeWebDocument



class BankCardData(TLObject):
    CONSTRUCTOR_ID = 0x3e24e573
    SUBCLASS_OF_ID = 0x8c6dd68b

    def __init__(self, title: str, open_urls: List['TypeBankCardOpenUrl']):
        """
        Constructor for payments.BankCardData: Instance of BankCardData.
        """
        self.title = title
        self.open_urls = open_urls

    def to_dict(self):
        return {
            '_': 'BankCardData',
            'title': self.title,
            'open_urls': [] if self.open_urls is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.open_urls]
        }

    def _bytes(self):
        return b''.join((
            b's\xe5$>',
            self.serialize_bytes(self.title),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.open_urls)),b''.join(x._bytes() for x in self.open_urls),
        ))

    @classmethod
    def from_reader(cls, reader):
        _title = reader.tgread_string()
        reader.read_int()
        _open_urls = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _open_urls.append(_x)

        return cls(title=_title, open_urls=_open_urls)


class PaymentForm(TLObject):
    CONSTRUCTOR_ID = 0x8d0b2415
    SUBCLASS_OF_ID = 0xa0483f19

    def __init__(self, form_id: int, bot_id: int, invoice: 'TypeInvoice', provider_id: int, url: str, users: List['TypeUser'], can_save_credentials: Optional[bool]=None, password_missing: Optional[bool]=None, native_provider: Optional[str]=None, native_params: Optional['TypeDataJSON']=None, saved_info: Optional['TypePaymentRequestedInfo']=None, saved_credentials: Optional['TypePaymentSavedCredentials']=None):
        """
        Constructor for payments.PaymentForm: Instance of PaymentForm.
        """
        self.form_id = form_id
        self.bot_id = bot_id
        self.invoice = invoice
        self.provider_id = provider_id
        self.url = url
        self.users = users
        self.can_save_credentials = can_save_credentials
        self.password_missing = password_missing
        self.native_provider = native_provider
        self.native_params = native_params
        self.saved_info = saved_info
        self.saved_credentials = saved_credentials

    def to_dict(self):
        return {
            '_': 'PaymentForm',
            'form_id': self.form_id,
            'bot_id': self.bot_id,
            'invoice': self.invoice.to_dict() if isinstance(self.invoice, TLObject) else self.invoice,
            'provider_id': self.provider_id,
            'url': self.url,
            'users': [] if self.users is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.users],
            'can_save_credentials': self.can_save_credentials,
            'password_missing': self.password_missing,
            'native_provider': self.native_provider,
            'native_params': self.native_params.to_dict() if isinstance(self.native_params, TLObject) else self.native_params,
            'saved_info': self.saved_info.to_dict() if isinstance(self.saved_info, TLObject) else self.saved_info,
            'saved_credentials': self.saved_credentials.to_dict() if isinstance(self.saved_credentials, TLObject) else self.saved_credentials
        }

    def _bytes(self):
        assert ((self.native_provider or self.native_provider is not None) and (self.native_params or self.native_params is not None)) or ((self.native_provider is None or self.native_provider is False) and (self.native_params is None or self.native_params is False)), 'native_provider, native_params parameters must all be False-y (like None) or all me True-y'
        return b''.join((
            b'\x15$\x0b\x8d',
            struct.pack('<I', (0 if self.can_save_credentials is None or self.can_save_credentials is False else 4) | (0 if self.password_missing is None or self.password_missing is False else 8) | (0 if self.native_provider is None or self.native_provider is False else 16) | (0 if self.native_params is None or self.native_params is False else 16) | (0 if self.saved_info is None or self.saved_info is False else 1) | (0 if self.saved_credentials is None or self.saved_credentials is False else 2)),
            struct.pack('<q', self.form_id),
            struct.pack('<i', self.bot_id),
            self.invoice._bytes(),
            struct.pack('<i', self.provider_id),
            self.serialize_bytes(self.url),
            b'' if self.native_provider is None or self.native_provider is False else (self.serialize_bytes(self.native_provider)),
            b'' if self.native_params is None or self.native_params is False else (self.native_params._bytes()),
            b'' if self.saved_info is None or self.saved_info is False else (self.saved_info._bytes()),
            b'' if self.saved_credentials is None or self.saved_credentials is False else (self.saved_credentials._bytes()),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _can_save_credentials = bool(flags & 4)
        _password_missing = bool(flags & 8)
        _form_id = reader.read_long()
        _bot_id = reader.read_int()
        _invoice = reader.tgread_object()
        _provider_id = reader.read_int()
        _url = reader.tgread_string()
        if flags & 16:
            _native_provider = reader.tgread_string()
        else:
            _native_provider = None
        if flags & 16:
            _native_params = reader.tgread_object()
        else:
            _native_params = None
        if flags & 1:
            _saved_info = reader.tgread_object()
        else:
            _saved_info = None
        if flags & 2:
            _saved_credentials = reader.tgread_object()
        else:
            _saved_credentials = None
        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        return cls(form_id=_form_id, bot_id=_bot_id, invoice=_invoice, provider_id=_provider_id, url=_url, users=_users, can_save_credentials=_can_save_credentials, password_missing=_password_missing, native_provider=_native_provider, native_params=_native_params, saved_info=_saved_info, saved_credentials=_saved_credentials)


class PaymentReceipt(TLObject):
    CONSTRUCTOR_ID = 0x10b555d0
    SUBCLASS_OF_ID = 0x590093c9

    def __init__(self, date: Optional[datetime], bot_id: int, provider_id: int, title: str, description: str, invoice: 'TypeInvoice', currency: str, total_amount: int, credentials_title: str, users: List['TypeUser'], photo: Optional['TypeWebDocument']=None, info: Optional['TypePaymentRequestedInfo']=None, shipping: Optional['TypeShippingOption']=None, tip_amount: Optional[int]=None):
        """
        Constructor for payments.PaymentReceipt: Instance of PaymentReceipt.
        """
        self.date = date
        self.bot_id = bot_id
        self.provider_id = provider_id
        self.title = title
        self.description = description
        self.invoice = invoice
        self.currency = currency
        self.total_amount = total_amount
        self.credentials_title = credentials_title
        self.users = users
        self.photo = photo
        self.info = info
        self.shipping = shipping
        self.tip_amount = tip_amount

    def to_dict(self):
        return {
            '_': 'PaymentReceipt',
            'date': self.date,
            'bot_id': self.bot_id,
            'provider_id': self.provider_id,
            'title': self.title,
            'description': self.description,
            'invoice': self.invoice.to_dict() if isinstance(self.invoice, TLObject) else self.invoice,
            'currency': self.currency,
            'total_amount': self.total_amount,
            'credentials_title': self.credentials_title,
            'users': [] if self.users is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.users],
            'photo': self.photo.to_dict() if isinstance(self.photo, TLObject) else self.photo,
            'info': self.info.to_dict() if isinstance(self.info, TLObject) else self.info,
            'shipping': self.shipping.to_dict() if isinstance(self.shipping, TLObject) else self.shipping,
            'tip_amount': self.tip_amount
        }

    def _bytes(self):
        return b''.join((
            b'\xd0U\xb5\x10',
            struct.pack('<I', (0 if self.photo is None or self.photo is False else 4) | (0 if self.info is None or self.info is False else 1) | (0 if self.shipping is None or self.shipping is False else 2) | (0 if self.tip_amount is None or self.tip_amount is False else 8)),
            self.serialize_datetime(self.date),
            struct.pack('<i', self.bot_id),
            struct.pack('<i', self.provider_id),
            self.serialize_bytes(self.title),
            self.serialize_bytes(self.description),
            b'' if self.photo is None or self.photo is False else (self.photo._bytes()),
            self.invoice._bytes(),
            b'' if self.info is None or self.info is False else (self.info._bytes()),
            b'' if self.shipping is None or self.shipping is False else (self.shipping._bytes()),
            b'' if self.tip_amount is None or self.tip_amount is False else (struct.pack('<q', self.tip_amount)),
            self.serialize_bytes(self.currency),
            struct.pack('<q', self.total_amount),
            self.serialize_bytes(self.credentials_title),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _date = reader.tgread_date()
        _bot_id = reader.read_int()
        _provider_id = reader.read_int()
        _title = reader.tgread_string()
        _description = reader.tgread_string()
        if flags & 4:
            _photo = reader.tgread_object()
        else:
            _photo = None
        _invoice = reader.tgread_object()
        if flags & 1:
            _info = reader.tgread_object()
        else:
            _info = None
        if flags & 2:
            _shipping = reader.tgread_object()
        else:
            _shipping = None
        if flags & 8:
            _tip_amount = reader.read_long()
        else:
            _tip_amount = None
        _currency = reader.tgread_string()
        _total_amount = reader.read_long()
        _credentials_title = reader.tgread_string()
        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        return cls(date=_date, bot_id=_bot_id, provider_id=_provider_id, title=_title, description=_description, invoice=_invoice, currency=_currency, total_amount=_total_amount, credentials_title=_credentials_title, users=_users, photo=_photo, info=_info, shipping=_shipping, tip_amount=_tip_amount)


class PaymentResult(TLObject):
    CONSTRUCTOR_ID = 0x4e5f810d
    SUBCLASS_OF_ID = 0x8ae16a9d

    def __init__(self, updates: 'TypeUpdates'):
        """
        Constructor for payments.PaymentResult: Instance of either PaymentResult, PaymentVerificationNeeded.
        """
        self.updates = updates

    def to_dict(self):
        return {
            '_': 'PaymentResult',
            'updates': self.updates.to_dict() if isinstance(self.updates, TLObject) else self.updates
        }

    def _bytes(self):
        return b''.join((
            b'\r\x81_N',
            self.updates._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _updates = reader.tgread_object()
        return cls(updates=_updates)


class PaymentVerificationNeeded(TLObject):
    CONSTRUCTOR_ID = 0xd8411139
    SUBCLASS_OF_ID = 0x8ae16a9d

    def __init__(self, url: str):
        """
        Constructor for payments.PaymentResult: Instance of either PaymentResult, PaymentVerificationNeeded.
        """
        self.url = url

    def to_dict(self):
        return {
            '_': 'PaymentVerificationNeeded',
            'url': self.url
        }

    def _bytes(self):
        return b''.join((
            b'9\x11A\xd8',
            self.serialize_bytes(self.url),
        ))

    @classmethod
    def from_reader(cls, reader):
        _url = reader.tgread_string()
        return cls(url=_url)


class SavedInfo(TLObject):
    CONSTRUCTOR_ID = 0xfb8fe43c
    SUBCLASS_OF_ID = 0xad3cf146

    def __init__(self, has_saved_credentials: Optional[bool]=None, saved_info: Optional['TypePaymentRequestedInfo']=None):
        """
        Constructor for payments.SavedInfo: Instance of SavedInfo.
        """
        self.has_saved_credentials = has_saved_credentials
        self.saved_info = saved_info

    def to_dict(self):
        return {
            '_': 'SavedInfo',
            'has_saved_credentials': self.has_saved_credentials,
            'saved_info': self.saved_info.to_dict() if isinstance(self.saved_info, TLObject) else self.saved_info
        }

    def _bytes(self):
        return b''.join((
            b'<\xe4\x8f\xfb',
            struct.pack('<I', (0 if self.has_saved_credentials is None or self.has_saved_credentials is False else 2) | (0 if self.saved_info is None or self.saved_info is False else 1)),
            b'' if self.saved_info is None or self.saved_info is False else (self.saved_info._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _has_saved_credentials = bool(flags & 2)
        if flags & 1:
            _saved_info = reader.tgread_object()
        else:
            _saved_info = None
        return cls(has_saved_credentials=_has_saved_credentials, saved_info=_saved_info)


class ValidatedRequestedInfo(TLObject):
    CONSTRUCTOR_ID = 0xd1451883
    SUBCLASS_OF_ID = 0x8f8044b7

    # noinspection PyShadowingBuiltins
    def __init__(self, id: Optional[str]=None, shipping_options: Optional[List['TypeShippingOption']]=None):
        """
        Constructor for payments.ValidatedRequestedInfo: Instance of ValidatedRequestedInfo.
        """
        self.id = id
        self.shipping_options = shipping_options

    def to_dict(self):
        return {
            '_': 'ValidatedRequestedInfo',
            'id': self.id,
            'shipping_options': [] if self.shipping_options is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.shipping_options]
        }

    def _bytes(self):
        return b''.join((
            b'\x83\x18E\xd1',
            struct.pack('<I', (0 if self.id is None or self.id is False else 1) | (0 if self.shipping_options is None or self.shipping_options is False else 2)),
            b'' if self.id is None or self.id is False else (self.serialize_bytes(self.id)),
            b'' if self.shipping_options is None or self.shipping_options is False else b''.join((b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.shipping_options)),b''.join(x._bytes() for x in self.shipping_options))),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        if flags & 1:
            _id = reader.tgread_string()
        else:
            _id = None
        if flags & 2:
            reader.read_int()
            _shipping_options = []
            for _ in range(reader.read_int()):
                _x = reader.tgread_object()
                _shipping_options.append(_x)

        else:
            _shipping_options = None
        return cls(id=_id, shipping_options=_shipping_options)

