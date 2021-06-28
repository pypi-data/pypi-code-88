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
from typing import Any, Dict, List

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
    ResettableElementNameType,
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
    "ActivateKeySigningKeyRequestTypeDef",
    "ActivateKeySigningKeyResponseResponseTypeDef",
    "AlarmIdentifierTypeDef",
    "AliasTargetTypeDef",
    "AssociateVPCWithHostedZoneRequestTypeDef",
    "AssociateVPCWithHostedZoneResponseResponseTypeDef",
    "ChangeBatchTypeDef",
    "ChangeInfoTypeDef",
    "ChangeResourceRecordSetsRequestTypeDef",
    "ChangeResourceRecordSetsResponseResponseTypeDef",
    "ChangeTagsForResourceRequestTypeDef",
    "ChangeTypeDef",
    "CloudWatchAlarmConfigurationTypeDef",
    "CreateHealthCheckRequestTypeDef",
    "CreateHealthCheckResponseResponseTypeDef",
    "CreateHostedZoneRequestTypeDef",
    "CreateHostedZoneResponseResponseTypeDef",
    "CreateKeySigningKeyRequestTypeDef",
    "CreateKeySigningKeyResponseResponseTypeDef",
    "CreateQueryLoggingConfigRequestTypeDef",
    "CreateQueryLoggingConfigResponseResponseTypeDef",
    "CreateReusableDelegationSetRequestTypeDef",
    "CreateReusableDelegationSetResponseResponseTypeDef",
    "CreateTrafficPolicyInstanceRequestTypeDef",
    "CreateTrafficPolicyInstanceResponseResponseTypeDef",
    "CreateTrafficPolicyRequestTypeDef",
    "CreateTrafficPolicyResponseResponseTypeDef",
    "CreateTrafficPolicyVersionRequestTypeDef",
    "CreateTrafficPolicyVersionResponseResponseTypeDef",
    "CreateVPCAssociationAuthorizationRequestTypeDef",
    "CreateVPCAssociationAuthorizationResponseResponseTypeDef",
    "DNSSECStatusTypeDef",
    "DeactivateKeySigningKeyRequestTypeDef",
    "DeactivateKeySigningKeyResponseResponseTypeDef",
    "DelegationSetTypeDef",
    "DeleteHealthCheckRequestTypeDef",
    "DeleteHostedZoneRequestTypeDef",
    "DeleteHostedZoneResponseResponseTypeDef",
    "DeleteKeySigningKeyRequestTypeDef",
    "DeleteKeySigningKeyResponseResponseTypeDef",
    "DeleteQueryLoggingConfigRequestTypeDef",
    "DeleteReusableDelegationSetRequestTypeDef",
    "DeleteTrafficPolicyInstanceRequestTypeDef",
    "DeleteTrafficPolicyRequestTypeDef",
    "DeleteVPCAssociationAuthorizationRequestTypeDef",
    "DimensionTypeDef",
    "DisableHostedZoneDNSSECRequestTypeDef",
    "DisableHostedZoneDNSSECResponseResponseTypeDef",
    "DisassociateVPCFromHostedZoneRequestTypeDef",
    "DisassociateVPCFromHostedZoneResponseResponseTypeDef",
    "EnableHostedZoneDNSSECRequestTypeDef",
    "EnableHostedZoneDNSSECResponseResponseTypeDef",
    "GeoLocationDetailsTypeDef",
    "GeoLocationTypeDef",
    "GetAccountLimitRequestTypeDef",
    "GetAccountLimitResponseResponseTypeDef",
    "GetChangeRequestTypeDef",
    "GetChangeResponseResponseTypeDef",
    "GetCheckerIpRangesResponseResponseTypeDef",
    "GetDNSSECRequestTypeDef",
    "GetDNSSECResponseResponseTypeDef",
    "GetGeoLocationRequestTypeDef",
    "GetGeoLocationResponseResponseTypeDef",
    "GetHealthCheckCountResponseResponseTypeDef",
    "GetHealthCheckLastFailureReasonRequestTypeDef",
    "GetHealthCheckLastFailureReasonResponseResponseTypeDef",
    "GetHealthCheckRequestTypeDef",
    "GetHealthCheckResponseResponseTypeDef",
    "GetHealthCheckStatusRequestTypeDef",
    "GetHealthCheckStatusResponseResponseTypeDef",
    "GetHostedZoneCountResponseResponseTypeDef",
    "GetHostedZoneLimitRequestTypeDef",
    "GetHostedZoneLimitResponseResponseTypeDef",
    "GetHostedZoneRequestTypeDef",
    "GetHostedZoneResponseResponseTypeDef",
    "GetQueryLoggingConfigRequestTypeDef",
    "GetQueryLoggingConfigResponseResponseTypeDef",
    "GetReusableDelegationSetLimitRequestTypeDef",
    "GetReusableDelegationSetLimitResponseResponseTypeDef",
    "GetReusableDelegationSetRequestTypeDef",
    "GetReusableDelegationSetResponseResponseTypeDef",
    "GetTrafficPolicyInstanceCountResponseResponseTypeDef",
    "GetTrafficPolicyInstanceRequestTypeDef",
    "GetTrafficPolicyInstanceResponseResponseTypeDef",
    "GetTrafficPolicyRequestTypeDef",
    "GetTrafficPolicyResponseResponseTypeDef",
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
    "ListGeoLocationsRequestTypeDef",
    "ListGeoLocationsResponseResponseTypeDef",
    "ListHealthChecksRequestTypeDef",
    "ListHealthChecksResponseResponseTypeDef",
    "ListHostedZonesByNameRequestTypeDef",
    "ListHostedZonesByNameResponseResponseTypeDef",
    "ListHostedZonesByVPCRequestTypeDef",
    "ListHostedZonesByVPCResponseResponseTypeDef",
    "ListHostedZonesRequestTypeDef",
    "ListHostedZonesResponseResponseTypeDef",
    "ListQueryLoggingConfigsRequestTypeDef",
    "ListQueryLoggingConfigsResponseResponseTypeDef",
    "ListResourceRecordSetsRequestTypeDef",
    "ListResourceRecordSetsResponseResponseTypeDef",
    "ListReusableDelegationSetsRequestTypeDef",
    "ListReusableDelegationSetsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTagsForResourcesRequestTypeDef",
    "ListTagsForResourcesResponseResponseTypeDef",
    "ListTrafficPoliciesRequestTypeDef",
    "ListTrafficPoliciesResponseResponseTypeDef",
    "ListTrafficPolicyInstancesByHostedZoneRequestTypeDef",
    "ListTrafficPolicyInstancesByHostedZoneResponseResponseTypeDef",
    "ListTrafficPolicyInstancesByPolicyRequestTypeDef",
    "ListTrafficPolicyInstancesByPolicyResponseResponseTypeDef",
    "ListTrafficPolicyInstancesRequestTypeDef",
    "ListTrafficPolicyInstancesResponseResponseTypeDef",
    "ListTrafficPolicyVersionsRequestTypeDef",
    "ListTrafficPolicyVersionsResponseResponseTypeDef",
    "ListVPCAssociationAuthorizationsRequestTypeDef",
    "ListVPCAssociationAuthorizationsResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QueryLoggingConfigTypeDef",
    "ResourceRecordSetTypeDef",
    "ResourceRecordTypeDef",
    "ResourceTagSetTypeDef",
    "ResponseMetadataTypeDef",
    "ReusableDelegationSetLimitTypeDef",
    "StatusReportTypeDef",
    "TagTypeDef",
    "TestDNSAnswerRequestTypeDef",
    "TestDNSAnswerResponseResponseTypeDef",
    "TrafficPolicyInstanceTypeDef",
    "TrafficPolicySummaryTypeDef",
    "TrafficPolicyTypeDef",
    "UpdateHealthCheckRequestTypeDef",
    "UpdateHealthCheckResponseResponseTypeDef",
    "UpdateHostedZoneCommentRequestTypeDef",
    "UpdateHostedZoneCommentResponseResponseTypeDef",
    "UpdateTrafficPolicyCommentRequestTypeDef",
    "UpdateTrafficPolicyCommentResponseResponseTypeDef",
    "UpdateTrafficPolicyInstanceRequestTypeDef",
    "UpdateTrafficPolicyInstanceResponseResponseTypeDef",
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

