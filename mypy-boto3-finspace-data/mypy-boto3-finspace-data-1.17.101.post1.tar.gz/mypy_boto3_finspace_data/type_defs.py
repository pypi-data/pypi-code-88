"""
Type annotations for finspace-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_finspace_data.type_defs import ChangesetInfoTypeDef

    data: ChangesetInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict

from .literals import (
    ChangesetStatusType,
    ChangeTypeType,
    ErrorCategoryType,
    FormatTypeType,
    locationTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ChangesetInfoTypeDef",
    "CreateChangesetRequestTypeDef",
    "CreateChangesetResponseResponseTypeDef",
    "CredentialsTypeDef",
    "ErrorInfoTypeDef",
    "GetProgrammaticAccessCredentialsRequestTypeDef",
    "GetProgrammaticAccessCredentialsResponseResponseTypeDef",
    "GetWorkingLocationRequestTypeDef",
    "GetWorkingLocationResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
)

ChangesetInfoTypeDef = TypedDict(
    "ChangesetInfoTypeDef",
    {
        "id": str,
        "changesetArn": str,
        "datasetId": str,
        "changeType": ChangeTypeType,
        "sourceType": Literal["S3"],
        "sourceParams": Dict[str, str],
        "formatType": FormatTypeType,
        "formatParams": Dict[str, str],
        "createTimestamp": datetime,
        "status": ChangesetStatusType,
        "errorInfo": "ErrorInfoTypeDef",
        "changesetLabels": Dict[str, str],
        "updatesChangesetId": str,
        "updatedByChangesetId": str,
    },
    total=False,
)

_RequiredCreateChangesetRequestTypeDef = TypedDict(
    "_RequiredCreateChangesetRequestTypeDef",
    {
        "datasetId": str,
        "changeType": ChangeTypeType,
        "sourceType": Literal["S3"],
        "sourceParams": Dict[str, str],
    },
)
_OptionalCreateChangesetRequestTypeDef = TypedDict(
    "_OptionalCreateChangesetRequestTypeDef",
    {
        "formatType": FormatTypeType,
        "formatParams": Dict[str, str],
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateChangesetRequestTypeDef(
    _RequiredCreateChangesetRequestTypeDef, _OptionalCreateChangesetRequestTypeDef
):
    pass


CreateChangesetResponseResponseTypeDef = TypedDict(
    "CreateChangesetResponseResponseTypeDef",
    {
        "changeset": "ChangesetInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "accessKeyId": str,
        "secretAccessKey": str,
        "sessionToken": str,
    },
    total=False,
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "errorMessage": str,
        "errorCategory": ErrorCategoryType,
    },
    total=False,
)

_RequiredGetProgrammaticAccessCredentialsRequestTypeDef = TypedDict(
    "_RequiredGetProgrammaticAccessCredentialsRequestTypeDef",
    {
        "environmentId": str,
    },
)
_OptionalGetProgrammaticAccessCredentialsRequestTypeDef = TypedDict(
    "_OptionalGetProgrammaticAccessCredentialsRequestTypeDef",
    {
        "durationInMinutes": int,
    },
    total=False,
)


class GetProgrammaticAccessCredentialsRequestTypeDef(
    _RequiredGetProgrammaticAccessCredentialsRequestTypeDef,
    _OptionalGetProgrammaticAccessCredentialsRequestTypeDef,
):
    pass


GetProgrammaticAccessCredentialsResponseResponseTypeDef = TypedDict(
    "GetProgrammaticAccessCredentialsResponseResponseTypeDef",
    {
        "credentials": "CredentialsTypeDef",
        "durationInMinutes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkingLocationRequestTypeDef = TypedDict(
    "GetWorkingLocationRequestTypeDef",
    {
        "locationType": locationTypeType,
    },
    total=False,
)

GetWorkingLocationResponseResponseTypeDef = TypedDict(
    "GetWorkingLocationResponseResponseTypeDef",
    {
        "s3Uri": str,
        "s3Path": str,
        "s3Bucket": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
