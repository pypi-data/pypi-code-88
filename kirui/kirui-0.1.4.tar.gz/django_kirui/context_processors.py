from django.middleware import csrf
from django.urls import reverse


class DjangoSamonBinding:
    def __init__(self, request):
        self.request = request

    def url(self, view_name, *args, **kwargs):
        return reverse(view_name, args=args, kwargs=kwargs)

    @property
    def csrf_token(self):
        return csrf.get_token(self.request)


def djsamon(request):
    return {
        'djsamon': DjangoSamonBinding(request)
    }
