#encoding:utf-8
import json
import re

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import RequestContext

# user autentication
from . import core
from . import forms
from .models import *
from microsip_api.apps.sms.core import SMSMasivo
from urllib.request import urlopen
#modo_pruebas = settings.MODO_SERVIDOR == 'PRUEBAS'
from dal import autocomplete
from datetime import datetime
import os

class ClienteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Cliente.objects.none()

        qs = Cliente.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

@login_required(login_url='/login/')
def index(request, template_name='django_msp_sms/index.html'):
    error = ''
    apikey = None
    creditos = 0
    if Registry.objects.get(nombre='SIC_SMS_InformacionExtra').get_value():
        creditos=Registry.objects.get(nombre='SIC_SMS_InformacionExtra').get_value()
    
    initial_configuration = core.InitialConfiguration()
    modo_pruebas=Registry.objects.get(nombre='SIC_SMS_ModoPruebas').get_value() == 'S'
    if not initial_configuration.is_valid:
        error = 'Inicializar Configuracion'
    else:
        apikey = str(Registry.objects.get(nombre='SIC_SMS_ApiKey').get_value())
    
    if Registry.objects.get(nombre='SIC_SMS_Saldo').get_value():
        creditos=Registry.objects.get(nombre='SIC_SMS_Saldo').get_value()
    if apikey != 'None':
        pass
    #     sms_masivo = SMSMasivo(apikey=apikey, pruebas=modo_pruebas)
    #     dic_cred = sms_masivo.credito()
    #     print(urlopen('http://icanhazip.com').read())
    #     #https://www.manusoft.es/raspberry-pi/comprobar-automaticamente-la-direccion-ip-publica/
    #     print(dic_cred['success'])
    #     if dic_cred['success'] == True:
    #         creditos = float(dic_cred['credit'])
    else:
        error = 'Llave no Definida'
    c = {'creditos': creditos, 'error': error, 'modo_pruebas': modo_pruebas}
    return render(request, template_name,c)
    #return render_to_response(template_name, c, context_instance=RequestContext(request))


@login_required(login_url='/login/')
def personalizadosView(request, template_name='django_msp_sms/personalizados.html'):
    apikey = str(Registry.objects.get(nombre='SIC_SMS_ApiKey').get_value())
    modo_pruebas=Registry.objects.get(nombre='SIC_SMS_ModoPruebas').get_value() == 'S'
    directorio=settings.MEDIA_ROOT+'\\numeros_invalidos\\'
    now = datetime.now()
    date_time = now.strftime("%m-%d-%Y_%H%M")
    nom_archivo='numeros_invalidos'+date_time+'.txt'

    try:
        os.mkdir(directorio)
    except OSError:
        print("La creación del directorio %s falló" % directorio)
    else:
        print("Se ha creado el directorio: %s " % directorio)
    file = open(directorio+nom_archivo, "w")
    
    c = {}
    multi = False
    num_enviados = 0
    num_no_enviados = 0
    form = forms.SMSForm(request.POST or None)
    mensaje_respuesta = ''
    estatus = ''
    if form.is_valid():
        mensaje = form.cleaned_data['mensaje']
        mensaje = mensaje.encode('ascii', 'replace')
        telefono = form.cleaned_data['telefono']
        sms_masivo = SMSMasivo(apikey=apikey, pruebas=modo_pruebas)
        creditos= float(Registry.objects.get(nombre='SIC_SMS_Saldo').get_value())
        if len(telefono.split(',')) > creditos:
            mensaje_respuesta="No tiene sufcientes creditos par enviar los mensajes (Mensajes por enviar "+str(len(telefono.split(',')))+", "+str(creditos)+" credito(s) disponbles) "
        elif (len(telefono.split(',')) > 1):
            for tel in telefono.split(','):
                print(telefono)
                multi = True
                j = sms_masivo.multisend(mensaje=mensaje, telefono=tel)
                if j['code']=='sms_19':
                    mensaje_respuesta="El numero de telefono es fijo o no existe "
                    file.write(tel+'\n')
                    num_no_enviados=num_no_enviados+1
                elif j['code']=='sms_11':
                    creditos= float(Registry.objects.get(nombre='SIC_SMS_Saldo').get_value())
                    creditos= creditos-1
                    saldo = Registry.objects.get(nombre = 'SIC_SMS_Saldo')
                    saldo.valor=str(creditos)
                    saldo.save()
                    mensaje_respuesta = j['message']
                    num_enviados=num_enviados+1
                #mensaje_respuesta = j['message']
                estatus = None
        else:
            j = sms_masivo.send(mensaje=mensaje, telefono=telefono)
            #mensaje_respuesta = j['message']
            estatus = j['code']
            if j['code']=='sms_19':
                mensaje_respuesta="El numero de telefono es fijo o no existe "
                num_no_enviados=num_no_enviados+1
                file.write(telefono+'\n')
            elif j['code']=='sms_11':
                creditos= float(Registry.objects.get(nombre='SIC_SMS_Saldo').get_value())
                creditos= creditos-1
                saldo = Registry.objects.get(nombre = 'SIC_SMS_Saldo')
                saldo.valor=str(creditos)
                saldo.save()
                mensaje_respuesta = j['message']
                num_enviados=num_enviados+1

    

    file.close()
    c = {'mensaje': mensaje_respuesta, 'form': form, 'estatus': estatus, 'multi': multi,'num_no_enviados':num_no_enviados, 'num_enviados':num_enviados,'archivo':'numeros_invalidos\\'+nom_archivo,'nom_archivo':nom_archivo, }
    return render(request, template_name,c)
    #return render_to_response(template_name, c, context_instance=RequestContext(request))



