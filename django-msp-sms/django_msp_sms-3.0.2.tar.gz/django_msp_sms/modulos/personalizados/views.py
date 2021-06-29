#encoding:utf-8
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
# user autentication
from .models import *
from .forms import *
from .core import *
from microsip_api.apps.sms.core import SMSMasivo
from django.conf import settings
from datetime import datetime
import os

#modo_pruebas = settings.MODO_SERVIDOR == 'PRUEBAS'


def get_num_enviados(respuestas):
    num_enviados = 0
    if type(respuestas) == list:
        num_enviados = 0
        for m in respuestas:
            if m['estatus'] == 'ok':
                num_enviados+=1        
    return num_enviados

@login_required(login_url='/login/')
def PorSeleccionView(request, template_name='django_msp_sms/personalizados/por_seleccion.html'):

    apikey=str(Registry.objects.get( nombre = 'SIC_SMS_ApiKey').get_value())
    modo_pruebas=Registry.objects.get(nombre='SIC_SMS_ModoPruebas').get_value()

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

    clientes_con_telefono_invalido=[]
    mensaje_respuesta = ''
    estatus = ''
    multi=False
    num_enviados = 0
    num_no_enviados = 0
    form = SelectMultipleClients(
        request.POST or None)
    if form.is_valid():
        mensaje = form.cleaned_data['mensaje']
        clientes = form.cleaned_data['clientes']
        print("clientes")
        print(clientes)
        telfonos_clientes= TelefonosClientes(clientes=clientes)
        telefonos = telfonos_clientes.telefonos
        print(telefonos)
        clientes_con_telefono_invalido = telfonos_clientes.clientes_con_telefono_invalido
        
        if None in clientes_con_telefono_invalido:
            clientes_con_telefono_invalido.remove(None)

        sms_masivo=SMSMasivo(apikey=apikey,pruebas=modo_pruebas)
        creditos= float(Registry.objects.get(nombre='SIC_SMS_Saldo').get_value())
        if len(telefonos) > creditos:
            mensaje_respuesta="No tiene sufcientes creditos par enviar los mensajes (Mensajes por enviar "+str(len(telefonos))+", "+str(creditos)+" credito(s) disponbles) "
        elif (len(telefonos)>1):            
            #telefono=",".join(telefonos)
            multi=True

            for telefono in telefonos:
                print(telefono)
                j = sms_masivo.send(mensaje=mensaje,telefono=telefono)
                if j['code']=='sms_19':
                    num_no_enviados=num_no_enviados+1
                    mensaje_respuesta="Numero de telefono es fijo o no existe"
                    file.write(telefono+'\n')
                    print("no")
                elif j['code']=='sms_11':
                    num_enviados=num_enviados+1
                    print("si")
                    creditos= float(Registry.objects.get(nombre='SIC_SMS_Saldo').get_value())
                    creditos= creditos-1
                    saldo = Registry.objects.get(nombre = 'SIC_SMS_Saldo')
                    saldo.valor=str(creditos)
                    saldo.save()
                    mensaje_respuesta = j['message']
                    #mensaje_respuesta = j['message']
                    estatus = j['code']
                    #mensaje_respuesta = j['message']
        elif len(telefonos)!= 0:
            telefono=telefonos[0]
            j = sms_masivo.send(mensaje=mensaje,telefono=telefono)
            if j['code']=='sms_19':
                num_no_enviados=num_no_enviados+1
                mensaje_respuesta="Numero de telefono es fijo o no existe"
                file.write(telefono+'\n')
            elif j['code']=='sms_11':
                num_enviados=num_enviados+1
                creditos= float(Registry.objects.get(nombre='SIC_SMS_Saldo').get_value())
                creditos= creditos-1
                saldo = Registry.objects.get(nombre = 'SIC_SMS_Saldo')
                saldo.valor=str(creditos)
                saldo.save()
                mensaje_respuesta = j['message']
                #mensaje_respuesta = j['message']
                estatus = j['code']
        else:
            mensaje_respuesta='Ningun Telefono es Valido'

    file.close()
        #num_enviados=get_num_enviados(mensaje_respuesta)
        
    c={'mensaje':mensaje_respuesta, 'form':form,'estatus':estatus,'multi':multi,'clientes_con_telefono_invalido':clientes_con_telefono_invalido, 'num_enviados':num_enviados, 'num_no_enviados':num_no_enviados,'archivo':'numeros_invalidos\\'+nom_archivo,'nom_archivo':nom_archivo,}

    return render(request, template_name,c)
    #return render_to_response( template_name, c , context_instance = RequestContext( request ) )

