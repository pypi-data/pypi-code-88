
from django.shortcuts import render, redirect
from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page

from seo.models import RedirectRecord, ErrorRecord


@cache_page(60 * 15)
def sitemap_download(request):

    try:
        from core.sitemaps import CommonSitemap
    except ImportError:
        from seo.sitemaps import CommonSitemap

    return sitemap(request, {'generic': CommonSitemap})


def sitemap_tree(request):
    return render(request, 'sitemap.html')


def page_not_found(request, **kwargs):

    path = request.path

    try:
        record = RedirectRecord.objects.get(old_path=path)
        return redirect(record.new_path, permanent=True)
    except RedirectRecord.DoesNotExist:
        pass

    if not path.startswith('/static/') and not path.startswith('/media/'):
        ErrorRecord.create(request, 404)

    return render(request, '404.html')
