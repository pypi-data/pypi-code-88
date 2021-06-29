# from django.conf.urls import patterns, url
from django.urls import path,include
from .views import ClienteListView,IgnorarView,cargar_archivo,add_archivo

urlpatterns = (
	path('clientes/', ClienteListView.as_view()),
	path('ignorar/', IgnorarView),
	path('cargar_archivo/', cargar_archivo),
	path('add_archivo/', add_archivo),
		
)

