from django.dispatch import Signal

from django_encryption.context import Context
from django_encryption.client import crypto_client

import logging

logger = logging.getLogger(__name__)
plain_sig = Signal()


class DataKeeper(object):
    def __init__(self, plain_text=None, cipher_text=None, mask_type=None, field=None, edk_key='default') -> None:
        # 是否存在脱敏
        if plain_text is not None and plain_text.count("*") > 0:
            raise ValueError("明文不能含有*字符:%s" % plain_text)

        self._plain_text = plain_text
        self._cipher_text = cipher_text
        self._model = self._field_name = self._verbose_name = None
        if field is not None:
            self._model = field.model._meta.db_table
            self._field_name = field.column
            self._verbose_name = field.verbose_name
        self._mask_type = mask_type if mask_type is not None else ""
        self._edk_key = edk_key
        self._id = None

    def plain(self, message=None):
        """
        获取原始明文，获取增加额外记录
        """
        try:
            plain_sig.send(sender=self.__class__, model=self._model, filed_name=self._field_name,
                           verbose_name=self._verbose_name, mask_text=self.mask(), cipher_text=self.cipher(), id=self._id,
                           context=Context.get(), message=message)
        except Exception as e:
            logging.warn("send plain sig error, %s" % e, )

        if self._plain_text is not None:
            return self._plain_text

        return '' if self._cipher_text is None else crypto_client(self._edk_key).decrypt(self._cipher_text)

    def cipher(self):
        """
        获取密文
        """
        if self._cipher_text is not None:
            return self._cipher_text
        if self._plain_text is not None:
            self._cipher_text = '' if self._plain_text == '' else crypto_client(self._edk_key).encrypt(self._plain_text)
            return self._cipher_text
        return None

    def mask(self, mask_type=None):
        """
        获取掩码信息
        """
        plain_info = self._plain_text if self._plain_text is not None else crypto_client(self._edk_key).decrypt(self._cipher_text)

        if plain_info == '':
            return ''

        mask_type = mask_type if mask_type is not None else self._mask_type
        # 自动判断掩码
        if mask_type == 'auto':
            """
            至少保证四位是加密的，优先后面原始显示，最多前3后4
            """
            if len(plain_info) <= 4:
                return "*"
            last_total = len(plain_info)-4
            before = 3 if last_total//2 > 3 else last_total//2
            after = 4 if last_total - before > 4 else last_total - before
            return plain_info[:before] + "****" + plain_info[len(plain_info) - after:]

        if len(mask_type) <= 1:
            return "*"

        mask_type = mask_type.split("*")
        before = int(mask_type[0]) if mask_type[0].isdigit() else 0
        after = int(mask_type[-1]) if mask_type[-1].isdigit() else 0

        if len(plain_info) <= (before + after):
            return "***"

        mask_text = "***" if mask_type.count("") == 0 else "*" * (len(plain_info) - before - after)
        return plain_info[:before] + mask_text + plain_info[len(plain_info) - after:]

    def __str__(self) -> str:
        return self.mask()

    def __repr__(self) -> str:
        return self.mask()


def get_plain(obj, message=None):
    if isinstance(obj, DataKeeper):
        return obj.plain(message=message)
    return obj


def get_mask(obj, mask_type=None):
    if isinstance(obj, DataKeeper):
        return obj.mask(mask_type=mask_type)


def default(obj):
    if isinstance(obj, DataKeeper):
        return obj.mask()
    return obj


def django_json_encoder():
    from django.core.serializers.json import DjangoJSONEncoder
    old_default = DjangoJSONEncoder.default

    def new_default(self, o):
        if isinstance(o, DataKeeper):
            return o.mask()
        return old_default(self, o)
    DjangoJSONEncoder.default = new_default

    from rest_framework.utils.encoders import JSONEncoder
    old_drf_default = JSONEncoder.default

    def new_drf_default(self, obj):
        if isinstance(obj, DataKeeper):
            return obj.mask()
        return old_drf_default(self, obj)
    JSONEncoder.default = new_drf_default
