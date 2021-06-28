"""
Type annotations for workspaces service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/type_defs.html)

Usage::

    ```python
    from mypy_boto3_workspaces.type_defs import AccountModificationTypeDef

    data: AccountModificationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccessPropertyValueType,
    ApplicationType,
    AssociationStatusType,
    ComputeType,
    ConnectionAliasStateType,
    ConnectionStateType,
    DedicatedTenancyModificationStateEnumType,
    DedicatedTenancySupportResultEnumType,
    ImageTypeType,
    ModificationResourceEnumType,
    ModificationStateEnumType,
    OperatingSystemTypeType,
    ReconnectEnumType,
    RunningModeType,
    TargetWorkspaceStateType,
    TenancyType,
    WorkspaceDirectoryStateType,
    WorkspaceDirectoryTypeType,
    WorkspaceImageIngestionProcessType,
    WorkspaceImageRequiredTenancyType,
    WorkspaceImageStateType,
    WorkspaceStateType,
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
    "AccountModificationTypeDef",
    "AssociateConnectionAliasRequestTypeDef",
    "AssociateConnectionAliasResultResponseTypeDef",
    "AssociateIpGroupsRequestTypeDef",
    "AuthorizeIpRulesRequestTypeDef",
    "ClientPropertiesResultTypeDef",
    "ClientPropertiesTypeDef",
    "ComputeTypeTypeDef",
    "ConnectionAliasAssociationTypeDef",
    "ConnectionAliasPermissionTypeDef",
    "ConnectionAliasTypeDef",
    "CopyWorkspaceImageRequestTypeDef",
    "CopyWorkspaceImageResultResponseTypeDef",
    "CreateConnectionAliasRequestTypeDef",
    "CreateConnectionAliasResultResponseTypeDef",
    "CreateIpGroupRequestTypeDef",
    "CreateIpGroupResultResponseTypeDef",
    "CreateTagsRequestTypeDef",
    "CreateWorkspaceBundleRequestTypeDef",
    "CreateWorkspaceBundleResultResponseTypeDef",
    "CreateWorkspacesRequestTypeDef",
    "CreateWorkspacesResultResponseTypeDef",
    "DefaultWorkspaceCreationPropertiesTypeDef",
    "DeleteConnectionAliasRequestTypeDef",
    "DeleteIpGroupRequestTypeDef",
    "DeleteTagsRequestTypeDef",
    "DeleteWorkspaceBundleRequestTypeDef",
    "DeleteWorkspaceImageRequestTypeDef",
    "DeregisterWorkspaceDirectoryRequestTypeDef",
    "DescribeAccountModificationsRequestTypeDef",
    "DescribeAccountModificationsResultResponseTypeDef",
    "DescribeAccountResultResponseTypeDef",
    "DescribeClientPropertiesRequestTypeDef",
    "DescribeClientPropertiesResultResponseTypeDef",
    "DescribeConnectionAliasPermissionsRequestTypeDef",
    "DescribeConnectionAliasPermissionsResultResponseTypeDef",
    "DescribeConnectionAliasesRequestTypeDef",
    "DescribeConnectionAliasesResultResponseTypeDef",
    "DescribeIpGroupsRequestTypeDef",
    "DescribeIpGroupsResultResponseTypeDef",
    "DescribeTagsRequestTypeDef",
    "DescribeTagsResultResponseTypeDef",
    "DescribeWorkspaceBundlesRequestTypeDef",
    "DescribeWorkspaceBundlesResultResponseTypeDef",
    "DescribeWorkspaceDirectoriesRequestTypeDef",
    "DescribeWorkspaceDirectoriesResultResponseTypeDef",
    "DescribeWorkspaceImagePermissionsRequestTypeDef",
    "DescribeWorkspaceImagePermissionsResultResponseTypeDef",
    "DescribeWorkspaceImagesRequestTypeDef",
    "DescribeWorkspaceImagesResultResponseTypeDef",
    "DescribeWorkspaceSnapshotsRequestTypeDef",
    "DescribeWorkspaceSnapshotsResultResponseTypeDef",
    "DescribeWorkspacesConnectionStatusRequestTypeDef",
    "DescribeWorkspacesConnectionStatusResultResponseTypeDef",
    "DescribeWorkspacesRequestTypeDef",
    "DescribeWorkspacesResultResponseTypeDef",
    "DisassociateConnectionAliasRequestTypeDef",
    "DisassociateIpGroupsRequestTypeDef",
    "FailedCreateWorkspaceRequestTypeDef",
    "FailedWorkspaceChangeRequestTypeDef",
    "ImagePermissionTypeDef",
    "ImportWorkspaceImageRequestTypeDef",
    "ImportWorkspaceImageResultResponseTypeDef",
    "IpRuleItemTypeDef",
    "ListAvailableManagementCidrRangesRequestTypeDef",
    "ListAvailableManagementCidrRangesResultResponseTypeDef",
    "MigrateWorkspaceRequestTypeDef",
    "MigrateWorkspaceResultResponseTypeDef",
    "ModificationStateTypeDef",
    "ModifyAccountRequestTypeDef",
    "ModifyClientPropertiesRequestTypeDef",
    "ModifySelfservicePermissionsRequestTypeDef",
    "ModifyWorkspaceAccessPropertiesRequestTypeDef",
    "ModifyWorkspaceCreationPropertiesRequestTypeDef",
    "ModifyWorkspacePropertiesRequestTypeDef",
    "ModifyWorkspaceStateRequestTypeDef",
    "OperatingSystemTypeDef",
    "PaginatorConfigTypeDef",
    "RebootRequestTypeDef",
    "RebootWorkspacesRequestTypeDef",
    "RebootWorkspacesResultResponseTypeDef",
    "RebuildRequestTypeDef",
    "RebuildWorkspacesRequestTypeDef",
    "RebuildWorkspacesResultResponseTypeDef",
    "RegisterWorkspaceDirectoryRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreWorkspaceRequestTypeDef",
    "RevokeIpRulesRequestTypeDef",
    "RootStorageTypeDef",
    "SelfservicePermissionsTypeDef",
    "SnapshotTypeDef",
    "StartRequestTypeDef",
    "StartWorkspacesRequestTypeDef",
    "StartWorkspacesResultResponseTypeDef",
    "StopRequestTypeDef",
    "StopWorkspacesRequestTypeDef",
    "StopWorkspacesResultResponseTypeDef",
    "TagTypeDef",
    "TerminateRequestTypeDef",
    "TerminateWorkspacesRequestTypeDef",
    "TerminateWorkspacesResultResponseTypeDef",
    "UpdateConnectionAliasPermissionRequestTypeDef",
    "UpdateRulesOfIpGroupRequestTypeDef",
    "UpdateWorkspaceBundleRequestTypeDef",
    "UpdateWorkspaceImagePermissionRequestTypeDef",
    "UserStorageTypeDef",
    "WorkspaceAccessPropertiesTypeDef",
    "WorkspaceBundleTypeDef",
    "WorkspaceConnectionStatusTypeDef",
    "WorkspaceCreationPropertiesTypeDef",
    "WorkspaceDirectoryTypeDef",
    "WorkspaceImageTypeDef",
    "WorkspacePropertiesTypeDef",
    "WorkspaceRequestTypeDef",
    "WorkspaceTypeDef",
    "WorkspacesIpGroupTypeDef",
)

AccountModificationTypeDef = TypedDict(
    "AccountModificationTypeDef",
    {
        "ModificationState": DedicatedTenancyModificationStateEnumType,
        "DedicatedTenancySupport": DedicatedTenancySupportResultEnumType,
        "DedicatedTenancyManagementCidrRange": str,
        "StartTime": datetime,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

AssociateConnectionAliasRequestTypeDef = TypedDict(
    "AssociateConnectionAliasRequestTypeDef",
    {
        "AliasId": str,
        "ResourceId": str,
    },
)

AssociateConnectionAliasResultResponseTypeDef = TypedDict(
    "AssociateConnectionAliasResultResponseTypeDef",
    {
        "ConnectionIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateIpGroupsRequestTypeDef = TypedDict(
    "AssociateIpGroupsRequestTypeDef",
    {
        "DirectoryId": str,
        "GroupIds": List[str],
    },
)

AuthorizeIpRulesRequestTypeDef = TypedDict(
    "AuthorizeIpRulesRequestTypeDef",
    {
        "GroupId": str,
        "UserRules": List["IpRuleItemTypeDef"],
    },
)

ClientPropertiesResultTypeDef = TypedDict(
    "ClientPropertiesResultTypeDef",
    {
        "ResourceId": str,
        "ClientProperties": "ClientPropertiesTypeDef",
    },
    total=False,
)

ClientPropertiesTypeDef = TypedDict(
    "ClientPropertiesTypeDef",
    {
        "ReconnectEnabled": ReconnectEnumType,
    },
    total=False,
)

ComputeTypeTypeDef = TypedDict(
    "ComputeTypeTypeDef",
    {
        "Name": ComputeType,
    },
    total=False,
)

ConnectionAliasAssociationTypeDef = TypedDict(
    "ConnectionAliasAssociationTypeDef",
    {
        "AssociationStatus": AssociationStatusType,
        "AssociatedAccountId": str,
        "ResourceId": str,
        "ConnectionIdentifier": str,
    },
    total=False,
)

ConnectionAliasPermissionTypeDef = TypedDict(
    "ConnectionAliasPermissionTypeDef",
    {
        "SharedAccountId": str,
        "AllowAssociation": bool,
    },
)

ConnectionAliasTypeDef = TypedDict(
    "ConnectionAliasTypeDef",
    {
        "ConnectionString": str,
        "AliasId": str,
        "State": ConnectionAliasStateType,
        "OwnerAccountId": str,
        "Associations": List["ConnectionAliasAssociationTypeDef"],
    },
    total=False,
)

_RequiredCopyWorkspaceImageRequestTypeDef = TypedDict(
    "_RequiredCopyWorkspaceImageRequestTypeDef",
    {
        "Name": str,
        "SourceImageId": str,
        "SourceRegion": str,
    },
)
_OptionalCopyWorkspaceImageRequestTypeDef = TypedDict(
    "_OptionalCopyWorkspaceImageRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CopyWorkspaceImageRequestTypeDef(
    _RequiredCopyWorkspaceImageRequestTypeDef, _OptionalCopyWorkspaceImageRequestTypeDef
):
    pass


CopyWorkspaceImageResultResponseTypeDef = TypedDict(
    "CopyWorkspaceImageResultResponseTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConnectionAliasRequestTypeDef = TypedDict(
    "_RequiredCreateConnectionAliasRequestTypeDef",
    {
        "ConnectionString": str,
    },
)
_OptionalCreateConnectionAliasRequestTypeDef = TypedDict(
    "_OptionalCreateConnectionAliasRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateConnectionAliasRequestTypeDef(
    _RequiredCreateConnectionAliasRequestTypeDef, _OptionalCreateConnectionAliasRequestTypeDef
):
    pass


CreateConnectionAliasResultResponseTypeDef = TypedDict(
    "CreateConnectionAliasResultResponseTypeDef",
    {
        "AliasId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIpGroupRequestTypeDef = TypedDict(
    "_RequiredCreateIpGroupRequestTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalCreateIpGroupRequestTypeDef = TypedDict(
    "_OptionalCreateIpGroupRequestTypeDef",
    {
        "GroupDesc": str,
        "UserRules": List["IpRuleItemTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateIpGroupRequestTypeDef(
    _RequiredCreateIpGroupRequestTypeDef, _OptionalCreateIpGroupRequestTypeDef
):
    pass


CreateIpGroupResultResponseTypeDef = TypedDict(
    "CreateIpGroupResultResponseTypeDef",
    {
        "GroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTagsRequestTypeDef = TypedDict(
    "CreateTagsRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": List["TagTypeDef"],
    },
)

_RequiredCreateWorkspaceBundleRequestTypeDef = TypedDict(
    "_RequiredCreateWorkspaceBundleRequestTypeDef",
    {
        "BundleName": str,
        "BundleDescription": str,
        "ImageId": str,
        "ComputeType": "ComputeTypeTypeDef",
        "UserStorage": "UserStorageTypeDef",
    },
)
_OptionalCreateWorkspaceBundleRequestTypeDef = TypedDict(
    "_OptionalCreateWorkspaceBundleRequestTypeDef",
    {
        "RootStorage": "RootStorageTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateWorkspaceBundleRequestTypeDef(
    _RequiredCreateWorkspaceBundleRequestTypeDef, _OptionalCreateWorkspaceBundleRequestTypeDef
):
    pass


CreateWorkspaceBundleResultResponseTypeDef = TypedDict(
    "CreateWorkspaceBundleResultResponseTypeDef",
    {
        "WorkspaceBundle": "WorkspaceBundleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkspacesRequestTypeDef = TypedDict(
    "CreateWorkspacesRequestTypeDef",
    {
        "Workspaces": List["WorkspaceRequestTypeDef"],
    },
)

CreateWorkspacesResultResponseTypeDef = TypedDict(
    "CreateWorkspacesResultResponseTypeDef",
    {
        "FailedRequests": List["FailedCreateWorkspaceRequestTypeDef"],
        "PendingRequests": List["WorkspaceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefaultWorkspaceCreationPropertiesTypeDef = TypedDict(
    "DefaultWorkspaceCreationPropertiesTypeDef",
    {
        "EnableWorkDocs": bool,
        "EnableInternetAccess": bool,
        "DefaultOu": str,
        "CustomSecurityGroupId": str,
        "UserEnabledAsLocalAdministrator": bool,
        "EnableMaintenanceMode": bool,
    },
    total=False,
)

DeleteConnectionAliasRequestTypeDef = TypedDict(
    "DeleteConnectionAliasRequestTypeDef",
    {
        "AliasId": str,
    },
)

DeleteIpGroupRequestTypeDef = TypedDict(
    "DeleteIpGroupRequestTypeDef",
    {
        "GroupId": str,
    },
)

DeleteTagsRequestTypeDef = TypedDict(
    "DeleteTagsRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeys": List[str],
    },
)

DeleteWorkspaceBundleRequestTypeDef = TypedDict(
    "DeleteWorkspaceBundleRequestTypeDef",
    {
        "BundleId": str,
    },
    total=False,
)

DeleteWorkspaceImageRequestTypeDef = TypedDict(
    "DeleteWorkspaceImageRequestTypeDef",
    {
        "ImageId": str,
    },
)

DeregisterWorkspaceDirectoryRequestTypeDef = TypedDict(
    "DeregisterWorkspaceDirectoryRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

DescribeAccountModificationsRequestTypeDef = TypedDict(
    "DescribeAccountModificationsRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

DescribeAccountModificationsResultResponseTypeDef = TypedDict(
    "DescribeAccountModificationsResultResponseTypeDef",
    {
        "AccountModifications": List["AccountModificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountResultResponseTypeDef = TypedDict(
    "DescribeAccountResultResponseTypeDef",
    {
        "DedicatedTenancySupport": DedicatedTenancySupportResultEnumType,
        "DedicatedTenancyManagementCidrRange": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClientPropertiesRequestTypeDef = TypedDict(
    "DescribeClientPropertiesRequestTypeDef",
    {
        "ResourceIds": List[str],
    },
)

DescribeClientPropertiesResultResponseTypeDef = TypedDict(
    "DescribeClientPropertiesResultResponseTypeDef",
    {
        "ClientPropertiesList": List["ClientPropertiesResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeConnectionAliasPermissionsRequestTypeDef = TypedDict(
    "_RequiredDescribeConnectionAliasPermissionsRequestTypeDef",
    {
        "AliasId": str,
    },
)
_OptionalDescribeConnectionAliasPermissionsRequestTypeDef = TypedDict(
    "_OptionalDescribeConnectionAliasPermissionsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class DescribeConnectionAliasPermissionsRequestTypeDef(
    _RequiredDescribeConnectionAliasPermissionsRequestTypeDef,
    _OptionalDescribeConnectionAliasPermissionsRequestTypeDef,
):
    pass


DescribeConnectionAliasPermissionsResultResponseTypeDef = TypedDict(
    "DescribeConnectionAliasPermissionsResultResponseTypeDef",
    {
        "AliasId": str,
        "ConnectionAliasPermissions": List["ConnectionAliasPermissionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectionAliasesRequestTypeDef = TypedDict(
    "DescribeConnectionAliasesRequestTypeDef",
    {
        "AliasIds": List[str],
        "ResourceId": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeConnectionAliasesResultResponseTypeDef = TypedDict(
    "DescribeConnectionAliasesResultResponseTypeDef",
    {
        "ConnectionAliases": List["ConnectionAliasTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIpGroupsRequestTypeDef = TypedDict(
    "DescribeIpGroupsRequestTypeDef",
    {
        "GroupIds": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeIpGroupsResultResponseTypeDef = TypedDict(
    "DescribeIpGroupsResultResponseTypeDef",
    {
        "Result": List["WorkspacesIpGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsRequestTypeDef = TypedDict(
    "DescribeTagsRequestTypeDef",
    {
        "ResourceId": str,
    },
)

DescribeTagsResultResponseTypeDef = TypedDict(
    "DescribeTagsResultResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceBundlesRequestTypeDef = TypedDict(
    "DescribeWorkspaceBundlesRequestTypeDef",
    {
        "BundleIds": List[str],
        "Owner": str,
        "NextToken": str,
    },
    total=False,
)

DescribeWorkspaceBundlesResultResponseTypeDef = TypedDict(
    "DescribeWorkspaceBundlesResultResponseTypeDef",
    {
        "Bundles": List["WorkspaceBundleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceDirectoriesRequestTypeDef = TypedDict(
    "DescribeWorkspaceDirectoriesRequestTypeDef",
    {
        "DirectoryIds": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeWorkspaceDirectoriesResultResponseTypeDef = TypedDict(
    "DescribeWorkspaceDirectoriesResultResponseTypeDef",
    {
        "Directories": List["WorkspaceDirectoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeWorkspaceImagePermissionsRequestTypeDef = TypedDict(
    "_RequiredDescribeWorkspaceImagePermissionsRequestTypeDef",
    {
        "ImageId": str,
    },
)
_OptionalDescribeWorkspaceImagePermissionsRequestTypeDef = TypedDict(
    "_OptionalDescribeWorkspaceImagePermissionsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class DescribeWorkspaceImagePermissionsRequestTypeDef(
    _RequiredDescribeWorkspaceImagePermissionsRequestTypeDef,
    _OptionalDescribeWorkspaceImagePermissionsRequestTypeDef,
):
    pass


DescribeWorkspaceImagePermissionsResultResponseTypeDef = TypedDict(
    "DescribeWorkspaceImagePermissionsResultResponseTypeDef",
    {
        "ImageId": str,
        "ImagePermissions": List["ImagePermissionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceImagesRequestTypeDef = TypedDict(
    "DescribeWorkspaceImagesRequestTypeDef",
    {
        "ImageIds": List[str],
        "ImageType": ImageTypeType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeWorkspaceImagesResultResponseTypeDef = TypedDict(
    "DescribeWorkspaceImagesResultResponseTypeDef",
    {
        "Images": List["WorkspaceImageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceSnapshotsRequestTypeDef = TypedDict(
    "DescribeWorkspaceSnapshotsRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)

DescribeWorkspaceSnapshotsResultResponseTypeDef = TypedDict(
    "DescribeWorkspaceSnapshotsResultResponseTypeDef",
    {
        "RebuildSnapshots": List["SnapshotTypeDef"],
        "RestoreSnapshots": List["SnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspacesConnectionStatusRequestTypeDef = TypedDict(
    "DescribeWorkspacesConnectionStatusRequestTypeDef",
    {
        "WorkspaceIds": List[str],
        "NextToken": str,
    },
    total=False,
)

DescribeWorkspacesConnectionStatusResultResponseTypeDef = TypedDict(
    "DescribeWorkspacesConnectionStatusResultResponseTypeDef",
    {
        "WorkspacesConnectionStatus": List["WorkspaceConnectionStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspacesRequestTypeDef = TypedDict(
    "DescribeWorkspacesRequestTypeDef",
    {
        "WorkspaceIds": List[str],
        "DirectoryId": str,
        "UserName": str,
        "BundleId": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeWorkspacesResultResponseTypeDef = TypedDict(
    "DescribeWorkspacesResultResponseTypeDef",
    {
        "Workspaces": List["WorkspaceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateConnectionAliasRequestTypeDef = TypedDict(
    "DisassociateConnectionAliasRequestTypeDef",
    {
        "AliasId": str,
    },
)

DisassociateIpGroupsRequestTypeDef = TypedDict(
    "DisassociateIpGroupsRequestTypeDef",
    {
        "DirectoryId": str,
        "GroupIds": List[str],
    },
)

FailedCreateWorkspaceRequestTypeDef = TypedDict(
    "FailedCreateWorkspaceRequestTypeDef",
    {
        "WorkspaceRequest": "WorkspaceRequestTypeDef",
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

FailedWorkspaceChangeRequestTypeDef = TypedDict(
    "FailedWorkspaceChangeRequestTypeDef",
    {
        "WorkspaceId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

ImagePermissionTypeDef = TypedDict(
    "ImagePermissionTypeDef",
    {
        "SharedAccountId": str,
    },
    total=False,
)

_RequiredImportWorkspaceImageRequestTypeDef = TypedDict(
    "_RequiredImportWorkspaceImageRequestTypeDef",
    {
        "Ec2ImageId": str,
        "IngestionProcess": WorkspaceImageIngestionProcessType,
        "ImageName": str,
        "ImageDescription": str,
    },
)
_OptionalImportWorkspaceImageRequestTypeDef = TypedDict(
    "_OptionalImportWorkspaceImageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "Applications": List[ApplicationType],
    },
    total=False,
)


class ImportWorkspaceImageRequestTypeDef(
    _RequiredImportWorkspaceImageRequestTypeDef, _OptionalImportWorkspaceImageRequestTypeDef
):
    pass


ImportWorkspaceImageResultResponseTypeDef = TypedDict(
    "ImportWorkspaceImageResultResponseTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IpRuleItemTypeDef = TypedDict(
    "IpRuleItemTypeDef",
    {
        "ipRule": str,
        "ruleDesc": str,
    },
    total=False,
)

_RequiredListAvailableManagementCidrRangesRequestTypeDef = TypedDict(
    "_RequiredListAvailableManagementCidrRangesRequestTypeDef",
    {
        "ManagementCidrRangeConstraint": str,
    },
)
_OptionalListAvailableManagementCidrRangesRequestTypeDef = TypedDict(
    "_OptionalListAvailableManagementCidrRangesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListAvailableManagementCidrRangesRequestTypeDef(
    _RequiredListAvailableManagementCidrRangesRequestTypeDef,
    _OptionalListAvailableManagementCidrRangesRequestTypeDef,
):
    pass


ListAvailableManagementCidrRangesResultResponseTypeDef = TypedDict(
    "ListAvailableManagementCidrRangesResultResponseTypeDef",
    {
        "ManagementCidrRanges": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MigrateWorkspaceRequestTypeDef = TypedDict(
    "MigrateWorkspaceRequestTypeDef",
    {
        "SourceWorkspaceId": str,
        "BundleId": str,
    },
)

MigrateWorkspaceResultResponseTypeDef = TypedDict(
    "MigrateWorkspaceResultResponseTypeDef",
    {
        "SourceWorkspaceId": str,
        "TargetWorkspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModificationStateTypeDef = TypedDict(
    "ModificationStateTypeDef",
    {
        "Resource": ModificationResourceEnumType,
        "State": ModificationStateEnumType,
    },
    total=False,
)

ModifyAccountRequestTypeDef = TypedDict(
    "ModifyAccountRequestTypeDef",
    {
        "DedicatedTenancySupport": Literal["ENABLED"],
        "DedicatedTenancyManagementCidrRange": str,
    },
    total=False,
)

ModifyClientPropertiesRequestTypeDef = TypedDict(
    "ModifyClientPropertiesRequestTypeDef",
    {
        "ResourceId": str,
        "ClientProperties": "ClientPropertiesTypeDef",
    },
)

ModifySelfservicePermissionsRequestTypeDef = TypedDict(
    "ModifySelfservicePermissionsRequestTypeDef",
    {
        "ResourceId": str,
        "SelfservicePermissions": "SelfservicePermissionsTypeDef",
    },
)

ModifyWorkspaceAccessPropertiesRequestTypeDef = TypedDict(
    "ModifyWorkspaceAccessPropertiesRequestTypeDef",
    {
        "ResourceId": str,
        "WorkspaceAccessProperties": "WorkspaceAccessPropertiesTypeDef",
    },
)

ModifyWorkspaceCreationPropertiesRequestTypeDef = TypedDict(
    "ModifyWorkspaceCreationPropertiesRequestTypeDef",
    {
        "ResourceId": str,
        "WorkspaceCreationProperties": "WorkspaceCreationPropertiesTypeDef",
    },
)

ModifyWorkspacePropertiesRequestTypeDef = TypedDict(
    "ModifyWorkspacePropertiesRequestTypeDef",
    {
        "WorkspaceId": str,
        "WorkspaceProperties": "WorkspacePropertiesTypeDef",
    },
)

ModifyWorkspaceStateRequestTypeDef = TypedDict(
    "ModifyWorkspaceStateRequestTypeDef",
    {
        "WorkspaceId": str,
        "WorkspaceState": TargetWorkspaceStateType,
    },
)

OperatingSystemTypeDef = TypedDict(
    "OperatingSystemTypeDef",
    {
        "Type": OperatingSystemTypeType,
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

RebootRequestTypeDef = TypedDict(
    "RebootRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)

RebootWorkspacesRequestTypeDef = TypedDict(
    "RebootWorkspacesRequestTypeDef",
    {
        "RebootWorkspaceRequests": List["RebootRequestTypeDef"],
    },
)

RebootWorkspacesResultResponseTypeDef = TypedDict(
    "RebootWorkspacesResultResponseTypeDef",
    {
        "FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RebuildRequestTypeDef = TypedDict(
    "RebuildRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)

RebuildWorkspacesRequestTypeDef = TypedDict(
    "RebuildWorkspacesRequestTypeDef",
    {
        "RebuildWorkspaceRequests": List["RebuildRequestTypeDef"],
    },
)

RebuildWorkspacesResultResponseTypeDef = TypedDict(
    "RebuildWorkspacesResultResponseTypeDef",
    {
        "FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterWorkspaceDirectoryRequestTypeDef = TypedDict(
    "_RequiredRegisterWorkspaceDirectoryRequestTypeDef",
    {
        "DirectoryId": str,
        "EnableWorkDocs": bool,
    },
)
_OptionalRegisterWorkspaceDirectoryRequestTypeDef = TypedDict(
    "_OptionalRegisterWorkspaceDirectoryRequestTypeDef",
    {
        "SubnetIds": List[str],
        "EnableSelfService": bool,
        "Tenancy": TenancyType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class RegisterWorkspaceDirectoryRequestTypeDef(
    _RequiredRegisterWorkspaceDirectoryRequestTypeDef,
    _OptionalRegisterWorkspaceDirectoryRequestTypeDef,
):
    pass


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

RestoreWorkspaceRequestTypeDef = TypedDict(
    "RestoreWorkspaceRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)

RevokeIpRulesRequestTypeDef = TypedDict(
    "RevokeIpRulesRequestTypeDef",
    {
        "GroupId": str,
        "UserRules": List[str],
    },
)

RootStorageTypeDef = TypedDict(
    "RootStorageTypeDef",
    {
        "Capacity": str,
    },
    total=False,
)

SelfservicePermissionsTypeDef = TypedDict(
    "SelfservicePermissionsTypeDef",
    {
        "RestartWorkspace": ReconnectEnumType,
        "IncreaseVolumeSize": ReconnectEnumType,
        "ChangeComputeType": ReconnectEnumType,
        "SwitchRunningMode": ReconnectEnumType,
        "RebuildWorkspace": ReconnectEnumType,
    },
    total=False,
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "SnapshotTime": datetime,
    },
    total=False,
)

StartRequestTypeDef = TypedDict(
    "StartRequestTypeDef",
    {
        "WorkspaceId": str,
    },
    total=False,
)

StartWorkspacesRequestTypeDef = TypedDict(
    "StartWorkspacesRequestTypeDef",
    {
        "StartWorkspaceRequests": List["StartRequestTypeDef"],
    },
)

StartWorkspacesResultResponseTypeDef = TypedDict(
    "StartWorkspacesResultResponseTypeDef",
    {
        "FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopRequestTypeDef = TypedDict(
    "StopRequestTypeDef",
    {
        "WorkspaceId": str,
    },
    total=False,
)

StopWorkspacesRequestTypeDef = TypedDict(
    "StopWorkspacesRequestTypeDef",
    {
        "StopWorkspaceRequests": List["StopRequestTypeDef"],
    },
)

StopWorkspacesResultResponseTypeDef = TypedDict(
    "StopWorkspacesResultResponseTypeDef",
    {
        "FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


TerminateRequestTypeDef = TypedDict(
    "TerminateRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)

TerminateWorkspacesRequestTypeDef = TypedDict(
    "TerminateWorkspacesRequestTypeDef",
    {
        "TerminateWorkspaceRequests": List["TerminateRequestTypeDef"],
    },
)

TerminateWorkspacesResultResponseTypeDef = TypedDict(
    "TerminateWorkspacesResultResponseTypeDef",
    {
        "FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConnectionAliasPermissionRequestTypeDef = TypedDict(
    "UpdateConnectionAliasPermissionRequestTypeDef",
    {
        "AliasId": str,
        "ConnectionAliasPermission": "ConnectionAliasPermissionTypeDef",
    },
)

UpdateRulesOfIpGroupRequestTypeDef = TypedDict(
    "UpdateRulesOfIpGroupRequestTypeDef",
    {
        "GroupId": str,
        "UserRules": List["IpRuleItemTypeDef"],
    },
)

UpdateWorkspaceBundleRequestTypeDef = TypedDict(
    "UpdateWorkspaceBundleRequestTypeDef",
    {
        "BundleId": str,
        "ImageId": str,
    },
    total=False,
)

UpdateWorkspaceImagePermissionRequestTypeDef = TypedDict(
    "UpdateWorkspaceImagePermissionRequestTypeDef",
    {
        "ImageId": str,
        "AllowCopyImage": bool,
        "SharedAccountId": str,
    },
)

UserStorageTypeDef = TypedDict(
    "UserStorageTypeDef",
    {
        "Capacity": str,
    },
    total=False,
)

WorkspaceAccessPropertiesTypeDef = TypedDict(
    "WorkspaceAccessPropertiesTypeDef",
    {
        "DeviceTypeWindows": AccessPropertyValueType,
        "DeviceTypeOsx": AccessPropertyValueType,
        "DeviceTypeWeb": AccessPropertyValueType,
        "DeviceTypeIos": AccessPropertyValueType,
        "DeviceTypeAndroid": AccessPropertyValueType,
        "DeviceTypeChromeOs": AccessPropertyValueType,
        "DeviceTypeZeroClient": AccessPropertyValueType,
        "DeviceTypeLinux": AccessPropertyValueType,
    },
    total=False,
)

WorkspaceBundleTypeDef = TypedDict(
    "WorkspaceBundleTypeDef",
    {
        "BundleId": str,
        "Name": str,
        "Owner": str,
        "Description": str,
        "ImageId": str,
        "RootStorage": "RootStorageTypeDef",
        "UserStorage": "UserStorageTypeDef",
        "ComputeType": "ComputeTypeTypeDef",
        "LastUpdatedTime": datetime,
        "CreationTime": datetime,
    },
    total=False,
)

WorkspaceConnectionStatusTypeDef = TypedDict(
    "WorkspaceConnectionStatusTypeDef",
    {
        "WorkspaceId": str,
        "ConnectionState": ConnectionStateType,
        "ConnectionStateCheckTimestamp": datetime,
        "LastKnownUserConnectionTimestamp": datetime,
    },
    total=False,
)

WorkspaceCreationPropertiesTypeDef = TypedDict(
    "WorkspaceCreationPropertiesTypeDef",
    {
        "EnableWorkDocs": bool,
        "EnableInternetAccess": bool,
        "DefaultOu": str,
        "CustomSecurityGroupId": str,
        "UserEnabledAsLocalAdministrator": bool,
        "EnableMaintenanceMode": bool,
    },
    total=False,
)

WorkspaceDirectoryTypeDef = TypedDict(
    "WorkspaceDirectoryTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
        "DirectoryName": str,
        "RegistrationCode": str,
        "SubnetIds": List[str],
        "DnsIpAddresses": List[str],
        "CustomerUserName": str,
        "IamRoleId": str,
        "DirectoryType": WorkspaceDirectoryTypeType,
        "WorkspaceSecurityGroupId": str,
        "State": WorkspaceDirectoryStateType,
        "WorkspaceCreationProperties": "DefaultWorkspaceCreationPropertiesTypeDef",
        "ipGroupIds": List[str],
        "WorkspaceAccessProperties": "WorkspaceAccessPropertiesTypeDef",
        "Tenancy": TenancyType,
        "SelfservicePermissions": "SelfservicePermissionsTypeDef",
    },
    total=False,
)

WorkspaceImageTypeDef = TypedDict(
    "WorkspaceImageTypeDef",
    {
        "ImageId": str,
        "Name": str,
        "Description": str,
        "OperatingSystem": "OperatingSystemTypeDef",
        "State": WorkspaceImageStateType,
        "RequiredTenancy": WorkspaceImageRequiredTenancyType,
        "ErrorCode": str,
        "ErrorMessage": str,
        "Created": datetime,
        "OwnerAccountId": str,
    },
    total=False,
)

WorkspacePropertiesTypeDef = TypedDict(
    "WorkspacePropertiesTypeDef",
    {
        "RunningMode": RunningModeType,
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": ComputeType,
    },
    total=False,
)

_RequiredWorkspaceRequestTypeDef = TypedDict(
    "_RequiredWorkspaceRequestTypeDef",
    {
        "DirectoryId": str,
        "UserName": str,
        "BundleId": str,
    },
)
_OptionalWorkspaceRequestTypeDef = TypedDict(
    "_OptionalWorkspaceRequestTypeDef",
    {
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": "WorkspacePropertiesTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class WorkspaceRequestTypeDef(_RequiredWorkspaceRequestTypeDef, _OptionalWorkspaceRequestTypeDef):
    pass


WorkspaceTypeDef = TypedDict(
    "WorkspaceTypeDef",
    {
        "WorkspaceId": str,
        "DirectoryId": str,
        "UserName": str,
        "IpAddress": str,
        "State": WorkspaceStateType,
        "BundleId": str,
        "SubnetId": str,
        "ErrorMessage": str,
        "ErrorCode": str,
        "ComputerName": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": "WorkspacePropertiesTypeDef",
        "ModificationStates": List["ModificationStateTypeDef"],
    },
    total=False,
)

WorkspacesIpGroupTypeDef = TypedDict(
    "WorkspacesIpGroupTypeDef",
    {
        "groupId": str,
        "groupName": str,
        "groupDesc": str,
        "userRules": List["IpRuleItemTypeDef"],
    },
    total=False,
)
