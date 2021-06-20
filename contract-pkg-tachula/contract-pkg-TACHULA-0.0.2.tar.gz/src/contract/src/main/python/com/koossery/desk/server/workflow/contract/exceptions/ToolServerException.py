#  here we define tool server exception


from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler


class ToolSeverException(APIException):
    def __init__(self, id, message):
        super().__init__( message)
        self.id = id
        self.message = message



