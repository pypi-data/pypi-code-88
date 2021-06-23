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
from typing import Dict, List

from .literals import ApplicationStateType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationSummaryTypeDef",
    "CreateApplicationResponseTypeDef",
    "DescribeApplicationResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
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


CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "applicationId": str,
        "applicationArn": str,
    },
)

_RequiredDescribeApplicationResponseTypeDef = TypedDict(
    "_RequiredDescribeApplicationResponseTypeDef",
    {
        "applicationId": str,
        "applicationArn": str,
        "applicationName": str,
        "applicationUrl": str,
        "applicationState": ApplicationStateType,
        "applicationCreationDate": int,
        "applicationLastUpdateDate": int,
        "roleArn": str,
    },
)
_OptionalDescribeApplicationResponseTypeDef = TypedDict(
    "_OptionalDescribeApplicationResponseTypeDef",
    {
        "applicationDescription": str,
        "ssoClientId": str,
        "errorMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class DescribeApplicationResponseTypeDef(
    _RequiredDescribeApplicationResponseTypeDef, _OptionalDescribeApplicationResponseTypeDef
):
    pass


ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "applicationSummaries": List["ApplicationSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
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
