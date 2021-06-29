#encoding:utf-8
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# user autentication
from .models import *
from .forms import *
from django.views.generic.list import ListView
from django.shortcuts import render,redirect, get_object_or_404
from cryptography.fernet import Fernet
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from datetime import datetime
import os
import json

class ClienteListView(ListView):
    context_object_name = "clientes"
    model = Cliente
    template_name = 'django_msp_sms/clientes/clientes.html'
    paginate_by = 50

    def get_queryset(self):
        
        get_dict = self.request.GET
        form =  ClienteSearchForm(self.request.GET)
        if form.is_valid():
            cliente = form.cleaned_data['cliente']
            nombre = form.cleaned_data['nombre']
            clave = form.cleaned_data['clave']
            clientes = Cliente.objects.all()
            if nombre:
                clientes = clientes.filter(nombre__contains=nombre)
            if clave:
                claves = ClienteClave.objects.filter(clave=clave)
                if claves:
                    clientes = Cliente.objects.filter(pk=claves[0].cliente.id)
            if cliente:
                clientes = Cliente.objects.filter(pk=cliente.id)

        return clientes

    def get_context_data(self, **kwargs):
        context = super(ClienteListView, self).get_context_data(**kwargs)
        context['form'] = ClienteSearchForm(self.request.GET or None)
        return context


@login_required(login_url='/login/')
def IgnorarView(request):
    cliente_id = request.GET['cliente_id']
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if cliente.no_enviar_sms :
        cliente.no_enviar_sms = False
    else:
        cliente.no_enviar_sms = True
    cliente.save()
    data = { 
            'cliente':cliente.nombre,
        }

    data = json.dumps(data)
    #return render(request, template_name,c)
    return HttpResponse(data, content_type='application/json')

# @login_required(login_url='/login/')
# def ClienteManageView(request, id=None, template_name='django_msp_sms/clientes/cliente.html'):
#     ''' Modificacion de puntos de un cliente '''

#     cliente = get_object_or_404(Cliente, pk=id)
#     form = ClienteManageForm(request.POST or None, instance= cliente)
  
#     #Si los datos de los formularios son correctos # and 
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect('/sms/clientes/')
#     c = {'form':form, 'cliente_nombre':cliente.nombre,}  
#     return render_to_response(template_name, c, context_instance=RequestContext(request))

def cargar_archivo(request):
    form=FileForm(request.POST or None)
    directorio=settings.MEDIA_ROOT+'\\llave_saldo\\'
    data=[]
    mensaje=None
    try:
        os.mkdir(directorio)
    except OSError:
        print("La creación del directorio %s falló" % directorio)
    else:
        print("Se ha creado el directorio: %s " % directorio)

    if form.is_valid():
        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y_%H%M")
        archivo=request.FILES['archivo']
        clave=cargar_clave()
        print("POST")
        print(directorio+archivo.name)
        if os.path.isfile(directorio+archivo.name):
            mensaje="Ya se cargo este archivo de saldo"
            print(mensaje)
        else:
            path = default_storage.save('llave_saldo/'+archivo.name, ContentFile(archivo.read()))
            tmp_file = os.path.join(directorio, path)
            desencript(directorio+archivo.name,clave)
            file = open(directorio+archivo.name, "r")
            for line in file:
                data.append(line.strip())
            if float(Registry.objects.get(nombre='SIC_SMS_Saldo').get_value())==0:
                saldo = Registry.objects.get(nombre = 'SIC_SMS_Saldo')
                saldo.valor=str(float(saldo.valor)+float(data[1]))
                saldo.save()
            else:
                saldo = Registry.objects.get(nombre = 'SIC_SMS_Saldo')
                saldo.valor=data[1]
                saldo.save() 
            
            mensaje="Saldo agregado regrese a la pagina principal"
            print(mensaje)

    
    return render( request,'django_msp_sms/clientes/cargar_archivo.html',{'form':form,'mensaje':mensaje,})

def add_archivo(request):
    creditos = request.GET['creditos']
    print("add_creditos",creditos)
    if Registry.objects.get(nombre='SIC_SMS_Saldo').get_value():
        saldo = Registry.objects.get(nombre = 'SIC_SMS_Saldo')
        saldo.valor=str(float(saldo.valor)+float(creditos))
        saldo.save()
    else:
        saldo = Registry.objects.get(nombre = 'SIC_SMS_Saldo')
        saldo.valor=creditos
        saldo.save() 

    archivo={}      
    return HttpResponse(json.dumps(data), content_type='application/json')

def generar_clave():
    clave=Fernet.generate_key()
    with open("sic_clave.key","wb") as archivo_clave:
        archivo_clave.write(clave)

def cargar_clave():
    return open("sic_clave.key","rb").read()

def encript(nom_archivo,clave):
    f=Fernet(clave)
    with open(nom_archivo,"rb") as file:
        archivo_info=file.read()
    encrypted_data=f.encrypt(archivo_info)
    with open(nom_archivo,"wb") as file:
        file.write(encrypted_data)

def desencript(nom_archivo,clave):
    f=Fernet(clave)
    with open(nom_archivo,"rb") as file:
        encrypted_data=file.read()
    decrypted_data=f.decrypt(encrypted_data)
    with open(nom_archivo,"wb") as file:
        file.write(decrypted_data)
