"""
Type annotations for outposts service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/type_defs.html)

Usage::

    ```python
    from mypy_boto3_outposts.type_defs import CreateOutpostInputTypeDef

    data: CreateOutpostInputTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateOutpostInputTypeDef",
    "CreateOutpostOutputResponseTypeDef",
    "DeleteOutpostInputTypeDef",
    "DeleteSiteInputTypeDef",
    "GetOutpostInputTypeDef",
    "GetOutpostInstanceTypesInputTypeDef",
    "GetOutpostInstanceTypesOutputResponseTypeDef",
    "GetOutpostOutputResponseTypeDef",
    "InstanceTypeItemTypeDef",
    "ListOutpostsInputTypeDef",
    "ListOutpostsOutputResponseTypeDef",
    "ListSitesInputTypeDef",
    "ListSitesOutputResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "OutpostTypeDef",
    "ResponseMetadataTypeDef",
    "SiteTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
)

_RequiredCreateOutpostInputTypeDef = TypedDict(
    "_RequiredCreateOutpostInputTypeDef",
    {
        "Name": str,
        "SiteId": str,
    },
)
_OptionalCreateOutpostInputTypeDef = TypedDict(
    "_OptionalCreateOutpostInputTypeDef",
    {
        "Description": str,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateOutpostInputTypeDef(
    _RequiredCreateOutpostInputTypeDef, _OptionalCreateOutpostInputTypeDef
):
    pass


CreateOutpostOutputResponseTypeDef = TypedDict(
    "CreateOutpostOutputResponseTypeDef",
    {
        "Outpost": "OutpostTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteOutpostInputTypeDef = TypedDict(
    "DeleteOutpostInputTypeDef",
    {
        "OutpostId": str,
    },
)

DeleteSiteInputTypeDef = TypedDict(
    "DeleteSiteInputTypeDef",
    {
        "SiteId": str,
    },
)

GetOutpostInputTypeDef = TypedDict(
    "GetOutpostInputTypeDef",
    {
        "OutpostId": str,
    },
)

_RequiredGetOutpostInstanceTypesInputTypeDef = TypedDict(
    "_RequiredGetOutpostInstanceTypesInputTypeDef",
    {
        "OutpostId": str,
    },
)
_OptionalGetOutpostInstanceTypesInputTypeDef = TypedDict(
    "_OptionalGetOutpostInstanceTypesInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetOutpostInstanceTypesInputTypeDef(
    _RequiredGetOutpostInstanceTypesInputTypeDef, _OptionalGetOutpostInstanceTypesInputTypeDef
):
    pass


GetOutpostInstanceTypesOutputResponseTypeDef = TypedDict(
    "GetOutpostInstanceTypesOutputResponseTypeDef",
    {
        "InstanceTypes": List["InstanceTypeItemTypeDef"],
        "NextToken": str,
        "OutpostId": str,
        "OutpostArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOutpostOutputResponseTypeDef = TypedDict(
    "GetOutpostOutputResponseTypeDef",
    {
        "Outpost": "OutpostTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceTypeItemTypeDef = TypedDict(
    "InstanceTypeItemTypeDef",
    {
        "InstanceType": str,
    },
    total=False,
)

ListOutpostsInputTypeDef = TypedDict(
    "ListOutpostsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListOutpostsOutputResponseTypeDef = TypedDict(
    "ListOutpostsOutputResponseTypeDef",
    {
        "Outposts": List["OutpostTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSitesInputTypeDef = TypedDict(
    "ListSitesInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListSitesOutputResponseTypeDef = TypedDict(
    "ListSitesOutputResponseTypeDef",
    {
        "Sites": List["SiteTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutpostTypeDef = TypedDict(
    "OutpostTypeDef",
    {
        "OutpostId": str,
        "OwnerId": str,
        "OutpostArn": str,
        "SiteId": str,
        "Name": str,
        "Description": str,
        "LifeCycleStatus": str,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "Tags": Dict[str, str],
        "SiteArn": str,
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

SiteTypeDef = TypedDict(
    "SiteTypeDef",
    {
        "SiteId": str,
        "AccountId": str,
        "Name": str,
        "Description": str,
        "Tags": Dict[str, str],
        "SiteArn": str,
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)
