# #encoding:utf-8
# from celery import task
from .modulos.saldos_clientes.core import formar_mensaje


# @task
def enviar_correo(**kwargs):
    data=formar_mensaje(kwargs=kwargs)
    # print("**************************data")
    # print(data)
    return data
