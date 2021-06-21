from fastapi.exceptions import HTTPException


class HTTPNotFoundException(HTTPException):
    def __init__(self, resource: str, *args, **kwargs):
        super().__init__(404, f"{resource} not found.", *args, **kwargs)


class ResourceExistsException(HTTPException):
    def __init__(self, resource: str, *args, **kwargs):
        super().__init__(400, f"{resource} already exists.", *args, **kwargs)
