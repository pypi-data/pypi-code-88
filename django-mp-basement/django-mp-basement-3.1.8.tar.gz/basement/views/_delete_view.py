
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


def delete_view(func):

    @csrf_exempt
    @require_POST
    def wrap(*args, **kwargs):
        return func(*args, **kwargs)

    return wrap
