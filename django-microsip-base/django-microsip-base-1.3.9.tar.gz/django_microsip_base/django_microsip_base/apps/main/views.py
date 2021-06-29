#encoding:utf-8
from .forms import *
from django.shortcuts import render_to_response,render,HttpResponse
from django.template import RequestContext
from microsip_api.comun.sic_db import first_or_none
from datetime import datetime
# user autentication
from django.contrib.auth.decorators import login_required
from microsip_api.comun.sic_db import get_conecctionname, get_existencias_articulo
from django_microsip_base.libs.models_base.models import Articulo,ArticuloPrecio,ArticuloClave, Moneda, PrecioEmpresa,Registry,ClienteDireccion, Cliente, CondicionPago, Vendedor, VentasDocumento, VentasDocumentoDetalle, Almacen,ClienteClave,VentasDocumentoLiga,SaldosSms
from datetime import datetime
import json
import textwrap
import time
import requests
import cfscrape
import re
import os
from django.db.models import F, FloatField, Sum
from cryptography.fernet import Fernet
from django.conf import settings
from .storage import send_mail_llave

@login_required( login_url = '/login/' )
def index( request ):

	return render( request,'main/index.html',{})

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

def preferencias(request):
	padre = first_or_none(Registry.objects.filter(nombre='PreferenciasEmpresa'))
	if not Registry.objects.filter( nombre = 'SIC_Administrador_Email' ).exists():
			Registry.objects.create(
				nombre = 'SIC_Administrador_Email',
				tipo = 'V',
				padre = padre,
				valor= '',
			)
	if not Registry.objects.filter( nombre = 'SIC_Administrador_Password' ).exists():
			Registry.objects.create(
				nombre = 'SIC_Administrador_Password',
				tipo = 'V',
				padre = padre,
				valor= '',
			)
	if not Registry.objects.filter( nombre = 'SIC_Administrador_Servidro_Correo' ).exists():
			Registry.objects.create(
				nombre = 'SIC_Administrador_Servidro_Correo',
				tipo = 'V',
				padre = padre,
				valor= '',
			)
	if not Registry.objects.filter( nombre = 'SIC_Administrador_Puerto' ).exists():
			Registry.objects.create(
				nombre = 'SIC_Administrador_Puerto',
				tipo = 'V',
				padre = padre,
				valor= '',
			)

	email= Registry.objects.get( nombre = 'SIC_Administrador_Email').get_value()
	password= Registry.objects.get( nombre = 'SIC_Administrador_Password').get_value()
	servidor_correo= Registry.objects.get( nombre = 'SIC_Administrador_Servidro_Correo').get_value()
	puerto= Registry.objects.get( nombre = 'SIC_Administrador_Puerto').get_value()
	form_initial = {
		'email':email,
		'password':password,
		'servidor_correo':servidor_correo,
		'puerto':puerto,
	}
	form = PreferenciasManageForm(request.POST or None,initial=form_initial)
	if form.is_valid():
		form.save()
	context = {
		'form': form,
	}
	return render(request, 'main/preferencias.html', context)

def informacion_cliente(request):
	rfc_cliente = request.GET['rfc_cliente']
	saldos=None
	suma_s=0.0
	suma_e=0.0
	cliente=first_or_none(ClienteDireccion.objects.filter(rfc_curp=rfc_cliente))

	if cliente:
		saldos=SaldosSms.objects.filter(cliente=cliente.cliente).order_by('fecha').last()
		suma_salida=SaldosSms.objects.filter(cliente=cliente.cliente,tipo='S').aggregate(Sum('cantidad'))
		if suma_salida['cantidad__sum']:
			suma_s=float(suma_salida['cantidad__sum'])
		
		suma_entrada=SaldosSms.objects.filter(tipo='E').aggregate(Sum('cantidad'))
		if suma_entrada['cantidad__sum']:
			suma_e=float(suma_entrada['cantidad__sum'])

		#print("---------",suma_s)
	# targetURL = "https://api.smsmasivos.com.mx/credits/consult"
	# headers = {
	#   "Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain",
	#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
	#   'apikey':"803ed1d5d94d5f5ee676750ac72c37146c27078b",
	# }
	# scraper = cfscrape.create_scraper()
	# r = scraper.post(url = targetURL, data = {}, headers = headers)
	# dict_cred=json.loads(r.text)
	creditos=suma_e-suma_s
	if cliente:
		if saldos:
			data={
				'cliente':cliente.cliente.nombre,
				'ultimo_saldo':saldos.cantidad,
				'fecha':str(saldos.fecha),
				'creditos':creditos,

			}
		else:
			data={
				'cliente':cliente.cliente.nombre,
				'ultimo_saldo':"",
				'fecha':"",
				'creditos':creditos,
			}
	else:
		data={
			'cliente':"",
			'ultimo_saldo':"",
			'fecha':"",		
			'creditos':creditos,
		}
	print(data)
	return HttpResponse(json.dumps(data), content_type='application/json')

