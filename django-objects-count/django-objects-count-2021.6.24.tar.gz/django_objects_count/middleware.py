from django.apps import apps
from django.contrib import admin
from django.urls import reverse

from .models import Model
from .utils import get_count, get_model, init_models, update_count

class ObjectsCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(reverse('admin:index')):
            init_models()
            for m in Model.objects.filter(is_middleware=True):
                model = get_model(m.db_table)
                if model:
                    try:
                        count = get_count(m.db_table)
                        update_count(m,count)
                        verbose_name_plural = '%ss (%s)' % (model._meta.verbose_name,count)
                    except Exception as e:
                        verbose_name_plural = model._meta.verbose_name
                    model._meta.verbose_name_plural = verbose_name_plural
        return self.get_response(request)