ActivateKeySigningKeyRequestTypeDef = TypedDict(
    "ActivateKeySigningKeyRequestTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
    },
)

ActivateKeySigningKeyResponseResponseTypeDef = TypedDict(
    "ActivateKeySigningKeyResponseResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredAssociateVPCWithHostedZoneRequestTypeDef = TypedDict(
    "_RequiredAssociateVPCWithHostedZoneRequestTypeDef",
    {
        "HostedZoneId": str,
        "VPC": "VPCTypeDef",
    },
)
_OptionalAssociateVPCWithHostedZoneRequestTypeDef = TypedDict(
    "_OptionalAssociateVPCWithHostedZoneRequestTypeDef",
    {
        "Comment": str,
    },
    total=False,
)


class AssociateVPCWithHostedZoneRequestTypeDef(
    _RequiredAssociateVPCWithHostedZoneRequestTypeDef,
    _OptionalAssociateVPCWithHostedZoneRequestTypeDef,
):
    pass


AssociateVPCWithHostedZoneResponseResponseTypeDef = TypedDict(
    "AssociateVPCWithHostedZoneResponseResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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


ChangeResourceRecordSetsRequestTypeDef = TypedDict(
    "ChangeResourceRecordSetsRequestTypeDef",
    {
        "HostedZoneId": str,
        "ChangeBatch": "ChangeBatchTypeDef",
    },
)

ChangeResourceRecordSetsResponseResponseTypeDef = TypedDict(
    "ChangeResourceRecordSetsResponseResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredChangeTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredChangeTagsForResourceRequestTypeDef",
    {
        "ResourceType": TagResourceTypeType,
        "ResourceId": str,
    },
)
_OptionalChangeTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalChangeTagsForResourceRequestTypeDef",
    {
        "AddTags": List["TagTypeDef"],
        "RemoveTagKeys": List[str],
    },
    total=False,
)


