"""
Type annotations for lakeformation service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lakeformation.type_defs import AddLFTagsToResourceResponseTypeDef

    data: AddLFTagsToResourceResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import ComparisonOperatorType, FieldNameStringType, PermissionType, ResourceTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddLFTagsToResourceResponseTypeDef",
    "BatchGrantPermissionsResponseTypeDef",
    "BatchPermissionsFailureEntryTypeDef",
    "BatchPermissionsRequestEntryTypeDef",
    "BatchRevokePermissionsResponseTypeDef",
    "ColumnLFTagTypeDef",
    "ColumnWildcardTypeDef",
    "DataLakePrincipalTypeDef",
    "DataLakeSettingsTypeDef",
    "DataLocationResourceTypeDef",
    "DatabaseResourceTypeDef",
    "DescribeResourceResponseTypeDef",
    "DetailsMapTypeDef",
    "ErrorDetailTypeDef",
    "FilterConditionTypeDef",
    "GetDataLakeSettingsResponseTypeDef",
    "GetEffectivePermissionsForPathResponseTypeDef",
    "GetLFTagResponseTypeDef",
    "GetResourceLFTagsResponseTypeDef",
    "LFTagErrorTypeDef",
    "LFTagKeyResourceTypeDef",
    "LFTagPairTypeDef",
    "LFTagPolicyResourceTypeDef",
    "LFTagTypeDef",
    "ListLFTagsResponseTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListResourcesResponseTypeDef",
    "PrincipalPermissionsTypeDef",
    "PrincipalResourcePermissionsTypeDef",
    "RemoveLFTagsFromResourceResponseTypeDef",
    "ResourceInfoTypeDef",
    "ResourceTypeDef",
    "SearchDatabasesByLFTagsResponseTypeDef",
    "SearchTablesByLFTagsResponseTypeDef",
    "TableResourceTypeDef",
    "TableWithColumnsResourceTypeDef",
    "TaggedDatabaseTypeDef",
    "TaggedTableTypeDef",
)

AddLFTagsToResourceResponseTypeDef = TypedDict(
    "AddLFTagsToResourceResponseTypeDef",
    {
        "Failures": List["LFTagErrorTypeDef"],
    },
    total=False,
)

BatchGrantPermissionsResponseTypeDef = TypedDict(
    "BatchGrantPermissionsResponseTypeDef",
    {
        "Failures": List["BatchPermissionsFailureEntryTypeDef"],
    },
    total=False,
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


BatchRevokePermissionsResponseTypeDef = TypedDict(
    "BatchRevokePermissionsResponseTypeDef",
    {
        "Failures": List["BatchPermissionsFailureEntryTypeDef"],
    },
    total=False,
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


DescribeResourceResponseTypeDef = TypedDict(
    "DescribeResourceResponseTypeDef",
    {
        "ResourceInfo": "ResourceInfoTypeDef",
    },
    total=False,
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

GetDataLakeSettingsResponseTypeDef = TypedDict(
    "GetDataLakeSettingsResponseTypeDef",
    {
        "DataLakeSettings": "DataLakeSettingsTypeDef",
    },
    total=False,
)

GetEffectivePermissionsForPathResponseTypeDef = TypedDict(
    "GetEffectivePermissionsForPathResponseTypeDef",
    {
        "Permissions": List["PrincipalResourcePermissionsTypeDef"],
        "NextToken": str,
    },
    total=False,
)

GetLFTagResponseTypeDef = TypedDict(
    "GetLFTagResponseTypeDef",
    {
        "CatalogId": str,
        "TagKey": str,
        "TagValues": List[str],
    },
    total=False,
)

GetResourceLFTagsResponseTypeDef = TypedDict(
    "GetResourceLFTagsResponseTypeDef",
    {
        "LFTagOnDatabase": List["LFTagPairTypeDef"],
        "LFTagsOnTable": List["LFTagPairTypeDef"],
        "LFTagsOnColumns": List["ColumnLFTagTypeDef"],
    },
    total=False,
)

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

ListLFTagsResponseTypeDef = TypedDict(
    "ListLFTagsResponseTypeDef",
    {
        "LFTags": List["LFTagPairTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {
        "PrincipalResourcePermissions": List["PrincipalResourcePermissionsTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListResourcesResponseTypeDef = TypedDict(
    "ListResourcesResponseTypeDef",
    {
        "ResourceInfoList": List["ResourceInfoTypeDef"],
        "NextToken": str,
    },
    total=False,
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

RemoveLFTagsFromResourceResponseTypeDef = TypedDict(
    "RemoveLFTagsFromResourceResponseTypeDef",
    {
        "Failures": List["LFTagErrorTypeDef"],
    },
    total=False,
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

SearchDatabasesByLFTagsResponseTypeDef = TypedDict(
    "SearchDatabasesByLFTagsResponseTypeDef",
    {
        "NextToken": str,
        "DatabaseList": List["TaggedDatabaseTypeDef"],
    },
    total=False,
)

SearchTablesByLFTagsResponseTypeDef = TypedDict(
    "SearchTablesByLFTagsResponseTypeDef",
    {
        "NextToken": str,
        "TableList": List["TaggedTableTypeDef"],
    },
    total=False,
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
