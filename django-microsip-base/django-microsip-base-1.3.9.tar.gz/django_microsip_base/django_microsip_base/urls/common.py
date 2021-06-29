from dal import autocomplete
from django.conf.urls.static import static
#autocomplete.autodiscover()

#from django.conf.urls import  include, url
from django.urls import include, path,re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings

urlpatterns = [
    path('', include('django_microsip_base.apps.main.urls')),
    path('', include('microsip_api.apps.config.urls')),
    path('administrador/', include('microsip_api.apps.administrador.urls')),
    #path('autocomplete/', include('autocomplete.urls')),
    path("select2/", include("django_select2.urls")),
    # path('media/<string:path>', include('django.views.static.serve'),
    #     {'document_root': settings.MEDIA_ROOT, }),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
for plugin in settings.EXTRA_APPS:
    urlpatterns += path(''+plugin['url_main_path'], include(plugin['app']+'.urls')),

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    
urlpatterns += staticfiles_urlpatterns()
