# from django.conf.urls import patterns, url
from django.urls import path,include
from .views import TodosView, PorSeleccionView, ZonaView

urlpatterns = (
	path('personalizados/todos/', TodosView),
	path('personalizados/por_seleccion/', PorSeleccionView),	
	path('personalizados/por_zona/', ZonaView),
)

