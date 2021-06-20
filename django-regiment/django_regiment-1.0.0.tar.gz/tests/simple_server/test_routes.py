from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_regiment import bulletlog


@csrf_exempt
def index(*args, **kwargs):
    return HttpResponse("works")

@csrf_exempt
def error(*args, **kwargs):
    raise Exception("custom exception")

@csrf_exempt
def custom(*args, **kwargs):
    bulletlog.log_info("custom log from django")
    return HttpResponse("custom log logged")