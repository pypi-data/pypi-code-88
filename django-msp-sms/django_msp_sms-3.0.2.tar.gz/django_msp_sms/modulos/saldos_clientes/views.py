#encoding:utf-8
from . import forms
from ...tasks import enviar_correo
from .core import formar_mensaje_por_vencer
from .models import *
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import RequestContext
from microsip_api.apps.cuentasxcobrar.core import CargosClientes
from microsip_api.apps.sms.core import SMSMasivo
from microsip_api.comun.sic_db import first_or_none
import json
from datetime import datetime
import os
#modo_pruebas = settings.MODO_SERVIDOR == 'PRUEBAS'


@login_required(login_url='/login/')
def PorSeleccionView(request, template_name='django_msp_sms/saldos_clientes/por_seleccion.html'):
    form = forms.SelectMultipleClients(request.POST or None)
    modo_pruebas=Registry.objects.get(nombre='SIC_SMS_ModoPruebas').get_value() == 'S'
    print(modo_pruebas)
    c = {'form': form}
    
    return render(request, template_name,c)
    #return render_to_response(template_name, c, context_instance=RequestContext(request))


@login_required(login_url='/login/')
def get_mensajes_saldos(request):
    ids = json.loads(request.GET['data'])
    enviar_remisiones = Registry.objects.get(nombre='SIC_SMS_EnviarRemisionesPendientes').get_value() == 'S'
    monto_minimo_mn = Registry.objects.get(nombre='SIC_SMS_MontoMinimo').get_value() or 0
    cargos = CargosClientes('sms', tomar_remisiones=enviar_remisiones, clientes_ids=ids, monto_minimo_mn=monto_minimo_mn)
    # print("+++++++++++++++++++++++++++++++++++++++++++")
    # print(cargos)
    clientes_telefono_invalido = cargos.clientes_informacion_invalida
    clientes_sin_mensaje = cargos.clientes_sin_mensaje
    #clientes_sin_mensaje = map(str, clientes_sin_mensaje)
    # Validacion de saldo
    # se checa disponiblidad de credito
    error = None
    apikey = str(Registry.objects.get(nombre='SIC_SMS_ApiKey').get_value())
    modo_pruebas=Registry.objects.get(nombre='SIC_SMS_ModoPruebas').get_value() == 'S'
    #print()
    sms_masivo = SMSMasivo(apikey=apikey, pruebas=modo_pruebas)
    creditos =  float(Registry.objects.get(nombre='SIC_SMS_Saldo').get_value())
    if modo_pruebas:
        creditos = len(cargos)
    if creditos < len(cargos):
        error = 'Creditos Insuficientes.<br>Creditos Disponibles: %s<br>Mensajes por enviar: %s<br>Creditos Necesarios: %s' % (creditos, len(cargos), len(cargos)-creditos)
        print(error)
    # print("**********")
    # print(ids)
    # print(cargos)
    # print(clientes_telefono_invalido)
    # print(clientes_sin_mensaje)
    # print(error)
    data = json.dumps({
        'cargos': cargos,
        'clientes_telefono_invalido': clientes_telefono_invalido,
        'clientes_sin_mensaje': clientes_sin_mensaje,
        'error': error,
    })

    return HttpResponse(data, content_type='application/json')


@login_required(login_url='/login/')
def enviar_cargos_seleccion(request):
    cargo = json.loads(request.GET['data'])
    creditos=0
    # print("////////////////////////////////////////")
    # print(cargo)
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
    

    login = {
        'apikey': Registry.objects.get(nombre='SIC_SMS_ApiKey').valor,
    }

    commun = {
        'empresa_nombre': Registry.objects.get(nombre='SIC_SMS_NombreEmpresa').get_value(),
        'informacion_extra': Registry.objects.get(nombre='SIC_SMS_InformacionExtra').get_value(),
    }
    resumir_mensajes = Registry.objects.get(nombre='SIC_SMS_ResumirMensajes').get_value() == 'S'
    kwargs = {
        'commun': commun,
        'login': login,
        'cargo': cargo,
        'options': {
            'resumir': resumir_mensajes,
        }
    }
    datos=enviar_correo(kwargs=kwargs)
    print("***************************RESULTADO***************************")
    print(datos)
    if datos['code'] == 'sms_11':
       creditos= float(Registry.objects.get(nombre='SIC_SMS_Saldo').get_value())
       creditos= creditos-1
       saldo = Registry.objects.get(nombre = 'SIC_SMS_Saldo')
       saldo.valor=str(creditos)
       saldo.save()
    else:
        print(str(datos['references'][0]['number']))
        file = open(directorio+nom_archivo, "w")
        file.write(str(datos['references'][0]['number']).replace('52','')+'\n')
        file.close()
    #print(creditos)

    resultado = 'Mensaje enviado'

    data = json.dumps({
        'resultado': datos,
        'media_url':settings.MEDIA_URL,
        'nom_archivo':nom_archivo,
        'carpeta':'/numeros_invalidos/',
    })
    return HttpResponse(data, content_type='application/json')


@login_required(login_url='/login/')
def todos_view(request, template_name='django_msp_sms/saldos_clientes/todos.html'):
    return render(request, template_name,{})
    #return render_to_response(template_name, {}, context_instance=RequestContext(request))


