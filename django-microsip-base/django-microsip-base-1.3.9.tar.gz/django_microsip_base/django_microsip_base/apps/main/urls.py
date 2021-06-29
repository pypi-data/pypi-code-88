from django.urls import  re_path,path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('informacion_cliente/', views.informacion_cliente),
    path('salida_creditos/', views.salida_creditos),
    #path('entrada_creditos/', views.entrada_creditos),
    path('lista_creditos/', views.lista_creditos),
    path('saldos_credit/', views.saldos_credit),
    path('preferencias/', views.preferencias),
    path('enviar_llave/', views.enviar_llave),
]