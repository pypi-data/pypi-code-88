"""
Type annotations for sdb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sdb.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttributeTypeDef",
    "BatchDeleteAttributesRequestTypeDef",
    "BatchPutAttributesRequestTypeDef",
    "CreateDomainRequestTypeDef",
    "DeletableItemTypeDef",
    "DeleteAttributesRequestTypeDef",
    "DeleteDomainRequestTypeDef",
    "DomainMetadataRequestTypeDef",
    "DomainMetadataResultResponseTypeDef",
    "GetAttributesRequestTypeDef",
    "GetAttributesResultResponseTypeDef",
    "ItemTypeDef",
    "ListDomainsRequestTypeDef",
    "ListDomainsResultResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutAttributesRequestTypeDef",
    "ReplaceableAttributeTypeDef",
    "ReplaceableItemTypeDef",
    "ResponseMetadataTypeDef",
    "SelectRequestTypeDef",
    "SelectResultResponseTypeDef",
    "UpdateConditionTypeDef",
)

_RequiredAttributeTypeDef = TypedDict(
    "_RequiredAttributeTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {
        "AlternateNameEncoding": str,
        "AlternateValueEncoding": str,
    },
    total=False,
)


class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass


BatchDeleteAttributesRequestTypeDef = TypedDict(
    "BatchDeleteAttributesRequestTypeDef",
    {
        "DomainName": str,
        "Items": List["DeletableItemTypeDef"],
    },
)

BatchPutAttributesRequestTypeDef = TypedDict(
    "BatchPutAttributesRequestTypeDef",
    {
        "DomainName": str,
        "Items": List["ReplaceableItemTypeDef"],
    },
)

CreateDomainRequestTypeDef = TypedDict(
    "CreateDomainRequestTypeDef",
    {
        "DomainName": str,
    },
)

_RequiredDeletableItemTypeDef = TypedDict(
    "_RequiredDeletableItemTypeDef",
    {
        "Name": str,
    },
)
_OptionalDeletableItemTypeDef = TypedDict(
    "_OptionalDeletableItemTypeDef",
    {
        "Attributes": List["AttributeTypeDef"],
    },
    total=False,
)


class DeletableItemTypeDef(_RequiredDeletableItemTypeDef, _OptionalDeletableItemTypeDef):
    pass


_RequiredDeleteAttributesRequestTypeDef = TypedDict(
    "_RequiredDeleteAttributesRequestTypeDef",
    {
        "DomainName": str,
        "ItemName": str,
    },
)
_OptionalDeleteAttributesRequestTypeDef = TypedDict(
    "_OptionalDeleteAttributesRequestTypeDef",
    {
        "Attributes": List["AttributeTypeDef"],
        "Expected": "UpdateConditionTypeDef",
    },
    total=False,
)


class DeleteAttributesRequestTypeDef(
    _RequiredDeleteAttributesRequestTypeDef, _OptionalDeleteAttributesRequestTypeDef
):
    pass


DeleteDomainRequestTypeDef = TypedDict(
    "DeleteDomainRequestTypeDef",
    {
        "DomainName": str,
    },
)

DomainMetadataRequestTypeDef = TypedDict(
    "DomainMetadataRequestTypeDef",
    {
        "DomainName": str,
    },
)

DomainMetadataResultResponseTypeDef = TypedDict(
    "DomainMetadataResultResponseTypeDef",
    {
        "ItemCount": int,
        "ItemNamesSizeBytes": int,
        "AttributeNameCount": int,
        "AttributeNamesSizeBytes": int,
        "AttributeValueCount": int,
        "AttributeValuesSizeBytes": int,
        "Timestamp": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAttributesRequestTypeDef = TypedDict(
    "_RequiredGetAttributesRequestTypeDef",
    {
        "DomainName": str,
        "ItemName": str,
    },
)
_OptionalGetAttributesRequestTypeDef = TypedDict(
    "_OptionalGetAttributesRequestTypeDef",
    {
        "AttributeNames": List[str],
        "ConsistentRead": bool,
    },
    total=False,
)


class GetAttributesRequestTypeDef(
    _RequiredGetAttributesRequestTypeDef, _OptionalGetAttributesRequestTypeDef
):
    pass


GetAttributesResultResponseTypeDef = TypedDict(
    "GetAttributesResultResponseTypeDef",
    {
        "Attributes": List["AttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredItemTypeDef = TypedDict(
    "_RequiredItemTypeDef",
    {
        "Name": str,
        "Attributes": List["AttributeTypeDef"],
    },
)
_OptionalItemTypeDef = TypedDict(
    "_OptionalItemTypeDef",
    {
        "AlternateNameEncoding": str,
    },
    total=False,
)


class ItemTypeDef(_RequiredItemTypeDef, _OptionalItemTypeDef):
    pass


ListDomainsRequestTypeDef = TypedDict(
    "ListDomainsRequestTypeDef",
    {
        "MaxNumberOfDomains": int,
        "NextToken": str,
    },
    total=False,
)

ListDomainsResultResponseTypeDef = TypedDict(
    "ListDomainsResultResponseTypeDef",
    {
        "DomainNames": List[str],
        "NextToken": str,
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

_RequiredPutAttributesRequestTypeDef = TypedDict(
    "_RequiredPutAttributesRequestTypeDef",
    {
        "DomainName": str,
        "ItemName": str,
        "Attributes": List["ReplaceableAttributeTypeDef"],
    },
)
_OptionalPutAttributesRequestTypeDef = TypedDict(
    "_OptionalPutAttributesRequestTypeDef",
    {
        "Expected": "UpdateConditionTypeDef",
    },
    total=False,
)


class PutAttributesRequestTypeDef(
    _RequiredPutAttributesRequestTypeDef, _OptionalPutAttributesRequestTypeDef
):
    pass


_RequiredReplaceableAttributeTypeDef = TypedDict(
    "_RequiredReplaceableAttributeTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
_OptionalReplaceableAttributeTypeDef = TypedDict(
    "_OptionalReplaceableAttributeTypeDef",
    {
        "Replace": bool,
    },
    total=False,
)


class ReplaceableAttributeTypeDef(
    _RequiredReplaceableAttributeTypeDef, _OptionalReplaceableAttributeTypeDef
):
    pass


ReplaceableItemTypeDef = TypedDict(
    "ReplaceableItemTypeDef",
    {
        "Name": str,
        "Attributes": List["ReplaceableAttributeTypeDef"],
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

_RequiredSelectRequestTypeDef = TypedDict(
    "_RequiredSelectRequestTypeDef",
    {
        "SelectExpression": str,
    },
)
_OptionalSelectRequestTypeDef = TypedDict(
    "_OptionalSelectRequestTypeDef",
    {
        "NextToken": str,
        "ConsistentRead": bool,
    },
    total=False,
)


class SelectRequestTypeDef(_RequiredSelectRequestTypeDef, _OptionalSelectRequestTypeDef):
    pass


SelectResultResponseTypeDef = TypedDict(
    "SelectResultResponseTypeDef",
    {
        "Items": List["ItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConditionTypeDef = TypedDict(
    "UpdateConditionTypeDef",
    {
        "Name": str,
        "Value": str,
        "Exists": bool,
    },
    total=False,
)
