import json as Json


def json_to_dict(json):
    if isinstance(json, dict): return json

    if not json: return {}
    json = json.replace('\'', '"')
    try:
        return Json.loads(json)
    except:
        print(f'Invalid json data: {json}')
        return {}


def body_to_dict(data):
    if isinstance(data, dict): return data

    if not data: return {}
    assert '=' in data, f'Invalid data: {data}'
    return dict(_.split('=', 1) for _ in data.split('&'))


def url_to_dict(url):
    if not url: return {}

    url = url.replace('://', '/')

    _path, _param = _spilt_url(url)
    protocol, domain, *path = _path.split('/')
    if _param:
        if '=' in _param:
            param = dict(p.split('=', 1) for p in _param.split('&'))
        else:
            param = {_param: _param}
    else:
        param = {}

    return {
        'protocol': protocol,
        'domain': domain,
        'path': path,
        'param': param
    }


def _spilt_url(url):
    if not url: return {}
    path = url.split('?', 1)
    return [path[0], ''] if len(path) == 1 else path


def dict_to_url(data):
    protocol = data.get('protocol')
    domain = data.get('domain')
    path = '/'.join(data.get('path'))
    _param = data.get('param')

    if len(_param) == 1 and len(set(list(_param.items())[0])) == 1:
        param = list(_param.values())[0]
    else:
        param = dict_to_body(_param)

    return f'{protocol}://{domain}/{path}?{param}'.strip('?')


def headers_to_dict(headers):
    if isinstance(headers, dict): return headers

    if not headers: return {}
    return {_.split(':', 1)[0].strip(): _.split(':', 1)[1].strip() for _ in headers.split('\n') if
            len(_.split(':', 1)) == 2}


def cookies_to_dict(cookies):
    if isinstance(cookies, dict): return cookies

    if not cookies: return {}
    return {_.split('=')[0].strip(): _.split('=')[1].strip() for _ in cookies.split(';')}


def dict_to_body(data: dict):
    return '&'.join([f'{key}={value}' for key, value in data.items()])


def dict_to_json(json: dict):
    return Json.dumps(json)
