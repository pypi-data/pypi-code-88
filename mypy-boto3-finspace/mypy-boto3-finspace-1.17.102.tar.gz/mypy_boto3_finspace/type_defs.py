"""
Type annotations for finspace service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/type_defs.html)

Usage::

    ```python
    from mypy_boto3_finspace.type_defs import CreateEnvironmentRequestTypeDef

    data: CreateEnvironmentRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import EnvironmentStatusType, FederationModeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateEnvironmentRequestTypeDef",
    "CreateEnvironmentResponseResponseTypeDef",
    "DeleteEnvironmentRequestTypeDef",
    "EnvironmentTypeDef",
    "FederationParametersTypeDef",
    "GetEnvironmentRequestTypeDef",
    "GetEnvironmentResponseResponseTypeDef",
    "ListEnvironmentsRequestTypeDef",
    "ListEnvironmentsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateEnvironmentRequestTypeDef",
    "UpdateEnvironmentResponseResponseTypeDef",
)

_RequiredCreateEnvironmentRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateEnvironmentRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentRequestTypeDef",
    {
        "description": str,
        "kmsKeyId": str,
        "tags": Dict[str, str],
        "federationMode": FederationModeType,
        "federationParameters": "FederationParametersTypeDef",
    },
    total=False,
)


class CreateEnvironmentRequestTypeDef(
    _RequiredCreateEnvironmentRequestTypeDef, _OptionalCreateEnvironmentRequestTypeDef
):
    pass


CreateEnvironmentResponseResponseTypeDef = TypedDict(
    "CreateEnvironmentResponseResponseTypeDef",
    {
        "environmentId": str,
        "environmentArn": str,
        "environmentUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentRequestTypeDef = TypedDict(
    "DeleteEnvironmentRequestTypeDef",
    {
        "environmentId": str,
    },
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "name": str,
        "environmentId": str,
        "awsAccountId": str,
        "status": EnvironmentStatusType,
        "environmentUrl": str,
        "description": str,
        "environmentArn": str,
        "sageMakerStudioDomainUrl": str,
        "kmsKeyId": str,
        "dedicatedServiceAccountId": str,
        "federationMode": FederationModeType,
        "federationParameters": "FederationParametersTypeDef",
    },
    total=False,
)

FederationParametersTypeDef = TypedDict(
    "FederationParametersTypeDef",
    {
        "samlMetadataDocument": str,
        "samlMetadataURL": str,
        "applicationCallBackURL": str,
        "federationURN": str,
        "federationProviderName": str,
        "attributeMap": Dict[str, str],
    },
    total=False,
)

GetEnvironmentRequestTypeDef = TypedDict(
    "GetEnvironmentRequestTypeDef",
    {
        "environmentId": str,
    },
)

GetEnvironmentResponseResponseTypeDef = TypedDict(
    "GetEnvironmentResponseResponseTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnvironmentsRequestTypeDef = TypedDict(
    "ListEnvironmentsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListEnvironmentsResponseResponseTypeDef = TypedDict(
    "ListEnvironmentsResponseResponseTypeDef",
    {
        "environments": List["EnvironmentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": Dict[str, str],
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateEnvironmentRequestTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentRequestTypeDef",
    {
        "environmentId": str,
    },
)
_OptionalUpdateEnvironmentRequestTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentRequestTypeDef",
    {
        "name": str,
        "description": str,
        "federationMode": FederationModeType,
        "federationParameters": "FederationParametersTypeDef",
    },
    total=False,
)


class UpdateEnvironmentRequestTypeDef(
    _RequiredUpdateEnvironmentRequestTypeDef, _OptionalUpdateEnvironmentRequestTypeDef
):
    pass


UpdateEnvironmentResponseResponseTypeDef = TypedDict(
    "UpdateEnvironmentResponseResponseTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
