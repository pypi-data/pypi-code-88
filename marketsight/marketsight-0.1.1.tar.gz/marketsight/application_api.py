import inspect
import hashlib
import pathlib
import functools
from time import sleep
import requests
import logging
import copy
import re
import json
from urllib.parse import urlparse
import dpath.util
from dateutil import parser

from bravado.client import SwaggerClient, inject_headers_for_remote_refs
from bravado.config import bravado_config_from_config_dict
from bravado.requests_client import Authenticator
from bravado.swagger_model import Loader
from bravado_core.formatter import SwaggerFormat
from bravado_core.model import Model

from bravado_core.spec import Spec
from requests.cookies import cookiejar_from_dict
from validator_collection import validators, checkers

from marketsight.http_client import MsRequestsClient

import marketsight.exceptions as ms_exp
import io

log = logging.getLogger(__name__)


__version__ = "11.2.0"

OPENAPI_URL = 'https://application.marketsight.com/api/v1/swagger/public.json'


class Helper(object):
    """Helper object that enables the download of binary data from an API given
    a delay."""

    api = None

    def __init__(self, api):
        """
        :param api: The API instance.

        :returns: A ``Helper`` instance
        :rtype: :class:`Helper`

        """
        self.api = api

    def wait_until(
        self,
        fnc,
        fnc_kwargs: dict,
        conditions: dict,
        sleep_time=5,
        max_attempts=60,
    ):
        """
        This helper allows to invoke function `fnc` with the `fnc_kwargs`
        as params every `sleep_time` second, and return result of invoking
        if `conditions` on result return True

        .. warning::

          If the operation is not complete after ``max_attempts``, then the
          result returned will be :obj:`None <python:None>`. **An error will not
          be raised**, however an error will be logged.

        :param fnc: The function that should be called periodically by the
          :class:`Helper` class.
        :type fnc: callable

        :param fnc_kwargs: The keyword arguments to supply to the function
          ``fnc``.
        :type fnc_kwargs: :class:`dict <python:dict>`

        :param conditions: A set of conditions against which to check the result
          returned by the function ``fnc``. Expects a
          :class:`dict <python:dict>` where each key represents a key or
          object attribute on the result of ``fnc``, and the value represents a
          value which must be present / matched on the result of ``fnc`` to
          proceed.
        :type conditions: :class:`dict <python:dict>`

        :param sleep_time: The number of seconds to wait between attempts.
          Defaults to ``5``.
        :type sleep_time: :class:`int <python:int>`

        :param max_attempts: The maximum number of attempts to make. Defaults to
          ``60``.
        :type max_attempts: :class:`int <python:int>`

        :returns: The result of ``fnc`` OR :obj:`None <python:None>`

        :raises ValueError: if ``max_attempts`` cannot be coerced to an
          :class:`int <python:int>`
        :raises ValueError: if ``sleep_time`` is not numeric

        :example:

        .. code-block:: python
           :linenos:

           job = api.wait_until(fnc = api.Jobs.retrieve,
                                fnc_kwargs = {'job_id': 1},
                                conditions = {'result': 'succeeded'}
                                )


        """
        res = None
        ready = False
        attempt = 0

        sleep_time = validators.numeric(sleep_time, allow_empty = False)
        max_attempts = validators.integer(max_attempts,
                                          allow_empty = False,
                                          coerce_value = True,
                                          minimum = 1)

        if not conditions:
            raise ValueError("conditions cannot be empty")

        while not ready:
            attempt += 1
            if attempt == max_attempts:
                log.error(
                    f"conditions were unsuccessful"
                    f"for {sleep_time * max_attempts} seconds"
                )
                break
            res = fnc(**fnc_kwargs)

            ready = all([getattr(res, k) == v for k, v in conditions.items()])
            if ready:
                return res

            log.info(
                f"Wait {sleep_time} sec. " f"{attempt}/{max_attempts} attempts"
            )
            sleep(sleep_time)

        return res

    def download_blob_data(self, job_id, sleep_time=5, max_attempts=50):
        """Download a collection of binary data items associated with ``job_id``
        from the Dynata Reporting & Analytics API.

        :param job_id: The unique identifier of the :term:`Job` whose data should
          be downloaded.

        :param sleep_time: The number of seconds to wait between download attempts.
          Defaults to ``5``.
        :type sleep_time: :class:`int <python:int>`

        :param max_attempts: The maximum number of download attempts to make.
          Defaults to ``50``.
        :type max_attempts: :class:`int <python:int>`

        :returns: a :class:`list <python:list>` of :class:`dict <python:dict>`
          objects where each :class:`dict <python:dict>` contains a key with
          a given job name and the underlying byte-data from the downloaded BLOB.
        :rtype: :class:`list <python:list>` of :class:`dict <python:dict>`

        """

        job = self.wait_until(
            fnc=self.api.Jobs.retrieve,
            fnc_kwargs={"job_id": job_id},
            conditions={"result": "succeeded"},
            sleep_time=sleep_time,
            max_attempts=max_attempts,
        )

        result = []
        for blob in job.blobs:
            name = getattr(blob, "name", None)
            data = io.BytesIO(
                self.api.Jobs.get_blob_data(job_id=job.id, blob_id=blob.id)
            )
        return result

    def wait_and_download_blob(self, job_id, sleep_time=6, max_attempts=20):
        """Download a single binary item associated with ``job_id``
        from the Dynata Reporting & Analytics API.

        :param job_id: The unique identifier of the :term:`Job` whose data should
          be downloaded.

        :param sleep_time: The number of seconds to wait between download attempts.
          Defaults to ``6``.
        :type sleep_time: :class:`int <python:int>`

        :param max_attempts: The maximum number of download attempts to make.
          Defaults to ``20``.
        :type max_attempts: :class:`int <python:int>`

        :returns: a bytes-literal with the data from all binary items (blobs)
          returned by ``job_id``.
        :rtype: :class:`bytes`

        """

        job = self.wait_until(
            fnc=self.api.Jobs.retrieve,
            fnc_kwargs={"job_id": job_id},
            conditions={"result": "succeeded"},
            sleep_time=sleep_time,
            max_attempts=max_attempts,
        )

        result = b''
        for blob in job.blobs:
            result += self.api.Jobs.get_blob_data(
                job_id=job.id,
                blob_id=blob.id
            )
        return result


