"""
Type annotations for marketplacecommerceanalytics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_marketplacecommerceanalytics.type_defs import GenerateDataSetRequestTypeDef

    data: GenerateDataSetRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, Union

from .literals import DataSetTypeType, SupportDataSetTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "GenerateDataSetRequestTypeDef",
    "GenerateDataSetResultResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartSupportDataExportRequestTypeDef",
    "StartSupportDataExportResultResponseTypeDef",
)

_RequiredGenerateDataSetRequestTypeDef = TypedDict(
    "_RequiredGenerateDataSetRequestTypeDef",
    {
        "dataSetType": DataSetTypeType,
        "dataSetPublicationDate": Union[datetime, str],
        "roleNameArn": str,
        "destinationS3BucketName": str,
        "snsTopicArn": str,
    },
)
_OptionalGenerateDataSetRequestTypeDef = TypedDict(
    "_OptionalGenerateDataSetRequestTypeDef",
    {
        "destinationS3Prefix": str,
        "customerDefinedValues": Dict[str, str],
    },
    total=False,
)


class GenerateDataSetRequestTypeDef(
    _RequiredGenerateDataSetRequestTypeDef, _OptionalGenerateDataSetRequestTypeDef
):
    pass


GenerateDataSetResultResponseTypeDef = TypedDict(
    "GenerateDataSetResultResponseTypeDef",
    {
        "dataSetRequestId": str,
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

_RequiredStartSupportDataExportRequestTypeDef = TypedDict(
    "_RequiredStartSupportDataExportRequestTypeDef",
    {
        "dataSetType": SupportDataSetTypeType,
        "fromDate": Union[datetime, str],
        "roleNameArn": str,
        "destinationS3BucketName": str,
        "snsTopicArn": str,
    },
)
_OptionalStartSupportDataExportRequestTypeDef = TypedDict(
    "_OptionalStartSupportDataExportRequestTypeDef",
    {
        "destinationS3Prefix": str,
        "customerDefinedValues": Dict[str, str],
    },
    total=False,
)


class StartSupportDataExportRequestTypeDef(
    _RequiredStartSupportDataExportRequestTypeDef, _OptionalStartSupportDataExportRequestTypeDef
):
    pass


StartSupportDataExportResultResponseTypeDef = TypedDict(
    "StartSupportDataExportResultResponseTypeDef",
    {
        "dataSetRequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
