
from django.conf import settings
from django.forms import DateField
from django.forms import Field, ValidationError
from django.utils.translation import ugettext_lazy as _

from basement.widgets import DatePickerInput


class FormField(Field):

    form = None

    def init_form(self, *args, **kwargs):
        self.form = self._build_form(*args, **kwargs)
        self.widget.form = self.form

    def clean(self, *args, **kwargs):
        if not self.form.is_valid():
            raise ValidationError(_('Form is invalid.'))

        return self.form.cleaned_data

    def commit(self, *args, **kwargs):
        return self.form.commit(*args, **kwargs)

    def _build_form(self, *args, **kwargs):
        raise NotImplementedError


class DatePickerField(DateField):

    widget = DatePickerInput

    input_formats = settings.DATE_INPUT_FORMATS