@login_required(login_url='/login/')
def TodosView( request, template_name = 'django_msp_sms/personalizados/todos.html' ):
    apikey=str(Registry.objects.get( nombre = 'SIC_SMS_ApiKey').get_value())
    num_enviados=0
    num_no_enviados = 0
    clientes_con_telefono_invalido=[]
    c={}
    multi=False
    form = SMSForm(request.POST or None)
    mensaje_respuesta = ''
    estatus = ''
    
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
    
    if form.is_valid():
        mensaje = form.cleaned_data['mensaje']
        telfonos_clientes=TelefonosClientes()
        telefonos = telfonos_clientes.telefonos
        clientes_con_telefono_invalido = telfonos_clientes.clientes_con_telefono_invalido
        if None in clientes_con_telefono_invalido:
            clientes_con_telefono_invalido.remove(None)
        sms_masivo=SMSMasivo(apikey=apikey,pruebas=None)
        #creditos_antes =int(sms_masivo.credito()['credito'])

        creditos= float(Registry.objects.get(nombre='SIC_SMS_Saldo').get_value())
        if len(telefonos) > creditos:
            mensaje_respuesta="No tiene sufcientes creditos par enviar los mensajes (Mensajes por enviar "+str(len(telefonos))+", "+str(creditos)+" credito(s) disponbles) "
        elif (len(telefonos)>1):            
            #telefono=",".join(telefonos)
            multi=True

            for telefono in telefonos:
                print(telefono)
                j = sms_masivo.send(mensaje=mensaje,telefono=telefono)
                if j['code']=='sms_19':
                    num_no_enviados=num_no_enviados+1
                    mensaje_respuesta="Numero de telefono es fijo o no existe"
                    file.write(telefono+'\n')
                    print("no")
                elif j['code']=='sms_11':
                    num_enviados=num_enviados+1
                    print("si")
                    creditos= float(Registry.objects.get(nombre='SIC_SMS_Saldo').get_value())
                    creditos= creditos-1
                    saldo = Registry.objects.get(nombre = 'SIC_SMS_Saldo')
                    saldo.valor=str(creditos)
                    saldo.save()
                    mensaje_respuesta = j['message']
                    #mensaje_respuesta = j['message']
                    estatus = j['code']
                    #mensaje_respuesta = j['message']
        elif len(telefonos)!= 0:
            telefono=telefonos[0]
            j = sms_masivo.send(mensaje=mensaje,telefono=telefono)
            if j['code']=='sms_19':
                num_no_enviados=num_no_enviados+1
                mensaje_respuesta="Numero de telefono es fijo o no existe"
                file.write(telefono+'\n')
            elif j['code']=='sms_11':
                num_enviados=num_enviados+1
                creditos= float(Registry.objects.get(nombre='SIC_SMS_Saldo').get_value())
                creditos= creditos-1
                saldo = Registry.objects.get(nombre = 'SIC_SMS_Saldo')
                saldo.valor=str(creditos)
                saldo.save()
                mensaje_respuesta = j['message']
                #mensaje_respuesta = j['message']
                estatus = j['code']
        else:
            mensaje_respuesta='Ningun Telefono es Valido'
        # num_enviados=get_num_enviados(mensaje_respuesta) 
    file.close()
    c={'mensaje':mensaje_respuesta,'form':form,'estatus':estatus,'multi':multi,'clientes_con_telefono_invalido':clientes_con_telefono_invalido,'num_enviados':num_enviados,'num_no_enviados':num_no_enviados,'archivo':'numeros_invalidos\\'+nom_archivo,'nom_archivo':nom_archivo, }

    return render(request, template_name,c)
    #return render_to_response( template_name, c, context_instance = RequestContext( request ) )


