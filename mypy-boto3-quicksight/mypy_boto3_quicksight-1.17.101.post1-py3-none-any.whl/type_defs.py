"""
Type annotations for quicksight service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/type_defs.html)

Usage::

    ```python
    from mypy_boto3_quicksight.type_defs import AccountCustomizationTypeDef

    data: AccountCustomizationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AnalysisErrorTypeType,
    AssignmentStatusType,
    ColumnDataTypeType,
    DashboardBehaviorType,
    DashboardErrorTypeType,
    DashboardUIStateType,
    DataSetImportModeType,
    DataSourceErrorInfoTypeType,
    DataSourceTypeType,
    EditionType,
    EmbeddingIdentityTypeType,
    FileFormatType,
    GeoSpatialDataRoleType,
    IdentityTypeType,
    IngestionErrorTypeType,
    IngestionRequestSourceType,
    IngestionRequestTypeType,
    IngestionStatusType,
    InputColumnDataTypeType,
    JoinTypeType,
    MemberTypeType,
    NamespaceErrorTypeType,
    NamespaceStatusType,
    ResourceStatusType,
    RowLevelPermissionFormatVersionType,
    RowLevelPermissionPolicyType,
    TemplateErrorTypeType,
    TextQualifierType,
    ThemeTypeType,
    UserRoleType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountCustomizationTypeDef",
    "AccountSettingsTypeDef",
    "ActiveIAMPolicyAssignmentTypeDef",
    "AdHocFilteringOptionTypeDef",
    "AmazonElasticsearchParametersTypeDef",
    "AnalysisErrorTypeDef",
    "AnalysisSearchFilterTypeDef",
    "AnalysisSourceEntityTypeDef",
    "AnalysisSourceTemplateTypeDef",
    "AnalysisSummaryTypeDef",
    "AnalysisTypeDef",
    "AthenaParametersTypeDef",
    "AuroraParametersTypeDef",
    "AuroraPostgreSqlParametersTypeDef",
    "AwsIotAnalyticsParametersTypeDef",
    "BorderStyleTypeDef",
    "CalculatedColumnTypeDef",
    "CancelIngestionRequestTypeDef",
    "CancelIngestionResponseResponseTypeDef",
    "CastColumnTypeOperationTypeDef",
    "ColumnDescriptionTypeDef",
    "ColumnGroupColumnSchemaTypeDef",
    "ColumnGroupSchemaTypeDef",
    "ColumnGroupTypeDef",
    "ColumnLevelPermissionRuleTypeDef",
    "ColumnSchemaTypeDef",
    "ColumnTagTypeDef",
    "CreateAccountCustomizationRequestTypeDef",
    "CreateAccountCustomizationResponseResponseTypeDef",
    "CreateAnalysisRequestTypeDef",
    "CreateAnalysisResponseResponseTypeDef",
    "CreateColumnsOperationTypeDef",
    "CreateDashboardRequestTypeDef",
    "CreateDashboardResponseResponseTypeDef",
    "CreateDataSetRequestTypeDef",
    "CreateDataSetResponseResponseTypeDef",
    "CreateDataSourceRequestTypeDef",
    "CreateDataSourceResponseResponseTypeDef",
    "CreateFolderMembershipRequestTypeDef",
    "CreateFolderMembershipResponseResponseTypeDef",
    "CreateFolderRequestTypeDef",
    "CreateFolderResponseResponseTypeDef",
    "CreateGroupMembershipRequestTypeDef",
    "CreateGroupMembershipResponseResponseTypeDef",
    "CreateGroupRequestTypeDef",
    "CreateGroupResponseResponseTypeDef",
    "CreateIAMPolicyAssignmentRequestTypeDef",
    "CreateIAMPolicyAssignmentResponseResponseTypeDef",
    "CreateIngestionRequestTypeDef",
    "CreateIngestionResponseResponseTypeDef",
    "CreateNamespaceRequestTypeDef",
    "CreateNamespaceResponseResponseTypeDef",
    "CreateTemplateAliasRequestTypeDef",
    "CreateTemplateAliasResponseResponseTypeDef",
    "CreateTemplateRequestTypeDef",
    "CreateTemplateResponseResponseTypeDef",
    "CreateThemeAliasRequestTypeDef",
    "CreateThemeAliasResponseResponseTypeDef",
    "CreateThemeRequestTypeDef",
    "CreateThemeResponseResponseTypeDef",
    "CredentialPairTypeDef",
    "CustomSqlTypeDef",
    "DashboardErrorTypeDef",
    "DashboardPublishOptionsTypeDef",
    "DashboardSearchFilterTypeDef",
    "DashboardSourceEntityTypeDef",
    "DashboardSourceTemplateTypeDef",
    "DashboardSummaryTypeDef",
    "DashboardTypeDef",
    "DashboardVersionSummaryTypeDef",
    "DashboardVersionTypeDef",
    "DataColorPaletteTypeDef",
    "DataSetConfigurationTypeDef",
    "DataSetReferenceTypeDef",
    "DataSetSchemaTypeDef",
    "DataSetSummaryTypeDef",
    "DataSetTypeDef",
    "DataSourceCredentialsTypeDef",
    "DataSourceErrorInfoTypeDef",
    "DataSourceParametersTypeDef",
    "DataSourceTypeDef",
    "DateTimeParameterTypeDef",
    "DecimalParameterTypeDef",
    "DeleteAccountCustomizationRequestTypeDef",
    "DeleteAccountCustomizationResponseResponseTypeDef",
    "DeleteAnalysisRequestTypeDef",
    "DeleteAnalysisResponseResponseTypeDef",
    "DeleteDashboardRequestTypeDef",
    "DeleteDashboardResponseResponseTypeDef",
    "DeleteDataSetRequestTypeDef",
    "DeleteDataSetResponseResponseTypeDef",
    "DeleteDataSourceRequestTypeDef",
    "DeleteDataSourceResponseResponseTypeDef",
    "DeleteFolderMembershipRequestTypeDef",
    "DeleteFolderMembershipResponseResponseTypeDef",
    "DeleteFolderRequestTypeDef",
    "DeleteFolderResponseResponseTypeDef",
    "DeleteGroupMembershipRequestTypeDef",
    "DeleteGroupMembershipResponseResponseTypeDef",
    "DeleteGroupRequestTypeDef",
    "DeleteGroupResponseResponseTypeDef",
    "DeleteIAMPolicyAssignmentRequestTypeDef",
    "DeleteIAMPolicyAssignmentResponseResponseTypeDef",
    "DeleteNamespaceRequestTypeDef",
    "DeleteNamespaceResponseResponseTypeDef",
    "DeleteTemplateAliasRequestTypeDef",
    "DeleteTemplateAliasResponseResponseTypeDef",
    "DeleteTemplateRequestTypeDef",
    "DeleteTemplateResponseResponseTypeDef",
    "DeleteThemeAliasRequestTypeDef",
    "DeleteThemeAliasResponseResponseTypeDef",
    "DeleteThemeRequestTypeDef",
    "DeleteThemeResponseResponseTypeDef",
    "DeleteUserByPrincipalIdRequestTypeDef",
    "DeleteUserByPrincipalIdResponseResponseTypeDef",
    "DeleteUserRequestTypeDef",
    "DeleteUserResponseResponseTypeDef",
    "DescribeAccountCustomizationRequestTypeDef",
    "DescribeAccountCustomizationResponseResponseTypeDef",
    "DescribeAccountSettingsRequestTypeDef",
    "DescribeAccountSettingsResponseResponseTypeDef",
    "DescribeAnalysisPermissionsRequestTypeDef",
    "DescribeAnalysisPermissionsResponseResponseTypeDef",
    "DescribeAnalysisRequestTypeDef",
    "DescribeAnalysisResponseResponseTypeDef",
    "DescribeDashboardPermissionsRequestTypeDef",
    "DescribeDashboardPermissionsResponseResponseTypeDef",
    "DescribeDashboardRequestTypeDef",
    "DescribeDashboardResponseResponseTypeDef",
    "DescribeDataSetPermissionsRequestTypeDef",
    "DescribeDataSetPermissionsResponseResponseTypeDef",
    "DescribeDataSetRequestTypeDef",
    "DescribeDataSetResponseResponseTypeDef",
    "DescribeDataSourcePermissionsRequestTypeDef",
    "DescribeDataSourcePermissionsResponseResponseTypeDef",
    "DescribeDataSourceRequestTypeDef",
    "DescribeDataSourceResponseResponseTypeDef",
    "DescribeFolderPermissionsRequestTypeDef",
    "DescribeFolderPermissionsResponseResponseTypeDef",
    "DescribeFolderRequestTypeDef",
    "DescribeFolderResolvedPermissionsRequestTypeDef",
    "DescribeFolderResolvedPermissionsResponseResponseTypeDef",
    "DescribeFolderResponseResponseTypeDef",
    "DescribeGroupRequestTypeDef",
    "DescribeGroupResponseResponseTypeDef",
    "DescribeIAMPolicyAssignmentRequestTypeDef",
    "DescribeIAMPolicyAssignmentResponseResponseTypeDef",
    "DescribeIngestionRequestTypeDef",
    "DescribeIngestionResponseResponseTypeDef",
    "DescribeNamespaceRequestTypeDef",
    "DescribeNamespaceResponseResponseTypeDef",
    "DescribeTemplateAliasRequestTypeDef",
    "DescribeTemplateAliasResponseResponseTypeDef",
    "DescribeTemplatePermissionsRequestTypeDef",
    "DescribeTemplatePermissionsResponseResponseTypeDef",
    "DescribeTemplateRequestTypeDef",
    "DescribeTemplateResponseResponseTypeDef",
    "DescribeThemeAliasRequestTypeDef",
    "DescribeThemeAliasResponseResponseTypeDef",
    "DescribeThemePermissionsRequestTypeDef",
    "DescribeThemePermissionsResponseResponseTypeDef",
    "DescribeThemeRequestTypeDef",
    "DescribeThemeResponseResponseTypeDef",
    "DescribeUserRequestTypeDef",
    "DescribeUserResponseResponseTypeDef",
    "ErrorInfoTypeDef",
    "ExportToCSVOptionTypeDef",
    "FieldFolderTypeDef",
    "FilterOperationTypeDef",
    "FolderMemberTypeDef",
    "FolderSearchFilterTypeDef",
    "FolderSummaryTypeDef",
    "FolderTypeDef",
    "GeoSpatialColumnGroupTypeDef",
    "GetDashboardEmbedUrlRequestTypeDef",
    "GetDashboardEmbedUrlResponseResponseTypeDef",
    "GetSessionEmbedUrlRequestTypeDef",
    "GetSessionEmbedUrlResponseResponseTypeDef",
    "GroupMemberTypeDef",
    "GroupTypeDef",
    "GutterStyleTypeDef",
    "IAMPolicyAssignmentSummaryTypeDef",
    "IAMPolicyAssignmentTypeDef",
    "IngestionTypeDef",
    "InputColumnTypeDef",
    "IntegerParameterTypeDef",
    "JiraParametersTypeDef",
    "JoinInstructionTypeDef",
    "JoinKeyPropertiesTypeDef",
    "ListAnalysesRequestTypeDef",
    "ListAnalysesResponseResponseTypeDef",
    "ListDashboardVersionsRequestTypeDef",
    "ListDashboardVersionsResponseResponseTypeDef",
    "ListDashboardsRequestTypeDef",
    "ListDashboardsResponseResponseTypeDef",
    "ListDataSetsRequestTypeDef",
    "ListDataSetsResponseResponseTypeDef",
    "ListDataSourcesRequestTypeDef",
    "ListDataSourcesResponseResponseTypeDef",
    "ListFolderMembersRequestTypeDef",
    "ListFolderMembersResponseResponseTypeDef",
    "ListFoldersRequestTypeDef",
    "ListFoldersResponseResponseTypeDef",
    "ListGroupMembershipsRequestTypeDef",
    "ListGroupMembershipsResponseResponseTypeDef",
    "ListGroupsRequestTypeDef",
    "ListGroupsResponseResponseTypeDef",
    "ListIAMPolicyAssignmentsForUserRequestTypeDef",
    "ListIAMPolicyAssignmentsForUserResponseResponseTypeDef",
    "ListIAMPolicyAssignmentsRequestTypeDef",
    "ListIAMPolicyAssignmentsResponseResponseTypeDef",
    "ListIngestionsRequestTypeDef",
    "ListIngestionsResponseResponseTypeDef",
    "ListNamespacesRequestTypeDef",
    "ListNamespacesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTemplateAliasesRequestTypeDef",
    "ListTemplateAliasesResponseResponseTypeDef",
    "ListTemplateVersionsRequestTypeDef",
    "ListTemplateVersionsResponseResponseTypeDef",
    "ListTemplatesRequestTypeDef",
    "ListTemplatesResponseResponseTypeDef",
    "ListThemeAliasesRequestTypeDef",
    "ListThemeAliasesResponseResponseTypeDef",
    "ListThemeVersionsRequestTypeDef",
    "ListThemeVersionsResponseResponseTypeDef",
    "ListThemesRequestTypeDef",
    "ListThemesResponseResponseTypeDef",
    "ListUserGroupsRequestTypeDef",
    "ListUserGroupsResponseResponseTypeDef",
    "ListUsersRequestTypeDef",
    "ListUsersResponseResponseTypeDef",
    "LogicalTableSourceTypeDef",
    "LogicalTableTypeDef",
    "ManifestFileLocationTypeDef",
    "MarginStyleTypeDef",
    "MariaDbParametersTypeDef",
    "MemberIdArnPairTypeDef",
    "MySqlParametersTypeDef",
    "NamespaceErrorTypeDef",
    "NamespaceInfoV2TypeDef",
    "OracleParametersTypeDef",
    "OutputColumnTypeDef",
    "PaginatorConfigTypeDef",
    "ParametersTypeDef",
    "PhysicalTableTypeDef",
    "PostgreSqlParametersTypeDef",
    "PrestoParametersTypeDef",
    "ProjectOperationTypeDef",
    "QueueInfoTypeDef",
    "RdsParametersTypeDef",
    "RedshiftParametersTypeDef",
    "RegisterUserRequestTypeDef",
    "RegisterUserResponseResponseTypeDef",
    "RelationalTableTypeDef",
    "RenameColumnOperationTypeDef",
    "ResourcePermissionTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreAnalysisRequestTypeDef",
    "RestoreAnalysisResponseResponseTypeDef",
    "RowInfoTypeDef",
    "RowLevelPermissionDataSetTypeDef",
    "S3ParametersTypeDef",
    "S3SourceTypeDef",
    "SearchAnalysesRequestTypeDef",
    "SearchAnalysesResponseResponseTypeDef",
    "SearchDashboardsRequestTypeDef",
    "SearchDashboardsResponseResponseTypeDef",
    "SearchFoldersRequestTypeDef",
    "SearchFoldersResponseResponseTypeDef",
    "ServiceNowParametersTypeDef",
    "SheetControlsOptionTypeDef",
    "SheetStyleTypeDef",
    "SheetTypeDef",
    "SnowflakeParametersTypeDef",
    "SparkParametersTypeDef",
    "SqlServerParametersTypeDef",
    "SslPropertiesTypeDef",
    "StringParameterTypeDef",
    "TagColumnOperationTypeDef",
    "TagResourceRequestTypeDef",
    "TagResourceResponseResponseTypeDef",
    "TagTypeDef",
    "TemplateAliasTypeDef",
    "TemplateErrorTypeDef",
    "TemplateSourceAnalysisTypeDef",
    "TemplateSourceEntityTypeDef",
    "TemplateSourceTemplateTypeDef",
    "TemplateSummaryTypeDef",
    "TemplateTypeDef",
    "TemplateVersionSummaryTypeDef",
    "TemplateVersionTypeDef",
    "TeradataParametersTypeDef",
    "ThemeAliasTypeDef",
    "ThemeConfigurationTypeDef",
    "ThemeErrorTypeDef",
    "ThemeSummaryTypeDef",
    "ThemeTypeDef",
    "ThemeVersionSummaryTypeDef",
    "ThemeVersionTypeDef",
    "TileLayoutStyleTypeDef",
    "TileStyleTypeDef",
    "TransformOperationTypeDef",
    "TwitterParametersTypeDef",
    "UIColorPaletteTypeDef",
    "UntagResourceRequestTypeDef",
    "UntagResourceResponseResponseTypeDef",
    "UpdateAccountCustomizationRequestTypeDef",
    "UpdateAccountCustomizationResponseResponseTypeDef",
    "UpdateAccountSettingsRequestTypeDef",
    "UpdateAccountSettingsResponseResponseTypeDef",
    "UpdateAnalysisPermissionsRequestTypeDef",
    "UpdateAnalysisPermissionsResponseResponseTypeDef",
    "UpdateAnalysisRequestTypeDef",
    "UpdateAnalysisResponseResponseTypeDef",
    "UpdateDashboardPermissionsRequestTypeDef",
    "UpdateDashboardPermissionsResponseResponseTypeDef",
    "UpdateDashboardPublishedVersionRequestTypeDef",
    "UpdateDashboardPublishedVersionResponseResponseTypeDef",
    "UpdateDashboardRequestTypeDef",
    "UpdateDashboardResponseResponseTypeDef",
    "UpdateDataSetPermissionsRequestTypeDef",
    "UpdateDataSetPermissionsResponseResponseTypeDef",
    "UpdateDataSetRequestTypeDef",
    "UpdateDataSetResponseResponseTypeDef",
    "UpdateDataSourcePermissionsRequestTypeDef",
    "UpdateDataSourcePermissionsResponseResponseTypeDef",
    "UpdateDataSourceRequestTypeDef",
    "UpdateDataSourceResponseResponseTypeDef",
    "UpdateFolderPermissionsRequestTypeDef",
    "UpdateFolderPermissionsResponseResponseTypeDef",
    "UpdateFolderRequestTypeDef",
    "UpdateFolderResponseResponseTypeDef",
    "UpdateGroupRequestTypeDef",
    "UpdateGroupResponseResponseTypeDef",
    "UpdateIAMPolicyAssignmentRequestTypeDef",
    "UpdateIAMPolicyAssignmentResponseResponseTypeDef",
    "UpdateTemplateAliasRequestTypeDef",
    "UpdateTemplateAliasResponseResponseTypeDef",
    "UpdateTemplatePermissionsRequestTypeDef",
    "UpdateTemplatePermissionsResponseResponseTypeDef",
    "UpdateTemplateRequestTypeDef",
    "UpdateTemplateResponseResponseTypeDef",
    "UpdateThemeAliasRequestTypeDef",
    "UpdateThemeAliasResponseResponseTypeDef",
    "UpdateThemePermissionsRequestTypeDef",
    "UpdateThemePermissionsResponseResponseTypeDef",
    "UpdateThemeRequestTypeDef",
    "UpdateThemeResponseResponseTypeDef",
    "UpdateUserRequestTypeDef",
    "UpdateUserResponseResponseTypeDef",
    "UploadSettingsTypeDef",
    "UserTypeDef",
    "VpcConnectionPropertiesTypeDef",
)

AccountCustomizationTypeDef = TypedDict(
    "AccountCustomizationTypeDef",
    {
        "DefaultTheme": str,
    },
    total=False,
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "AccountName": str,
        "Edition": EditionType,
        "DefaultNamespace": str,
        "NotificationEmail": str,
    },
    total=False,
)

ActiveIAMPolicyAssignmentTypeDef = TypedDict(
    "ActiveIAMPolicyAssignmentTypeDef",
    {
        "AssignmentName": str,
        "PolicyArn": str,
    },
    total=False,
)

AdHocFilteringOptionTypeDef = TypedDict(
    "AdHocFilteringOptionTypeDef",
    {
        "AvailabilityStatus": DashboardBehaviorType,
    },
    total=False,
)

AmazonElasticsearchParametersTypeDef = TypedDict(
    "AmazonElasticsearchParametersTypeDef",
    {
        "Domain": str,
    },
)

AnalysisErrorTypeDef = TypedDict(
    "AnalysisErrorTypeDef",
    {
        "Type": AnalysisErrorTypeType,
        "Message": str,
    },
    total=False,
)

AnalysisSearchFilterTypeDef = TypedDict(
    "AnalysisSearchFilterTypeDef",
    {
        "Operator": Literal["StringEquals"],
        "Name": Literal["QUICKSIGHT_USER"],
        "Value": str,
    },
    total=False,
)

AnalysisSourceEntityTypeDef = TypedDict(
    "AnalysisSourceEntityTypeDef",
    {
        "SourceTemplate": "AnalysisSourceTemplateTypeDef",
    },
    total=False,
)

AnalysisSourceTemplateTypeDef = TypedDict(
    "AnalysisSourceTemplateTypeDef",
    {
        "DataSetReferences": List["DataSetReferenceTypeDef"],
        "Arn": str,
    },
)

AnalysisSummaryTypeDef = TypedDict(
    "AnalysisSummaryTypeDef",
    {
        "Arn": str,
        "AnalysisId": str,
        "Name": str,
        "Status": ResourceStatusType,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

AnalysisTypeDef = TypedDict(
    "AnalysisTypeDef",
    {
        "AnalysisId": str,
        "Arn": str,
        "Name": str,
        "Status": ResourceStatusType,
        "Errors": List["AnalysisErrorTypeDef"],
        "DataSetArns": List[str],
        "ThemeArn": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "Sheets": List["SheetTypeDef"],
    },
    total=False,
)

AthenaParametersTypeDef = TypedDict(
    "AthenaParametersTypeDef",
    {
        "WorkGroup": str,
    },
    total=False,
)

AuroraParametersTypeDef = TypedDict(
    "AuroraParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

AuroraPostgreSqlParametersTypeDef = TypedDict(
    "AuroraPostgreSqlParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

AwsIotAnalyticsParametersTypeDef = TypedDict(
    "AwsIotAnalyticsParametersTypeDef",
    {
        "DataSetName": str,
    },
)

BorderStyleTypeDef = TypedDict(
    "BorderStyleTypeDef",
    {
        "Show": bool,
    },
    total=False,
)

CalculatedColumnTypeDef = TypedDict(
    "CalculatedColumnTypeDef",
    {
        "ColumnName": str,
        "ColumnId": str,
        "Expression": str,
    },
)

CancelIngestionRequestTypeDef = TypedDict(
    "CancelIngestionRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "IngestionId": str,
    },
)

CancelIngestionResponseResponseTypeDef = TypedDict(
    "CancelIngestionResponseResponseTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCastColumnTypeOperationTypeDef = TypedDict(
    "_RequiredCastColumnTypeOperationTypeDef",
    {
        "ColumnName": str,
        "NewColumnType": ColumnDataTypeType,
    },
)
_OptionalCastColumnTypeOperationTypeDef = TypedDict(
    "_OptionalCastColumnTypeOperationTypeDef",
    {
        "Format": str,
    },
    total=False,
)


class CastColumnTypeOperationTypeDef(
    _RequiredCastColumnTypeOperationTypeDef, _OptionalCastColumnTypeOperationTypeDef
):
    pass


ColumnDescriptionTypeDef = TypedDict(
    "ColumnDescriptionTypeDef",
    {
        "Text": str,
    },
    total=False,
)

ColumnGroupColumnSchemaTypeDef = TypedDict(
    "ColumnGroupColumnSchemaTypeDef",
    {
        "Name": str,
    },
    total=False,
)

ColumnGroupSchemaTypeDef = TypedDict(
    "ColumnGroupSchemaTypeDef",
    {
        "Name": str,
        "ColumnGroupColumnSchemaList": List["ColumnGroupColumnSchemaTypeDef"],
    },
    total=False,
)

ColumnGroupTypeDef = TypedDict(
    "ColumnGroupTypeDef",
    {
        "GeoSpatialColumnGroup": "GeoSpatialColumnGroupTypeDef",
    },
    total=False,
)

ColumnLevelPermissionRuleTypeDef = TypedDict(
    "ColumnLevelPermissionRuleTypeDef",
    {
        "Principals": List[str],
        "ColumnNames": List[str],
    },
    total=False,
)

ColumnSchemaTypeDef = TypedDict(
    "ColumnSchemaTypeDef",
    {
        "Name": str,
        "DataType": str,
        "GeographicRole": str,
    },
    total=False,
)

ColumnTagTypeDef = TypedDict(
    "ColumnTagTypeDef",
    {
        "ColumnGeographicRole": GeoSpatialDataRoleType,
        "ColumnDescription": "ColumnDescriptionTypeDef",
    },
    total=False,
)

_RequiredCreateAccountCustomizationRequestTypeDef = TypedDict(
    "_RequiredCreateAccountCustomizationRequestTypeDef",
    {
        "AwsAccountId": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
    },
)
_OptionalCreateAccountCustomizationRequestTypeDef = TypedDict(
    "_OptionalCreateAccountCustomizationRequestTypeDef",
    {
        "Namespace": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateAccountCustomizationRequestTypeDef(
    _RequiredCreateAccountCustomizationRequestTypeDef,
    _OptionalCreateAccountCustomizationRequestTypeDef,
):
    pass


CreateAccountCustomizationResponseResponseTypeDef = TypedDict(
    "CreateAccountCustomizationResponseResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAnalysisRequestTypeDef = TypedDict(
    "_RequiredCreateAnalysisRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
        "Name": str,
        "SourceEntity": "AnalysisSourceEntityTypeDef",
    },
)
_OptionalCreateAnalysisRequestTypeDef = TypedDict(
    "_OptionalCreateAnalysisRequestTypeDef",
    {
        "Parameters": "ParametersTypeDef",
        "Permissions": List["ResourcePermissionTypeDef"],
        "ThemeArn": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateAnalysisRequestTypeDef(
    _RequiredCreateAnalysisRequestTypeDef, _OptionalCreateAnalysisRequestTypeDef
):
    pass


CreateAnalysisResponseResponseTypeDef = TypedDict(
    "CreateAnalysisResponseResponseTypeDef",
    {
        "Arn": str,
        "AnalysisId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateColumnsOperationTypeDef = TypedDict(
    "CreateColumnsOperationTypeDef",
    {
        "Columns": List["CalculatedColumnTypeDef"],
    },
)

_RequiredCreateDashboardRequestTypeDef = TypedDict(
    "_RequiredCreateDashboardRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "Name": str,
        "SourceEntity": "DashboardSourceEntityTypeDef",
    },
)
_OptionalCreateDashboardRequestTypeDef = TypedDict(
    "_OptionalCreateDashboardRequestTypeDef",
    {
        "Parameters": "ParametersTypeDef",
        "Permissions": List["ResourcePermissionTypeDef"],
        "Tags": List["TagTypeDef"],
        "VersionDescription": str,
        "DashboardPublishOptions": "DashboardPublishOptionsTypeDef",
        "ThemeArn": str,
    },
    total=False,
)


class CreateDashboardRequestTypeDef(
    _RequiredCreateDashboardRequestTypeDef, _OptionalCreateDashboardRequestTypeDef
):
    pass


CreateDashboardResponseResponseTypeDef = TypedDict(
    "CreateDashboardResponseResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "DashboardId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSetRequestTypeDef = TypedDict(
    "_RequiredCreateDataSetRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "Name": str,
        "PhysicalTableMap": Dict[str, "PhysicalTableTypeDef"],
        "ImportMode": DataSetImportModeType,
    },
)
_OptionalCreateDataSetRequestTypeDef = TypedDict(
    "_OptionalCreateDataSetRequestTypeDef",
    {
        "LogicalTableMap": Dict[str, "LogicalTableTypeDef"],
        "ColumnGroups": List["ColumnGroupTypeDef"],
        "FieldFolders": Dict[str, "FieldFolderTypeDef"],
        "Permissions": List["ResourcePermissionTypeDef"],
        "RowLevelPermissionDataSet": "RowLevelPermissionDataSetTypeDef",
        "ColumnLevelPermissionRules": List["ColumnLevelPermissionRuleTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDataSetRequestTypeDef(
    _RequiredCreateDataSetRequestTypeDef, _OptionalCreateDataSetRequestTypeDef
):
    pass


CreateDataSetResponseResponseTypeDef = TypedDict(
    "CreateDataSetResponseResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "IngestionArn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSourceRequestTypeDef = TypedDict(
    "_RequiredCreateDataSourceRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
        "Name": str,
        "Type": DataSourceTypeType,
    },
)
_OptionalCreateDataSourceRequestTypeDef = TypedDict(
    "_OptionalCreateDataSourceRequestTypeDef",
    {
        "DataSourceParameters": "DataSourceParametersTypeDef",
        "Credentials": "DataSourceCredentialsTypeDef",
        "Permissions": List["ResourcePermissionTypeDef"],
        "VpcConnectionProperties": "VpcConnectionPropertiesTypeDef",
        "SslProperties": "SslPropertiesTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDataSourceRequestTypeDef(
    _RequiredCreateDataSourceRequestTypeDef, _OptionalCreateDataSourceRequestTypeDef
):
    pass


CreateDataSourceResponseResponseTypeDef = TypedDict(
    "CreateDataSourceResponseResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "CreationStatus": ResourceStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFolderMembershipRequestTypeDef = TypedDict(
    "CreateFolderMembershipRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "MemberId": str,
        "MemberType": MemberTypeType,
    },
)

CreateFolderMembershipResponseResponseTypeDef = TypedDict(
    "CreateFolderMembershipResponseResponseTypeDef",
    {
        "Status": int,
        "FolderMember": "FolderMemberTypeDef",
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFolderRequestTypeDef = TypedDict(
    "_RequiredCreateFolderRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)
_OptionalCreateFolderRequestTypeDef = TypedDict(
    "_OptionalCreateFolderRequestTypeDef",
    {
        "Name": str,
        "FolderType": Literal["SHARED"],
        "ParentFolderArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateFolderRequestTypeDef(
    _RequiredCreateFolderRequestTypeDef, _OptionalCreateFolderRequestTypeDef
):
    pass


CreateFolderResponseResponseTypeDef = TypedDict(
    "CreateFolderResponseResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGroupMembershipRequestTypeDef = TypedDict(
    "CreateGroupMembershipRequestTypeDef",
    {
        "MemberName": str,
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

CreateGroupMembershipResponseResponseTypeDef = TypedDict(
    "CreateGroupMembershipResponseResponseTypeDef",
    {
        "GroupMember": "GroupMemberTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGroupRequestTypeDef = TypedDict(
    "_RequiredCreateGroupRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalCreateGroupRequestTypeDef = TypedDict(
    "_OptionalCreateGroupRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class CreateGroupRequestTypeDef(
    _RequiredCreateGroupRequestTypeDef, _OptionalCreateGroupRequestTypeDef
):
    pass


CreateGroupResponseResponseTypeDef = TypedDict(
    "CreateGroupResponseResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIAMPolicyAssignmentRequestTypeDef = TypedDict(
    "_RequiredCreateIAMPolicyAssignmentRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "AssignmentStatus": AssignmentStatusType,
        "Namespace": str,
    },
)
_OptionalCreateIAMPolicyAssignmentRequestTypeDef = TypedDict(
    "_OptionalCreateIAMPolicyAssignmentRequestTypeDef",
    {
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
    },
    total=False,
)


class CreateIAMPolicyAssignmentRequestTypeDef(
    _RequiredCreateIAMPolicyAssignmentRequestTypeDef,
    _OptionalCreateIAMPolicyAssignmentRequestTypeDef,
):
    pass


CreateIAMPolicyAssignmentResponseResponseTypeDef = TypedDict(
    "CreateIAMPolicyAssignmentResponseResponseTypeDef",
    {
        "AssignmentName": str,
        "AssignmentId": str,
        "AssignmentStatus": AssignmentStatusType,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIngestionRequestTypeDef = TypedDict(
    "CreateIngestionRequestTypeDef",
    {
        "DataSetId": str,
        "IngestionId": str,
        "AwsAccountId": str,
    },
)

CreateIngestionResponseResponseTypeDef = TypedDict(
    "CreateIngestionResponseResponseTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "IngestionStatus": IngestionStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNamespaceRequestTypeDef = TypedDict(
    "_RequiredCreateNamespaceRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "IdentityStore": Literal["QUICKSIGHT"],
    },
)
_OptionalCreateNamespaceRequestTypeDef = TypedDict(
    "_OptionalCreateNamespaceRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateNamespaceRequestTypeDef(
    _RequiredCreateNamespaceRequestTypeDef, _OptionalCreateNamespaceRequestTypeDef
):
    pass


CreateNamespaceResponseResponseTypeDef = TypedDict(
    "CreateNamespaceResponseResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "CapacityRegion": str,
        "CreationStatus": NamespaceStatusType,
        "IdentityStore": Literal["QUICKSIGHT"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTemplateAliasRequestTypeDef = TypedDict(
    "CreateTemplateAliasRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
        "TemplateVersionNumber": int,
    },
)

CreateTemplateAliasResponseResponseTypeDef = TypedDict(
    "CreateTemplateAliasResponseResponseTypeDef",
    {
        "TemplateAlias": "TemplateAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTemplateRequestTypeDef = TypedDict(
    "_RequiredCreateTemplateRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "SourceEntity": "TemplateSourceEntityTypeDef",
    },
)
_OptionalCreateTemplateRequestTypeDef = TypedDict(
    "_OptionalCreateTemplateRequestTypeDef",
    {
        "Name": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "Tags": List["TagTypeDef"],
        "VersionDescription": str,
    },
    total=False,
)


class CreateTemplateRequestTypeDef(
    _RequiredCreateTemplateRequestTypeDef, _OptionalCreateTemplateRequestTypeDef
):
    pass


CreateTemplateResponseResponseTypeDef = TypedDict(
    "CreateTemplateResponseResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "TemplateId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateThemeAliasRequestTypeDef = TypedDict(
    "CreateThemeAliasRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
        "ThemeVersionNumber": int,
    },
)

CreateThemeAliasResponseResponseTypeDef = TypedDict(
    "CreateThemeAliasResponseResponseTypeDef",
    {
        "ThemeAlias": "ThemeAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateThemeRequestTypeDef = TypedDict(
    "_RequiredCreateThemeRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "Name": str,
        "BaseThemeId": str,
        "Configuration": "ThemeConfigurationTypeDef",
    },
)
_OptionalCreateThemeRequestTypeDef = TypedDict(
    "_OptionalCreateThemeRequestTypeDef",
    {
        "VersionDescription": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateThemeRequestTypeDef(
    _RequiredCreateThemeRequestTypeDef, _OptionalCreateThemeRequestTypeDef
):
    pass


CreateThemeResponseResponseTypeDef = TypedDict(
    "CreateThemeResponseResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "ThemeId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCredentialPairTypeDef = TypedDict(
    "_RequiredCredentialPairTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)
_OptionalCredentialPairTypeDef = TypedDict(
    "_OptionalCredentialPairTypeDef",
    {
        "AlternateDataSourceParameters": List["DataSourceParametersTypeDef"],
    },
    total=False,
)


class CredentialPairTypeDef(_RequiredCredentialPairTypeDef, _OptionalCredentialPairTypeDef):
    pass


_RequiredCustomSqlTypeDef = TypedDict(
    "_RequiredCustomSqlTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "SqlQuery": str,
    },
)
_OptionalCustomSqlTypeDef = TypedDict(
    "_OptionalCustomSqlTypeDef",
    {
        "Columns": List["InputColumnTypeDef"],
    },
    total=False,
)


class CustomSqlTypeDef(_RequiredCustomSqlTypeDef, _OptionalCustomSqlTypeDef):
    pass


DashboardErrorTypeDef = TypedDict(
    "DashboardErrorTypeDef",
    {
        "Type": DashboardErrorTypeType,
        "Message": str,
    },
    total=False,
)

DashboardPublishOptionsTypeDef = TypedDict(
    "DashboardPublishOptionsTypeDef",
    {
        "AdHocFilteringOption": "AdHocFilteringOptionTypeDef",
        "ExportToCSVOption": "ExportToCSVOptionTypeDef",
        "SheetControlsOption": "SheetControlsOptionTypeDef",
    },
    total=False,
)

_RequiredDashboardSearchFilterTypeDef = TypedDict(
    "_RequiredDashboardSearchFilterTypeDef",
    {
        "Operator": Literal["StringEquals"],
    },
)
_OptionalDashboardSearchFilterTypeDef = TypedDict(
    "_OptionalDashboardSearchFilterTypeDef",
    {
        "Name": Literal["QUICKSIGHT_USER"],
        "Value": str,
    },
    total=False,
)


class DashboardSearchFilterTypeDef(
    _RequiredDashboardSearchFilterTypeDef, _OptionalDashboardSearchFilterTypeDef
):
    pass


DashboardSourceEntityTypeDef = TypedDict(
    "DashboardSourceEntityTypeDef",
    {
        "SourceTemplate": "DashboardSourceTemplateTypeDef",
    },
    total=False,
)

DashboardSourceTemplateTypeDef = TypedDict(
    "DashboardSourceTemplateTypeDef",
    {
        "DataSetReferences": List["DataSetReferenceTypeDef"],
        "Arn": str,
    },
)

DashboardSummaryTypeDef = TypedDict(
    "DashboardSummaryTypeDef",
    {
        "Arn": str,
        "DashboardId": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "PublishedVersionNumber": int,
        "LastPublishedTime": datetime,
    },
    total=False,
)

DashboardTypeDef = TypedDict(
    "DashboardTypeDef",
    {
        "DashboardId": str,
        "Arn": str,
        "Name": str,
        "Version": "DashboardVersionTypeDef",
        "CreatedTime": datetime,
        "LastPublishedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

DashboardVersionSummaryTypeDef = TypedDict(
    "DashboardVersionSummaryTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "VersionNumber": int,
        "Status": ResourceStatusType,
        "SourceEntityArn": str,
        "Description": str,
    },
    total=False,
)

DashboardVersionTypeDef = TypedDict(
    "DashboardVersionTypeDef",
    {
        "CreatedTime": datetime,
        "Errors": List["DashboardErrorTypeDef"],
        "VersionNumber": int,
        "Status": ResourceStatusType,
        "Arn": str,
        "SourceEntityArn": str,
        "DataSetArns": List[str],
        "Description": str,
        "ThemeArn": str,
        "Sheets": List["SheetTypeDef"],
    },
    total=False,
)

DataColorPaletteTypeDef = TypedDict(
    "DataColorPaletteTypeDef",
    {
        "Colors": List[str],
        "MinMaxGradient": List[str],
        "EmptyFillColor": str,
    },
    total=False,
)

DataSetConfigurationTypeDef = TypedDict(
    "DataSetConfigurationTypeDef",
    {
        "Placeholder": str,
        "DataSetSchema": "DataSetSchemaTypeDef",
        "ColumnGroupSchemaList": List["ColumnGroupSchemaTypeDef"],
    },
    total=False,
)

DataSetReferenceTypeDef = TypedDict(
    "DataSetReferenceTypeDef",
    {
        "DataSetPlaceholder": str,
        "DataSetArn": str,
    },
)

DataSetSchemaTypeDef = TypedDict(
    "DataSetSchemaTypeDef",
    {
        "ColumnSchemaList": List["ColumnSchemaTypeDef"],
    },
    total=False,
)

DataSetSummaryTypeDef = TypedDict(
    "DataSetSummaryTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "ImportMode": DataSetImportModeType,
        "RowLevelPermissionDataSet": "RowLevelPermissionDataSetTypeDef",
        "ColumnLevelPermissionRulesApplied": bool,
    },
    total=False,
)

DataSetTypeDef = TypedDict(
    "DataSetTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "PhysicalTableMap": Dict[str, "PhysicalTableTypeDef"],
        "LogicalTableMap": Dict[str, "LogicalTableTypeDef"],
        "OutputColumns": List["OutputColumnTypeDef"],
        "ImportMode": DataSetImportModeType,
        "ConsumedSpiceCapacityInBytes": int,
        "ColumnGroups": List["ColumnGroupTypeDef"],
        "FieldFolders": Dict[str, "FieldFolderTypeDef"],
        "RowLevelPermissionDataSet": "RowLevelPermissionDataSetTypeDef",
        "ColumnLevelPermissionRules": List["ColumnLevelPermissionRuleTypeDef"],
    },
    total=False,
)

DataSourceCredentialsTypeDef = TypedDict(
    "DataSourceCredentialsTypeDef",
    {
        "CredentialPair": "CredentialPairTypeDef",
        "CopySourceArn": str,
    },
    total=False,
)

DataSourceErrorInfoTypeDef = TypedDict(
    "DataSourceErrorInfoTypeDef",
    {
        "Type": DataSourceErrorInfoTypeType,
        "Message": str,
    },
    total=False,
)

DataSourceParametersTypeDef = TypedDict(
    "DataSourceParametersTypeDef",
    {
        "AmazonElasticsearchParameters": "AmazonElasticsearchParametersTypeDef",
        "AthenaParameters": "AthenaParametersTypeDef",
        "AuroraParameters": "AuroraParametersTypeDef",
        "AuroraPostgreSqlParameters": "AuroraPostgreSqlParametersTypeDef",
        "AwsIotAnalyticsParameters": "AwsIotAnalyticsParametersTypeDef",
        "JiraParameters": "JiraParametersTypeDef",
        "MariaDbParameters": "MariaDbParametersTypeDef",
        "MySqlParameters": "MySqlParametersTypeDef",
        "OracleParameters": "OracleParametersTypeDef",
        "PostgreSqlParameters": "PostgreSqlParametersTypeDef",
        "PrestoParameters": "PrestoParametersTypeDef",
        "RdsParameters": "RdsParametersTypeDef",
        "RedshiftParameters": "RedshiftParametersTypeDef",
        "S3Parameters": "S3ParametersTypeDef",
        "ServiceNowParameters": "ServiceNowParametersTypeDef",
        "SnowflakeParameters": "SnowflakeParametersTypeDef",
        "SparkParameters": "SparkParametersTypeDef",
        "SqlServerParameters": "SqlServerParametersTypeDef",
        "TeradataParameters": "TeradataParametersTypeDef",
        "TwitterParameters": "TwitterParametersTypeDef",
    },
    total=False,
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "Name": str,
        "Type": DataSourceTypeType,
        "Status": ResourceStatusType,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "DataSourceParameters": "DataSourceParametersTypeDef",
        "AlternateDataSourceParameters": List["DataSourceParametersTypeDef"],
        "VpcConnectionProperties": "VpcConnectionPropertiesTypeDef",
        "SslProperties": "SslPropertiesTypeDef",
        "ErrorInfo": "DataSourceErrorInfoTypeDef",
    },
    total=False,
)

DateTimeParameterTypeDef = TypedDict(
    "DateTimeParameterTypeDef",
    {
        "Name": str,
        "Values": List[Union[datetime, str]],
    },
)

DecimalParameterTypeDef = TypedDict(
    "DecimalParameterTypeDef",
    {
        "Name": str,
        "Values": List[float],
    },
)

_RequiredDeleteAccountCustomizationRequestTypeDef = TypedDict(
    "_RequiredDeleteAccountCustomizationRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalDeleteAccountCustomizationRequestTypeDef = TypedDict(
    "_OptionalDeleteAccountCustomizationRequestTypeDef",
    {
        "Namespace": str,
    },
    total=False,
)


class DeleteAccountCustomizationRequestTypeDef(
    _RequiredDeleteAccountCustomizationRequestTypeDef,
    _OptionalDeleteAccountCustomizationRequestTypeDef,
):
    pass


DeleteAccountCustomizationResponseResponseTypeDef = TypedDict(
    "DeleteAccountCustomizationResponseResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAnalysisRequestTypeDef = TypedDict(
    "_RequiredDeleteAnalysisRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)
_OptionalDeleteAnalysisRequestTypeDef = TypedDict(
    "_OptionalDeleteAnalysisRequestTypeDef",
    {
        "RecoveryWindowInDays": int,
        "ForceDeleteWithoutRecovery": bool,
    },
    total=False,
)


class DeleteAnalysisRequestTypeDef(
    _RequiredDeleteAnalysisRequestTypeDef, _OptionalDeleteAnalysisRequestTypeDef
):
    pass


DeleteAnalysisResponseResponseTypeDef = TypedDict(
    "DeleteAnalysisResponseResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "AnalysisId": str,
        "DeletionTime": datetime,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteDashboardRequestTypeDef = TypedDict(
    "_RequiredDeleteDashboardRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)
_OptionalDeleteDashboardRequestTypeDef = TypedDict(
    "_OptionalDeleteDashboardRequestTypeDef",
    {
        "VersionNumber": int,
    },
    total=False,
)


class DeleteDashboardRequestTypeDef(
    _RequiredDeleteDashboardRequestTypeDef, _OptionalDeleteDashboardRequestTypeDef
):
    pass


DeleteDashboardResponseResponseTypeDef = TypedDict(
    "DeleteDashboardResponseResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "DashboardId": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataSetRequestTypeDef = TypedDict(
    "DeleteDataSetRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)

DeleteDataSetResponseResponseTypeDef = TypedDict(
    "DeleteDataSetResponseResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataSourceRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)

DeleteDataSourceResponseResponseTypeDef = TypedDict(
    "DeleteDataSourceResponseResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFolderMembershipRequestTypeDef = TypedDict(
    "DeleteFolderMembershipRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "MemberId": str,
        "MemberType": MemberTypeType,
    },
)

DeleteFolderMembershipResponseResponseTypeDef = TypedDict(
    "DeleteFolderMembershipResponseResponseTypeDef",
    {
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFolderRequestTypeDef = TypedDict(
    "DeleteFolderRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)

DeleteFolderResponseResponseTypeDef = TypedDict(
    "DeleteFolderResponseResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGroupMembershipRequestTypeDef = TypedDict(
    "DeleteGroupMembershipRequestTypeDef",
    {
        "MemberName": str,
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteGroupMembershipResponseResponseTypeDef = TypedDict(
    "DeleteGroupMembershipResponseResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGroupRequestTypeDef = TypedDict(
    "DeleteGroupRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteGroupResponseResponseTypeDef = TypedDict(
    "DeleteGroupResponseResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIAMPolicyAssignmentRequestTypeDef = TypedDict(
    "DeleteIAMPolicyAssignmentRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "Namespace": str,
    },
)

DeleteIAMPolicyAssignmentResponseResponseTypeDef = TypedDict(
    "DeleteIAMPolicyAssignmentResponseResponseTypeDef",
    {
        "AssignmentName": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNamespaceRequestTypeDef = TypedDict(
    "DeleteNamespaceRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteNamespaceResponseResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTemplateAliasRequestTypeDef = TypedDict(
    "DeleteTemplateAliasRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
    },
)

DeleteTemplateAliasResponseResponseTypeDef = TypedDict(
    "DeleteTemplateAliasResponseResponseTypeDef",
    {
        "Status": int,
        "TemplateId": str,
        "AliasName": str,
        "Arn": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTemplateRequestTypeDef = TypedDict(
    "_RequiredDeleteTemplateRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalDeleteTemplateRequestTypeDef = TypedDict(
    "_OptionalDeleteTemplateRequestTypeDef",
    {
        "VersionNumber": int,
    },
    total=False,
)


class DeleteTemplateRequestTypeDef(
    _RequiredDeleteTemplateRequestTypeDef, _OptionalDeleteTemplateRequestTypeDef
):
    pass


DeleteTemplateResponseResponseTypeDef = TypedDict(
    "DeleteTemplateResponseResponseTypeDef",
    {
        "RequestId": str,
        "Arn": str,
        "TemplateId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteThemeAliasRequestTypeDef = TypedDict(
    "DeleteThemeAliasRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
    },
)

DeleteThemeAliasResponseResponseTypeDef = TypedDict(
    "DeleteThemeAliasResponseResponseTypeDef",
    {
        "AliasName": str,
        "Arn": str,
        "RequestId": str,
        "Status": int,
        "ThemeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteThemeRequestTypeDef = TypedDict(
    "_RequiredDeleteThemeRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
_OptionalDeleteThemeRequestTypeDef = TypedDict(
    "_OptionalDeleteThemeRequestTypeDef",
    {
        "VersionNumber": int,
    },
    total=False,
)


class DeleteThemeRequestTypeDef(
    _RequiredDeleteThemeRequestTypeDef, _OptionalDeleteThemeRequestTypeDef
):
    pass


DeleteThemeResponseResponseTypeDef = TypedDict(
    "DeleteThemeResponseResponseTypeDef",
    {
        "Arn": str,
        "RequestId": str,
        "Status": int,
        "ThemeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserByPrincipalIdRequestTypeDef = TypedDict(
    "DeleteUserByPrincipalIdRequestTypeDef",
    {
        "PrincipalId": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteUserByPrincipalIdResponseResponseTypeDef = TypedDict(
    "DeleteUserByPrincipalIdResponseResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserRequestTypeDef = TypedDict(
    "DeleteUserRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteUserResponseResponseTypeDef = TypedDict(
    "DeleteUserResponseResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAccountCustomizationRequestTypeDef = TypedDict(
    "_RequiredDescribeAccountCustomizationRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalDescribeAccountCustomizationRequestTypeDef = TypedDict(
    "_OptionalDescribeAccountCustomizationRequestTypeDef",
    {
        "Namespace": str,
        "Resolved": bool,
    },
    total=False,
)


class DescribeAccountCustomizationRequestTypeDef(
    _RequiredDescribeAccountCustomizationRequestTypeDef,
    _OptionalDescribeAccountCustomizationRequestTypeDef,
):
    pass


DescribeAccountCustomizationResponseResponseTypeDef = TypedDict(
    "DescribeAccountCustomizationResponseResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountSettingsRequestTypeDef = TypedDict(
    "DescribeAccountSettingsRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)

DescribeAccountSettingsResponseResponseTypeDef = TypedDict(
    "DescribeAccountSettingsResponseResponseTypeDef",
    {
        "AccountSettings": "AccountSettingsTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnalysisPermissionsRequestTypeDef = TypedDict(
    "DescribeAnalysisPermissionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)

DescribeAnalysisPermissionsResponseResponseTypeDef = TypedDict(
    "DescribeAnalysisPermissionsResponseResponseTypeDef",
    {
        "AnalysisId": str,
        "AnalysisArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnalysisRequestTypeDef = TypedDict(
    "DescribeAnalysisRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)

DescribeAnalysisResponseResponseTypeDef = TypedDict(
    "DescribeAnalysisResponseResponseTypeDef",
    {
        "Analysis": "AnalysisTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDashboardPermissionsRequestTypeDef = TypedDict(
    "DescribeDashboardPermissionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)

DescribeDashboardPermissionsResponseResponseTypeDef = TypedDict(
    "DescribeDashboardPermissionsResponseResponseTypeDef",
    {
        "DashboardId": str,
        "DashboardArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDashboardRequestTypeDef = TypedDict(
    "_RequiredDescribeDashboardRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)
_OptionalDescribeDashboardRequestTypeDef = TypedDict(
    "_OptionalDescribeDashboardRequestTypeDef",
    {
        "VersionNumber": int,
        "AliasName": str,
    },
    total=False,
)


class DescribeDashboardRequestTypeDef(
    _RequiredDescribeDashboardRequestTypeDef, _OptionalDescribeDashboardRequestTypeDef
):
    pass


DescribeDashboardResponseResponseTypeDef = TypedDict(
    "DescribeDashboardResponseResponseTypeDef",
    {
        "Dashboard": "DashboardTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSetPermissionsRequestTypeDef = TypedDict(
    "DescribeDataSetPermissionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)

DescribeDataSetPermissionsResponseResponseTypeDef = TypedDict(
    "DescribeDataSetPermissionsResponseResponseTypeDef",
    {
        "DataSetArn": str,
        "DataSetId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSetRequestTypeDef = TypedDict(
    "DescribeDataSetRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)

DescribeDataSetResponseResponseTypeDef = TypedDict(
    "DescribeDataSetResponseResponseTypeDef",
    {
        "DataSet": "DataSetTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSourcePermissionsRequestTypeDef = TypedDict(
    "DescribeDataSourcePermissionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)

DescribeDataSourcePermissionsResponseResponseTypeDef = TypedDict(
    "DescribeDataSourcePermissionsResponseResponseTypeDef",
    {
        "DataSourceArn": str,
        "DataSourceId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSourceRequestTypeDef = TypedDict(
    "DescribeDataSourceRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)

DescribeDataSourceResponseResponseTypeDef = TypedDict(
    "DescribeDataSourceResponseResponseTypeDef",
    {
        "DataSource": "DataSourceTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFolderPermissionsRequestTypeDef = TypedDict(
    "DescribeFolderPermissionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)

DescribeFolderPermissionsResponseResponseTypeDef = TypedDict(
    "DescribeFolderPermissionsResponseResponseTypeDef",
    {
        "Status": int,
        "FolderId": str,
        "Arn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFolderRequestTypeDef = TypedDict(
    "DescribeFolderRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)

DescribeFolderResolvedPermissionsRequestTypeDef = TypedDict(
    "DescribeFolderResolvedPermissionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)

DescribeFolderResolvedPermissionsResponseResponseTypeDef = TypedDict(
    "DescribeFolderResolvedPermissionsResponseResponseTypeDef",
    {
        "Status": int,
        "FolderId": str,
        "Arn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFolderResponseResponseTypeDef = TypedDict(
    "DescribeFolderResponseResponseTypeDef",
    {
        "Status": int,
        "Folder": "FolderTypeDef",
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGroupRequestTypeDef = TypedDict(
    "DescribeGroupRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DescribeGroupResponseResponseTypeDef = TypedDict(
    "DescribeGroupResponseResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIAMPolicyAssignmentRequestTypeDef = TypedDict(
    "DescribeIAMPolicyAssignmentRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "Namespace": str,
    },
)

DescribeIAMPolicyAssignmentResponseResponseTypeDef = TypedDict(
    "DescribeIAMPolicyAssignmentResponseResponseTypeDef",
    {
        "IAMPolicyAssignment": "IAMPolicyAssignmentTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIngestionRequestTypeDef = TypedDict(
    "DescribeIngestionRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "IngestionId": str,
    },
)

DescribeIngestionResponseResponseTypeDef = TypedDict(
    "DescribeIngestionResponseResponseTypeDef",
    {
        "Ingestion": "IngestionTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNamespaceRequestTypeDef = TypedDict(
    "DescribeNamespaceRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DescribeNamespaceResponseResponseTypeDef = TypedDict(
    "DescribeNamespaceResponseResponseTypeDef",
    {
        "Namespace": "NamespaceInfoV2TypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTemplateAliasRequestTypeDef = TypedDict(
    "DescribeTemplateAliasRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
    },
)

DescribeTemplateAliasResponseResponseTypeDef = TypedDict(
    "DescribeTemplateAliasResponseResponseTypeDef",
    {
        "TemplateAlias": "TemplateAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTemplatePermissionsRequestTypeDef = TypedDict(
    "DescribeTemplatePermissionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)

DescribeTemplatePermissionsResponseResponseTypeDef = TypedDict(
    "DescribeTemplatePermissionsResponseResponseTypeDef",
    {
        "TemplateId": str,
        "TemplateArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTemplateRequestTypeDef = TypedDict(
    "_RequiredDescribeTemplateRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalDescribeTemplateRequestTypeDef = TypedDict(
    "_OptionalDescribeTemplateRequestTypeDef",
    {
        "VersionNumber": int,
        "AliasName": str,
    },
    total=False,
)


class DescribeTemplateRequestTypeDef(
    _RequiredDescribeTemplateRequestTypeDef, _OptionalDescribeTemplateRequestTypeDef
):
    pass


DescribeTemplateResponseResponseTypeDef = TypedDict(
    "DescribeTemplateResponseResponseTypeDef",
    {
        "Template": "TemplateTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThemeAliasRequestTypeDef = TypedDict(
    "DescribeThemeAliasRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
    },
)

DescribeThemeAliasResponseResponseTypeDef = TypedDict(
    "DescribeThemeAliasResponseResponseTypeDef",
    {
        "ThemeAlias": "ThemeAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThemePermissionsRequestTypeDef = TypedDict(
    "DescribeThemePermissionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)

DescribeThemePermissionsResponseResponseTypeDef = TypedDict(
    "DescribeThemePermissionsResponseResponseTypeDef",
    {
        "ThemeId": str,
        "ThemeArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeThemeRequestTypeDef = TypedDict(
    "_RequiredDescribeThemeRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
_OptionalDescribeThemeRequestTypeDef = TypedDict(
    "_OptionalDescribeThemeRequestTypeDef",
    {
        "VersionNumber": int,
        "AliasName": str,
    },
    total=False,
)


class DescribeThemeRequestTypeDef(
    _RequiredDescribeThemeRequestTypeDef, _OptionalDescribeThemeRequestTypeDef
):
    pass


DescribeThemeResponseResponseTypeDef = TypedDict(
    "DescribeThemeResponseResponseTypeDef",
    {
        "Theme": "ThemeTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestTypeDef = TypedDict(
    "DescribeUserRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DescribeUserResponseResponseTypeDef = TypedDict(
    "DescribeUserResponseResponseTypeDef",
    {
        "User": "UserTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "Type": IngestionErrorTypeType,
        "Message": str,
    },
    total=False,
)

ExportToCSVOptionTypeDef = TypedDict(
    "ExportToCSVOptionTypeDef",
    {
        "AvailabilityStatus": DashboardBehaviorType,
    },
    total=False,
)

FieldFolderTypeDef = TypedDict(
    "FieldFolderTypeDef",
    {
        "description": str,
        "columns": List[str],
    },
    total=False,
)

FilterOperationTypeDef = TypedDict(
    "FilterOperationTypeDef",
    {
        "ConditionExpression": str,
    },
)

FolderMemberTypeDef = TypedDict(
    "FolderMemberTypeDef",
    {
        "MemberId": str,
        "MemberType": MemberTypeType,
    },
    total=False,
)

FolderSearchFilterTypeDef = TypedDict(
    "FolderSearchFilterTypeDef",
    {
        "Operator": Literal["StringEquals"],
        "Name": Literal["PARENT_FOLDER_ARN"],
        "Value": str,
    },
    total=False,
)

FolderSummaryTypeDef = TypedDict(
    "FolderSummaryTypeDef",
    {
        "Arn": str,
        "FolderId": str,
        "Name": str,
        "FolderType": Literal["SHARED"],
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

FolderTypeDef = TypedDict(
    "FolderTypeDef",
    {
        "FolderId": str,
        "Arn": str,
        "Name": str,
        "FolderType": Literal["SHARED"],
        "FolderPath": List[str],
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

GeoSpatialColumnGroupTypeDef = TypedDict(
    "GeoSpatialColumnGroupTypeDef",
    {
        "Name": str,
        "CountryCode": Literal["US"],
        "Columns": List[str],
    },
)

_RequiredGetDashboardEmbedUrlRequestTypeDef = TypedDict(
    "_RequiredGetDashboardEmbedUrlRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "IdentityType": EmbeddingIdentityTypeType,
    },
)
_OptionalGetDashboardEmbedUrlRequestTypeDef = TypedDict(
    "_OptionalGetDashboardEmbedUrlRequestTypeDef",
    {
        "SessionLifetimeInMinutes": int,
        "UndoRedoDisabled": bool,
        "ResetDisabled": bool,
        "StatePersistenceEnabled": bool,
        "UserArn": str,
        "Namespace": str,
        "AdditionalDashboardIds": List[str],
    },
    total=False,
)


class GetDashboardEmbedUrlRequestTypeDef(
    _RequiredGetDashboardEmbedUrlRequestTypeDef, _OptionalGetDashboardEmbedUrlRequestTypeDef
):
    pass


GetDashboardEmbedUrlResponseResponseTypeDef = TypedDict(
    "GetDashboardEmbedUrlResponseResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSessionEmbedUrlRequestTypeDef = TypedDict(
    "_RequiredGetSessionEmbedUrlRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalGetSessionEmbedUrlRequestTypeDef = TypedDict(
    "_OptionalGetSessionEmbedUrlRequestTypeDef",
    {
        "EntryPoint": str,
        "SessionLifetimeInMinutes": int,
        "UserArn": str,
    },
    total=False,
)


class GetSessionEmbedUrlRequestTypeDef(
    _RequiredGetSessionEmbedUrlRequestTypeDef, _OptionalGetSessionEmbedUrlRequestTypeDef
):
    pass


GetSessionEmbedUrlResponseResponseTypeDef = TypedDict(
    "GetSessionEmbedUrlResponseResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupMemberTypeDef = TypedDict(
    "GroupMemberTypeDef",
    {
        "Arn": str,
        "MemberName": str,
    },
    total=False,
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Arn": str,
        "GroupName": str,
        "Description": str,
        "PrincipalId": str,
    },
    total=False,
)

GutterStyleTypeDef = TypedDict(
    "GutterStyleTypeDef",
    {
        "Show": bool,
    },
    total=False,
)

IAMPolicyAssignmentSummaryTypeDef = TypedDict(
    "IAMPolicyAssignmentSummaryTypeDef",
    {
        "AssignmentName": str,
        "AssignmentStatus": AssignmentStatusType,
    },
    total=False,
)

IAMPolicyAssignmentTypeDef = TypedDict(
    "IAMPolicyAssignmentTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentId": str,
        "AssignmentName": str,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "AssignmentStatus": AssignmentStatusType,
    },
    total=False,
)

_RequiredIngestionTypeDef = TypedDict(
    "_RequiredIngestionTypeDef",
    {
        "Arn": str,
        "IngestionStatus": IngestionStatusType,
        "CreatedTime": datetime,
    },
)
_OptionalIngestionTypeDef = TypedDict(
    "_OptionalIngestionTypeDef",
    {
        "IngestionId": str,
        "ErrorInfo": "ErrorInfoTypeDef",
        "RowInfo": "RowInfoTypeDef",
        "QueueInfo": "QueueInfoTypeDef",
        "IngestionTimeInSeconds": int,
        "IngestionSizeInBytes": int,
        "RequestSource": IngestionRequestSourceType,
        "RequestType": IngestionRequestTypeType,
    },
    total=False,
)


class IngestionTypeDef(_RequiredIngestionTypeDef, _OptionalIngestionTypeDef):
    pass


InputColumnTypeDef = TypedDict(
    "InputColumnTypeDef",
    {
        "Name": str,
        "Type": InputColumnDataTypeType,
    },
)

IntegerParameterTypeDef = TypedDict(
    "IntegerParameterTypeDef",
    {
        "Name": str,
        "Values": List[int],
    },
)

JiraParametersTypeDef = TypedDict(
    "JiraParametersTypeDef",
    {
        "SiteBaseUrl": str,
    },
)

_RequiredJoinInstructionTypeDef = TypedDict(
    "_RequiredJoinInstructionTypeDef",
    {
        "LeftOperand": str,
        "RightOperand": str,
        "Type": JoinTypeType,
        "OnClause": str,
    },
)
_OptionalJoinInstructionTypeDef = TypedDict(
    "_OptionalJoinInstructionTypeDef",
    {
        "LeftJoinKeyProperties": "JoinKeyPropertiesTypeDef",
        "RightJoinKeyProperties": "JoinKeyPropertiesTypeDef",
    },
    total=False,
)


class JoinInstructionTypeDef(_RequiredJoinInstructionTypeDef, _OptionalJoinInstructionTypeDef):
    pass


JoinKeyPropertiesTypeDef = TypedDict(
    "JoinKeyPropertiesTypeDef",
    {
        "UniqueKey": bool,
    },
    total=False,
)

_RequiredListAnalysesRequestTypeDef = TypedDict(
    "_RequiredListAnalysesRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListAnalysesRequestTypeDef = TypedDict(
    "_OptionalListAnalysesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAnalysesRequestTypeDef(
    _RequiredListAnalysesRequestTypeDef, _OptionalListAnalysesRequestTypeDef
):
    pass


ListAnalysesResponseResponseTypeDef = TypedDict(
    "ListAnalysesResponseResponseTypeDef",
    {
        "AnalysisSummaryList": List["AnalysisSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDashboardVersionsRequestTypeDef = TypedDict(
    "_RequiredListDashboardVersionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)
_OptionalListDashboardVersionsRequestTypeDef = TypedDict(
    "_OptionalListDashboardVersionsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDashboardVersionsRequestTypeDef(
    _RequiredListDashboardVersionsRequestTypeDef, _OptionalListDashboardVersionsRequestTypeDef
):
    pass


ListDashboardVersionsResponseResponseTypeDef = TypedDict(
    "ListDashboardVersionsResponseResponseTypeDef",
    {
        "DashboardVersionSummaryList": List["DashboardVersionSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDashboardsRequestTypeDef = TypedDict(
    "_RequiredListDashboardsRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListDashboardsRequestTypeDef = TypedDict(
    "_OptionalListDashboardsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDashboardsRequestTypeDef(
    _RequiredListDashboardsRequestTypeDef, _OptionalListDashboardsRequestTypeDef
):
    pass


ListDashboardsResponseResponseTypeDef = TypedDict(
    "ListDashboardsResponseResponseTypeDef",
    {
        "DashboardSummaryList": List["DashboardSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSetsRequestTypeDef = TypedDict(
    "_RequiredListDataSetsRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListDataSetsRequestTypeDef = TypedDict(
    "_OptionalListDataSetsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDataSetsRequestTypeDef(
    _RequiredListDataSetsRequestTypeDef, _OptionalListDataSetsRequestTypeDef
):
    pass


ListDataSetsResponseResponseTypeDef = TypedDict(
    "ListDataSetsResponseResponseTypeDef",
    {
        "DataSetSummaries": List["DataSetSummaryTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSourcesRequestTypeDef = TypedDict(
    "_RequiredListDataSourcesRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListDataSourcesRequestTypeDef = TypedDict(
    "_OptionalListDataSourcesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDataSourcesRequestTypeDef(
    _RequiredListDataSourcesRequestTypeDef, _OptionalListDataSourcesRequestTypeDef
):
    pass


ListDataSourcesResponseResponseTypeDef = TypedDict(
    "ListDataSourcesResponseResponseTypeDef",
    {
        "DataSources": List["DataSourceTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFolderMembersRequestTypeDef = TypedDict(
    "_RequiredListFolderMembersRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)
_OptionalListFolderMembersRequestTypeDef = TypedDict(
    "_OptionalListFolderMembersRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListFolderMembersRequestTypeDef(
    _RequiredListFolderMembersRequestTypeDef, _OptionalListFolderMembersRequestTypeDef
):
    pass


ListFolderMembersResponseResponseTypeDef = TypedDict(
    "ListFolderMembersResponseResponseTypeDef",
    {
        "Status": int,
        "FolderMemberList": List["MemberIdArnPairTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFoldersRequestTypeDef = TypedDict(
    "_RequiredListFoldersRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListFoldersRequestTypeDef = TypedDict(
    "_OptionalListFoldersRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListFoldersRequestTypeDef(
    _RequiredListFoldersRequestTypeDef, _OptionalListFoldersRequestTypeDef
):
    pass


ListFoldersResponseResponseTypeDef = TypedDict(
    "ListFoldersResponseResponseTypeDef",
    {
        "Status": int,
        "FolderSummaryList": List["FolderSummaryTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupMembershipsRequestTypeDef = TypedDict(
    "_RequiredListGroupMembershipsRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListGroupMembershipsRequestTypeDef = TypedDict(
    "_OptionalListGroupMembershipsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListGroupMembershipsRequestTypeDef(
    _RequiredListGroupMembershipsRequestTypeDef, _OptionalListGroupMembershipsRequestTypeDef
):
    pass


ListGroupMembershipsResponseResponseTypeDef = TypedDict(
    "ListGroupMembershipsResponseResponseTypeDef",
    {
        "GroupMemberList": List["GroupMemberTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupsRequestTypeDef = TypedDict(
    "_RequiredListGroupsRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListGroupsRequestTypeDef = TypedDict(
    "_OptionalListGroupsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListGroupsRequestTypeDef(
    _RequiredListGroupsRequestTypeDef, _OptionalListGroupsRequestTypeDef
):
    pass


ListGroupsResponseResponseTypeDef = TypedDict(
    "ListGroupsResponseResponseTypeDef",
    {
        "GroupList": List["GroupTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIAMPolicyAssignmentsForUserRequestTypeDef = TypedDict(
    "_RequiredListIAMPolicyAssignmentsForUserRequestTypeDef",
    {
        "AwsAccountId": str,
        "UserName": str,
        "Namespace": str,
    },
)
_OptionalListIAMPolicyAssignmentsForUserRequestTypeDef = TypedDict(
    "_OptionalListIAMPolicyAssignmentsForUserRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListIAMPolicyAssignmentsForUserRequestTypeDef(
    _RequiredListIAMPolicyAssignmentsForUserRequestTypeDef,
    _OptionalListIAMPolicyAssignmentsForUserRequestTypeDef,
):
    pass


ListIAMPolicyAssignmentsForUserResponseResponseTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsForUserResponseResponseTypeDef",
    {
        "ActiveAssignments": List["ActiveIAMPolicyAssignmentTypeDef"],
        "RequestId": str,
        "NextToken": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIAMPolicyAssignmentsRequestTypeDef = TypedDict(
    "_RequiredListIAMPolicyAssignmentsRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListIAMPolicyAssignmentsRequestTypeDef = TypedDict(
    "_OptionalListIAMPolicyAssignmentsRequestTypeDef",
    {
        "AssignmentStatus": AssignmentStatusType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListIAMPolicyAssignmentsRequestTypeDef(
    _RequiredListIAMPolicyAssignmentsRequestTypeDef, _OptionalListIAMPolicyAssignmentsRequestTypeDef
):
    pass


ListIAMPolicyAssignmentsResponseResponseTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsResponseResponseTypeDef",
    {
        "IAMPolicyAssignments": List["IAMPolicyAssignmentSummaryTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIngestionsRequestTypeDef = TypedDict(
    "_RequiredListIngestionsRequestTypeDef",
    {
        "DataSetId": str,
        "AwsAccountId": str,
    },
)
_OptionalListIngestionsRequestTypeDef = TypedDict(
    "_OptionalListIngestionsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListIngestionsRequestTypeDef(
    _RequiredListIngestionsRequestTypeDef, _OptionalListIngestionsRequestTypeDef
):
    pass


ListIngestionsResponseResponseTypeDef = TypedDict(
    "ListIngestionsResponseResponseTypeDef",
    {
        "Ingestions": List["IngestionTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNamespacesRequestTypeDef = TypedDict(
    "_RequiredListNamespacesRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListNamespacesRequestTypeDef = TypedDict(
    "_OptionalListNamespacesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListNamespacesRequestTypeDef(
    _RequiredListNamespacesRequestTypeDef, _OptionalListNamespacesRequestTypeDef
):
    pass


ListNamespacesResponseResponseTypeDef = TypedDict(
    "ListNamespacesResponseResponseTypeDef",
    {
        "Namespaces": List["NamespaceInfoV2TypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
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
        "Tags": List["TagTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTemplateAliasesRequestTypeDef = TypedDict(
    "_RequiredListTemplateAliasesRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalListTemplateAliasesRequestTypeDef = TypedDict(
    "_OptionalListTemplateAliasesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTemplateAliasesRequestTypeDef(
    _RequiredListTemplateAliasesRequestTypeDef, _OptionalListTemplateAliasesRequestTypeDef
):
    pass


ListTemplateAliasesResponseResponseTypeDef = TypedDict(
    "ListTemplateAliasesResponseResponseTypeDef",
    {
        "TemplateAliasList": List["TemplateAliasTypeDef"],
        "Status": int,
        "RequestId": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTemplateVersionsRequestTypeDef = TypedDict(
    "_RequiredListTemplateVersionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalListTemplateVersionsRequestTypeDef = TypedDict(
    "_OptionalListTemplateVersionsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTemplateVersionsRequestTypeDef(
    _RequiredListTemplateVersionsRequestTypeDef, _OptionalListTemplateVersionsRequestTypeDef
):
    pass


ListTemplateVersionsResponseResponseTypeDef = TypedDict(
    "ListTemplateVersionsResponseResponseTypeDef",
    {
        "TemplateVersionSummaryList": List["TemplateVersionSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTemplatesRequestTypeDef = TypedDict(
    "_RequiredListTemplatesRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListTemplatesRequestTypeDef = TypedDict(
    "_OptionalListTemplatesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTemplatesRequestTypeDef(
    _RequiredListTemplatesRequestTypeDef, _OptionalListTemplatesRequestTypeDef
):
    pass


ListTemplatesResponseResponseTypeDef = TypedDict(
    "ListTemplatesResponseResponseTypeDef",
    {
        "TemplateSummaryList": List["TemplateSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThemeAliasesRequestTypeDef = TypedDict(
    "_RequiredListThemeAliasesRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
_OptionalListThemeAliasesRequestTypeDef = TypedDict(
    "_OptionalListThemeAliasesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListThemeAliasesRequestTypeDef(
    _RequiredListThemeAliasesRequestTypeDef, _OptionalListThemeAliasesRequestTypeDef
):
    pass


ListThemeAliasesResponseResponseTypeDef = TypedDict(
    "ListThemeAliasesResponseResponseTypeDef",
    {
        "ThemeAliasList": List["ThemeAliasTypeDef"],
        "Status": int,
        "RequestId": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThemeVersionsRequestTypeDef = TypedDict(
    "_RequiredListThemeVersionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
_OptionalListThemeVersionsRequestTypeDef = TypedDict(
    "_OptionalListThemeVersionsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListThemeVersionsRequestTypeDef(
    _RequiredListThemeVersionsRequestTypeDef, _OptionalListThemeVersionsRequestTypeDef
):
    pass


ListThemeVersionsResponseResponseTypeDef = TypedDict(
    "ListThemeVersionsResponseResponseTypeDef",
    {
        "ThemeVersionSummaryList": List["ThemeVersionSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThemesRequestTypeDef = TypedDict(
    "_RequiredListThemesRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListThemesRequestTypeDef = TypedDict(
    "_OptionalListThemesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Type": ThemeTypeType,
    },
    total=False,
)


class ListThemesRequestTypeDef(
    _RequiredListThemesRequestTypeDef, _OptionalListThemesRequestTypeDef
):
    pass


ListThemesResponseResponseTypeDef = TypedDict(
    "ListThemesResponseResponseTypeDef",
    {
        "ThemeSummaryList": List["ThemeSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserGroupsRequestTypeDef = TypedDict(
    "_RequiredListUserGroupsRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListUserGroupsRequestTypeDef = TypedDict(
    "_OptionalListUserGroupsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListUserGroupsRequestTypeDef(
    _RequiredListUserGroupsRequestTypeDef, _OptionalListUserGroupsRequestTypeDef
):
    pass


ListUserGroupsResponseResponseTypeDef = TypedDict(
    "ListUserGroupsResponseResponseTypeDef",
    {
        "GroupList": List["GroupTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListUsersRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListUsersRequestTypeDef(_RequiredListUsersRequestTypeDef, _OptionalListUsersRequestTypeDef):
    pass


ListUsersResponseResponseTypeDef = TypedDict(
    "ListUsersResponseResponseTypeDef",
    {
        "UserList": List["UserTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogicalTableSourceTypeDef = TypedDict(
    "LogicalTableSourceTypeDef",
    {
        "JoinInstruction": "JoinInstructionTypeDef",
        "PhysicalTableId": str,
    },
    total=False,
)

_RequiredLogicalTableTypeDef = TypedDict(
    "_RequiredLogicalTableTypeDef",
    {
        "Alias": str,
        "Source": "LogicalTableSourceTypeDef",
    },
)
_OptionalLogicalTableTypeDef = TypedDict(
    "_OptionalLogicalTableTypeDef",
    {
        "DataTransforms": List["TransformOperationTypeDef"],
    },
    total=False,
)


class LogicalTableTypeDef(_RequiredLogicalTableTypeDef, _OptionalLogicalTableTypeDef):
    pass


ManifestFileLocationTypeDef = TypedDict(
    "ManifestFileLocationTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)

MarginStyleTypeDef = TypedDict(
    "MarginStyleTypeDef",
    {
        "Show": bool,
    },
    total=False,
)

MariaDbParametersTypeDef = TypedDict(
    "MariaDbParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

MemberIdArnPairTypeDef = TypedDict(
    "MemberIdArnPairTypeDef",
    {
        "MemberId": str,
        "MemberArn": str,
    },
    total=False,
)

MySqlParametersTypeDef = TypedDict(
    "MySqlParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

NamespaceErrorTypeDef = TypedDict(
    "NamespaceErrorTypeDef",
    {
        "Type": NamespaceErrorTypeType,
        "Message": str,
    },
    total=False,
)

NamespaceInfoV2TypeDef = TypedDict(
    "NamespaceInfoV2TypeDef",
    {
        "Name": str,
        "Arn": str,
        "CapacityRegion": str,
        "CreationStatus": NamespaceStatusType,
        "IdentityStore": Literal["QUICKSIGHT"],
        "NamespaceError": "NamespaceErrorTypeDef",
    },
    total=False,
)

OracleParametersTypeDef = TypedDict(
    "OracleParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

OutputColumnTypeDef = TypedDict(
    "OutputColumnTypeDef",
    {
        "Name": str,
        "Description": str,
        "Type": ColumnDataTypeType,
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

ParametersTypeDef = TypedDict(
    "ParametersTypeDef",
    {
        "StringParameters": List["StringParameterTypeDef"],
        "IntegerParameters": List["IntegerParameterTypeDef"],
        "DecimalParameters": List["DecimalParameterTypeDef"],
        "DateTimeParameters": List["DateTimeParameterTypeDef"],
    },
    total=False,
)

PhysicalTableTypeDef = TypedDict(
    "PhysicalTableTypeDef",
    {
        "RelationalTable": "RelationalTableTypeDef",
        "CustomSql": "CustomSqlTypeDef",
        "S3Source": "S3SourceTypeDef",
    },
    total=False,
)

PostgreSqlParametersTypeDef = TypedDict(
    "PostgreSqlParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

PrestoParametersTypeDef = TypedDict(
    "PrestoParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Catalog": str,
    },
)

ProjectOperationTypeDef = TypedDict(
    "ProjectOperationTypeDef",
    {
        "ProjectedColumns": List[str],
    },
)

QueueInfoTypeDef = TypedDict(
    "QueueInfoTypeDef",
    {
        "WaitingOnIngestion": str,
        "QueuedIngestion": str,
    },
)

RdsParametersTypeDef = TypedDict(
    "RdsParametersTypeDef",
    {
        "InstanceId": str,
        "Database": str,
    },
)

_RequiredRedshiftParametersTypeDef = TypedDict(
    "_RequiredRedshiftParametersTypeDef",
    {
        "Database": str,
    },
)
_OptionalRedshiftParametersTypeDef = TypedDict(
    "_OptionalRedshiftParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "ClusterId": str,
    },
    total=False,
)


class RedshiftParametersTypeDef(
    _RequiredRedshiftParametersTypeDef, _OptionalRedshiftParametersTypeDef
):
    pass


_RequiredRegisterUserRequestTypeDef = TypedDict(
    "_RequiredRegisterUserRequestTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "Email": str,
        "UserRole": UserRoleType,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalRegisterUserRequestTypeDef = TypedDict(
    "_OptionalRegisterUserRequestTypeDef",
    {
        "IamArn": str,
        "SessionName": str,
        "UserName": str,
        "CustomPermissionsName": str,
        "ExternalLoginFederationProviderType": str,
        "CustomFederationProviderUrl": str,
        "ExternalLoginId": str,
    },
    total=False,
)


class RegisterUserRequestTypeDef(
    _RequiredRegisterUserRequestTypeDef, _OptionalRegisterUserRequestTypeDef
):
    pass


RegisterUserResponseResponseTypeDef = TypedDict(
    "RegisterUserResponseResponseTypeDef",
    {
        "User": "UserTypeDef",
        "UserInvitationUrl": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRelationalTableTypeDef = TypedDict(
    "_RequiredRelationalTableTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "InputColumns": List["InputColumnTypeDef"],
    },
)
_OptionalRelationalTableTypeDef = TypedDict(
    "_OptionalRelationalTableTypeDef",
    {
        "Catalog": str,
        "Schema": str,
    },
    total=False,
)


class RelationalTableTypeDef(_RequiredRelationalTableTypeDef, _OptionalRelationalTableTypeDef):
    pass


RenameColumnOperationTypeDef = TypedDict(
    "RenameColumnOperationTypeDef",
    {
        "ColumnName": str,
        "NewColumnName": str,
    },
)

ResourcePermissionTypeDef = TypedDict(
    "ResourcePermissionTypeDef",
    {
        "Principal": str,
        "Actions": List[str],
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

RestoreAnalysisRequestTypeDef = TypedDict(
    "RestoreAnalysisRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)

RestoreAnalysisResponseResponseTypeDef = TypedDict(
    "RestoreAnalysisResponseResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "AnalysisId": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RowInfoTypeDef = TypedDict(
    "RowInfoTypeDef",
    {
        "RowsIngested": int,
        "RowsDropped": int,
    },
    total=False,
)

_RequiredRowLevelPermissionDataSetTypeDef = TypedDict(
    "_RequiredRowLevelPermissionDataSetTypeDef",
    {
        "Arn": str,
        "PermissionPolicy": RowLevelPermissionPolicyType,
    },
)
_OptionalRowLevelPermissionDataSetTypeDef = TypedDict(
    "_OptionalRowLevelPermissionDataSetTypeDef",
    {
        "Namespace": str,
        "FormatVersion": RowLevelPermissionFormatVersionType,
    },
    total=False,
)


class RowLevelPermissionDataSetTypeDef(
    _RequiredRowLevelPermissionDataSetTypeDef, _OptionalRowLevelPermissionDataSetTypeDef
):
    pass


S3ParametersTypeDef = TypedDict(
    "S3ParametersTypeDef",
    {
        "ManifestFileLocation": "ManifestFileLocationTypeDef",
    },
)

_RequiredS3SourceTypeDef = TypedDict(
    "_RequiredS3SourceTypeDef",
    {
        "DataSourceArn": str,
        "InputColumns": List["InputColumnTypeDef"],
    },
)
_OptionalS3SourceTypeDef = TypedDict(
    "_OptionalS3SourceTypeDef",
    {
        "UploadSettings": "UploadSettingsTypeDef",
    },
    total=False,
)


class S3SourceTypeDef(_RequiredS3SourceTypeDef, _OptionalS3SourceTypeDef):
    pass


_RequiredSearchAnalysesRequestTypeDef = TypedDict(
    "_RequiredSearchAnalysesRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": List["AnalysisSearchFilterTypeDef"],
    },
)
_OptionalSearchAnalysesRequestTypeDef = TypedDict(
    "_OptionalSearchAnalysesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class SearchAnalysesRequestTypeDef(
    _RequiredSearchAnalysesRequestTypeDef, _OptionalSearchAnalysesRequestTypeDef
):
    pass


SearchAnalysesResponseResponseTypeDef = TypedDict(
    "SearchAnalysesResponseResponseTypeDef",
    {
        "AnalysisSummaryList": List["AnalysisSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchDashboardsRequestTypeDef = TypedDict(
    "_RequiredSearchDashboardsRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": List["DashboardSearchFilterTypeDef"],
    },
)
_OptionalSearchDashboardsRequestTypeDef = TypedDict(
    "_OptionalSearchDashboardsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class SearchDashboardsRequestTypeDef(
    _RequiredSearchDashboardsRequestTypeDef, _OptionalSearchDashboardsRequestTypeDef
):
    pass


SearchDashboardsResponseResponseTypeDef = TypedDict(
    "SearchDashboardsResponseResponseTypeDef",
    {
        "DashboardSummaryList": List["DashboardSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchFoldersRequestTypeDef = TypedDict(
    "_RequiredSearchFoldersRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": List["FolderSearchFilterTypeDef"],
    },
)
_OptionalSearchFoldersRequestTypeDef = TypedDict(
    "_OptionalSearchFoldersRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class SearchFoldersRequestTypeDef(
    _RequiredSearchFoldersRequestTypeDef, _OptionalSearchFoldersRequestTypeDef
):
    pass


SearchFoldersResponseResponseTypeDef = TypedDict(
    "SearchFoldersResponseResponseTypeDef",
    {
        "Status": int,
        "FolderSummaryList": List["FolderSummaryTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceNowParametersTypeDef = TypedDict(
    "ServiceNowParametersTypeDef",
    {
        "SiteBaseUrl": str,
    },
)

SheetControlsOptionTypeDef = TypedDict(
    "SheetControlsOptionTypeDef",
    {
        "VisibilityState": DashboardUIStateType,
    },
    total=False,
)

SheetStyleTypeDef = TypedDict(
    "SheetStyleTypeDef",
    {
        "Tile": "TileStyleTypeDef",
        "TileLayout": "TileLayoutStyleTypeDef",
    },
    total=False,
)

SheetTypeDef = TypedDict(
    "SheetTypeDef",
    {
        "SheetId": str,
        "Name": str,
    },
    total=False,
)

SnowflakeParametersTypeDef = TypedDict(
    "SnowflakeParametersTypeDef",
    {
        "Host": str,
        "Database": str,
        "Warehouse": str,
    },
)

SparkParametersTypeDef = TypedDict(
    "SparkParametersTypeDef",
    {
        "Host": str,
        "Port": int,
    },
)

SqlServerParametersTypeDef = TypedDict(
    "SqlServerParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

SslPropertiesTypeDef = TypedDict(
    "SslPropertiesTypeDef",
    {
        "DisableSsl": bool,
    },
    total=False,
)

StringParameterTypeDef = TypedDict(
    "StringParameterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
)

TagColumnOperationTypeDef = TypedDict(
    "TagColumnOperationTypeDef",
    {
        "ColumnName": str,
        "Tags": List["ColumnTagTypeDef"],
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagResourceResponseResponseTypeDef = TypedDict(
    "TagResourceResponseResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TemplateAliasTypeDef = TypedDict(
    "TemplateAliasTypeDef",
    {
        "AliasName": str,
        "Arn": str,
        "TemplateVersionNumber": int,
    },
    total=False,
)

TemplateErrorTypeDef = TypedDict(
    "TemplateErrorTypeDef",
    {
        "Type": TemplateErrorTypeType,
        "Message": str,
    },
    total=False,
)

TemplateSourceAnalysisTypeDef = TypedDict(
    "TemplateSourceAnalysisTypeDef",
    {
        "Arn": str,
        "DataSetReferences": List["DataSetReferenceTypeDef"],
    },
)

TemplateSourceEntityTypeDef = TypedDict(
    "TemplateSourceEntityTypeDef",
    {
        "SourceAnalysis": "TemplateSourceAnalysisTypeDef",
        "SourceTemplate": "TemplateSourceTemplateTypeDef",
    },
    total=False,
)

TemplateSourceTemplateTypeDef = TypedDict(
    "TemplateSourceTemplateTypeDef",
    {
        "Arn": str,
    },
)

TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "Arn": str,
        "TemplateId": str,
        "Name": str,
        "LatestVersionNumber": int,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Version": "TemplateVersionTypeDef",
        "TemplateId": str,
        "LastUpdatedTime": datetime,
        "CreatedTime": datetime,
    },
    total=False,
)

TemplateVersionSummaryTypeDef = TypedDict(
    "TemplateVersionSummaryTypeDef",
    {
        "Arn": str,
        "VersionNumber": int,
        "CreatedTime": datetime,
        "Status": ResourceStatusType,
        "Description": str,
    },
    total=False,
)

TemplateVersionTypeDef = TypedDict(
    "TemplateVersionTypeDef",
    {
        "CreatedTime": datetime,
        "Errors": List["TemplateErrorTypeDef"],
        "VersionNumber": int,
        "Status": ResourceStatusType,
        "DataSetConfigurations": List["DataSetConfigurationTypeDef"],
        "Description": str,
        "SourceEntityArn": str,
        "ThemeArn": str,
        "Sheets": List["SheetTypeDef"],
    },
    total=False,
)

TeradataParametersTypeDef = TypedDict(
    "TeradataParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

ThemeAliasTypeDef = TypedDict(
    "ThemeAliasTypeDef",
    {
        "Arn": str,
        "AliasName": str,
        "ThemeVersionNumber": int,
    },
    total=False,
)

ThemeConfigurationTypeDef = TypedDict(
    "ThemeConfigurationTypeDef",
    {
        "DataColorPalette": "DataColorPaletteTypeDef",
        "UIColorPalette": "UIColorPaletteTypeDef",
        "Sheet": "SheetStyleTypeDef",
    },
    total=False,
)

ThemeErrorTypeDef = TypedDict(
    "ThemeErrorTypeDef",
    {
        "Type": Literal["INTERNAL_FAILURE"],
        "Message": str,
    },
    total=False,
)

ThemeSummaryTypeDef = TypedDict(
    "ThemeSummaryTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ThemeId": str,
        "LatestVersionNumber": int,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ThemeTypeDef = TypedDict(
    "ThemeTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ThemeId": str,
        "Version": "ThemeVersionTypeDef",
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "Type": ThemeTypeType,
    },
    total=False,
)

ThemeVersionSummaryTypeDef = TypedDict(
    "ThemeVersionSummaryTypeDef",
    {
        "VersionNumber": int,
        "Arn": str,
        "Description": str,
        "CreatedTime": datetime,
        "Status": ResourceStatusType,
    },
    total=False,
)

ThemeVersionTypeDef = TypedDict(
    "ThemeVersionTypeDef",
    {
        "VersionNumber": int,
        "Arn": str,
        "Description": str,
        "BaseThemeId": str,
        "CreatedTime": datetime,
        "Configuration": "ThemeConfigurationTypeDef",
        "Errors": List["ThemeErrorTypeDef"],
        "Status": ResourceStatusType,
    },
    total=False,
)

TileLayoutStyleTypeDef = TypedDict(
    "TileLayoutStyleTypeDef",
    {
        "Gutter": "GutterStyleTypeDef",
        "Margin": "MarginStyleTypeDef",
    },
    total=False,
)

TileStyleTypeDef = TypedDict(
    "TileStyleTypeDef",
    {
        "Border": "BorderStyleTypeDef",
    },
    total=False,
)

TransformOperationTypeDef = TypedDict(
    "TransformOperationTypeDef",
    {
        "ProjectOperation": "ProjectOperationTypeDef",
        "FilterOperation": "FilterOperationTypeDef",
        "CreateColumnsOperation": "CreateColumnsOperationTypeDef",
        "RenameColumnOperation": "RenameColumnOperationTypeDef",
        "CastColumnTypeOperation": "CastColumnTypeOperationTypeDef",
        "TagColumnOperation": "TagColumnOperationTypeDef",
    },
    total=False,
)

TwitterParametersTypeDef = TypedDict(
    "TwitterParametersTypeDef",
    {
        "Query": str,
        "MaxRows": int,
    },
)

UIColorPaletteTypeDef = TypedDict(
    "UIColorPaletteTypeDef",
    {
        "PrimaryForeground": str,
        "PrimaryBackground": str,
        "SecondaryForeground": str,
        "SecondaryBackground": str,
        "Accent": str,
        "AccentForeground": str,
        "Danger": str,
        "DangerForeground": str,
        "Warning": str,
        "WarningForeground": str,
        "Success": str,
        "SuccessForeground": str,
        "Dimension": str,
        "DimensionForeground": str,
        "Measure": str,
        "MeasureForeground": str,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UntagResourceResponseResponseTypeDef = TypedDict(
    "UntagResourceResponseResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAccountCustomizationRequestTypeDef = TypedDict(
    "_RequiredUpdateAccountCustomizationRequestTypeDef",
    {
        "AwsAccountId": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
    },
)
_OptionalUpdateAccountCustomizationRequestTypeDef = TypedDict(
    "_OptionalUpdateAccountCustomizationRequestTypeDef",
    {
        "Namespace": str,
    },
    total=False,
)


class UpdateAccountCustomizationRequestTypeDef(
    _RequiredUpdateAccountCustomizationRequestTypeDef,
    _OptionalUpdateAccountCustomizationRequestTypeDef,
):
    pass


UpdateAccountCustomizationResponseResponseTypeDef = TypedDict(
    "UpdateAccountCustomizationResponseResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAccountSettingsRequestTypeDef = TypedDict(
    "_RequiredUpdateAccountSettingsRequestTypeDef",
    {
        "AwsAccountId": str,
        "DefaultNamespace": str,
    },
)
_OptionalUpdateAccountSettingsRequestTypeDef = TypedDict(
    "_OptionalUpdateAccountSettingsRequestTypeDef",
    {
        "NotificationEmail": str,
    },
    total=False,
)


class UpdateAccountSettingsRequestTypeDef(
    _RequiredUpdateAccountSettingsRequestTypeDef, _OptionalUpdateAccountSettingsRequestTypeDef
):
    pass


UpdateAccountSettingsResponseResponseTypeDef = TypedDict(
    "UpdateAccountSettingsResponseResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAnalysisPermissionsRequestTypeDef = TypedDict(
    "_RequiredUpdateAnalysisPermissionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)
_OptionalUpdateAnalysisPermissionsRequestTypeDef = TypedDict(
    "_OptionalUpdateAnalysisPermissionsRequestTypeDef",
    {
        "GrantPermissions": List["ResourcePermissionTypeDef"],
        "RevokePermissions": List["ResourcePermissionTypeDef"],
    },
    total=False,
)


class UpdateAnalysisPermissionsRequestTypeDef(
    _RequiredUpdateAnalysisPermissionsRequestTypeDef,
    _OptionalUpdateAnalysisPermissionsRequestTypeDef,
):
    pass


UpdateAnalysisPermissionsResponseResponseTypeDef = TypedDict(
    "UpdateAnalysisPermissionsResponseResponseTypeDef",
    {
        "AnalysisArn": str,
        "AnalysisId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAnalysisRequestTypeDef = TypedDict(
    "_RequiredUpdateAnalysisRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
        "Name": str,
        "SourceEntity": "AnalysisSourceEntityTypeDef",
    },
)
_OptionalUpdateAnalysisRequestTypeDef = TypedDict(
    "_OptionalUpdateAnalysisRequestTypeDef",
    {
        "Parameters": "ParametersTypeDef",
        "ThemeArn": str,
    },
    total=False,
)


class UpdateAnalysisRequestTypeDef(
    _RequiredUpdateAnalysisRequestTypeDef, _OptionalUpdateAnalysisRequestTypeDef
):
    pass


UpdateAnalysisResponseResponseTypeDef = TypedDict(
    "UpdateAnalysisResponseResponseTypeDef",
    {
        "Arn": str,
        "AnalysisId": str,
        "UpdateStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDashboardPermissionsRequestTypeDef = TypedDict(
    "_RequiredUpdateDashboardPermissionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)
_OptionalUpdateDashboardPermissionsRequestTypeDef = TypedDict(
    "_OptionalUpdateDashboardPermissionsRequestTypeDef",
    {
        "GrantPermissions": List["ResourcePermissionTypeDef"],
        "RevokePermissions": List["ResourcePermissionTypeDef"],
    },
    total=False,
)


class UpdateDashboardPermissionsRequestTypeDef(
    _RequiredUpdateDashboardPermissionsRequestTypeDef,
    _OptionalUpdateDashboardPermissionsRequestTypeDef,
):
    pass


UpdateDashboardPermissionsResponseResponseTypeDef = TypedDict(
    "UpdateDashboardPermissionsResponseResponseTypeDef",
    {
        "DashboardArn": str,
        "DashboardId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDashboardPublishedVersionRequestTypeDef = TypedDict(
    "UpdateDashboardPublishedVersionRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "VersionNumber": int,
    },
)

UpdateDashboardPublishedVersionResponseResponseTypeDef = TypedDict(
    "UpdateDashboardPublishedVersionResponseResponseTypeDef",
    {
        "DashboardId": str,
        "DashboardArn": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDashboardRequestTypeDef = TypedDict(
    "_RequiredUpdateDashboardRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "Name": str,
        "SourceEntity": "DashboardSourceEntityTypeDef",
    },
)
_OptionalUpdateDashboardRequestTypeDef = TypedDict(
    "_OptionalUpdateDashboardRequestTypeDef",
    {
        "Parameters": "ParametersTypeDef",
        "VersionDescription": str,
        "DashboardPublishOptions": "DashboardPublishOptionsTypeDef",
        "ThemeArn": str,
    },
    total=False,
)


class UpdateDashboardRequestTypeDef(
    _RequiredUpdateDashboardRequestTypeDef, _OptionalUpdateDashboardRequestTypeDef
):
    pass


UpdateDashboardResponseResponseTypeDef = TypedDict(
    "UpdateDashboardResponseResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "DashboardId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDataSetPermissionsRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSetPermissionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)
_OptionalUpdateDataSetPermissionsRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSetPermissionsRequestTypeDef",
    {
        "GrantPermissions": List["ResourcePermissionTypeDef"],
        "RevokePermissions": List["ResourcePermissionTypeDef"],
    },
    total=False,
)


class UpdateDataSetPermissionsRequestTypeDef(
    _RequiredUpdateDataSetPermissionsRequestTypeDef, _OptionalUpdateDataSetPermissionsRequestTypeDef
):
    pass


UpdateDataSetPermissionsResponseResponseTypeDef = TypedDict(
    "UpdateDataSetPermissionsResponseResponseTypeDef",
    {
        "DataSetArn": str,
        "DataSetId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDataSetRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSetRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "Name": str,
        "PhysicalTableMap": Dict[str, "PhysicalTableTypeDef"],
        "ImportMode": DataSetImportModeType,
    },
)
_OptionalUpdateDataSetRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSetRequestTypeDef",
    {
        "LogicalTableMap": Dict[str, "LogicalTableTypeDef"],
        "ColumnGroups": List["ColumnGroupTypeDef"],
        "FieldFolders": Dict[str, "FieldFolderTypeDef"],
        "RowLevelPermissionDataSet": "RowLevelPermissionDataSetTypeDef",
        "ColumnLevelPermissionRules": List["ColumnLevelPermissionRuleTypeDef"],
    },
    total=False,
)


class UpdateDataSetRequestTypeDef(
    _RequiredUpdateDataSetRequestTypeDef, _OptionalUpdateDataSetRequestTypeDef
):
    pass


UpdateDataSetResponseResponseTypeDef = TypedDict(
    "UpdateDataSetResponseResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "IngestionArn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDataSourcePermissionsRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSourcePermissionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)
_OptionalUpdateDataSourcePermissionsRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSourcePermissionsRequestTypeDef",
    {
        "GrantPermissions": List["ResourcePermissionTypeDef"],
        "RevokePermissions": List["ResourcePermissionTypeDef"],
    },
    total=False,
)


class UpdateDataSourcePermissionsRequestTypeDef(
    _RequiredUpdateDataSourcePermissionsRequestTypeDef,
    _OptionalUpdateDataSourcePermissionsRequestTypeDef,
):
    pass


UpdateDataSourcePermissionsResponseResponseTypeDef = TypedDict(
    "UpdateDataSourcePermissionsResponseResponseTypeDef",
    {
        "DataSourceArn": str,
        "DataSourceId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDataSourceRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSourceRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
        "Name": str,
    },
)
_OptionalUpdateDataSourceRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSourceRequestTypeDef",
    {
        "DataSourceParameters": "DataSourceParametersTypeDef",
        "Credentials": "DataSourceCredentialsTypeDef",
        "VpcConnectionProperties": "VpcConnectionPropertiesTypeDef",
        "SslProperties": "SslPropertiesTypeDef",
    },
    total=False,
)


class UpdateDataSourceRequestTypeDef(
    _RequiredUpdateDataSourceRequestTypeDef, _OptionalUpdateDataSourceRequestTypeDef
):
    pass


UpdateDataSourceResponseResponseTypeDef = TypedDict(
    "UpdateDataSourceResponseResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "UpdateStatus": ResourceStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFolderPermissionsRequestTypeDef = TypedDict(
    "_RequiredUpdateFolderPermissionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)
_OptionalUpdateFolderPermissionsRequestTypeDef = TypedDict(
    "_OptionalUpdateFolderPermissionsRequestTypeDef",
    {
        "GrantPermissions": List["ResourcePermissionTypeDef"],
        "RevokePermissions": List["ResourcePermissionTypeDef"],
    },
    total=False,
)


class UpdateFolderPermissionsRequestTypeDef(
    _RequiredUpdateFolderPermissionsRequestTypeDef, _OptionalUpdateFolderPermissionsRequestTypeDef
):
    pass


UpdateFolderPermissionsResponseResponseTypeDef = TypedDict(
    "UpdateFolderPermissionsResponseResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFolderRequestTypeDef = TypedDict(
    "UpdateFolderRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "Name": str,
    },
)

UpdateFolderResponseResponseTypeDef = TypedDict(
    "UpdateFolderResponseResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGroupRequestTypeDef = TypedDict(
    "_RequiredUpdateGroupRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalUpdateGroupRequestTypeDef = TypedDict(
    "_OptionalUpdateGroupRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateGroupRequestTypeDef(
    _RequiredUpdateGroupRequestTypeDef, _OptionalUpdateGroupRequestTypeDef
):
    pass


UpdateGroupResponseResponseTypeDef = TypedDict(
    "UpdateGroupResponseResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateIAMPolicyAssignmentRequestTypeDef = TypedDict(
    "_RequiredUpdateIAMPolicyAssignmentRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "Namespace": str,
    },
)
_OptionalUpdateIAMPolicyAssignmentRequestTypeDef = TypedDict(
    "_OptionalUpdateIAMPolicyAssignmentRequestTypeDef",
    {
        "AssignmentStatus": AssignmentStatusType,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
    },
    total=False,
)


class UpdateIAMPolicyAssignmentRequestTypeDef(
    _RequiredUpdateIAMPolicyAssignmentRequestTypeDef,
    _OptionalUpdateIAMPolicyAssignmentRequestTypeDef,
):
    pass


UpdateIAMPolicyAssignmentResponseResponseTypeDef = TypedDict(
    "UpdateIAMPolicyAssignmentResponseResponseTypeDef",
    {
        "AssignmentName": str,
        "AssignmentId": str,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "AssignmentStatus": AssignmentStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTemplateAliasRequestTypeDef = TypedDict(
    "UpdateTemplateAliasRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
        "TemplateVersionNumber": int,
    },
)

UpdateTemplateAliasResponseResponseTypeDef = TypedDict(
    "UpdateTemplateAliasResponseResponseTypeDef",
    {
        "TemplateAlias": "TemplateAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTemplatePermissionsRequestTypeDef = TypedDict(
    "_RequiredUpdateTemplatePermissionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalUpdateTemplatePermissionsRequestTypeDef = TypedDict(
    "_OptionalUpdateTemplatePermissionsRequestTypeDef",
    {
        "GrantPermissions": List["ResourcePermissionTypeDef"],
        "RevokePermissions": List["ResourcePermissionTypeDef"],
    },
    total=False,
)


class UpdateTemplatePermissionsRequestTypeDef(
    _RequiredUpdateTemplatePermissionsRequestTypeDef,
    _OptionalUpdateTemplatePermissionsRequestTypeDef,
):
    pass


UpdateTemplatePermissionsResponseResponseTypeDef = TypedDict(
    "UpdateTemplatePermissionsResponseResponseTypeDef",
    {
        "TemplateId": str,
        "TemplateArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTemplateRequestTypeDef = TypedDict(
    "_RequiredUpdateTemplateRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "SourceEntity": "TemplateSourceEntityTypeDef",
    },
)
_OptionalUpdateTemplateRequestTypeDef = TypedDict(
    "_OptionalUpdateTemplateRequestTypeDef",
    {
        "VersionDescription": str,
        "Name": str,
    },
    total=False,
)


class UpdateTemplateRequestTypeDef(
    _RequiredUpdateTemplateRequestTypeDef, _OptionalUpdateTemplateRequestTypeDef
):
    pass


UpdateTemplateResponseResponseTypeDef = TypedDict(
    "UpdateTemplateResponseResponseTypeDef",
    {
        "TemplateId": str,
        "Arn": str,
        "VersionArn": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateThemeAliasRequestTypeDef = TypedDict(
    "UpdateThemeAliasRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
        "ThemeVersionNumber": int,
    },
)

UpdateThemeAliasResponseResponseTypeDef = TypedDict(
    "UpdateThemeAliasResponseResponseTypeDef",
    {
        "ThemeAlias": "ThemeAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateThemePermissionsRequestTypeDef = TypedDict(
    "_RequiredUpdateThemePermissionsRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
_OptionalUpdateThemePermissionsRequestTypeDef = TypedDict(
    "_OptionalUpdateThemePermissionsRequestTypeDef",
    {
        "GrantPermissions": List["ResourcePermissionTypeDef"],
        "RevokePermissions": List["ResourcePermissionTypeDef"],
    },
    total=False,
)


class UpdateThemePermissionsRequestTypeDef(
    _RequiredUpdateThemePermissionsRequestTypeDef, _OptionalUpdateThemePermissionsRequestTypeDef
):
    pass


UpdateThemePermissionsResponseResponseTypeDef = TypedDict(
    "UpdateThemePermissionsResponseResponseTypeDef",
    {
        "ThemeId": str,
        "ThemeArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateThemeRequestTypeDef = TypedDict(
    "_RequiredUpdateThemeRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "BaseThemeId": str,
    },
)
_OptionalUpdateThemeRequestTypeDef = TypedDict(
    "_OptionalUpdateThemeRequestTypeDef",
    {
        "Name": str,
        "VersionDescription": str,
        "Configuration": "ThemeConfigurationTypeDef",
    },
    total=False,
)


class UpdateThemeRequestTypeDef(
    _RequiredUpdateThemeRequestTypeDef, _OptionalUpdateThemeRequestTypeDef
):
    pass


UpdateThemeResponseResponseTypeDef = TypedDict(
    "UpdateThemeResponseResponseTypeDef",
    {
        "ThemeId": str,
        "Arn": str,
        "VersionArn": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
        "Email": str,
        "Role": UserRoleType,
    },
)
_OptionalUpdateUserRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestTypeDef",
    {
        "CustomPermissionsName": str,
        "UnapplyCustomPermissions": bool,
        "ExternalLoginFederationProviderType": str,
        "CustomFederationProviderUrl": str,
        "ExternalLoginId": str,
    },
    total=False,
)


class UpdateUserRequestTypeDef(
    _RequiredUpdateUserRequestTypeDef, _OptionalUpdateUserRequestTypeDef
):
    pass


UpdateUserResponseResponseTypeDef = TypedDict(
    "UpdateUserResponseResponseTypeDef",
    {
        "User": "UserTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadSettingsTypeDef = TypedDict(
    "UploadSettingsTypeDef",
    {
        "Format": FileFormatType,
        "StartFromRow": int,
        "ContainsHeader": bool,
        "TextQualifier": TextQualifierType,
        "Delimiter": str,
    },
    total=False,
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Email": str,
        "Role": UserRoleType,
        "IdentityType": IdentityTypeType,
        "Active": bool,
        "PrincipalId": str,
        "CustomPermissionsName": str,
        "ExternalLoginFederationProviderType": str,
        "ExternalLoginFederationProviderUrl": str,
        "ExternalLoginId": str,
    },
    total=False,
)

VpcConnectionPropertiesTypeDef = TypedDict(
    "VpcConnectionPropertiesTypeDef",
    {
        "VpcConnectionArn": str,
    },
)
