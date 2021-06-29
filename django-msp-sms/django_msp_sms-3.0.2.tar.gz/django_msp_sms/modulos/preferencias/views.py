#encoding:utf-8
from microsip_api.comun.sic_db import get_conecctionname,first_or_none
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
# user autentication
from .models import *
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from .procedures import procedures as procedures_sic
from django.db import connections, router
from django.core import management
from ...config import configuration_registers, extrafields


@login_required(login_url='/login/')
def PreferenciasManageView(request, template_name='django_msp_sms/preferencias.html'):
    msg = ''
    form_initial = {
        'empresa_nombre': Registry.objects.get(nombre='SIC_SMS_NombreEmpresa').get_value(),
        'informacion_extra': Registry.objects.get(nombre='SIC_SMS_InformacionExtra').get_value(),
        'telefono_default': Registry.objects.get(nombre='SIC_SMS_TelDefault').get_value(),
        'apikey': Registry.objects.get(nombre='SIC_SMS_ApiKey').get_value(),
        'enviar_remisiones': Registry.objects.get(nombre='SIC_SMS_EnviarRemisionesPendientes').get_value() == 'S',
        'resumir_mensajes': Registry.objects.get(nombre='SIC_SMS_ResumirMensajes').get_value() == 'S',
        'monto_minimo': Registry.objects.get(nombre='SIC_SMS_MontoMinimo').get_value(),
        'dias_atraso': Registry.objects.get(nombre='SIC_SMS_DiasPorVencer').get_value(),
        'saldo': Registry.objects.get(nombre='SIC_SMS_Saldo').get_value(),
        'ip_publica': Registry.objects.get(nombre='SIC_SMS_Ip_publica').get_value(),
        'modo_pruebas': Registry.objects.get(nombre='SIC_SMS_ModoPruebas').get_value() == 'S',
    }
    form = PreferenciasManageForm(request.POST or None, initial=form_initial)
    if form.is_valid():
        form.save()
        msg = 'Datos guardados correctamente'
    c = {'form': form, 'msg': msg, }
    return render(request, template_name,c)
    #return render_to_response(template_name, c, context_instance=RequestContext(request))


@login_required(login_url='/login/')
def InitialzeConfigurationDatabase(request):
    """ Agrega campos nuevos en tablas de base de datos. """
    padre = first_or_none(Registry.objects.filter(nombre='PreferenciasEmpresa'))
    if request.user.is_superuser and padre:
        
        using = router.db_for_write(Registry)
        for procedure  in procedures_sic:
            c = connections[using].cursor()
            c.execute(procedures_sic[procedure])
            c.execute('EXECUTE PROCEDURE %s;'%procedure)
            c.execute('DROP PROCEDURE %s;'%procedure)
            c.close()
            
        management.call_command( 'syncdb', database = using, interactive= False)       

        for register in configuration_registers:
            if not Registry.objects.filter(nombre = register).exists():
                Registry.objects.create(
                    nombre = register,
                    tipo = 'V',
                    padre = padre,
                    valor= '',
                )
                
    return HttpResponseRedirect('/sms/preferencias')
