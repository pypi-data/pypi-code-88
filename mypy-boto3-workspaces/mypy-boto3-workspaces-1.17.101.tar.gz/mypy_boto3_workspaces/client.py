"""
Type annotations for workspaces service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_workspaces import WorkSpacesClient

    client: WorkSpacesClient = boto3.client("workspaces")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    ApplicationType,
    ImageTypeType,
    TargetWorkspaceStateType,
    TenancyType,
    WorkspaceImageIngestionProcessType,
)
from .paginator import (
    DescribeAccountModificationsPaginator,
    DescribeIpGroupsPaginator,
    DescribeWorkspaceBundlesPaginator,
    DescribeWorkspaceDirectoriesPaginator,
    DescribeWorkspaceImagesPaginator,
    DescribeWorkspacesConnectionStatusPaginator,
    DescribeWorkspacesPaginator,
    ListAvailableManagementCidrRangesPaginator,
)
from .type_defs import (
    AssociateConnectionAliasResultTypeDef,
    ClientPropertiesTypeDef,
    ComputeTypeTypeDef,
    ConnectionAliasPermissionTypeDef,
    CopyWorkspaceImageResultTypeDef,
    CreateConnectionAliasResultTypeDef,
    CreateIpGroupResultTypeDef,
    CreateWorkspaceBundleResultTypeDef,
    CreateWorkspacesResultTypeDef,
    DescribeAccountModificationsResultTypeDef,
    DescribeAccountResultTypeDef,
    DescribeClientPropertiesResultTypeDef,
    DescribeConnectionAliasesResultTypeDef,
    DescribeConnectionAliasPermissionsResultTypeDef,
    DescribeIpGroupsResultTypeDef,
    DescribeTagsResultTypeDef,
    DescribeWorkspaceBundlesResultTypeDef,
    DescribeWorkspaceDirectoriesResultTypeDef,
    DescribeWorkspaceImagePermissionsResultTypeDef,
    DescribeWorkspaceImagesResultTypeDef,
    DescribeWorkspacesConnectionStatusResultTypeDef,
    DescribeWorkspaceSnapshotsResultTypeDef,
    DescribeWorkspacesResultTypeDef,
    ImportWorkspaceImageResultTypeDef,
    IpRuleItemTypeDef,
    ListAvailableManagementCidrRangesResultTypeDef,
    MigrateWorkspaceResultTypeDef,
    RebootRequestTypeDef,
    RebootWorkspacesResultTypeDef,
    RebuildRequestTypeDef,
    RebuildWorkspacesResultTypeDef,
    RootStorageTypeDef,
    SelfservicePermissionsTypeDef,
    StartRequestTypeDef,
    StartWorkspacesResultTypeDef,
    StopRequestTypeDef,
    StopWorkspacesResultTypeDef,
    TagTypeDef,
    TerminateRequestTypeDef,
    TerminateWorkspacesResultTypeDef,
    UserStorageTypeDef,
    WorkspaceAccessPropertiesTypeDef,
    WorkspaceCreationPropertiesTypeDef,
    WorkspacePropertiesTypeDef,
    WorkspaceRequestTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WorkSpacesClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InvalidParameterValuesException: Type[BotocoreClientError]
    InvalidResourceStateException: Type[BotocoreClientError]
    OperationInProgressException: Type[BotocoreClientError]
    OperationNotSupportedException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceAssociatedException: Type[BotocoreClientError]
    ResourceCreationFailedException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    UnsupportedNetworkConfigurationException: Type[BotocoreClientError]
    UnsupportedWorkspaceConfigurationException: Type[BotocoreClientError]
    WorkspacesDefaultRoleNotFoundException: Type[BotocoreClientError]


class WorkSpacesClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_connection_alias(
        self, *, AliasId: str, ResourceId: str
    ) -> AssociateConnectionAliasResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.associate_connection_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#associate_connection_alias)
        """

    def associate_ip_groups(self, *, DirectoryId: str, GroupIds: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.associate_ip_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#associate_ip_groups)
        """

    def authorize_ip_rules(
        self, *, GroupId: str, UserRules: List["IpRuleItemTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.authorize_ip_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#authorize_ip_rules)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#can_paginate)
        """

    def copy_workspace_image(
        self,
        *,
        Name: str,
        SourceImageId: str,
        SourceRegion: str,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CopyWorkspaceImageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.copy_workspace_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#copy_workspace_image)
        """

    def create_connection_alias(
        self, *, ConnectionString: str, Tags: List["TagTypeDef"] = None
    ) -> CreateConnectionAliasResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.create_connection_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#create_connection_alias)
        """

    def create_ip_group(
        self,
        *,
        GroupName: str,
        GroupDesc: str = None,
        UserRules: List["IpRuleItemTypeDef"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateIpGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.create_ip_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#create_ip_group)
        """

    def create_tags(self, *, ResourceId: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#create_tags)
        """

    def create_workspace_bundle(
        self,
        *,
        BundleName: str,
        BundleDescription: str,
        ImageId: str,
        ComputeType: "ComputeTypeTypeDef",
        UserStorage: "UserStorageTypeDef",
        RootStorage: "RootStorageTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateWorkspaceBundleResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.create_workspace_bundle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#create_workspace_bundle)
        """

    def create_workspaces(
        self, *, Workspaces: List["WorkspaceRequestTypeDef"]
    ) -> CreateWorkspacesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.create_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#create_workspaces)
        """

    def delete_connection_alias(self, *, AliasId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.delete_connection_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#delete_connection_alias)
        """

    def delete_ip_group(self, *, GroupId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.delete_ip_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#delete_ip_group)
        """

    def delete_tags(self, *, ResourceId: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#delete_tags)
        """

    def delete_workspace_bundle(self, *, BundleId: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.delete_workspace_bundle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#delete_workspace_bundle)
        """

    def delete_workspace_image(self, *, ImageId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.delete_workspace_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#delete_workspace_image)
        """

    def deregister_workspace_directory(self, *, DirectoryId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.deregister_workspace_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#deregister_workspace_directory)
        """

    def describe_account(self) -> DescribeAccountResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.describe_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_account)
        """

    def describe_account_modifications(
        self, *, NextToken: str = None
    ) -> DescribeAccountModificationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.describe_account_modifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_account_modifications)
        """

    def describe_client_properties(
        self, *, ResourceIds: List[str]
    ) -> DescribeClientPropertiesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.describe_client_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_client_properties)
        """

    def describe_connection_alias_permissions(
        self, *, AliasId: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeConnectionAliasPermissionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.describe_connection_alias_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_connection_alias_permissions)
        """

    def describe_connection_aliases(
        self,
        *,
        AliasIds: List[str] = None,
        ResourceId: str = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeConnectionAliasesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.describe_connection_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_connection_aliases)
        """

    def describe_ip_groups(
        self, *, GroupIds: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeIpGroupsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.describe_ip_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_ip_groups)
        """

    def describe_tags(self, *, ResourceId: str) -> DescribeTagsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.describe_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_tags)
        """

    def describe_workspace_bundles(
        self, *, BundleIds: List[str] = None, Owner: str = None, NextToken: str = None
    ) -> DescribeWorkspaceBundlesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_bundles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_workspace_bundles)
        """

    def describe_workspace_directories(
        self, *, DirectoryIds: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeWorkspaceDirectoriesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_directories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_workspace_directories)
        """

    def describe_workspace_image_permissions(
        self, *, ImageId: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeWorkspaceImagePermissionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_image_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_workspace_image_permissions)
        """

    def describe_workspace_images(
        self,
        *,
        ImageIds: List[str] = None,
        ImageType: ImageTypeType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeWorkspaceImagesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_workspace_images)
        """

    def describe_workspace_snapshots(
        self, *, WorkspaceId: str
    ) -> DescribeWorkspaceSnapshotsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_workspace_snapshots)
        """

    def describe_workspaces(
        self,
        *,
        WorkspaceIds: List[str] = None,
        DirectoryId: str = None,
        UserName: str = None,
        BundleId: str = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeWorkspacesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.describe_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_workspaces)
        """

    def describe_workspaces_connection_status(
        self, *, WorkspaceIds: List[str] = None, NextToken: str = None
    ) -> DescribeWorkspacesConnectionStatusResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.describe_workspaces_connection_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#describe_workspaces_connection_status)
        """

    def disassociate_connection_alias(self, *, AliasId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.disassociate_connection_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#disassociate_connection_alias)
        """

    def disassociate_ip_groups(self, *, DirectoryId: str, GroupIds: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.disassociate_ip_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#disassociate_ip_groups)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#generate_presigned_url)
        """

    def import_workspace_image(
        self,
        *,
        Ec2ImageId: str,
        IngestionProcess: WorkspaceImageIngestionProcessType,
        ImageName: str,
        ImageDescription: str,
        Tags: List["TagTypeDef"] = None,
        Applications: List[ApplicationType] = None
    ) -> ImportWorkspaceImageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.import_workspace_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#import_workspace_image)
        """

    def list_available_management_cidr_ranges(
        self, *, ManagementCidrRangeConstraint: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAvailableManagementCidrRangesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.list_available_management_cidr_ranges)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#list_available_management_cidr_ranges)
        """

    def migrate_workspace(
        self, *, SourceWorkspaceId: str, BundleId: str
    ) -> MigrateWorkspaceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.migrate_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#migrate_workspace)
        """

    def modify_account(
        self,
        *,
        DedicatedTenancySupport: Literal["ENABLED"] = None,
        DedicatedTenancyManagementCidrRange: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.modify_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#modify_account)
        """

    def modify_client_properties(
        self, *, ResourceId: str, ClientProperties: "ClientPropertiesTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.modify_client_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#modify_client_properties)
        """

    def modify_selfservice_permissions(
        self, *, ResourceId: str, SelfservicePermissions: "SelfservicePermissionsTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.modify_selfservice_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#modify_selfservice_permissions)
        """

    def modify_workspace_access_properties(
        self, *, ResourceId: str, WorkspaceAccessProperties: "WorkspaceAccessPropertiesTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_access_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#modify_workspace_access_properties)
        """

    def modify_workspace_creation_properties(
        self, *, ResourceId: str, WorkspaceCreationProperties: WorkspaceCreationPropertiesTypeDef
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_creation_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#modify_workspace_creation_properties)
        """

    def modify_workspace_properties(
        self, *, WorkspaceId: str, WorkspaceProperties: "WorkspacePropertiesTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#modify_workspace_properties)
        """

    def modify_workspace_state(
        self, *, WorkspaceId: str, WorkspaceState: TargetWorkspaceStateType
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#modify_workspace_state)
        """

    def reboot_workspaces(
        self, *, RebootWorkspaceRequests: List[RebootRequestTypeDef]
    ) -> RebootWorkspacesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.reboot_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#reboot_workspaces)
        """

    def rebuild_workspaces(
        self, *, RebuildWorkspaceRequests: List[RebuildRequestTypeDef]
    ) -> RebuildWorkspacesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.rebuild_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#rebuild_workspaces)
        """

    def register_workspace_directory(
        self,
        *,
        DirectoryId: str,
        EnableWorkDocs: bool,
        SubnetIds: List[str] = None,
        EnableSelfService: bool = None,
        Tenancy: TenancyType = None,
        Tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.register_workspace_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#register_workspace_directory)
        """

    def restore_workspace(self, *, WorkspaceId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.restore_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#restore_workspace)
        """

    def revoke_ip_rules(self, *, GroupId: str, UserRules: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.revoke_ip_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#revoke_ip_rules)
        """

    def start_workspaces(
        self, *, StartWorkspaceRequests: List[StartRequestTypeDef]
    ) -> StartWorkspacesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.start_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#start_workspaces)
        """

    def stop_workspaces(
        self, *, StopWorkspaceRequests: List[StopRequestTypeDef]
    ) -> StopWorkspacesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.stop_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#stop_workspaces)
        """

    def terminate_workspaces(
        self, *, TerminateWorkspaceRequests: List[TerminateRequestTypeDef]
    ) -> TerminateWorkspacesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.terminate_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#terminate_workspaces)
        """

    def update_connection_alias_permission(
        self, *, AliasId: str, ConnectionAliasPermission: "ConnectionAliasPermissionTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.update_connection_alias_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#update_connection_alias_permission)
        """

    def update_rules_of_ip_group(
        self, *, GroupId: str, UserRules: List["IpRuleItemTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.update_rules_of_ip_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#update_rules_of_ip_group)
        """

    def update_workspace_bundle(
        self, *, BundleId: str = None, ImageId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.update_workspace_bundle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#update_workspace_bundle)
        """

    def update_workspace_image_permission(
        self, *, ImageId: str, AllowCopyImage: bool, SharedAccountId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Client.update_workspace_image_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/client.html#update_workspace_image_permission)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_modifications"]
    ) -> DescribeAccountModificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeAccountModifications)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeaccountmodificationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ip_groups"]
    ) -> DescribeIpGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeIpGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeipgroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspace_bundles"]
    ) -> DescribeWorkspaceBundlesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceBundles)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspacebundlespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspace_directories"]
    ) -> DescribeWorkspaceDirectoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspacedirectoriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspace_images"]
    ) -> DescribeWorkspaceImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceImages)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspaceimagespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspaces"]
    ) -> DescribeWorkspacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaces)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspacespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspaces_connection_status"]
    ) -> DescribeWorkspacesConnectionStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspacesconnectionstatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_available_management_cidr_ranges"]
    ) -> ListAvailableManagementCidrRangesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workspaces.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#listavailablemanagementcidrrangespaginator)
        """
