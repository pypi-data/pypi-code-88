from rest_framework.exceptions import ParseError

def mandatory_key(request, name):
    try:
        if request.method == 'GET':
            data = request.GET[name]
        else:
            data = request.POST[name]
        if data == '':
            raise ParseError(detail="Missing Mandatory Field")
    except:
        try:
            json_body = request.data
            data = json_body[name]
            if data == "":
                raise ParseError(detail="Missing Mandatory Field")
        except:
            raise ParseError(detail="Missing Mandatory Field")
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


def paging(request):
    page = int(request.GET.get('page', 1)) - 1
    size = int(request.GET.get('size', 10))
    start_row = page * size
    end_row = (page + 1) * size
    return start_row, end_row


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
