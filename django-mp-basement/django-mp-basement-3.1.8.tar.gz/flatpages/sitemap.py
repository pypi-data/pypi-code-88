
from flatpages.models import FlatPage

from seo.sitemaps import get_urls_from_qs


def get_urls(**kwargs):
    return get_urls_from_qs(FlatPage.objects.all())
