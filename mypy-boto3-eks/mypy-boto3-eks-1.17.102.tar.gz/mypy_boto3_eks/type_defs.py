"""
Type annotations for eks service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/type_defs.html)

Usage::

    ```python
    from mypy_boto3_eks.type_defs import AddonHealthTypeDef

    data: AddonHealthTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AddonIssueCodeType,
    AddonStatusType,
    AMITypesType,
    CapacityTypesType,
    ClusterStatusType,
    ErrorCodeType,
    FargateProfileStatusType,
    LogTypeType,
    NodegroupIssueCodeType,
    NodegroupStatusType,
    ResolveConflictsType,
    TaintEffectType,
    UpdateParamTypeType,
    UpdateStatusType,
    UpdateTypeType,
    configStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddonHealthTypeDef",
    "AddonInfoTypeDef",
    "AddonIssueTypeDef",
    "AddonTypeDef",
    "AddonVersionInfoTypeDef",
    "AssociateEncryptionConfigRequestTypeDef",
    "AssociateEncryptionConfigResponseResponseTypeDef",
    "AssociateIdentityProviderConfigRequestTypeDef",
    "AssociateIdentityProviderConfigResponseResponseTypeDef",
    "AutoScalingGroupTypeDef",
    "CertificateTypeDef",
    "ClusterTypeDef",
    "CompatibilityTypeDef",
    "CreateAddonRequestTypeDef",
    "CreateAddonResponseResponseTypeDef",
    "CreateClusterRequestTypeDef",
    "CreateClusterResponseResponseTypeDef",
    "CreateFargateProfileRequestTypeDef",
    "CreateFargateProfileResponseResponseTypeDef",
    "CreateNodegroupRequestTypeDef",
    "CreateNodegroupResponseResponseTypeDef",
    "DeleteAddonRequestTypeDef",
    "DeleteAddonResponseResponseTypeDef",
    "DeleteClusterRequestTypeDef",
    "DeleteClusterResponseResponseTypeDef",
    "DeleteFargateProfileRequestTypeDef",
    "DeleteFargateProfileResponseResponseTypeDef",
    "DeleteNodegroupRequestTypeDef",
    "DeleteNodegroupResponseResponseTypeDef",
    "DescribeAddonRequestTypeDef",
    "DescribeAddonResponseResponseTypeDef",
    "DescribeAddonVersionsRequestTypeDef",
    "DescribeAddonVersionsResponseResponseTypeDef",
    "DescribeClusterRequestTypeDef",
    "DescribeClusterResponseResponseTypeDef",
    "DescribeFargateProfileRequestTypeDef",
    "DescribeFargateProfileResponseResponseTypeDef",
    "DescribeIdentityProviderConfigRequestTypeDef",
    "DescribeIdentityProviderConfigResponseResponseTypeDef",
    "DescribeNodegroupRequestTypeDef",
    "DescribeNodegroupResponseResponseTypeDef",
    "DescribeUpdateRequestTypeDef",
    "DescribeUpdateResponseResponseTypeDef",
    "DisassociateIdentityProviderConfigRequestTypeDef",
    "DisassociateIdentityProviderConfigResponseResponseTypeDef",
    "EncryptionConfigTypeDef",
    "ErrorDetailTypeDef",
    "FargateProfileSelectorTypeDef",
    "FargateProfileTypeDef",
    "IdentityProviderConfigResponseTypeDef",
    "IdentityProviderConfigTypeDef",
    "IdentityTypeDef",
    "IssueTypeDef",
    "KubernetesNetworkConfigRequestTypeDef",
    "KubernetesNetworkConfigResponseTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "ListAddonsRequestTypeDef",
    "ListAddonsResponseResponseTypeDef",
    "ListClustersRequestTypeDef",
    "ListClustersResponseResponseTypeDef",
    "ListFargateProfilesRequestTypeDef",
    "ListFargateProfilesResponseResponseTypeDef",
    "ListIdentityProviderConfigsRequestTypeDef",
    "ListIdentityProviderConfigsResponseResponseTypeDef",
    "ListNodegroupsRequestTypeDef",
    "ListNodegroupsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListUpdatesRequestTypeDef",
    "ListUpdatesResponseResponseTypeDef",
    "LogSetupTypeDef",
    "LoggingTypeDef",
    "NodegroupHealthTypeDef",
    "NodegroupResourcesTypeDef",
    "NodegroupScalingConfigTypeDef",
    "NodegroupTypeDef",
    "NodegroupUpdateConfigTypeDef",
    "OIDCTypeDef",
    "OidcIdentityProviderConfigRequestTypeDef",
    "OidcIdentityProviderConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ProviderTypeDef",
    "RemoteAccessConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TaintTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAddonRequestTypeDef",
    "UpdateAddonResponseResponseTypeDef",
    "UpdateClusterConfigRequestTypeDef",
    "UpdateClusterConfigResponseResponseTypeDef",
    "UpdateClusterVersionRequestTypeDef",
    "UpdateClusterVersionResponseResponseTypeDef",
    "UpdateLabelsPayloadTypeDef",
    "UpdateNodegroupConfigRequestTypeDef",
    "UpdateNodegroupConfigResponseResponseTypeDef",
    "UpdateNodegroupVersionRequestTypeDef",
    "UpdateNodegroupVersionResponseResponseTypeDef",
    "UpdateParamTypeDef",
    "UpdateTaintsPayloadTypeDef",
    "UpdateTypeDef",
    "VpcConfigRequestTypeDef",
    "VpcConfigResponseTypeDef",
    "WaiterConfigTypeDef",
)

AddonHealthTypeDef = TypedDict(
    "AddonHealthTypeDef",
    {
        "issues": List["AddonIssueTypeDef"],
    },
    total=False,
)

AddonInfoTypeDef = TypedDict(
    "AddonInfoTypeDef",
    {
        "addonName": str,
        "type": str,
        "addonVersions": List["AddonVersionInfoTypeDef"],
    },
    total=False,
)

AddonIssueTypeDef = TypedDict(
    "AddonIssueTypeDef",
    {
        "code": AddonIssueCodeType,
        "message": str,
        "resourceIds": List[str],
    },
    total=False,
)

AddonTypeDef = TypedDict(
    "AddonTypeDef",
    {
        "addonName": str,
        "clusterName": str,
        "status": AddonStatusType,
        "addonVersion": str,
        "health": "AddonHealthTypeDef",
        "addonArn": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "serviceAccountRoleArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

AddonVersionInfoTypeDef = TypedDict(
    "AddonVersionInfoTypeDef",
    {
        "addonVersion": str,
        "architecture": List[str],
        "compatibilities": List["CompatibilityTypeDef"],
    },
    total=False,
)

_RequiredAssociateEncryptionConfigRequestTypeDef = TypedDict(
    "_RequiredAssociateEncryptionConfigRequestTypeDef",
    {
        "clusterName": str,
        "encryptionConfig": List["EncryptionConfigTypeDef"],
    },
)
_OptionalAssociateEncryptionConfigRequestTypeDef = TypedDict(
    "_OptionalAssociateEncryptionConfigRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)


class AssociateEncryptionConfigRequestTypeDef(
    _RequiredAssociateEncryptionConfigRequestTypeDef,
    _OptionalAssociateEncryptionConfigRequestTypeDef,
):
    pass


AssociateEncryptionConfigResponseResponseTypeDef = TypedDict(
    "AssociateEncryptionConfigResponseResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateIdentityProviderConfigRequestTypeDef = TypedDict(
    "_RequiredAssociateIdentityProviderConfigRequestTypeDef",
    {
        "clusterName": str,
        "oidc": "OidcIdentityProviderConfigRequestTypeDef",
    },
)
_OptionalAssociateIdentityProviderConfigRequestTypeDef = TypedDict(
    "_OptionalAssociateIdentityProviderConfigRequestTypeDef",
    {
        "tags": Dict[str, str],
        "clientRequestToken": str,
    },
    total=False,
)


class AssociateIdentityProviderConfigRequestTypeDef(
    _RequiredAssociateIdentityProviderConfigRequestTypeDef,
    _OptionalAssociateIdentityProviderConfigRequestTypeDef,
):
    pass


AssociateIdentityProviderConfigResponseResponseTypeDef = TypedDict(
    "AssociateIdentityProviderConfigResponseResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutoScalingGroupTypeDef = TypedDict(
    "AutoScalingGroupTypeDef",
    {
        "name": str,
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "data": str,
    },
    total=False,
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "version": str,
        "endpoint": str,
        "roleArn": str,
        "resourcesVpcConfig": "VpcConfigResponseTypeDef",
        "kubernetesNetworkConfig": "KubernetesNetworkConfigResponseTypeDef",
        "logging": "LoggingTypeDef",
        "identity": "IdentityTypeDef",
        "status": ClusterStatusType,
        "certificateAuthority": "CertificateTypeDef",
        "clientRequestToken": str,
        "platformVersion": str,
        "tags": Dict[str, str],
        "encryptionConfig": List["EncryptionConfigTypeDef"],
    },
    total=False,
)

CompatibilityTypeDef = TypedDict(
    "CompatibilityTypeDef",
    {
        "clusterVersion": str,
        "platformVersions": List[str],
        "defaultVersion": bool,
    },
    total=False,
)

_RequiredCreateAddonRequestTypeDef = TypedDict(
    "_RequiredCreateAddonRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
    },
)
_OptionalCreateAddonRequestTypeDef = TypedDict(
    "_OptionalCreateAddonRequestTypeDef",
    {
        "addonVersion": str,
        "serviceAccountRoleArn": str,
        "resolveConflicts": ResolveConflictsType,
        "clientRequestToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateAddonRequestTypeDef(
    _RequiredCreateAddonRequestTypeDef, _OptionalCreateAddonRequestTypeDef
):
    pass


CreateAddonResponseResponseTypeDef = TypedDict(
    "CreateAddonResponseResponseTypeDef",
    {
        "addon": "AddonTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClusterRequestTypeDef = TypedDict(
    "_RequiredCreateClusterRequestTypeDef",
    {
        "name": str,
        "roleArn": str,
        "resourcesVpcConfig": "VpcConfigRequestTypeDef",
    },
)
_OptionalCreateClusterRequestTypeDef = TypedDict(
    "_OptionalCreateClusterRequestTypeDef",
    {
        "version": str,
        "kubernetesNetworkConfig": "KubernetesNetworkConfigRequestTypeDef",
        "logging": "LoggingTypeDef",
        "clientRequestToken": str,
        "tags": Dict[str, str],
        "encryptionConfig": List["EncryptionConfigTypeDef"],
    },
    total=False,
)


class CreateClusterRequestTypeDef(
    _RequiredCreateClusterRequestTypeDef, _OptionalCreateClusterRequestTypeDef
):
    pass


CreateClusterResponseResponseTypeDef = TypedDict(
    "CreateClusterResponseResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFargateProfileRequestTypeDef = TypedDict(
    "_RequiredCreateFargateProfileRequestTypeDef",
    {
        "fargateProfileName": str,
        "clusterName": str,
        "podExecutionRoleArn": str,
    },
)
_OptionalCreateFargateProfileRequestTypeDef = TypedDict(
    "_OptionalCreateFargateProfileRequestTypeDef",
    {
        "subnets": List[str],
        "selectors": List["FargateProfileSelectorTypeDef"],
        "clientRequestToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateFargateProfileRequestTypeDef(
    _RequiredCreateFargateProfileRequestTypeDef, _OptionalCreateFargateProfileRequestTypeDef
):
    pass


CreateFargateProfileResponseResponseTypeDef = TypedDict(
    "CreateFargateProfileResponseResponseTypeDef",
    {
        "fargateProfile": "FargateProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNodegroupRequestTypeDef = TypedDict(
    "_RequiredCreateNodegroupRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
        "subnets": List[str],
        "nodeRole": str,
    },
)
_OptionalCreateNodegroupRequestTypeDef = TypedDict(
    "_OptionalCreateNodegroupRequestTypeDef",
    {
        "scalingConfig": "NodegroupScalingConfigTypeDef",
        "diskSize": int,
        "instanceTypes": List[str],
        "amiType": AMITypesType,
        "remoteAccess": "RemoteAccessConfigTypeDef",
        "labels": Dict[str, str],
        "taints": List["TaintTypeDef"],
        "tags": Dict[str, str],
        "clientRequestToken": str,
        "launchTemplate": "LaunchTemplateSpecificationTypeDef",
        "updateConfig": "NodegroupUpdateConfigTypeDef",
        "capacityType": CapacityTypesType,
        "version": str,
        "releaseVersion": str,
    },
    total=False,
)


class CreateNodegroupRequestTypeDef(
    _RequiredCreateNodegroupRequestTypeDef, _OptionalCreateNodegroupRequestTypeDef
):
    pass


CreateNodegroupResponseResponseTypeDef = TypedDict(
    "CreateNodegroupResponseResponseTypeDef",
    {
        "nodegroup": "NodegroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAddonRequestTypeDef = TypedDict(
    "DeleteAddonRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
    },
)

DeleteAddonResponseResponseTypeDef = TypedDict(
    "DeleteAddonResponseResponseTypeDef",
    {
        "addon": "AddonTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterRequestTypeDef = TypedDict(
    "DeleteClusterRequestTypeDef",
    {
        "name": str,
    },
)

DeleteClusterResponseResponseTypeDef = TypedDict(
    "DeleteClusterResponseResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFargateProfileRequestTypeDef = TypedDict(
    "DeleteFargateProfileRequestTypeDef",
    {
        "clusterName": str,
        "fargateProfileName": str,
    },
)

DeleteFargateProfileResponseResponseTypeDef = TypedDict(
    "DeleteFargateProfileResponseResponseTypeDef",
    {
        "fargateProfile": "FargateProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNodegroupRequestTypeDef = TypedDict(
    "DeleteNodegroupRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
    },
)

DeleteNodegroupResponseResponseTypeDef = TypedDict(
    "DeleteNodegroupResponseResponseTypeDef",
    {
        "nodegroup": "NodegroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddonRequestTypeDef = TypedDict(
    "DescribeAddonRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
    },
)

DescribeAddonResponseResponseTypeDef = TypedDict(
    "DescribeAddonResponseResponseTypeDef",
    {
        "addon": "AddonTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddonVersionsRequestTypeDef = TypedDict(
    "DescribeAddonVersionsRequestTypeDef",
    {
        "kubernetesVersion": str,
        "maxResults": int,
        "nextToken": str,
        "addonName": str,
    },
    total=False,
)

DescribeAddonVersionsResponseResponseTypeDef = TypedDict(
    "DescribeAddonVersionsResponseResponseTypeDef",
    {
        "addons": List["AddonInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClusterRequestTypeDef = TypedDict(
    "DescribeClusterRequestTypeDef",
    {
        "name": str,
    },
)

DescribeClusterResponseResponseTypeDef = TypedDict(
    "DescribeClusterResponseResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFargateProfileRequestTypeDef = TypedDict(
    "DescribeFargateProfileRequestTypeDef",
    {
        "clusterName": str,
        "fargateProfileName": str,
    },
)

DescribeFargateProfileResponseResponseTypeDef = TypedDict(
    "DescribeFargateProfileResponseResponseTypeDef",
    {
        "fargateProfile": "FargateProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdentityProviderConfigRequestTypeDef = TypedDict(
    "DescribeIdentityProviderConfigRequestTypeDef",
    {
        "clusterName": str,
        "identityProviderConfig": "IdentityProviderConfigTypeDef",
    },
)

DescribeIdentityProviderConfigResponseResponseTypeDef = TypedDict(
    "DescribeIdentityProviderConfigResponseResponseTypeDef",
    {
        "identityProviderConfig": "IdentityProviderConfigResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNodegroupRequestTypeDef = TypedDict(
    "DescribeNodegroupRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
    },
)

DescribeNodegroupResponseResponseTypeDef = TypedDict(
    "DescribeNodegroupResponseResponseTypeDef",
    {
        "nodegroup": "NodegroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeUpdateRequestTypeDef = TypedDict(
    "_RequiredDescribeUpdateRequestTypeDef",
    {
        "name": str,
        "updateId": str,
    },
)
_OptionalDescribeUpdateRequestTypeDef = TypedDict(
    "_OptionalDescribeUpdateRequestTypeDef",
    {
        "nodegroupName": str,
        "addonName": str,
    },
    total=False,
)


class DescribeUpdateRequestTypeDef(
    _RequiredDescribeUpdateRequestTypeDef, _OptionalDescribeUpdateRequestTypeDef
):
    pass


DescribeUpdateResponseResponseTypeDef = TypedDict(
    "DescribeUpdateResponseResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateIdentityProviderConfigRequestTypeDef = TypedDict(
    "_RequiredDisassociateIdentityProviderConfigRequestTypeDef",
    {
        "clusterName": str,
        "identityProviderConfig": "IdentityProviderConfigTypeDef",
    },
)
_OptionalDisassociateIdentityProviderConfigRequestTypeDef = TypedDict(
    "_OptionalDisassociateIdentityProviderConfigRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)


class DisassociateIdentityProviderConfigRequestTypeDef(
    _RequiredDisassociateIdentityProviderConfigRequestTypeDef,
    _OptionalDisassociateIdentityProviderConfigRequestTypeDef,
):
    pass


DisassociateIdentityProviderConfigResponseResponseTypeDef = TypedDict(
    "DisassociateIdentityProviderConfigResponseResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "resources": List[str],
        "provider": "ProviderTypeDef",
    },
    total=False,
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "errorCode": ErrorCodeType,
        "errorMessage": str,
        "resourceIds": List[str],
    },
    total=False,
)

FargateProfileSelectorTypeDef = TypedDict(
    "FargateProfileSelectorTypeDef",
    {
        "namespace": str,
        "labels": Dict[str, str],
    },
    total=False,
)

FargateProfileTypeDef = TypedDict(
    "FargateProfileTypeDef",
    {
        "fargateProfileName": str,
        "fargateProfileArn": str,
        "clusterName": str,
        "createdAt": datetime,
        "podExecutionRoleArn": str,
        "subnets": List[str],
        "selectors": List["FargateProfileSelectorTypeDef"],
        "status": FargateProfileStatusType,
        "tags": Dict[str, str],
    },
    total=False,
)

IdentityProviderConfigResponseTypeDef = TypedDict(
    "IdentityProviderConfigResponseTypeDef",
    {
        "oidc": "OidcIdentityProviderConfigTypeDef",
    },
    total=False,
)

IdentityProviderConfigTypeDef = TypedDict(
    "IdentityProviderConfigTypeDef",
    {
        "type": str,
        "name": str,
    },
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "oidc": "OIDCTypeDef",
    },
    total=False,
)

IssueTypeDef = TypedDict(
    "IssueTypeDef",
    {
        "code": NodegroupIssueCodeType,
        "message": str,
        "resourceIds": List[str],
    },
    total=False,
)

KubernetesNetworkConfigRequestTypeDef = TypedDict(
    "KubernetesNetworkConfigRequestTypeDef",
    {
        "serviceIpv4Cidr": str,
    },
    total=False,
)

KubernetesNetworkConfigResponseTypeDef = TypedDict(
    "KubernetesNetworkConfigResponseTypeDef",
    {
        "serviceIpv4Cidr": str,
    },
    total=False,
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "name": str,
        "version": str,
        "id": str,
    },
    total=False,
)

_RequiredListAddonsRequestTypeDef = TypedDict(
    "_RequiredListAddonsRequestTypeDef",
    {
        "clusterName": str,
    },
)
_OptionalListAddonsRequestTypeDef = TypedDict(
    "_OptionalListAddonsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListAddonsRequestTypeDef(
    _RequiredListAddonsRequestTypeDef, _OptionalListAddonsRequestTypeDef
):
    pass


ListAddonsResponseResponseTypeDef = TypedDict(
    "ListAddonsResponseResponseTypeDef",
    {
        "addons": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersRequestTypeDef = TypedDict(
    "ListClustersRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListClustersResponseResponseTypeDef = TypedDict(
    "ListClustersResponseResponseTypeDef",
    {
        "clusters": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFargateProfilesRequestTypeDef = TypedDict(
    "_RequiredListFargateProfilesRequestTypeDef",
    {
        "clusterName": str,
    },
)
_OptionalListFargateProfilesRequestTypeDef = TypedDict(
    "_OptionalListFargateProfilesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListFargateProfilesRequestTypeDef(
    _RequiredListFargateProfilesRequestTypeDef, _OptionalListFargateProfilesRequestTypeDef
):
    pass


ListFargateProfilesResponseResponseTypeDef = TypedDict(
    "ListFargateProfilesResponseResponseTypeDef",
    {
        "fargateProfileNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIdentityProviderConfigsRequestTypeDef = TypedDict(
    "_RequiredListIdentityProviderConfigsRequestTypeDef",
    {
        "clusterName": str,
    },
)
_OptionalListIdentityProviderConfigsRequestTypeDef = TypedDict(
    "_OptionalListIdentityProviderConfigsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListIdentityProviderConfigsRequestTypeDef(
    _RequiredListIdentityProviderConfigsRequestTypeDef,
    _OptionalListIdentityProviderConfigsRequestTypeDef,
):
    pass


ListIdentityProviderConfigsResponseResponseTypeDef = TypedDict(
    "ListIdentityProviderConfigsResponseResponseTypeDef",
    {
        "identityProviderConfigs": List["IdentityProviderConfigTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNodegroupsRequestTypeDef = TypedDict(
    "_RequiredListNodegroupsRequestTypeDef",
    {
        "clusterName": str,
    },
)
_OptionalListNodegroupsRequestTypeDef = TypedDict(
    "_OptionalListNodegroupsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListNodegroupsRequestTypeDef(
    _RequiredListNodegroupsRequestTypeDef, _OptionalListNodegroupsRequestTypeDef
):
    pass


ListNodegroupsResponseResponseTypeDef = TypedDict(
    "ListNodegroupsResponseResponseTypeDef",
    {
        "nodegroups": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUpdatesRequestTypeDef = TypedDict(
    "_RequiredListUpdatesRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalListUpdatesRequestTypeDef = TypedDict(
    "_OptionalListUpdatesRequestTypeDef",
    {
        "nodegroupName": str,
        "addonName": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListUpdatesRequestTypeDef(
    _RequiredListUpdatesRequestTypeDef, _OptionalListUpdatesRequestTypeDef
):
    pass


ListUpdatesResponseResponseTypeDef = TypedDict(
    "ListUpdatesResponseResponseTypeDef",
    {
        "updateIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogSetupTypeDef = TypedDict(
    "LogSetupTypeDef",
    {
        "types": List[LogTypeType],
        "enabled": bool,
    },
    total=False,
)

LoggingTypeDef = TypedDict(
    "LoggingTypeDef",
    {
        "clusterLogging": List["LogSetupTypeDef"],
    },
    total=False,
)

NodegroupHealthTypeDef = TypedDict(
    "NodegroupHealthTypeDef",
    {
        "issues": List["IssueTypeDef"],
    },
    total=False,
)

NodegroupResourcesTypeDef = TypedDict(
    "NodegroupResourcesTypeDef",
    {
        "autoScalingGroups": List["AutoScalingGroupTypeDef"],
        "remoteAccessSecurityGroup": str,
    },
    total=False,
)

NodegroupScalingConfigTypeDef = TypedDict(
    "NodegroupScalingConfigTypeDef",
    {
        "minSize": int,
        "maxSize": int,
        "desiredSize": int,
    },
    total=False,
)

NodegroupTypeDef = TypedDict(
    "NodegroupTypeDef",
    {
        "nodegroupName": str,
        "nodegroupArn": str,
        "clusterName": str,
        "version": str,
        "releaseVersion": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": NodegroupStatusType,
        "capacityType": CapacityTypesType,
        "scalingConfig": "NodegroupScalingConfigTypeDef",
        "instanceTypes": List[str],
        "subnets": List[str],
        "remoteAccess": "RemoteAccessConfigTypeDef",
        "amiType": AMITypesType,
        "nodeRole": str,
        "labels": Dict[str, str],
        "taints": List["TaintTypeDef"],
        "resources": "NodegroupResourcesTypeDef",
        "diskSize": int,
        "health": "NodegroupHealthTypeDef",
        "updateConfig": "NodegroupUpdateConfigTypeDef",
        "launchTemplate": "LaunchTemplateSpecificationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

NodegroupUpdateConfigTypeDef = TypedDict(
    "NodegroupUpdateConfigTypeDef",
    {
        "maxUnavailable": int,
        "maxUnavailablePercentage": int,
    },
    total=False,
)

OIDCTypeDef = TypedDict(
    "OIDCTypeDef",
    {
        "issuer": str,
    },
    total=False,
)

_RequiredOidcIdentityProviderConfigRequestTypeDef = TypedDict(
    "_RequiredOidcIdentityProviderConfigRequestTypeDef",
    {
        "identityProviderConfigName": str,
        "issuerUrl": str,
        "clientId": str,
    },
)
_OptionalOidcIdentityProviderConfigRequestTypeDef = TypedDict(
    "_OptionalOidcIdentityProviderConfigRequestTypeDef",
    {
        "usernameClaim": str,
        "usernamePrefix": str,
        "groupsClaim": str,
        "groupsPrefix": str,
        "requiredClaims": Dict[str, str],
    },
    total=False,
)


class OidcIdentityProviderConfigRequestTypeDef(
    _RequiredOidcIdentityProviderConfigRequestTypeDef,
    _OptionalOidcIdentityProviderConfigRequestTypeDef,
):
    pass


OidcIdentityProviderConfigTypeDef = TypedDict(
    "OidcIdentityProviderConfigTypeDef",
    {
        "identityProviderConfigName": str,
        "identityProviderConfigArn": str,
        "clusterName": str,
        "issuerUrl": str,
        "clientId": str,
        "usernameClaim": str,
        "usernamePrefix": str,
        "groupsClaim": str,
        "groupsPrefix": str,
        "requiredClaims": Dict[str, str],
        "tags": Dict[str, str],
        "status": configStatusType,
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

ProviderTypeDef = TypedDict(
    "ProviderTypeDef",
    {
        "keyArn": str,
    },
    total=False,
)

RemoteAccessConfigTypeDef = TypedDict(
    "RemoteAccessConfigTypeDef",
    {
        "ec2SshKey": str,
        "sourceSecurityGroups": List[str],
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TaintTypeDef = TypedDict(
    "TaintTypeDef",
    {
        "key": str,
        "value": str,
        "effect": TaintEffectType,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateAddonRequestTypeDef = TypedDict(
    "_RequiredUpdateAddonRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
    },
)
_OptionalUpdateAddonRequestTypeDef = TypedDict(
    "_OptionalUpdateAddonRequestTypeDef",
    {
        "addonVersion": str,
        "serviceAccountRoleArn": str,
        "resolveConflicts": ResolveConflictsType,
        "clientRequestToken": str,
    },
    total=False,
)


class UpdateAddonRequestTypeDef(
    _RequiredUpdateAddonRequestTypeDef, _OptionalUpdateAddonRequestTypeDef
):
    pass


UpdateAddonResponseResponseTypeDef = TypedDict(
    "UpdateAddonResponseResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateClusterConfigRequestTypeDef = TypedDict(
    "_RequiredUpdateClusterConfigRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateClusterConfigRequestTypeDef = TypedDict(
    "_OptionalUpdateClusterConfigRequestTypeDef",
    {
        "resourcesVpcConfig": "VpcConfigRequestTypeDef",
        "logging": "LoggingTypeDef",
        "clientRequestToken": str,
    },
    total=False,
)


class UpdateClusterConfigRequestTypeDef(
    _RequiredUpdateClusterConfigRequestTypeDef, _OptionalUpdateClusterConfigRequestTypeDef
):
    pass


UpdateClusterConfigResponseResponseTypeDef = TypedDict(
    "UpdateClusterConfigResponseResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateClusterVersionRequestTypeDef = TypedDict(
    "_RequiredUpdateClusterVersionRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)
_OptionalUpdateClusterVersionRequestTypeDef = TypedDict(
    "_OptionalUpdateClusterVersionRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)


class UpdateClusterVersionRequestTypeDef(
    _RequiredUpdateClusterVersionRequestTypeDef, _OptionalUpdateClusterVersionRequestTypeDef
):
    pass


UpdateClusterVersionResponseResponseTypeDef = TypedDict(
    "UpdateClusterVersionResponseResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateLabelsPayloadTypeDef = TypedDict(
    "UpdateLabelsPayloadTypeDef",
    {
        "addOrUpdateLabels": Dict[str, str],
        "removeLabels": List[str],
    },
    total=False,
)

_RequiredUpdateNodegroupConfigRequestTypeDef = TypedDict(
    "_RequiredUpdateNodegroupConfigRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
    },
)
_OptionalUpdateNodegroupConfigRequestTypeDef = TypedDict(
    "_OptionalUpdateNodegroupConfigRequestTypeDef",
    {
        "labels": "UpdateLabelsPayloadTypeDef",
        "taints": "UpdateTaintsPayloadTypeDef",
        "scalingConfig": "NodegroupScalingConfigTypeDef",
        "updateConfig": "NodegroupUpdateConfigTypeDef",
        "clientRequestToken": str,
    },
    total=False,
)


class UpdateNodegroupConfigRequestTypeDef(
    _RequiredUpdateNodegroupConfigRequestTypeDef, _OptionalUpdateNodegroupConfigRequestTypeDef
):
    pass


UpdateNodegroupConfigResponseResponseTypeDef = TypedDict(
    "UpdateNodegroupConfigResponseResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateNodegroupVersionRequestTypeDef = TypedDict(
    "_RequiredUpdateNodegroupVersionRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
    },
)
_OptionalUpdateNodegroupVersionRequestTypeDef = TypedDict(
    "_OptionalUpdateNodegroupVersionRequestTypeDef",
    {
        "version": str,
        "releaseVersion": str,
        "launchTemplate": "LaunchTemplateSpecificationTypeDef",
        "force": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class UpdateNodegroupVersionRequestTypeDef(
    _RequiredUpdateNodegroupVersionRequestTypeDef, _OptionalUpdateNodegroupVersionRequestTypeDef
):
    pass


UpdateNodegroupVersionResponseResponseTypeDef = TypedDict(
    "UpdateNodegroupVersionResponseResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateParamTypeDef = TypedDict(
    "UpdateParamTypeDef",
    {
        "type": UpdateParamTypeType,
        "value": str,
    },
    total=False,
)

UpdateTaintsPayloadTypeDef = TypedDict(
    "UpdateTaintsPayloadTypeDef",
    {
        "addOrUpdateTaints": List["TaintTypeDef"],
        "removeTaints": List["TaintTypeDef"],
    },
    total=False,
)

UpdateTypeDef = TypedDict(
    "UpdateTypeDef",
    {
        "id": str,
        "status": UpdateStatusType,
        "type": UpdateTypeType,
        "params": List["UpdateParamTypeDef"],
        "createdAt": datetime,
        "errors": List["ErrorDetailTypeDef"],
    },
    total=False,
)

VpcConfigRequestTypeDef = TypedDict(
    "VpcConfigRequestTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
        "publicAccessCidrs": List[str],
    },
    total=False,
)

VpcConfigResponseTypeDef = TypedDict(
    "VpcConfigResponseTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "clusterSecurityGroupId": str,
        "vpcId": str,
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
        "publicAccessCidrs": List[str],
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
