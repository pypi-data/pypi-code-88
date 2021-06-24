from bravado.requests_client import RequestsClient, RequestsFutureAdapter, \
    RequestsResponseAdapter
from marketsight._compat import json
import requests


class MsRequestsClient(RequestsClient):
    """The synchronous HTTP client used by the MarketSight library."""

    def __init__(
        self,
        ssl_verify=True,  # type: bool
        ssl_cert=None,  # type:  typing.Any
        future_adapter_class=RequestsFutureAdapter,
        response_adapter_class=RequestsResponseAdapter,
    ):
        # type: (...) -> None

        self.session = requests.Session()
        adapt = requests.adapters.HTTPAdapter(
            pool_connections=500,
            pool_maxsize=500
        )
        self.session.mount('http://', adapt)
        self.session.mount('https://', adapt)

        self.authenticator = None  # type: typing.Optional[Authenticator]
        self.ssl_verify = ssl_verify
        self.ssl_cert = ssl_cert
        self.future_adapter_class = future_adapter_class
        self.response_adapter_class = response_adapter_class


    def request(
        self,
        request_params,  # type: typing.MutableMapping[str, typing.Any]
        operation = None,  # type: typing.Optional[Operation]
        request_config = None,  # type: typing.Optional[RequestConfig]
    ):
        """Execute a synchronous HTTP request.

        :param request_params: Complete map of HTTP request instructions. Expects a
          :class:`dict <python:dict>` with keys: ``url``, ``method``, ``headers``, etc.
          compliant with the :func:`requests.api.request() <requests:requests.api.request>`
          function.
        :type request_params: :class:`dict <python:dict>` with
          :class:`str <python:str>` keys

        :param operation: The :term:`Swagger`
          :class:`Operation <bravado_core:operation.Operation>` to execute in the
          request. Defaults to :obj:`None <python:None>`.
        :type operation: :class:`bravado_core.operation.Operation <bravado_core:operation.Operation>` /
          :obj:`None <python:None>`

        :param request_config: Configuration of the HTTP request. Defaults to
          :obj:`None <python:None>`.
        :type request_config: :class:`bravado.config.RequestConfig <bravado:config.RequestConfig>` /
          :obj:`None <python:None>`.

        :returns: A :class:`Future <concurrent.futures.Future>`-like
          object that represents the HTTP response.
        :rtype: :class:`HttpFuture <bravado:bravado.http_future.HttpFuture`

        """
        if (
            hasattr(operation, "consumes")
            and "multipart/form-data" in operation.consumes
            and [
                param
                for param in operation.op_spec.get("parameters", [])
                if param.get("in") == "formData"
            ]
        ) or request_params.get("files"):

            files = {}

            if request_params.get("files"):
                for f in request_params.get("files"):
                    files[f[0]] = f[1][1]

            if request_params.get("data"):
                for k, v in request_params.get("data").items():
                    if isinstance(v, dict):
                        files[k] = json.dumps(v)
                    else:
                        files[k] = v
                del request_params["data"]

            request_params["files"] = files

        return super(MsRequestsClient, self).request(
            request_params=request_params,
            operation=operation,
            request_config=request_config,
        )
