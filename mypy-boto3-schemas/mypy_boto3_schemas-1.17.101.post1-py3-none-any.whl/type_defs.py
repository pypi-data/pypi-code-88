"""
Type annotations for schemas service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/type_defs.html)

Usage::

    ```python
    from mypy_boto3_schemas.type_defs import CreateDiscovererRequestTypeDef

    data: CreateDiscovererRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import CodeGenerationStatusType, DiscovererStateType, TypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateDiscovererRequestTypeDef",
    "CreateDiscovererResponseResponseTypeDef",
    "CreateRegistryRequestTypeDef",
    "CreateRegistryResponseResponseTypeDef",
    "CreateSchemaRequestTypeDef",
    "CreateSchemaResponseResponseTypeDef",
    "DeleteDiscovererRequestTypeDef",
    "DeleteRegistryRequestTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteSchemaRequestTypeDef",
    "DeleteSchemaVersionRequestTypeDef",
    "DescribeCodeBindingRequestTypeDef",
    "DescribeCodeBindingResponseResponseTypeDef",
    "DescribeDiscovererRequestTypeDef",
    "DescribeDiscovererResponseResponseTypeDef",
    "DescribeRegistryRequestTypeDef",
    "DescribeRegistryResponseResponseTypeDef",
    "DescribeSchemaRequestTypeDef",
    "DescribeSchemaResponseResponseTypeDef",
    "DiscovererSummaryTypeDef",
    "ExportSchemaRequestTypeDef",
    "ExportSchemaResponseResponseTypeDef",
    "GetCodeBindingSourceRequestTypeDef",
    "GetCodeBindingSourceResponseResponseTypeDef",
    "GetDiscoveredSchemaRequestTypeDef",
    "GetDiscoveredSchemaResponseResponseTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResponseResponseTypeDef",
    "ListDiscoverersRequestTypeDef",
    "ListDiscoverersResponseResponseTypeDef",
    "ListRegistriesRequestTypeDef",
    "ListRegistriesResponseResponseTypeDef",
    "ListSchemaVersionsRequestTypeDef",
    "ListSchemaVersionsResponseResponseTypeDef",
    "ListSchemasRequestTypeDef",
    "ListSchemasResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutCodeBindingRequestTypeDef",
    "PutCodeBindingResponseResponseTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResponseResponseTypeDef",
    "RegistrySummaryTypeDef",
    "ResponseMetadataTypeDef",
    "SchemaSummaryTypeDef",
    "SchemaVersionSummaryTypeDef",
    "SearchSchemaSummaryTypeDef",
    "SearchSchemaVersionSummaryTypeDef",
    "SearchSchemasRequestTypeDef",
    "SearchSchemasResponseResponseTypeDef",
    "StartDiscovererRequestTypeDef",
    "StartDiscovererResponseResponseTypeDef",
    "StopDiscovererRequestTypeDef",
    "StopDiscovererResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDiscovererRequestTypeDef",
    "UpdateDiscovererResponseResponseTypeDef",
    "UpdateRegistryRequestTypeDef",
    "UpdateRegistryResponseResponseTypeDef",
    "UpdateSchemaRequestTypeDef",
    "UpdateSchemaResponseResponseTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredCreateDiscovererRequestTypeDef = TypedDict(
    "_RequiredCreateDiscovererRequestTypeDef",
    {
        "SourceArn": str,
    },
)
_OptionalCreateDiscovererRequestTypeDef = TypedDict(
    "_OptionalCreateDiscovererRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateDiscovererRequestTypeDef(
    _RequiredCreateDiscovererRequestTypeDef, _OptionalCreateDiscovererRequestTypeDef
):
    pass


CreateDiscovererResponseResponseTypeDef = TypedDict(
    "CreateDiscovererResponseResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": DiscovererStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRegistryRequestTypeDef = TypedDict(
    "_RequiredCreateRegistryRequestTypeDef",
    {
        "RegistryName": str,
    },
)
_OptionalCreateRegistryRequestTypeDef = TypedDict(
    "_OptionalCreateRegistryRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateRegistryRequestTypeDef(
    _RequiredCreateRegistryRequestTypeDef, _OptionalCreateRegistryRequestTypeDef
):
    pass


CreateRegistryResponseResponseTypeDef = TypedDict(
    "CreateRegistryResponseResponseTypeDef",
    {
        "Description": str,
        "RegistryArn": str,
        "RegistryName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSchemaRequestTypeDef = TypedDict(
    "_RequiredCreateSchemaRequestTypeDef",
    {
        "Content": str,
        "RegistryName": str,
        "SchemaName": str,
        "Type": TypeType,
    },
)
_OptionalCreateSchemaRequestTypeDef = TypedDict(
    "_OptionalCreateSchemaRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateSchemaRequestTypeDef(
    _RequiredCreateSchemaRequestTypeDef, _OptionalCreateSchemaRequestTypeDef
):
    pass


CreateSchemaResponseResponseTypeDef = TypedDict(
    "CreateSchemaResponseResponseTypeDef",
    {
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDiscovererRequestTypeDef = TypedDict(
    "DeleteDiscovererRequestTypeDef",
    {
        "DiscovererId": str,
    },
)

DeleteRegistryRequestTypeDef = TypedDict(
    "DeleteRegistryRequestTypeDef",
    {
        "RegistryName": str,
    },
)

DeleteResourcePolicyRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestTypeDef",
    {
        "RegistryName": str,
    },
    total=False,
)

DeleteSchemaRequestTypeDef = TypedDict(
    "DeleteSchemaRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
    },
)

DeleteSchemaVersionRequestTypeDef = TypedDict(
    "DeleteSchemaVersionRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "SchemaVersion": str,
    },
)

_RequiredDescribeCodeBindingRequestTypeDef = TypedDict(
    "_RequiredDescribeCodeBindingRequestTypeDef",
    {
        "Language": str,
        "RegistryName": str,
        "SchemaName": str,
    },
)
_OptionalDescribeCodeBindingRequestTypeDef = TypedDict(
    "_OptionalDescribeCodeBindingRequestTypeDef",
    {
        "SchemaVersion": str,
    },
    total=False,
)


class DescribeCodeBindingRequestTypeDef(
    _RequiredDescribeCodeBindingRequestTypeDef, _OptionalDescribeCodeBindingRequestTypeDef
):
    pass


DescribeCodeBindingResponseResponseTypeDef = TypedDict(
    "DescribeCodeBindingResponseResponseTypeDef",
    {
        "CreationDate": datetime,
        "LastModified": datetime,
        "SchemaVersion": str,
        "Status": CodeGenerationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDiscovererRequestTypeDef = TypedDict(
    "DescribeDiscovererRequestTypeDef",
    {
        "DiscovererId": str,
    },
)

DescribeDiscovererResponseResponseTypeDef = TypedDict(
    "DescribeDiscovererResponseResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": DiscovererStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegistryRequestTypeDef = TypedDict(
    "DescribeRegistryRequestTypeDef",
    {
        "RegistryName": str,
    },
)

DescribeRegistryResponseResponseTypeDef = TypedDict(
    "DescribeRegistryResponseResponseTypeDef",
    {
        "Description": str,
        "RegistryArn": str,
        "RegistryName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSchemaRequestTypeDef = TypedDict(
    "_RequiredDescribeSchemaRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
    },
)
_OptionalDescribeSchemaRequestTypeDef = TypedDict(
    "_OptionalDescribeSchemaRequestTypeDef",
    {
        "SchemaVersion": str,
    },
    total=False,
)


class DescribeSchemaRequestTypeDef(
    _RequiredDescribeSchemaRequestTypeDef, _OptionalDescribeSchemaRequestTypeDef
):
    pass


DescribeSchemaResponseResponseTypeDef = TypedDict(
    "DescribeSchemaResponseResponseTypeDef",
    {
        "Content": str,
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiscovererSummaryTypeDef = TypedDict(
    "DiscovererSummaryTypeDef",
    {
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": DiscovererStateType,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredExportSchemaRequestTypeDef = TypedDict(
    "_RequiredExportSchemaRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "Type": str,
    },
)
_OptionalExportSchemaRequestTypeDef = TypedDict(
    "_OptionalExportSchemaRequestTypeDef",
    {
        "SchemaVersion": str,
    },
    total=False,
)


class ExportSchemaRequestTypeDef(
    _RequiredExportSchemaRequestTypeDef, _OptionalExportSchemaRequestTypeDef
):
    pass


ExportSchemaResponseResponseTypeDef = TypedDict(
    "ExportSchemaResponseResponseTypeDef",
    {
        "Content": str,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Type": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCodeBindingSourceRequestTypeDef = TypedDict(
    "_RequiredGetCodeBindingSourceRequestTypeDef",
    {
        "Language": str,
        "RegistryName": str,
        "SchemaName": str,
    },
)
_OptionalGetCodeBindingSourceRequestTypeDef = TypedDict(
    "_OptionalGetCodeBindingSourceRequestTypeDef",
    {
        "SchemaVersion": str,
    },
    total=False,
)


class GetCodeBindingSourceRequestTypeDef(
    _RequiredGetCodeBindingSourceRequestTypeDef, _OptionalGetCodeBindingSourceRequestTypeDef
):
    pass


GetCodeBindingSourceResponseResponseTypeDef = TypedDict(
    "GetCodeBindingSourceResponseResponseTypeDef",
    {
        "Body": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDiscoveredSchemaRequestTypeDef = TypedDict(
    "GetDiscoveredSchemaRequestTypeDef",
    {
        "Events": List[str],
        "Type": TypeType,
    },
)

GetDiscoveredSchemaResponseResponseTypeDef = TypedDict(
    "GetDiscoveredSchemaResponseResponseTypeDef",
    {
        "Content": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestTypeDef",
    {
        "RegistryName": str,
    },
    total=False,
)

GetResourcePolicyResponseResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseResponseTypeDef",
    {
        "Policy": str,
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDiscoverersRequestTypeDef = TypedDict(
    "ListDiscoverersRequestTypeDef",
    {
        "DiscovererIdPrefix": str,
        "Limit": int,
        "NextToken": str,
        "SourceArnPrefix": str,
    },
    total=False,
)

ListDiscoverersResponseResponseTypeDef = TypedDict(
    "ListDiscoverersResponseResponseTypeDef",
    {
        "Discoverers": List["DiscovererSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRegistriesRequestTypeDef = TypedDict(
    "ListRegistriesRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
        "RegistryNamePrefix": str,
        "Scope": str,
    },
    total=False,
)

ListRegistriesResponseResponseTypeDef = TypedDict(
    "ListRegistriesResponseResponseTypeDef",
    {
        "NextToken": str,
        "Registries": List["RegistrySummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSchemaVersionsRequestTypeDef = TypedDict(
    "_RequiredListSchemaVersionsRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
    },
)
_OptionalListSchemaVersionsRequestTypeDef = TypedDict(
    "_OptionalListSchemaVersionsRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class ListSchemaVersionsRequestTypeDef(
    _RequiredListSchemaVersionsRequestTypeDef, _OptionalListSchemaVersionsRequestTypeDef
):
    pass


ListSchemaVersionsResponseResponseTypeDef = TypedDict(
    "ListSchemaVersionsResponseResponseTypeDef",
    {
        "NextToken": str,
        "SchemaVersions": List["SchemaVersionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSchemasRequestTypeDef = TypedDict(
    "_RequiredListSchemasRequestTypeDef",
    {
        "RegistryName": str,
    },
)
_OptionalListSchemasRequestTypeDef = TypedDict(
    "_OptionalListSchemasRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
        "SchemaNamePrefix": str,
    },
    total=False,
)


class ListSchemasRequestTypeDef(
    _RequiredListSchemasRequestTypeDef, _OptionalListSchemasRequestTypeDef
):
    pass


ListSchemasResponseResponseTypeDef = TypedDict(
    "ListSchemasResponseResponseTypeDef",
    {
        "NextToken": str,
        "Schemas": List["SchemaSummaryTypeDef"],
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPutCodeBindingRequestTypeDef = TypedDict(
    "_RequiredPutCodeBindingRequestTypeDef",
    {
        "Language": str,
        "RegistryName": str,
        "SchemaName": str,
    },
)
_OptionalPutCodeBindingRequestTypeDef = TypedDict(
    "_OptionalPutCodeBindingRequestTypeDef",
    {
        "SchemaVersion": str,
    },
    total=False,
)


class PutCodeBindingRequestTypeDef(
    _RequiredPutCodeBindingRequestTypeDef, _OptionalPutCodeBindingRequestTypeDef
):
    pass


PutCodeBindingResponseResponseTypeDef = TypedDict(
    "PutCodeBindingResponseResponseTypeDef",
    {
        "CreationDate": datetime,
        "LastModified": datetime,
        "SchemaVersion": str,
        "Status": CodeGenerationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutResourcePolicyRequestTypeDef = TypedDict(
    "_RequiredPutResourcePolicyRequestTypeDef",
    {
        "Policy": str,
    },
)
_OptionalPutResourcePolicyRequestTypeDef = TypedDict(
    "_OptionalPutResourcePolicyRequestTypeDef",
    {
        "RegistryName": str,
        "RevisionId": str,
    },
    total=False,
)


class PutResourcePolicyRequestTypeDef(
    _RequiredPutResourcePolicyRequestTypeDef, _OptionalPutResourcePolicyRequestTypeDef
):
    pass


PutResourcePolicyResponseResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseResponseTypeDef",
    {
        "Policy": str,
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegistrySummaryTypeDef = TypedDict(
    "RegistrySummaryTypeDef",
    {
        "RegistryArn": str,
        "RegistryName": str,
        "Tags": Dict[str, str],
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

SchemaSummaryTypeDef = TypedDict(
    "SchemaSummaryTypeDef",
    {
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "Tags": Dict[str, str],
        "VersionCount": int,
    },
    total=False,
)

SchemaVersionSummaryTypeDef = TypedDict(
    "SchemaVersionSummaryTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Type": TypeType,
    },
    total=False,
)

SearchSchemaSummaryTypeDef = TypedDict(
    "SearchSchemaSummaryTypeDef",
    {
        "RegistryName": str,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersions": List["SearchSchemaVersionSummaryTypeDef"],
    },
    total=False,
)

SearchSchemaVersionSummaryTypeDef = TypedDict(
    "SearchSchemaVersionSummaryTypeDef",
    {
        "CreatedDate": datetime,
        "SchemaVersion": str,
        "Type": TypeType,
    },
    total=False,
)

_RequiredSearchSchemasRequestTypeDef = TypedDict(
    "_RequiredSearchSchemasRequestTypeDef",
    {
        "Keywords": str,
        "RegistryName": str,
    },
)
_OptionalSearchSchemasRequestTypeDef = TypedDict(
    "_OptionalSearchSchemasRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class SearchSchemasRequestTypeDef(
    _RequiredSearchSchemasRequestTypeDef, _OptionalSearchSchemasRequestTypeDef
):
    pass


SearchSchemasResponseResponseTypeDef = TypedDict(
    "SearchSchemasResponseResponseTypeDef",
    {
        "NextToken": str,
        "Schemas": List["SearchSchemaSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartDiscovererRequestTypeDef = TypedDict(
    "StartDiscovererRequestTypeDef",
    {
        "DiscovererId": str,
    },
)

StartDiscovererResponseResponseTypeDef = TypedDict(
    "StartDiscovererResponseResponseTypeDef",
    {
        "DiscovererId": str,
        "State": DiscovererStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDiscovererRequestTypeDef = TypedDict(
    "StopDiscovererRequestTypeDef",
    {
        "DiscovererId": str,
    },
)

StopDiscovererResponseResponseTypeDef = TypedDict(
    "StopDiscovererResponseResponseTypeDef",
    {
        "DiscovererId": str,
        "State": DiscovererStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredUpdateDiscovererRequestTypeDef = TypedDict(
    "_RequiredUpdateDiscovererRequestTypeDef",
    {
        "DiscovererId": str,
    },
)
_OptionalUpdateDiscovererRequestTypeDef = TypedDict(
    "_OptionalUpdateDiscovererRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateDiscovererRequestTypeDef(
    _RequiredUpdateDiscovererRequestTypeDef, _OptionalUpdateDiscovererRequestTypeDef
):
    pass


UpdateDiscovererResponseResponseTypeDef = TypedDict(
    "UpdateDiscovererResponseResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": DiscovererStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRegistryRequestTypeDef = TypedDict(
    "_RequiredUpdateRegistryRequestTypeDef",
    {
        "RegistryName": str,
    },
)
_OptionalUpdateRegistryRequestTypeDef = TypedDict(
    "_OptionalUpdateRegistryRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateRegistryRequestTypeDef(
    _RequiredUpdateRegistryRequestTypeDef, _OptionalUpdateRegistryRequestTypeDef
):
    pass


UpdateRegistryResponseResponseTypeDef = TypedDict(
    "UpdateRegistryResponseResponseTypeDef",
    {
        "Description": str,
        "RegistryArn": str,
        "RegistryName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSchemaRequestTypeDef = TypedDict(
    "_RequiredUpdateSchemaRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
    },
)
_OptionalUpdateSchemaRequestTypeDef = TypedDict(
    "_OptionalUpdateSchemaRequestTypeDef",
    {
        "ClientTokenId": str,
        "Content": str,
        "Description": str,
        "Type": TypeType,
    },
    total=False,
)


class UpdateSchemaRequestTypeDef(
    _RequiredUpdateSchemaRequestTypeDef, _OptionalUpdateSchemaRequestTypeDef
):
    pass


UpdateSchemaResponseResponseTypeDef = TypedDict(
    "UpdateSchemaResponseResponseTypeDef",
    {
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
