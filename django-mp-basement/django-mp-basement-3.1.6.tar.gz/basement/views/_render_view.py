
from django.shortcuts import render
from django.http.response import Http404
from django.core.exceptions import ObjectDoesNotExist

from basement.utils import decorate


def render_view(template_name, renderer=render, decorators=None):

    def decorator(view_func):

        def wrapper(request, *args, **kwargs):

            try:
                context = decorate(view_func, decorators)(
                    request, *args, **kwargs)
            except ObjectDoesNotExist:
                raise Http404

            return renderer(request, template_name, context)

        return wrapper

    return decorator
