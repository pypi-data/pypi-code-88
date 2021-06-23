"""
Type annotations for route53 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/type_defs.html)

Usage::

    ```python
    from mypy_boto3_route53.type_defs import AccountLimitTypeDef

    data: AccountLimitTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from .literals import (
    AccountLimitTypeType,
    ChangeActionType,
    ChangeStatusType,
    CloudWatchRegionType,
    ComparisonOperatorType,
    HealthCheckRegionType,
    HealthCheckTypeType,
    HostedZoneLimitTypeType,
    InsufficientDataHealthStatusType,
    ResourceRecordSetFailoverType,
    ResourceRecordSetRegionType,
    RRTypeType,
    StatisticType,
    TagResourceTypeType,
    VPCRegionType,
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
    "AccountLimitTypeDef",
    "ActivateKeySigningKeyResponseTypeDef",
    "AlarmIdentifierTypeDef",
    "AliasTargetTypeDef",
    "AssociateVPCWithHostedZoneResponseTypeDef",
    "ChangeBatchTypeDef",
    "ChangeInfoTypeDef",
    "ChangeResourceRecordSetsResponseTypeDef",
    "ChangeTypeDef",
    "CloudWatchAlarmConfigurationTypeDef",
    "CreateHealthCheckResponseTypeDef",
    "CreateHostedZoneResponseTypeDef",
    "CreateKeySigningKeyResponseTypeDef",
    "CreateQueryLoggingConfigResponseTypeDef",
    "CreateReusableDelegationSetResponseTypeDef",
    "CreateTrafficPolicyInstanceResponseTypeDef",
    "CreateTrafficPolicyResponseTypeDef",
    "CreateTrafficPolicyVersionResponseTypeDef",
    "CreateVPCAssociationAuthorizationResponseTypeDef",
    "DNSSECStatusTypeDef",
    "DeactivateKeySigningKeyResponseTypeDef",
    "DelegationSetTypeDef",
    "DeleteHostedZoneResponseTypeDef",
    "DeleteKeySigningKeyResponseTypeDef",
    "DimensionTypeDef",
    "DisableHostedZoneDNSSECResponseTypeDef",
    "DisassociateVPCFromHostedZoneResponseTypeDef",
    "EnableHostedZoneDNSSECResponseTypeDef",
    "GeoLocationDetailsTypeDef",
    "GeoLocationTypeDef",
    "GetAccountLimitResponseTypeDef",
    "GetChangeResponseTypeDef",
    "GetCheckerIpRangesResponseTypeDef",
    "GetDNSSECResponseTypeDef",
    "GetGeoLocationResponseTypeDef",
    "GetHealthCheckCountResponseTypeDef",
    "GetHealthCheckLastFailureReasonResponseTypeDef",
    "GetHealthCheckResponseTypeDef",
    "GetHealthCheckStatusResponseTypeDef",
    "GetHostedZoneCountResponseTypeDef",
    "GetHostedZoneLimitResponseTypeDef",
    "GetHostedZoneResponseTypeDef",
    "GetQueryLoggingConfigResponseTypeDef",
    "GetReusableDelegationSetLimitResponseTypeDef",
    "GetReusableDelegationSetResponseTypeDef",
    "GetTrafficPolicyInstanceCountResponseTypeDef",
    "GetTrafficPolicyInstanceResponseTypeDef",
    "GetTrafficPolicyResponseTypeDef",
    "HealthCheckConfigTypeDef",
    "HealthCheckObservationTypeDef",
    "HealthCheckTypeDef",
    "HostedZoneConfigTypeDef",
    "HostedZoneLimitTypeDef",
    "HostedZoneOwnerTypeDef",
    "HostedZoneSummaryTypeDef",
    "HostedZoneTypeDef",
    "KeySigningKeyTypeDef",
    "LinkedServiceTypeDef",
    "ListGeoLocationsResponseTypeDef",
    "ListHealthChecksResponseTypeDef",
    "ListHostedZonesByNameResponseTypeDef",
    "ListHostedZonesByVPCResponseTypeDef",
    "ListHostedZonesResponseTypeDef",
    "ListQueryLoggingConfigsResponseTypeDef",
    "ListResourceRecordSetsResponseTypeDef",
    "ListReusableDelegationSetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTagsForResourcesResponseTypeDef",
    "ListTrafficPoliciesResponseTypeDef",
    "ListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    "ListTrafficPolicyInstancesByPolicyResponseTypeDef",
    "ListTrafficPolicyInstancesResponseTypeDef",
    "ListTrafficPolicyVersionsResponseTypeDef",
    "ListVPCAssociationAuthorizationsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QueryLoggingConfigTypeDef",
    "ResourceRecordSetTypeDef",
    "ResourceRecordTypeDef",
    "ResourceTagSetTypeDef",
    "ReusableDelegationSetLimitTypeDef",
    "StatusReportTypeDef",
    "TagTypeDef",
    "TestDNSAnswerResponseTypeDef",
    "TrafficPolicyInstanceTypeDef",
    "TrafficPolicySummaryTypeDef",
    "TrafficPolicyTypeDef",
    "UpdateHealthCheckResponseTypeDef",
    "UpdateHostedZoneCommentResponseTypeDef",
    "UpdateTrafficPolicyCommentResponseTypeDef",
    "UpdateTrafficPolicyInstanceResponseTypeDef",
    "VPCTypeDef",
    "WaiterConfigTypeDef",
)

AccountLimitTypeDef = TypedDict(
    "AccountLimitTypeDef",
    {
        "Type": AccountLimitTypeType,
        "Value": int,
    },
)

ActivateKeySigningKeyResponseTypeDef = TypedDict(
    "ActivateKeySigningKeyResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
    },
)

AlarmIdentifierTypeDef = TypedDict(
    "AlarmIdentifierTypeDef",
    {
        "Region": CloudWatchRegionType,
        "Name": str,
    },
)

AliasTargetTypeDef = TypedDict(
    "AliasTargetTypeDef",
    {
        "HostedZoneId": str,
        "DNSName": str,
        "EvaluateTargetHealth": bool,
    },
)

AssociateVPCWithHostedZoneResponseTypeDef = TypedDict(
    "AssociateVPCWithHostedZoneResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
    },
)

_RequiredChangeBatchTypeDef = TypedDict(
    "_RequiredChangeBatchTypeDef",
    {
        "Changes": List["ChangeTypeDef"],
    },
)
_OptionalChangeBatchTypeDef = TypedDict(
    "_OptionalChangeBatchTypeDef",
    {
        "Comment": str,
    },
    total=False,
)


class ChangeBatchTypeDef(_RequiredChangeBatchTypeDef, _OptionalChangeBatchTypeDef):
    pass


_RequiredChangeInfoTypeDef = TypedDict(
    "_RequiredChangeInfoTypeDef",
    {
        "Id": str,
        "Status": ChangeStatusType,
        "SubmittedAt": datetime,
    },
)
_OptionalChangeInfoTypeDef = TypedDict(
    "_OptionalChangeInfoTypeDef",
    {
        "Comment": str,
    },
    total=False,
)


class ChangeInfoTypeDef(_RequiredChangeInfoTypeDef, _OptionalChangeInfoTypeDef):
    pass


ChangeResourceRecordSetsResponseTypeDef = TypedDict(
    "ChangeResourceRecordSetsResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
    },
)

ChangeTypeDef = TypedDict(
    "ChangeTypeDef",
    {
        "Action": ChangeActionType,
        "ResourceRecordSet": "ResourceRecordSetTypeDef",
    },
)

_RequiredCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_RequiredCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": ComparisonOperatorType,
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": StatisticType,
    },
)
_OptionalCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_OptionalCloudWatchAlarmConfigurationTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
    },
    total=False,
)


class CloudWatchAlarmConfigurationTypeDef(
    _RequiredCloudWatchAlarmConfigurationTypeDef, _OptionalCloudWatchAlarmConfigurationTypeDef
):
    pass


CreateHealthCheckResponseTypeDef = TypedDict(
    "CreateHealthCheckResponseTypeDef",
    {
        "HealthCheck": "HealthCheckTypeDef",
        "Location": str,
    },
)

_RequiredCreateHostedZoneResponseTypeDef = TypedDict(
    "_RequiredCreateHostedZoneResponseTypeDef",
    {
        "HostedZone": "HostedZoneTypeDef",
        "ChangeInfo": "ChangeInfoTypeDef",
        "DelegationSet": "DelegationSetTypeDef",
        "Location": str,
    },
)
_OptionalCreateHostedZoneResponseTypeDef = TypedDict(
    "_OptionalCreateHostedZoneResponseTypeDef",
    {
        "VPC": "VPCTypeDef",
    },
    total=False,
)


class CreateHostedZoneResponseTypeDef(
    _RequiredCreateHostedZoneResponseTypeDef, _OptionalCreateHostedZoneResponseTypeDef
):
    pass


CreateKeySigningKeyResponseTypeDef = TypedDict(
    "CreateKeySigningKeyResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "KeySigningKey": "KeySigningKeyTypeDef",
        "Location": str,
    },
)

CreateQueryLoggingConfigResponseTypeDef = TypedDict(
    "CreateQueryLoggingConfigResponseTypeDef",
    {
        "QueryLoggingConfig": "QueryLoggingConfigTypeDef",
        "Location": str,
    },
)

CreateReusableDelegationSetResponseTypeDef = TypedDict(
    "CreateReusableDelegationSetResponseTypeDef",
    {
        "DelegationSet": "DelegationSetTypeDef",
        "Location": str,
    },
)

CreateTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "CreateTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": "TrafficPolicyInstanceTypeDef",
        "Location": str,
    },
)

CreateTrafficPolicyResponseTypeDef = TypedDict(
    "CreateTrafficPolicyResponseTypeDef",
    {
        "TrafficPolicy": "TrafficPolicyTypeDef",
        "Location": str,
    },
)

CreateTrafficPolicyVersionResponseTypeDef = TypedDict(
    "CreateTrafficPolicyVersionResponseTypeDef",
    {
        "TrafficPolicy": "TrafficPolicyTypeDef",
        "Location": str,
    },
)

CreateVPCAssociationAuthorizationResponseTypeDef = TypedDict(
    "CreateVPCAssociationAuthorizationResponseTypeDef",
    {
        "HostedZoneId": str,
        "VPC": "VPCTypeDef",
    },
)

DNSSECStatusTypeDef = TypedDict(
    "DNSSECStatusTypeDef",
    {
        "ServeSignature": str,
        "StatusMessage": str,
    },
    total=False,
)

DeactivateKeySigningKeyResponseTypeDef = TypedDict(
    "DeactivateKeySigningKeyResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
    },
)

_RequiredDelegationSetTypeDef = TypedDict(
    "_RequiredDelegationSetTypeDef",
    {
        "NameServers": List[str],
    },
)
_OptionalDelegationSetTypeDef = TypedDict(
    "_OptionalDelegationSetTypeDef",
    {
        "Id": str,
        "CallerReference": str,
    },
    total=False,
)


class DelegationSetTypeDef(_RequiredDelegationSetTypeDef, _OptionalDelegationSetTypeDef):
    pass


DeleteHostedZoneResponseTypeDef = TypedDict(
    "DeleteHostedZoneResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
    },
)

DeleteKeySigningKeyResponseTypeDef = TypedDict(
    "DeleteKeySigningKeyResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
    },
)

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

DisableHostedZoneDNSSECResponseTypeDef = TypedDict(
    "DisableHostedZoneDNSSECResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
    },
)

DisassociateVPCFromHostedZoneResponseTypeDef = TypedDict(
    "DisassociateVPCFromHostedZoneResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
    },
)

EnableHostedZoneDNSSECResponseTypeDef = TypedDict(
    "EnableHostedZoneDNSSECResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
    },
)

GeoLocationDetailsTypeDef = TypedDict(
    "GeoLocationDetailsTypeDef",
    {
        "ContinentCode": str,
        "ContinentName": str,
        "CountryCode": str,
        "CountryName": str,
        "SubdivisionCode": str,
        "SubdivisionName": str,
    },
    total=False,
)

GeoLocationTypeDef = TypedDict(
    "GeoLocationTypeDef",
    {
        "ContinentCode": str,
        "CountryCode": str,
        "SubdivisionCode": str,
    },
    total=False,
)

GetAccountLimitResponseTypeDef = TypedDict(
    "GetAccountLimitResponseTypeDef",
    {
        "Limit": "AccountLimitTypeDef",
        "Count": int,
    },
)

GetChangeResponseTypeDef = TypedDict(
    "GetChangeResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
    },
)

GetCheckerIpRangesResponseTypeDef = TypedDict(
    "GetCheckerIpRangesResponseTypeDef",
    {
        "CheckerIpRanges": List[str],
    },
)

GetDNSSECResponseTypeDef = TypedDict(
    "GetDNSSECResponseTypeDef",
    {
        "Status": "DNSSECStatusTypeDef",
        "KeySigningKeys": List["KeySigningKeyTypeDef"],
    },
)

GetGeoLocationResponseTypeDef = TypedDict(
    "GetGeoLocationResponseTypeDef",
    {
        "GeoLocationDetails": "GeoLocationDetailsTypeDef",
    },
)

GetHealthCheckCountResponseTypeDef = TypedDict(
    "GetHealthCheckCountResponseTypeDef",
    {
        "HealthCheckCount": int,
    },
)

GetHealthCheckLastFailureReasonResponseTypeDef = TypedDict(
    "GetHealthCheckLastFailureReasonResponseTypeDef",
    {
        "HealthCheckObservations": List["HealthCheckObservationTypeDef"],
    },
)

GetHealthCheckResponseTypeDef = TypedDict(
    "GetHealthCheckResponseTypeDef",
    {
        "HealthCheck": "HealthCheckTypeDef",
    },
)

GetHealthCheckStatusResponseTypeDef = TypedDict(
    "GetHealthCheckStatusResponseTypeDef",
    {
        "HealthCheckObservations": List["HealthCheckObservationTypeDef"],
    },
)

GetHostedZoneCountResponseTypeDef = TypedDict(
    "GetHostedZoneCountResponseTypeDef",
    {
        "HostedZoneCount": int,
    },
)

GetHostedZoneLimitResponseTypeDef = TypedDict(
    "GetHostedZoneLimitResponseTypeDef",
    {
        "Limit": "HostedZoneLimitTypeDef",
        "Count": int,
    },
)

_RequiredGetHostedZoneResponseTypeDef = TypedDict(
    "_RequiredGetHostedZoneResponseTypeDef",
    {
        "HostedZone": "HostedZoneTypeDef",
    },
)
_OptionalGetHostedZoneResponseTypeDef = TypedDict(
    "_OptionalGetHostedZoneResponseTypeDef",
    {
        "DelegationSet": "DelegationSetTypeDef",
        "VPCs": List["VPCTypeDef"],
    },
    total=False,
)


class GetHostedZoneResponseTypeDef(
    _RequiredGetHostedZoneResponseTypeDef, _OptionalGetHostedZoneResponseTypeDef
):
    pass


GetQueryLoggingConfigResponseTypeDef = TypedDict(
    "GetQueryLoggingConfigResponseTypeDef",
    {
        "QueryLoggingConfig": "QueryLoggingConfigTypeDef",
    },
)

GetReusableDelegationSetLimitResponseTypeDef = TypedDict(
    "GetReusableDelegationSetLimitResponseTypeDef",
    {
        "Limit": "ReusableDelegationSetLimitTypeDef",
        "Count": int,
    },
)

GetReusableDelegationSetResponseTypeDef = TypedDict(
    "GetReusableDelegationSetResponseTypeDef",
    {
        "DelegationSet": "DelegationSetTypeDef",
    },
)

GetTrafficPolicyInstanceCountResponseTypeDef = TypedDict(
    "GetTrafficPolicyInstanceCountResponseTypeDef",
    {
        "TrafficPolicyInstanceCount": int,
    },
)

GetTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "GetTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": "TrafficPolicyInstanceTypeDef",
    },
)

GetTrafficPolicyResponseTypeDef = TypedDict(
    "GetTrafficPolicyResponseTypeDef",
    {
        "TrafficPolicy": "TrafficPolicyTypeDef",
    },
)

_RequiredHealthCheckConfigTypeDef = TypedDict(
    "_RequiredHealthCheckConfigTypeDef",
    {
        "Type": HealthCheckTypeType,
    },
)
_OptionalHealthCheckConfigTypeDef = TypedDict(
    "_OptionalHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[HealthCheckRegionType],
        "AlarmIdentifier": "AlarmIdentifierTypeDef",
        "InsufficientDataHealthStatus": InsufficientDataHealthStatusType,
    },
    total=False,
)


class HealthCheckConfigTypeDef(
    _RequiredHealthCheckConfigTypeDef, _OptionalHealthCheckConfigTypeDef
):
    pass


HealthCheckObservationTypeDef = TypedDict(
    "HealthCheckObservationTypeDef",
    {
        "Region": HealthCheckRegionType,
        "IPAddress": str,
        "StatusReport": "StatusReportTypeDef",
    },
    total=False,
)

_RequiredHealthCheckTypeDef = TypedDict(
    "_RequiredHealthCheckTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
        "HealthCheckVersion": int,
    },
)
_OptionalHealthCheckTypeDef = TypedDict(
    "_OptionalHealthCheckTypeDef",
    {
        "LinkedService": "LinkedServiceTypeDef",
        "CloudWatchAlarmConfiguration": "CloudWatchAlarmConfigurationTypeDef",
    },
    total=False,
)


class HealthCheckTypeDef(_RequiredHealthCheckTypeDef, _OptionalHealthCheckTypeDef):
    pass


HostedZoneConfigTypeDef = TypedDict(
    "HostedZoneConfigTypeDef",
    {
        "Comment": str,
        "PrivateZone": bool,
    },
    total=False,
)

HostedZoneLimitTypeDef = TypedDict(
    "HostedZoneLimitTypeDef",
    {
        "Type": HostedZoneLimitTypeType,
        "Value": int,
    },
)

HostedZoneOwnerTypeDef = TypedDict(
    "HostedZoneOwnerTypeDef",
    {
        "OwningAccount": str,
        "OwningService": str,
    },
    total=False,
)

HostedZoneSummaryTypeDef = TypedDict(
    "HostedZoneSummaryTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
        "Owner": "HostedZoneOwnerTypeDef",
    },
)

_RequiredHostedZoneTypeDef = TypedDict(
    "_RequiredHostedZoneTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
    },
)
_OptionalHostedZoneTypeDef = TypedDict(
    "_OptionalHostedZoneTypeDef",
    {
        "Config": "HostedZoneConfigTypeDef",
        "ResourceRecordSetCount": int,
        "LinkedService": "LinkedServiceTypeDef",
    },
    total=False,
)


class HostedZoneTypeDef(_RequiredHostedZoneTypeDef, _OptionalHostedZoneTypeDef):
    pass


KeySigningKeyTypeDef = TypedDict(
    "KeySigningKeyTypeDef",
    {
        "Name": str,
        "KmsArn": str,
        "Flag": int,
        "SigningAlgorithmMnemonic": str,
        "SigningAlgorithmType": int,
        "DigestAlgorithmMnemonic": str,
        "DigestAlgorithmType": int,
        "KeyTag": int,
        "DigestValue": str,
        "PublicKey": str,
        "DSRecord": str,
        "DNSKEYRecord": str,
        "Status": str,
        "StatusMessage": str,
        "CreatedDate": datetime,
        "LastModifiedDate": datetime,
    },
    total=False,
)

LinkedServiceTypeDef = TypedDict(
    "LinkedServiceTypeDef",
    {
        "ServicePrincipal": str,
        "Description": str,
    },
    total=False,
)

_RequiredListGeoLocationsResponseTypeDef = TypedDict(
    "_RequiredListGeoLocationsResponseTypeDef",
    {
        "GeoLocationDetailsList": List["GeoLocationDetailsTypeDef"],
        "IsTruncated": bool,
        "MaxItems": str,
    },
)
_OptionalListGeoLocationsResponseTypeDef = TypedDict(
    "_OptionalListGeoLocationsResponseTypeDef",
    {
        "NextContinentCode": str,
        "NextCountryCode": str,
        "NextSubdivisionCode": str,
    },
    total=False,
)


class ListGeoLocationsResponseTypeDef(
    _RequiredListGeoLocationsResponseTypeDef, _OptionalListGeoLocationsResponseTypeDef
):
    pass


_RequiredListHealthChecksResponseTypeDef = TypedDict(
    "_RequiredListHealthChecksResponseTypeDef",
    {
        "HealthChecks": List["HealthCheckTypeDef"],
        "Marker": str,
        "IsTruncated": bool,
        "MaxItems": str,
    },
)
_OptionalListHealthChecksResponseTypeDef = TypedDict(
    "_OptionalListHealthChecksResponseTypeDef",
    {
        "NextMarker": str,
    },
    total=False,
)


class ListHealthChecksResponseTypeDef(
    _RequiredListHealthChecksResponseTypeDef, _OptionalListHealthChecksResponseTypeDef
):
    pass


_RequiredListHostedZonesByNameResponseTypeDef = TypedDict(
    "_RequiredListHostedZonesByNameResponseTypeDef",
    {
        "HostedZones": List["HostedZoneTypeDef"],
        "IsTruncated": bool,
        "MaxItems": str,
    },
)
_OptionalListHostedZonesByNameResponseTypeDef = TypedDict(
    "_OptionalListHostedZonesByNameResponseTypeDef",
    {
        "DNSName": str,
        "HostedZoneId": str,
        "NextDNSName": str,
        "NextHostedZoneId": str,
    },
    total=False,
)


class ListHostedZonesByNameResponseTypeDef(
    _RequiredListHostedZonesByNameResponseTypeDef, _OptionalListHostedZonesByNameResponseTypeDef
):
    pass


_RequiredListHostedZonesByVPCResponseTypeDef = TypedDict(
    "_RequiredListHostedZonesByVPCResponseTypeDef",
    {
        "HostedZoneSummaries": List["HostedZoneSummaryTypeDef"],
        "MaxItems": str,
    },
)
_OptionalListHostedZonesByVPCResponseTypeDef = TypedDict(
    "_OptionalListHostedZonesByVPCResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListHostedZonesByVPCResponseTypeDef(
    _RequiredListHostedZonesByVPCResponseTypeDef, _OptionalListHostedZonesByVPCResponseTypeDef
):
    pass


_RequiredListHostedZonesResponseTypeDef = TypedDict(
    "_RequiredListHostedZonesResponseTypeDef",
    {
        "HostedZones": List["HostedZoneTypeDef"],
        "Marker": str,
        "IsTruncated": bool,
        "MaxItems": str,
    },
)
_OptionalListHostedZonesResponseTypeDef = TypedDict(
    "_OptionalListHostedZonesResponseTypeDef",
    {
        "NextMarker": str,
    },
    total=False,
)


class ListHostedZonesResponseTypeDef(
    _RequiredListHostedZonesResponseTypeDef, _OptionalListHostedZonesResponseTypeDef
):
    pass


_RequiredListQueryLoggingConfigsResponseTypeDef = TypedDict(
    "_RequiredListQueryLoggingConfigsResponseTypeDef",
    {
        "QueryLoggingConfigs": List["QueryLoggingConfigTypeDef"],
    },
)
_OptionalListQueryLoggingConfigsResponseTypeDef = TypedDict(
    "_OptionalListQueryLoggingConfigsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListQueryLoggingConfigsResponseTypeDef(
    _RequiredListQueryLoggingConfigsResponseTypeDef, _OptionalListQueryLoggingConfigsResponseTypeDef
):
    pass


_RequiredListResourceRecordSetsResponseTypeDef = TypedDict(
    "_RequiredListResourceRecordSetsResponseTypeDef",
    {
        "ResourceRecordSets": List["ResourceRecordSetTypeDef"],
        "IsTruncated": bool,
        "MaxItems": str,
    },
)
_OptionalListResourceRecordSetsResponseTypeDef = TypedDict(
    "_OptionalListResourceRecordSetsResponseTypeDef",
    {
        "NextRecordName": str,
        "NextRecordType": RRTypeType,
        "NextRecordIdentifier": str,
    },
    total=False,
)


class ListResourceRecordSetsResponseTypeDef(
    _RequiredListResourceRecordSetsResponseTypeDef, _OptionalListResourceRecordSetsResponseTypeDef
):
    pass


_RequiredListReusableDelegationSetsResponseTypeDef = TypedDict(
    "_RequiredListReusableDelegationSetsResponseTypeDef",
    {
        "DelegationSets": List["DelegationSetTypeDef"],
        "Marker": str,
        "IsTruncated": bool,
        "MaxItems": str,
    },
)
_OptionalListReusableDelegationSetsResponseTypeDef = TypedDict(
    "_OptionalListReusableDelegationSetsResponseTypeDef",
    {
        "NextMarker": str,
    },
    total=False,
)


class ListReusableDelegationSetsResponseTypeDef(
    _RequiredListReusableDelegationSetsResponseTypeDef,
    _OptionalListReusableDelegationSetsResponseTypeDef,
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "ResourceTagSet": "ResourceTagSetTypeDef",
    },
)

ListTagsForResourcesResponseTypeDef = TypedDict(
    "ListTagsForResourcesResponseTypeDef",
    {
        "ResourceTagSets": List["ResourceTagSetTypeDef"],
    },
)

ListTrafficPoliciesResponseTypeDef = TypedDict(
    "ListTrafficPoliciesResponseTypeDef",
    {
        "TrafficPolicySummaries": List["TrafficPolicySummaryTypeDef"],
        "IsTruncated": bool,
        "TrafficPolicyIdMarker": str,
        "MaxItems": str,
    },
)

_RequiredListTrafficPolicyInstancesByHostedZoneResponseTypeDef = TypedDict(
    "_RequiredListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    {
        "TrafficPolicyInstances": List["TrafficPolicyInstanceTypeDef"],
        "IsTruncated": bool,
        "MaxItems": str,
    },
)
_OptionalListTrafficPolicyInstancesByHostedZoneResponseTypeDef = TypedDict(
    "_OptionalListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    {
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
    },
    total=False,
)


class ListTrafficPolicyInstancesByHostedZoneResponseTypeDef(
    _RequiredListTrafficPolicyInstancesByHostedZoneResponseTypeDef,
    _OptionalListTrafficPolicyInstancesByHostedZoneResponseTypeDef,
):
    pass


_RequiredListTrafficPolicyInstancesByPolicyResponseTypeDef = TypedDict(
    "_RequiredListTrafficPolicyInstancesByPolicyResponseTypeDef",
    {
        "TrafficPolicyInstances": List["TrafficPolicyInstanceTypeDef"],
        "IsTruncated": bool,
        "MaxItems": str,
    },
)
_OptionalListTrafficPolicyInstancesByPolicyResponseTypeDef = TypedDict(
    "_OptionalListTrafficPolicyInstancesByPolicyResponseTypeDef",
    {
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
    },
    total=False,
)


class ListTrafficPolicyInstancesByPolicyResponseTypeDef(
    _RequiredListTrafficPolicyInstancesByPolicyResponseTypeDef,
    _OptionalListTrafficPolicyInstancesByPolicyResponseTypeDef,
):
    pass


_RequiredListTrafficPolicyInstancesResponseTypeDef = TypedDict(
    "_RequiredListTrafficPolicyInstancesResponseTypeDef",
    {
        "TrafficPolicyInstances": List["TrafficPolicyInstanceTypeDef"],
        "IsTruncated": bool,
        "MaxItems": str,
    },
)
_OptionalListTrafficPolicyInstancesResponseTypeDef = TypedDict(
    "_OptionalListTrafficPolicyInstancesResponseTypeDef",
    {
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
    },
    total=False,
)


class ListTrafficPolicyInstancesResponseTypeDef(
    _RequiredListTrafficPolicyInstancesResponseTypeDef,
    _OptionalListTrafficPolicyInstancesResponseTypeDef,
):
    pass


ListTrafficPolicyVersionsResponseTypeDef = TypedDict(
    "ListTrafficPolicyVersionsResponseTypeDef",
    {
        "TrafficPolicies": List["TrafficPolicyTypeDef"],
        "IsTruncated": bool,
        "TrafficPolicyVersionMarker": str,
        "MaxItems": str,
    },
)

_RequiredListVPCAssociationAuthorizationsResponseTypeDef = TypedDict(
    "_RequiredListVPCAssociationAuthorizationsResponseTypeDef",
    {
        "HostedZoneId": str,
        "VPCs": List["VPCTypeDef"],
    },
)
_OptionalListVPCAssociationAuthorizationsResponseTypeDef = TypedDict(
    "_OptionalListVPCAssociationAuthorizationsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListVPCAssociationAuthorizationsResponseTypeDef(
    _RequiredListVPCAssociationAuthorizationsResponseTypeDef,
    _OptionalListVPCAssociationAuthorizationsResponseTypeDef,
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

QueryLoggingConfigTypeDef = TypedDict(
    "QueryLoggingConfigTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "CloudWatchLogsLogGroupArn": str,
    },
)

_RequiredResourceRecordSetTypeDef = TypedDict(
    "_RequiredResourceRecordSetTypeDef",
    {
        "Name": str,
        "Type": RRTypeType,
    },
)
_OptionalResourceRecordSetTypeDef = TypedDict(
    "_OptionalResourceRecordSetTypeDef",
    {
        "SetIdentifier": str,
        "Weight": int,
        "Region": ResourceRecordSetRegionType,
        "GeoLocation": "GeoLocationTypeDef",
        "Failover": ResourceRecordSetFailoverType,
        "MultiValueAnswer": bool,
        "TTL": int,
        "ResourceRecords": List["ResourceRecordTypeDef"],
        "AliasTarget": "AliasTargetTypeDef",
        "HealthCheckId": str,
        "TrafficPolicyInstanceId": str,
    },
    total=False,
)


class ResourceRecordSetTypeDef(
    _RequiredResourceRecordSetTypeDef, _OptionalResourceRecordSetTypeDef
):
    pass


ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef",
    {
        "Value": str,
    },
)

ResourceTagSetTypeDef = TypedDict(
    "ResourceTagSetTypeDef",
    {
        "ResourceType": TagResourceTypeType,
        "ResourceId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ReusableDelegationSetLimitTypeDef = TypedDict(
    "ReusableDelegationSetLimitTypeDef",
    {
        "Type": Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"],
        "Value": int,
    },
)

StatusReportTypeDef = TypedDict(
    "StatusReportTypeDef",
    {
        "Status": str,
        "CheckedTime": datetime,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TestDNSAnswerResponseTypeDef = TypedDict(
    "TestDNSAnswerResponseTypeDef",
    {
        "Nameserver": str,
        "RecordName": str,
        "RecordType": RRTypeType,
        "RecordData": List[str],
        "ResponseCode": str,
        "Protocol": str,
    },
)

TrafficPolicyInstanceTypeDef = TypedDict(
    "TrafficPolicyInstanceTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": RRTypeType,
    },
)

TrafficPolicySummaryTypeDef = TypedDict(
    "TrafficPolicySummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": RRTypeType,
        "LatestVersion": int,
        "TrafficPolicyCount": int,
    },
)

_RequiredTrafficPolicyTypeDef = TypedDict(
    "_RequiredTrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": RRTypeType,
        "Document": str,
    },
)
_OptionalTrafficPolicyTypeDef = TypedDict(
    "_OptionalTrafficPolicyTypeDef",
    {
        "Comment": str,
    },
    total=False,
)


class TrafficPolicyTypeDef(_RequiredTrafficPolicyTypeDef, _OptionalTrafficPolicyTypeDef):
    pass


UpdateHealthCheckResponseTypeDef = TypedDict(
    "UpdateHealthCheckResponseTypeDef",
    {
        "HealthCheck": "HealthCheckTypeDef",
    },
)

UpdateHostedZoneCommentResponseTypeDef = TypedDict(
    "UpdateHostedZoneCommentResponseTypeDef",
    {
        "HostedZone": "HostedZoneTypeDef",
    },
)

UpdateTrafficPolicyCommentResponseTypeDef = TypedDict(
    "UpdateTrafficPolicyCommentResponseTypeDef",
    {
        "TrafficPolicy": "TrafficPolicyTypeDef",
    },
)

UpdateTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "UpdateTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": "TrafficPolicyInstanceTypeDef",
    },
)

VPCTypeDef = TypedDict(
    "VPCTypeDef",
    {
        "VPCRegion": VPCRegionType,
        "VPCId": str,
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