class BearerAuthenticator(Authenticator):
    token_type = "Bearer"
    access_token = None

    def __init__(self, host, access_token=None):
        super().__init__(host)
        self.access_token = access_token

    def apply(self, request):
        if self.access_token:
            request.headers.update({
                "Authorization": "%s %s" % (self.token_type, self.access_token)
            })
        return request


class ApplicationApiSwaggerClient(SwaggerClient):
    system_url = None
    partner_id = None
    partner_secret = None

    @classmethod
    def _clean_spec_dict(cls, spec_dict):
        """
        TODO: should fix the swagger JSON schema on
              server and remove this function

        :param spec_dict:
        :return:
        """

        delete = functools.partial(dpath.util.delete, separator=".")
        get = functools.partial(dpath.util.get, separator=".")
        _new = functools.partial(dpath.util.new, separator=".")
        _set = functools.partial(dpath.util.set, separator=".")

        # TODO
        try:
            for key, parameter in enumerate(spec_dict["paths"]["/objects/{object_id}/navigate"]["get"]["parameters"]):
                if parameter["name"] == 'locale':
                    parameter["schema"] = {"ref": parameter['$ref']}
                    del parameter['$ref']
        except:
            # route can't be present in external swagger schema
            pass

        for path in spec_dict["paths"]:
            for method in spec_dict["paths"][path]:
                for i, v in enumerate(
                    spec_dict["paths"][path][method]["parameters"]
                ):
                    if (
                            v.get("required") and
                            v.get("type") == "object" and
                            v.get('in') == "formData"
                    ):
                        del spec_dict["paths"][path][method]["parameters"][i][
                            "required"
                        ]

        path = (
            "/accounts/{account_id}/datasets/{dataset_id}/"
            "variables/{variable_code}/external-identity"
        )
        try:
            response = get(spec_dict,  f"paths.{path}.put.responses.201")
            _set(
                spec_dict,
                f"paths.{path}.put.responses",
                {"200": response, "201": response}
            )
        except:
            pass

    @classmethod
    def from_url(
        cls,
        spec_url,
        client_id,
        client_secret,
        http_client=None,
        request_headers=None,
        config=None,
        ssl_verify=True,
    ):
        """Generate the client from an OpenAPI v.2.0 specification that should
        be synchronously downloaded.

        :param spec_url: The URL pointing at the URL where the OpenAPI v.2.0
          (Swagger) specification resides. Defaults to :obj:`None <python:None>`
        :type spec_url: :class:`str <python:str>` / :obj:`None <python:None>`

        :param client_id: ?????

        :param client_secret: ?????

        :param http_client: The HTTP client to use for requests. Defaults to
          :obj:`None <python:None>`

        :param request_headers: :class:`dict <python:dict>` of HTTP headers to
          supply when requesting the OpenAPI v.2.0 (Swagger) specification.
          Defaults to :obj:`None <python:None>`
        :type request_headers: :class:`dict <python:dict>` /
          :obj:`None <python:None>`

        :param config: :class:`dict <python:dict>` with custom configuration options.
          Defaults to :obj:`None <python:None>`
        :type config: :class:`dict <python:dict>` / :obj:`None <python:None>`

        :returns: A :class:`ApplicationApiSwaggerClient` instance.
        :rtype: :class:`ApplicationApiSwaggerClient`
        """

        http_client = http_client or MsRequestsClient()
        loader = Loader(http_client, request_headers=request_headers)
        spec_dict = loader.load_spec(spec_url)
        if request_headers is not None:
            http_client.request = inject_headers_for_remote_refs(
                http_client.request, request_headers
            )

        return cls.from_spec(
            spec_dict, client_id, client_secret, spec_url, http_client, config
        )

    @classmethod
    def from_spec(
        cls,
        api_url,
        api_swagger_url = None,
        spec_dict = None,
        http_client = None,
        config = None,
        origin_url = None,
        authenticator_class: Authenticator = BearerAuthenticator,
        ssl_verify = True,
    ):
        """Build a :class:`ApplicationApiSwaggerClient` from an OpenAPI v.2.0 (Swagger)
        specification.

        :param api_url: The URL pointing at the actual API.
        :type api_url: :class:`str <python:str>`

        :param api_swagger_url: The URL pointing at the URL where the OpenAPI v.2.0
          (Swagger) specification resides. Defaults to :obj:`None <python:None>`
        :type api_swagger_url: :class:`str <python:str>` / :obj:`None <python:None>`

        :param spec_dict: a :class:`dict <python:dict>` containing the OpenAPI v.2.0
          (Swagger) specification as a JSON-like object. Defaults to
          :obj:`None <python:None>`
        :type spec_dict: :class:`dict <python:dict>` / :obj:`None <python:None>`

        :param http_client: The HTTP client to use for requests. Defaults to
          :obj:`None <python:None>`

        :param config: :class:`dict <python:dict>` with custom configuration options.
          Defaults to :obj:`None <python:None>`
        :type config: :class:`dict <python:dict>` / :obj:`None <python:None>`

        :param origin_url: The URL pointing at the URL where the OpenAPI v.2.0
          (Swagger) specification resides. Defaults to :obj:`None <python:None>`
        :type origin_url: :class:`str <python:str>` / :obj:`None <python:None>`

        .. todo::

          What is the difference between ``api_swagger_url`` and why are they both
          needed here if only ``origin_url`` is used?

        :returns: A :class:`ApplicationApiSwaggerClient` instance.
        :rtype: :class:`ApplicationApiSwaggerClient`

        """
        _parse = urlparse(api_url)
        spec_dict["schemes"] = [_parse.scheme]
        spec_dict["host"] = _parse.netloc
        spec_dict["basePath"] = _parse.path.rstrip("/")

        http_client = http_client or MsRequestsClient(ssl_verify=ssl_verify)
        config = config or dict(
            validate_responses=False,
            validate_requests=False,
            validate_swagger_spec=False,
            formats=[
                SwaggerFormat(
                    format="email",
                    description="Email format",
                    to_python=lambda x: x,
                    to_wire=lambda x: x,
                    validate=lambda x: x,
                ),
                SwaggerFormat(
                    format="uri",
                    description="Uri format",
                    to_python=lambda x: x,
                    to_wire=lambda x: x,
                    validate=lambda x: x,
                ),
                SwaggerFormat(
                    format="date-time",
                    description="Uri format",
                    to_python=parser.parse,
                    to_wire=lambda x: x.strftime("%Y-%m-%d %H:%M:%S"),
                    validate=lambda x: x,
                ),
            ],
        )

        bravado_config = bravado_config_from_config_dict(config)
        for key in set(bravado_config._fields).intersection(set(config)):
            del config[key]
        config["bravado"] = bravado_config

        # TODO REMVOVE _clean_spec_dict
        try:
            cls._clean_spec_dict(spec_dict)
        except:
            pass

        swagger_spec = Spec.from_dict(
            spec_dict, origin_url, http_client, config
        )

        _client = cls(
            swagger_spec,
            also_return_response=bravado_config.also_return_response,
        )

        _client.swagger_spec.http_client.authenticator = authenticator_class(
            host=spec_dict["host"], access_token=None
        )

        return _client


