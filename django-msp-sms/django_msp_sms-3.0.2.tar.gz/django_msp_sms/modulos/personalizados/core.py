from .models import *
import re
from django.db.models import Q

class TelefonosClientes(list):
    ''' diccionario de sms. '''
    
    def __init__(self, clientes=None, zona=None):
        self.clientes_con_telefono_invalido = []
        self.telefono_default = Registry.objects.get( nombre = 'SIC_SMS_TelDefault').get_value()
        self.telefonos=[]

        if clientes:
            self.clientes_sin_mensaje = clientes
        else:
            self.clientes_sin_mensaje = []    
        
        if clientes:
            self.get_telefonos_seleccion(clientes=clientes)
        elif zona:
            self.get_telefonos_zona(zona=zona)
        else:
            self.get_telefonos_todos()


    def validar_numeros(self,clientes):
        for cliente in clientes:
            cliente_nombre =  cliente[0].lstrip().rstrip()
            telefono =  cliente[1]
            if telefono:
                telefono = telefono.encode('utf-8')
                telefono = re.sub("[^0-9]", "", str(telefono))
                print(telefono)

                #validacion de telefonos invalidos  y creacion de mensajes
                if len(telefono) != 10 and cliente_nombre not in self.clientes_con_telefono_invalido:
                    # print("not")
                    # print(telefono)
                    self.clientes_con_telefono_invalido.append(cliente_nombre)
                elif not telefono in self.telefonos:
                    # print("yes")
                    # print(telefono)
                    self.telefonos.append(telefono)
            else:
                if not telefono in self.clientes_con_telefono_invalido:
                    self.clientes_con_telefono_invalido.append(cliente_nombre)
                    A = self.clientes_con_telefono_invalido
            
    def get_telefonos_todos(self):
        clientes = ClienteDireccion.objects.filter(es_ppal='S').filter(Q(cliente__no_enviar_sms=None) | Q(cliente__no_enviar_sms=0)).order_by('telefono1').values_list('cliente__nombre','telefono1',)
        self.validar_numeros(clientes)

    def get_telefonos_seleccion(self,clientes):
        clientes = ClienteDireccion.objects.filter(es_ppal='S', cliente__in=clientes).filter(Q(cliente__no_enviar_sms=None) | Q(cliente__no_enviar_sms=0)).order_by('telefono1').values_list('cliente__nombre','telefono1',)
        self.validar_numeros(clientes)

    def get_telefonos_zona(self,zona):
        clientes = ClienteDireccion.objects.filter(es_ppal='S', cliente__zona=zona).filter(Q(cliente__no_enviar_sms=None) | Q(cliente__no_enviar_sms=0)).order_by('telefono1').values_list('cliente__nombre','telefono1',)
        self.validar_numeros(clientes)

    def get_clientes_sin_mensajes(self):
        clientes = Cliente.objects.filter(id__in=self.clientes_sin_mensaje).values_list('nombre', flat=True)
        return clientes