@login_required(login_url='/login/')
def enviar_cargos_por_vencer(request,  template_name='django_msp_sms/saldos_clientes/por_vencer.html'):
    ids = []
    enviar_remisiones = Registry.objects.get(nombre='SIC_SMS_EnviarRemisionesPendientes').get_value() == 'S'
    monto_minimo_mn = Registry.objects.get(nombre='SIC_SMS_MontoMinimo').get_value() or 0
    cargos = CargosClientes('sms', tomar_remisiones=enviar_remisiones, clientes_ids=ids, monto_minimo_mn=monto_minimo_mn)
    clientes_telefono_invalido = cargos.clientes_informacion_invalida
    clientes_sin_mensaje = cargos.clientes_sin_mensaje
    clientes_sin_mensaje = map(str, clientes_sin_mensaje)
    error = ''
    apikey = str(Registry.objects.get(nombre='SIC_SMS_ApiKey').get_value())
    modo_pruebas=Registry.objects.get(nombre='SIC_SMS_ModoPruebas').get_value() == 'S'
    sms_masivo = SMSMasivo(apikey=apikey, pruebas=modo_pruebas)
    creditos = float(sms_masivo.credito()['credit'])
    if modo_pruebas:
        creditos = len(cargos)
    if creditos < len(cargos):
        error = 'Creditos Insuficientes.<br>Creditos Disponibles: %s<br>Mensajes por enviar: %s<br>Creditos Necesarios: %s' % (creditos, len(cargos), len(cargos)-creditos)

    data = {
        'cargos': cargos,
        'clientes_telefono_invalido': clientes_telefono_invalido,
        'clientes_sin_mensaje': clientes_sin_mensaje,
        'error': error,
    }

    login = {
        'apikey': Registry.objects.get(nombre='SIC_SMS_ApiKey').valor,
    }

    commun = {
        'empresa_nombre': Registry.objects.get(nombre='SIC_SMS_NombreEmpresa').get_value(),
        'informacion_extra': Registry.objects.get(nombre='SIC_SMS_InformacionExtra').get_value(),
    }

    resumir_mensajes = Registry.objects.get(nombre='SIC_SMS_ResumirMensajes').get_value() == 'S'
    kwargs = {
        'commun': commun,
        'login': login,
        'data': data,
        'options': {
            'resumir': resumir_mensajes,
        }
    }

    formar_mensaje_por_vencer(kwargs=kwargs)
    resultado = 'Mensaje enviado'

    data = {
        'resultado': resultado,
    }
    return render(request, template_name,c)
    #return render_to_response(template_name, data, context_instance=RequestContext(request))


@login_required(login_url='/login/')
def saldos_automaticos_preferencias(request, template_name='django_msp_sms/saldos_clientes/saldos_automaticos_preferencias.html'):
    """
    Guarda o actualiza una la tarea para envio de mensajes Automaticos

    **** Si next_execution(Siguiente ejecucion) no se a indicado nunca
         la fecha de siguiente ejecucion sera la fecha de inicio. ****
    """

    context = {
        'errors': []
    }

    if 'djmicrosip_tareas' in settings.EXTRA_MODULES:
        from djmicrosip_tareas.models import ProgrammedTask
        task = first_or_none(ProgrammedTask.objects.filter(description='SMS Saldos Automaticos')) or ProgrammedTask()

        form = forms.ProgrammedTaskForm(request.POST or None, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            # Si no se acreado le agregamos los paramentros comunes de la tarea
            if not task.id:
                task.description = 'SMS Saldos Automaticos'
                task.command_type = 'http'
                task.command = 'http://127.0.0.1:8001/sms/saldos/todos_automatico/'
            task.save()
            form = forms.ProgrammedTaskForm(None, instance=task)
            context['msg'] = 'Información actualizada correctamente.'
        context['form'] = form
    else:
        context['errors'].append('Por favor instalarla para poder configurar esta opción')

    return render(request, template_name,c)
    #return render_to_response(template_name, context, context_instance=RequestContext(request))


@login_required(login_url='/login/')
def envia_saldos_automaticos(request):
    enviar_remisiones = Registry.objects.get(nombre='SIC_SMS_EnviarRemisionesPendientes').get_value() == 'S'
    monto_minimo_mn = Registry.objects.get(nombre='SIC_SMS_MontoMinimo').get_value() or 0
    cargos = CargosClientes('sms', tomar_remisiones=enviar_remisiones, clientes_ids=[], monto_minimo_mn=monto_minimo_mn)

    login = {
        'apikey': Registry.objects.get(nombre='SIC_SMS_ApiKey').valor,
    }

    commun = {
        'empresa_nombre': Registry.objects.get(nombre='SIC_SMS_NombreEmpresa').get_value(),
    }

    kwargs = {
        'commun': commun,
        'login': login,
    }

    for cargo in cargos:
        kwargs['cargo'] = cargo
        enviar_correo(kwargs=kwargs)

    return HttpResponseRedirect('/sms/')


@login_required(login_url='/login/')
def saldos_por_vencer_automaticos_preferencias(request, template_name='django_msp_sms/saldos_clientes/saldos_automaticos_por_vencer_preferencias.html'):
    context = {
        'errors': []
    }
    if 'djmicrosip_tareas' in settings.EXTRA_MODULES:
        from djmicrosip_tareas.models import ProgrammedTask
        task = first_or_none(ProgrammedTask.objects.filter(description='SMS Saldos por vencer Automaticos')) or ProgrammedTask()

        form = forms.ProgrammedTaskForm(request.POST or None, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            if not task.id:
                task.description = 'SMS Saldos por vencer Automaticos'
                task.command_type = 'http'
                task.command = 'http://127.0.0.1:8001/sms/saldos/enviar_por_vencer/'
            task.save()
            form = forms.ProgrammedTaskForm(None, instance=task)
        context['form'] = form
    else:
        context['errors'].append('Por favor instalarla para poder configurar esta opción')

    return render(request, template_name,c)
    #return render_to_response(template_name, context, context_instance=RequestContext(request))