
from django.forms import Form, ModelForm, ValidationError

from basement.fields import FormField


def get_clean_data(django_form):

    validate_form(django_form)

    return django_form.cleaned_data


def validate_form(django_form):
    if not django_form.is_valid():
        raise ArgumentValidationError(django_form)


class ArgumentValidationError(ValidationError):

    def __init__(self, form):
        self._form = form
        super(ArgumentValidationError, self).__init__(form.errors)

    @property
    def form(self):
        return self._form

    def __str__(self):
        return self.form.errors.as_text()


class BasementFormMixin(object):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field, FormField):
                field.init_form(*args, **kwargs)

    def commit(self, instance):
        for field in self.fields.values():
            if isinstance(field, FormField):
                field.commit(instance)


class BasementForm(BasementFormMixin, Form):
    pass


class BasementModelForm(BasementFormMixin, ModelForm):
    pass