@login_required(login_url='/login/')
def enviar_smsView(request):
    apikey = str(Registry.objects.get(nombre='SIC_SMS_ApiKey').get_value())
    modo_pruebas=Registry.objects.get(nombre='SIC_SMS_ModoPruebas').get_value() == 'S'
    mensaje = request.GET['mensaje']
    mensaje = mensaje.encode('ascii', 'replace')
    telefono = request.GET['telefono']
    numero_mensaje = int(request.GET['numero_mensaje'])
    numero_mensaje += 1
    sms = SMSMasivo(apikey=apikey, pruebas=modo_pruebas)
    resultado = sms.send(mensaje=mensaje, telefono=telefono)['message']
    data = {
        'telefono': telefono,
        'numero_mensaje': numero_mensaje,
        'resultado': resultado,
    }

    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')


@login_required(login_url='/login/')
def enviar_mensaje(request):
    apikey = str(Registry.objects.get(nombre='SIC_SMS_ApiKey').get_value())
    modo_pruebas=Registry.objects.get(nombre='SIC_SMS_ModoPruebas').get_value() == 'S'
    telefono = request.GET['telefono']
    mensaje = request.GET['mensaje']
    mensaje = mensaje.encode('ascii', 'replace')

    sms = SMSMasivo(apikey=apikey, pruebas=modo_pruebas)
    resultado = sms.send(mensaje=mensaje, telefono=telefono)['message']

    data = json.dumps({
        'resultado': resultado,
    })
    return HttpResponse(data, content_type='application/json')


@login_required(login_url='/login/')
def get_creditos(request):
    apikey = str(Registry.objects.get(nombre='SIC_SMS_ApiKey').get_value())
    modo_pruebas=Registry.objects.get(nombre='SIC_SMS_ModoPruebas').get_value() == 'S'
    sms_masivo = SMSMasivo(apikey=apikey, pruebas=modo_pruebas)
    creditos = float(sms_masivo.credito()['credit'])
    #se envian datos
    if modo_pruebas=='S':
        creditos = len(mensajes)
    data = json.dumps({
        'creditos': creditos,
    })

    return HttpResponse(data, content_type='application/json')


@login_required(login_url='/login/')
def get_mensajes_personalizados(request):
    clientes_ids = str(request.GET['clientes_ids']).replace('[', '').replace(']', '').replace('"', '').split(',')
    mensaje = request.GET['mensaje']
    mensaje = mensaje.encode('ascii', 'replace')

    clientes = ClienteDireccion.objects.filter(cliente__id__in=clientes_ids).order_by('telefono1').values_list('cliente', 'cliente__nombre', 'telefono1',)

    mensajes_clientes = {}
    clientes_con_telefono_invalido = []
    for cliente in clientes:
        cliente_id = cliente[0]
        cliente_nombre = cliente[1].lstrip().rstrip()
        telefono = cliente[2]

        if telefono:
            telefono = unicode(telefono.encode('utf-8'), errors='ignore')
            telefono = re.sub("[^0-9]", "", str(telefono))

            #validacion de telefonos invalidos  y creacion de mensajes
            if len(telefono) != 10 and cliente_nombre not in clientes_con_telefono_invalido:
                clientes_con_telefono_invalido.append(cliente_nombre)
            elif not cliente_id in mensajes_clientes:
                if cliente_nombre in clientes_con_telefono_invalido:
                    clientes_con_telefono_invalido.remove(cliente_nombre)

                mensajes_clientes[cliente_id] = (telefono, mensaje, cliente_nombre)
        else:
            if not cliente_nombre in clientes_con_telefono_invalido:
                clientes_con_telefono_invalido.append(cliente_nombre)

    data = json.dumps({
        'mensajes': mensajes_clientes.values(),
        'clientes_con_telefono_invalido': clientes_con_telefono_invalido,
    })

    return HttpResponse(data, content_type='application/json')
