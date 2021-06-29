"""
Type annotations for healthlake service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/type_defs.html)

Usage::

    ```python
    from mypy_boto3_healthlake.type_defs import CreateFHIRDatastoreRequestRequestTypeDef

    data: CreateFHIRDatastoreRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import DatastoreStatusType, JobStatusType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateFHIRDatastoreRequestRequestTypeDef",
    "CreateFHIRDatastoreResponseTypeDef",
    "DatastoreFilterTypeDef",
    "DatastorePropertiesTypeDef",
    "DeleteFHIRDatastoreRequestRequestTypeDef",
    "DeleteFHIRDatastoreResponseTypeDef",
    "DescribeFHIRDatastoreRequestRequestTypeDef",
    "DescribeFHIRDatastoreResponseTypeDef",
    "DescribeFHIRExportJobRequestRequestTypeDef",
    "DescribeFHIRExportJobResponseTypeDef",
    "DescribeFHIRImportJobRequestRequestTypeDef",
    "DescribeFHIRImportJobResponseTypeDef",
    "ExportJobPropertiesTypeDef",
    "ImportJobPropertiesTypeDef",
    "InputDataConfigTypeDef",
    "ListFHIRDatastoresRequestRequestTypeDef",
    "ListFHIRDatastoresResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PreloadDataConfigTypeDef",
    "ResponseMetadataTypeDef",
    "StartFHIRExportJobRequestRequestTypeDef",
    "StartFHIRExportJobResponseTypeDef",
    "StartFHIRImportJobRequestRequestTypeDef",
    "StartFHIRImportJobResponseTypeDef",
)

_RequiredCreateFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreTypeVersion": Literal["R4"],
    },
)
_OptionalCreateFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreName": str,
        "PreloadDataConfig": "PreloadDataConfigTypeDef",
        "ClientToken": str,
    },
    total=False,
)


class CreateFHIRDatastoreRequestRequestTypeDef(
    _RequiredCreateFHIRDatastoreRequestRequestTypeDef,
    _OptionalCreateFHIRDatastoreRequestRequestTypeDef,
):
    pass


CreateFHIRDatastoreResponseTypeDef = TypedDict(
    "CreateFHIRDatastoreResponseTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": DatastoreStatusType,
        "DatastoreEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatastoreFilterTypeDef = TypedDict(
    "DatastoreFilterTypeDef",
    {
        "DatastoreName": str,
        "DatastoreStatus": DatastoreStatusType,
        "CreatedBefore": Union[datetime, str],
        "CreatedAfter": Union[datetime, str],
    },
    total=False,
)

_RequiredDatastorePropertiesTypeDef = TypedDict(
    "_RequiredDatastorePropertiesTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": DatastoreStatusType,
        "DatastoreTypeVersion": Literal["R4"],
        "DatastoreEndpoint": str,
    },
)
_OptionalDatastorePropertiesTypeDef = TypedDict(
    "_OptionalDatastorePropertiesTypeDef",
    {
        "DatastoreName": str,
        "CreatedAt": datetime,
        "PreloadDataConfig": "PreloadDataConfigTypeDef",
    },
    total=False,
)


class DatastorePropertiesTypeDef(
    _RequiredDatastorePropertiesTypeDef, _OptionalDatastorePropertiesTypeDef
):
    pass


DeleteFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "DeleteFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreId": str,
    },
    total=False,
)

DeleteFHIRDatastoreResponseTypeDef = TypedDict(
    "DeleteFHIRDatastoreResponseTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": DatastoreStatusType,
        "DatastoreEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "DescribeFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreId": str,
    },
    total=False,
)

DescribeFHIRDatastoreResponseTypeDef = TypedDict(
    "DescribeFHIRDatastoreResponseTypeDef",
    {
        "DatastoreProperties": "DatastorePropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFHIRExportJobRequestRequestTypeDef = TypedDict(
    "DescribeFHIRExportJobRequestRequestTypeDef",
    {
        "DatastoreId": str,
        "JobId": str,
    },
)

DescribeFHIRExportJobResponseTypeDef = TypedDict(
    "DescribeFHIRExportJobResponseTypeDef",
    {
        "ExportJobProperties": "ExportJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFHIRImportJobRequestRequestTypeDef = TypedDict(
    "DescribeFHIRImportJobRequestRequestTypeDef",
    {
        "DatastoreId": str,
        "JobId": str,
    },
)

DescribeFHIRImportJobResponseTypeDef = TypedDict(
    "DescribeFHIRImportJobResponseTypeDef",
    {
        "ImportJobProperties": "ImportJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportJobPropertiesTypeDef = TypedDict(
    "_RequiredExportJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "SubmitTime": datetime,
        "DatastoreId": str,
        "OutputDataConfig": "OutputDataConfigTypeDef",
    },
)
_OptionalExportJobPropertiesTypeDef = TypedDict(
    "_OptionalExportJobPropertiesTypeDef",
    {
        "JobName": str,
        "EndTime": datetime,
        "DataAccessRoleArn": str,
        "Message": str,
    },
    total=False,
)


class ExportJobPropertiesTypeDef(
    _RequiredExportJobPropertiesTypeDef, _OptionalExportJobPropertiesTypeDef
):
    pass


_RequiredImportJobPropertiesTypeDef = TypedDict(
    "_RequiredImportJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "SubmitTime": datetime,
        "DatastoreId": str,
        "InputDataConfig": "InputDataConfigTypeDef",
    },
)
_OptionalImportJobPropertiesTypeDef = TypedDict(
    "_OptionalImportJobPropertiesTypeDef",
    {
        "JobName": str,
        "EndTime": datetime,
        "DataAccessRoleArn": str,
        "Message": str,
    },
    total=False,
)


class ImportJobPropertiesTypeDef(
    _RequiredImportJobPropertiesTypeDef, _OptionalImportJobPropertiesTypeDef
):
    pass


InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

ListFHIRDatastoresRequestRequestTypeDef = TypedDict(
    "ListFHIRDatastoresRequestRequestTypeDef",
    {
        "Filter": "DatastoreFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListFHIRDatastoresResponseTypeDef = TypedDict(
    "ListFHIRDatastoresResponseTypeDef",
    {
        "DatastorePropertiesList": List["DatastorePropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

PreloadDataConfigTypeDef = TypedDict(
    "PreloadDataConfigTypeDef",
    {
        "PreloadDataType": Literal["SYNTHEA"],
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredStartFHIRExportJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartFHIRExportJobRequestRequestTypeDef",
    {
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DatastoreId": str,
        "DataAccessRoleArn": str,
        "ClientToken": str,
    },
)
_OptionalStartFHIRExportJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartFHIRExportJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
    total=False,
)


class StartFHIRExportJobRequestRequestTypeDef(
    _RequiredStartFHIRExportJobRequestRequestTypeDef,
    _OptionalStartFHIRExportJobRequestRequestTypeDef,
):
    pass


StartFHIRExportJobResponseTypeDef = TypedDict(
    "StartFHIRExportJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "DatastoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartFHIRImportJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartFHIRImportJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "DatastoreId": str,
        "DataAccessRoleArn": str,
        "ClientToken": str,
    },
)
_OptionalStartFHIRImportJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartFHIRImportJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
    total=False,
)


class StartFHIRImportJobRequestRequestTypeDef(
    _RequiredStartFHIRImportJobRequestRequestTypeDef,
    _OptionalStartFHIRImportJobRequestRequestTypeDef,
):
    pass


StartFHIRImportJobResponseTypeDef = TypedDict(
    "StartFHIRImportJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "DatastoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
