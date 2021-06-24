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
from typing import Dict

from .literals import ChangesetStatusType, ChangeTypeType, ErrorCategoryType, FormatTypeType

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
    "CreateChangesetResponseTypeDef",
    "CredentialsTypeDef",
    "ErrorInfoTypeDef",
    "GetProgrammaticAccessCredentialsResponseTypeDef",
    "GetWorkingLocationResponseTypeDef",
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

CreateChangesetResponseTypeDef = TypedDict(
    "CreateChangesetResponseTypeDef",
    {
        "changeset": "ChangesetInfoTypeDef",
    },
    total=False,
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

GetProgrammaticAccessCredentialsResponseTypeDef = TypedDict(
    "GetProgrammaticAccessCredentialsResponseTypeDef",
    {
        "credentials": "CredentialsTypeDef",
        "durationInMinutes": int,
    },
    total=False,
)

GetWorkingLocationResponseTypeDef = TypedDict(
    "GetWorkingLocationResponseTypeDef",
    {
        "s3Uri": str,
        "s3Path": str,
        "s3Bucket": str,
    },
    total=False,
)
