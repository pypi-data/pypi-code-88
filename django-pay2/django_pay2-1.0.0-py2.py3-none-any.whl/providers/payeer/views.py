import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .functions import get_payeer_api
from .exceptions import PayeerValidationError, AlreadyPaid


@method_decorator(csrf_exempt, name="dispatch")
class NotifyView(generic.View):
    def post(self, request, *args, **kwargs):
        api = get_payeer_api()
        try:
            result = api.notify(request.POST)
        except PayeerValidationError as exc:
            return HttpResponse(f"{exc.order_id}|error")
        except AlreadyPaid as exc:
            return HttpResponse(f"{exc.order_id}|success")

        result.payment.accept()
        return HttpResponse(f"{result.raw_order_id}|success")
