#----encoding:utf-8------------
from django import forms
from .models import *
from dal import autocomplete
from django.core.validators import RegexValidator
from django_select2 import forms as s2forms
from dal import autocomplete
from django.forms.widgets import CheckboxSelectMultiple

class ClienteWidget(s2forms.ModelSelect2MultipleWidget):
	search_fields = [
		"nombre__icontains",
	]
class SMSForm(forms.Form):
    telefono =forms.CharField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de telefono(10 digitos)...'}) )
    mensaje = forms.CharField(max_length=160,  widget = forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe tu mensaje aqui (160 caracteres)...','cols':35, 'rows':5, 'maxlength':160, }))

class SelectMultipleClients(forms.Form):
	clientes = forms.ModelMultipleChoiceField(queryset=Cliente.objects.all(), widget=s2forms.Select2Widget())
	#clientes = forms.ModelMultipleChoiceField(widget=s2forms.Select2MultipleWidget(),choices=[(obj.name, obj.name) for obj in Cliente.objects.all()])

