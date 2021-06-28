"""
Type annotations for iotfleethub service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleethub/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotfleethub.type_defs import ApplicationSummaryTypeDef

    data: ApplicationSummaryTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import ApplicationStateType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationSummaryTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateApplicationResponseResponseTypeDef",
    "DeleteApplicationRequestTypeDef",
    "DescribeApplicationRequestTypeDef",
    "DescribeApplicationResponseResponseTypeDef",
    "ListApplicationsRequestTypeDef",
    "ListApplicationsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApplicationRequestTypeDef",
)

_RequiredApplicationSummaryTypeDef = TypedDict(
    "_RequiredApplicationSummaryTypeDef",
    {
        "applicationId": str,
        "applicationName": str,
        "applicationUrl": str,
    },
)
_OptionalApplicationSummaryTypeDef = TypedDict(
    "_OptionalApplicationSummaryTypeDef",
    {
        "applicationDescription": str,
        "applicationCreationDate": int,
        "applicationLastUpdateDate": int,
        "applicationState": ApplicationStateType,
    },
    total=False,
)


class ApplicationSummaryTypeDef(
    _RequiredApplicationSummaryTypeDef, _OptionalApplicationSummaryTypeDef
):
    pass


_RequiredCreateApplicationRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestTypeDef",
    {
        "applicationName": str,
        "roleArn": str,
    },
)
_OptionalCreateApplicationRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestTypeDef",
    {
        "applicationDescription": str,
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateApplicationRequestTypeDef(
    _RequiredCreateApplicationRequestTypeDef, _OptionalCreateApplicationRequestTypeDef
):
    pass


CreateApplicationResponseResponseTypeDef = TypedDict(
    "CreateApplicationResponseResponseTypeDef",
    {
        "applicationId": str,
        "applicationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteApplicationRequestTypeDef = TypedDict(
    "_RequiredDeleteApplicationRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalDeleteApplicationRequestTypeDef = TypedDict(
    "_OptionalDeleteApplicationRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteApplicationRequestTypeDef(
    _RequiredDeleteApplicationRequestTypeDef, _OptionalDeleteApplicationRequestTypeDef
):
    pass


DescribeApplicationRequestTypeDef = TypedDict(
    "DescribeApplicationRequestTypeDef",
    {
        "applicationId": str,
    },
)

DescribeApplicationResponseResponseTypeDef = TypedDict(
    "DescribeApplicationResponseResponseTypeDef",
    {
        "applicationId": str,
        "applicationArn": str,
        "applicationName": str,
        "applicationDescription": str,
        "applicationUrl": str,
        "applicationState": ApplicationStateType,
        "applicationCreationDate": int,
        "applicationLastUpdateDate": int,
        "roleArn": str,
        "ssoClientId": str,
        "errorMessage": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsRequestTypeDef = TypedDict(
    "ListApplicationsRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListApplicationsResponseResponseTypeDef = TypedDict(
    "ListApplicationsResponseResponseTypeDef",
    {
        "applicationSummaries": List["ApplicationSummaryTypeDef"],
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
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

_RequiredUpdateApplicationRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalUpdateApplicationRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestTypeDef",
    {
        "applicationName": str,
        "applicationDescription": str,
        "clientToken": str,
    },
    total=False,
)


class UpdateApplicationRequestTypeDef(
    _RequiredUpdateApplicationRequestTypeDef, _OptionalUpdateApplicationRequestTypeDef
):
    pass
