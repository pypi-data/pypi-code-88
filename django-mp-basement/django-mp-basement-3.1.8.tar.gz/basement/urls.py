
from django.apps import apps
from django.urls import path, include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView, TemplateView

from pydoc import locate
from basement import views


def get_urlpatterns(
        home_view=None,
        is_db_download_enabled=False):

    if home_view is None:
        home_view = TemplateView.as_view(template_name='home.html')

    result = [
        path('raise-exception/', lambda request: 1/0),

        path('', RedirectView.as_view(
            url='/{}/'.format(settings.LANGUAGE_CODE))
        )

    ] + i18n_patterns(
        path('', home_view, name='home')
    )

    if is_db_download_enabled:
        result.append(
            path('db/download/', views.download_db, name='download-db'))

    if apps.is_installed('ckeditor_uploader'):
        result.append(path('ckeditor/', include('ckeditor_uploader.urls')))

    for app in settings.INSTALLED_APPS:
        located_urls = locate('{}.urls.app_urls'.format(app))

        if not located_urls:
            continue

        result += located_urls

    return result