class Resource(object):
    _swagger_client = None
    _mapping_schema = None
    _class_name = None
    _api = None

    def __new__(cls, **kwargs):
        try:
            resource, operation = cls._mapping_schema["methods"][
                "create"
            ].split(".")
        except:
            raise ms_exp.MarketSightError("No 'create' endpoint")

        callable_o = getattr(getattr(cls._swagger_client, resource), operation)
        instance_class_name = None
        for param_spec in callable_o.operation.op_spec["parameters"]:
            if param_spec.get("name") == "model" and param_spec.get("schema"):
                instance_class_name = (
                    param_spec["schema"]["$ref"].split("/").pop()
                )
        if instance_class_name:
            properties = cls._swagger_client.swagger_spec.spec_dict[
                "definitions"
            ][instance_class_name]["properties"]
            for field_name, prop_schema in properties.items():
                if "$ref" in prop_schema:
                    property_class_name = prop_schema["$ref"].split("/").pop()
                    property_class = cls._swagger_client.get_model(
                        property_class_name
                    )
                    kwargs[field_name] = property_class(
                        **kwargs.get(field_name, {})
                    )

        return type(
            cls._class_name,
            (cls._swagger_client.get_model(instance_class_name),),
            {},
        )(**kwargs)

    @classmethod
    def __dir__(cls):
        return [x for x in cls._api._schema[cls.__name__]["methods"].keys()]


