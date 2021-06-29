#----encoding:utf-8------------
from django import forms
from .models import *
from dal import autocomplete

class ClienteSearchForm(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), widget=autocomplete.ModelSelect2(), required=False)
    nombre = forms.CharField(max_length=50,  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'nombre...'}), required=False)
    clave = forms.CharField(max_length=20,  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'clave...'}),required=False)
    
    def __init__(self, *args, **kwargs):
        super(ClienteSearchForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].widget.attrs['class'] = 'form-control'


class FileForm(forms.Form):
    archivo = forms.FileField(required=False)
    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        self.fields['archivo'].widget.attrs['class'] = 'form-control'

class ClienteManageForm(forms.ModelForm):

    class Meta:
        model = Cliente
        exclude = ('cuenta_xcobrar','estatus','tipo_cliente', 'condicion_de_pago', 'emir_estado_cuenta', 'cobrar_impuestos', 'moneda', 'nombre', 'generar_interereses',)