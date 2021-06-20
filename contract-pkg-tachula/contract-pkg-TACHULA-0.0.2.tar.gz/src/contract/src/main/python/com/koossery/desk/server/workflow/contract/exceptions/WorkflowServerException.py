#  here we define workflow  server exception
from rest_framework.exceptions import APIException


class WorkflowSeverException(APIException):
    def __init__(self, id, message):
        super().__init__(message)
        self.id = id
        self.message = message
