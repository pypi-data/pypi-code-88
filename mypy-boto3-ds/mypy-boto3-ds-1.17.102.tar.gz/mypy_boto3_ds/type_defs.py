"""
Type annotations for ds service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ds.type_defs import AcceptSharedDirectoryRequestTypeDef

    data: AcceptSharedDirectoryRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    CertificateStateType,
    CertificateTypeType,
    DirectoryEditionType,
    DirectorySizeType,
    DirectoryStageType,
    DirectoryTypeType,
    DomainControllerStatusType,
    IpRouteStatusMsgType,
    LDAPSStatusType,
    RadiusAuthenticationProtocolType,
    RadiusStatusType,
    RegionTypeType,
    SchemaExtensionStatusType,
    SelectiveAuthType,
    ShareMethodType,
    ShareStatusType,
    SnapshotStatusType,
    SnapshotTypeType,
    TopicStatusType,
    TrustDirectionType,
    TrustStateType,
    TrustTypeType,
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
    "AcceptSharedDirectoryRequestTypeDef",
    "AcceptSharedDirectoryResultResponseTypeDef",
    "AddIpRoutesRequestTypeDef",
    "AddRegionRequestTypeDef",
    "AddTagsToResourceRequestTypeDef",
    "AttributeTypeDef",
    "CancelSchemaExtensionRequestTypeDef",
    "CertificateInfoTypeDef",
    "CertificateTypeDef",
    "ClientCertAuthSettingsTypeDef",
    "ComputerTypeDef",
    "ConditionalForwarderTypeDef",
    "ConnectDirectoryRequestTypeDef",
    "ConnectDirectoryResultResponseTypeDef",
    "CreateAliasRequestTypeDef",
    "CreateAliasResultResponseTypeDef",
    "CreateComputerRequestTypeDef",
    "CreateComputerResultResponseTypeDef",
    "CreateConditionalForwarderRequestTypeDef",
    "CreateDirectoryRequestTypeDef",
    "CreateDirectoryResultResponseTypeDef",
    "CreateLogSubscriptionRequestTypeDef",
    "CreateMicrosoftADRequestTypeDef",
    "CreateMicrosoftADResultResponseTypeDef",
    "CreateSnapshotRequestTypeDef",
    "CreateSnapshotResultResponseTypeDef",
    "CreateTrustRequestTypeDef",
    "CreateTrustResultResponseTypeDef",
    "DeleteConditionalForwarderRequestTypeDef",
    "DeleteDirectoryRequestTypeDef",
    "DeleteDirectoryResultResponseTypeDef",
    "DeleteLogSubscriptionRequestTypeDef",
    "DeleteSnapshotRequestTypeDef",
    "DeleteSnapshotResultResponseTypeDef",
    "DeleteTrustRequestTypeDef",
    "DeleteTrustResultResponseTypeDef",
    "DeregisterCertificateRequestTypeDef",
    "DeregisterEventTopicRequestTypeDef",
    "DescribeCertificateRequestTypeDef",
    "DescribeCertificateResultResponseTypeDef",
    "DescribeConditionalForwardersRequestTypeDef",
    "DescribeConditionalForwardersResultResponseTypeDef",
    "DescribeDirectoriesRequestTypeDef",
    "DescribeDirectoriesResultResponseTypeDef",
    "DescribeDomainControllersRequestTypeDef",
    "DescribeDomainControllersResultResponseTypeDef",
    "DescribeEventTopicsRequestTypeDef",
    "DescribeEventTopicsResultResponseTypeDef",
    "DescribeLDAPSSettingsRequestTypeDef",
    "DescribeLDAPSSettingsResultResponseTypeDef",
    "DescribeRegionsRequestTypeDef",
    "DescribeRegionsResultResponseTypeDef",
    "DescribeSharedDirectoriesRequestTypeDef",
    "DescribeSharedDirectoriesResultResponseTypeDef",
    "DescribeSnapshotsRequestTypeDef",
    "DescribeSnapshotsResultResponseTypeDef",
    "DescribeTrustsRequestTypeDef",
    "DescribeTrustsResultResponseTypeDef",
    "DirectoryConnectSettingsDescriptionTypeDef",
    "DirectoryConnectSettingsTypeDef",
    "DirectoryDescriptionTypeDef",
    "DirectoryLimitsTypeDef",
    "DirectoryVpcSettingsDescriptionTypeDef",
    "DirectoryVpcSettingsTypeDef",
    "DisableClientAuthenticationRequestTypeDef",
    "DisableLDAPSRequestTypeDef",
    "DisableRadiusRequestTypeDef",
    "DisableSsoRequestTypeDef",
    "DomainControllerTypeDef",
    "EnableClientAuthenticationRequestTypeDef",
    "EnableLDAPSRequestTypeDef",
    "EnableRadiusRequestTypeDef",
    "EnableSsoRequestTypeDef",
    "EventTopicTypeDef",
    "GetDirectoryLimitsResultResponseTypeDef",
    "GetSnapshotLimitsRequestTypeDef",
    "GetSnapshotLimitsResultResponseTypeDef",
    "IpRouteInfoTypeDef",
    "IpRouteTypeDef",
    "LDAPSSettingInfoTypeDef",
    "ListCertificatesRequestTypeDef",
    "ListCertificatesResultResponseTypeDef",
    "ListIpRoutesRequestTypeDef",
    "ListIpRoutesResultResponseTypeDef",
    "ListLogSubscriptionsRequestTypeDef",
    "ListLogSubscriptionsResultResponseTypeDef",
    "ListSchemaExtensionsRequestTypeDef",
    "ListSchemaExtensionsResultResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResultResponseTypeDef",
    "LogSubscriptionTypeDef",
    "OwnerDirectoryDescriptionTypeDef",
    "PaginatorConfigTypeDef",
    "RadiusSettingsTypeDef",
    "RegionDescriptionTypeDef",
    "RegionsInfoTypeDef",
    "RegisterCertificateRequestTypeDef",
    "RegisterCertificateResultResponseTypeDef",
    "RegisterEventTopicRequestTypeDef",
    "RejectSharedDirectoryRequestTypeDef",
    "RejectSharedDirectoryResultResponseTypeDef",
    "RemoveIpRoutesRequestTypeDef",
    "RemoveRegionRequestTypeDef",
    "RemoveTagsFromResourceRequestTypeDef",
    "ResetUserPasswordRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreFromSnapshotRequestTypeDef",
    "SchemaExtensionInfoTypeDef",
    "ShareDirectoryRequestTypeDef",
    "ShareDirectoryResultResponseTypeDef",
    "ShareTargetTypeDef",
    "SharedDirectoryTypeDef",
    "SnapshotLimitsTypeDef",
    "SnapshotTypeDef",
    "StartSchemaExtensionRequestTypeDef",
    "StartSchemaExtensionResultResponseTypeDef",
    "TagTypeDef",
    "TrustTypeDef",
    "UnshareDirectoryRequestTypeDef",
    "UnshareDirectoryResultResponseTypeDef",
    "UnshareTargetTypeDef",
    "UpdateConditionalForwarderRequestTypeDef",
    "UpdateNumberOfDomainControllersRequestTypeDef",
    "UpdateRadiusRequestTypeDef",
    "UpdateTrustRequestTypeDef",
    "UpdateTrustResultResponseTypeDef",
    "VerifyTrustRequestTypeDef",
    "VerifyTrustResultResponseTypeDef",
)

AcceptSharedDirectoryRequestTypeDef = TypedDict(
    "AcceptSharedDirectoryRequestTypeDef",
    {
        "SharedDirectoryId": str,
    },
)

AcceptSharedDirectoryResultResponseTypeDef = TypedDict(
    "AcceptSharedDirectoryResultResponseTypeDef",
    {
        "SharedDirectory": "SharedDirectoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAddIpRoutesRequestTypeDef = TypedDict(
    "_RequiredAddIpRoutesRequestTypeDef",
    {
        "DirectoryId": str,
        "IpRoutes": List["IpRouteTypeDef"],
    },
)
_OptionalAddIpRoutesRequestTypeDef = TypedDict(
    "_OptionalAddIpRoutesRequestTypeDef",
    {
        "UpdateSecurityGroupForDirectoryControllers": bool,
    },
    total=False,
)


class AddIpRoutesRequestTypeDef(
    _RequiredAddIpRoutesRequestTypeDef, _OptionalAddIpRoutesRequestTypeDef
):
    pass


AddRegionRequestTypeDef = TypedDict(
    "AddRegionRequestTypeDef",
    {
        "DirectoryId": str,
        "RegionName": str,
        "VPCSettings": "DirectoryVpcSettingsTypeDef",
    },
)

AddTagsToResourceRequestTypeDef = TypedDict(
    "AddTagsToResourceRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": List["TagTypeDef"],
    },
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

CancelSchemaExtensionRequestTypeDef = TypedDict(
    "CancelSchemaExtensionRequestTypeDef",
    {
        "DirectoryId": str,
        "SchemaExtensionId": str,
    },
)

CertificateInfoTypeDef = TypedDict(
    "CertificateInfoTypeDef",
    {
        "CertificateId": str,
        "CommonName": str,
        "State": CertificateStateType,
        "ExpiryDateTime": datetime,
        "Type": CertificateTypeType,
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateId": str,
        "State": CertificateStateType,
        "StateReason": str,
        "CommonName": str,
        "RegisteredDateTime": datetime,
        "ExpiryDateTime": datetime,
        "Type": CertificateTypeType,
        "ClientCertAuthSettings": "ClientCertAuthSettingsTypeDef",
    },
    total=False,
)

ClientCertAuthSettingsTypeDef = TypedDict(
    "ClientCertAuthSettingsTypeDef",
    {
        "OCSPUrl": str,
    },
    total=False,
)

ComputerTypeDef = TypedDict(
    "ComputerTypeDef",
    {
        "ComputerId": str,
        "ComputerName": str,
        "ComputerAttributes": List["AttributeTypeDef"],
    },
    total=False,
)

ConditionalForwarderTypeDef = TypedDict(
    "ConditionalForwarderTypeDef",
    {
        "RemoteDomainName": str,
        "DnsIpAddrs": List[str],
        "ReplicationScope": Literal["Domain"],
    },
    total=False,
)

_RequiredConnectDirectoryRequestTypeDef = TypedDict(
    "_RequiredConnectDirectoryRequestTypeDef",
    {
        "Name": str,
        "Password": str,
        "Size": DirectorySizeType,
        "ConnectSettings": "DirectoryConnectSettingsTypeDef",
    },
)
_OptionalConnectDirectoryRequestTypeDef = TypedDict(
    "_OptionalConnectDirectoryRequestTypeDef",
    {
        "ShortName": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class ConnectDirectoryRequestTypeDef(
    _RequiredConnectDirectoryRequestTypeDef, _OptionalConnectDirectoryRequestTypeDef
):
    pass


ConnectDirectoryResultResponseTypeDef = TypedDict(
    "ConnectDirectoryResultResponseTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAliasRequestTypeDef = TypedDict(
    "CreateAliasRequestTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
    },
)

CreateAliasResultResponseTypeDef = TypedDict(
    "CreateAliasResultResponseTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateComputerRequestTypeDef = TypedDict(
    "_RequiredCreateComputerRequestTypeDef",
    {
        "DirectoryId": str,
        "ComputerName": str,
        "Password": str,
    },
)
_OptionalCreateComputerRequestTypeDef = TypedDict(
    "_OptionalCreateComputerRequestTypeDef",
    {
        "OrganizationalUnitDistinguishedName": str,
        "ComputerAttributes": List["AttributeTypeDef"],
    },
    total=False,
)


class CreateComputerRequestTypeDef(
    _RequiredCreateComputerRequestTypeDef, _OptionalCreateComputerRequestTypeDef
):
    pass


CreateComputerResultResponseTypeDef = TypedDict(
    "CreateComputerResultResponseTypeDef",
    {
        "Computer": "ComputerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConditionalForwarderRequestTypeDef = TypedDict(
    "CreateConditionalForwarderRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainName": str,
        "DnsIpAddrs": List[str],
    },
)

_RequiredCreateDirectoryRequestTypeDef = TypedDict(
    "_RequiredCreateDirectoryRequestTypeDef",
    {
        "Name": str,
        "Password": str,
        "Size": DirectorySizeType,
    },
)
_OptionalCreateDirectoryRequestTypeDef = TypedDict(
    "_OptionalCreateDirectoryRequestTypeDef",
    {
        "ShortName": str,
        "Description": str,
        "VpcSettings": "DirectoryVpcSettingsTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDirectoryRequestTypeDef(
    _RequiredCreateDirectoryRequestTypeDef, _OptionalCreateDirectoryRequestTypeDef
):
    pass


CreateDirectoryResultResponseTypeDef = TypedDict(
    "CreateDirectoryResultResponseTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLogSubscriptionRequestTypeDef = TypedDict(
    "CreateLogSubscriptionRequestTypeDef",
    {
        "DirectoryId": str,
        "LogGroupName": str,
    },
)

_RequiredCreateMicrosoftADRequestTypeDef = TypedDict(
    "_RequiredCreateMicrosoftADRequestTypeDef",
    {
        "Name": str,
        "Password": str,
        "VpcSettings": "DirectoryVpcSettingsTypeDef",
    },
)
_OptionalCreateMicrosoftADRequestTypeDef = TypedDict(
    "_OptionalCreateMicrosoftADRequestTypeDef",
    {
        "ShortName": str,
        "Description": str,
        "Edition": DirectoryEditionType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateMicrosoftADRequestTypeDef(
    _RequiredCreateMicrosoftADRequestTypeDef, _OptionalCreateMicrosoftADRequestTypeDef
):
    pass


CreateMicrosoftADResultResponseTypeDef = TypedDict(
    "CreateMicrosoftADResultResponseTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSnapshotRequestTypeDef = TypedDict(
    "_RequiredCreateSnapshotRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalCreateSnapshotRequestTypeDef = TypedDict(
    "_OptionalCreateSnapshotRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class CreateSnapshotRequestTypeDef(
    _RequiredCreateSnapshotRequestTypeDef, _OptionalCreateSnapshotRequestTypeDef
):
    pass


CreateSnapshotResultResponseTypeDef = TypedDict(
    "CreateSnapshotResultResponseTypeDef",
    {
        "SnapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrustRequestTypeDef = TypedDict(
    "_RequiredCreateTrustRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainName": str,
        "TrustPassword": str,
        "TrustDirection": TrustDirectionType,
    },
)
_OptionalCreateTrustRequestTypeDef = TypedDict(
    "_OptionalCreateTrustRequestTypeDef",
    {
        "TrustType": TrustTypeType,
        "ConditionalForwarderIpAddrs": List[str],
        "SelectiveAuth": SelectiveAuthType,
    },
    total=False,
)


class CreateTrustRequestTypeDef(
    _RequiredCreateTrustRequestTypeDef, _OptionalCreateTrustRequestTypeDef
):
    pass


CreateTrustResultResponseTypeDef = TypedDict(
    "CreateTrustResultResponseTypeDef",
    {
        "TrustId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConditionalForwarderRequestTypeDef = TypedDict(
    "DeleteConditionalForwarderRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainName": str,
    },
)

DeleteDirectoryRequestTypeDef = TypedDict(
    "DeleteDirectoryRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

DeleteDirectoryResultResponseTypeDef = TypedDict(
    "DeleteDirectoryResultResponseTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLogSubscriptionRequestTypeDef = TypedDict(
    "DeleteLogSubscriptionRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

DeleteSnapshotRequestTypeDef = TypedDict(
    "DeleteSnapshotRequestTypeDef",
    {
        "SnapshotId": str,
    },
)

DeleteSnapshotResultResponseTypeDef = TypedDict(
    "DeleteSnapshotResultResponseTypeDef",
    {
        "SnapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTrustRequestTypeDef = TypedDict(
    "_RequiredDeleteTrustRequestTypeDef",
    {
        "TrustId": str,
    },
)
_OptionalDeleteTrustRequestTypeDef = TypedDict(
    "_OptionalDeleteTrustRequestTypeDef",
    {
        "DeleteAssociatedConditionalForwarder": bool,
    },
    total=False,
)


class DeleteTrustRequestTypeDef(
    _RequiredDeleteTrustRequestTypeDef, _OptionalDeleteTrustRequestTypeDef
):
    pass


DeleteTrustResultResponseTypeDef = TypedDict(
    "DeleteTrustResultResponseTypeDef",
    {
        "TrustId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterCertificateRequestTypeDef = TypedDict(
    "DeregisterCertificateRequestTypeDef",
    {
        "DirectoryId": str,
        "CertificateId": str,
    },
)

DeregisterEventTopicRequestTypeDef = TypedDict(
    "DeregisterEventTopicRequestTypeDef",
    {
        "DirectoryId": str,
        "TopicName": str,
    },
)

DescribeCertificateRequestTypeDef = TypedDict(
    "DescribeCertificateRequestTypeDef",
    {
        "DirectoryId": str,
        "CertificateId": str,
    },
)

DescribeCertificateResultResponseTypeDef = TypedDict(
    "DescribeCertificateResultResponseTypeDef",
    {
        "Certificate": "CertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeConditionalForwardersRequestTypeDef = TypedDict(
    "_RequiredDescribeConditionalForwardersRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalDescribeConditionalForwardersRequestTypeDef = TypedDict(
    "_OptionalDescribeConditionalForwardersRequestTypeDef",
    {
        "RemoteDomainNames": List[str],
    },
    total=False,
)


class DescribeConditionalForwardersRequestTypeDef(
    _RequiredDescribeConditionalForwardersRequestTypeDef,
    _OptionalDescribeConditionalForwardersRequestTypeDef,
):
    pass


DescribeConditionalForwardersResultResponseTypeDef = TypedDict(
    "DescribeConditionalForwardersResultResponseTypeDef",
    {
        "ConditionalForwarders": List["ConditionalForwarderTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDirectoriesRequestTypeDef = TypedDict(
    "DescribeDirectoriesRequestTypeDef",
    {
        "DirectoryIds": List[str],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeDirectoriesResultResponseTypeDef = TypedDict(
    "DescribeDirectoriesResultResponseTypeDef",
    {
        "DirectoryDescriptions": List["DirectoryDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDomainControllersRequestTypeDef = TypedDict(
    "_RequiredDescribeDomainControllersRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalDescribeDomainControllersRequestTypeDef = TypedDict(
    "_OptionalDescribeDomainControllersRequestTypeDef",
    {
        "DomainControllerIds": List[str],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class DescribeDomainControllersRequestTypeDef(
    _RequiredDescribeDomainControllersRequestTypeDef,
    _OptionalDescribeDomainControllersRequestTypeDef,
):
    pass


DescribeDomainControllersResultResponseTypeDef = TypedDict(
    "DescribeDomainControllersResultResponseTypeDef",
    {
        "DomainControllers": List["DomainControllerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventTopicsRequestTypeDef = TypedDict(
    "DescribeEventTopicsRequestTypeDef",
    {
        "DirectoryId": str,
        "TopicNames": List[str],
    },
    total=False,
)

DescribeEventTopicsResultResponseTypeDef = TypedDict(
    "DescribeEventTopicsResultResponseTypeDef",
    {
        "EventTopics": List["EventTopicTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeLDAPSSettingsRequestTypeDef = TypedDict(
    "_RequiredDescribeLDAPSSettingsRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalDescribeLDAPSSettingsRequestTypeDef = TypedDict(
    "_OptionalDescribeLDAPSSettingsRequestTypeDef",
    {
        "Type": Literal["Client"],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class DescribeLDAPSSettingsRequestTypeDef(
    _RequiredDescribeLDAPSSettingsRequestTypeDef, _OptionalDescribeLDAPSSettingsRequestTypeDef
):
    pass


DescribeLDAPSSettingsResultResponseTypeDef = TypedDict(
    "DescribeLDAPSSettingsResultResponseTypeDef",
    {
        "LDAPSSettingsInfo": List["LDAPSSettingInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRegionsRequestTypeDef = TypedDict(
    "_RequiredDescribeRegionsRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalDescribeRegionsRequestTypeDef = TypedDict(
    "_OptionalDescribeRegionsRequestTypeDef",
    {
        "RegionName": str,
        "NextToken": str,
    },
    total=False,
)


class DescribeRegionsRequestTypeDef(
    _RequiredDescribeRegionsRequestTypeDef, _OptionalDescribeRegionsRequestTypeDef
):
    pass


DescribeRegionsResultResponseTypeDef = TypedDict(
    "DescribeRegionsResultResponseTypeDef",
    {
        "RegionsDescription": List["RegionDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSharedDirectoriesRequestTypeDef = TypedDict(
    "_RequiredDescribeSharedDirectoriesRequestTypeDef",
    {
        "OwnerDirectoryId": str,
    },
)
_OptionalDescribeSharedDirectoriesRequestTypeDef = TypedDict(
    "_OptionalDescribeSharedDirectoriesRequestTypeDef",
    {
        "SharedDirectoryIds": List[str],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class DescribeSharedDirectoriesRequestTypeDef(
    _RequiredDescribeSharedDirectoriesRequestTypeDef,
    _OptionalDescribeSharedDirectoriesRequestTypeDef,
):
    pass


DescribeSharedDirectoriesResultResponseTypeDef = TypedDict(
    "DescribeSharedDirectoriesResultResponseTypeDef",
    {
        "SharedDirectories": List["SharedDirectoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotsRequestTypeDef = TypedDict(
    "DescribeSnapshotsRequestTypeDef",
    {
        "DirectoryId": str,
        "SnapshotIds": List[str],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeSnapshotsResultResponseTypeDef = TypedDict(
    "DescribeSnapshotsResultResponseTypeDef",
    {
        "Snapshots": List["SnapshotTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrustsRequestTypeDef = TypedDict(
    "DescribeTrustsRequestTypeDef",
    {
        "DirectoryId": str,
        "TrustIds": List[str],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeTrustsResultResponseTypeDef = TypedDict(
    "DescribeTrustsResultResponseTypeDef",
    {
        "Trusts": List["TrustTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DirectoryConnectSettingsDescriptionTypeDef = TypedDict(
    "DirectoryConnectSettingsDescriptionTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "CustomerUserName": str,
        "SecurityGroupId": str,
        "AvailabilityZones": List[str],
        "ConnectIps": List[str],
    },
    total=False,
)

DirectoryConnectSettingsTypeDef = TypedDict(
    "DirectoryConnectSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "CustomerDnsIps": List[str],
        "CustomerUserName": str,
    },
)

DirectoryDescriptionTypeDef = TypedDict(
    "DirectoryDescriptionTypeDef",
    {
        "DirectoryId": str,
        "Name": str,
        "ShortName": str,
        "Size": DirectorySizeType,
        "Edition": DirectoryEditionType,
        "Alias": str,
        "AccessUrl": str,
        "Description": str,
        "DnsIpAddrs": List[str],
        "Stage": DirectoryStageType,
        "ShareStatus": ShareStatusType,
        "ShareMethod": ShareMethodType,
        "ShareNotes": str,
        "LaunchTime": datetime,
        "StageLastUpdatedDateTime": datetime,
        "Type": DirectoryTypeType,
        "VpcSettings": "DirectoryVpcSettingsDescriptionTypeDef",
        "ConnectSettings": "DirectoryConnectSettingsDescriptionTypeDef",
        "RadiusSettings": "RadiusSettingsTypeDef",
        "RadiusStatus": RadiusStatusType,
        "StageReason": str,
        "SsoEnabled": bool,
        "DesiredNumberOfDomainControllers": int,
        "OwnerDirectoryDescription": "OwnerDirectoryDescriptionTypeDef",
        "RegionsInfo": "RegionsInfoTypeDef",
    },
    total=False,
)

DirectoryLimitsTypeDef = TypedDict(
    "DirectoryLimitsTypeDef",
    {
        "CloudOnlyDirectoriesLimit": int,
        "CloudOnlyDirectoriesCurrentCount": int,
        "CloudOnlyDirectoriesLimitReached": bool,
        "CloudOnlyMicrosoftADLimit": int,
        "CloudOnlyMicrosoftADCurrentCount": int,
        "CloudOnlyMicrosoftADLimitReached": bool,
        "ConnectedDirectoriesLimit": int,
        "ConnectedDirectoriesCurrentCount": int,
        "ConnectedDirectoriesLimitReached": bool,
    },
    total=False,
)

DirectoryVpcSettingsDescriptionTypeDef = TypedDict(
    "DirectoryVpcSettingsDescriptionTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupId": str,
        "AvailabilityZones": List[str],
    },
    total=False,
)

DirectoryVpcSettingsTypeDef = TypedDict(
    "DirectoryVpcSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
    },
)

DisableClientAuthenticationRequestTypeDef = TypedDict(
    "DisableClientAuthenticationRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": Literal["SmartCard"],
    },
)

DisableLDAPSRequestTypeDef = TypedDict(
    "DisableLDAPSRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": Literal["Client"],
    },
)

DisableRadiusRequestTypeDef = TypedDict(
    "DisableRadiusRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

_RequiredDisableSsoRequestTypeDef = TypedDict(
    "_RequiredDisableSsoRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalDisableSsoRequestTypeDef = TypedDict(
    "_OptionalDisableSsoRequestTypeDef",
    {
        "UserName": str,
        "Password": str,
    },
    total=False,
)


class DisableSsoRequestTypeDef(
    _RequiredDisableSsoRequestTypeDef, _OptionalDisableSsoRequestTypeDef
):
    pass


DomainControllerTypeDef = TypedDict(
    "DomainControllerTypeDef",
    {
        "DirectoryId": str,
        "DomainControllerId": str,
        "DnsIpAddr": str,
        "VpcId": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "Status": DomainControllerStatusType,
        "StatusReason": str,
        "LaunchTime": datetime,
        "StatusLastUpdatedDateTime": datetime,
    },
    total=False,
)

EnableClientAuthenticationRequestTypeDef = TypedDict(
    "EnableClientAuthenticationRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": Literal["SmartCard"],
    },
)

EnableLDAPSRequestTypeDef = TypedDict(
    "EnableLDAPSRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": Literal["Client"],
    },
)

EnableRadiusRequestTypeDef = TypedDict(
    "EnableRadiusRequestTypeDef",
    {
        "DirectoryId": str,
        "RadiusSettings": "RadiusSettingsTypeDef",
    },
)

_RequiredEnableSsoRequestTypeDef = TypedDict(
    "_RequiredEnableSsoRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalEnableSsoRequestTypeDef = TypedDict(
    "_OptionalEnableSsoRequestTypeDef",
    {
        "UserName": str,
        "Password": str,
    },
    total=False,
)


class EnableSsoRequestTypeDef(_RequiredEnableSsoRequestTypeDef, _OptionalEnableSsoRequestTypeDef):
    pass


EventTopicTypeDef = TypedDict(
    "EventTopicTypeDef",
    {
        "DirectoryId": str,
        "TopicName": str,
        "TopicArn": str,
        "CreatedDateTime": datetime,
        "Status": TopicStatusType,
    },
    total=False,
)

GetDirectoryLimitsResultResponseTypeDef = TypedDict(
    "GetDirectoryLimitsResultResponseTypeDef",
    {
        "DirectoryLimits": "DirectoryLimitsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSnapshotLimitsRequestTypeDef = TypedDict(
    "GetSnapshotLimitsRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

GetSnapshotLimitsResultResponseTypeDef = TypedDict(
    "GetSnapshotLimitsResultResponseTypeDef",
    {
        "SnapshotLimits": "SnapshotLimitsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IpRouteInfoTypeDef = TypedDict(
    "IpRouteInfoTypeDef",
    {
        "DirectoryId": str,
        "CidrIp": str,
        "IpRouteStatusMsg": IpRouteStatusMsgType,
        "AddedDateTime": datetime,
        "IpRouteStatusReason": str,
        "Description": str,
    },
    total=False,
)

IpRouteTypeDef = TypedDict(
    "IpRouteTypeDef",
    {
        "CidrIp": str,
        "Description": str,
    },
    total=False,
)

LDAPSSettingInfoTypeDef = TypedDict(
    "LDAPSSettingInfoTypeDef",
    {
        "LDAPSStatus": LDAPSStatusType,
        "LDAPSStatusReason": str,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)

_RequiredListCertificatesRequestTypeDef = TypedDict(
    "_RequiredListCertificatesRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalListCertificatesRequestTypeDef = TypedDict(
    "_OptionalListCertificatesRequestTypeDef",
    {
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class ListCertificatesRequestTypeDef(
    _RequiredListCertificatesRequestTypeDef, _OptionalListCertificatesRequestTypeDef
):
    pass


ListCertificatesResultResponseTypeDef = TypedDict(
    "ListCertificatesResultResponseTypeDef",
    {
        "NextToken": str,
        "CertificatesInfo": List["CertificateInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIpRoutesRequestTypeDef = TypedDict(
    "_RequiredListIpRoutesRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalListIpRoutesRequestTypeDef = TypedDict(
    "_OptionalListIpRoutesRequestTypeDef",
    {
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class ListIpRoutesRequestTypeDef(
    _RequiredListIpRoutesRequestTypeDef, _OptionalListIpRoutesRequestTypeDef
):
    pass


ListIpRoutesResultResponseTypeDef = TypedDict(
    "ListIpRoutesResultResponseTypeDef",
    {
        "IpRoutesInfo": List["IpRouteInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLogSubscriptionsRequestTypeDef = TypedDict(
    "ListLogSubscriptionsRequestTypeDef",
    {
        "DirectoryId": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListLogSubscriptionsResultResponseTypeDef = TypedDict(
    "ListLogSubscriptionsResultResponseTypeDef",
    {
        "LogSubscriptions": List["LogSubscriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSchemaExtensionsRequestTypeDef = TypedDict(
    "_RequiredListSchemaExtensionsRequestTypeDef",
    {
        "DirectoryId": str,
    },
)
_OptionalListSchemaExtensionsRequestTypeDef = TypedDict(
    "_OptionalListSchemaExtensionsRequestTypeDef",
    {
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class ListSchemaExtensionsRequestTypeDef(
    _RequiredListSchemaExtensionsRequestTypeDef, _OptionalListSchemaExtensionsRequestTypeDef
):
    pass


ListSchemaExtensionsResultResponseTypeDef = TypedDict(
    "ListSchemaExtensionsResultResponseTypeDef",
    {
        "SchemaExtensionsInfo": List["SchemaExtensionInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalListTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestTypeDef",
    {
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class ListTagsForResourceRequestTypeDef(
    _RequiredListTagsForResourceRequestTypeDef, _OptionalListTagsForResourceRequestTypeDef
):
    pass


ListTagsForResourceResultResponseTypeDef = TypedDict(
    "ListTagsForResourceResultResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogSubscriptionTypeDef = TypedDict(
    "LogSubscriptionTypeDef",
    {
        "DirectoryId": str,
        "LogGroupName": str,
        "SubscriptionCreatedDateTime": datetime,
    },
    total=False,
)

OwnerDirectoryDescriptionTypeDef = TypedDict(
    "OwnerDirectoryDescriptionTypeDef",
    {
        "DirectoryId": str,
        "AccountId": str,
        "DnsIpAddrs": List[str],
        "VpcSettings": "DirectoryVpcSettingsDescriptionTypeDef",
        "RadiusSettings": "RadiusSettingsTypeDef",
        "RadiusStatus": RadiusStatusType,
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

RadiusSettingsTypeDef = TypedDict(
    "RadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": RadiusAuthenticationProtocolType,
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)

RegionDescriptionTypeDef = TypedDict(
    "RegionDescriptionTypeDef",
    {
        "DirectoryId": str,
        "RegionName": str,
        "RegionType": RegionTypeType,
        "Status": DirectoryStageType,
        "VpcSettings": "DirectoryVpcSettingsTypeDef",
        "DesiredNumberOfDomainControllers": int,
        "LaunchTime": datetime,
        "StatusLastUpdatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)

RegionsInfoTypeDef = TypedDict(
    "RegionsInfoTypeDef",
    {
        "PrimaryRegion": str,
        "AdditionalRegions": List[str],
    },
    total=False,
)

_RequiredRegisterCertificateRequestTypeDef = TypedDict(
    "_RequiredRegisterCertificateRequestTypeDef",
    {
        "DirectoryId": str,
        "CertificateData": str,
    },
)
_OptionalRegisterCertificateRequestTypeDef = TypedDict(
    "_OptionalRegisterCertificateRequestTypeDef",
    {
        "Type": CertificateTypeType,
        "ClientCertAuthSettings": "ClientCertAuthSettingsTypeDef",
    },
    total=False,
)


class RegisterCertificateRequestTypeDef(
    _RequiredRegisterCertificateRequestTypeDef, _OptionalRegisterCertificateRequestTypeDef
):
    pass


RegisterCertificateResultResponseTypeDef = TypedDict(
    "RegisterCertificateResultResponseTypeDef",
    {
        "CertificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterEventTopicRequestTypeDef = TypedDict(
    "RegisterEventTopicRequestTypeDef",
    {
        "DirectoryId": str,
        "TopicName": str,
    },
)

RejectSharedDirectoryRequestTypeDef = TypedDict(
    "RejectSharedDirectoryRequestTypeDef",
    {
        "SharedDirectoryId": str,
    },
)

RejectSharedDirectoryResultResponseTypeDef = TypedDict(
    "RejectSharedDirectoryResultResponseTypeDef",
    {
        "SharedDirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveIpRoutesRequestTypeDef = TypedDict(
    "RemoveIpRoutesRequestTypeDef",
    {
        "DirectoryId": str,
        "CidrIps": List[str],
    },
)

RemoveRegionRequestTypeDef = TypedDict(
    "RemoveRegionRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

RemoveTagsFromResourceRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeys": List[str],
    },
)

ResetUserPasswordRequestTypeDef = TypedDict(
    "ResetUserPasswordRequestTypeDef",
    {
        "DirectoryId": str,
        "UserName": str,
        "NewPassword": str,
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

RestoreFromSnapshotRequestTypeDef = TypedDict(
    "RestoreFromSnapshotRequestTypeDef",
    {
        "SnapshotId": str,
    },
)

SchemaExtensionInfoTypeDef = TypedDict(
    "SchemaExtensionInfoTypeDef",
    {
        "DirectoryId": str,
        "SchemaExtensionId": str,
        "Description": str,
        "SchemaExtensionStatus": SchemaExtensionStatusType,
        "SchemaExtensionStatusReason": str,
        "StartDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

_RequiredShareDirectoryRequestTypeDef = TypedDict(
    "_RequiredShareDirectoryRequestTypeDef",
    {
        "DirectoryId": str,
        "ShareTarget": "ShareTargetTypeDef",
        "ShareMethod": ShareMethodType,
    },
)
_OptionalShareDirectoryRequestTypeDef = TypedDict(
    "_OptionalShareDirectoryRequestTypeDef",
    {
        "ShareNotes": str,
    },
    total=False,
)


class ShareDirectoryRequestTypeDef(
    _RequiredShareDirectoryRequestTypeDef, _OptionalShareDirectoryRequestTypeDef
):
    pass


ShareDirectoryResultResponseTypeDef = TypedDict(
    "ShareDirectoryResultResponseTypeDef",
    {
        "SharedDirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ShareTargetTypeDef = TypedDict(
    "ShareTargetTypeDef",
    {
        "Id": str,
        "Type": Literal["ACCOUNT"],
    },
)

SharedDirectoryTypeDef = TypedDict(
    "SharedDirectoryTypeDef",
    {
        "OwnerAccountId": str,
        "OwnerDirectoryId": str,
        "ShareMethod": ShareMethodType,
        "SharedAccountId": str,
        "SharedDirectoryId": str,
        "ShareStatus": ShareStatusType,
        "ShareNotes": str,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)

SnapshotLimitsTypeDef = TypedDict(
    "SnapshotLimitsTypeDef",
    {
        "ManualSnapshotsLimit": int,
        "ManualSnapshotsCurrentCount": int,
        "ManualSnapshotsLimitReached": bool,
    },
    total=False,
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "DirectoryId": str,
        "SnapshotId": str,
        "Type": SnapshotTypeType,
        "Name": str,
        "Status": SnapshotStatusType,
        "StartTime": datetime,
    },
    total=False,
)

StartSchemaExtensionRequestTypeDef = TypedDict(
    "StartSchemaExtensionRequestTypeDef",
    {
        "DirectoryId": str,
        "CreateSnapshotBeforeSchemaExtension": bool,
        "LdifContent": str,
        "Description": str,
    },
)

StartSchemaExtensionResultResponseTypeDef = TypedDict(
    "StartSchemaExtensionResultResponseTypeDef",
    {
        "SchemaExtensionId": str,
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

TrustTypeDef = TypedDict(
    "TrustTypeDef",
    {
        "DirectoryId": str,
        "TrustId": str,
        "RemoteDomainName": str,
        "TrustType": TrustTypeType,
        "TrustDirection": TrustDirectionType,
        "TrustState": TrustStateType,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
        "StateLastUpdatedDateTime": datetime,
        "TrustStateReason": str,
        "SelectiveAuth": SelectiveAuthType,
    },
    total=False,
)

UnshareDirectoryRequestTypeDef = TypedDict(
    "UnshareDirectoryRequestTypeDef",
    {
        "DirectoryId": str,
        "UnshareTarget": "UnshareTargetTypeDef",
    },
)

UnshareDirectoryResultResponseTypeDef = TypedDict(
    "UnshareDirectoryResultResponseTypeDef",
    {
        "SharedDirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnshareTargetTypeDef = TypedDict(
    "UnshareTargetTypeDef",
    {
        "Id": str,
        "Type": Literal["ACCOUNT"],
    },
)

UpdateConditionalForwarderRequestTypeDef = TypedDict(
    "UpdateConditionalForwarderRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainName": str,
        "DnsIpAddrs": List[str],
    },
)

UpdateNumberOfDomainControllersRequestTypeDef = TypedDict(
    "UpdateNumberOfDomainControllersRequestTypeDef",
    {
        "DirectoryId": str,
        "DesiredNumber": int,
    },
)

UpdateRadiusRequestTypeDef = TypedDict(
    "UpdateRadiusRequestTypeDef",
    {
        "DirectoryId": str,
        "RadiusSettings": "RadiusSettingsTypeDef",
    },
)

_RequiredUpdateTrustRequestTypeDef = TypedDict(
    "_RequiredUpdateTrustRequestTypeDef",
    {
        "TrustId": str,
    },
)
_OptionalUpdateTrustRequestTypeDef = TypedDict(
    "_OptionalUpdateTrustRequestTypeDef",
    {
        "SelectiveAuth": SelectiveAuthType,
    },
    total=False,
)


class UpdateTrustRequestTypeDef(
    _RequiredUpdateTrustRequestTypeDef, _OptionalUpdateTrustRequestTypeDef
):
    pass


UpdateTrustResultResponseTypeDef = TypedDict(
    "UpdateTrustResultResponseTypeDef",
    {
        "RequestId": str,
        "TrustId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerifyTrustRequestTypeDef = TypedDict(
    "VerifyTrustRequestTypeDef",
    {
        "TrustId": str,
    },
)

VerifyTrustResultResponseTypeDef = TypedDict(
    "VerifyTrustResultResponseTypeDef",
    {
        "TrustId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
