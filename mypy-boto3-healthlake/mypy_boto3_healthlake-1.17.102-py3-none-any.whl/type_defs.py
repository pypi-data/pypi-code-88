"""
Type annotations for healthlake service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/type_defs.html)

Usage::

    ```python
    from mypy_boto3_healthlake.type_defs import CreateFHIRDatastoreRequestTypeDef

    data: CreateFHIRDatastoreRequestTypeDef = {...}
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
    "CreateFHIRDatastoreRequestTypeDef",
    "CreateFHIRDatastoreResponseResponseTypeDef",
    "DatastoreFilterTypeDef",
    "DatastorePropertiesTypeDef",
    "DeleteFHIRDatastoreRequestTypeDef",
    "DeleteFHIRDatastoreResponseResponseTypeDef",
    "DescribeFHIRDatastoreRequestTypeDef",
    "DescribeFHIRDatastoreResponseResponseTypeDef",
    "DescribeFHIRExportJobRequestTypeDef",
    "DescribeFHIRExportJobResponseResponseTypeDef",
    "DescribeFHIRImportJobRequestTypeDef",
    "DescribeFHIRImportJobResponseResponseTypeDef",
    "ExportJobPropertiesTypeDef",
    "ImportJobPropertiesTypeDef",
    "InputDataConfigTypeDef",
    "ListFHIRDatastoresRequestTypeDef",
    "ListFHIRDatastoresResponseResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PreloadDataConfigTypeDef",
    "ResponseMetadataTypeDef",
    "StartFHIRExportJobRequestTypeDef",
    "StartFHIRExportJobResponseResponseTypeDef",
    "StartFHIRImportJobRequestTypeDef",
    "StartFHIRImportJobResponseResponseTypeDef",
)

_RequiredCreateFHIRDatastoreRequestTypeDef = TypedDict(
    "_RequiredCreateFHIRDatastoreRequestTypeDef",
    {
        "DatastoreTypeVersion": Literal["R4"],
    },
)
_OptionalCreateFHIRDatastoreRequestTypeDef = TypedDict(
    "_OptionalCreateFHIRDatastoreRequestTypeDef",
    {
        "DatastoreName": str,
        "PreloadDataConfig": "PreloadDataConfigTypeDef",
        "ClientToken": str,
    },
    total=False,
)


class CreateFHIRDatastoreRequestTypeDef(
    _RequiredCreateFHIRDatastoreRequestTypeDef, _OptionalCreateFHIRDatastoreRequestTypeDef
):
    pass


CreateFHIRDatastoreResponseResponseTypeDef = TypedDict(
    "CreateFHIRDatastoreResponseResponseTypeDef",
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


DeleteFHIRDatastoreRequestTypeDef = TypedDict(
    "DeleteFHIRDatastoreRequestTypeDef",
    {
        "DatastoreId": str,
    },
    total=False,
)

DeleteFHIRDatastoreResponseResponseTypeDef = TypedDict(
    "DeleteFHIRDatastoreResponseResponseTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": DatastoreStatusType,
        "DatastoreEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFHIRDatastoreRequestTypeDef = TypedDict(
    "DescribeFHIRDatastoreRequestTypeDef",
    {
        "DatastoreId": str,
    },
    total=False,
)

DescribeFHIRDatastoreResponseResponseTypeDef = TypedDict(
    "DescribeFHIRDatastoreResponseResponseTypeDef",
    {
        "DatastoreProperties": "DatastorePropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFHIRExportJobRequestTypeDef = TypedDict(
    "DescribeFHIRExportJobRequestTypeDef",
    {
        "DatastoreId": str,
        "JobId": str,
    },
)

DescribeFHIRExportJobResponseResponseTypeDef = TypedDict(
    "DescribeFHIRExportJobResponseResponseTypeDef",
    {
        "ExportJobProperties": "ExportJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFHIRImportJobRequestTypeDef = TypedDict(
    "DescribeFHIRImportJobRequestTypeDef",
    {
        "DatastoreId": str,
        "JobId": str,
    },
)

DescribeFHIRImportJobResponseResponseTypeDef = TypedDict(
    "DescribeFHIRImportJobResponseResponseTypeDef",
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

ListFHIRDatastoresRequestTypeDef = TypedDict(
    "ListFHIRDatastoresRequestTypeDef",
    {
        "Filter": "DatastoreFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListFHIRDatastoresResponseResponseTypeDef = TypedDict(
    "ListFHIRDatastoresResponseResponseTypeDef",
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

_RequiredStartFHIRExportJobRequestTypeDef = TypedDict(
    "_RequiredStartFHIRExportJobRequestTypeDef",
    {
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DatastoreId": str,
        "DataAccessRoleArn": str,
        "ClientToken": str,
    },
)
_OptionalStartFHIRExportJobRequestTypeDef = TypedDict(
    "_OptionalStartFHIRExportJobRequestTypeDef",
    {
        "JobName": str,
    },
    total=False,
)


class StartFHIRExportJobRequestTypeDef(
    _RequiredStartFHIRExportJobRequestTypeDef, _OptionalStartFHIRExportJobRequestTypeDef
):
    pass


StartFHIRExportJobResponseResponseTypeDef = TypedDict(
    "StartFHIRExportJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "DatastoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartFHIRImportJobRequestTypeDef = TypedDict(
    "_RequiredStartFHIRImportJobRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "DatastoreId": str,
        "DataAccessRoleArn": str,
        "ClientToken": str,
    },
)
_OptionalStartFHIRImportJobRequestTypeDef = TypedDict(
    "_OptionalStartFHIRImportJobRequestTypeDef",
    {
        "JobName": str,
    },
    total=False,
)


class StartFHIRImportJobRequestTypeDef(
    _RequiredStartFHIRImportJobRequestTypeDef, _OptionalStartFHIRImportJobRequestTypeDef
):
    pass


StartFHIRImportJobResponseResponseTypeDef = TypedDict(
    "StartFHIRImportJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "DatastoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
