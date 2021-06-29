# from django.conf.urls import patterns, url, include
from django.urls import path,include
from . import views
from .modulos.preferencias import urls as preferencias_urls
from .modulos.personalizados import urls as personalizados_urls
from .modulos.saldos_clientes import urls as saldos_clientes_urls
from .modulos.clientes import urls as clientes_urls

urlpatterns = (
    path('', views.index),
    #ajax
    path('enviar_sms/', views.enviar_smsView),
    path('enviar_mensaje/', views.enviar_mensaje),
    path('get_creditos/', views.get_creditos),
    path('get_mensajes_personalizados/', views.get_mensajes_personalizados),

    #personalizados
    path('personalizados/por_telefono/', views.personalizadosView),
    path('clientes_autocomplete/', views.ClienteAutocomplete),

    path('', include(preferencias_urls)),
    path('', include(personalizados_urls)),
    path('', include(saldos_clientes_urls)),
    path('', include(clientes_urls)),
)
 