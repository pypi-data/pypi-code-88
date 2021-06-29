import requests
from leveropen.api_errors import APIError
from leveropen.utils import BASE_URL, VERSION


class Protocol:
    """

    :param access_token: Lever Open API Secret Token
    :type access_token: str
    :param base_url: e.g. ``'https://www.leveropen.com/api/'``
    :type base_url: str
    :param version: Lever Open API version e.g. ``'v1'``
    :type version: str

    :ivar host_url: (str) the host url for the Lever Open API
    :ivar session: (requests.Session()) the session
    """

    def __init__(self, access_token: str, base_url=BASE_URL, version=VERSION):
        self.host_url = base_url + version + "/"
        self.session = self.get_session(access_token=access_token)

    def get(
        self, url_ext: str, params: dict = None, verbose: bool = True
    ) -> requests.Response:
        """

        :param params: params to pass in the request
        :type params: dict
        :param verbose: if ``True`` then show print statements
        :type verbose: bool
        :param url_ext: URL extension to add to ``self.host_url``
        :return: requests.Response
        """
        url = self.host_url + url_ext
        if verbose:
            print(f"GET {url}")
            if params:
                print(f"with params: {params}")
        parameters = self.session.params
        if params:
            for k, v in params.items():
                parameters[k] = v
        resp = requests.get(url, params=parameters)
        resp = self._validate_response(resp=resp)
        return resp

    @staticmethod
    def _validate_response(resp):
        if resp.status_code != 200:
            raise APIError(resp=resp)
        else:
            return resp

    @staticmethod
    def get_session(access_token: str):
        """
        :param access_token: Lever Open API Secret Token
        :return: session
        :rtype: requests.Session()
        """
        session = requests.Session()
        session.params = {}
        session.params["token"] = access_token
        return session
