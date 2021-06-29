#----encoding:utf-8------------
from django import forms
from .models import *
from django.core.validators import RegexValidator
from microsip_api.apps.sms.core import SMSMasivo


def UpdateRegistry(registry_name, value):
    registry = Registry.objects.get(nombre=registry_name)
    registry.valor = value
    registry.save()


class PreferenciasManageForm(forms.Form):
    enviar_remisiones = forms.BooleanField(label='Enviar remisiones Pendientes', required=False)
    resumir_mensajes = forms.BooleanField(label='Resumir mensajes', required=False)
    empresa_nombre = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':"off",'class':'col-md-12', }))  
    informacion_extra = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':"off",'class':'col-md-12', }), required=False)  
    telefono_default = forms.CharField(max_length=10, validators=[RegexValidator(regex='^\d{10}$', message='Longitud de 10', code='TGelefono invalido')], required=False)
    apikey = forms.CharField(max_length=41,widget=forms.PasswordInput ,required=False)
    monto_minimo = forms.DecimalField(max_digits=7, decimal_places=2)
    dias_atraso = forms.DecimalField(max_digits=10, decimal_places=3)
    modo_pruebas = forms.BooleanField(label='Modo pruebas', required=False)


    def save(self, *args, **kwargs):
        empresa_nombre = Registry.objects.get( nombre = 'SIC_SMS_NombreEmpresa')
        empresa_nombre.valor = self.cleaned_data['empresa_nombre']
        empresa_nombre.save()

        telefono_default = Registry.objects.get( nombre = 'SIC_SMS_TelDefault')
        telefono_default.valor = self.cleaned_data['telefono_default']
        telefono_default.save()

        enviar_remisiones = 'S' if self.cleaned_data['enviar_remisiones'] else 'N'
        UpdateRegistry('SIC_SMS_EnviarRemisionesPendientes', enviar_remisiones)
        UpdateRegistry('SIC_SMS_DiasPorVencer', self.cleaned_data['dias_atraso'])
        UpdateRegistry('SIC_SMS_InformacionExtra', self.cleaned_data['informacion_extra'])

        resumir_mensajes = 'S' if self.cleaned_data['resumir_mensajes'] else 'N'
        UpdateRegistry('SIC_SMS_ResumirMensajes', resumir_mensajes)
       
        modo_pruebas = 'S' if self.cleaned_data['modo_pruebas'] else 'N'
        UpdateRegistry('SIC_SMS_ModoPruebas', modo_pruebas)

        apikey = Registry.objects.get( nombre = 'SIC_SMS_ApiKey')
        apikey.valor = self.cleaned_data['apikey']
        if apikey.valor:
            apikey.save()

        monto_minimo = Registry.objects.get( nombre = 'SIC_SMS_MontoMinimo')
        monto_minimo.valor = self.cleaned_data['monto_minimo']
        monto_minimo.save()

    def clean_apikey(self,*args,**kwargs):
        apikey= self.cleaned_data['apikey']
        if apikey:
            sms=SMSMasivo(apikey=apikey)
            if sms.credito()['success'] != True:
                raise forms.ValidationError(u'Llave Invalida')

        apikey_registry = Registry.objects.get( nombre = 'SIC_SMS_ApiKey').valor
        if not apikey_registry and not apikey:
            raise forms.ValidationError(u'Campo Obligatorio')

        return apikey


