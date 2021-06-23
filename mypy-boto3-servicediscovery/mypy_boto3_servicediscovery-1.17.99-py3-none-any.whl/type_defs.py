"""
Type annotations for servicediscovery service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/type_defs.html)

Usage::

    ```python
    from mypy_boto3_servicediscovery.type_defs import CreateHttpNamespaceResponseTypeDef

    data: CreateHttpNamespaceResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from .literals import (
    FilterConditionType,
    HealthCheckTypeType,
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
    "CreateHttpNamespaceResponseTypeDef",
    "CreatePrivateDnsNamespaceResponseTypeDef",
    "CreatePublicDnsNamespaceResponseTypeDef",
    "CreateServiceResponseTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeregisterInstanceResponseTypeDef",
    "DiscoverInstancesResponseTypeDef",
    "DnsConfigChangeTypeDef",
    "DnsConfigTypeDef",
    "DnsPropertiesTypeDef",
    "DnsRecordTypeDef",
    "GetInstanceResponseTypeDef",
    "GetInstancesHealthStatusResponseTypeDef",
    "GetNamespaceResponseTypeDef",
    "GetOperationResponseTypeDef",
    "GetServiceResponseTypeDef",
    "HealthCheckConfigTypeDef",
    "HealthCheckCustomConfigTypeDef",
    "HttpInstanceSummaryTypeDef",
    "HttpPropertiesTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTypeDef",
    "ListInstancesResponseTypeDef",
    "ListNamespacesResponseTypeDef",
    "ListOperationsResponseTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NamespaceFilterTypeDef",
    "NamespacePropertiesTypeDef",
    "NamespaceSummaryTypeDef",
    "NamespaceTypeDef",
    "OperationFilterTypeDef",
    "OperationSummaryTypeDef",
    "OperationTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterInstanceResponseTypeDef",
    "ServiceChangeTypeDef",
    "ServiceFilterTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTypeDef",
    "TagTypeDef",
    "UpdateServiceResponseTypeDef",
)

CreateHttpNamespaceResponseTypeDef = TypedDict(
    "CreateHttpNamespaceResponseTypeDef",
    {
        "OperationId": str,
    },
    total=False,
)

CreatePrivateDnsNamespaceResponseTypeDef = TypedDict(
    "CreatePrivateDnsNamespaceResponseTypeDef",
    {
        "OperationId": str,
    },
    total=False,
)

CreatePublicDnsNamespaceResponseTypeDef = TypedDict(
    "CreatePublicDnsNamespaceResponseTypeDef",
    {
        "OperationId": str,
    },
    total=False,
)

CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
    },
    total=False,
)

DeleteNamespaceResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseTypeDef",
    {
        "OperationId": str,
    },
    total=False,
)

DeregisterInstanceResponseTypeDef = TypedDict(
    "DeregisterInstanceResponseTypeDef",
    {
        "OperationId": str,
    },
    total=False,
)

DiscoverInstancesResponseTypeDef = TypedDict(
    "DiscoverInstancesResponseTypeDef",
    {
        "Instances": List["HttpInstanceSummaryTypeDef"],
    },
    total=False,
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

GetInstanceResponseTypeDef = TypedDict(
    "GetInstanceResponseTypeDef",
    {
        "Instance": "InstanceTypeDef",
    },
    total=False,
)

GetInstancesHealthStatusResponseTypeDef = TypedDict(
    "GetInstancesHealthStatusResponseTypeDef",
    {
        "Status": Dict[str, HealthStatusType],
        "NextToken": str,
    },
    total=False,
)

GetNamespaceResponseTypeDef = TypedDict(
    "GetNamespaceResponseTypeDef",
    {
        "Namespace": "NamespaceTypeDef",
    },
    total=False,
)

GetOperationResponseTypeDef = TypedDict(
    "GetOperationResponseTypeDef",
    {
        "Operation": "OperationTypeDef",
    },
    total=False,
)

GetServiceResponseTypeDef = TypedDict(
    "GetServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
    },
    total=False,
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


ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {
        "Instances": List["InstanceSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListNamespacesResponseTypeDef = TypedDict(
    "ListNamespacesResponseTypeDef",
    {
        "Namespaces": List["NamespaceSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListOperationsResponseTypeDef = TypedDict(
    "ListOperationsResponseTypeDef",
    {
        "Operations": List["OperationSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "Services": List["ServiceSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
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

RegisterInstanceResponseTypeDef = TypedDict(
    "RegisterInstanceResponseTypeDef",
    {
        "OperationId": str,
    },
    total=False,
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

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef",
    {
        "OperationId": str,
    },
    total=False,
)
