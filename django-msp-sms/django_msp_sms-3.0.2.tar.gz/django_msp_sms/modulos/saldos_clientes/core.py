# #encoding:utf-8
from microsip_api.apps.sms.core import SMSMasivo
from django.conf import settings
modo_pruebas = settings.MODO_SERVIDOR == 'PRUEBAS'
from .models import *
from datetime import datetime

def formar_mensaje(kwargs):
    cargo = kwargs['kwargs']['cargo']
    commun = kwargs['kwargs']['commun']
    login = kwargs['kwargs']['login']
    options = kwargs['kwargs']['options']
    cargo['total'] = cargo['total'].replace('$ ', '')[0:-3]
    detalles_str = ''
    for documento in cargo['documentos']:
        documento['saldo_cargo'] = documento['saldo_cargo'][0:-3]
        detalles_str += '%s- %s, ' % (documento['folio'], documento['saldo_cargo'])
    detalles_str = detalles_str[0:-1]
    mensaje = '%s: Edo de Cta: %sTotal= %s en %s Documentos.' % (commun['empresa_nombre'], detalles_str, cargo['total'], cargo['documentos_numero'])
    # Si solo fue un documento
    if cargo['documentos_numero'] == 1:
        mensaje = '%s: Edo de Cta: Total= %s en %s' % (commun['empresa_nombre'], cargo['total'], cargo['documentos'][0]['folio'])

    if len(mensaje) > 160:
        mensaje = '%s: Edo de Cta: Total= %s en %s Documentos.' % (commun['empresa_nombre'], cargo['total'], cargo['documentos_numero'])

    mensaje += ' Docs en %s' % cargo['cliente_moneda_simbolo']
    if commun['informacion_extra']:
        if (len(mensaje)+len(commun['informacion_extra'])<=160):
            mensaje += ' %s' % commun['informacion_extra']
    
    #mensaje = mensaje[0:160]
    sms_masivo = SMSMasivo(apikey=login['apikey'], pruebas=modo_pruebas)
    data=sms_masivo.send(mensaje=mensaje, telefono=cargo['telefono'])

    # print("///////////////sms_masivo")
    # print(data)
    return data


def formar_mensaje_por_vencer(kwargs):
    dias_por_vencer = int(Registry.objects.get(nombre='SIC_SMS_DiasPorVencer').get_value())
    cargos = kwargs['data']['cargos']
    commun = kwargs['commun']
    login = kwargs['login']
    options = kwargs['options']
    for cargo in cargos:
        detalles = False
        cargo['total'] = cargo['total'].replace('$ ', '')[0:-3]
        detalles_str = 'Hoy faltan %s dias para vencer: ' % dias_por_vencer
        for documento in cargo['documentos']:
            documento['saldo_cargo'] = documento['saldo_cargo'][0:-3]
            vencimiento_date = datetime.strptime(documento['vencimiento'], "%d/%m/%Y").date()
            dias_dif = (vencimiento_date - datetime.now().date()).days
            if dias_dif == dias_por_vencer:
                detalles_str += 'Folio : %s = %s;' % (documento['folio'], documento['saldo_cargo'])
                detalles = True
        detalles_str = detalles_str[0:-1]
        mensaje = '%s: Le informa: %s' % (commun['empresa_nombre'], detalles_str)

        mensaje += ' Docs en %s.' % cargo['cliente_moneda_simbolo']
        if commun['informacion_extra']:
            mensaje += ' %s' % commun['informacion_extra']
        sms_masivo = SMSMasivo(apikey=login['apikey'], pruebas=modo_pruebas)
        if detalles:
            print( sms_masivo.send(mensaje=mensaje, telefono=cargo['telefono']))
        return mensaje