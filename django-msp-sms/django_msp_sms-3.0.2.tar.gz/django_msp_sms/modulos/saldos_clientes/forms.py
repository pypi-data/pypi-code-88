#----encoding:utf-8------------
#from dal import autocomplete

from django.conf import settings
from django import forms

from .models import *
from django_select2 import forms as s2forms


class SelectMultipleClients(forms.Form):
    clientes = forms.ModelMultipleChoiceField(queryset=Cliente.objects.all())
    mensaje = forms.CharField(max_length=160,  widget=forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Escribe tu mensaje aqui (160 Caracteres)...', 'cols': 35, 'rows': 5, 'maxlength': 160,
    }))


# Solo si esta instalada la aplicacion de tareas
if 'djmicrosip_tareas' in settings.EXTRA_MODULES:
    from djmicrosip_tareas.models import ProgrammedTask

    class ProgrammedTaskForm(forms.ModelForm):
        period_start_datetime = forms.CharField(label='Inicio', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha inicio periodo...'}))
        period_end_datetime = forms.CharField(label='Fin', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '...'}), required=False)
        period_quantity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'unidades...'}))
        next_execution = forms.CharField(widget=forms.HiddenInput(), required=False)

        class Meta:
            model = ProgrammedTask
            exclude = ('description', 'command_type', 'command', 'status', 'last_execution',)
            widgets = {
                'period_unit': forms.Select(attrs={'class': 'form-control'}),
            }
