"""
Type annotations for ds service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ds.type_defs import AcceptSharedDirectoryResultTypeDef

    data: AcceptSharedDirectoryResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

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
    "AcceptSharedDirectoryResultTypeDef",
    "AttributeTypeDef",
    "CertificateInfoTypeDef",
    "CertificateTypeDef",
    "ClientCertAuthSettingsTypeDef",
    "ComputerTypeDef",
    "ConditionalForwarderTypeDef",
    "ConnectDirectoryResultTypeDef",
    "CreateAliasResultTypeDef",
    "CreateComputerResultTypeDef",
    "CreateDirectoryResultTypeDef",
    "CreateMicrosoftADResultTypeDef",
    "CreateSnapshotResultTypeDef",
    "CreateTrustResultTypeDef",
    "DeleteDirectoryResultTypeDef",
    "DeleteSnapshotResultTypeDef",
    "DeleteTrustResultTypeDef",
    "DescribeCertificateResultTypeDef",
    "DescribeConditionalForwardersResultTypeDef",
    "DescribeDirectoriesResultTypeDef",
    "DescribeDomainControllersResultTypeDef",
    "DescribeEventTopicsResultTypeDef",
    "DescribeLDAPSSettingsResultTypeDef",
    "DescribeRegionsResultTypeDef",
    "DescribeSharedDirectoriesResultTypeDef",
    "DescribeSnapshotsResultTypeDef",
    "DescribeTrustsResultTypeDef",
    "DirectoryConnectSettingsDescriptionTypeDef",
    "DirectoryConnectSettingsTypeDef",
    "DirectoryDescriptionTypeDef",
    "DirectoryLimitsTypeDef",
    "DirectoryVpcSettingsDescriptionTypeDef",
    "DirectoryVpcSettingsTypeDef",
    "DomainControllerTypeDef",
    "EventTopicTypeDef",
    "GetDirectoryLimitsResultTypeDef",
    "GetSnapshotLimitsResultTypeDef",
    "IpRouteInfoTypeDef",
    "IpRouteTypeDef",
    "LDAPSSettingInfoTypeDef",
    "ListCertificatesResultTypeDef",
    "ListIpRoutesResultTypeDef",
    "ListLogSubscriptionsResultTypeDef",
    "ListSchemaExtensionsResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "LogSubscriptionTypeDef",
    "OwnerDirectoryDescriptionTypeDef",
    "PaginatorConfigTypeDef",
    "RadiusSettingsTypeDef",
    "RegionDescriptionTypeDef",
    "RegionsInfoTypeDef",
    "RegisterCertificateResultTypeDef",
    "RejectSharedDirectoryResultTypeDef",
    "SchemaExtensionInfoTypeDef",
    "ShareDirectoryResultTypeDef",
    "ShareTargetTypeDef",
    "SharedDirectoryTypeDef",
    "SnapshotLimitsTypeDef",
    "SnapshotTypeDef",
    "StartSchemaExtensionResultTypeDef",
    "TagTypeDef",
    "TrustTypeDef",
    "UnshareDirectoryResultTypeDef",
    "UnshareTargetTypeDef",
    "UpdateTrustResultTypeDef",
    "VerifyTrustResultTypeDef",
)

AcceptSharedDirectoryResultTypeDef = TypedDict(
    "AcceptSharedDirectoryResultTypeDef",
    {
        "SharedDirectory": "SharedDirectoryTypeDef",
    },
    total=False,
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
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

ConnectDirectoryResultTypeDef = TypedDict(
    "ConnectDirectoryResultTypeDef",
    {
        "DirectoryId": str,
    },
    total=False,
)

CreateAliasResultTypeDef = TypedDict(
    "CreateAliasResultTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
    },
    total=False,
)

CreateComputerResultTypeDef = TypedDict(
    "CreateComputerResultTypeDef",
    {
        "Computer": "ComputerTypeDef",
    },
    total=False,
)

CreateDirectoryResultTypeDef = TypedDict(
    "CreateDirectoryResultTypeDef",
    {
        "DirectoryId": str,
    },
    total=False,
)

CreateMicrosoftADResultTypeDef = TypedDict(
    "CreateMicrosoftADResultTypeDef",
    {
        "DirectoryId": str,
    },
    total=False,
)

CreateSnapshotResultTypeDef = TypedDict(
    "CreateSnapshotResultTypeDef",
    {
        "SnapshotId": str,
    },
    total=False,
)

CreateTrustResultTypeDef = TypedDict(
    "CreateTrustResultTypeDef",
    {
        "TrustId": str,
    },
    total=False,
)

DeleteDirectoryResultTypeDef = TypedDict(
    "DeleteDirectoryResultTypeDef",
    {
        "DirectoryId": str,
    },
    total=False,
)

DeleteSnapshotResultTypeDef = TypedDict(
    "DeleteSnapshotResultTypeDef",
    {
        "SnapshotId": str,
    },
    total=False,
)

DeleteTrustResultTypeDef = TypedDict(
    "DeleteTrustResultTypeDef",
    {
        "TrustId": str,
    },
    total=False,
)

DescribeCertificateResultTypeDef = TypedDict(
    "DescribeCertificateResultTypeDef",
    {
        "Certificate": "CertificateTypeDef",
    },
    total=False,
)

DescribeConditionalForwardersResultTypeDef = TypedDict(
    "DescribeConditionalForwardersResultTypeDef",
    {
        "ConditionalForwarders": List["ConditionalForwarderTypeDef"],
    },
    total=False,
)

DescribeDirectoriesResultTypeDef = TypedDict(
    "DescribeDirectoriesResultTypeDef",
    {
        "DirectoryDescriptions": List["DirectoryDescriptionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeDomainControllersResultTypeDef = TypedDict(
    "DescribeDomainControllersResultTypeDef",
    {
        "DomainControllers": List["DomainControllerTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeEventTopicsResultTypeDef = TypedDict(
    "DescribeEventTopicsResultTypeDef",
    {
        "EventTopics": List["EventTopicTypeDef"],
    },
    total=False,
)

DescribeLDAPSSettingsResultTypeDef = TypedDict(
    "DescribeLDAPSSettingsResultTypeDef",
    {
        "LDAPSSettingsInfo": List["LDAPSSettingInfoTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeRegionsResultTypeDef = TypedDict(
    "DescribeRegionsResultTypeDef",
    {
        "RegionsDescription": List["RegionDescriptionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeSharedDirectoriesResultTypeDef = TypedDict(
    "DescribeSharedDirectoriesResultTypeDef",
    {
        "SharedDirectories": List["SharedDirectoryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeSnapshotsResultTypeDef = TypedDict(
    "DescribeSnapshotsResultTypeDef",
    {
        "Snapshots": List["SnapshotTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeTrustsResultTypeDef = TypedDict(
    "DescribeTrustsResultTypeDef",
    {
        "Trusts": List["TrustTypeDef"],
        "NextToken": str,
    },
    total=False,
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

GetDirectoryLimitsResultTypeDef = TypedDict(
    "GetDirectoryLimitsResultTypeDef",
    {
        "DirectoryLimits": "DirectoryLimitsTypeDef",
    },
    total=False,
)

GetSnapshotLimitsResultTypeDef = TypedDict(
    "GetSnapshotLimitsResultTypeDef",
    {
        "SnapshotLimits": "SnapshotLimitsTypeDef",
    },
    total=False,
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

ListCertificatesResultTypeDef = TypedDict(
    "ListCertificatesResultTypeDef",
    {
        "NextToken": str,
        "CertificatesInfo": List["CertificateInfoTypeDef"],
    },
    total=False,
)

ListIpRoutesResultTypeDef = TypedDict(
    "ListIpRoutesResultTypeDef",
    {
        "IpRoutesInfo": List["IpRouteInfoTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListLogSubscriptionsResultTypeDef = TypedDict(
    "ListLogSubscriptionsResultTypeDef",
    {
        "LogSubscriptions": List["LogSubscriptionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListSchemaExtensionsResultTypeDef = TypedDict(
    "ListSchemaExtensionsResultTypeDef",
    {
        "SchemaExtensionsInfo": List["SchemaExtensionInfoTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
    },
    total=False,
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

RegisterCertificateResultTypeDef = TypedDict(
    "RegisterCertificateResultTypeDef",
    {
        "CertificateId": str,
    },
    total=False,
)

RejectSharedDirectoryResultTypeDef = TypedDict(
    "RejectSharedDirectoryResultTypeDef",
    {
        "SharedDirectoryId": str,
    },
    total=False,
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

ShareDirectoryResultTypeDef = TypedDict(
    "ShareDirectoryResultTypeDef",
    {
        "SharedDirectoryId": str,
    },
    total=False,
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

StartSchemaExtensionResultTypeDef = TypedDict(
    "StartSchemaExtensionResultTypeDef",
    {
        "SchemaExtensionId": str,
    },
    total=False,
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

UnshareDirectoryResultTypeDef = TypedDict(
    "UnshareDirectoryResultTypeDef",
    {
        "SharedDirectoryId": str,
    },
    total=False,
)

UnshareTargetTypeDef = TypedDict(
    "UnshareTargetTypeDef",
    {
        "Id": str,
        "Type": Literal["ACCOUNT"],
    },
)

UpdateTrustResultTypeDef = TypedDict(
    "UpdateTrustResultTypeDef",
    {
        "RequestId": str,
        "TrustId": str,
    },
    total=False,
)

VerifyTrustResultTypeDef = TypedDict(
    "VerifyTrustResultTypeDef",
    {
        "TrustId": str,
    },
    total=False,
)
