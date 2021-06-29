"""
Type annotations for healthlake service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_healthlake import HealthLakeClient

    client: HealthLakeClient = boto3.client("healthlake")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from .type_defs import (
    CreateFHIRDatastoreResponseTypeDef,
    DatastoreFilterTypeDef,
    DeleteFHIRDatastoreResponseTypeDef,
    DescribeFHIRDatastoreResponseTypeDef,
    DescribeFHIRExportJobResponseTypeDef,
    DescribeFHIRImportJobResponseTypeDef,
    InputDataConfigTypeDef,
    ListFHIRDatastoresResponseTypeDef,
    OutputDataConfigTypeDef,
    PreloadDataConfigTypeDef,
    StartFHIRExportJobResponseTypeDef,
    StartFHIRImportJobResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("HealthLakeClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class HealthLakeClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/healthlake.html#HealthLake.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/healthlake.html#HealthLake.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#can_paginate)
        """

    def create_fhir_datastore(
        self,
        *,
        DatastoreTypeVersion: Literal["R4"],
        DatastoreName: str = None,
        PreloadDataConfig: "PreloadDataConfigTypeDef" = None,
        ClientToken: str = None
    ) -> CreateFHIRDatastoreResponseTypeDef:
        """
        Creates a Data Store that can ingest and export FHIR formatted data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/healthlake.html#HealthLake.Client.create_fhir_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#create_fhir_datastore)
        """

    def delete_fhir_datastore(
        self, *, DatastoreId: str = None
    ) -> DeleteFHIRDatastoreResponseTypeDef:
        """
        Deletes a Data Store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/healthlake.html#HealthLake.Client.delete_fhir_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#delete_fhir_datastore)
        """

    def describe_fhir_datastore(
        self, *, DatastoreId: str = None
    ) -> DescribeFHIRDatastoreResponseTypeDef:
        """
        Gets the properties associated with the FHIR Data Store, including the Data
        Store ID, Data Store ARN, Data Store name, Data Store status, created at, Data
        Store type version, and Data Store endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/healthlake.html#HealthLake.Client.describe_fhir_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#describe_fhir_datastore)
        """

    def describe_fhir_export_job(
        self, *, DatastoreId: str, JobId: str
    ) -> DescribeFHIRExportJobResponseTypeDef:
        """
        Displays the properties of a FHIR export job, including the ID, ARN, name, and
        the status of the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/healthlake.html#HealthLake.Client.describe_fhir_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#describe_fhir_export_job)
        """

    def describe_fhir_import_job(
        self, *, DatastoreId: str, JobId: str
    ) -> DescribeFHIRImportJobResponseTypeDef:
        """
        Displays the properties of a FHIR import job, including the ID, ARN, name, and
        the status of the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/healthlake.html#HealthLake.Client.describe_fhir_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#describe_fhir_import_job)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/healthlake.html#HealthLake.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#generate_presigned_url)
        """

    def list_fhir_datastores(
        self,
        *,
        Filter: "DatastoreFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListFHIRDatastoresResponseTypeDef:
        """
        Lists all FHIR Data Stores that are in the user’s account, regardless of Data
        Store status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/healthlake.html#HealthLake.Client.list_fhir_datastores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#list_fhir_datastores)
        """

    def start_fhir_export_job(
        self,
        *,
        OutputDataConfig: "OutputDataConfigTypeDef",
        DatastoreId: str,
        DataAccessRoleArn: str,
        ClientToken: str,
        JobName: str = None
    ) -> StartFHIRExportJobResponseTypeDef:
        """
        Begins a FHIR export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/healthlake.html#HealthLake.Client.start_fhir_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#start_fhir_export_job)
        """

    def start_fhir_import_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        DatastoreId: str,
        DataAccessRoleArn: str,
        ClientToken: str,
        JobName: str = None
    ) -> StartFHIRImportJobResponseTypeDef:
        """
        Begins a FHIR Import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/healthlake.html#HealthLake.Client.start_fhir_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/client.html#start_fhir_import_job)
        """