def conv2dict(obj):
    if issubclass(type(obj), Model):
        return {
            attr: conv2dict(getattr(obj, attr))
            for attr in obj
            if getattr(obj, attr) and conv2dict(getattr(obj, attr))
        }
    else:
        return obj


class ObjectFactory:
    def __init__(self, api):
        self._api = api

    def __getattr__(self, item):
        try:
            return self._api._swagger_client.swagger_spec.definitions[item]
        except KeyError:
            raise('No schema for {item}')

    def __dir__(self):
        return self._api._swagger_client.swagger_spec.definitions.keys()


class ApplicationAPI(object):
    """The **MarketSight API Client** primary API object."""

    _latest_response = None
    _swagger_client = None
    client_id = None
    _helper = None
    _method_alias = {
        "Partners": {
            "partners_partner_id": "retrieve"
        }
    }

    _schema = {}

    def _create_options_alias(self, resource_name, operation_id):

        loc_resource_name = resource_name
        result = []
        ident = (operation_id.split("_", 1) + [operation_id])[1]
        matches = re.finditer(
            ".+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)", ident
        )
        res = [m.group(0) for m in matches]

        if res.__len__() == 3:
            if (
                res[0] in ("Post", "Delete", "Get", "Put", "Patch")
                and res[1] + "_" + res[2] == resource_name[:-1]
            ) or (res[0] == "Get" and res[1] + "_" + res[2] == resource_name):
                res = [res[0], res[1] + "_" + res[2]]

        if res[0] == "Post":
            if res.__len__() == 2 and res[1] == resource_name[:-1]:
                result.append("create")
            else:
                result = res

        elif res[0] == "Delete":
            if res.__len__() == 2 and res[1] == resource_name[:-1]:
                result.append("delete")
            else:
                result = res

        elif res[0] == "Get":
            if res.__len__() == 2 and res[1] == resource_name[:-1]:
                result.append("retrieve")
            elif res.__len__() == 2 and res[1] == resource_name:
                result.append("list")
            else:
                result = res

        elif res[0] == "Put":
            if res.__len__() == 2 and res[1] == resource_name[:-1]:
                result.append("create_or_modify")
            else:
                result = res
        elif res[0] == "Patch":
            if res.__len__() == 2 and res[1] == resource_name[:-1]:
                result.append("modify")
            else:
                result = res
        else:
            result = res

        # remove `resource_name` from the method.
        # api.Charts.export_chart will be just `api.Charts.export`
        if resource_name == "Data_Views":
            try:
                if result[1] == "Data" and result[2] == "View":
                    result = [result[0]] + result[3:]
            except:
                pass
        result = list(filter(lambda x: x != resource_name[:-1], result))

        result = map(lambda x: x.lower(), result)
        return loc_resource_name, "_".join(result)

    def _create_operations_aliases(self):
        result = {}
        for (
            resource_name,
            resource,
        ) in self._swagger_client.swagger_spec.resources.items():
            for operation_id in resource.operations:
                (
                    local_resource_name,
                    local_operation_id,
                ) = self._create_options_alias(resource_name, operation_id)
                if not result.get(local_resource_name):
                    result[local_resource_name] = {"methods": {}}

                local_operation_id = self._method_alias.get(
                    local_resource_name, {}
                ).get(local_operation_id, local_operation_id)

                result[local_resource_name]["methods"][
                    local_operation_id
                ] = "{}.{}".format(resource_name, operation_id)
        return result

    def __init__(
        self,
        api_url,
        spec_dict = None,
        http_client = None,
        config = None,
        method_alias = {},
        helper = None,
        authenticator_class: Authenticator = BearerAuthenticator,
        ssl_verify = True
    ):

        """Instantiate an ``ApplicationAPI`` object to interact with the Dynata
        Reporting & Analytics API.

        :param api_url: The API URL that will be called to interact with the Dynata
          Reporting & Analytics API. Defaults to
          ``'https://application.marketsight.com/api/v1/'``.
        :type api_url: :class:`str <python:str>`

        :param spec_dict: a :class:`dict <python:dict>` containing the OpenAPI v.2.0
          (Swagger) specification as a JSON-like object. Defaults to
          :obj:`None <python:None>`
        :type spec_dict: :class:`dict <python:dict>` / :obj:`None <python:None>`

        :param http_client: The HTTP client to use for requests. Defaults to
          :obj:`None <python:None>`

        :param config: :class:`dict <python:dict>` with custom configuration options.
          Defaults to :obj:`None <python:None>`
        :type config: :class:`dict <python:dict>` / :obj:`None <python:None>`

        :param method_alias: A dictionary providing default aliasing for methods.
          Defaults to :obj:`None <python:None>`
        :type method_alias: :class:`dict <python:dict>` / :obj:`None <python:None>`

        :param helper: A helper class or instance that is used to facilitate
          delayed requests and asynchronous :term:`Jobs <Job>`. Defaults to
          :obj:`None <python:None>`
        :type helper: :class:`Helper <marketsight.application_api.Helper>`
          instance or subclass / :obj:`None <python:None>`

        :returns: A **MarketSight API Client** instance
        :rtype: :class:`ApplicationAPI <marketsight.application_api.ApplicationAPI>`

        :raises validator_collection.errors.InvalidURLError: if ``api_url`` is not a valid URL
        :raises validator_collection.errors.EmptyValueError: if ``api_url`` or ``version``
          are empty
        :raises validator_collection.errors.CannotCoerceError: if ``spec_dict``,
          ``method_alias``, or ``config`` are not empty and cannot be coerced to
          a :class:`dict <python:dict>`
        :raises HelperError: if ``helper`` is not a
          :class:`Helper <marketsight.application_api.Helper>` instance, subclass,
          or :obj:`None <python:None>`

        """
        api_url = validators.url(api_url, allow_empty = False)
        spec_dict = validators.dict(spec_dict, allow_empty = True)
        config = validators.dict(config, allow_empty = True)
        method_alias = validators.dict(method_alias, allow_empty = True)

        if helper and not inspect.isclass(helper) and not checkers.is_type(helper, 'Helper'):
            raise ms_exp.HelperError(
                'helper must be a class object, or a Helper instance, but was an '
                'instance of %s' % helper.__class__.__name__
            )

        self._swagger_client = ApplicationApiSwaggerClient.from_spec(
            api_url = api_url,
            spec_dict = spec_dict,
            http_client = http_client,
            config = config,
            authenticator_class = authenticator_class,
            ssl_verify = ssl_verify,
        )

        if method_alias:
            self._method_alias.update(**method_alias)

        self._schema = self._create_operations_aliases()

        self.helper = helper

        self._definitions = ObjectFactory(self)

    def connect(self,
                client_id = None,  # partner's id
                client_secret = None,  # partner's secret
                token = None,  # or token,
                _sa_token = None):
        """Authorize the instance against the MarketSight API.

        :param client_id: The Partner ID that you were supplied to authenticate
          against the API. Defaults to :obj:`None <python:None>`
        :type client_id: :class:`str <python:str>` / :obj:`None <python:None>`

        :param client_secret: The Partner Secret that you were supplied to
          authenticate against the API. Defaults to :obj:`None <python:None>`
        :type client_secret: :class:`str <python:str>` / :obj:`None <python:None>`

        :param token: An access token to connect with. Defaults to
          :obj:`None <python:None>`
        :type token: :class:`str <python:str>` / :obj:`None <python:None>`

        :raises ValueError: if ``client_id``/``client_secret`` and ``token`` are
          all empty

        """
        if not any([all([client_id, client_secret]), token, _sa_token]):
            raise ValueError('must supply either a client_id/client_secret '
                             'combination or a token')

        if any([client_id, client_secret, token]):
            if token:
                self.access_token = token
            elif all([client_id, client_secret]):
                _token = self.OAuth.token(
                    grant_type = "client_credentials",
                    client_id = client_id,
                    client_secret = client_secret,
                )

                self.access_token = _token.access_token

            else:
                raise ValueError(
                    "client_id and client_secret cannot both be empty"
                )

        elif _sa_token:
            self.access_token = ""

            sd = self._swagger_client.swagger_spec.spec_dict
            referer = f"{sd['schemes'][0]}://{sd['host']}{sd['basePath']}"

            session = self._swagger_client.swagger_spec.http_client.session
            session.cookies = cookiejar_from_dict(
                dict(MarketSightAuth=_sa_token)
            )
            session.headers = {"Referer": referer}

    @classmethod
    def from_url(cls,
                 url,
                 client_id,
                 client_secret,
                 method_alias = None):
        """Instantiate an
        :class:`ApplicationAPI <marketsight.application_api.ApplicationAPI>`
        object to interact with the Dynata Reporting & Analytics API based on a
        remote OpenAPI v.2.0 (Swagger) specification.

        :param url: The URL where the OpenAPI v.2.0 (Swagger) specification
          resides. Defaults to :obj:`None <python:None>`
        :type url: :class:`str <python:str>` / :obj:`None <python:None>`

        :param client_id: The Partner ID that you were supplied to authenticate
          against the API. Defaults to :obj:`None <python:None>`
        :type client_id: :class:`str <python:str>` / :obj:`None <python:None>`

        :param client_secret: The Partner Secret that you were supplied to
          authenticate against the API. Defaults to :obj:`None <python:None>`
        :type client_secret: :class:`str <python:str>` / :obj:`None <python:None>`

        :param method_alias: A dictionary providing default aliasing for methods.
          Defaults to :obj:`None <python:None>`
        :type method_alias: :class:`dict <python:dict>` / :obj:`None <python:None>`

        :returns: A **MarketSight API Client** instance
        :rtype: :class:`ApplicationAPI <marketsight.application_api.ApplicationAPI>`

        :raises validator_collection.errors.InvalidURLError: if ``url`` is not a valid URL
        :raises marketsight.exceptions.MarketSightError: if unable to retrieve
          the OpenAPI specification from ``url``

        """
        url = validators.url(url, allow_empty = False)

        response = requests.get(url)

        if response.status_code == 200:
            return cls(response.json(), client_id, client_secret, method_alias)

        raise ms_exp.MarketSightError('Unable to retrieve the OpenAPI '
                                      'Specification from "{}"'.format(url))

    @property
    def models(self):
        return self._definitions

    def __getattr__(self, item):
        try:
            schema = self._schema[item]
        except KeyError:
            raise ValueError("Resource `{}` doesn't exist".format(item))
        _bases = [Resource]

        def _create_class_method(method_name):
            def _class_method(cls, *argv, **kwargs):
                method_name = _class_method.__name__
                if method_name in cls._mapping_schema["methods"]:
                    swagger_resource, swagget_operation = cls._mapping_schema[
                        "methods"
                    ][method_name].split(".")
                    callable_operation = getattr(
                        getattr(cls._swagger_client, swagger_resource),
                        swagget_operation,
                    )
                    if argv:
                        kwargs.update(
                            zip(
                                tuple(
                                    [
                                        k
                                        for k, v in callable_operation.operation.params.items()
                                        if v.location
                                        in ["path", "body", "formData"]
                                    ]
                                ),
                                argv,
                            )
                        )
                    # fill kwargs with the not empty default value
                    for k, v in callable_operation.operation.params.items():
                        if (
                            hasattr(v, "default")
                            and v.default
                            and k not in kwargs
                        ):
                            kwargs.update({k: v.default})
                        if k.endswith("_id") and k not in kwargs:
                            kwargs.update({k: "-"})

                    for key, value in kwargs.copy().items():
                        kwargs[key] = conv2dict(value)

                    if hasattr(callable_operation.operation, 'produces'):
                        produces = callable_operation.operation.produces
                    else:
                        produces = []

                    _request_options = kwargs.get("_request_options", {})
                    _custom_headers = _request_options.get("headers", {})
                    _custom_headers = {
                        idx.lower(): value.lower()
                        for idx, value in _custom_headers.items()
                    }

                    if _custom_headers.get("accept") and \
                       _custom_headers.get("accept") not in \
                            list(map(lambda x: x.lower(), produces)):
                        raise ValueError(
                            f'headers.accept value can be one of {produces}'
                        )

                    if produces and "accept" not in _custom_headers:
                        _custom_headers["accept"] = produces[0]

                    kwargs["_request_options"] = _request_options
                    kwargs["_request_options"]["headers"] = _custom_headers

                    response = callable_operation(**kwargs).response()

                    self._latest_response = response.incoming_response
                    return response.result

            _class_method.__name__ = method_name
            return copy.deepcopy(_class_method)

        _initial_data = {
            "_swagger_client": self._swagger_client,
            "_mapping_schema": schema,
            "_class_name": item,
            "_api": self,
        }
        for method in schema["methods"]:
            _initial_data.update(
                {method: classmethod(_create_class_method(method))}
            )
        return type(item, tuple(_bases), _initial_data)

    @property
    def access_token(self):
        """The access token that was authorized for the API instance.

        :rtype: :class:`str <python:str>` / :obj:`None <python:None>`
        """
        return (
            self._swagger_client.swagger_spec.http_client.authenticator.access_token
        )

    @access_token.setter
    def access_token(self, value):
        self._swagger_client.swagger_spec.http_client.authenticator.access_token = (
            value
        )

    def __dir__(self):
        return self._schema.keys()

    def connect_as_system_administrator(self, referrer, marketsight_sa_cookie):
        """Establish a connection as a MarketSight :term:`System Administrator`.

        .. note::

          This is a helper-function for Dynata staff who may be executing
          Python scripts locally leveraging the MarketSight API Client. This
          function relies on a cookie in the runtime environment that is
          authenticated as a valid System Administrator in the platform, and
          then inherits that authentication and authorization for the purposes
          of initializing the MarketSight API Client.

        :param referrer: The value to use as the ``Referrer`` header in the
          session.
        :type referrer: :class:`str <python:str>`

        :param marketsight_sa_cookie: The MarketSight System Administrator
          cookie that exists locally in the MarketSight API Client's runtime
          environment.

        """
        self.access_token = ""

        session = self._swagger_client.swagger_spec.http_client.session
        session.cookies = cookiejar_from_dict(
            dict(MarketSightAuth = marketsight_sa_cookie)
        )

        session.headers = {
            "Referrer": referrer,
            "Content-Type": "application/json; charset=utf-8",
        }

        return self

    def inspect_resources(self):
        """Retrieve a map of the :term:`resources <Resource>` exposed by the
        **Dynata Reporting & Analytics API** and their corresponding methods
        supported by the **MarketSight Core**.

        :returns: :class:`dict <python:dict>` where keys are resources exposed
          by the API instance, and values are a list of methods exposed by each
          resource
        :rtype: :class:`dict <python:dict>` with keys as :class:`str <python:str>`
          and values as :class:`list <python:list>` of :class:`str <python:str>`

        """
        output = {}

        for resource in self.__dir__():
            output[resource] = [x for x in getattr(self, resource).__dir__()]

        return output

    @property
    def helper(self):
        """An instance of a :class:`Helper <marketsight.application_api.Helper>`
        class that can be used to facilitate asynchronous :term:`Jobs <Job>`.

        .. seealso::

          * :doc:`API Reference <api>`: :class:`Helper <marketsight.application_api.Helper>` objects
          * :doc:`Using the MarketSight API Client <using>`: :ref:`Asynchronous Jobs <long_running_jobs>`
          * :doc:`Using the MarketSight API Client <using>`: :ref:`Working with Helpers <working_with_helpers>`

        :rtype: :class:`Helper <marketsight.application_api.Helper>`

        :raises marketsight.exceptions.HelperError: if a value is supplied that
        is neither a :class:`Helper <marketsight.application_api.Helper>` instance,
        subclass, or :obj:`None <python:None>`

        """
        return self._helper

    @helper.setter
    def helper(self, value):
        if not value:
            value = Helper

        if value and not inspect.isclass(value) and not checkers.is_type(value, 'Helper'):
            raise ms_exp.HelperError(
                'helper must be a class object, or a Helper instance, but was an '
                'instance of %s' % value.__class__.__name__
            )
        elif value and inspect.isclass(value):
            helper_class = value
            self._helper = helper_class(self)
        elif value:
            self._helper = value


