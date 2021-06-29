#----encoding:utf-8------------
from django import forms
from django.forms import ModelForm
# from .models import *
from django_microsip_base.libs.models_base.models import Articulo,ArticuloPrecio,ArticuloClave, Moneda, PrecioEmpresa,Registry,ClienteDireccion, Cliente, CondicionPago, Vendedor, VentasDocumento, VentasDocumentoDetalle, Almacen,ClienteClave,VentasDocumentoLiga,SaldosSms
from dal import autocomplete

class SearchForm(forms.Form):
	cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), widget=autocomplete.ModelSelect2(), required=False)
	TIPO = (
		(u'E', u'ENTRADA'), 
		(u'S', u'SALIDA'),
		)
	tipo = forms.ChoiceField(choices=TIPO,widget=forms.Select(attrs={'class': 'form-control'}), required=False)    
	def __init__(self, *args, **kwargs):
		super(SearchForm, self).__init__(*args, **kwargs)
		self.fields['cliente'].widget.attrs['class'] = 'form-control'
		self.fields['tipo'].widget.attrs['class'] = 'form-control'

class SaldoForm(ModelForm):
	TIPO = (
		(u'E', u'ENTRADA'), 
		(u'S', u'SALIDA'),
		)
	tipo = forms.ChoiceField(choices=TIPO,widget=forms.Select(attrs={'class': 'form-control'}), required=False)    
	class Meta:
		model = SaldosSms
		fields = ['cliente', 'cantidad','archivo']
	
	def __init__(self, *args, **kwargs):
		super(SaldoForm, self).__init__(*args, **kwargs)
		self.fields['tipo'].widget.attrs['class'] = 'form-control'
		self.fields['cliente'].widget.attrs['class'] = 'form-control'
		self.fields['cantidad'].widget.attrs['class'] = 'form-control'
		self.fields['archivo'].widget.attrs['class'] = 'form-control'

class PreferenciasManageForm(forms.Form):
	email=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),)
	password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}),)
	servidor_correo = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),)
	puerto=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control'}),)

	
	def save(self, *args, **kwargs):
		email = Registry.objects.get( nombre = 'SIC_Administrador_Email')
		email.valor = self.cleaned_data['email']
		email.save()

		password = Registry.objects.get( nombre = 'SIC_Administrador_Password')
		password.valor = self.cleaned_data['password']
		password.save()

		servidor_correo = Registry.objects.get( nombre = 'SIC_Administrador_Servidro_Correo')
		servidor_correo.valor = self.cleaned_data['servidor_correo']
		servidor_correo.save()

		puerto = Registry.objects.get( nombre = 'SIC_Administrador_Puerto')
		puerto.valor = self.cleaned_data['puerto']
		puerto.save()