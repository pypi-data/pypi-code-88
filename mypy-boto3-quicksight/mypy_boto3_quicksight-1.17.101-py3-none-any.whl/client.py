"""
Type annotations for quicksight service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_quicksight import QuickSightClient

    client: QuickSightClient = boto3.client("quicksight")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    AssignmentStatusType,
    DataSetImportModeType,
    DataSourceTypeType,
    EmbeddingIdentityTypeType,
    IdentityTypeType,
    MemberTypeType,
    ThemeTypeType,
    UserRoleType,
)
from .paginator import (
    ListAnalysesPaginator,
    ListDashboardsPaginator,
    ListDashboardVersionsPaginator,
    ListDataSetsPaginator,
    ListDataSourcesPaginator,
    ListIngestionsPaginator,
    ListNamespacesPaginator,
    ListTemplateAliasesPaginator,
    ListTemplatesPaginator,
    ListTemplateVersionsPaginator,
    ListThemesPaginator,
    ListThemeVersionsPaginator,
    SearchAnalysesPaginator,
    SearchDashboardsPaginator,
)
from .type_defs import (
    AccountCustomizationTypeDef,
    AnalysisSearchFilterTypeDef,
    AnalysisSourceEntityTypeDef,
    CancelIngestionResponseTypeDef,
    ColumnGroupTypeDef,
    ColumnLevelPermissionRuleTypeDef,
    CreateAccountCustomizationResponseTypeDef,
    CreateAnalysisResponseTypeDef,
    CreateDashboardResponseTypeDef,
    CreateDataSetResponseTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateFolderMembershipResponseTypeDef,
    CreateFolderResponseTypeDef,
    CreateGroupMembershipResponseTypeDef,
    CreateGroupResponseTypeDef,
    CreateIAMPolicyAssignmentResponseTypeDef,
    CreateIngestionResponseTypeDef,
    CreateNamespaceResponseTypeDef,
    CreateTemplateAliasResponseTypeDef,
    CreateTemplateResponseTypeDef,
    CreateThemeAliasResponseTypeDef,
    CreateThemeResponseTypeDef,
    DashboardPublishOptionsTypeDef,
    DashboardSearchFilterTypeDef,
    DashboardSourceEntityTypeDef,
    DataSourceCredentialsTypeDef,
    DataSourceParametersTypeDef,
    DeleteAccountCustomizationResponseTypeDef,
    DeleteAnalysisResponseTypeDef,
    DeleteDashboardResponseTypeDef,
    DeleteDataSetResponseTypeDef,
    DeleteDataSourceResponseTypeDef,
    DeleteFolderMembershipResponseTypeDef,
    DeleteFolderResponseTypeDef,
    DeleteGroupMembershipResponseTypeDef,
    DeleteGroupResponseTypeDef,
    DeleteIAMPolicyAssignmentResponseTypeDef,
    DeleteNamespaceResponseTypeDef,
    DeleteTemplateAliasResponseTypeDef,
    DeleteTemplateResponseTypeDef,
    DeleteThemeAliasResponseTypeDef,
    DeleteThemeResponseTypeDef,
    DeleteUserByPrincipalIdResponseTypeDef,
    DeleteUserResponseTypeDef,
    DescribeAccountCustomizationResponseTypeDef,
    DescribeAccountSettingsResponseTypeDef,
    DescribeAnalysisPermissionsResponseTypeDef,
    DescribeAnalysisResponseTypeDef,
    DescribeDashboardPermissionsResponseTypeDef,
    DescribeDashboardResponseTypeDef,
    DescribeDataSetPermissionsResponseTypeDef,
    DescribeDataSetResponseTypeDef,
    DescribeDataSourcePermissionsResponseTypeDef,
    DescribeDataSourceResponseTypeDef,
    DescribeFolderPermissionsResponseTypeDef,
    DescribeFolderResolvedPermissionsResponseTypeDef,
    DescribeFolderResponseTypeDef,
    DescribeGroupResponseTypeDef,
    DescribeIAMPolicyAssignmentResponseTypeDef,
    DescribeIngestionResponseTypeDef,
    DescribeNamespaceResponseTypeDef,
    DescribeTemplateAliasResponseTypeDef,
    DescribeTemplatePermissionsResponseTypeDef,
    DescribeTemplateResponseTypeDef,
    DescribeThemeAliasResponseTypeDef,
    DescribeThemePermissionsResponseTypeDef,
    DescribeThemeResponseTypeDef,
    DescribeUserResponseTypeDef,
    FieldFolderTypeDef,
    FolderSearchFilterTypeDef,
    GetDashboardEmbedUrlResponseTypeDef,
    GetSessionEmbedUrlResponseTypeDef,
    ListAnalysesResponseTypeDef,
    ListDashboardsResponseTypeDef,
    ListDashboardVersionsResponseTypeDef,
    ListDataSetsResponseTypeDef,
    ListDataSourcesResponseTypeDef,
    ListFolderMembersResponseTypeDef,
    ListFoldersResponseTypeDef,
    ListGroupMembershipsResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListIAMPolicyAssignmentsForUserResponseTypeDef,
    ListIAMPolicyAssignmentsResponseTypeDef,
    ListIngestionsResponseTypeDef,
    ListNamespacesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplateAliasesResponseTypeDef,
    ListTemplatesResponseTypeDef,
    ListTemplateVersionsResponseTypeDef,
    ListThemeAliasesResponseTypeDef,
    ListThemesResponseTypeDef,
    ListThemeVersionsResponseTypeDef,
    ListUserGroupsResponseTypeDef,
    ListUsersResponseTypeDef,
    LogicalTableTypeDef,
    ParametersTypeDef,
    PhysicalTableTypeDef,
    RegisterUserResponseTypeDef,
    ResourcePermissionTypeDef,
    RestoreAnalysisResponseTypeDef,
    RowLevelPermissionDataSetTypeDef,
    SearchAnalysesResponseTypeDef,
    SearchDashboardsResponseTypeDef,
    SearchFoldersResponseTypeDef,
    SslPropertiesTypeDef,
    TagResourceResponseTypeDef,
    TagTypeDef,
    TemplateSourceEntityTypeDef,
    ThemeConfigurationTypeDef,
    UntagResourceResponseTypeDef,
    UpdateAccountCustomizationResponseTypeDef,
    UpdateAccountSettingsResponseTypeDef,
    UpdateAnalysisPermissionsResponseTypeDef,
    UpdateAnalysisResponseTypeDef,
    UpdateDashboardPermissionsResponseTypeDef,
    UpdateDashboardPublishedVersionResponseTypeDef,
    UpdateDashboardResponseTypeDef,
    UpdateDataSetPermissionsResponseTypeDef,
    UpdateDataSetResponseTypeDef,
    UpdateDataSourcePermissionsResponseTypeDef,
    UpdateDataSourceResponseTypeDef,
    UpdateFolderPermissionsResponseTypeDef,
    UpdateFolderResponseTypeDef,
    UpdateGroupResponseTypeDef,
    UpdateIAMPolicyAssignmentResponseTypeDef,
    UpdateTemplateAliasResponseTypeDef,
    UpdateTemplatePermissionsResponseTypeDef,
    UpdateTemplateResponseTypeDef,
    UpdateThemeAliasResponseTypeDef,
    UpdateThemePermissionsResponseTypeDef,
    UpdateThemeResponseTypeDef,
    UpdateUserResponseTypeDef,
    VpcConnectionPropertiesTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("QuickSightClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentUpdatingException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DomainNotWhitelistedException: Type[BotocoreClientError]
    IdentityTypeNotSupportedException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    PreconditionNotMetException: Type[BotocoreClientError]
    QuickSightUserNotFoundException: Type[BotocoreClientError]
    ResourceExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    SessionLifetimeInMinutesInvalidException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedPricingPlanException: Type[BotocoreClientError]
    UnsupportedUserEditionException: Type[BotocoreClientError]


class QuickSightClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#can_paginate)
        """

    def cancel_ingestion(
        self, *, AwsAccountId: str, DataSetId: str, IngestionId: str
    ) -> CancelIngestionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.cancel_ingestion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#cancel_ingestion)
        """

    def create_account_customization(
        self,
        *,
        AwsAccountId: str,
        AccountCustomization: "AccountCustomizationTypeDef",
        Namespace: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAccountCustomizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_account_customization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_account_customization)
        """

    def create_analysis(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
        Name: str,
        SourceEntity: AnalysisSourceEntityTypeDef,
        Parameters: ParametersTypeDef = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        ThemeArn: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAnalysisResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_analysis)
        """

    def create_dashboard(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        Name: str,
        SourceEntity: DashboardSourceEntityTypeDef,
        Parameters: ParametersTypeDef = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        VersionDescription: str = None,
        DashboardPublishOptions: DashboardPublishOptionsTypeDef = None,
        ThemeArn: str = None
    ) -> CreateDashboardResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_dashboard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_dashboard)
        """

    def create_data_set(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
        Name: str,
        PhysicalTableMap: Dict[str, "PhysicalTableTypeDef"],
        ImportMode: DataSetImportModeType,
        LogicalTableMap: Dict[str, "LogicalTableTypeDef"] = None,
        ColumnGroups: List["ColumnGroupTypeDef"] = None,
        FieldFolders: Dict[str, "FieldFolderTypeDef"] = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        RowLevelPermissionDataSet: "RowLevelPermissionDataSetTypeDef" = None,
        ColumnLevelPermissionRules: List["ColumnLevelPermissionRuleTypeDef"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDataSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_data_set)
        """

    def create_data_source(
        self,
        *,
        AwsAccountId: str,
        DataSourceId: str,
        Name: str,
        Type: DataSourceTypeType,
        DataSourceParameters: "DataSourceParametersTypeDef" = None,
        Credentials: DataSourceCredentialsTypeDef = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        VpcConnectionProperties: "VpcConnectionPropertiesTypeDef" = None,
        SslProperties: "SslPropertiesTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDataSourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_data_source)
        """

    def create_folder(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
        Name: str = None,
        FolderType: Literal["SHARED"] = None,
        ParentFolderArn: str = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateFolderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_folder)
        """

    def create_folder_membership(
        self, *, AwsAccountId: str, FolderId: str, MemberId: str, MemberType: MemberTypeType
    ) -> CreateFolderMembershipResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_folder_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_folder_membership)
        """

    def create_group(
        self, *, GroupName: str, AwsAccountId: str, Namespace: str, Description: str = None
    ) -> CreateGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_group)
        """

    def create_group_membership(
        self, *, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> CreateGroupMembershipResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_group_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_group_membership)
        """

    def create_iam_policy_assignment(
        self,
        *,
        AwsAccountId: str,
        AssignmentName: str,
        AssignmentStatus: AssignmentStatusType,
        Namespace: str,
        PolicyArn: str = None,
        Identities: Dict[str, List[str]] = None
    ) -> CreateIAMPolicyAssignmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_iam_policy_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_iam_policy_assignment)
        """

    def create_ingestion(
        self, *, DataSetId: str, IngestionId: str, AwsAccountId: str
    ) -> CreateIngestionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_ingestion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_ingestion)
        """

    def create_namespace(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        IdentityStore: Literal["QUICKSIGHT"],
        Tags: List["TagTypeDef"] = None
    ) -> CreateNamespaceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_namespace)
        """

    def create_template(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        SourceEntity: TemplateSourceEntityTypeDef,
        Name: str = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        VersionDescription: str = None
    ) -> CreateTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_template)
        """

    def create_template_alias(
        self, *, AwsAccountId: str, TemplateId: str, AliasName: str, TemplateVersionNumber: int
    ) -> CreateTemplateAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_template_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_template_alias)
        """

    def create_theme(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        Name: str,
        BaseThemeId: str,
        Configuration: "ThemeConfigurationTypeDef",
        VersionDescription: str = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateThemeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_theme)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_theme)
        """

    def create_theme_alias(
        self, *, AwsAccountId: str, ThemeId: str, AliasName: str, ThemeVersionNumber: int
    ) -> CreateThemeAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_theme_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_theme_alias)
        """

    def delete_account_customization(
        self, *, AwsAccountId: str, Namespace: str = None
    ) -> DeleteAccountCustomizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_account_customization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_account_customization)
        """

    def delete_analysis(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
        RecoveryWindowInDays: int = None,
        ForceDeleteWithoutRecovery: bool = None
    ) -> DeleteAnalysisResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_analysis)
        """

    def delete_dashboard(
        self, *, AwsAccountId: str, DashboardId: str, VersionNumber: int = None
    ) -> DeleteDashboardResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_dashboard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_dashboard)
        """

    def delete_data_set(self, *, AwsAccountId: str, DataSetId: str) -> DeleteDataSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_data_set)
        """

    def delete_data_source(
        self, *, AwsAccountId: str, DataSourceId: str
    ) -> DeleteDataSourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_data_source)
        """

    def delete_folder(self, *, AwsAccountId: str, FolderId: str) -> DeleteFolderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_folder)
        """

    def delete_folder_membership(
        self, *, AwsAccountId: str, FolderId: str, MemberId: str, MemberType: MemberTypeType
    ) -> DeleteFolderMembershipResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_folder_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_folder_membership)
        """

    def delete_group(
        self, *, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> DeleteGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_group)
        """

    def delete_group_membership(
        self, *, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> DeleteGroupMembershipResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_group_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_group_membership)
        """

    def delete_iam_policy_assignment(
        self, *, AwsAccountId: str, AssignmentName: str, Namespace: str
    ) -> DeleteIAMPolicyAssignmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_iam_policy_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_iam_policy_assignment)
        """

    def delete_namespace(
        self, *, AwsAccountId: str, Namespace: str
    ) -> DeleteNamespaceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_namespace)
        """

    def delete_template(
        self, *, AwsAccountId: str, TemplateId: str, VersionNumber: int = None
    ) -> DeleteTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_template)
        """

    def delete_template_alias(
        self, *, AwsAccountId: str, TemplateId: str, AliasName: str
    ) -> DeleteTemplateAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_template_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_template_alias)
        """

    def delete_theme(
        self, *, AwsAccountId: str, ThemeId: str, VersionNumber: int = None
    ) -> DeleteThemeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_theme)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_theme)
        """

    def delete_theme_alias(
        self, *, AwsAccountId: str, ThemeId: str, AliasName: str
    ) -> DeleteThemeAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_theme_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_theme_alias)
        """

    def delete_user(
        self, *, UserName: str, AwsAccountId: str, Namespace: str
    ) -> DeleteUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_user)
        """

    def delete_user_by_principal_id(
        self, *, PrincipalId: str, AwsAccountId: str, Namespace: str
    ) -> DeleteUserByPrincipalIdResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_user_by_principal_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_user_by_principal_id)
        """

    def describe_account_customization(
        self, *, AwsAccountId: str, Namespace: str = None, Resolved: bool = None
    ) -> DescribeAccountCustomizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_account_customization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_account_customization)
        """

    def describe_account_settings(
        self, *, AwsAccountId: str
    ) -> DescribeAccountSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_account_settings)
        """

    def describe_analysis(
        self, *, AwsAccountId: str, AnalysisId: str
    ) -> DescribeAnalysisResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_analysis)
        """

    def describe_analysis_permissions(
        self, *, AwsAccountId: str, AnalysisId: str
    ) -> DescribeAnalysisPermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_analysis_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_analysis_permissions)
        """

    def describe_dashboard(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        VersionNumber: int = None,
        AliasName: str = None
    ) -> DescribeDashboardResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_dashboard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_dashboard)
        """

    def describe_dashboard_permissions(
        self, *, AwsAccountId: str, DashboardId: str
    ) -> DescribeDashboardPermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_dashboard_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_dashboard_permissions)
        """

    def describe_data_set(
        self, *, AwsAccountId: str, DataSetId: str
    ) -> DescribeDataSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_data_set)
        """

    def describe_data_set_permissions(
        self, *, AwsAccountId: str, DataSetId: str
    ) -> DescribeDataSetPermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_data_set_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_data_set_permissions)
        """

    def describe_data_source(
        self, *, AwsAccountId: str, DataSourceId: str
    ) -> DescribeDataSourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_data_source)
        """

    def describe_data_source_permissions(
        self, *, AwsAccountId: str, DataSourceId: str
    ) -> DescribeDataSourcePermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_data_source_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_data_source_permissions)
        """

    def describe_folder(self, *, AwsAccountId: str, FolderId: str) -> DescribeFolderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_folder)
        """

    def describe_folder_permissions(
        self, *, AwsAccountId: str, FolderId: str
    ) -> DescribeFolderPermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_folder_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_folder_permissions)
        """

    def describe_folder_resolved_permissions(
        self, *, AwsAccountId: str, FolderId: str
    ) -> DescribeFolderResolvedPermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_folder_resolved_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_folder_resolved_permissions)
        """

    def describe_group(
        self, *, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> DescribeGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_group)
        """

    def describe_iam_policy_assignment(
        self, *, AwsAccountId: str, AssignmentName: str, Namespace: str
    ) -> DescribeIAMPolicyAssignmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_iam_policy_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_iam_policy_assignment)
        """

    def describe_ingestion(
        self, *, AwsAccountId: str, DataSetId: str, IngestionId: str
    ) -> DescribeIngestionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_ingestion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_ingestion)
        """

    def describe_namespace(
        self, *, AwsAccountId: str, Namespace: str
    ) -> DescribeNamespaceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_namespace)
        """

    def describe_template(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        VersionNumber: int = None,
        AliasName: str = None
    ) -> DescribeTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_template)
        """

    def describe_template_alias(
        self, *, AwsAccountId: str, TemplateId: str, AliasName: str
    ) -> DescribeTemplateAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_template_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_template_alias)
        """

    def describe_template_permissions(
        self, *, AwsAccountId: str, TemplateId: str
    ) -> DescribeTemplatePermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_template_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_template_permissions)
        """

    def describe_theme(
        self, *, AwsAccountId: str, ThemeId: str, VersionNumber: int = None, AliasName: str = None
    ) -> DescribeThemeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_theme)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_theme)
        """

    def describe_theme_alias(
        self, *, AwsAccountId: str, ThemeId: str, AliasName: str
    ) -> DescribeThemeAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_theme_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_theme_alias)
        """

    def describe_theme_permissions(
        self, *, AwsAccountId: str, ThemeId: str
    ) -> DescribeThemePermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_theme_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_theme_permissions)
        """

    def describe_user(
        self, *, UserName: str, AwsAccountId: str, Namespace: str
    ) -> DescribeUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_user)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#generate_presigned_url)
        """

    def get_dashboard_embed_url(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        IdentityType: EmbeddingIdentityTypeType,
        SessionLifetimeInMinutes: int = None,
        UndoRedoDisabled: bool = None,
        ResetDisabled: bool = None,
        StatePersistenceEnabled: bool = None,
        UserArn: str = None,
        Namespace: str = None,
        AdditionalDashboardIds: List[str] = None
    ) -> GetDashboardEmbedUrlResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.get_dashboard_embed_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#get_dashboard_embed_url)
        """

    def get_session_embed_url(
        self,
        *,
        AwsAccountId: str,
        EntryPoint: str = None,
        SessionLifetimeInMinutes: int = None,
        UserArn: str = None
    ) -> GetSessionEmbedUrlResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.get_session_embed_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#get_session_embed_url)
        """

    def list_analyses(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAnalysesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_analyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_analyses)
        """

    def list_dashboard_versions(
        self, *, AwsAccountId: str, DashboardId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDashboardVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_dashboard_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_dashboard_versions)
        """

    def list_dashboards(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDashboardsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_dashboards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_dashboards)
        """

    def list_data_sets(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDataSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_data_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_data_sets)
        """

    def list_data_sources(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDataSourcesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_data_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_data_sources)
        """

    def list_folder_members(
        self, *, AwsAccountId: str, FolderId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFolderMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_folder_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_folder_members)
        """

    def list_folders(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFoldersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_folders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_folders)
        """

    def list_group_memberships(
        self,
        *,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListGroupMembershipsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_group_memberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_group_memberships)
        """

    def list_groups(
        self, *, AwsAccountId: str, Namespace: str, NextToken: str = None, MaxResults: int = None
    ) -> ListGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_groups)
        """

    def list_iam_policy_assignments(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        AssignmentStatus: AssignmentStatusType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListIAMPolicyAssignmentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_iam_policy_assignments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_iam_policy_assignments)
        """

    def list_iam_policy_assignments_for_user(
        self,
        *,
        AwsAccountId: str,
        UserName: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListIAMPolicyAssignmentsForUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_iam_policy_assignments_for_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_iam_policy_assignments_for_user)
        """

    def list_ingestions(
        self, *, DataSetId: str, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListIngestionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_ingestions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_ingestions)
        """

    def list_namespaces(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListNamespacesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_namespaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_namespaces)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_tags_for_resource)
        """

    def list_template_aliases(
        self, *, AwsAccountId: str, TemplateId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTemplateAliasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_template_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_template_aliases)
        """

    def list_template_versions(
        self, *, AwsAccountId: str, TemplateId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTemplateVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_template_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_template_versions)
        """

    def list_templates(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTemplatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_templates)
        """

    def list_theme_aliases(
        self, *, AwsAccountId: str, ThemeId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListThemeAliasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_theme_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_theme_aliases)
        """

    def list_theme_versions(
        self, *, AwsAccountId: str, ThemeId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListThemeVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_theme_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_theme_versions)
        """

    def list_themes(
        self,
        *,
        AwsAccountId: str,
        NextToken: str = None,
        MaxResults: int = None,
        Type: ThemeTypeType = None
    ) -> ListThemesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_themes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_themes)
        """

    def list_user_groups(
        self,
        *,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListUserGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_user_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_user_groups)
        """

    def list_users(
        self, *, AwsAccountId: str, Namespace: str, NextToken: str = None, MaxResults: int = None
    ) -> ListUsersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_users)
        """

    def register_user(
        self,
        *,
        IdentityType: IdentityTypeType,
        Email: str,
        UserRole: UserRoleType,
        AwsAccountId: str,
        Namespace: str,
        IamArn: str = None,
        SessionName: str = None,
        UserName: str = None,
        CustomPermissionsName: str = None,
        ExternalLoginFederationProviderType: str = None,
        CustomFederationProviderUrl: str = None,
        ExternalLoginId: str = None
    ) -> RegisterUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.register_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#register_user)
        """

    def restore_analysis(
        self, *, AwsAccountId: str, AnalysisId: str
    ) -> RestoreAnalysisResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.restore_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#restore_analysis)
        """

    def search_analyses(
        self,
        *,
        AwsAccountId: str,
        Filters: List[AnalysisSearchFilterTypeDef],
        NextToken: str = None,
        MaxResults: int = None
    ) -> SearchAnalysesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.search_analyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#search_analyses)
        """

    def search_dashboards(
        self,
        *,
        AwsAccountId: str,
        Filters: List[DashboardSearchFilterTypeDef],
        NextToken: str = None,
        MaxResults: int = None
    ) -> SearchDashboardsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.search_dashboards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#search_dashboards)
        """

    def search_folders(
        self,
        *,
        AwsAccountId: str,
        Filters: List[FolderSearchFilterTypeDef],
        NextToken: str = None,
        MaxResults: int = None
    ) -> SearchFoldersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.search_folders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#search_folders)
        """

    def tag_resource(
        self, *, ResourceArn: str, Tags: List["TagTypeDef"]
    ) -> TagResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#tag_resource)
        """

    def untag_resource(
        self, *, ResourceArn: str, TagKeys: List[str]
    ) -> UntagResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#untag_resource)
        """

    def update_account_customization(
        self,
        *,
        AwsAccountId: str,
        AccountCustomization: "AccountCustomizationTypeDef",
        Namespace: str = None
    ) -> UpdateAccountCustomizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_account_customization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_account_customization)
        """

    def update_account_settings(
        self, *, AwsAccountId: str, DefaultNamespace: str, NotificationEmail: str = None
    ) -> UpdateAccountSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_account_settings)
        """

    def update_analysis(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
        Name: str,
        SourceEntity: AnalysisSourceEntityTypeDef,
        Parameters: ParametersTypeDef = None,
        ThemeArn: str = None
    ) -> UpdateAnalysisResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_analysis)
        """

    def update_analysis_permissions(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None
    ) -> UpdateAnalysisPermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_analysis_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_analysis_permissions)
        """

    def update_dashboard(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        Name: str,
        SourceEntity: DashboardSourceEntityTypeDef,
        Parameters: ParametersTypeDef = None,
        VersionDescription: str = None,
        DashboardPublishOptions: DashboardPublishOptionsTypeDef = None,
        ThemeArn: str = None
    ) -> UpdateDashboardResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_dashboard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_dashboard)
        """

    def update_dashboard_permissions(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None
    ) -> UpdateDashboardPermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_dashboard_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_dashboard_permissions)
        """

    def update_dashboard_published_version(
        self, *, AwsAccountId: str, DashboardId: str, VersionNumber: int
    ) -> UpdateDashboardPublishedVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_dashboard_published_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_dashboard_published_version)
        """

    def update_data_set(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
        Name: str,
        PhysicalTableMap: Dict[str, "PhysicalTableTypeDef"],
        ImportMode: DataSetImportModeType,
        LogicalTableMap: Dict[str, "LogicalTableTypeDef"] = None,
        ColumnGroups: List["ColumnGroupTypeDef"] = None,
        FieldFolders: Dict[str, "FieldFolderTypeDef"] = None,
        RowLevelPermissionDataSet: "RowLevelPermissionDataSetTypeDef" = None,
        ColumnLevelPermissionRules: List["ColumnLevelPermissionRuleTypeDef"] = None
    ) -> UpdateDataSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_data_set)
        """

    def update_data_set_permissions(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None
    ) -> UpdateDataSetPermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_data_set_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_data_set_permissions)
        """

    def update_data_source(
        self,
        *,
        AwsAccountId: str,
        DataSourceId: str,
        Name: str,
        DataSourceParameters: "DataSourceParametersTypeDef" = None,
        Credentials: DataSourceCredentialsTypeDef = None,
        VpcConnectionProperties: "VpcConnectionPropertiesTypeDef" = None,
        SslProperties: "SslPropertiesTypeDef" = None
    ) -> UpdateDataSourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_data_source)
        """

    def update_data_source_permissions(
        self,
        *,
        AwsAccountId: str,
        DataSourceId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None
    ) -> UpdateDataSourcePermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_data_source_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_data_source_permissions)
        """

    def update_folder(
        self, *, AwsAccountId: str, FolderId: str, Name: str
    ) -> UpdateFolderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_folder)
        """

    def update_folder_permissions(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None
    ) -> UpdateFolderPermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_folder_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_folder_permissions)
        """

    def update_group(
        self, *, GroupName: str, AwsAccountId: str, Namespace: str, Description: str = None
    ) -> UpdateGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_group)
        """

    def update_iam_policy_assignment(
        self,
        *,
        AwsAccountId: str,
        AssignmentName: str,
        Namespace: str,
        AssignmentStatus: AssignmentStatusType = None,
        PolicyArn: str = None,
        Identities: Dict[str, List[str]] = None
    ) -> UpdateIAMPolicyAssignmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_iam_policy_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_iam_policy_assignment)
        """

    def update_template(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        SourceEntity: TemplateSourceEntityTypeDef,
        VersionDescription: str = None,
        Name: str = None
    ) -> UpdateTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_template)
        """

    def update_template_alias(
        self, *, AwsAccountId: str, TemplateId: str, AliasName: str, TemplateVersionNumber: int
    ) -> UpdateTemplateAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_template_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_template_alias)
        """

    def update_template_permissions(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None
    ) -> UpdateTemplatePermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_template_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_template_permissions)
        """

    def update_theme(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        BaseThemeId: str,
        Name: str = None,
        VersionDescription: str = None,
        Configuration: "ThemeConfigurationTypeDef" = None
    ) -> UpdateThemeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_theme)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_theme)
        """

    def update_theme_alias(
        self, *, AwsAccountId: str, ThemeId: str, AliasName: str, ThemeVersionNumber: int
    ) -> UpdateThemeAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_theme_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_theme_alias)
        """

    def update_theme_permissions(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None
    ) -> UpdateThemePermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_theme_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_theme_permissions)
        """

    def update_user(
        self,
        *,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        Email: str,
        Role: UserRoleType,
        CustomPermissionsName: str = None,
        UnapplyCustomPermissions: bool = None,
        ExternalLoginFederationProviderType: str = None,
        CustomFederationProviderUrl: str = None,
        ExternalLoginId: str = None
    ) -> UpdateUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_user)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_analyses"]) -> ListAnalysesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListAnalyses)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listanalysespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dashboard_versions"]
    ) -> ListDashboardVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListDashboardVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdashboardversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_dashboards"]) -> ListDashboardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListDashboards)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdashboardspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_data_sets"]) -> ListDataSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListDataSets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdatasetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListDataSources)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdatasourcespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ingestions"]) -> ListIngestionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListIngestions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listingestionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_namespaces"]) -> ListNamespacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListNamespaces)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listnamespacespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_aliases"]
    ) -> ListTemplateAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateAliases)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplatealiasespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_versions"]
    ) -> ListTemplateVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplateversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_templates"]) -> ListTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListTemplates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_theme_versions"]
    ) -> ListThemeVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListThemeVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listthemeversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_themes"]) -> ListThemesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListThemes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listthemespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_analyses"]) -> SearchAnalysesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.SearchAnalyses)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchanalysespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_dashboards"]
    ) -> SearchDashboardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.SearchDashboards)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdashboardspaginator)
        """