@login_required(login_url='/login/')
def ZonaView(request, template_name='django_msp_sms/personalizados/zona.html'):
    apikey = str(Registry.objects.get(nombre='SIC_SMS_ApiKey').get_value())
    modo_pruebas=Registry.objects.get(nombre='SIC_SMS_ModoPruebas').get_value()
    print(modo_pruebas)
    sms_masivo = None
    num_enviados = 0
    num_no_enviados = 0
    creditos_antes = 0
    creditos_despues = 0
    clientes_con_telefono_invalido = []
    c = {}
    multi = False
    form = ZonaForm(request.POST or None)
    mensaje_respuesta = ''
    estatus = ''
    
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

    if form.is_valid():

        mensaje = form.cleaned_data['mensaje']
        zona = form.cleaned_data['zona']

        telfonos_clientes = TelefonosClientes(zona=zona)
        telefonos = telfonos_clientes.telefonos
        clientes_con_telefono_invalido = telfonos_clientes.clientes_con_telefono_invalido
        print(telfonos_clientes.telefonos)
        if None in clientes_con_telefono_invalido:
            clientes_con_telefono_invalido.remove(None)

        sms_masivo = SMSMasivo(apikey=apikey, pruebas=modo_pruebas)
        print("telefonos")
        print(telefonos)
        
        creditos= float(Registry.objects.get(nombre='SIC_SMS_Saldo').get_value())
        if len(telefonos) > creditos:
            mensaje_respuesta="No tiene sufcientes creditos par enviar los mensajes (Mensajes por enviar "+str(len(telefonos))+", "+str(creditos)+" credito(s) disponbles) "
        elif (len(telefonos)>1):            
            #telefono=",".join(telefonos)
            multi=True

            for telefono in telefonos:
                print(telefono)
                j = sms_masivo.send(mensaje=mensaje,telefono=telefono)
                if j['code']=='sms_19':
                    num_no_enviados=num_no_enviados+1
                    mensaje_respuesta="Numero de telefono es fijo o no existe"
                    file.write(telefono+'\n')
                    print("no")
                elif j['code']=='sms_11':
                    num_enviados=num_enviados+1
                    print("si")
                    creditos= float(Registry.objects.get(nombre='SIC_SMS_Saldo').get_value())
                    creditos= creditos-1
                    saldo = Registry.objects.get(nombre = 'SIC_SMS_Saldo')
                    saldo.valor=str(creditos)
                    saldo.save()
                    mensaje_respuesta = j['message']
                    #mensaje_respuesta = j['message']
                    estatus = j['code']
                    #mensaje_respuesta = j['message']
        elif len(telefonos)!= 0:
            telefono=telefonos[0]
            j = sms_masivo.send(mensaje=mensaje,telefono=telefono)
            if j['code']=='sms_19':
                num_no_enviados=num_no_enviados+1
                mensaje_respuesta="Numero de telefono es fijo o no existe"
                file.write(telefono+'\n')
            elif j['code']=='sms_11':
                num_enviados=num_enviados+1
                creditos= float(Registry.objects.get(nombre='SIC_SMS_Saldo').get_value())
                creditos= creditos-1
                saldo = Registry.objects.get(nombre = 'SIC_SMS_Saldo')
                saldo.valor=str(creditos)
                saldo.save()
                mensaje_respuesta = j['message']
                #mensaje_respuesta = j['message']
                estatus = j['code']
        else:
            mensaje_respuesta='Ningun Telefono es Valido'
        #num_enviados = get_num_enviados(mensaje_respuesta)
    file.close()
    c = {'mensaje': mensaje_respuesta, 'form': form, 'estatus': estatus, 'multi': multi, 'clientes_con_telefono_invalido': clientes_con_telefono_invalido, 'num_enviados': num_enviados,'num_no_enviados':num_no_enviados,'archivo':'numeros_invalidos\\'+nom_archivo,'nom_archivo':nom_archivo,}
    return render(request, template_name,c)
    #return render_to_response(template_name, c, context_instance=RequestContext(request))


@login_required(login_url='/login/')
def archivoView(request, template_name='django_msp_sms/personalizados.html'):
    apikey = str(Registry.objects.get(nombre='SIC_SMS_ApiKey').get_value())
    c = {}
    multi = False
    form = SMSForm(request.POST or None)
    mensaje_respuesta = ''
    estatus = ''
    if form.is_valid():
        mensaje = form.cleaned_data['mensaje']
        mensaje = mensaje.encode('ascii', 'replace')
        telefono = form.cleaned_data['telefono']
        sms_masivo = SMSMasivo(apikey=apikey, pruebas=modo_pruebas)

        if (len(telefono.split(',')) > 1):
            multi = True
            j = sms_masivo.multisend(mensaje=mensaje, telefono=telefono)
            mensaje_respuesta = j['respuestas']
            estatus = None
        else:
            j = sms_masivo.send(mensaje=mensaje, telefono=telefono)
            mensaje_respuesta = j['mensaje']
            estatus = j['estatus']

    c = {'mensaje': mensaje_respuesta, 'form': form, 'estatus': estatus, 'multi': multi, }
    return render(request, template_name,c)
    #return render_to_response(template_name, c, context_instance=RequestContext(request))
