#----encoding:utf-8------------
from django import forms
from .models import *
from django.core.validators import RegexValidator
from dal import autocomplete

class SMSForm(forms.Form):
    telefono =forms.CharField(required=False,widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de telefono(10 digitos)...'}) )
    mensaje = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe tu mensaje aqui (160 Caracteres)...','cols':35, 'rows':5, 'maxlength':160, }))

class SelectMultipleClients(forms.Form):
	clientes = forms.ModelMultipleChoiceField(queryset=Cliente.objects.all())
	mensaje = forms.CharField(max_length=160,  widget = forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe tu mensaje aqui (160 Caracteres)...','cols':35, 'rows':5, 'maxlength':160, }))
	

class ZonaForm(forms.Form):
	zona = forms.ModelChoiceField(queryset=Zona.objects.all(), widget= forms.Select(attrs={'class':'form-control'}))
	mensaje = forms.CharField(max_length=160,  widget = forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe tu mensaje aqui (160 Caracteres)...','cols':35, 'rows':5, 'maxlength':160, }))

