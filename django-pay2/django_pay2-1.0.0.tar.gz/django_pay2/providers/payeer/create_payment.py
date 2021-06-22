from django_pay2.exceptions import CreatePaymentError
from django_pay2.decorators import handle_debug
from django_pay2.models import Payment

from .functions import get_payeer_api
from .exceptions import PayeerError


@handle_debug
def create_payeer_payment(request, amount, desc, receiver, currency):
    payment = Payment.objects.create(amount=amount, receiver=receiver)
    try:
        api = get_payeer_api()
        return api.create_payment(str(payment.id), amount, currency, desc)
    except PayeerError as exc:
        payment.reject()
        raise CreatePaymentError(str(exc))
