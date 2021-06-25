"""
Type annotations for guardduty service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/type_defs.html)

Usage::

    ```python
    from mypy_boto3_guardduty.type_defs import AccessControlListTypeDef

    data: AccessControlListTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from .literals import (
    AdminStatusType,
    DataSourceStatusType,
    DataSourceType,
    DetectorStatusType,
    FilterActionType,
    FindingPublishingFrequencyType,
    IpSetFormatType,
    IpSetStatusType,
    OrderByType,
    PublishingStatusType,
    ThreatIntelSetFormatType,
    ThreatIntelSetStatusType,
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
    "AccessControlListTypeDef",
    "AccessKeyDetailsTypeDef",
    "AccountDetailTypeDef",
    "AccountLevelPermissionsTypeDef",
    "ActionTypeDef",
    "AdminAccountTypeDef",
    "AwsApiCallActionTypeDef",
    "BlockPublicAccessTypeDef",
    "BucketLevelPermissionsTypeDef",
    "BucketPolicyTypeDef",
    "CityTypeDef",
    "CloudTrailConfigurationResultTypeDef",
    "ConditionTypeDef",
    "CountryTypeDef",
    "CreateDetectorResponseTypeDef",
    "CreateFilterResponseTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateMembersResponseTypeDef",
    "CreatePublishingDestinationResponseTypeDef",
    "CreateThreatIntelSetResponseTypeDef",
    "DNSLogsConfigurationResultTypeDef",
    "DataSourceConfigurationsResultTypeDef",
    "DataSourceConfigurationsTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DefaultServerSideEncryptionTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DeleteMembersResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DescribePublishingDestinationResponseTypeDef",
    "DestinationPropertiesTypeDef",
    "DestinationTypeDef",
    "DisassociateMembersResponseTypeDef",
    "DnsRequestActionTypeDef",
    "DomainDetailsTypeDef",
    "EvidenceTypeDef",
    "FindingCriteriaTypeDef",
    "FindingStatisticsTypeDef",
    "FindingTypeDef",
    "FlowLogsConfigurationResultTypeDef",
    "GeoLocationTypeDef",
    "GetDetectorResponseTypeDef",
    "GetFilterResponseTypeDef",
    "GetFindingsResponseTypeDef",
    "GetFindingsStatisticsResponseTypeDef",
    "GetIPSetResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMemberDetectorsResponseTypeDef",
    "GetMembersResponseTypeDef",
    "GetThreatIntelSetResponseTypeDef",
    "GetUsageStatisticsResponseTypeDef",
    "IamInstanceProfileTypeDef",
    "InstanceDetailsTypeDef",
    "InvitationTypeDef",
    "InviteMembersResponseTypeDef",
    "ListDetectorsResponseTypeDef",
    "ListFiltersResponseTypeDef",
    "ListFindingsResponseTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListPublishingDestinationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListThreatIntelSetsResponseTypeDef",
    "LocalIpDetailsTypeDef",
    "LocalPortDetailsTypeDef",
    "MasterTypeDef",
    "MemberDataSourceConfigurationTypeDef",
    "MemberTypeDef",
    "NetworkConnectionActionTypeDef",
    "NetworkInterfaceTypeDef",
    "OrganizationDataSourceConfigurationsResultTypeDef",
    "OrganizationDataSourceConfigurationsTypeDef",
    "OrganizationS3LogsConfigurationResultTypeDef",
    "OrganizationS3LogsConfigurationTypeDef",
    "OrganizationTypeDef",
    "OwnerTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionConfigurationTypeDef",
    "PortProbeActionTypeDef",
    "PortProbeDetailTypeDef",
    "PrivateIpAddressDetailsTypeDef",
    "ProductCodeTypeDef",
    "PublicAccessTypeDef",
    "RemoteIpDetailsTypeDef",
    "RemotePortDetailsTypeDef",
    "ResourceTypeDef",
    "S3BucketDetailTypeDef",
    "S3LogsConfigurationResultTypeDef",
    "S3LogsConfigurationTypeDef",
    "SecurityGroupTypeDef",
    "ServiceTypeDef",
    "SortCriteriaTypeDef",
    "StartMonitoringMembersResponseTypeDef",
    "StopMonitoringMembersResponseTypeDef",
    "TagTypeDef",
    "ThreatIntelligenceDetailTypeDef",
    "TotalTypeDef",
    "UnprocessedAccountTypeDef",
    "UpdateFilterResponseTypeDef",
    "UpdateMemberDetectorsResponseTypeDef",
    "UsageAccountResultTypeDef",
    "UsageCriteriaTypeDef",
    "UsageDataSourceResultTypeDef",
    "UsageResourceResultTypeDef",
    "UsageStatisticsTypeDef",
)

AccessControlListTypeDef = TypedDict(
    "AccessControlListTypeDef",
    {
        "AllowsPublicReadAccess": bool,
        "AllowsPublicWriteAccess": bool,
    },
    total=False,
)

AccessKeyDetailsTypeDef = TypedDict(
    "AccessKeyDetailsTypeDef",
    {
        "AccessKeyId": str,
        "PrincipalId": str,
        "UserName": str,
        "UserType": str,
    },
    total=False,
)

AccountDetailTypeDef = TypedDict(
    "AccountDetailTypeDef",
    {
        "AccountId": str,
        "Email": str,
    },
)

AccountLevelPermissionsTypeDef = TypedDict(
    "AccountLevelPermissionsTypeDef",
    {
        "BlockPublicAccess": "BlockPublicAccessTypeDef",
    },
    total=False,
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ActionType": str,
        "AwsApiCallAction": "AwsApiCallActionTypeDef",
        "DnsRequestAction": "DnsRequestActionTypeDef",
        "NetworkConnectionAction": "NetworkConnectionActionTypeDef",
        "PortProbeAction": "PortProbeActionTypeDef",
    },
    total=False,
)

AdminAccountTypeDef = TypedDict(
    "AdminAccountTypeDef",
    {
        "AdminAccountId": str,
        "AdminStatus": AdminStatusType,
    },
    total=False,
)

AwsApiCallActionTypeDef = TypedDict(
    "AwsApiCallActionTypeDef",
    {
        "Api": str,
        "CallerType": str,
        "DomainDetails": "DomainDetailsTypeDef",
        "ErrorCode": str,
        "RemoteIpDetails": "RemoteIpDetailsTypeDef",
        "ServiceName": str,
    },
    total=False,
)

BlockPublicAccessTypeDef = TypedDict(
    "BlockPublicAccessTypeDef",
    {
        "IgnorePublicAcls": bool,
        "RestrictPublicBuckets": bool,
        "BlockPublicAcls": bool,
        "BlockPublicPolicy": bool,
    },
    total=False,
)

BucketLevelPermissionsTypeDef = TypedDict(
    "BucketLevelPermissionsTypeDef",
    {
        "AccessControlList": "AccessControlListTypeDef",
        "BucketPolicy": "BucketPolicyTypeDef",
        "BlockPublicAccess": "BlockPublicAccessTypeDef",
    },
    total=False,
)

BucketPolicyTypeDef = TypedDict(
    "BucketPolicyTypeDef",
    {
        "AllowsPublicReadAccess": bool,
        "AllowsPublicWriteAccess": bool,
    },
    total=False,
)

CityTypeDef = TypedDict(
    "CityTypeDef",
    {
        "CityName": str,
    },
    total=False,
)

CloudTrailConfigurationResultTypeDef = TypedDict(
    "CloudTrailConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)

CountryTypeDef = TypedDict(
    "CountryTypeDef",
    {
        "CountryCode": str,
        "CountryName": str,
    },
    total=False,
)

CreateDetectorResponseTypeDef = TypedDict(
    "CreateDetectorResponseTypeDef",
    {
        "DetectorId": str,
    },
    total=False,
)

CreateFilterResponseTypeDef = TypedDict(
    "CreateFilterResponseTypeDef",
    {
        "Name": str,
    },
)

CreateIPSetResponseTypeDef = TypedDict(
    "CreateIPSetResponseTypeDef",
    {
        "IpSetId": str,
    },
)

CreateMembersResponseTypeDef = TypedDict(
    "CreateMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
    },
)

CreatePublishingDestinationResponseTypeDef = TypedDict(
    "CreatePublishingDestinationResponseTypeDef",
    {
        "DestinationId": str,
    },
)

CreateThreatIntelSetResponseTypeDef = TypedDict(
    "CreateThreatIntelSetResponseTypeDef",
    {
        "ThreatIntelSetId": str,
    },
)

DNSLogsConfigurationResultTypeDef = TypedDict(
    "DNSLogsConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)

DataSourceConfigurationsResultTypeDef = TypedDict(
    "DataSourceConfigurationsResultTypeDef",
    {
        "CloudTrail": "CloudTrailConfigurationResultTypeDef",
        "DNSLogs": "DNSLogsConfigurationResultTypeDef",
        "FlowLogs": "FlowLogsConfigurationResultTypeDef",
        "S3Logs": "S3LogsConfigurationResultTypeDef",
    },
)

DataSourceConfigurationsTypeDef = TypedDict(
    "DataSourceConfigurationsTypeDef",
    {
        "S3Logs": "S3LogsConfigurationTypeDef",
    },
    total=False,
)

DeclineInvitationsResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
    },
)

DefaultServerSideEncryptionTypeDef = TypedDict(
    "DefaultServerSideEncryptionTypeDef",
    {
        "EncryptionType": str,
        "KmsMasterKeyArn": str,
    },
    total=False,
)

DeleteInvitationsResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
    },
)

DeleteMembersResponseTypeDef = TypedDict(
    "DeleteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
    },
)

_RequiredDescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "_RequiredDescribeOrganizationConfigurationResponseTypeDef",
    {
        "AutoEnable": bool,
        "MemberAccountLimitReached": bool,
    },
)
_OptionalDescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "_OptionalDescribeOrganizationConfigurationResponseTypeDef",
    {
        "DataSources": "OrganizationDataSourceConfigurationsResultTypeDef",
    },
    total=False,
)


class DescribeOrganizationConfigurationResponseTypeDef(
    _RequiredDescribeOrganizationConfigurationResponseTypeDef,
    _OptionalDescribeOrganizationConfigurationResponseTypeDef,
):
    pass


DescribePublishingDestinationResponseTypeDef = TypedDict(
    "DescribePublishingDestinationResponseTypeDef",
    {
        "DestinationId": str,
        "DestinationType": Literal["S3"],
        "Status": PublishingStatusType,
        "PublishingFailureStartTimestamp": int,
        "DestinationProperties": "DestinationPropertiesTypeDef",
    },
)

DestinationPropertiesTypeDef = TypedDict(
    "DestinationPropertiesTypeDef",
    {
        "DestinationArn": str,
        "KmsKeyArn": str,
    },
    total=False,
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "DestinationId": str,
        "DestinationType": Literal["S3"],
        "Status": PublishingStatusType,
    },
)

DisassociateMembersResponseTypeDef = TypedDict(
    "DisassociateMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
    },
)

DnsRequestActionTypeDef = TypedDict(
    "DnsRequestActionTypeDef",
    {
        "Domain": str,
    },
    total=False,
)

DomainDetailsTypeDef = TypedDict(
    "DomainDetailsTypeDef",
    {
        "Domain": str,
    },
    total=False,
)

EvidenceTypeDef = TypedDict(
    "EvidenceTypeDef",
    {
        "ThreatIntelligenceDetails": List["ThreatIntelligenceDetailTypeDef"],
    },
    total=False,
)

FindingCriteriaTypeDef = TypedDict(
    "FindingCriteriaTypeDef",
    {
        "Criterion": Dict[str, "ConditionTypeDef"],
    },
    total=False,
)

FindingStatisticsTypeDef = TypedDict(
    "FindingStatisticsTypeDef",
    {
        "CountBySeverity": Dict[str, int],
    },
    total=False,
)

_RequiredFindingTypeDef = TypedDict(
    "_RequiredFindingTypeDef",
    {
        "AccountId": str,
        "Arn": str,
        "CreatedAt": str,
        "Id": str,
        "Region": str,
        "Resource": "ResourceTypeDef",
        "SchemaVersion": str,
        "Severity": float,
        "Type": str,
        "UpdatedAt": str,
    },
)
_OptionalFindingTypeDef = TypedDict(
    "_OptionalFindingTypeDef",
    {
        "Confidence": float,
        "Description": str,
        "Partition": str,
        "Service": "ServiceTypeDef",
        "Title": str,
    },
    total=False,
)


class FindingTypeDef(_RequiredFindingTypeDef, _OptionalFindingTypeDef):
    pass


FlowLogsConfigurationResultTypeDef = TypedDict(
    "FlowLogsConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)

GeoLocationTypeDef = TypedDict(
    "GeoLocationTypeDef",
    {
        "Lat": float,
        "Lon": float,
    },
    total=False,
)

_RequiredGetDetectorResponseTypeDef = TypedDict(
    "_RequiredGetDetectorResponseTypeDef",
    {
        "ServiceRole": str,
        "Status": DetectorStatusType,
    },
)
_OptionalGetDetectorResponseTypeDef = TypedDict(
    "_OptionalGetDetectorResponseTypeDef",
    {
        "CreatedAt": str,
        "FindingPublishingFrequency": FindingPublishingFrequencyType,
        "UpdatedAt": str,
        "DataSources": "DataSourceConfigurationsResultTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class GetDetectorResponseTypeDef(
    _RequiredGetDetectorResponseTypeDef, _OptionalGetDetectorResponseTypeDef
):
    pass


_RequiredGetFilterResponseTypeDef = TypedDict(
    "_RequiredGetFilterResponseTypeDef",
    {
        "Name": str,
        "Action": FilterActionType,
        "FindingCriteria": "FindingCriteriaTypeDef",
    },
)
_OptionalGetFilterResponseTypeDef = TypedDict(
    "_OptionalGetFilterResponseTypeDef",
    {
        "Description": str,
        "Rank": int,
        "Tags": Dict[str, str],
    },
    total=False,
)


class GetFilterResponseTypeDef(
    _RequiredGetFilterResponseTypeDef, _OptionalGetFilterResponseTypeDef
):
    pass


GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef",
    {
        "Findings": List["FindingTypeDef"],
    },
)

GetFindingsStatisticsResponseTypeDef = TypedDict(
    "GetFindingsStatisticsResponseTypeDef",
    {
        "FindingStatistics": "FindingStatisticsTypeDef",
    },
)

_RequiredGetIPSetResponseTypeDef = TypedDict(
    "_RequiredGetIPSetResponseTypeDef",
    {
        "Name": str,
        "Format": IpSetFormatType,
        "Location": str,
        "Status": IpSetStatusType,
    },
)
_OptionalGetIPSetResponseTypeDef = TypedDict(
    "_OptionalGetIPSetResponseTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class GetIPSetResponseTypeDef(_RequiredGetIPSetResponseTypeDef, _OptionalGetIPSetResponseTypeDef):
    pass


GetInvitationsCountResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseTypeDef",
    {
        "InvitationsCount": int,
    },
    total=False,
)

GetMasterAccountResponseTypeDef = TypedDict(
    "GetMasterAccountResponseTypeDef",
    {
        "Master": "MasterTypeDef",
    },
)

GetMemberDetectorsResponseTypeDef = TypedDict(
    "GetMemberDetectorsResponseTypeDef",
    {
        "MemberDataSourceConfigurations": List["MemberDataSourceConfigurationTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
    },
)

GetMembersResponseTypeDef = TypedDict(
    "GetMembersResponseTypeDef",
    {
        "Members": List["MemberTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
    },
)

_RequiredGetThreatIntelSetResponseTypeDef = TypedDict(
    "_RequiredGetThreatIntelSetResponseTypeDef",
    {
        "Name": str,
        "Format": ThreatIntelSetFormatType,
        "Location": str,
        "Status": ThreatIntelSetStatusType,
    },
)
_OptionalGetThreatIntelSetResponseTypeDef = TypedDict(
    "_OptionalGetThreatIntelSetResponseTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class GetThreatIntelSetResponseTypeDef(
    _RequiredGetThreatIntelSetResponseTypeDef, _OptionalGetThreatIntelSetResponseTypeDef
):
    pass


GetUsageStatisticsResponseTypeDef = TypedDict(
    "GetUsageStatisticsResponseTypeDef",
    {
        "UsageStatistics": "UsageStatisticsTypeDef",
        "NextToken": str,
    },
    total=False,
)

IamInstanceProfileTypeDef = TypedDict(
    "IamInstanceProfileTypeDef",
    {
        "Arn": str,
        "Id": str,
    },
    total=False,
)

InstanceDetailsTypeDef = TypedDict(
    "InstanceDetailsTypeDef",
    {
        "AvailabilityZone": str,
        "IamInstanceProfile": "IamInstanceProfileTypeDef",
        "ImageDescription": str,
        "ImageId": str,
        "InstanceId": str,
        "InstanceState": str,
        "InstanceType": str,
        "OutpostArn": str,
        "LaunchTime": str,
        "NetworkInterfaces": List["NetworkInterfaceTypeDef"],
        "Platform": str,
        "ProductCodes": List["ProductCodeTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "AccountId": str,
        "InvitationId": str,
        "RelationshipStatus": str,
        "InvitedAt": str,
    },
    total=False,
)

InviteMembersResponseTypeDef = TypedDict(
    "InviteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
    },
)

_RequiredListDetectorsResponseTypeDef = TypedDict(
    "_RequiredListDetectorsResponseTypeDef",
    {
        "DetectorIds": List[str],
    },
)
_OptionalListDetectorsResponseTypeDef = TypedDict(
    "_OptionalListDetectorsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListDetectorsResponseTypeDef(
    _RequiredListDetectorsResponseTypeDef, _OptionalListDetectorsResponseTypeDef
):
    pass


_RequiredListFiltersResponseTypeDef = TypedDict(
    "_RequiredListFiltersResponseTypeDef",
    {
        "FilterNames": List[str],
    },
)
_OptionalListFiltersResponseTypeDef = TypedDict(
    "_OptionalListFiltersResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListFiltersResponseTypeDef(
    _RequiredListFiltersResponseTypeDef, _OptionalListFiltersResponseTypeDef
):
    pass


_RequiredListFindingsResponseTypeDef = TypedDict(
    "_RequiredListFindingsResponseTypeDef",
    {
        "FindingIds": List[str],
    },
)
_OptionalListFindingsResponseTypeDef = TypedDict(
    "_OptionalListFindingsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListFindingsResponseTypeDef(
    _RequiredListFindingsResponseTypeDef, _OptionalListFindingsResponseTypeDef
):
    pass


_RequiredListIPSetsResponseTypeDef = TypedDict(
    "_RequiredListIPSetsResponseTypeDef",
    {
        "IpSetIds": List[str],
    },
)
_OptionalListIPSetsResponseTypeDef = TypedDict(
    "_OptionalListIPSetsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListIPSetsResponseTypeDef(
    _RequiredListIPSetsResponseTypeDef, _OptionalListIPSetsResponseTypeDef
):
    pass


ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {
        "Invitations": List["InvitationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {
        "Members": List["MemberTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {
        "AdminAccounts": List["AdminAccountTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredListPublishingDestinationsResponseTypeDef = TypedDict(
    "_RequiredListPublishingDestinationsResponseTypeDef",
    {
        "Destinations": List["DestinationTypeDef"],
    },
)
_OptionalListPublishingDestinationsResponseTypeDef = TypedDict(
    "_OptionalListPublishingDestinationsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListPublishingDestinationsResponseTypeDef(
    _RequiredListPublishingDestinationsResponseTypeDef,
    _OptionalListPublishingDestinationsResponseTypeDef,
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredListThreatIntelSetsResponseTypeDef = TypedDict(
    "_RequiredListThreatIntelSetsResponseTypeDef",
    {
        "ThreatIntelSetIds": List[str],
    },
)
_OptionalListThreatIntelSetsResponseTypeDef = TypedDict(
    "_OptionalListThreatIntelSetsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListThreatIntelSetsResponseTypeDef(
    _RequiredListThreatIntelSetsResponseTypeDef, _OptionalListThreatIntelSetsResponseTypeDef
):
    pass


LocalIpDetailsTypeDef = TypedDict(
    "LocalIpDetailsTypeDef",
    {
        "IpAddressV4": str,
    },
    total=False,
)

LocalPortDetailsTypeDef = TypedDict(
    "LocalPortDetailsTypeDef",
    {
        "Port": int,
        "PortName": str,
    },
    total=False,
)

MasterTypeDef = TypedDict(
    "MasterTypeDef",
    {
        "AccountId": str,
        "InvitationId": str,
        "RelationshipStatus": str,
        "InvitedAt": str,
    },
    total=False,
)

MemberDataSourceConfigurationTypeDef = TypedDict(
    "MemberDataSourceConfigurationTypeDef",
    {
        "AccountId": str,
        "DataSources": "DataSourceConfigurationsResultTypeDef",
    },
)

_RequiredMemberTypeDef = TypedDict(
    "_RequiredMemberTypeDef",
    {
        "AccountId": str,
        "MasterId": str,
        "Email": str,
        "RelationshipStatus": str,
        "UpdatedAt": str,
    },
)
_OptionalMemberTypeDef = TypedDict(
    "_OptionalMemberTypeDef",
    {
        "DetectorId": str,
        "InvitedAt": str,
    },
    total=False,
)


class MemberTypeDef(_RequiredMemberTypeDef, _OptionalMemberTypeDef):
    pass


NetworkConnectionActionTypeDef = TypedDict(
    "NetworkConnectionActionTypeDef",
    {
        "Blocked": bool,
        "ConnectionDirection": str,
        "LocalPortDetails": "LocalPortDetailsTypeDef",
        "Protocol": str,
        "LocalIpDetails": "LocalIpDetailsTypeDef",
        "RemoteIpDetails": "RemoteIpDetailsTypeDef",
        "RemotePortDetails": "RemotePortDetailsTypeDef",
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "Ipv6Addresses": List[str],
        "NetworkInterfaceId": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressDetailsTypeDef"],
        "PublicDnsName": str,
        "PublicIp": str,
        "SecurityGroups": List["SecurityGroupTypeDef"],
        "SubnetId": str,
        "VpcId": str,
    },
    total=False,
)

OrganizationDataSourceConfigurationsResultTypeDef = TypedDict(
    "OrganizationDataSourceConfigurationsResultTypeDef",
    {
        "S3Logs": "OrganizationS3LogsConfigurationResultTypeDef",
    },
)

OrganizationDataSourceConfigurationsTypeDef = TypedDict(
    "OrganizationDataSourceConfigurationsTypeDef",
    {
        "S3Logs": "OrganizationS3LogsConfigurationTypeDef",
    },
    total=False,
)

OrganizationS3LogsConfigurationResultTypeDef = TypedDict(
    "OrganizationS3LogsConfigurationResultTypeDef",
    {
        "AutoEnable": bool,
    },
)

OrganizationS3LogsConfigurationTypeDef = TypedDict(
    "OrganizationS3LogsConfigurationTypeDef",
    {
        "AutoEnable": bool,
    },
)

OrganizationTypeDef = TypedDict(
    "OrganizationTypeDef",
    {
        "Asn": str,
        "AsnOrg": str,
        "Isp": str,
        "Org": str,
    },
    total=False,
)

OwnerTypeDef = TypedDict(
    "OwnerTypeDef",
    {
        "Id": str,
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

PermissionConfigurationTypeDef = TypedDict(
    "PermissionConfigurationTypeDef",
    {
        "BucketLevelPermissions": "BucketLevelPermissionsTypeDef",
        "AccountLevelPermissions": "AccountLevelPermissionsTypeDef",
    },
    total=False,
)

PortProbeActionTypeDef = TypedDict(
    "PortProbeActionTypeDef",
    {
        "Blocked": bool,
        "PortProbeDetails": List["PortProbeDetailTypeDef"],
    },
    total=False,
)

PortProbeDetailTypeDef = TypedDict(
    "PortProbeDetailTypeDef",
    {
        "LocalPortDetails": "LocalPortDetailsTypeDef",
        "LocalIpDetails": "LocalIpDetailsTypeDef",
        "RemoteIpDetails": "RemoteIpDetailsTypeDef",
    },
    total=False,
)

PrivateIpAddressDetailsTypeDef = TypedDict(
    "PrivateIpAddressDetailsTypeDef",
    {
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
    },
    total=False,
)

ProductCodeTypeDef = TypedDict(
    "ProductCodeTypeDef",
    {
        "Code": str,
        "ProductType": str,
    },
    total=False,
)

PublicAccessTypeDef = TypedDict(
    "PublicAccessTypeDef",
    {
        "PermissionConfiguration": "PermissionConfigurationTypeDef",
        "EffectivePermission": str,
    },
    total=False,
)

RemoteIpDetailsTypeDef = TypedDict(
    "RemoteIpDetailsTypeDef",
    {
        "City": "CityTypeDef",
        "Country": "CountryTypeDef",
        "GeoLocation": "GeoLocationTypeDef",
        "IpAddressV4": str,
        "Organization": "OrganizationTypeDef",
    },
    total=False,
)

RemotePortDetailsTypeDef = TypedDict(
    "RemotePortDetailsTypeDef",
    {
        "Port": int,
        "PortName": str,
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "AccessKeyDetails": "AccessKeyDetailsTypeDef",
        "S3BucketDetails": List["S3BucketDetailTypeDef"],
        "InstanceDetails": "InstanceDetailsTypeDef",
        "ResourceType": str,
    },
    total=False,
)

S3BucketDetailTypeDef = TypedDict(
    "S3BucketDetailTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": str,
        "CreatedAt": datetime,
        "Owner": "OwnerTypeDef",
        "Tags": List["TagTypeDef"],
        "DefaultServerSideEncryption": "DefaultServerSideEncryptionTypeDef",
        "PublicAccess": "PublicAccessTypeDef",
    },
    total=False,
)

S3LogsConfigurationResultTypeDef = TypedDict(
    "S3LogsConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)

S3LogsConfigurationTypeDef = TypedDict(
    "S3LogsConfigurationTypeDef",
    {
        "Enable": bool,
    },
)

SecurityGroupTypeDef = TypedDict(
    "SecurityGroupTypeDef",
    {
        "GroupId": str,
        "GroupName": str,
    },
    total=False,
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "Action": "ActionTypeDef",
        "Evidence": "EvidenceTypeDef",
        "Archived": bool,
        "Count": int,
        "DetectorId": str,
        "EventFirstSeen": str,
        "EventLastSeen": str,
        "ResourceRole": str,
        "ServiceName": str,
        "UserFeedback": str,
    },
    total=False,
)

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "AttributeName": str,
        "OrderBy": OrderByType,
    },
    total=False,
)

StartMonitoringMembersResponseTypeDef = TypedDict(
    "StartMonitoringMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
    },
)

StopMonitoringMembersResponseTypeDef = TypedDict(
    "StopMonitoringMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

ThreatIntelligenceDetailTypeDef = TypedDict(
    "ThreatIntelligenceDetailTypeDef",
    {
        "ThreatListName": str,
        "ThreatNames": List[str],
    },
    total=False,
)

TotalTypeDef = TypedDict(
    "TotalTypeDef",
    {
        "Amount": str,
        "Unit": str,
    },
    total=False,
)

UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {
        "AccountId": str,
        "Result": str,
    },
)

UpdateFilterResponseTypeDef = TypedDict(
    "UpdateFilterResponseTypeDef",
    {
        "Name": str,
    },
)

UpdateMemberDetectorsResponseTypeDef = TypedDict(
    "UpdateMemberDetectorsResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
    },
)

UsageAccountResultTypeDef = TypedDict(
    "UsageAccountResultTypeDef",
    {
        "AccountId": str,
        "Total": "TotalTypeDef",
    },
    total=False,
)

_RequiredUsageCriteriaTypeDef = TypedDict(
    "_RequiredUsageCriteriaTypeDef",
    {
        "DataSources": List[DataSourceType],
    },
)
_OptionalUsageCriteriaTypeDef = TypedDict(
    "_OptionalUsageCriteriaTypeDef",
    {
        "AccountIds": List[str],
        "Resources": List[str],
    },
    total=False,
)


class UsageCriteriaTypeDef(_RequiredUsageCriteriaTypeDef, _OptionalUsageCriteriaTypeDef):
    pass


UsageDataSourceResultTypeDef = TypedDict(
    "UsageDataSourceResultTypeDef",
    {
        "DataSource": DataSourceType,
        "Total": "TotalTypeDef",
    },
    total=False,
)

UsageResourceResultTypeDef = TypedDict(
    "UsageResourceResultTypeDef",
    {
        "Resource": str,
        "Total": "TotalTypeDef",
    },
    total=False,
)

UsageStatisticsTypeDef = TypedDict(
    "UsageStatisticsTypeDef",
    {
        "SumByAccount": List["UsageAccountResultTypeDef"],
        "SumByDataSource": List["UsageDataSourceResultTypeDef"],
        "SumByResource": List["UsageResourceResultTypeDef"],
        "TopResources": List["UsageResourceResultTypeDef"],
    },
    total=False,
)
