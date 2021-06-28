"""
Type annotations for guardduty service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/type_defs.html)

Usage::

    ```python
    from mypy_boto3_guardduty.type_defs import AcceptInvitationRequestTypeDef

    data: AcceptInvitationRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AdminStatusType,
    DataSourceStatusType,
    DataSourceType,
    DetectorStatusType,
    FeedbackType,
    FilterActionType,
    FindingPublishingFrequencyType,
    IpSetFormatType,
    IpSetStatusType,
    OrderByType,
    PublishingStatusType,
    ThreatIntelSetFormatType,
    ThreatIntelSetStatusType,
    UsageStatisticTypeType,
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
    "AcceptInvitationRequestTypeDef",
    "AccessControlListTypeDef",
    "AccessKeyDetailsTypeDef",
    "AccountDetailTypeDef",
    "AccountLevelPermissionsTypeDef",
    "ActionTypeDef",
    "AdminAccountTypeDef",
    "ArchiveFindingsRequestTypeDef",
    "AwsApiCallActionTypeDef",
    "BlockPublicAccessTypeDef",
    "BucketLevelPermissionsTypeDef",
    "BucketPolicyTypeDef",
    "CityTypeDef",
    "CloudTrailConfigurationResultTypeDef",
    "ConditionTypeDef",
    "CountryTypeDef",
    "CreateDetectorRequestTypeDef",
    "CreateDetectorResponseResponseTypeDef",
    "CreateFilterRequestTypeDef",
    "CreateFilterResponseResponseTypeDef",
    "CreateIPSetRequestTypeDef",
    "CreateIPSetResponseResponseTypeDef",
    "CreateMembersRequestTypeDef",
    "CreateMembersResponseResponseTypeDef",
    "CreatePublishingDestinationRequestTypeDef",
    "CreatePublishingDestinationResponseResponseTypeDef",
    "CreateSampleFindingsRequestTypeDef",
    "CreateThreatIntelSetRequestTypeDef",
    "CreateThreatIntelSetResponseResponseTypeDef",
    "DNSLogsConfigurationResultTypeDef",
    "DataSourceConfigurationsResultTypeDef",
    "DataSourceConfigurationsTypeDef",
    "DeclineInvitationsRequestTypeDef",
    "DeclineInvitationsResponseResponseTypeDef",
    "DefaultServerSideEncryptionTypeDef",
    "DeleteDetectorRequestTypeDef",
    "DeleteFilterRequestTypeDef",
    "DeleteIPSetRequestTypeDef",
    "DeleteInvitationsRequestTypeDef",
    "DeleteInvitationsResponseResponseTypeDef",
    "DeleteMembersRequestTypeDef",
    "DeleteMembersResponseResponseTypeDef",
    "DeletePublishingDestinationRequestTypeDef",
    "DeleteThreatIntelSetRequestTypeDef",
    "DescribeOrganizationConfigurationRequestTypeDef",
    "DescribeOrganizationConfigurationResponseResponseTypeDef",
    "DescribePublishingDestinationRequestTypeDef",
    "DescribePublishingDestinationResponseResponseTypeDef",
    "DestinationPropertiesTypeDef",
    "DestinationTypeDef",
    "DisableOrganizationAdminAccountRequestTypeDef",
    "DisassociateFromMasterAccountRequestTypeDef",
    "DisassociateMembersRequestTypeDef",
    "DisassociateMembersResponseResponseTypeDef",
    "DnsRequestActionTypeDef",
    "DomainDetailsTypeDef",
    "EnableOrganizationAdminAccountRequestTypeDef",
    "EvidenceTypeDef",
    "FindingCriteriaTypeDef",
    "FindingStatisticsTypeDef",
    "FindingTypeDef",
    "FlowLogsConfigurationResultTypeDef",
    "GeoLocationTypeDef",
    "GetDetectorRequestTypeDef",
    "GetDetectorResponseResponseTypeDef",
    "GetFilterRequestTypeDef",
    "GetFilterResponseResponseTypeDef",
    "GetFindingsRequestTypeDef",
    "GetFindingsResponseResponseTypeDef",
    "GetFindingsStatisticsRequestTypeDef",
    "GetFindingsStatisticsResponseResponseTypeDef",
    "GetIPSetRequestTypeDef",
    "GetIPSetResponseResponseTypeDef",
    "GetInvitationsCountResponseResponseTypeDef",
    "GetMasterAccountRequestTypeDef",
    "GetMasterAccountResponseResponseTypeDef",
    "GetMemberDetectorsRequestTypeDef",
    "GetMemberDetectorsResponseResponseTypeDef",
    "GetMembersRequestTypeDef",
    "GetMembersResponseResponseTypeDef",
    "GetThreatIntelSetRequestTypeDef",
    "GetThreatIntelSetResponseResponseTypeDef",
    "GetUsageStatisticsRequestTypeDef",
    "GetUsageStatisticsResponseResponseTypeDef",
    "IamInstanceProfileTypeDef",
    "InstanceDetailsTypeDef",
    "InvitationTypeDef",
    "InviteMembersRequestTypeDef",
    "InviteMembersResponseResponseTypeDef",
    "ListDetectorsRequestTypeDef",
    "ListDetectorsResponseResponseTypeDef",
    "ListFiltersRequestTypeDef",
    "ListFiltersResponseResponseTypeDef",
    "ListFindingsRequestTypeDef",
    "ListFindingsResponseResponseTypeDef",
    "ListIPSetsRequestTypeDef",
    "ListIPSetsResponseResponseTypeDef",
    "ListInvitationsRequestTypeDef",
    "ListInvitationsResponseResponseTypeDef",
    "ListMembersRequestTypeDef",
    "ListMembersResponseResponseTypeDef",
    "ListOrganizationAdminAccountsRequestTypeDef",
    "ListOrganizationAdminAccountsResponseResponseTypeDef",
    "ListPublishingDestinationsRequestTypeDef",
    "ListPublishingDestinationsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListThreatIntelSetsRequestTypeDef",
    "ListThreatIntelSetsResponseResponseTypeDef",
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
    "ResponseMetadataTypeDef",
    "S3BucketDetailTypeDef",
    "S3LogsConfigurationResultTypeDef",
    "S3LogsConfigurationTypeDef",
    "SecurityGroupTypeDef",
    "ServiceTypeDef",
    "SortCriteriaTypeDef",
    "StartMonitoringMembersRequestTypeDef",
    "StartMonitoringMembersResponseResponseTypeDef",
    "StopMonitoringMembersRequestTypeDef",
    "StopMonitoringMembersResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "ThreatIntelligenceDetailTypeDef",
    "TotalTypeDef",
    "UnarchiveFindingsRequestTypeDef",
    "UnprocessedAccountTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDetectorRequestTypeDef",
    "UpdateFilterRequestTypeDef",
    "UpdateFilterResponseResponseTypeDef",
    "UpdateFindingsFeedbackRequestTypeDef",
    "UpdateIPSetRequestTypeDef",
    "UpdateMemberDetectorsRequestTypeDef",
    "UpdateMemberDetectorsResponseResponseTypeDef",
    "UpdateOrganizationConfigurationRequestTypeDef",
    "UpdatePublishingDestinationRequestTypeDef",
    "UpdateThreatIntelSetRequestTypeDef",
    "UsageAccountResultTypeDef",
    "UsageCriteriaTypeDef",
    "UsageDataSourceResultTypeDef",
    "UsageResourceResultTypeDef",
    "UsageStatisticsTypeDef",
)

AcceptInvitationRequestTypeDef = TypedDict(
    "AcceptInvitationRequestTypeDef",
    {
        "DetectorId": str,
        "MasterId": str,
        "InvitationId": str,
    },
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

ArchiveFindingsRequestTypeDef = TypedDict(
    "ArchiveFindingsRequestTypeDef",
    {
        "DetectorId": str,
        "FindingIds": List[str],
    },
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

_RequiredCreateDetectorRequestTypeDef = TypedDict(
    "_RequiredCreateDetectorRequestTypeDef",
    {
        "Enable": bool,
    },
)
_OptionalCreateDetectorRequestTypeDef = TypedDict(
    "_OptionalCreateDetectorRequestTypeDef",
    {
        "ClientToken": str,
        "FindingPublishingFrequency": FindingPublishingFrequencyType,
        "DataSources": "DataSourceConfigurationsTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateDetectorRequestTypeDef(
    _RequiredCreateDetectorRequestTypeDef, _OptionalCreateDetectorRequestTypeDef
):
    pass


CreateDetectorResponseResponseTypeDef = TypedDict(
    "CreateDetectorResponseResponseTypeDef",
    {
        "DetectorId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFilterRequestTypeDef = TypedDict(
    "_RequiredCreateFilterRequestTypeDef",
    {
        "DetectorId": str,
        "Name": str,
        "FindingCriteria": "FindingCriteriaTypeDef",
    },
)
_OptionalCreateFilterRequestTypeDef = TypedDict(
    "_OptionalCreateFilterRequestTypeDef",
    {
        "Description": str,
        "Action": FilterActionType,
        "Rank": int,
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateFilterRequestTypeDef(
    _RequiredCreateFilterRequestTypeDef, _OptionalCreateFilterRequestTypeDef
):
    pass


CreateFilterResponseResponseTypeDef = TypedDict(
    "CreateFilterResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIPSetRequestTypeDef = TypedDict(
    "_RequiredCreateIPSetRequestTypeDef",
    {
        "DetectorId": str,
        "Name": str,
        "Format": IpSetFormatType,
        "Location": str,
        "Activate": bool,
    },
)
_OptionalCreateIPSetRequestTypeDef = TypedDict(
    "_OptionalCreateIPSetRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateIPSetRequestTypeDef(
    _RequiredCreateIPSetRequestTypeDef, _OptionalCreateIPSetRequestTypeDef
):
    pass


CreateIPSetResponseResponseTypeDef = TypedDict(
    "CreateIPSetResponseResponseTypeDef",
    {
        "IpSetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMembersRequestTypeDef = TypedDict(
    "CreateMembersRequestTypeDef",
    {
        "DetectorId": str,
        "AccountDetails": List["AccountDetailTypeDef"],
    },
)

CreateMembersResponseResponseTypeDef = TypedDict(
    "CreateMembersResponseResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePublishingDestinationRequestTypeDef = TypedDict(
    "_RequiredCreatePublishingDestinationRequestTypeDef",
    {
        "DetectorId": str,
        "DestinationType": Literal["S3"],
        "DestinationProperties": "DestinationPropertiesTypeDef",
    },
)
_OptionalCreatePublishingDestinationRequestTypeDef = TypedDict(
    "_OptionalCreatePublishingDestinationRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class CreatePublishingDestinationRequestTypeDef(
    _RequiredCreatePublishingDestinationRequestTypeDef,
    _OptionalCreatePublishingDestinationRequestTypeDef,
):
    pass


CreatePublishingDestinationResponseResponseTypeDef = TypedDict(
    "CreatePublishingDestinationResponseResponseTypeDef",
    {
        "DestinationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSampleFindingsRequestTypeDef = TypedDict(
    "_RequiredCreateSampleFindingsRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalCreateSampleFindingsRequestTypeDef = TypedDict(
    "_OptionalCreateSampleFindingsRequestTypeDef",
    {
        "FindingTypes": List[str],
    },
    total=False,
)


class CreateSampleFindingsRequestTypeDef(
    _RequiredCreateSampleFindingsRequestTypeDef, _OptionalCreateSampleFindingsRequestTypeDef
):
    pass


_RequiredCreateThreatIntelSetRequestTypeDef = TypedDict(
    "_RequiredCreateThreatIntelSetRequestTypeDef",
    {
        "DetectorId": str,
        "Name": str,
        "Format": ThreatIntelSetFormatType,
        "Location": str,
        "Activate": bool,
    },
)
_OptionalCreateThreatIntelSetRequestTypeDef = TypedDict(
    "_OptionalCreateThreatIntelSetRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateThreatIntelSetRequestTypeDef(
    _RequiredCreateThreatIntelSetRequestTypeDef, _OptionalCreateThreatIntelSetRequestTypeDef
):
    pass


CreateThreatIntelSetResponseResponseTypeDef = TypedDict(
    "CreateThreatIntelSetResponseResponseTypeDef",
    {
        "ThreatIntelSetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

DeclineInvitationsRequestTypeDef = TypedDict(
    "DeclineInvitationsRequestTypeDef",
    {
        "AccountIds": List[str],
    },
)

DeclineInvitationsResponseResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

DeleteDetectorRequestTypeDef = TypedDict(
    "DeleteDetectorRequestTypeDef",
    {
        "DetectorId": str,
    },
)

DeleteFilterRequestTypeDef = TypedDict(
    "DeleteFilterRequestTypeDef",
    {
        "DetectorId": str,
        "FilterName": str,
    },
)

DeleteIPSetRequestTypeDef = TypedDict(
    "DeleteIPSetRequestTypeDef",
    {
        "DetectorId": str,
        "IpSetId": str,
    },
)

DeleteInvitationsRequestTypeDef = TypedDict(
    "DeleteInvitationsRequestTypeDef",
    {
        "AccountIds": List[str],
    },
)

DeleteInvitationsResponseResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMembersRequestTypeDef = TypedDict(
    "DeleteMembersRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": List[str],
    },
)

DeleteMembersResponseResponseTypeDef = TypedDict(
    "DeleteMembersResponseResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePublishingDestinationRequestTypeDef = TypedDict(
    "DeletePublishingDestinationRequestTypeDef",
    {
        "DetectorId": str,
        "DestinationId": str,
    },
)

DeleteThreatIntelSetRequestTypeDef = TypedDict(
    "DeleteThreatIntelSetRequestTypeDef",
    {
        "DetectorId": str,
        "ThreatIntelSetId": str,
    },
)

DescribeOrganizationConfigurationRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigurationRequestTypeDef",
    {
        "DetectorId": str,
    },
)

DescribeOrganizationConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseResponseTypeDef",
    {
        "AutoEnable": bool,
        "MemberAccountLimitReached": bool,
        "DataSources": "OrganizationDataSourceConfigurationsResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePublishingDestinationRequestTypeDef = TypedDict(
    "DescribePublishingDestinationRequestTypeDef",
    {
        "DetectorId": str,
        "DestinationId": str,
    },
)

DescribePublishingDestinationResponseResponseTypeDef = TypedDict(
    "DescribePublishingDestinationResponseResponseTypeDef",
    {
        "DestinationId": str,
        "DestinationType": Literal["S3"],
        "Status": PublishingStatusType,
        "PublishingFailureStartTimestamp": int,
        "DestinationProperties": "DestinationPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

DisableOrganizationAdminAccountRequestTypeDef = TypedDict(
    "DisableOrganizationAdminAccountRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)

DisassociateFromMasterAccountRequestTypeDef = TypedDict(
    "DisassociateFromMasterAccountRequestTypeDef",
    {
        "DetectorId": str,
    },
)

DisassociateMembersRequestTypeDef = TypedDict(
    "DisassociateMembersRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": List[str],
    },
)

DisassociateMembersResponseResponseTypeDef = TypedDict(
    "DisassociateMembersResponseResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

EnableOrganizationAdminAccountRequestTypeDef = TypedDict(
    "EnableOrganizationAdminAccountRequestTypeDef",
    {
        "AdminAccountId": str,
    },
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

GetDetectorRequestTypeDef = TypedDict(
    "GetDetectorRequestTypeDef",
    {
        "DetectorId": str,
    },
)

GetDetectorResponseResponseTypeDef = TypedDict(
    "GetDetectorResponseResponseTypeDef",
    {
        "CreatedAt": str,
        "FindingPublishingFrequency": FindingPublishingFrequencyType,
        "ServiceRole": str,
        "Status": DetectorStatusType,
        "UpdatedAt": str,
        "DataSources": "DataSourceConfigurationsResultTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFilterRequestTypeDef = TypedDict(
    "GetFilterRequestTypeDef",
    {
        "DetectorId": str,
        "FilterName": str,
    },
)

GetFilterResponseResponseTypeDef = TypedDict(
    "GetFilterResponseResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": FilterActionType,
        "Rank": int,
        "FindingCriteria": "FindingCriteriaTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFindingsRequestTypeDef = TypedDict(
    "_RequiredGetFindingsRequestTypeDef",
    {
        "DetectorId": str,
        "FindingIds": List[str],
    },
)
_OptionalGetFindingsRequestTypeDef = TypedDict(
    "_OptionalGetFindingsRequestTypeDef",
    {
        "SortCriteria": "SortCriteriaTypeDef",
    },
    total=False,
)


class GetFindingsRequestTypeDef(
    _RequiredGetFindingsRequestTypeDef, _OptionalGetFindingsRequestTypeDef
):
    pass


GetFindingsResponseResponseTypeDef = TypedDict(
    "GetFindingsResponseResponseTypeDef",
    {
        "Findings": List["FindingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFindingsStatisticsRequestTypeDef = TypedDict(
    "_RequiredGetFindingsStatisticsRequestTypeDef",
    {
        "DetectorId": str,
        "FindingStatisticTypes": List[Literal["COUNT_BY_SEVERITY"]],
    },
)
_OptionalGetFindingsStatisticsRequestTypeDef = TypedDict(
    "_OptionalGetFindingsStatisticsRequestTypeDef",
    {
        "FindingCriteria": "FindingCriteriaTypeDef",
    },
    total=False,
)


class GetFindingsStatisticsRequestTypeDef(
    _RequiredGetFindingsStatisticsRequestTypeDef, _OptionalGetFindingsStatisticsRequestTypeDef
):
    pass


GetFindingsStatisticsResponseResponseTypeDef = TypedDict(
    "GetFindingsStatisticsResponseResponseTypeDef",
    {
        "FindingStatistics": "FindingStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIPSetRequestTypeDef = TypedDict(
    "GetIPSetRequestTypeDef",
    {
        "DetectorId": str,
        "IpSetId": str,
    },
)

GetIPSetResponseResponseTypeDef = TypedDict(
    "GetIPSetResponseResponseTypeDef",
    {
        "Name": str,
        "Format": IpSetFormatType,
        "Location": str,
        "Status": IpSetStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInvitationsCountResponseResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseResponseTypeDef",
    {
        "InvitationsCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMasterAccountRequestTypeDef = TypedDict(
    "GetMasterAccountRequestTypeDef",
    {
        "DetectorId": str,
    },
)

GetMasterAccountResponseResponseTypeDef = TypedDict(
    "GetMasterAccountResponseResponseTypeDef",
    {
        "Master": "MasterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMemberDetectorsRequestTypeDef = TypedDict(
    "GetMemberDetectorsRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": List[str],
    },
)

GetMemberDetectorsResponseResponseTypeDef = TypedDict(
    "GetMemberDetectorsResponseResponseTypeDef",
    {
        "MemberDataSourceConfigurations": List["MemberDataSourceConfigurationTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMembersRequestTypeDef = TypedDict(
    "GetMembersRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": List[str],
    },
)

GetMembersResponseResponseTypeDef = TypedDict(
    "GetMembersResponseResponseTypeDef",
    {
        "Members": List["MemberTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetThreatIntelSetRequestTypeDef = TypedDict(
    "GetThreatIntelSetRequestTypeDef",
    {
        "DetectorId": str,
        "ThreatIntelSetId": str,
    },
)

GetThreatIntelSetResponseResponseTypeDef = TypedDict(
    "GetThreatIntelSetResponseResponseTypeDef",
    {
        "Name": str,
        "Format": ThreatIntelSetFormatType,
        "Location": str,
        "Status": ThreatIntelSetStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUsageStatisticsRequestTypeDef = TypedDict(
    "_RequiredGetUsageStatisticsRequestTypeDef",
    {
        "DetectorId": str,
        "UsageStatisticType": UsageStatisticTypeType,
        "UsageCriteria": "UsageCriteriaTypeDef",
    },
)
_OptionalGetUsageStatisticsRequestTypeDef = TypedDict(
    "_OptionalGetUsageStatisticsRequestTypeDef",
    {
        "Unit": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetUsageStatisticsRequestTypeDef(
    _RequiredGetUsageStatisticsRequestTypeDef, _OptionalGetUsageStatisticsRequestTypeDef
):
    pass


GetUsageStatisticsResponseResponseTypeDef = TypedDict(
    "GetUsageStatisticsResponseResponseTypeDef",
    {
        "UsageStatistics": "UsageStatisticsTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredInviteMembersRequestTypeDef = TypedDict(
    "_RequiredInviteMembersRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": List[str],
    },
)
_OptionalInviteMembersRequestTypeDef = TypedDict(
    "_OptionalInviteMembersRequestTypeDef",
    {
        "DisableEmailNotification": bool,
        "Message": str,
    },
    total=False,
)


class InviteMembersRequestTypeDef(
    _RequiredInviteMembersRequestTypeDef, _OptionalInviteMembersRequestTypeDef
):
    pass


InviteMembersResponseResponseTypeDef = TypedDict(
    "InviteMembersResponseResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDetectorsRequestTypeDef = TypedDict(
    "ListDetectorsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDetectorsResponseResponseTypeDef = TypedDict(
    "ListDetectorsResponseResponseTypeDef",
    {
        "DetectorIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFiltersRequestTypeDef = TypedDict(
    "_RequiredListFiltersRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalListFiltersRequestTypeDef = TypedDict(
    "_OptionalListFiltersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListFiltersRequestTypeDef(
    _RequiredListFiltersRequestTypeDef, _OptionalListFiltersRequestTypeDef
):
    pass


ListFiltersResponseResponseTypeDef = TypedDict(
    "ListFiltersResponseResponseTypeDef",
    {
        "FilterNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFindingsRequestTypeDef = TypedDict(
    "_RequiredListFindingsRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalListFindingsRequestTypeDef = TypedDict(
    "_OptionalListFindingsRequestTypeDef",
    {
        "FindingCriteria": "FindingCriteriaTypeDef",
        "SortCriteria": "SortCriteriaTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListFindingsRequestTypeDef(
    _RequiredListFindingsRequestTypeDef, _OptionalListFindingsRequestTypeDef
):
    pass


ListFindingsResponseResponseTypeDef = TypedDict(
    "ListFindingsResponseResponseTypeDef",
    {
        "FindingIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIPSetsRequestTypeDef = TypedDict(
    "_RequiredListIPSetsRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalListIPSetsRequestTypeDef = TypedDict(
    "_OptionalListIPSetsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListIPSetsRequestTypeDef(
    _RequiredListIPSetsRequestTypeDef, _OptionalListIPSetsRequestTypeDef
):
    pass


ListIPSetsResponseResponseTypeDef = TypedDict(
    "ListIPSetsResponseResponseTypeDef",
    {
        "IpSetIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInvitationsRequestTypeDef = TypedDict(
    "ListInvitationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListInvitationsResponseResponseTypeDef = TypedDict(
    "ListInvitationsResponseResponseTypeDef",
    {
        "Invitations": List["InvitationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMembersRequestTypeDef = TypedDict(
    "_RequiredListMembersRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalListMembersRequestTypeDef = TypedDict(
    "_OptionalListMembersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "OnlyAssociated": str,
    },
    total=False,
)


class ListMembersRequestTypeDef(
    _RequiredListMembersRequestTypeDef, _OptionalListMembersRequestTypeDef
):
    pass


ListMembersResponseResponseTypeDef = TypedDict(
    "ListMembersResponseResponseTypeDef",
    {
        "Members": List["MemberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationAdminAccountsRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListOrganizationAdminAccountsResponseResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseResponseTypeDef",
    {
        "AdminAccounts": List["AdminAccountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPublishingDestinationsRequestTypeDef = TypedDict(
    "_RequiredListPublishingDestinationsRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalListPublishingDestinationsRequestTypeDef = TypedDict(
    "_OptionalListPublishingDestinationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListPublishingDestinationsRequestTypeDef(
    _RequiredListPublishingDestinationsRequestTypeDef,
    _OptionalListPublishingDestinationsRequestTypeDef,
):
    pass


ListPublishingDestinationsResponseResponseTypeDef = TypedDict(
    "ListPublishingDestinationsResponseResponseTypeDef",
    {
        "Destinations": List["DestinationTypeDef"],
        "NextToken": str,
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
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThreatIntelSetsRequestTypeDef = TypedDict(
    "_RequiredListThreatIntelSetsRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalListThreatIntelSetsRequestTypeDef = TypedDict(
    "_OptionalListThreatIntelSetsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListThreatIntelSetsRequestTypeDef(
    _RequiredListThreatIntelSetsRequestTypeDef, _OptionalListThreatIntelSetsRequestTypeDef
):
    pass


ListThreatIntelSetsResponseResponseTypeDef = TypedDict(
    "ListThreatIntelSetsResponseResponseTypeDef",
    {
        "ThreatIntelSetIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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

StartMonitoringMembersRequestTypeDef = TypedDict(
    "StartMonitoringMembersRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": List[str],
    },
)

StartMonitoringMembersResponseResponseTypeDef = TypedDict(
    "StartMonitoringMembersResponseResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopMonitoringMembersRequestTypeDef = TypedDict(
    "StopMonitoringMembersRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": List[str],
    },
)

StopMonitoringMembersResponseResponseTypeDef = TypedDict(
    "StopMonitoringMembersResponseResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
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

UnarchiveFindingsRequestTypeDef = TypedDict(
    "UnarchiveFindingsRequestTypeDef",
    {
        "DetectorId": str,
        "FindingIds": List[str],
    },
)

UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {
        "AccountId": str,
        "Result": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDetectorRequestTypeDef = TypedDict(
    "_RequiredUpdateDetectorRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalUpdateDetectorRequestTypeDef = TypedDict(
    "_OptionalUpdateDetectorRequestTypeDef",
    {
        "Enable": bool,
        "FindingPublishingFrequency": FindingPublishingFrequencyType,
        "DataSources": "DataSourceConfigurationsTypeDef",
    },
    total=False,
)


class UpdateDetectorRequestTypeDef(
    _RequiredUpdateDetectorRequestTypeDef, _OptionalUpdateDetectorRequestTypeDef
):
    pass


_RequiredUpdateFilterRequestTypeDef = TypedDict(
    "_RequiredUpdateFilterRequestTypeDef",
    {
        "DetectorId": str,
        "FilterName": str,
    },
)
_OptionalUpdateFilterRequestTypeDef = TypedDict(
    "_OptionalUpdateFilterRequestTypeDef",
    {
        "Description": str,
        "Action": FilterActionType,
        "Rank": int,
        "FindingCriteria": "FindingCriteriaTypeDef",
    },
    total=False,
)


class UpdateFilterRequestTypeDef(
    _RequiredUpdateFilterRequestTypeDef, _OptionalUpdateFilterRequestTypeDef
):
    pass


UpdateFilterResponseResponseTypeDef = TypedDict(
    "UpdateFilterResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFindingsFeedbackRequestTypeDef = TypedDict(
    "_RequiredUpdateFindingsFeedbackRequestTypeDef",
    {
        "DetectorId": str,
        "FindingIds": List[str],
        "Feedback": FeedbackType,
    },
)
_OptionalUpdateFindingsFeedbackRequestTypeDef = TypedDict(
    "_OptionalUpdateFindingsFeedbackRequestTypeDef",
    {
        "Comments": str,
    },
    total=False,
)


class UpdateFindingsFeedbackRequestTypeDef(
    _RequiredUpdateFindingsFeedbackRequestTypeDef, _OptionalUpdateFindingsFeedbackRequestTypeDef
):
    pass


_RequiredUpdateIPSetRequestTypeDef = TypedDict(
    "_RequiredUpdateIPSetRequestTypeDef",
    {
        "DetectorId": str,
        "IpSetId": str,
    },
)
_OptionalUpdateIPSetRequestTypeDef = TypedDict(
    "_OptionalUpdateIPSetRequestTypeDef",
    {
        "Name": str,
        "Location": str,
        "Activate": bool,
    },
    total=False,
)


class UpdateIPSetRequestTypeDef(
    _RequiredUpdateIPSetRequestTypeDef, _OptionalUpdateIPSetRequestTypeDef
):
    pass


_RequiredUpdateMemberDetectorsRequestTypeDef = TypedDict(
    "_RequiredUpdateMemberDetectorsRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": List[str],
    },
)
_OptionalUpdateMemberDetectorsRequestTypeDef = TypedDict(
    "_OptionalUpdateMemberDetectorsRequestTypeDef",
    {
        "DataSources": "DataSourceConfigurationsTypeDef",
    },
    total=False,
)


class UpdateMemberDetectorsRequestTypeDef(
    _RequiredUpdateMemberDetectorsRequestTypeDef, _OptionalUpdateMemberDetectorsRequestTypeDef
):
    pass


UpdateMemberDetectorsResponseResponseTypeDef = TypedDict(
    "UpdateMemberDetectorsResponseResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateOrganizationConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateOrganizationConfigurationRequestTypeDef",
    {
        "DetectorId": str,
        "AutoEnable": bool,
    },
)
_OptionalUpdateOrganizationConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateOrganizationConfigurationRequestTypeDef",
    {
        "DataSources": "OrganizationDataSourceConfigurationsTypeDef",
    },
    total=False,
)


class UpdateOrganizationConfigurationRequestTypeDef(
    _RequiredUpdateOrganizationConfigurationRequestTypeDef,
    _OptionalUpdateOrganizationConfigurationRequestTypeDef,
):
    pass


_RequiredUpdatePublishingDestinationRequestTypeDef = TypedDict(
    "_RequiredUpdatePublishingDestinationRequestTypeDef",
    {
        "DetectorId": str,
        "DestinationId": str,
    },
)
_OptionalUpdatePublishingDestinationRequestTypeDef = TypedDict(
    "_OptionalUpdatePublishingDestinationRequestTypeDef",
    {
        "DestinationProperties": "DestinationPropertiesTypeDef",
    },
    total=False,
)


class UpdatePublishingDestinationRequestTypeDef(
    _RequiredUpdatePublishingDestinationRequestTypeDef,
    _OptionalUpdatePublishingDestinationRequestTypeDef,
):
    pass


_RequiredUpdateThreatIntelSetRequestTypeDef = TypedDict(
    "_RequiredUpdateThreatIntelSetRequestTypeDef",
    {
        "DetectorId": str,
        "ThreatIntelSetId": str,
    },
)
_OptionalUpdateThreatIntelSetRequestTypeDef = TypedDict(
    "_OptionalUpdateThreatIntelSetRequestTypeDef",
    {
        "Name": str,
        "Location": str,
        "Activate": bool,
    },
    total=False,
)


class UpdateThreatIntelSetRequestTypeDef(
    _RequiredUpdateThreatIntelSetRequestTypeDef, _OptionalUpdateThreatIntelSetRequestTypeDef
):
    pass


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
