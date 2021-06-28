from .microservices import AbstractMicroservice
from rest_framework.exceptions import APIException


class PainkillerUnavailable(APIException):
    status_code = 503
    default_detail = 'Order service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'


class GreatPumpkinUnavailable(APIException):
    status_code = 503
    default_detail = 'Payment service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'


class CementMixerUnavailable(APIException):
    status_code = 503
    default_detail = 'Location service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

class PainkillerClient(AbstractMicroservice):

    def __init__(self):
        super().__init__(
            url_prefix="pain",
            localhost_port="7777",
            service_name='painkiller',
            exception=PainkillerUnavailable,
            api_version="v1",
            service_description='order manager'
            )


class GreatPumpkinClient(AbstractMicroservice):
    def __init__(self):
        super().__init__(
            url_prefix="pumpkin",
            localhost_port="2344",
            service_name='great-pumpkin',
            exception=GreatPumpkinUnavailable,
            api_version="v1",
            service_description='payment manager'
        )


class CementMixerClient(AbstractMicroservice):

    def __init__(self):
        super().__init__(
            url_prefix="api",
            localhost_port="8000",
            service_name='cement-mixer',
            exception=CementMixerUnavailable,
            api_version="v1",
            service_description='location manager'
        )
