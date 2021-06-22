
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from flatpages.views import flatpage


app_name = 'flatpages'


urlpatterns = [

    path('<str:url>/', flatpage, name='page')

]


app_urls = i18n_patterns(
    path('page/', include((urlpatterns, app_name)))
)
