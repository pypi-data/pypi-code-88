from rest_framework import status
from rest_framework.exceptions import APIException


class MessageStillProcessingException(APIException):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_detail = "Message is Still processing"
    default_code = "too_many_requests"
