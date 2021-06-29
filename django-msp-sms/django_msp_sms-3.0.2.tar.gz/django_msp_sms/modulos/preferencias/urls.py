# from django.conf.urls import patterns, url
from django.urls import path,include
from .views import PreferenciasManageView,InitialzeConfigurationDatabase

urlpatterns = (
path('preferencias/', PreferenciasManageView),
path('inicializar/', InitialzeConfigurationDatabase),
		
)