def salida_creditos(request):
	try:
		rfc_cliente = request.GET['rfc_cliente']
		creditos = request.GET['creditos']
		cliente=first_or_none(ClienteDireccion.objects.filter(rfc_curp=rfc_cliente))
		SaldosSms.objects.create(
			tipo='S',
			cliente=cliente.cliente,
			cantidad=float(creditos),
			fecha=datetime.now(),
				)

		data={
			'mensaje':"Se han agregado "+creditos+ " a tu cuenta",
		}
	except Exception as e:
		print(e)
		data={
			'mensaje':"Ocurrio un error al agregar los creditos contactar con el administrador del sistema",
		}

	return HttpResponse(json.dumps(data), content_type='application/json')

@login_required( login_url = '/login/' )
def lista_creditos(request):
	form=SearchForm(request.POST or None)
	saldos=SaldosSms.objects.all()  
	if form.is_valid():
		cliente=form.cleaned_data['cliente']		
		tipo=form.cleaned_data['tipo']
		print(tipo)
		if cliente:
			saldos=saldos.filter(cliente=cliente)
		if tipo:
			saldos=saldos.filter(tipo=tipo)

	context={
		'form':form,
		'saldos':saldos,
	}

	return render( request,'main/lista_creditos.html',context)

def saldos_credit(request):
	now = datetime.now()
	form=SaldoForm(request.POST or None)
	directorio=settings.MEDIA_ROOT+'\\llaves\\'
	archivo=None
	email=None
	nom_archivo=None
	suma_s=0.00
	suma_e=0.00
	creditos=0.00
	mensaje=None
	try:
		os.mkdir(directorio)
	except OSError:
		print("La creación del directorio %s falló" % directorio)
	else:
		print("Se ha creado el directorio: %s " % directorio)
	
	if form.is_valid():
		date_time = now.strftime("%m-%d-%Y_%H%M")
		clave=cargar_clave()

		tipo=form.cleaned_data['tipo']
		cliente=form.cleaned_data['cliente']
		cantidad=form.cleaned_data['cantidad']

		if cliente:
			
			#saldos=SaldosSms.objects.filter(cliente=cliente).order_by('fecha').last()
			suma_salida=SaldosSms.objects.filter(tipo='S').aggregate(Sum('cantidad'))
			
			if suma_salida['cantidad__sum']:
				suma_s=float(suma_salida['cantidad__sum'])
			
			suma_entrada=SaldosSms.objects.filter(tipo='E').aggregate(Sum('cantidad'))
			
			if suma_entrada['cantidad__sum']:
				suma_e=float(suma_entrada['cantidad__sum'])

			creditos=suma_e-suma_s
			print("***************************************")
			print(creditos)
			
			if float(cantidad) > creditos and tipo=='S':
				mensaje='No hay suficiente credito para hacer esa entrada. Credito disponible'+str(creditos)
			else:
				dir_cli=first_or_none(ClienteDireccion.objects.filter(cliente=cliente,es_ppal='S'))
				archivo='llaves\\'+dir_cli.rfc_curp+date_time+'.txt'
				email=dir_cli.email
				nom_archivo=archivo.replace('llaves\\','')
				file = open(directorio+nom_archivo, "w")
				file.write(dir_cli.rfc_curp+'\n')
				file.write(str(cantidad)+'\n')
				file.write(date_time+'\n')
				file.write('Activo')

				file.close()
				
				encript(directorio+nom_archivo,clave)
		
		if float(cantidad) <= creditos and tipo=='S':
			form.instance.archivo=archivo
			form.instance.tipo=tipo
			form.save()
	

	context={
		'form':form,
		'saldos':'0',
		'archivo':archivo,
		'email':email,
		'nom_archivo':nom_archivo,
		'mensaje':mensaje,
	}
	return render( request,'main/saldos_credit.html',context)

def enviar_llave(request):
	email = request.GET['email']
	archivo = request.GET['archivo']
	directorio=settings.MEDIA_ROOT+'\\llaves\\'
	file=directorio+archivo
	email= Registry.objects.get( nombre = 'SIC_Administrador_Email').get_value()
	password= Registry.objects.get( nombre = 'SIC_Administrador_Password').get_value()
	servidor_correo= Registry.objects.get( nombre = 'SIC_Administrador_Servidro_Correo').get_value()
	puerto= Registry.objects.get( nombre = 'SIC_Administrador_Puerto').get_value()
	bandera=send_mail_llave(servidor_correo,puerto,email,password,email,"LLAVE SALDOS","<p>Archivo para agregar creditos</p>",file,archivo)

	data={
		'bandera':bandera,
	}
	print(data)
	return HttpResponse(json.dumps(data), content_type='application/json')