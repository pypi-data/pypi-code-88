# from django.conf.urls import patterns
from django.urls import path,include
from . import views

urlpatterns = (
    path('saldos/por_seleccion/', views.PorSeleccionView),
    path('saldos/get_mensajes_saldos/', views.get_mensajes_saldos),
    path('saldos/enviar_cargo/', views.enviar_cargos_seleccion),
    path('saldos/todos/', views.todos_view),
    path('saldos/todos_automatico_preferencias/', views.saldos_automaticos_preferencias),
    path('saldos/todos_automatico/', views.envia_saldos_automaticos),
    path('saldos/enviar_por_vencer/', views.enviar_cargos_por_vencer),
    path('saldos/por_vencer_automatico_preferencias/', views.saldos_por_vencer_automaticos_preferencias),
)
