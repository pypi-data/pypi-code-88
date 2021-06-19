import requests
import json
NoneType = type(None)

class BaseAPIResponse(object):
    def __init__(self, response):
        self.response = response

    @property
    def is_success(self):
        return self.response.status_code < 400

    @property
    def is_error(self):
        return self.response.status_code >= 400

    @property
    def status_code(self):
        return self.response.status_code

    @property
    def not_found(self):
        return self.response.status_code == 404

class TextAPIResponse(BaseAPIResponse):
    pass

class DictAPIResponse(BaseAPIResponse, dict):
    def __init__(self, res):
        self.response = res
        self.update(res.json())

class ListAPIResponse(BaseAPIResponse, list):
    def __init__(self, res):
        self.response = res
        self.extend(res.json())

class StrAPIResponse(BaseAPIResponse, str):
    pass

class IntAPIResponse(BaseAPIResponse, int):
    pass

class FloatAPIResponse(BaseAPIResponse, float):
    pass

class BoolAPIResponse(BaseAPIResponse):
    def __init__(self, res):
        self.response = res
        self.value = res.json()

    @property
    def is_true(self):
        return self.value is True

    @property
    def is_false(self):
        return self.value is False

class NoneAPIResponse(BaseAPIResponse):
    def __init__(self, res):
        self.response = res
        self.value = res.json()

    # def __init__(self, res):
    #     self.response = res
    #     str.__init__(res.json())
    #     # import pdb; pdb.set_trace()
    #     # self.join(res.json())

class APIResponse(dict):
    text = None
    def __init__(self, res):
        self.response = res
        if res.status_code != 204:
            try:
                res_json = res.json()
            except json.decoder.JSONDecodeError:
                res_json = None

            if type(res_json) == dict:
                self.update(res_json)

            elif type(res_json) == str:
                self.update({"text": res_json})

    @property
    def is_success(self):
        return self.response.status_code < 400

    @property
    def is_error(self):
        return self.response.status_code >= 400

    @property
    def status_code(self):
        return self.response.status_code

    @property
    def not_found(self):
        return self.response.status_code == 404

    def as_dict(self):
        return dict(self)

class ApiWrapper():
    def __init__(self, base_url):
        self.base_url = base_url
        self.verbose_logging = False

    def make_request(self, method, endpoint, success_code=None, allowed_errors=None, **kwargs):
        allowed_errors = allowed_errors or []
        request = getattr(requests, method.lower())

        if self.verbose_logging:
            logger.info("--> [{}] {} {} {}".format(method, self.base_url, endpoint,  kwargs))

        resp = request('{}{}'.format(self.base_url, endpoint), **kwargs)

        if self.verbose_logging:
            logger.info("<-- [{}] {}".format(resp.status_code, resp))


        if resp.ok or resp.status_code in allowed_errors:
            if success_code and resp.status_code != success_code and resp.ok:
                raise KeyError("Response status code is not the expected one")

            try:
                res_json = resp.json()
                is_json = True
            except json.decoder.JSONDecodeError:
                is_json = False

            if not is_json:
                return TextAPIResponse(resp)

            if type(res_json) == dict:
                return DictAPIResponse(resp)

            elif type(res_json) == list:
                return ListAPIResponse(resp)

            elif type(res_json) == str:
                _resp = StrAPIResponse(res_json)
                _resp.response = resp
                return _resp

            elif type(res_json) == int:
                _resp = IntAPIResponse(res_json)
                _resp.response = resp
                return _resp

            elif type(res_json) == float:
                _resp = FloatAPIResponse(res_json)
                _resp.response = resp
                return _resp

            elif type(res_json) == bool:
                return BoolAPIResponse(resp)

            elif type(res_json) == NoneType:
                return NoneAPIResponse(resp)



        resp.raise_for_status()


    def head(self, *args, **kwargs):
        return self.make_request("head", *args, **kwargs)

    def get(self, *args, **kwargs):
        return self.make_request("get", *args, **kwargs)

    def post(self, *args, **kwargs):
        return self.make_request("post", *args, **kwargs)

    def put(self, *args, **kwargs):
        return self.make_request("put", *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.make_request("patch", *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.make_request("delete", *args, **kwargs)