def client(
    openapi_url=OPENAPI_URL,
    openapi_dict=None,
    ssl_verify=True,
    helper=None,
) -> ApplicationAPI:
    """
    Factory function that is used to initialize an instance of the
    **MarketSight API Client**.

    :param openapi_url: The URL which the OpenAPI Specification file can be
      downloaded. Defaults to :obj:`None <python:None>`
    :type openapi_url: :class:`str <python:str>` / :obj:`None <python:None>`

    :param openapi_dict: The :class:`dict <python:dict>` representation of an
      OpenAPI Specification. Defaults to :obj:`None <python:None>`.
    :type openapi_dict: :class:`dict <python:dict>` / :obj:`None <python:None>`

    :param ssl_verify: If ``True``, will verify the SSL Certificate when calling
      the ``openapi_url`` to download the OpenAPI Specification. Defaults to
      ``True``.
    :type ssl_verify: :class:`bool <python:bool>`

    :param helper: A :class:`Helper` instance to use when asynchronously
      downloading blob data. Defaults to :obj:`None <python:None>`
    :type helper: :class:`Helper` / :obj:`None <python:None>`

    :returns: An initialized instance of the **MarketSight API Client**.
    :rtype: :class:`ApplicationAPI`

    :raises ValueError: if ``api_url``, ``openapi_url``, and ``openapi_dict``
      are all empty
    :raises validator_collection.errors.InvalidURLError: if ``api_url`` or
      ``openapi_url`` are invalid URLs.

    :example:

      .. code-block:: python
         :linenos:

         import marketsight

         api = marketsight.client()
    """
    spec_dict = None
    cache_dir = pathlib.Path() / '.marketsight'

    if openapi_url is None:
        openapi_url = OPENAPI_URL

    if openapi_dict:
        spec_dict = openapi_dict

    if spec_dict is None:
        cache_dir.mkdir(exist_ok=True)
        openapi_url = validators.url(openapi_url, allow_empty = False)
        response = requests.head(
            url=openapi_url,
            verify=ssl_verify
        )
        chunk = (
                openapi_url +
                response.headers.pop('Content-Length', '')
        ).encode()

        cache_file = cache_dir / ("%s.json" % hashlib.sha256(chunk).hexdigest())

        if cache_file.exists():
            spec_dict = json.load(cache_file.open('r'))
        else:
            response = requests.get(openapi_url, verify = ssl_verify)
            spec_dict = response.json()
            json.dump(spec_dict, cache_file.open('w'))

    if "schemes" not in spec_dict:
        _parse = urlparse(openapi_url)
        spec_dict["schemes"] = [_parse.scheme]
        spec_dict["host"] = _parse.netloc

    schema = spec_dict["schemes"][0]
    api_url = f"{schema}://{spec_dict['host']}{spec_dict.get('basePath', '')}"

    return ApplicationAPI(
        api_url = api_url,
        spec_dict = spec_dict,
        ssl_verify = ssl_verify,
        helper = helper,
    )
