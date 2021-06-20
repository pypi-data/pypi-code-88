from django.db.models import CharField
from django.utils.translation import gettext_lazy as _


import logging

from .client import DataKeeper


logger = logging.getLogger(__name__)


class DataKeeperCharField(CharField):
    description = _("Plain Data Keeper String (base CharField)")

    def __init__(self, *args, mask_type="auto", edk_key='default', **kwargs):
        """
        mask_type: [num1] (*|**) [num2]
        num1:前num1位明文显示
        (*|**): *表示固定三个*，(即***)，**表示按遮挡长度显示*
        num2: 后num2位明文显示
        """
        self.mask_type = mask_type
        self.edk_key = edk_key
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        """
        将会在从数据库中载入的生命周期中调用，包括聚集和 values() 调用
        """
        if value is None:
            return value
        return self.to_python(value)

    def to_python(self, value):
        """
        回显python
        """
        if value is None:
            return value

        if isinstance(value, DataKeeper):
            return value

        return DataKeeper(cipher_text=value, mask_type=self.mask_type, edk_key=self.edk_key, field=self)

    def get_prep_value(self, value):
        """
        落库
        """
        if value is None:
            return ""
        if isinstance(value, DataKeeper):
            return value.cipher()

        dk = DataKeeper(plain_text=value, edk_key=self.edk_key)
        return dk.cipher()

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # Only include kwarg if it's not the default
        if self.mask_type != "auto":
            kwargs["mask_type"] = self.mask_type
        if self.edk_key != 'default':
            kwargs["edk_key"] = self.edk_key
        return name, path, args, kwargs

