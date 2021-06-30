from pydoc import locate

from django.urls import reverse
from django.conf import settings
from datetime import datetime
from django.utils.translation import activate
from django.contrib.sitemaps import Sitemap


class CommonSitemap(Sitemap):

    changefreq = 'monthly'
    priority = 1.0

    def items(self):

        result = []

        getters = self._collect_getters()

        for lang_code, lang_name in settings.LANGUAGES:

            activate(lang_code)

            for getter in getters:
                if getter is not None:
                    if settings.DEBUG:
                        print('{} {}'.format(lang_code, getter.__module__))
                    result += getter(lang_code=lang_code)

        return result

    def _collect_getters(self):

        result = []

        for app in settings.INSTALLED_APPS:
            result.append(locate('{}.sitemap.get_urls'.format(app)))

        return result

    def location(self, obj):
        return obj

    def lastmod(self, obj):
        return datetime.now()


def get_urls_from_qs(queryset):
    return [i.get_absolute_url() for i in queryset]


def get_urls_from_patterns(patterns):
    return [reverse(i) for i in patterns]
