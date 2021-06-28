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
    CancelIngestionResponseResponseTypeDef,
    ColumnGroupTypeDef,
    ColumnLevelPermissionRuleTypeDef,
    CreateAccountCustomizationResponseResponseTypeDef,
    CreateAnalysisResponseResponseTypeDef,
    CreateDashboardResponseResponseTypeDef,
    CreateDataSetResponseResponseTypeDef,
    CreateDataSourceResponseResponseTypeDef,
    CreateFolderMembershipResponseResponseTypeDef,
    CreateFolderResponseResponseTypeDef,
    CreateGroupMembershipResponseResponseTypeDef,
    CreateGroupResponseResponseTypeDef,
    CreateIAMPolicyAssignmentResponseResponseTypeDef,
    CreateIngestionResponseResponseTypeDef,
    CreateNamespaceResponseResponseTypeDef,
    CreateTemplateAliasResponseResponseTypeDef,
    CreateTemplateResponseResponseTypeDef,
    CreateThemeAliasResponseResponseTypeDef,
    CreateThemeResponseResponseTypeDef,
    DashboardPublishOptionsTypeDef,
    DashboardSearchFilterTypeDef,
    DashboardSourceEntityTypeDef,
    DataSourceCredentialsTypeDef,
    DataSourceParametersTypeDef,
    DeleteAccountCustomizationResponseResponseTypeDef,
    DeleteAnalysisResponseResponseTypeDef,
    DeleteDashboardResponseResponseTypeDef,
    DeleteDataSetResponseResponseTypeDef,
    DeleteDataSourceResponseResponseTypeDef,
    DeleteFolderMembershipResponseResponseTypeDef,
    DeleteFolderResponseResponseTypeDef,
    DeleteGroupMembershipResponseResponseTypeDef,
    DeleteGroupResponseResponseTypeDef,
    DeleteIAMPolicyAssignmentResponseResponseTypeDef,
    DeleteNamespaceResponseResponseTypeDef,
    DeleteTemplateAliasResponseResponseTypeDef,
    DeleteTemplateResponseResponseTypeDef,
    DeleteThemeAliasResponseResponseTypeDef,
    DeleteThemeResponseResponseTypeDef,
    DeleteUserByPrincipalIdResponseResponseTypeDef,
    DeleteUserResponseResponseTypeDef,
    DescribeAccountCustomizationResponseResponseTypeDef,
    DescribeAccountSettingsResponseResponseTypeDef,
    DescribeAnalysisPermissionsResponseResponseTypeDef,
    DescribeAnalysisResponseResponseTypeDef,
    DescribeDashboardPermissionsResponseResponseTypeDef,
    DescribeDashboardResponseResponseTypeDef,
    DescribeDataSetPermissionsResponseResponseTypeDef,
    DescribeDataSetResponseResponseTypeDef,
    DescribeDataSourcePermissionsResponseResponseTypeDef,
    DescribeDataSourceResponseResponseTypeDef,
    DescribeFolderPermissionsResponseResponseTypeDef,
    DescribeFolderResolvedPermissionsResponseResponseTypeDef,
    DescribeFolderResponseResponseTypeDef,
    DescribeGroupResponseResponseTypeDef,
    DescribeIAMPolicyAssignmentResponseResponseTypeDef,
    DescribeIngestionResponseResponseTypeDef,
    DescribeNamespaceResponseResponseTypeDef,
    DescribeTemplateAliasResponseResponseTypeDef,
    DescribeTemplatePermissionsResponseResponseTypeDef,
    DescribeTemplateResponseResponseTypeDef,
    DescribeThemeAliasResponseResponseTypeDef,
    DescribeThemePermissionsResponseResponseTypeDef,
    DescribeThemeResponseResponseTypeDef,
    DescribeUserResponseResponseTypeDef,
    FieldFolderTypeDef,
    FolderSearchFilterTypeDef,
    GetDashboardEmbedUrlResponseResponseTypeDef,
    GetSessionEmbedUrlResponseResponseTypeDef,
    ListAnalysesResponseResponseTypeDef,
    ListDashboardsResponseResponseTypeDef,
    ListDashboardVersionsResponseResponseTypeDef,
    ListDataSetsResponseResponseTypeDef,
    ListDataSourcesResponseResponseTypeDef,
    ListFolderMembersResponseResponseTypeDef,
    ListFoldersResponseResponseTypeDef,
    ListGroupMembershipsResponseResponseTypeDef,
    ListGroupsResponseResponseTypeDef,
    ListIAMPolicyAssignmentsForUserResponseResponseTypeDef,
    ListIAMPolicyAssignmentsResponseResponseTypeDef,
    ListIngestionsResponseResponseTypeDef,
    ListNamespacesResponseResponseTypeDef,
    ListTagsForResourceResponseResponseTypeDef,
    ListTemplateAliasesResponseResponseTypeDef,
    ListTemplatesResponseResponseTypeDef,
    ListTemplateVersionsResponseResponseTypeDef,
    ListThemeAliasesResponseResponseTypeDef,
    ListThemesResponseResponseTypeDef,
    ListThemeVersionsResponseResponseTypeDef,
    ListUserGroupsResponseResponseTypeDef,
    ListUsersResponseResponseTypeDef,
    LogicalTableTypeDef,
    ParametersTypeDef,
    PhysicalTableTypeDef,
    RegisterUserResponseResponseTypeDef,
    ResourcePermissionTypeDef,
    RestoreAnalysisResponseResponseTypeDef,
    RowLevelPermissionDataSetTypeDef,
    SearchAnalysesResponseResponseTypeDef,
    SearchDashboardsResponseResponseTypeDef,
    SearchFoldersResponseResponseTypeDef,
    SslPropertiesTypeDef,
    TagResourceResponseResponseTypeDef,
    TagTypeDef,
    TemplateSourceEntityTypeDef,
    ThemeConfigurationTypeDef,
    UntagResourceResponseResponseTypeDef,
    UpdateAccountCustomizationResponseResponseTypeDef,
    UpdateAccountSettingsResponseResponseTypeDef,
    UpdateAnalysisPermissionsResponseResponseTypeDef,
    UpdateAnalysisResponseResponseTypeDef,
    UpdateDashboardPermissionsResponseResponseTypeDef,
    UpdateDashboardPublishedVersionResponseResponseTypeDef,
    UpdateDashboardResponseResponseTypeDef,
    UpdateDataSetPermissionsResponseResponseTypeDef,
    UpdateDataSetResponseResponseTypeDef,
    UpdateDataSourcePermissionsResponseResponseTypeDef,
    UpdateDataSourceResponseResponseTypeDef,
    UpdateFolderPermissionsResponseResponseTypeDef,
    UpdateFolderResponseResponseTypeDef,
    UpdateGroupResponseResponseTypeDef,
    UpdateIAMPolicyAssignmentResponseResponseTypeDef,
    UpdateTemplateAliasResponseResponseTypeDef,
    UpdateTemplatePermissionsResponseResponseTypeDef,
    UpdateTemplateResponseResponseTypeDef,
    UpdateThemeAliasResponseResponseTypeDef,
    UpdateThemePermissionsResponseResponseTypeDef,
    UpdateThemeResponseResponseTypeDef,
    UpdateUserResponseResponseTypeDef,
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
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#can_paginate)
        """

    def cancel_ingestion(
        self, *, AwsAccountId: str, DataSetId: str, IngestionId: str
    ) -> CancelIngestionResponseResponseTypeDef:
        """
        Cancels an ongoing ingestion of data into SPICE.

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
    ) -> CreateAccountCustomizationResponseResponseTypeDef:
        """
        Creates Amazon QuickSight customizations the current AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_account_customization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_account_customization)
        """

    def create_analysis(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
        Name: str,
        SourceEntity: "AnalysisSourceEntityTypeDef",
        Parameters: "ParametersTypeDef" = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        ThemeArn: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAnalysisResponseResponseTypeDef:
        """
        Creates an analysis in Amazon QuickSight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_analysis)
        """

    def create_dashboard(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        Name: str,
        SourceEntity: "DashboardSourceEntityTypeDef",
        Parameters: "ParametersTypeDef" = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        VersionDescription: str = None,
        DashboardPublishOptions: "DashboardPublishOptionsTypeDef" = None,
        ThemeArn: str = None
    ) -> CreateDashboardResponseResponseTypeDef:
        """
        Creates a dashboard from a template.

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
    ) -> CreateDataSetResponseResponseTypeDef:
        """
        Creates a dataset.

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
        Credentials: "DataSourceCredentialsTypeDef" = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        VpcConnectionProperties: "VpcConnectionPropertiesTypeDef" = None,
        SslProperties: "SslPropertiesTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDataSourceResponseResponseTypeDef:
        """
        Creates a data source.

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
    ) -> CreateFolderResponseResponseTypeDef:
        """
        Creates an empty shared folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_folder)
        """

    def create_folder_membership(
        self, *, AwsAccountId: str, FolderId: str, MemberId: str, MemberType: MemberTypeType
    ) -> CreateFolderMembershipResponseResponseTypeDef:
        """
        Adds an asset, such as a dashboard, analysis, or dataset into a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_folder_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_folder_membership)
        """

    def create_group(
        self, *, GroupName: str, AwsAccountId: str, Namespace: str, Description: str = None
    ) -> CreateGroupResponseResponseTypeDef:
        """
        Creates an Amazon QuickSight group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_group)
        """

    def create_group_membership(
        self, *, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> CreateGroupMembershipResponseResponseTypeDef:
        """
        Adds an Amazon QuickSight user to an Amazon QuickSight group.

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
    ) -> CreateIAMPolicyAssignmentResponseResponseTypeDef:
        """
        Creates an assignment with one specified IAM policy, identified by its Amazon
        Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_iam_policy_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_iam_policy_assignment)
        """

    def create_ingestion(
        self, *, DataSetId: str, IngestionId: str, AwsAccountId: str
    ) -> CreateIngestionResponseResponseTypeDef:
        """
        Creates and starts a new SPICE ingestion on a dataset Any ingestions operating
        on tagged datasets inherit the same tags automatically for use in access
        control.

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
    ) -> CreateNamespaceResponseResponseTypeDef:
        """
        (Enterprise edition only) Creates a new namespace for you to use with Amazon
        QuickSight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_namespace)
        """

    def create_template(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        SourceEntity: "TemplateSourceEntityTypeDef",
        Name: str = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        VersionDescription: str = None
    ) -> CreateTemplateResponseResponseTypeDef:
        """
        Creates a template from an existing QuickSight analysis or template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_template)
        """

    def create_template_alias(
        self, *, AwsAccountId: str, TemplateId: str, AliasName: str, TemplateVersionNumber: int
    ) -> CreateTemplateAliasResponseResponseTypeDef:
        """
        Creates a template alias for a template.

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
    ) -> CreateThemeResponseResponseTypeDef:
        """
        Creates a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_theme)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_theme)
        """

    def create_theme_alias(
        self, *, AwsAccountId: str, ThemeId: str, AliasName: str, ThemeVersionNumber: int
    ) -> CreateThemeAliasResponseResponseTypeDef:
        """
        Creates a theme alias for a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.create_theme_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_theme_alias)
        """

    def delete_account_customization(
        self, *, AwsAccountId: str, Namespace: str = None
    ) -> DeleteAccountCustomizationResponseResponseTypeDef:
        """
        Deletes all Amazon QuickSight customizations in this AWS Region for the
        specified AWS account and QuickSight namespace.

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
    ) -> DeleteAnalysisResponseResponseTypeDef:
        """
        Deletes an analysis from Amazon QuickSight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_analysis)
        """

    def delete_dashboard(
        self, *, AwsAccountId: str, DashboardId: str, VersionNumber: int = None
    ) -> DeleteDashboardResponseResponseTypeDef:
        """
        Deletes a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_dashboard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_dashboard)
        """

    def delete_data_set(
        self, *, AwsAccountId: str, DataSetId: str
    ) -> DeleteDataSetResponseResponseTypeDef:
        """
        Deletes a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_data_set)
        """

    def delete_data_source(
        self, *, AwsAccountId: str, DataSourceId: str
    ) -> DeleteDataSourceResponseResponseTypeDef:
        """
        Deletes the data source permanently.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_data_source)
        """

    def delete_folder(
        self, *, AwsAccountId: str, FolderId: str
    ) -> DeleteFolderResponseResponseTypeDef:
        """
        Deletes an empty folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_folder)
        """

    def delete_folder_membership(
        self, *, AwsAccountId: str, FolderId: str, MemberId: str, MemberType: MemberTypeType
    ) -> DeleteFolderMembershipResponseResponseTypeDef:
        """
        Removes an asset, such as a dashboard, analysis, or dataset, from a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_folder_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_folder_membership)
        """

    def delete_group(
        self, *, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> DeleteGroupResponseResponseTypeDef:
        """
        Removes a user group from Amazon QuickSight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_group)
        """

    def delete_group_membership(
        self, *, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> DeleteGroupMembershipResponseResponseTypeDef:
        """
        Removes a user from a group so that the user is no longer a member of the group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_group_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_group_membership)
        """

    def delete_iam_policy_assignment(
        self, *, AwsAccountId: str, AssignmentName: str, Namespace: str
    ) -> DeleteIAMPolicyAssignmentResponseResponseTypeDef:
        """
        Deletes an existing IAM policy assignment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_iam_policy_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_iam_policy_assignment)
        """

    def delete_namespace(
        self, *, AwsAccountId: str, Namespace: str
    ) -> DeleteNamespaceResponseResponseTypeDef:
        """
        Deletes a namespace and the users and groups that are associated with the
        namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_namespace)
        """

    def delete_template(
        self, *, AwsAccountId: str, TemplateId: str, VersionNumber: int = None
    ) -> DeleteTemplateResponseResponseTypeDef:
        """
        Deletes a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_template)
        """

    def delete_template_alias(
        self, *, AwsAccountId: str, TemplateId: str, AliasName: str
    ) -> DeleteTemplateAliasResponseResponseTypeDef:
        """
        Deletes the item that the specified template alias points to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_template_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_template_alias)
        """

    def delete_theme(
        self, *, AwsAccountId: str, ThemeId: str, VersionNumber: int = None
    ) -> DeleteThemeResponseResponseTypeDef:
        """
        Deletes a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_theme)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_theme)
        """

    def delete_theme_alias(
        self, *, AwsAccountId: str, ThemeId: str, AliasName: str
    ) -> DeleteThemeAliasResponseResponseTypeDef:
        """
        Deletes the version of the theme that the specified theme alias points to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_theme_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_theme_alias)
        """

    def delete_user(
        self, *, UserName: str, AwsAccountId: str, Namespace: str
    ) -> DeleteUserResponseResponseTypeDef:
        """
        Deletes the Amazon QuickSight user that is associated with the identity of the
        AWS Identity and Access Management (IAM) user or role that's making the call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_user)
        """

    def delete_user_by_principal_id(
        self, *, PrincipalId: str, AwsAccountId: str, Namespace: str
    ) -> DeleteUserByPrincipalIdResponseResponseTypeDef:
        """
        Deletes a user identified by its principal ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.delete_user_by_principal_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_user_by_principal_id)
        """

    def describe_account_customization(
        self, *, AwsAccountId: str, Namespace: str = None, Resolved: bool = None
    ) -> DescribeAccountCustomizationResponseResponseTypeDef:
        """
        Describes the customizations associated with the provided AWS account and Amazon
        QuickSight namespace in an AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_account_customization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_account_customization)
        """

    def describe_account_settings(
        self, *, AwsAccountId: str
    ) -> DescribeAccountSettingsResponseResponseTypeDef:
        """
        Describes the settings that were used when your QuickSight subscription was
        first created in this AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_account_settings)
        """

    def describe_analysis(
        self, *, AwsAccountId: str, AnalysisId: str
    ) -> DescribeAnalysisResponseResponseTypeDef:
        """
        Provides a summary of the metadata for an analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_analysis)
        """

    def describe_analysis_permissions(
        self, *, AwsAccountId: str, AnalysisId: str
    ) -> DescribeAnalysisPermissionsResponseResponseTypeDef:
        """
        Provides the read and write permissions for an analysis.

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
    ) -> DescribeDashboardResponseResponseTypeDef:
        """
        Provides a summary for a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_dashboard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_dashboard)
        """

    def describe_dashboard_permissions(
        self, *, AwsAccountId: str, DashboardId: str
    ) -> DescribeDashboardPermissionsResponseResponseTypeDef:
        """
        Describes read and write permissions for a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_dashboard_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_dashboard_permissions)
        """

    def describe_data_set(
        self, *, AwsAccountId: str, DataSetId: str
    ) -> DescribeDataSetResponseResponseTypeDef:
        """
        Describes a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_data_set)
        """

    def describe_data_set_permissions(
        self, *, AwsAccountId: str, DataSetId: str
    ) -> DescribeDataSetPermissionsResponseResponseTypeDef:
        """
        Describes the permissions on a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_data_set_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_data_set_permissions)
        """

    def describe_data_source(
        self, *, AwsAccountId: str, DataSourceId: str
    ) -> DescribeDataSourceResponseResponseTypeDef:
        """
        Describes a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_data_source)
        """

    def describe_data_source_permissions(
        self, *, AwsAccountId: str, DataSourceId: str
    ) -> DescribeDataSourcePermissionsResponseResponseTypeDef:
        """
        Describes the resource permissions for a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_data_source_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_data_source_permissions)
        """

    def describe_folder(
        self, *, AwsAccountId: str, FolderId: str
    ) -> DescribeFolderResponseResponseTypeDef:
        """
        Describes a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_folder)
        """

    def describe_folder_permissions(
        self, *, AwsAccountId: str, FolderId: str
    ) -> DescribeFolderPermissionsResponseResponseTypeDef:
        """
        Describes permissions for a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_folder_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_folder_permissions)
        """

    def describe_folder_resolved_permissions(
        self, *, AwsAccountId: str, FolderId: str
    ) -> DescribeFolderResolvedPermissionsResponseResponseTypeDef:
        """
        Describes the folder resolved permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_folder_resolved_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_folder_resolved_permissions)
        """

    def describe_group(
        self, *, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> DescribeGroupResponseResponseTypeDef:
        """
        Returns an Amazon QuickSight group's description and Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_group)
        """

    def describe_iam_policy_assignment(
        self, *, AwsAccountId: str, AssignmentName: str, Namespace: str
    ) -> DescribeIAMPolicyAssignmentResponseResponseTypeDef:
        """
        Describes an existing IAM policy assignment, as specified by the assignment
        name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_iam_policy_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_iam_policy_assignment)
        """

    def describe_ingestion(
        self, *, AwsAccountId: str, DataSetId: str, IngestionId: str
    ) -> DescribeIngestionResponseResponseTypeDef:
        """
        Describes a SPICE ingestion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_ingestion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_ingestion)
        """

    def describe_namespace(
        self, *, AwsAccountId: str, Namespace: str
    ) -> DescribeNamespaceResponseResponseTypeDef:
        """
        Describes the current namespace.

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
    ) -> DescribeTemplateResponseResponseTypeDef:
        """
        Describes a template's metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_template)
        """

    def describe_template_alias(
        self, *, AwsAccountId: str, TemplateId: str, AliasName: str
    ) -> DescribeTemplateAliasResponseResponseTypeDef:
        """
        Describes the template alias for a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_template_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_template_alias)
        """

    def describe_template_permissions(
        self, *, AwsAccountId: str, TemplateId: str
    ) -> DescribeTemplatePermissionsResponseResponseTypeDef:
        """
        Describes read and write permissions on a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_template_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_template_permissions)
        """

    def describe_theme(
        self, *, AwsAccountId: str, ThemeId: str, VersionNumber: int = None, AliasName: str = None
    ) -> DescribeThemeResponseResponseTypeDef:
        """
        Describes a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_theme)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_theme)
        """

    def describe_theme_alias(
        self, *, AwsAccountId: str, ThemeId: str, AliasName: str
    ) -> DescribeThemeAliasResponseResponseTypeDef:
        """
        Describes the alias for a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_theme_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_theme_alias)
        """

    def describe_theme_permissions(
        self, *, AwsAccountId: str, ThemeId: str
    ) -> DescribeThemePermissionsResponseResponseTypeDef:
        """
        Describes the read and write permissions for a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.describe_theme_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_theme_permissions)
        """

    def describe_user(
        self, *, UserName: str, AwsAccountId: str, Namespace: str
    ) -> DescribeUserResponseResponseTypeDef:
        """
        Returns information about a user, given the user name.

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
        Generate a presigned url given a client, its method, and arguments.

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
    ) -> GetDashboardEmbedUrlResponseResponseTypeDef:
        """
        Generates a session URL and authorization code that you can use to embed an
        Amazon QuickSight read-only dashboard in your web server code.

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
    ) -> GetSessionEmbedUrlResponseResponseTypeDef:
        """
        Generates a session URL and authorization code that you can use to embed the
        Amazon QuickSight console in your web server code.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.get_session_embed_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#get_session_embed_url)
        """

    def list_analyses(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAnalysesResponseResponseTypeDef:
        """
        Lists Amazon QuickSight analyses that exist in the specified AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_analyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_analyses)
        """

    def list_dashboard_versions(
        self, *, AwsAccountId: str, DashboardId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDashboardVersionsResponseResponseTypeDef:
        """
        Lists all the versions of the dashboards in the QuickSight subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_dashboard_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_dashboard_versions)
        """

    def list_dashboards(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDashboardsResponseResponseTypeDef:
        """
        Lists dashboards in an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_dashboards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_dashboards)
        """

    def list_data_sets(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDataSetsResponseResponseTypeDef:
        """
        Lists all of the datasets belonging to the current AWS account in an AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_data_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_data_sets)
        """

    def list_data_sources(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDataSourcesResponseResponseTypeDef:
        """
        Lists data sources in current AWS Region that belong to this AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_data_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_data_sources)
        """

    def list_folder_members(
        self, *, AwsAccountId: str, FolderId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFolderMembersResponseResponseTypeDef:
        """
        List all assets (`DASHBOARD` , `ANALYSIS` , and `DATASET` ) in a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_folder_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_folder_members)
        """

    def list_folders(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFoldersResponseResponseTypeDef:
        """
        Lists all folders in an account.

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
    ) -> ListGroupMembershipsResponseResponseTypeDef:
        """
        Lists member users in a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_group_memberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_group_memberships)
        """

    def list_groups(
        self, *, AwsAccountId: str, Namespace: str, NextToken: str = None, MaxResults: int = None
    ) -> ListGroupsResponseResponseTypeDef:
        """
        Lists all user groups in Amazon QuickSight.

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
    ) -> ListIAMPolicyAssignmentsResponseResponseTypeDef:
        """
        Lists IAM policy assignments in the current Amazon QuickSight account.

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
    ) -> ListIAMPolicyAssignmentsForUserResponseResponseTypeDef:
        """
        Lists all the IAM policy assignments, including the Amazon Resource Names (ARNs)
        for the IAM policies assigned to the specified user and group or groups that the
        user belongs to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_iam_policy_assignments_for_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_iam_policy_assignments_for_user)
        """

    def list_ingestions(
        self, *, DataSetId: str, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListIngestionsResponseResponseTypeDef:
        """
        Lists the history of SPICE ingestions for a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_ingestions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_ingestions)
        """

    def list_namespaces(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListNamespacesResponseResponseTypeDef:
        """
        Lists the namespaces for the specified AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_namespaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_namespaces)
        """

    def list_tags_for_resource(
        self, *, ResourceArn: str
    ) -> ListTagsForResourceResponseResponseTypeDef:
        """
        Lists the tags assigned to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_tags_for_resource)
        """

    def list_template_aliases(
        self, *, AwsAccountId: str, TemplateId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTemplateAliasesResponseResponseTypeDef:
        """
        Lists all the aliases of a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_template_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_template_aliases)
        """

    def list_template_versions(
        self, *, AwsAccountId: str, TemplateId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTemplateVersionsResponseResponseTypeDef:
        """
        Lists all the versions of the templates in the current Amazon QuickSight
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_template_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_template_versions)
        """

    def list_templates(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTemplatesResponseResponseTypeDef:
        """
        Lists all the templates in the current Amazon QuickSight account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_templates)
        """

    def list_theme_aliases(
        self, *, AwsAccountId: str, ThemeId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListThemeAliasesResponseResponseTypeDef:
        """
        Lists all the aliases of a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_theme_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_theme_aliases)
        """

    def list_theme_versions(
        self, *, AwsAccountId: str, ThemeId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListThemeVersionsResponseResponseTypeDef:
        """
        Lists all the versions of the themes in the current AWS account.

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
    ) -> ListThemesResponseResponseTypeDef:
        """
        Lists all the themes in the current AWS account.

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
    ) -> ListUserGroupsResponseResponseTypeDef:
        """
        Lists the Amazon QuickSight groups that an Amazon QuickSight user is a member
        of.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.list_user_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_user_groups)
        """

    def list_users(
        self, *, AwsAccountId: str, Namespace: str, NextToken: str = None, MaxResults: int = None
    ) -> ListUsersResponseResponseTypeDef:
        """
        Returns a list of all of the Amazon QuickSight users belonging to this account.

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
    ) -> RegisterUserResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.register_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#register_user)
        """

    def restore_analysis(
        self, *, AwsAccountId: str, AnalysisId: str
    ) -> RestoreAnalysisResponseResponseTypeDef:
        """
        Restores an analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.restore_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#restore_analysis)
        """

    def search_analyses(
        self,
        *,
        AwsAccountId: str,
        Filters: List["AnalysisSearchFilterTypeDef"],
        NextToken: str = None,
        MaxResults: int = None
    ) -> SearchAnalysesResponseResponseTypeDef:
        """
        Searches for analyses that belong to the user specified in the filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.search_analyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#search_analyses)
        """

    def search_dashboards(
        self,
        *,
        AwsAccountId: str,
        Filters: List["DashboardSearchFilterTypeDef"],
        NextToken: str = None,
        MaxResults: int = None
    ) -> SearchDashboardsResponseResponseTypeDef:
        """
        Searches for dashboards that belong to a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.search_dashboards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#search_dashboards)
        """

    def search_folders(
        self,
        *,
        AwsAccountId: str,
        Filters: List["FolderSearchFilterTypeDef"],
        NextToken: str = None,
        MaxResults: int = None
    ) -> SearchFoldersResponseResponseTypeDef:
        """
        Searches the subfolders in a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.search_folders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#search_folders)
        """

    def tag_resource(
        self, *, ResourceArn: str, Tags: List["TagTypeDef"]
    ) -> TagResourceResponseResponseTypeDef:
        """
        Assigns one or more tags (key-value pairs) to the specified QuickSight resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#tag_resource)
        """

    def untag_resource(
        self, *, ResourceArn: str, TagKeys: List[str]
    ) -> UntagResourceResponseResponseTypeDef:
        """
        Removes a tag or tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#untag_resource)
        """

    def update_account_customization(
        self,
        *,
        AwsAccountId: str,
        AccountCustomization: "AccountCustomizationTypeDef",
        Namespace: str = None
    ) -> UpdateAccountCustomizationResponseResponseTypeDef:
        """
        Updates Amazon QuickSight customizations the current AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_account_customization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_account_customization)
        """

    def update_account_settings(
        self, *, AwsAccountId: str, DefaultNamespace: str, NotificationEmail: str = None
    ) -> UpdateAccountSettingsResponseResponseTypeDef:
        """
        Updates the Amazon QuickSight settings in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_account_settings)
        """

    def update_analysis(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
        Name: str,
        SourceEntity: "AnalysisSourceEntityTypeDef",
        Parameters: "ParametersTypeDef" = None,
        ThemeArn: str = None
    ) -> UpdateAnalysisResponseResponseTypeDef:
        """
        Updates an analysis in Amazon QuickSight See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/UpdateAnalysis>`_
        **Request Syntax** response = client.update_analysis( AwsAccountId='string',
        AnalysisId='string', Name='string',...

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
    ) -> UpdateAnalysisPermissionsResponseResponseTypeDef:
        """
        Updates the read and write permissions for an analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_analysis_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_analysis_permissions)
        """

    def update_dashboard(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        Name: str,
        SourceEntity: "DashboardSourceEntityTypeDef",
        Parameters: "ParametersTypeDef" = None,
        VersionDescription: str = None,
        DashboardPublishOptions: "DashboardPublishOptionsTypeDef" = None,
        ThemeArn: str = None
    ) -> UpdateDashboardResponseResponseTypeDef:
        """
        Updates a dashboard in an AWS account.

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
    ) -> UpdateDashboardPermissionsResponseResponseTypeDef:
        """
        Updates read and write permissions on a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_dashboard_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_dashboard_permissions)
        """

    def update_dashboard_published_version(
        self, *, AwsAccountId: str, DashboardId: str, VersionNumber: int
    ) -> UpdateDashboardPublishedVersionResponseResponseTypeDef:
        """
        Updates the published version of a dashboard.

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
    ) -> UpdateDataSetResponseResponseTypeDef:
        """
        Updates a dataset.

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
    ) -> UpdateDataSetPermissionsResponseResponseTypeDef:
        """
        Updates the permissions on a dataset.

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
        Credentials: "DataSourceCredentialsTypeDef" = None,
        VpcConnectionProperties: "VpcConnectionPropertiesTypeDef" = None,
        SslProperties: "SslPropertiesTypeDef" = None
    ) -> UpdateDataSourceResponseResponseTypeDef:
        """
        Updates a data source.

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
    ) -> UpdateDataSourcePermissionsResponseResponseTypeDef:
        """
        Updates the permissions to a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_data_source_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_data_source_permissions)
        """

    def update_folder(
        self, *, AwsAccountId: str, FolderId: str, Name: str
    ) -> UpdateFolderResponseResponseTypeDef:
        """
        Updates the name of a folder.

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
    ) -> UpdateFolderPermissionsResponseResponseTypeDef:
        """
        Updates permissions of a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_folder_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_folder_permissions)
        """

    def update_group(
        self, *, GroupName: str, AwsAccountId: str, Namespace: str, Description: str = None
    ) -> UpdateGroupResponseResponseTypeDef:
        """
        Changes a group description.

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
    ) -> UpdateIAMPolicyAssignmentResponseResponseTypeDef:
        """
        Updates an existing IAM policy assignment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_iam_policy_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_iam_policy_assignment)
        """

    def update_template(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        SourceEntity: "TemplateSourceEntityTypeDef",
        VersionDescription: str = None,
        Name: str = None
    ) -> UpdateTemplateResponseResponseTypeDef:
        """
        Updates a template from an existing Amazon QuickSight analysis or another
        template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_template)
        """

    def update_template_alias(
        self, *, AwsAccountId: str, TemplateId: str, AliasName: str, TemplateVersionNumber: int
    ) -> UpdateTemplateAliasResponseResponseTypeDef:
        """
        Updates the template alias of a template.

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
    ) -> UpdateTemplatePermissionsResponseResponseTypeDef:
        """
        Updates the resource permissions for a template.

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
    ) -> UpdateThemeResponseResponseTypeDef:
        """
        Updates a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_theme)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_theme)
        """

    def update_theme_alias(
        self, *, AwsAccountId: str, ThemeId: str, AliasName: str, ThemeVersionNumber: int
    ) -> UpdateThemeAliasResponseResponseTypeDef:
        """
        Updates an alias of a theme.

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
    ) -> UpdateThemePermissionsResponseResponseTypeDef:
        """
        Updates the resource permissions for a theme.

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
    ) -> UpdateUserResponseResponseTypeDef:
        """
        Updates an Amazon QuickSight user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Client.update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_user)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_analyses"]) -> ListAnalysesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListAnalyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listanalysespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dashboard_versions"]
    ) -> ListDashboardVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListDashboardVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdashboardversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_dashboards"]) -> ListDashboardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListDashboards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdashboardspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_data_sets"]) -> ListDataSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListDataSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdatasetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListDataSources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdatasourcespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ingestions"]) -> ListIngestionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListIngestions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listingestionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_namespaces"]) -> ListNamespacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListNamespaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listnamespacespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_aliases"]
    ) -> ListTemplateAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateAliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplatealiasespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_versions"]
    ) -> ListTemplateVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplateversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_templates"]) -> ListTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_theme_versions"]
    ) -> ListThemeVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListThemeVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listthemeversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_themes"]) -> ListThemesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.ListThemes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listthemespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_analyses"]) -> SearchAnalysesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.SearchAnalyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchanalysespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_dashboards"]
    ) -> SearchDashboardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/quicksight.html#QuickSight.Paginator.SearchDashboards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdashboardspaginator)
        """
