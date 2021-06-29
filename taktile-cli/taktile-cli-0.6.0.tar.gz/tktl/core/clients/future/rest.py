import typing as t

from tktl.core.clients.future.http import API
from tktl.core.clients.future.taktile import DeploymentApiClient
from tktl.core.clients.http_client import interpret_response
from tktl.core.exceptions import TaktileSdkError
from tktl.core.schemas.future.service import InfoEndpointResponseModel
from tktl.core.schemas.repository import RepositoryDeployment, _format_http_url

from .endpoint import RestEndpoints


class RestClient:

    endpoints: RestEndpoints

    def __init__(
        self,
        api_key: str,
        repository_name: str,
        branch_name: str,
        url: t.Optional[str] = None,
    ):
        self._api_key = api_key
        self._repository_name = repository_name
        self._branch_name = branch_name
        self._url = RestClient.__get_url(
            url=url,
            repository_name=repository_name,
            branch_name=branch_name,
            api_key=api_key,
        )

        self._client = RestClient.__get_deployment_client(
            url=self._url, api_key=api_key
        )

        self._info = self.__get_info(api_key=api_key, client=self._client)

        self.endpoints = RestEndpoints(api=self._client, infos=self._info.endpoints)

    @staticmethod
    def __get_deployment(
        *, repository_name: str, branch_name: str, client: DeploymentApiClient
    ) -> RepositoryDeployment:
        return client.get_deployment_by_branch_name(
            repository_name=repository_name, branch_name=branch_name
        )

    @staticmethod
    def __get_info(*, api_key: str, client: API) -> InfoEndpointResponseModel:
        response = client.get("/info")
        response.raise_for_status()
        if "schema_version" not in response.json():
            raise TaktileSdkError(
                "Deployment is based on pre v1.0 image, can't use this client"
            )

        return interpret_response(response, InfoEndpointResponseModel)

    @staticmethod
    def __get_dapi_client(*, api_key: str) -> DeploymentApiClient:
        return DeploymentApiClient(api_key=api_key)

    @staticmethod
    def __get_deployment_client(*, url: str, api_key: str) -> API:
        client = API(api_url=url, headers={"X-Api-Key": api_key})

        return client

    @staticmethod
    def __get_url(
        *, url: t.Optional[str], repository_name: str, branch_name: str, api_key: str
    ) -> str:
        if url:
            return url

        client = RestClient.__get_dapi_client(api_key=api_key)
        deployment = RestClient.__get_deployment(
            repository_name=repository_name, branch_name=branch_name, client=client
        )

        return _format_http_url(deployment.public_docs_url, docs=False)
