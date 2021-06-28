"""
Type annotations for servicediscovery service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/type_defs.html)

Usage::

    ```python
    from mypy_boto3_servicediscovery.type_defs import CreateHttpNamespaceRequestTypeDef

    data: CreateHttpNamespaceRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    CustomHealthStatusType,
    FilterConditionType,
    HealthCheckTypeType,
    HealthStatusFilterType,
    HealthStatusType,
    NamespaceTypeType,
    OperationFilterNameType,
    OperationStatusType,
    OperationTargetTypeType,
    OperationTypeType,
    RecordTypeType,
    RoutingPolicyType,
    ServiceTypeType,
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
    "CreateHttpNamespaceRequestTypeDef",
    "CreateHttpNamespaceResponseResponseTypeDef",
    "CreatePrivateDnsNamespaceRequestTypeDef",
    "CreatePrivateDnsNamespaceResponseResponseTypeDef",
    "CreatePublicDnsNamespaceRequestTypeDef",
    "CreatePublicDnsNamespaceResponseResponseTypeDef",
    "CreateServiceRequestTypeDef",
    "CreateServiceResponseResponseTypeDef",
    "DeleteNamespaceRequestTypeDef",
    "DeleteNamespaceResponseResponseTypeDef",
    "DeleteServiceRequestTypeDef",
    "DeregisterInstanceRequestTypeDef",
    "DeregisterInstanceResponseResponseTypeDef",
    "DiscoverInstancesRequestTypeDef",
    "DiscoverInstancesResponseResponseTypeDef",
    "DnsConfigChangeTypeDef",
    "DnsConfigTypeDef",
    "DnsPropertiesTypeDef",
    "DnsRecordTypeDef",
    "GetInstanceRequestTypeDef",
    "GetInstanceResponseResponseTypeDef",
    "GetInstancesHealthStatusRequestTypeDef",
    "GetInstancesHealthStatusResponseResponseTypeDef",
    "GetNamespaceRequestTypeDef",
    "GetNamespaceResponseResponseTypeDef",
    "GetOperationRequestTypeDef",
    "GetOperationResponseResponseTypeDef",
    "GetServiceRequestTypeDef",
    "GetServiceResponseResponseTypeDef",
    "HealthCheckConfigTypeDef",
    "HealthCheckCustomConfigTypeDef",
    "HttpInstanceSummaryTypeDef",
    "HttpPropertiesTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTypeDef",
    "ListInstancesRequestTypeDef",
    "ListInstancesResponseResponseTypeDef",
    "ListNamespacesRequestTypeDef",
    "ListNamespacesResponseResponseTypeDef",
    "ListOperationsRequestTypeDef",
    "ListOperationsResponseResponseTypeDef",
    "ListServicesRequestTypeDef",
    "ListServicesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "NamespaceFilterTypeDef",
    "NamespacePropertiesTypeDef",
    "NamespaceSummaryTypeDef",
    "NamespaceTypeDef",
    "OperationFilterTypeDef",
    "OperationSummaryTypeDef",
    "OperationTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterInstanceRequestTypeDef",
    "RegisterInstanceResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceChangeTypeDef",
    "ServiceFilterTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateInstanceCustomHealthStatusRequestTypeDef",
    "UpdateServiceRequestTypeDef",
    "UpdateServiceResponseResponseTypeDef",
)

_RequiredCreateHttpNamespaceRequestTypeDef = TypedDict(
    "_RequiredCreateHttpNamespaceRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateHttpNamespaceRequestTypeDef = TypedDict(
    "_OptionalCreateHttpNamespaceRequestTypeDef",
    {
        "CreatorRequestId": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateHttpNamespaceRequestTypeDef(
    _RequiredCreateHttpNamespaceRequestTypeDef, _OptionalCreateHttpNamespaceRequestTypeDef
):
    pass


CreateHttpNamespaceResponseResponseTypeDef = TypedDict(
    "CreateHttpNamespaceResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePrivateDnsNamespaceRequestTypeDef = TypedDict(
    "_RequiredCreatePrivateDnsNamespaceRequestTypeDef",
    {
        "Name": str,
        "Vpc": str,
    },
)
_OptionalCreatePrivateDnsNamespaceRequestTypeDef = TypedDict(
    "_OptionalCreatePrivateDnsNamespaceRequestTypeDef",
    {
        "CreatorRequestId": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreatePrivateDnsNamespaceRequestTypeDef(
    _RequiredCreatePrivateDnsNamespaceRequestTypeDef,
    _OptionalCreatePrivateDnsNamespaceRequestTypeDef,
):
    pass


CreatePrivateDnsNamespaceResponseResponseTypeDef = TypedDict(
    "CreatePrivateDnsNamespaceResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePublicDnsNamespaceRequestTypeDef = TypedDict(
    "_RequiredCreatePublicDnsNamespaceRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreatePublicDnsNamespaceRequestTypeDef = TypedDict(
    "_OptionalCreatePublicDnsNamespaceRequestTypeDef",
    {
        "CreatorRequestId": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreatePublicDnsNamespaceRequestTypeDef(
    _RequiredCreatePublicDnsNamespaceRequestTypeDef, _OptionalCreatePublicDnsNamespaceRequestTypeDef
):
    pass


CreatePublicDnsNamespaceResponseResponseTypeDef = TypedDict(
    "CreatePublicDnsNamespaceResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceRequestTypeDef = TypedDict(
    "_RequiredCreateServiceRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateServiceRequestTypeDef = TypedDict(
    "_OptionalCreateServiceRequestTypeDef",
    {
        "NamespaceId": str,
        "CreatorRequestId": str,
        "Description": str,
        "DnsConfig": "DnsConfigTypeDef",
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
        "HealthCheckCustomConfig": "HealthCheckCustomConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "Type": Literal["HTTP"],
    },
    total=False,
)


class CreateServiceRequestTypeDef(
    _RequiredCreateServiceRequestTypeDef, _OptionalCreateServiceRequestTypeDef
):
    pass


CreateServiceResponseResponseTypeDef = TypedDict(
    "CreateServiceResponseResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNamespaceRequestTypeDef = TypedDict(
    "DeleteNamespaceRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteNamespaceResponseResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceRequestTypeDef = TypedDict(
    "DeleteServiceRequestTypeDef",
    {
        "Id": str,
    },
)

DeregisterInstanceRequestTypeDef = TypedDict(
    "DeregisterInstanceRequestTypeDef",
    {
        "ServiceId": str,
        "InstanceId": str,
    },
)

DeregisterInstanceResponseResponseTypeDef = TypedDict(
    "DeregisterInstanceResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDiscoverInstancesRequestTypeDef = TypedDict(
    "_RequiredDiscoverInstancesRequestTypeDef",
    {
        "NamespaceName": str,
        "ServiceName": str,
    },
)
_OptionalDiscoverInstancesRequestTypeDef = TypedDict(
    "_OptionalDiscoverInstancesRequestTypeDef",
    {
        "MaxResults": int,
        "QueryParameters": Dict[str, str],
        "OptionalParameters": Dict[str, str],
        "HealthStatus": HealthStatusFilterType,
    },
    total=False,
)


class DiscoverInstancesRequestTypeDef(
    _RequiredDiscoverInstancesRequestTypeDef, _OptionalDiscoverInstancesRequestTypeDef
):
    pass


DiscoverInstancesResponseResponseTypeDef = TypedDict(
    "DiscoverInstancesResponseResponseTypeDef",
    {
        "Instances": List["HttpInstanceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DnsConfigChangeTypeDef = TypedDict(
    "DnsConfigChangeTypeDef",
    {
        "DnsRecords": List["DnsRecordTypeDef"],
    },
)

_RequiredDnsConfigTypeDef = TypedDict(
    "_RequiredDnsConfigTypeDef",
    {
        "DnsRecords": List["DnsRecordTypeDef"],
    },
)
_OptionalDnsConfigTypeDef = TypedDict(
    "_OptionalDnsConfigTypeDef",
    {
        "NamespaceId": str,
        "RoutingPolicy": RoutingPolicyType,
    },
    total=False,
)


class DnsConfigTypeDef(_RequiredDnsConfigTypeDef, _OptionalDnsConfigTypeDef):
    pass


DnsPropertiesTypeDef = TypedDict(
    "DnsPropertiesTypeDef",
    {
        "HostedZoneId": str,
    },
    total=False,
)

DnsRecordTypeDef = TypedDict(
    "DnsRecordTypeDef",
    {
        "Type": RecordTypeType,
        "TTL": int,
    },
)

GetInstanceRequestTypeDef = TypedDict(
    "GetInstanceRequestTypeDef",
    {
        "ServiceId": str,
        "InstanceId": str,
    },
)

GetInstanceResponseResponseTypeDef = TypedDict(
    "GetInstanceResponseResponseTypeDef",
    {
        "Instance": "InstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInstancesHealthStatusRequestTypeDef = TypedDict(
    "_RequiredGetInstancesHealthStatusRequestTypeDef",
    {
        "ServiceId": str,
    },
)
_OptionalGetInstancesHealthStatusRequestTypeDef = TypedDict(
    "_OptionalGetInstancesHealthStatusRequestTypeDef",
    {
        "Instances": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetInstancesHealthStatusRequestTypeDef(
    _RequiredGetInstancesHealthStatusRequestTypeDef, _OptionalGetInstancesHealthStatusRequestTypeDef
):
    pass


GetInstancesHealthStatusResponseResponseTypeDef = TypedDict(
    "GetInstancesHealthStatusResponseResponseTypeDef",
    {
        "Status": Dict[str, HealthStatusType],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNamespaceRequestTypeDef = TypedDict(
    "GetNamespaceRequestTypeDef",
    {
        "Id": str,
    },
)

GetNamespaceResponseResponseTypeDef = TypedDict(
    "GetNamespaceResponseResponseTypeDef",
    {
        "Namespace": "NamespaceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOperationRequestTypeDef = TypedDict(
    "GetOperationRequestTypeDef",
    {
        "OperationId": str,
    },
)

GetOperationResponseResponseTypeDef = TypedDict(
    "GetOperationResponseResponseTypeDef",
    {
        "Operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceRequestTypeDef = TypedDict(
    "GetServiceRequestTypeDef",
    {
        "Id": str,
    },
)

GetServiceResponseResponseTypeDef = TypedDict(
    "GetServiceResponseResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
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
        "ResourcePath": str,
        "FailureThreshold": int,
    },
    total=False,
)


class HealthCheckConfigTypeDef(
    _RequiredHealthCheckConfigTypeDef, _OptionalHealthCheckConfigTypeDef
):
    pass


HealthCheckCustomConfigTypeDef = TypedDict(
    "HealthCheckCustomConfigTypeDef",
    {
        "FailureThreshold": int,
    },
    total=False,
)

HttpInstanceSummaryTypeDef = TypedDict(
    "HttpInstanceSummaryTypeDef",
    {
        "InstanceId": str,
        "NamespaceName": str,
        "ServiceName": str,
        "HealthStatus": HealthStatusType,
        "Attributes": Dict[str, str],
    },
    total=False,
)

HttpPropertiesTypeDef = TypedDict(
    "HttpPropertiesTypeDef",
    {
        "HttpName": str,
    },
    total=False,
)

InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "Id": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

_RequiredInstanceTypeDef = TypedDict(
    "_RequiredInstanceTypeDef",
    {
        "Id": str,
    },
)
_OptionalInstanceTypeDef = TypedDict(
    "_OptionalInstanceTypeDef",
    {
        "CreatorRequestId": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class InstanceTypeDef(_RequiredInstanceTypeDef, _OptionalInstanceTypeDef):
    pass


_RequiredListInstancesRequestTypeDef = TypedDict(
    "_RequiredListInstancesRequestTypeDef",
    {
        "ServiceId": str,
    },
)
_OptionalListInstancesRequestTypeDef = TypedDict(
    "_OptionalListInstancesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListInstancesRequestTypeDef(
    _RequiredListInstancesRequestTypeDef, _OptionalListInstancesRequestTypeDef
):
    pass


ListInstancesResponseResponseTypeDef = TypedDict(
    "ListInstancesResponseResponseTypeDef",
    {
        "Instances": List["InstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNamespacesRequestTypeDef = TypedDict(
    "ListNamespacesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["NamespaceFilterTypeDef"],
    },
    total=False,
)

ListNamespacesResponseResponseTypeDef = TypedDict(
    "ListNamespacesResponseResponseTypeDef",
    {
        "Namespaces": List["NamespaceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOperationsRequestTypeDef = TypedDict(
    "ListOperationsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["OperationFilterTypeDef"],
    },
    total=False,
)

ListOperationsResponseResponseTypeDef = TypedDict(
    "ListOperationsResponseResponseTypeDef",
    {
        "Operations": List["OperationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesRequestTypeDef = TypedDict(
    "ListServicesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["ServiceFilterTypeDef"],
    },
    total=False,
)

ListServicesResponseResponseTypeDef = TypedDict(
    "ListServicesResponseResponseTypeDef",
    {
        "Services": List["ServiceSummaryTypeDef"],
        "NextToken": str,
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

_RequiredNamespaceFilterTypeDef = TypedDict(
    "_RequiredNamespaceFilterTypeDef",
    {
        "Name": Literal["TYPE"],
        "Values": List[str],
    },
)
_OptionalNamespaceFilterTypeDef = TypedDict(
    "_OptionalNamespaceFilterTypeDef",
    {
        "Condition": FilterConditionType,
    },
    total=False,
)


class NamespaceFilterTypeDef(_RequiredNamespaceFilterTypeDef, _OptionalNamespaceFilterTypeDef):
    pass


NamespacePropertiesTypeDef = TypedDict(
    "NamespacePropertiesTypeDef",
    {
        "DnsProperties": "DnsPropertiesTypeDef",
        "HttpProperties": "HttpPropertiesTypeDef",
    },
    total=False,
)

NamespaceSummaryTypeDef = TypedDict(
    "NamespaceSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": NamespaceTypeType,
        "Description": str,
        "ServiceCount": int,
        "Properties": "NamespacePropertiesTypeDef",
        "CreateDate": datetime,
    },
    total=False,
)

NamespaceTypeDef = TypedDict(
    "NamespaceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": NamespaceTypeType,
        "Description": str,
        "ServiceCount": int,
        "Properties": "NamespacePropertiesTypeDef",
        "CreateDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)

_RequiredOperationFilterTypeDef = TypedDict(
    "_RequiredOperationFilterTypeDef",
    {
        "Name": OperationFilterNameType,
        "Values": List[str],
    },
)
_OptionalOperationFilterTypeDef = TypedDict(
    "_OptionalOperationFilterTypeDef",
    {
        "Condition": FilterConditionType,
    },
    total=False,
)


class OperationFilterTypeDef(_RequiredOperationFilterTypeDef, _OptionalOperationFilterTypeDef):
    pass


OperationSummaryTypeDef = TypedDict(
    "OperationSummaryTypeDef",
    {
        "Id": str,
        "Status": OperationStatusType,
    },
    total=False,
)

OperationTypeDef = TypedDict(
    "OperationTypeDef",
    {
        "Id": str,
        "Type": OperationTypeType,
        "Status": OperationStatusType,
        "ErrorMessage": str,
        "ErrorCode": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
        "Targets": Dict[OperationTargetTypeType, str],
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

_RequiredRegisterInstanceRequestTypeDef = TypedDict(
    "_RequiredRegisterInstanceRequestTypeDef",
    {
        "ServiceId": str,
        "InstanceId": str,
        "Attributes": Dict[str, str],
    },
)
_OptionalRegisterInstanceRequestTypeDef = TypedDict(
    "_OptionalRegisterInstanceRequestTypeDef",
    {
        "CreatorRequestId": str,
    },
    total=False,
)


class RegisterInstanceRequestTypeDef(
    _RequiredRegisterInstanceRequestTypeDef, _OptionalRegisterInstanceRequestTypeDef
):
    pass


RegisterInstanceResponseResponseTypeDef = TypedDict(
    "RegisterInstanceResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

ServiceChangeTypeDef = TypedDict(
    "ServiceChangeTypeDef",
    {
        "Description": str,
        "DnsConfig": "DnsConfigChangeTypeDef",
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
    },
    total=False,
)

_RequiredServiceFilterTypeDef = TypedDict(
    "_RequiredServiceFilterTypeDef",
    {
        "Name": Literal["NAMESPACE_ID"],
        "Values": List[str],
    },
)
_OptionalServiceFilterTypeDef = TypedDict(
    "_OptionalServiceFilterTypeDef",
    {
        "Condition": FilterConditionType,
    },
    total=False,
)


class ServiceFilterTypeDef(_RequiredServiceFilterTypeDef, _OptionalServiceFilterTypeDef):
    pass


ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": ServiceTypeType,
        "Description": str,
        "InstanceCount": int,
        "DnsConfig": "DnsConfigTypeDef",
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
        "HealthCheckCustomConfig": "HealthCheckCustomConfigTypeDef",
        "CreateDate": datetime,
    },
    total=False,
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "NamespaceId": str,
        "Description": str,
        "InstanceCount": int,
        "DnsConfig": "DnsConfigTypeDef",
        "Type": ServiceTypeType,
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
        "HealthCheckCustomConfig": "HealthCheckCustomConfigTypeDef",
        "CreateDate": datetime,
        "CreatorRequestId": str,
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

UpdateInstanceCustomHealthStatusRequestTypeDef = TypedDict(
    "UpdateInstanceCustomHealthStatusRequestTypeDef",
    {
        "ServiceId": str,
        "InstanceId": str,
        "Status": CustomHealthStatusType,
    },
)

UpdateServiceRequestTypeDef = TypedDict(
    "UpdateServiceRequestTypeDef",
    {
        "Id": str,
        "Service": "ServiceChangeTypeDef",
    },
)

UpdateServiceResponseResponseTypeDef = TypedDict(
    "UpdateServiceResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
