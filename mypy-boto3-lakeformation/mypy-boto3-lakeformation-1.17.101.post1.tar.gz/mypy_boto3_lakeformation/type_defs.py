"""
Type annotations for lakeformation service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lakeformation.type_defs import AddLFTagsToResourceRequestTypeDef

    data: AddLFTagsToResourceRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ComparisonOperatorType,
    DataLakeResourceTypeType,
    FieldNameStringType,
    PermissionType,
    ResourceShareTypeType,
    ResourceTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddLFTagsToResourceRequestTypeDef",
    "AddLFTagsToResourceResponseResponseTypeDef",
    "BatchGrantPermissionsRequestTypeDef",
    "BatchGrantPermissionsResponseResponseTypeDef",
    "BatchPermissionsFailureEntryTypeDef",
    "BatchPermissionsRequestEntryTypeDef",
    "BatchRevokePermissionsRequestTypeDef",
    "BatchRevokePermissionsResponseResponseTypeDef",
    "ColumnLFTagTypeDef",
    "ColumnWildcardTypeDef",
    "CreateLFTagRequestTypeDef",
    "DataLakePrincipalTypeDef",
    "DataLakeSettingsTypeDef",
    "DataLocationResourceTypeDef",
    "DatabaseResourceTypeDef",
    "DeleteLFTagRequestTypeDef",
    "DeregisterResourceRequestTypeDef",
    "DescribeResourceRequestTypeDef",
    "DescribeResourceResponseResponseTypeDef",
    "DetailsMapTypeDef",
    "ErrorDetailTypeDef",
    "FilterConditionTypeDef",
    "GetDataLakeSettingsRequestTypeDef",
    "GetDataLakeSettingsResponseResponseTypeDef",
    "GetEffectivePermissionsForPathRequestTypeDef",
    "GetEffectivePermissionsForPathResponseResponseTypeDef",
    "GetLFTagRequestTypeDef",
    "GetLFTagResponseResponseTypeDef",
    "GetResourceLFTagsRequestTypeDef",
    "GetResourceLFTagsResponseResponseTypeDef",
    "GrantPermissionsRequestTypeDef",
    "LFTagErrorTypeDef",
    "LFTagKeyResourceTypeDef",
    "LFTagPairTypeDef",
    "LFTagPolicyResourceTypeDef",
    "LFTagTypeDef",
    "ListLFTagsRequestTypeDef",
    "ListLFTagsResponseResponseTypeDef",
    "ListPermissionsRequestTypeDef",
    "ListPermissionsResponseResponseTypeDef",
    "ListResourcesRequestTypeDef",
    "ListResourcesResponseResponseTypeDef",
    "PrincipalPermissionsTypeDef",
    "PrincipalResourcePermissionsTypeDef",
    "PutDataLakeSettingsRequestTypeDef",
    "RegisterResourceRequestTypeDef",
    "RemoveLFTagsFromResourceRequestTypeDef",
    "RemoveLFTagsFromResourceResponseResponseTypeDef",
    "ResourceInfoTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RevokePermissionsRequestTypeDef",
    "SearchDatabasesByLFTagsRequestTypeDef",
    "SearchDatabasesByLFTagsResponseResponseTypeDef",
    "SearchTablesByLFTagsRequestTypeDef",
    "SearchTablesByLFTagsResponseResponseTypeDef",
    "TableResourceTypeDef",
    "TableWithColumnsResourceTypeDef",
    "TaggedDatabaseTypeDef",
    "TaggedTableTypeDef",
    "UpdateLFTagRequestTypeDef",
    "UpdateResourceRequestTypeDef",
)

_RequiredAddLFTagsToResourceRequestTypeDef = TypedDict(
    "_RequiredAddLFTagsToResourceRequestTypeDef",
    {
        "Resource": "ResourceTypeDef",
        "LFTags": List["LFTagPairTypeDef"],
    },
)
_OptionalAddLFTagsToResourceRequestTypeDef = TypedDict(
    "_OptionalAddLFTagsToResourceRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class AddLFTagsToResourceRequestTypeDef(
    _RequiredAddLFTagsToResourceRequestTypeDef, _OptionalAddLFTagsToResourceRequestTypeDef
):
    pass


AddLFTagsToResourceResponseResponseTypeDef = TypedDict(
    "AddLFTagsToResourceResponseResponseTypeDef",
    {
        "Failures": List["LFTagErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGrantPermissionsRequestTypeDef = TypedDict(
    "_RequiredBatchGrantPermissionsRequestTypeDef",
    {
        "Entries": List["BatchPermissionsRequestEntryTypeDef"],
    },
)
_OptionalBatchGrantPermissionsRequestTypeDef = TypedDict(
    "_OptionalBatchGrantPermissionsRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class BatchGrantPermissionsRequestTypeDef(
    _RequiredBatchGrantPermissionsRequestTypeDef, _OptionalBatchGrantPermissionsRequestTypeDef
):
    pass


BatchGrantPermissionsResponseResponseTypeDef = TypedDict(
    "BatchGrantPermissionsResponseResponseTypeDef",
    {
        "Failures": List["BatchPermissionsFailureEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPermissionsFailureEntryTypeDef = TypedDict(
    "BatchPermissionsFailureEntryTypeDef",
    {
        "RequestEntry": "BatchPermissionsRequestEntryTypeDef",
        "Error": "ErrorDetailTypeDef",
    },
    total=False,
)

_RequiredBatchPermissionsRequestEntryTypeDef = TypedDict(
    "_RequiredBatchPermissionsRequestEntryTypeDef",
    {
        "Id": str,
    },
)
_OptionalBatchPermissionsRequestEntryTypeDef = TypedDict(
    "_OptionalBatchPermissionsRequestEntryTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Resource": "ResourceTypeDef",
        "Permissions": List[PermissionType],
        "PermissionsWithGrantOption": List[PermissionType],
    },
    total=False,
)


class BatchPermissionsRequestEntryTypeDef(
    _RequiredBatchPermissionsRequestEntryTypeDef, _OptionalBatchPermissionsRequestEntryTypeDef
):
    pass


_RequiredBatchRevokePermissionsRequestTypeDef = TypedDict(
    "_RequiredBatchRevokePermissionsRequestTypeDef",
    {
        "Entries": List["BatchPermissionsRequestEntryTypeDef"],
    },
)
_OptionalBatchRevokePermissionsRequestTypeDef = TypedDict(
    "_OptionalBatchRevokePermissionsRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class BatchRevokePermissionsRequestTypeDef(
    _RequiredBatchRevokePermissionsRequestTypeDef, _OptionalBatchRevokePermissionsRequestTypeDef
):
    pass


BatchRevokePermissionsResponseResponseTypeDef = TypedDict(
    "BatchRevokePermissionsResponseResponseTypeDef",
    {
        "Failures": List["BatchPermissionsFailureEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ColumnLFTagTypeDef = TypedDict(
    "ColumnLFTagTypeDef",
    {
        "Name": str,
        "LFTags": List["LFTagPairTypeDef"],
    },
    total=False,
)

ColumnWildcardTypeDef = TypedDict(
    "ColumnWildcardTypeDef",
    {
        "ExcludedColumnNames": List[str],
    },
    total=False,
)

_RequiredCreateLFTagRequestTypeDef = TypedDict(
    "_RequiredCreateLFTagRequestTypeDef",
    {
        "TagKey": str,
        "TagValues": List[str],
    },
)
_OptionalCreateLFTagRequestTypeDef = TypedDict(
    "_OptionalCreateLFTagRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class CreateLFTagRequestTypeDef(
    _RequiredCreateLFTagRequestTypeDef, _OptionalCreateLFTagRequestTypeDef
):
    pass


DataLakePrincipalTypeDef = TypedDict(
    "DataLakePrincipalTypeDef",
    {
        "DataLakePrincipalIdentifier": str,
    },
    total=False,
)

DataLakeSettingsTypeDef = TypedDict(
    "DataLakeSettingsTypeDef",
    {
        "DataLakeAdmins": List["DataLakePrincipalTypeDef"],
        "CreateDatabaseDefaultPermissions": List["PrincipalPermissionsTypeDef"],
        "CreateTableDefaultPermissions": List["PrincipalPermissionsTypeDef"],
        "TrustedResourceOwners": List[str],
    },
    total=False,
)

_RequiredDataLocationResourceTypeDef = TypedDict(
    "_RequiredDataLocationResourceTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalDataLocationResourceTypeDef = TypedDict(
    "_OptionalDataLocationResourceTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class DataLocationResourceTypeDef(
    _RequiredDataLocationResourceTypeDef, _OptionalDataLocationResourceTypeDef
):
    pass


_RequiredDatabaseResourceTypeDef = TypedDict(
    "_RequiredDatabaseResourceTypeDef",
    {
        "Name": str,
    },
)
_OptionalDatabaseResourceTypeDef = TypedDict(
    "_OptionalDatabaseResourceTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class DatabaseResourceTypeDef(_RequiredDatabaseResourceTypeDef, _OptionalDatabaseResourceTypeDef):
    pass


_RequiredDeleteLFTagRequestTypeDef = TypedDict(
    "_RequiredDeleteLFTagRequestTypeDef",
    {
        "TagKey": str,
    },
)
_OptionalDeleteLFTagRequestTypeDef = TypedDict(
    "_OptionalDeleteLFTagRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class DeleteLFTagRequestTypeDef(
    _RequiredDeleteLFTagRequestTypeDef, _OptionalDeleteLFTagRequestTypeDef
):
    pass


DeregisterResourceRequestTypeDef = TypedDict(
    "DeregisterResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeResourceRequestTypeDef = TypedDict(
    "DescribeResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeResourceResponseResponseTypeDef = TypedDict(
    "DescribeResourceResponseResponseTypeDef",
    {
        "ResourceInfo": "ResourceInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetailsMapTypeDef = TypedDict(
    "DetailsMapTypeDef",
    {
        "ResourceShare": List[str],
    },
    total=False,
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

FilterConditionTypeDef = TypedDict(
    "FilterConditionTypeDef",
    {
        "Field": FieldNameStringType,
        "ComparisonOperator": ComparisonOperatorType,
        "StringValueList": List[str],
    },
    total=False,
)

GetDataLakeSettingsRequestTypeDef = TypedDict(
    "GetDataLakeSettingsRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

GetDataLakeSettingsResponseResponseTypeDef = TypedDict(
    "GetDataLakeSettingsResponseResponseTypeDef",
    {
        "DataLakeSettings": "DataLakeSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetEffectivePermissionsForPathRequestTypeDef = TypedDict(
    "_RequiredGetEffectivePermissionsForPathRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalGetEffectivePermissionsForPathRequestTypeDef = TypedDict(
    "_OptionalGetEffectivePermissionsForPathRequestTypeDef",
    {
        "CatalogId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetEffectivePermissionsForPathRequestTypeDef(
    _RequiredGetEffectivePermissionsForPathRequestTypeDef,
    _OptionalGetEffectivePermissionsForPathRequestTypeDef,
):
    pass


GetEffectivePermissionsForPathResponseResponseTypeDef = TypedDict(
    "GetEffectivePermissionsForPathResponseResponseTypeDef",
    {
        "Permissions": List["PrincipalResourcePermissionsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLFTagRequestTypeDef = TypedDict(
    "_RequiredGetLFTagRequestTypeDef",
    {
        "TagKey": str,
    },
)
_OptionalGetLFTagRequestTypeDef = TypedDict(
    "_OptionalGetLFTagRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class GetLFTagRequestTypeDef(_RequiredGetLFTagRequestTypeDef, _OptionalGetLFTagRequestTypeDef):
    pass


GetLFTagResponseResponseTypeDef = TypedDict(
    "GetLFTagResponseResponseTypeDef",
    {
        "CatalogId": str,
        "TagKey": str,
        "TagValues": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourceLFTagsRequestTypeDef = TypedDict(
    "_RequiredGetResourceLFTagsRequestTypeDef",
    {
        "Resource": "ResourceTypeDef",
    },
)
_OptionalGetResourceLFTagsRequestTypeDef = TypedDict(
    "_OptionalGetResourceLFTagsRequestTypeDef",
    {
        "CatalogId": str,
        "ShowAssignedLFTags": bool,
    },
    total=False,
)


class GetResourceLFTagsRequestTypeDef(
    _RequiredGetResourceLFTagsRequestTypeDef, _OptionalGetResourceLFTagsRequestTypeDef
):
    pass


GetResourceLFTagsResponseResponseTypeDef = TypedDict(
    "GetResourceLFTagsResponseResponseTypeDef",
    {
        "LFTagOnDatabase": List["LFTagPairTypeDef"],
        "LFTagsOnTable": List["LFTagPairTypeDef"],
        "LFTagsOnColumns": List["ColumnLFTagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGrantPermissionsRequestTypeDef = TypedDict(
    "_RequiredGrantPermissionsRequestTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Resource": "ResourceTypeDef",
        "Permissions": List[PermissionType],
    },
)
_OptionalGrantPermissionsRequestTypeDef = TypedDict(
    "_OptionalGrantPermissionsRequestTypeDef",
    {
        "CatalogId": str,
        "PermissionsWithGrantOption": List[PermissionType],
    },
    total=False,
)


class GrantPermissionsRequestTypeDef(
    _RequiredGrantPermissionsRequestTypeDef, _OptionalGrantPermissionsRequestTypeDef
):
    pass


LFTagErrorTypeDef = TypedDict(
    "LFTagErrorTypeDef",
    {
        "LFTag": "LFTagPairTypeDef",
        "Error": "ErrorDetailTypeDef",
    },
    total=False,
)

_RequiredLFTagKeyResourceTypeDef = TypedDict(
    "_RequiredLFTagKeyResourceTypeDef",
    {
        "TagKey": str,
        "TagValues": List[str],
    },
)
_OptionalLFTagKeyResourceTypeDef = TypedDict(
    "_OptionalLFTagKeyResourceTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class LFTagKeyResourceTypeDef(_RequiredLFTagKeyResourceTypeDef, _OptionalLFTagKeyResourceTypeDef):
    pass


_RequiredLFTagPairTypeDef = TypedDict(
    "_RequiredLFTagPairTypeDef",
    {
        "TagKey": str,
        "TagValues": List[str],
    },
)
_OptionalLFTagPairTypeDef = TypedDict(
    "_OptionalLFTagPairTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class LFTagPairTypeDef(_RequiredLFTagPairTypeDef, _OptionalLFTagPairTypeDef):
    pass


_RequiredLFTagPolicyResourceTypeDef = TypedDict(
    "_RequiredLFTagPolicyResourceTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "Expression": List["LFTagTypeDef"],
    },
)
_OptionalLFTagPolicyResourceTypeDef = TypedDict(
    "_OptionalLFTagPolicyResourceTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class LFTagPolicyResourceTypeDef(
    _RequiredLFTagPolicyResourceTypeDef, _OptionalLFTagPolicyResourceTypeDef
):
    pass


LFTagTypeDef = TypedDict(
    "LFTagTypeDef",
    {
        "TagKey": str,
        "TagValues": List[str],
    },
)

ListLFTagsRequestTypeDef = TypedDict(
    "ListLFTagsRequestTypeDef",
    {
        "CatalogId": str,
        "ResourceShareType": ResourceShareTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListLFTagsResponseResponseTypeDef = TypedDict(
    "ListLFTagsResponseResponseTypeDef",
    {
        "LFTags": List["LFTagPairTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPermissionsRequestTypeDef = TypedDict(
    "ListPermissionsRequestTypeDef",
    {
        "CatalogId": str,
        "Principal": "DataLakePrincipalTypeDef",
        "ResourceType": DataLakeResourceTypeType,
        "Resource": "ResourceTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPermissionsResponseResponseTypeDef = TypedDict(
    "ListPermissionsResponseResponseTypeDef",
    {
        "PrincipalResourcePermissions": List["PrincipalResourcePermissionsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourcesRequestTypeDef = TypedDict(
    "ListResourcesRequestTypeDef",
    {
        "FilterConditionList": List["FilterConditionTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListResourcesResponseResponseTypeDef = TypedDict(
    "ListResourcesResponseResponseTypeDef",
    {
        "ResourceInfoList": List["ResourceInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PrincipalPermissionsTypeDef = TypedDict(
    "PrincipalPermissionsTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Permissions": List[PermissionType],
    },
    total=False,
)

PrincipalResourcePermissionsTypeDef = TypedDict(
    "PrincipalResourcePermissionsTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Resource": "ResourceTypeDef",
        "Permissions": List[PermissionType],
        "PermissionsWithGrantOption": List[PermissionType],
        "AdditionalDetails": "DetailsMapTypeDef",
    },
    total=False,
)

_RequiredPutDataLakeSettingsRequestTypeDef = TypedDict(
    "_RequiredPutDataLakeSettingsRequestTypeDef",
    {
        "DataLakeSettings": "DataLakeSettingsTypeDef",
    },
)
_OptionalPutDataLakeSettingsRequestTypeDef = TypedDict(
    "_OptionalPutDataLakeSettingsRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class PutDataLakeSettingsRequestTypeDef(
    _RequiredPutDataLakeSettingsRequestTypeDef, _OptionalPutDataLakeSettingsRequestTypeDef
):
    pass


_RequiredRegisterResourceRequestTypeDef = TypedDict(
    "_RequiredRegisterResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalRegisterResourceRequestTypeDef = TypedDict(
    "_OptionalRegisterResourceRequestTypeDef",
    {
        "UseServiceLinkedRole": bool,
        "RoleArn": str,
    },
    total=False,
)


class RegisterResourceRequestTypeDef(
    _RequiredRegisterResourceRequestTypeDef, _OptionalRegisterResourceRequestTypeDef
):
    pass


_RequiredRemoveLFTagsFromResourceRequestTypeDef = TypedDict(
    "_RequiredRemoveLFTagsFromResourceRequestTypeDef",
    {
        "Resource": "ResourceTypeDef",
        "LFTags": List["LFTagPairTypeDef"],
    },
)
_OptionalRemoveLFTagsFromResourceRequestTypeDef = TypedDict(
    "_OptionalRemoveLFTagsFromResourceRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class RemoveLFTagsFromResourceRequestTypeDef(
    _RequiredRemoveLFTagsFromResourceRequestTypeDef, _OptionalRemoveLFTagsFromResourceRequestTypeDef
):
    pass


RemoveLFTagsFromResourceResponseResponseTypeDef = TypedDict(
    "RemoveLFTagsFromResourceResponseResponseTypeDef",
    {
        "Failures": List["LFTagErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceInfoTypeDef = TypedDict(
    "ResourceInfoTypeDef",
    {
        "ResourceArn": str,
        "RoleArn": str,
        "LastModified": datetime,
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": "DatabaseResourceTypeDef",
        "Table": "TableResourceTypeDef",
        "TableWithColumns": "TableWithColumnsResourceTypeDef",
        "DataLocation": "DataLocationResourceTypeDef",
        "LFTag": "LFTagKeyResourceTypeDef",
        "LFTagPolicy": "LFTagPolicyResourceTypeDef",
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

_RequiredRevokePermissionsRequestTypeDef = TypedDict(
    "_RequiredRevokePermissionsRequestTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Resource": "ResourceTypeDef",
        "Permissions": List[PermissionType],
    },
)
_OptionalRevokePermissionsRequestTypeDef = TypedDict(
    "_OptionalRevokePermissionsRequestTypeDef",
    {
        "CatalogId": str,
        "PermissionsWithGrantOption": List[PermissionType],
    },
    total=False,
)


class RevokePermissionsRequestTypeDef(
    _RequiredRevokePermissionsRequestTypeDef, _OptionalRevokePermissionsRequestTypeDef
):
    pass


_RequiredSearchDatabasesByLFTagsRequestTypeDef = TypedDict(
    "_RequiredSearchDatabasesByLFTagsRequestTypeDef",
    {
        "Expression": List["LFTagTypeDef"],
    },
)
_OptionalSearchDatabasesByLFTagsRequestTypeDef = TypedDict(
    "_OptionalSearchDatabasesByLFTagsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CatalogId": str,
    },
    total=False,
)


class SearchDatabasesByLFTagsRequestTypeDef(
    _RequiredSearchDatabasesByLFTagsRequestTypeDef, _OptionalSearchDatabasesByLFTagsRequestTypeDef
):
    pass


SearchDatabasesByLFTagsResponseResponseTypeDef = TypedDict(
    "SearchDatabasesByLFTagsResponseResponseTypeDef",
    {
        "NextToken": str,
        "DatabaseList": List["TaggedDatabaseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchTablesByLFTagsRequestTypeDef = TypedDict(
    "_RequiredSearchTablesByLFTagsRequestTypeDef",
    {
        "Expression": List["LFTagTypeDef"],
    },
)
_OptionalSearchTablesByLFTagsRequestTypeDef = TypedDict(
    "_OptionalSearchTablesByLFTagsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CatalogId": str,
    },
    total=False,
)


class SearchTablesByLFTagsRequestTypeDef(
    _RequiredSearchTablesByLFTagsRequestTypeDef, _OptionalSearchTablesByLFTagsRequestTypeDef
):
    pass


SearchTablesByLFTagsResponseResponseTypeDef = TypedDict(
    "SearchTablesByLFTagsResponseResponseTypeDef",
    {
        "NextToken": str,
        "TableList": List["TaggedTableTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTableResourceTypeDef = TypedDict(
    "_RequiredTableResourceTypeDef",
    {
        "DatabaseName": str,
    },
)
_OptionalTableResourceTypeDef = TypedDict(
    "_OptionalTableResourceTypeDef",
    {
        "CatalogId": str,
        "Name": str,
        "TableWildcard": Dict[str, Any],
    },
    total=False,
)


class TableResourceTypeDef(_RequiredTableResourceTypeDef, _OptionalTableResourceTypeDef):
    pass


_RequiredTableWithColumnsResourceTypeDef = TypedDict(
    "_RequiredTableWithColumnsResourceTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
    },
)
_OptionalTableWithColumnsResourceTypeDef = TypedDict(
    "_OptionalTableWithColumnsResourceTypeDef",
    {
        "CatalogId": str,
        "ColumnNames": List[str],
        "ColumnWildcard": "ColumnWildcardTypeDef",
    },
    total=False,
)


class TableWithColumnsResourceTypeDef(
    _RequiredTableWithColumnsResourceTypeDef, _OptionalTableWithColumnsResourceTypeDef
):
    pass


TaggedDatabaseTypeDef = TypedDict(
    "TaggedDatabaseTypeDef",
    {
        "Database": "DatabaseResourceTypeDef",
        "LFTags": List["LFTagPairTypeDef"],
    },
    total=False,
)

TaggedTableTypeDef = TypedDict(
    "TaggedTableTypeDef",
    {
        "Table": "TableResourceTypeDef",
        "LFTagOnDatabase": List["LFTagPairTypeDef"],
        "LFTagsOnTable": List["LFTagPairTypeDef"],
        "LFTagsOnColumns": List["ColumnLFTagTypeDef"],
    },
    total=False,
)

_RequiredUpdateLFTagRequestTypeDef = TypedDict(
    "_RequiredUpdateLFTagRequestTypeDef",
    {
        "TagKey": str,
    },
)
_OptionalUpdateLFTagRequestTypeDef = TypedDict(
    "_OptionalUpdateLFTagRequestTypeDef",
    {
        "CatalogId": str,
        "TagValuesToDelete": List[str],
        "TagValuesToAdd": List[str],
    },
    total=False,
)


class UpdateLFTagRequestTypeDef(
    _RequiredUpdateLFTagRequestTypeDef, _OptionalUpdateLFTagRequestTypeDef
):
    pass


UpdateResourceRequestTypeDef = TypedDict(
    "UpdateResourceRequestTypeDef",
    {
        "RoleArn": str,
        "ResourceArn": str,
    },
)
