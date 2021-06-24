import datetime

from django import forms
from django.forms import widgets
from django_kirui.widgets import CheckboxSwitch


class SampleForm(forms.Form):
    elso = forms.CharField(label='Próba felirat', required=False)
    harmadik = forms.MultipleChoiceField(label='Harmadik', choices=[(1, 'One'), (2, 'Two'), (3, 'Three')], initial=[],
                                         widget=widgets.CheckboxSelectMultiple)
    masodik = forms.ChoiceField(label='Próba választó', choices=[(None, '-----------------'), (1, 'One'), (2, 'Two'), (3, 'Three')], initial=None)
    negyedik = forms.BooleanField(label='Valami', widget=CheckboxSwitch)
    otodik = forms.BooleanField(label='Ötödik', widget=CheckboxSwitch)
    hatodik = forms.IntegerField(label='Hatodik')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['elso'].initial = str(datetime.datetime.now())
