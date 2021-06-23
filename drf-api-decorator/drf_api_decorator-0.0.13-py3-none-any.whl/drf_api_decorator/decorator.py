from rest_framework.exceptions import APIException


class MissingMandatoryKey(APIException):
    status_code = 400
    default_detail = 'Missing Mandatory Field'


def mandatory_key(request, name):
    try:
        if request.method == 'GET':
            data = request.GET[name]
        else:
            data = request.POST[name]
        if data == '':
            raise MissingMandatoryKey()
    except:
        try:
            json_body = request.data
            data = json_body[name]
            if data == "":
                raise MissingMandatoryKey()
        except:
            raise MissingMandatoryKey()
    return data


def optional_key(request, name, default_value=''):
    try:
        if request.method == 'GET':
            data = request.GET[name]
        else:
            data = request.POST[name]
        if data in ["", None, 'null', 'undefined']:
            data = default_value
    except:
        try:
            json_body = request.data
            data = json_body[name]
            if data in ["", None, 'null', 'undefined']:
                data = default_value
        except:
            data = default_value
    return data


def optionals(*keys):
    def decorate(func):
        def wrapper(APIView, *args, **kwargs):
            optional = dict()
            for arg in keys:
                for key, val in arg.items():
                    data = optional_key(APIView.request, key, val)
                    optional[key] = data
            return func(APIView, o=optional, *args, **kwargs)

        return wrapper

    return decorate


def mandatories(*keys):
    def decorate(func):
        def wrapper(APIView, *args, **kwargs):
            mandatory = dict()
            for key in keys:
                data = mandatory_key(APIView.request, key)
                mandatory[key] = data
            return func(APIView, m=mandatory, *args, **kwargs)

        return wrapper

    return decorate


def pagination():
    def decorate(func):
        def wrapper(APIView, *args, **kwargs):
            start_row, end_row = paging(APIView.request)
            return func(APIView, start_row=start_row, end_row=end_row, *args, **kwargs)

        return wrapper

    return decorate
