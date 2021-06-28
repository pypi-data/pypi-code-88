"""
Type annotations for service-quotas service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/type_defs.html)

Usage::

    ```python
    from mypy_boto3_service_quotas.type_defs import DeleteServiceQuotaIncreaseRequestFromTemplateRequestTypeDef

    data: DeleteServiceQuotaIncreaseRequestFromTemplateRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ErrorCodeType,
    PeriodUnitType,
    RequestStatusType,
    ServiceQuotaTemplateAssociationStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeleteServiceQuotaIncreaseRequestFromTemplateRequestTypeDef",
    "ErrorReasonTypeDef",
    "GetAWSDefaultServiceQuotaRequestTypeDef",
    "GetAWSDefaultServiceQuotaResponseResponseTypeDef",
    "GetAssociationForServiceQuotaTemplateResponseResponseTypeDef",
    "GetRequestedServiceQuotaChangeRequestTypeDef",
    "GetRequestedServiceQuotaChangeResponseResponseTypeDef",
    "GetServiceQuotaIncreaseRequestFromTemplateRequestTypeDef",
    "GetServiceQuotaIncreaseRequestFromTemplateResponseResponseTypeDef",
    "GetServiceQuotaRequestTypeDef",
    "GetServiceQuotaResponseResponseTypeDef",
    "ListAWSDefaultServiceQuotasRequestTypeDef",
    "ListAWSDefaultServiceQuotasResponseResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaResponseResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryRequestTypeDef",
    "ListRequestedServiceQuotaChangeHistoryResponseResponseTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplateRequestTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplateResponseResponseTypeDef",
    "ListServiceQuotasRequestTypeDef",
    "ListServiceQuotasResponseResponseTypeDef",
    "ListServicesRequestTypeDef",
    "ListServicesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MetricInfoTypeDef",
    "PaginatorConfigTypeDef",
    "PutServiceQuotaIncreaseRequestIntoTemplateRequestTypeDef",
    "PutServiceQuotaIncreaseRequestIntoTemplateResponseResponseTypeDef",
    "QuotaPeriodTypeDef",
    "RequestServiceQuotaIncreaseRequestTypeDef",
    "RequestServiceQuotaIncreaseResponseResponseTypeDef",
    "RequestedServiceQuotaChangeTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceInfoTypeDef",
    "ServiceQuotaIncreaseRequestInTemplateTypeDef",
    "ServiceQuotaTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
)

DeleteServiceQuotaIncreaseRequestFromTemplateRequestTypeDef = TypedDict(
    "DeleteServiceQuotaIncreaseRequestFromTemplateRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
        "AwsRegion": str,
    },
)

ErrorReasonTypeDef = TypedDict(
    "ErrorReasonTypeDef",
    {
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

GetAWSDefaultServiceQuotaRequestTypeDef = TypedDict(
    "GetAWSDefaultServiceQuotaRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
    },
)

GetAWSDefaultServiceQuotaResponseResponseTypeDef = TypedDict(
    "GetAWSDefaultServiceQuotaResponseResponseTypeDef",
    {
        "Quota": "ServiceQuotaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssociationForServiceQuotaTemplateResponseResponseTypeDef = TypedDict(
    "GetAssociationForServiceQuotaTemplateResponseResponseTypeDef",
    {
        "ServiceQuotaTemplateAssociationStatus": ServiceQuotaTemplateAssociationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRequestedServiceQuotaChangeRequestTypeDef = TypedDict(
    "GetRequestedServiceQuotaChangeRequestTypeDef",
    {
        "RequestId": str,
    },
)

GetRequestedServiceQuotaChangeResponseResponseTypeDef = TypedDict(
    "GetRequestedServiceQuotaChangeResponseResponseTypeDef",
    {
        "RequestedQuota": "RequestedServiceQuotaChangeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceQuotaIncreaseRequestFromTemplateRequestTypeDef = TypedDict(
    "GetServiceQuotaIncreaseRequestFromTemplateRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
        "AwsRegion": str,
    },
)

GetServiceQuotaIncreaseRequestFromTemplateResponseResponseTypeDef = TypedDict(
    "GetServiceQuotaIncreaseRequestFromTemplateResponseResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplate": "ServiceQuotaIncreaseRequestInTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceQuotaRequestTypeDef = TypedDict(
    "GetServiceQuotaRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
    },
)

GetServiceQuotaResponseResponseTypeDef = TypedDict(
    "GetServiceQuotaResponseResponseTypeDef",
    {
        "Quota": "ServiceQuotaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAWSDefaultServiceQuotasRequestTypeDef = TypedDict(
    "_RequiredListAWSDefaultServiceQuotasRequestTypeDef",
    {
        "ServiceCode": str,
    },
)
_OptionalListAWSDefaultServiceQuotasRequestTypeDef = TypedDict(
    "_OptionalListAWSDefaultServiceQuotasRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAWSDefaultServiceQuotasRequestTypeDef(
    _RequiredListAWSDefaultServiceQuotasRequestTypeDef,
    _OptionalListAWSDefaultServiceQuotasRequestTypeDef,
):
    pass


ListAWSDefaultServiceQuotasResponseResponseTypeDef = TypedDict(
    "ListAWSDefaultServiceQuotasResponseResponseTypeDef",
    {
        "NextToken": str,
        "Quotas": List["ServiceQuotaTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef = TypedDict(
    "_RequiredListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
    },
)
_OptionalListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef = TypedDict(
    "_OptionalListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef",
    {
        "Status": RequestStatusType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef(
    _RequiredListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef,
    _OptionalListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef,
):
    pass


ListRequestedServiceQuotaChangeHistoryByQuotaResponseResponseTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryByQuotaResponseResponseTypeDef",
    {
        "NextToken": str,
        "RequestedQuotas": List["RequestedServiceQuotaChangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRequestedServiceQuotaChangeHistoryRequestTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryRequestTypeDef",
    {
        "ServiceCode": str,
        "Status": RequestStatusType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListRequestedServiceQuotaChangeHistoryResponseResponseTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryResponseResponseTypeDef",
    {
        "NextToken": str,
        "RequestedQuotas": List["RequestedServiceQuotaChangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceQuotaIncreaseRequestsInTemplateRequestTypeDef = TypedDict(
    "ListServiceQuotaIncreaseRequestsInTemplateRequestTypeDef",
    {
        "ServiceCode": str,
        "AwsRegion": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListServiceQuotaIncreaseRequestsInTemplateResponseResponseTypeDef = TypedDict(
    "ListServiceQuotaIncreaseRequestsInTemplateResponseResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplateList": List[
            "ServiceQuotaIncreaseRequestInTemplateTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServiceQuotasRequestTypeDef = TypedDict(
    "_RequiredListServiceQuotasRequestTypeDef",
    {
        "ServiceCode": str,
    },
)
_OptionalListServiceQuotasRequestTypeDef = TypedDict(
    "_OptionalListServiceQuotasRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListServiceQuotasRequestTypeDef(
    _RequiredListServiceQuotasRequestTypeDef, _OptionalListServiceQuotasRequestTypeDef
):
    pass


ListServiceQuotasResponseResponseTypeDef = TypedDict(
    "ListServiceQuotasResponseResponseTypeDef",
    {
        "NextToken": str,
        "Quotas": List["ServiceQuotaTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesRequestTypeDef = TypedDict(
    "ListServicesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListServicesResponseResponseTypeDef = TypedDict(
    "ListServicesResponseResponseTypeDef",
    {
        "NextToken": str,
        "Services": List["ServiceInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricInfoTypeDef = TypedDict(
    "MetricInfoTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
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

PutServiceQuotaIncreaseRequestIntoTemplateRequestTypeDef = TypedDict(
    "PutServiceQuotaIncreaseRequestIntoTemplateRequestTypeDef",
    {
        "QuotaCode": str,
        "ServiceCode": str,
        "AwsRegion": str,
        "DesiredValue": float,
    },
)

PutServiceQuotaIncreaseRequestIntoTemplateResponseResponseTypeDef = TypedDict(
    "PutServiceQuotaIncreaseRequestIntoTemplateResponseResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplate": "ServiceQuotaIncreaseRequestInTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QuotaPeriodTypeDef = TypedDict(
    "QuotaPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": PeriodUnitType,
    },
    total=False,
)

RequestServiceQuotaIncreaseRequestTypeDef = TypedDict(
    "RequestServiceQuotaIncreaseRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
        "DesiredValue": float,
    },
)

RequestServiceQuotaIncreaseResponseResponseTypeDef = TypedDict(
    "RequestServiceQuotaIncreaseResponseResponseTypeDef",
    {
        "RequestedQuota": "RequestedServiceQuotaChangeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestedServiceQuotaChangeTypeDef = TypedDict(
    "RequestedServiceQuotaChangeTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": RequestStatusType,
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
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

ServiceInfoTypeDef = TypedDict(
    "ServiceInfoTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
    },
    total=False,
)

ServiceQuotaIncreaseRequestInTemplateTypeDef = TypedDict(
    "ServiceQuotaIncreaseRequestInTemplateTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "AwsRegion": str,
        "Unit": str,
        "GlobalQuota": bool,
    },
    total=False,
)

ServiceQuotaTypeDef = TypedDict(
    "ServiceQuotaTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": "MetricInfoTypeDef",
        "Period": "QuotaPeriodTypeDef",
        "ErrorReason": "ErrorReasonTypeDef",
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)