class ChangeTagsForResourceRequestTypeDef(
    _RequiredChangeTagsForResourceRequestTypeDef, _OptionalChangeTagsForResourceRequestTypeDef
):
    pass


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


CreateHealthCheckRequestTypeDef = TypedDict(
    "CreateHealthCheckRequestTypeDef",
    {
        "CallerReference": str,
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
    },
)

CreateHealthCheckResponseResponseTypeDef = TypedDict(
    "CreateHealthCheckResponseResponseTypeDef",
    {
        "HealthCheck": "HealthCheckTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHostedZoneRequestTypeDef = TypedDict(
    "_RequiredCreateHostedZoneRequestTypeDef",
    {
        "Name": str,
        "CallerReference": str,
    },
)
_OptionalCreateHostedZoneRequestTypeDef = TypedDict(
    "_OptionalCreateHostedZoneRequestTypeDef",
    {
        "VPC": "VPCTypeDef",
        "HostedZoneConfig": "HostedZoneConfigTypeDef",
        "DelegationSetId": str,
    },
    total=False,
)


class CreateHostedZoneRequestTypeDef(
    _RequiredCreateHostedZoneRequestTypeDef, _OptionalCreateHostedZoneRequestTypeDef
):
    pass


CreateHostedZoneResponseResponseTypeDef = TypedDict(
    "CreateHostedZoneResponseResponseTypeDef",
    {
        "HostedZone": "HostedZoneTypeDef",
        "ChangeInfo": "ChangeInfoTypeDef",
        "DelegationSet": "DelegationSetTypeDef",
        "VPC": "VPCTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKeySigningKeyRequestTypeDef = TypedDict(
    "CreateKeySigningKeyRequestTypeDef",
    {
        "CallerReference": str,
        "HostedZoneId": str,
        "KeyManagementServiceArn": str,
        "Name": str,
        "Status": str,
    },
)

CreateKeySigningKeyResponseResponseTypeDef = TypedDict(
    "CreateKeySigningKeyResponseResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "KeySigningKey": "KeySigningKeyTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateQueryLoggingConfigRequestTypeDef = TypedDict(
    "CreateQueryLoggingConfigRequestTypeDef",
    {
        "HostedZoneId": str,
        "CloudWatchLogsLogGroupArn": str,
    },
)

CreateQueryLoggingConfigResponseResponseTypeDef = TypedDict(
    "CreateQueryLoggingConfigResponseResponseTypeDef",
    {
        "QueryLoggingConfig": "QueryLoggingConfigTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReusableDelegationSetRequestTypeDef = TypedDict(
    "_RequiredCreateReusableDelegationSetRequestTypeDef",
    {
        "CallerReference": str,
    },
)
_OptionalCreateReusableDelegationSetRequestTypeDef = TypedDict(
    "_OptionalCreateReusableDelegationSetRequestTypeDef",
    {
        "HostedZoneId": str,
    },
    total=False,
)


class CreateReusableDelegationSetRequestTypeDef(
    _RequiredCreateReusableDelegationSetRequestTypeDef,
    _OptionalCreateReusableDelegationSetRequestTypeDef,
):
    pass


CreateReusableDelegationSetResponseResponseTypeDef = TypedDict(
    "CreateReusableDelegationSetResponseResponseTypeDef",
    {
        "DelegationSet": "DelegationSetTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrafficPolicyInstanceRequestTypeDef = TypedDict(
    "CreateTrafficPolicyInstanceRequestTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
    },
)

CreateTrafficPolicyInstanceResponseResponseTypeDef = TypedDict(
    "CreateTrafficPolicyInstanceResponseResponseTypeDef",
    {
        "TrafficPolicyInstance": "TrafficPolicyInstanceTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrafficPolicyRequestTypeDef = TypedDict(
    "_RequiredCreateTrafficPolicyRequestTypeDef",
    {
        "Name": str,
        "Document": str,
    },
)
_OptionalCreateTrafficPolicyRequestTypeDef = TypedDict(
    "_OptionalCreateTrafficPolicyRequestTypeDef",
    {
        "Comment": str,
    },
    total=False,
)


class CreateTrafficPolicyRequestTypeDef(
    _RequiredCreateTrafficPolicyRequestTypeDef, _OptionalCreateTrafficPolicyRequestTypeDef
):
    pass


CreateTrafficPolicyResponseResponseTypeDef = TypedDict(
    "CreateTrafficPolicyResponseResponseTypeDef",
    {
        "TrafficPolicy": "TrafficPolicyTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrafficPolicyVersionRequestTypeDef = TypedDict(
    "_RequiredCreateTrafficPolicyVersionRequestTypeDef",
    {
        "Id": str,
        "Document": str,
    },
)
_OptionalCreateTrafficPolicyVersionRequestTypeDef = TypedDict(
    "_OptionalCreateTrafficPolicyVersionRequestTypeDef",
    {
        "Comment": str,
    },
    total=False,
)


class CreateTrafficPolicyVersionRequestTypeDef(
    _RequiredCreateTrafficPolicyVersionRequestTypeDef,
    _OptionalCreateTrafficPolicyVersionRequestTypeDef,
):
    pass


CreateTrafficPolicyVersionResponseResponseTypeDef = TypedDict(
    "CreateTrafficPolicyVersionResponseResponseTypeDef",
    {
        "TrafficPolicy": "TrafficPolicyTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVPCAssociationAuthorizationRequestTypeDef = TypedDict(
    "CreateVPCAssociationAuthorizationRequestTypeDef",
    {
        "HostedZoneId": str,
        "VPC": "VPCTypeDef",
    },
)

CreateVPCAssociationAuthorizationResponseResponseTypeDef = TypedDict(
    "CreateVPCAssociationAuthorizationResponseResponseTypeDef",
    {
        "HostedZoneId": str,
        "VPC": "VPCTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

DeactivateKeySigningKeyRequestTypeDef = TypedDict(
    "DeactivateKeySigningKeyRequestTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
    },
)

DeactivateKeySigningKeyResponseResponseTypeDef = TypedDict(
    "DeactivateKeySigningKeyResponseResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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


DeleteHealthCheckRequestTypeDef = TypedDict(
    "DeleteHealthCheckRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)

DeleteHostedZoneRequestTypeDef = TypedDict(
    "DeleteHostedZoneRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteHostedZoneResponseResponseTypeDef = TypedDict(
    "DeleteHostedZoneResponseResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteKeySigningKeyRequestTypeDef = TypedDict(
    "DeleteKeySigningKeyRequestTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
    },
)

DeleteKeySigningKeyResponseResponseTypeDef = TypedDict(
    "DeleteKeySigningKeyResponseResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteQueryLoggingConfigRequestTypeDef = TypedDict(
    "DeleteQueryLoggingConfigRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteReusableDelegationSetRequestTypeDef = TypedDict(
    "DeleteReusableDelegationSetRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteTrafficPolicyInstanceRequestTypeDef = TypedDict(
    "DeleteTrafficPolicyInstanceRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteTrafficPolicyRequestTypeDef = TypedDict(
    "DeleteTrafficPolicyRequestTypeDef",
    {
        "Id": str,
        "Version": int,
    },
)

DeleteVPCAssociationAuthorizationRequestTypeDef = TypedDict(
    "DeleteVPCAssociationAuthorizationRequestTypeDef",
    {
        "HostedZoneId": str,
        "VPC": "VPCTypeDef",
    },
)

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

DisableHostedZoneDNSSECRequestTypeDef = TypedDict(
    "DisableHostedZoneDNSSECRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)

DisableHostedZoneDNSSECResponseResponseTypeDef = TypedDict(
    "DisableHostedZoneDNSSECResponseResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateVPCFromHostedZoneRequestTypeDef = TypedDict(
    "_RequiredDisassociateVPCFromHostedZoneRequestTypeDef",
    {
        "HostedZoneId": str,
        "VPC": "VPCTypeDef",
    },
)
_OptionalDisassociateVPCFromHostedZoneRequestTypeDef = TypedDict(
    "_OptionalDisassociateVPCFromHostedZoneRequestTypeDef",
    {
        "Comment": str,
    },
    total=False,
)


class DisassociateVPCFromHostedZoneRequestTypeDef(
    _RequiredDisassociateVPCFromHostedZoneRequestTypeDef,
    _OptionalDisassociateVPCFromHostedZoneRequestTypeDef,
):
    pass


DisassociateVPCFromHostedZoneResponseResponseTypeDef = TypedDict(
    "DisassociateVPCFromHostedZoneResponseResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableHostedZoneDNSSECRequestTypeDef = TypedDict(
    "EnableHostedZoneDNSSECRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)

EnableHostedZoneDNSSECResponseResponseTypeDef = TypedDict(
    "EnableHostedZoneDNSSECResponseResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

GetAccountLimitRequestTypeDef = TypedDict(
    "GetAccountLimitRequestTypeDef",
    {
        "Type": AccountLimitTypeType,
    },
)

GetAccountLimitResponseResponseTypeDef = TypedDict(
    "GetAccountLimitResponseResponseTypeDef",
    {
        "Limit": "AccountLimitTypeDef",
        "Count": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChangeRequestTypeDef = TypedDict(
    "GetChangeRequestTypeDef",
    {
        "Id": str,
    },
)

GetChangeResponseResponseTypeDef = TypedDict(
    "GetChangeResponseResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCheckerIpRangesResponseResponseTypeDef = TypedDict(
    "GetCheckerIpRangesResponseResponseTypeDef",
    {
        "CheckerIpRanges": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDNSSECRequestTypeDef = TypedDict(
    "GetDNSSECRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)

GetDNSSECResponseResponseTypeDef = TypedDict(
    "GetDNSSECResponseResponseTypeDef",
    {
        "Status": "DNSSECStatusTypeDef",
        "KeySigningKeys": List["KeySigningKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGeoLocationRequestTypeDef = TypedDict(
    "GetGeoLocationRequestTypeDef",
    {
        "ContinentCode": str,
        "CountryCode": str,
        "SubdivisionCode": str,
    },
    total=False,
)

GetGeoLocationResponseResponseTypeDef = TypedDict(
    "GetGeoLocationResponseResponseTypeDef",
    {
        "GeoLocationDetails": "GeoLocationDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHealthCheckCountResponseResponseTypeDef = TypedDict(
    "GetHealthCheckCountResponseResponseTypeDef",
    {
        "HealthCheckCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHealthCheckLastFailureReasonRequestTypeDef = TypedDict(
    "GetHealthCheckLastFailureReasonRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)

GetHealthCheckLastFailureReasonResponseResponseTypeDef = TypedDict(
    "GetHealthCheckLastFailureReasonResponseResponseTypeDef",
    {
        "HealthCheckObservations": List["HealthCheckObservationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHealthCheckRequestTypeDef = TypedDict(
    "GetHealthCheckRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)

GetHealthCheckResponseResponseTypeDef = TypedDict(
    "GetHealthCheckResponseResponseTypeDef",
    {
        "HealthCheck": "HealthCheckTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHealthCheckStatusRequestTypeDef = TypedDict(
    "GetHealthCheckStatusRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)

GetHealthCheckStatusResponseResponseTypeDef = TypedDict(
    "GetHealthCheckStatusResponseResponseTypeDef",
    {
        "HealthCheckObservations": List["HealthCheckObservationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHostedZoneCountResponseResponseTypeDef = TypedDict(
    "GetHostedZoneCountResponseResponseTypeDef",
    {
        "HostedZoneCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHostedZoneLimitRequestTypeDef = TypedDict(
    "GetHostedZoneLimitRequestTypeDef",
    {
        "Type": HostedZoneLimitTypeType,
        "HostedZoneId": str,
    },
)

GetHostedZoneLimitResponseResponseTypeDef = TypedDict(
    "GetHostedZoneLimitResponseResponseTypeDef",
    {
        "Limit": "HostedZoneLimitTypeDef",
        "Count": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHostedZoneRequestTypeDef = TypedDict(
    "GetHostedZoneRequestTypeDef",
    {
        "Id": str,
    },
)

GetHostedZoneResponseResponseTypeDef = TypedDict(
    "GetHostedZoneResponseResponseTypeDef",
    {
        "HostedZone": "HostedZoneTypeDef",
        "DelegationSet": "DelegationSetTypeDef",
        "VPCs": List["VPCTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryLoggingConfigRequestTypeDef = TypedDict(
    "GetQueryLoggingConfigRequestTypeDef",
    {
        "Id": str,
    },
)

GetQueryLoggingConfigResponseResponseTypeDef = TypedDict(
    "GetQueryLoggingConfigResponseResponseTypeDef",
    {
        "QueryLoggingConfig": "QueryLoggingConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReusableDelegationSetLimitRequestTypeDef = TypedDict(
    "GetReusableDelegationSetLimitRequestTypeDef",
    {
        "Type": Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"],
        "DelegationSetId": str,
    },
)

GetReusableDelegationSetLimitResponseResponseTypeDef = TypedDict(
    "GetReusableDelegationSetLimitResponseResponseTypeDef",
    {
        "Limit": "ReusableDelegationSetLimitTypeDef",
        "Count": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReusableDelegationSetRequestTypeDef = TypedDict(
    "GetReusableDelegationSetRequestTypeDef",
    {
        "Id": str,
    },
)

GetReusableDelegationSetResponseResponseTypeDef = TypedDict(
    "GetReusableDelegationSetResponseResponseTypeDef",
    {
        "DelegationSet": "DelegationSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrafficPolicyInstanceCountResponseResponseTypeDef = TypedDict(
    "GetTrafficPolicyInstanceCountResponseResponseTypeDef",
    {
        "TrafficPolicyInstanceCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrafficPolicyInstanceRequestTypeDef = TypedDict(
    "GetTrafficPolicyInstanceRequestTypeDef",
    {
        "Id": str,
    },
)

GetTrafficPolicyInstanceResponseResponseTypeDef = TypedDict(
    "GetTrafficPolicyInstanceResponseResponseTypeDef",
    {
        "TrafficPolicyInstance": "TrafficPolicyInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrafficPolicyRequestTypeDef = TypedDict(
    "GetTrafficPolicyRequestTypeDef",
    {
        "Id": str,
        "Version": int,
    },
)

GetTrafficPolicyResponseResponseTypeDef = TypedDict(
    "GetTrafficPolicyResponseResponseTypeDef",
    {
        "TrafficPolicy": "TrafficPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

ListGeoLocationsRequestTypeDef = TypedDict(
    "ListGeoLocationsRequestTypeDef",
    {
        "StartContinentCode": str,
        "StartCountryCode": str,
        "StartSubdivisionCode": str,
        "MaxItems": str,
    },
    total=False,
)

ListGeoLocationsResponseResponseTypeDef = TypedDict(
    "ListGeoLocationsResponseResponseTypeDef",
    {
        "GeoLocationDetailsList": List["GeoLocationDetailsTypeDef"],
        "IsTruncated": bool,
        "NextContinentCode": str,
        "NextCountryCode": str,
        "NextSubdivisionCode": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHealthChecksRequestTypeDef = TypedDict(
    "ListHealthChecksRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListHealthChecksResponseResponseTypeDef = TypedDict(
    "ListHealthChecksResponseResponseTypeDef",
    {
        "HealthChecks": List["HealthCheckTypeDef"],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHostedZonesByNameRequestTypeDef = TypedDict(
    "ListHostedZonesByNameRequestTypeDef",
    {
        "DNSName": str,
        "HostedZoneId": str,
        "MaxItems": str,
    },
    total=False,
)

ListHostedZonesByNameResponseResponseTypeDef = TypedDict(
    "ListHostedZonesByNameResponseResponseTypeDef",
    {
        "HostedZones": List["HostedZoneTypeDef"],
        "DNSName": str,
        "HostedZoneId": str,
        "IsTruncated": bool,
        "NextDNSName": str,
        "NextHostedZoneId": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListHostedZonesByVPCRequestTypeDef = TypedDict(
    "_RequiredListHostedZonesByVPCRequestTypeDef",
    {
        "VPCId": str,
        "VPCRegion": VPCRegionType,
    },
)
_OptionalListHostedZonesByVPCRequestTypeDef = TypedDict(
    "_OptionalListHostedZonesByVPCRequestTypeDef",
    {
        "MaxItems": str,
        "NextToken": str,
    },
    total=False,
)


class ListHostedZonesByVPCRequestTypeDef(
    _RequiredListHostedZonesByVPCRequestTypeDef, _OptionalListHostedZonesByVPCRequestTypeDef
):
    pass


ListHostedZonesByVPCResponseResponseTypeDef = TypedDict(
    "ListHostedZonesByVPCResponseResponseTypeDef",
    {
        "HostedZoneSummaries": List["HostedZoneSummaryTypeDef"],
        "MaxItems": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHostedZonesRequestTypeDef = TypedDict(
    "ListHostedZonesRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
        "DelegationSetId": str,
    },
    total=False,
)

ListHostedZonesResponseResponseTypeDef = TypedDict(
    "ListHostedZonesResponseResponseTypeDef",
    {
        "HostedZones": List["HostedZoneTypeDef"],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueryLoggingConfigsRequestTypeDef = TypedDict(
    "ListQueryLoggingConfigsRequestTypeDef",
    {
        "HostedZoneId": str,
        "NextToken": str,
        "MaxResults": str,
    },
    total=False,
)

ListQueryLoggingConfigsResponseResponseTypeDef = TypedDict(
    "ListQueryLoggingConfigsResponseResponseTypeDef",
    {
        "QueryLoggingConfigs": List["QueryLoggingConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourceRecordSetsRequestTypeDef = TypedDict(
    "_RequiredListResourceRecordSetsRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)
_OptionalListResourceRecordSetsRequestTypeDef = TypedDict(
    "_OptionalListResourceRecordSetsRequestTypeDef",
    {
        "StartRecordName": str,
        "StartRecordType": RRTypeType,
        "StartRecordIdentifier": str,
        "MaxItems": str,
    },
    total=False,
)


class ListResourceRecordSetsRequestTypeDef(
    _RequiredListResourceRecordSetsRequestTypeDef, _OptionalListResourceRecordSetsRequestTypeDef
):
    pass


ListResourceRecordSetsResponseResponseTypeDef = TypedDict(
    "ListResourceRecordSetsResponseResponseTypeDef",
    {
        "ResourceRecordSets": List["ResourceRecordSetTypeDef"],
        "IsTruncated": bool,
        "NextRecordName": str,
        "NextRecordType": RRTypeType,
        "NextRecordIdentifier": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReusableDelegationSetsRequestTypeDef = TypedDict(
    "ListReusableDelegationSetsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListReusableDelegationSetsResponseResponseTypeDef = TypedDict(
    "ListReusableDelegationSetsResponseResponseTypeDef",
    {
        "DelegationSets": List["DelegationSetTypeDef"],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceType": TagResourceTypeType,
        "ResourceId": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "ResourceTagSet": "ResourceTagSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourcesRequestTypeDef = TypedDict(
    "ListTagsForResourcesRequestTypeDef",
    {
        "ResourceType": TagResourceTypeType,
        "ResourceIds": List[str],
    },
)

ListTagsForResourcesResponseResponseTypeDef = TypedDict(
    "ListTagsForResourcesResponseResponseTypeDef",
    {
        "ResourceTagSets": List["ResourceTagSetTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrafficPoliciesRequestTypeDef = TypedDict(
    "ListTrafficPoliciesRequestTypeDef",
    {
        "TrafficPolicyIdMarker": str,
        "MaxItems": str,
    },
    total=False,
)

ListTrafficPoliciesResponseResponseTypeDef = TypedDict(
    "ListTrafficPoliciesResponseResponseTypeDef",
    {
        "TrafficPolicySummaries": List["TrafficPolicySummaryTypeDef"],
        "IsTruncated": bool,
        "TrafficPolicyIdMarker": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTrafficPolicyInstancesByHostedZoneRequestTypeDef = TypedDict(
    "_RequiredListTrafficPolicyInstancesByHostedZoneRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)
_OptionalListTrafficPolicyInstancesByHostedZoneRequestTypeDef = TypedDict(
    "_OptionalListTrafficPolicyInstancesByHostedZoneRequestTypeDef",
    {
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "MaxItems": str,
    },
    total=False,
)


class ListTrafficPolicyInstancesByHostedZoneRequestTypeDef(
    _RequiredListTrafficPolicyInstancesByHostedZoneRequestTypeDef,
    _OptionalListTrafficPolicyInstancesByHostedZoneRequestTypeDef,
):
    pass


ListTrafficPolicyInstancesByHostedZoneResponseResponseTypeDef = TypedDict(
    "ListTrafficPolicyInstancesByHostedZoneResponseResponseTypeDef",
    {
        "TrafficPolicyInstances": List["TrafficPolicyInstanceTypeDef"],
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "IsTruncated": bool,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTrafficPolicyInstancesByPolicyRequestTypeDef = TypedDict(
    "_RequiredListTrafficPolicyInstancesByPolicyRequestTypeDef",
    {
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
    },
)
_OptionalListTrafficPolicyInstancesByPolicyRequestTypeDef = TypedDict(
    "_OptionalListTrafficPolicyInstancesByPolicyRequestTypeDef",
    {
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "MaxItems": str,
    },
    total=False,
)


class ListTrafficPolicyInstancesByPolicyRequestTypeDef(
    _RequiredListTrafficPolicyInstancesByPolicyRequestTypeDef,
    _OptionalListTrafficPolicyInstancesByPolicyRequestTypeDef,
):
    pass


ListTrafficPolicyInstancesByPolicyResponseResponseTypeDef = TypedDict(
    "ListTrafficPolicyInstancesByPolicyResponseResponseTypeDef",
    {
        "TrafficPolicyInstances": List["TrafficPolicyInstanceTypeDef"],
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "IsTruncated": bool,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrafficPolicyInstancesRequestTypeDef = TypedDict(
    "ListTrafficPolicyInstancesRequestTypeDef",
    {
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "MaxItems": str,
    },
    total=False,
)

ListTrafficPolicyInstancesResponseResponseTypeDef = TypedDict(
    "ListTrafficPolicyInstancesResponseResponseTypeDef",
    {
        "TrafficPolicyInstances": List["TrafficPolicyInstanceTypeDef"],
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "IsTruncated": bool,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTrafficPolicyVersionsRequestTypeDef = TypedDict(
    "_RequiredListTrafficPolicyVersionsRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalListTrafficPolicyVersionsRequestTypeDef = TypedDict(
    "_OptionalListTrafficPolicyVersionsRequestTypeDef",
    {
        "TrafficPolicyVersionMarker": str,
        "MaxItems": str,
    },
    total=False,
)


class ListTrafficPolicyVersionsRequestTypeDef(
    _RequiredListTrafficPolicyVersionsRequestTypeDef,
    _OptionalListTrafficPolicyVersionsRequestTypeDef,
):
    pass


ListTrafficPolicyVersionsResponseResponseTypeDef = TypedDict(
    "ListTrafficPolicyVersionsResponseResponseTypeDef",
    {
        "TrafficPolicies": List["TrafficPolicyTypeDef"],
        "IsTruncated": bool,
        "TrafficPolicyVersionMarker": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListVPCAssociationAuthorizationsRequestTypeDef = TypedDict(
    "_RequiredListVPCAssociationAuthorizationsRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)
_OptionalListVPCAssociationAuthorizationsRequestTypeDef = TypedDict(
    "_OptionalListVPCAssociationAuthorizationsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": str,
    },
    total=False,
)


class ListVPCAssociationAuthorizationsRequestTypeDef(
    _RequiredListVPCAssociationAuthorizationsRequestTypeDef,
    _OptionalListVPCAssociationAuthorizationsRequestTypeDef,
):
    pass


ListVPCAssociationAuthorizationsResponseResponseTypeDef = TypedDict(
    "ListVPCAssociationAuthorizationsResponseResponseTypeDef",
    {
        "HostedZoneId": str,
        "NextToken": str,
        "VPCs": List["VPCTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredTestDNSAnswerRequestTypeDef = TypedDict(
    "_RequiredTestDNSAnswerRequestTypeDef",
    {
        "HostedZoneId": str,
        "RecordName": str,
        "RecordType": RRTypeType,
    },
)
_OptionalTestDNSAnswerRequestTypeDef = TypedDict(
    "_OptionalTestDNSAnswerRequestTypeDef",
    {
        "ResolverIP": str,
        "EDNS0ClientSubnetIP": str,
        "EDNS0ClientSubnetMask": str,
    },
    total=False,
)


class TestDNSAnswerRequestTypeDef(
    _RequiredTestDNSAnswerRequestTypeDef, _OptionalTestDNSAnswerRequestTypeDef
):
    pass


TestDNSAnswerResponseResponseTypeDef = TypedDict(
    "TestDNSAnswerResponseResponseTypeDef",
    {
        "Nameserver": str,
        "RecordName": str,
        "RecordType": RRTypeType,
        "RecordData": List[str],
        "ResponseCode": str,
        "Protocol": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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


_RequiredUpdateHealthCheckRequestTypeDef = TypedDict(
    "_RequiredUpdateHealthCheckRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)
_OptionalUpdateHealthCheckRequestTypeDef = TypedDict(
    "_OptionalUpdateHealthCheckRequestTypeDef",
    {
        "HealthCheckVersion": int,
        "IPAddress": str,
        "Port": int,
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "FailureThreshold": int,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[HealthCheckRegionType],
        "AlarmIdentifier": "AlarmIdentifierTypeDef",
        "InsufficientDataHealthStatus": InsufficientDataHealthStatusType,
        "ResetElements": List[ResettableElementNameType],
    },
    total=False,
)


class UpdateHealthCheckRequestTypeDef(
    _RequiredUpdateHealthCheckRequestTypeDef, _OptionalUpdateHealthCheckRequestTypeDef
):
    pass


UpdateHealthCheckResponseResponseTypeDef = TypedDict(
    "UpdateHealthCheckResponseResponseTypeDef",
    {
        "HealthCheck": "HealthCheckTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateHostedZoneCommentRequestTypeDef = TypedDict(
    "_RequiredUpdateHostedZoneCommentRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateHostedZoneCommentRequestTypeDef = TypedDict(
    "_OptionalUpdateHostedZoneCommentRequestTypeDef",
    {
        "Comment": str,
    },
    total=False,
)


class UpdateHostedZoneCommentRequestTypeDef(
    _RequiredUpdateHostedZoneCommentRequestTypeDef, _OptionalUpdateHostedZoneCommentRequestTypeDef
):
    pass


UpdateHostedZoneCommentResponseResponseTypeDef = TypedDict(
    "UpdateHostedZoneCommentResponseResponseTypeDef",
    {
        "HostedZone": "HostedZoneTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTrafficPolicyCommentRequestTypeDef = TypedDict(
    "UpdateTrafficPolicyCommentRequestTypeDef",
    {
        "Id": str,
        "Version": int,
        "Comment": str,
    },
)

UpdateTrafficPolicyCommentResponseResponseTypeDef = TypedDict(
    "UpdateTrafficPolicyCommentResponseResponseTypeDef",
    {
        "TrafficPolicy": "TrafficPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTrafficPolicyInstanceRequestTypeDef = TypedDict(
    "UpdateTrafficPolicyInstanceRequestTypeDef",
    {
        "Id": str,
        "TTL": int,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
    },
)

UpdateTrafficPolicyInstanceResponseResponseTypeDef = TypedDict(
    "UpdateTrafficPolicyInstanceResponseResponseTypeDef",
    {
        "TrafficPolicyInstance": "TrafficPolicyInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
