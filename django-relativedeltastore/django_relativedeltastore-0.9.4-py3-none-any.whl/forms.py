from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from dateutil.relativedelta import relativedelta

from . import create_relativedelta_string, parse_relativedelta_string


class RelativeDeltaStoreField(forms.Field):
    def __init__(
            self, *, required=True, widget=None, label=None, initial=None,
            help_text=None, error_messages=None, show_hidden_initial=False,
            validators=(), localize=False, disabled=False, label_suffix=None,
            serializer=create_relativedelta_string,
            deserializer=parse_relativedelta_string,
            encoder=None, decoder=None,
    ):
        self.serializer = serializer
        self.deserializer = deserializer

        super().__init__(
            required=required, widget=widget, label=label, initial=initial,
            help_text=help_text, error_messages=error_messages, show_hidden_initial=show_hidden_initial,
            validators=validators, localize=localize, disabled=disabled, label_suffix=label_suffix,
            # omit unused encoder/decoder args
        )

    def prepare_value(self, value):
        if isinstance(value, (relativedelta, dict)):
            value = self.serializer(value)
        return value

    def to_python(self, value):
        if value in self.empty_values:
            return None
        else:
            return str(value).strip()

    def clean(self, value):
        value = super().clean(value)
        if value is None:
            return value
        relativedelta_kwargs, remainder = self.deserializer(value)
        if remainder:
            raise ValidationError(_('Invalid value at: %(remainder)s'), params={'remainder': remainder})
        return relativedelta(**relativedelta_kwargs)
