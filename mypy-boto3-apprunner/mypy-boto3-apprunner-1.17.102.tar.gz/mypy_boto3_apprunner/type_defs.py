"""
Type annotations for apprunner service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/type_defs.html)

Usage::

    ```python
    from mypy_boto3_apprunner.type_defs import AssociateCustomDomainRequestTypeDef

    data: AssociateCustomDomainRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AutoScalingConfigurationStatusType,
    CertificateValidationRecordStatusType,
    ConfigurationSourceType,
    ConnectionStatusType,
    CustomDomainAssociationStatusType,
    HealthCheckProtocolType,
    ImageRepositoryTypeType,
    OperationStatusType,
    OperationTypeType,
    RuntimeType,
    ServiceStatusType,
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
    "AssociateCustomDomainRequestTypeDef",
    "AssociateCustomDomainResponseResponseTypeDef",
    "AuthenticationConfigurationTypeDef",
    "AutoScalingConfigurationSummaryTypeDef",
    "AutoScalingConfigurationTypeDef",
    "CertificateValidationRecordTypeDef",
    "CodeConfigurationTypeDef",
    "CodeConfigurationValuesTypeDef",
    "CodeRepositoryTypeDef",
    "ConnectionSummaryTypeDef",
    "ConnectionTypeDef",
    "CreateAutoScalingConfigurationRequestTypeDef",
    "CreateAutoScalingConfigurationResponseResponseTypeDef",
    "CreateConnectionRequestTypeDef",
    "CreateConnectionResponseResponseTypeDef",
    "CreateServiceRequestTypeDef",
    "CreateServiceResponseResponseTypeDef",
    "CustomDomainTypeDef",
    "DeleteAutoScalingConfigurationRequestTypeDef",
    "DeleteAutoScalingConfigurationResponseResponseTypeDef",
    "DeleteConnectionRequestTypeDef",
    "DeleteConnectionResponseResponseTypeDef",
    "DeleteServiceRequestTypeDef",
    "DeleteServiceResponseResponseTypeDef",
    "DescribeAutoScalingConfigurationRequestTypeDef",
    "DescribeAutoScalingConfigurationResponseResponseTypeDef",
    "DescribeCustomDomainsRequestTypeDef",
    "DescribeCustomDomainsResponseResponseTypeDef",
    "DescribeServiceRequestTypeDef",
    "DescribeServiceResponseResponseTypeDef",
    "DisassociateCustomDomainRequestTypeDef",
    "DisassociateCustomDomainResponseResponseTypeDef",
    "EncryptionConfigurationTypeDef",
    "HealthCheckConfigurationTypeDef",
    "ImageConfigurationTypeDef",
    "ImageRepositoryTypeDef",
    "InstanceConfigurationTypeDef",
    "ListAutoScalingConfigurationsRequestTypeDef",
    "ListAutoScalingConfigurationsResponseResponseTypeDef",
    "ListConnectionsRequestTypeDef",
    "ListConnectionsResponseResponseTypeDef",
    "ListOperationsRequestTypeDef",
    "ListOperationsResponseResponseTypeDef",
    "ListServicesRequestTypeDef",
    "ListServicesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "OperationSummaryTypeDef",
    "PauseServiceRequestTypeDef",
    "PauseServiceResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeServiceRequestTypeDef",
    "ResumeServiceResponseResponseTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTypeDef",
    "SourceCodeVersionTypeDef",
    "SourceConfigurationTypeDef",
    "StartDeploymentRequestTypeDef",
    "StartDeploymentResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateServiceRequestTypeDef",
    "UpdateServiceResponseResponseTypeDef",
)

_RequiredAssociateCustomDomainRequestTypeDef = TypedDict(
    "_RequiredAssociateCustomDomainRequestTypeDef",
    {
        "ServiceArn": str,
        "DomainName": str,
    },
)
_OptionalAssociateCustomDomainRequestTypeDef = TypedDict(
    "_OptionalAssociateCustomDomainRequestTypeDef",
    {
        "EnableWWWSubdomain": bool,
    },
    total=False,
)


class AssociateCustomDomainRequestTypeDef(
    _RequiredAssociateCustomDomainRequestTypeDef, _OptionalAssociateCustomDomainRequestTypeDef
):
    pass


AssociateCustomDomainResponseResponseTypeDef = TypedDict(
    "AssociateCustomDomainResponseResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomain": "CustomDomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthenticationConfigurationTypeDef = TypedDict(
    "AuthenticationConfigurationTypeDef",
    {
        "ConnectionArn": str,
        "AccessRoleArn": str,
    },
    total=False,
)

AutoScalingConfigurationSummaryTypeDef = TypedDict(
    "AutoScalingConfigurationSummaryTypeDef",
    {
        "AutoScalingConfigurationArn": str,
        "AutoScalingConfigurationName": str,
        "AutoScalingConfigurationRevision": int,
    },
    total=False,
)

AutoScalingConfigurationTypeDef = TypedDict(
    "AutoScalingConfigurationTypeDef",
    {
        "AutoScalingConfigurationArn": str,
        "AutoScalingConfigurationName": str,
        "AutoScalingConfigurationRevision": int,
        "Latest": bool,
        "Status": AutoScalingConfigurationStatusType,
        "MaxConcurrency": int,
        "MinSize": int,
        "MaxSize": int,
        "CreatedAt": datetime,
        "DeletedAt": datetime,
    },
    total=False,
)

CertificateValidationRecordTypeDef = TypedDict(
    "CertificateValidationRecordTypeDef",
    {
        "Name": str,
        "Type": str,
        "Value": str,
        "Status": CertificateValidationRecordStatusType,
    },
    total=False,
)

_RequiredCodeConfigurationTypeDef = TypedDict(
    "_RequiredCodeConfigurationTypeDef",
    {
        "ConfigurationSource": ConfigurationSourceType,
    },
)
_OptionalCodeConfigurationTypeDef = TypedDict(
    "_OptionalCodeConfigurationTypeDef",
    {
        "CodeConfigurationValues": "CodeConfigurationValuesTypeDef",
    },
    total=False,
)


class CodeConfigurationTypeDef(
    _RequiredCodeConfigurationTypeDef, _OptionalCodeConfigurationTypeDef
):
    pass


_RequiredCodeConfigurationValuesTypeDef = TypedDict(
    "_RequiredCodeConfigurationValuesTypeDef",
    {
        "Runtime": RuntimeType,
    },
)
_OptionalCodeConfigurationValuesTypeDef = TypedDict(
    "_OptionalCodeConfigurationValuesTypeDef",
    {
        "BuildCommand": str,
        "StartCommand": str,
        "Port": str,
        "RuntimeEnvironmentVariables": Dict[str, str],
    },
    total=False,
)


class CodeConfigurationValuesTypeDef(
    _RequiredCodeConfigurationValuesTypeDef, _OptionalCodeConfigurationValuesTypeDef
):
    pass


_RequiredCodeRepositoryTypeDef = TypedDict(
    "_RequiredCodeRepositoryTypeDef",
    {
        "RepositoryUrl": str,
        "SourceCodeVersion": "SourceCodeVersionTypeDef",
    },
)
_OptionalCodeRepositoryTypeDef = TypedDict(
    "_OptionalCodeRepositoryTypeDef",
    {
        "CodeConfiguration": "CodeConfigurationTypeDef",
    },
    total=False,
)


class CodeRepositoryTypeDef(_RequiredCodeRepositoryTypeDef, _OptionalCodeRepositoryTypeDef):
    pass


ConnectionSummaryTypeDef = TypedDict(
    "ConnectionSummaryTypeDef",
    {
        "ConnectionName": str,
        "ConnectionArn": str,
        "ProviderType": Literal["GITHUB"],
        "Status": ConnectionStatusType,
        "CreatedAt": datetime,
    },
    total=False,
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionName": str,
        "ConnectionArn": str,
        "ProviderType": Literal["GITHUB"],
        "Status": ConnectionStatusType,
        "CreatedAt": datetime,
    },
    total=False,
)

_RequiredCreateAutoScalingConfigurationRequestTypeDef = TypedDict(
    "_RequiredCreateAutoScalingConfigurationRequestTypeDef",
    {
        "AutoScalingConfigurationName": str,
    },
)
_OptionalCreateAutoScalingConfigurationRequestTypeDef = TypedDict(
    "_OptionalCreateAutoScalingConfigurationRequestTypeDef",
    {
        "MaxConcurrency": int,
        "MinSize": int,
        "MaxSize": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateAutoScalingConfigurationRequestTypeDef(
    _RequiredCreateAutoScalingConfigurationRequestTypeDef,
    _OptionalCreateAutoScalingConfigurationRequestTypeDef,
):
    pass


CreateAutoScalingConfigurationResponseResponseTypeDef = TypedDict(
    "CreateAutoScalingConfigurationResponseResponseTypeDef",
    {
        "AutoScalingConfiguration": "AutoScalingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConnectionRequestTypeDef = TypedDict(
    "_RequiredCreateConnectionRequestTypeDef",
    {
        "ConnectionName": str,
        "ProviderType": Literal["GITHUB"],
    },
)
_OptionalCreateConnectionRequestTypeDef = TypedDict(
    "_OptionalCreateConnectionRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateConnectionRequestTypeDef(
    _RequiredCreateConnectionRequestTypeDef, _OptionalCreateConnectionRequestTypeDef
):
    pass


CreateConnectionResponseResponseTypeDef = TypedDict(
    "CreateConnectionResponseResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceRequestTypeDef = TypedDict(
    "_RequiredCreateServiceRequestTypeDef",
    {
        "ServiceName": str,
        "SourceConfiguration": "SourceConfigurationTypeDef",
    },
)
_OptionalCreateServiceRequestTypeDef = TypedDict(
    "_OptionalCreateServiceRequestTypeDef",
    {
        "InstanceConfiguration": "InstanceConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "HealthCheckConfiguration": "HealthCheckConfigurationTypeDef",
        "AutoScalingConfigurationArn": str,
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
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomDomainTypeDef = TypedDict(
    "_RequiredCustomDomainTypeDef",
    {
        "DomainName": str,
        "EnableWWWSubdomain": bool,
        "Status": CustomDomainAssociationStatusType,
    },
)
_OptionalCustomDomainTypeDef = TypedDict(
    "_OptionalCustomDomainTypeDef",
    {
        "CertificateValidationRecords": List["CertificateValidationRecordTypeDef"],
    },
    total=False,
)


class CustomDomainTypeDef(_RequiredCustomDomainTypeDef, _OptionalCustomDomainTypeDef):
    pass


DeleteAutoScalingConfigurationRequestTypeDef = TypedDict(
    "DeleteAutoScalingConfigurationRequestTypeDef",
    {
        "AutoScalingConfigurationArn": str,
    },
)

DeleteAutoScalingConfigurationResponseResponseTypeDef = TypedDict(
    "DeleteAutoScalingConfigurationResponseResponseTypeDef",
    {
        "AutoScalingConfiguration": "AutoScalingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectionRequestTypeDef = TypedDict(
    "DeleteConnectionRequestTypeDef",
    {
        "ConnectionArn": str,
    },
)

DeleteConnectionResponseResponseTypeDef = TypedDict(
    "DeleteConnectionResponseResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceRequestTypeDef = TypedDict(
    "DeleteServiceRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

DeleteServiceResponseResponseTypeDef = TypedDict(
    "DeleteServiceResponseResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAutoScalingConfigurationRequestTypeDef = TypedDict(
    "DescribeAutoScalingConfigurationRequestTypeDef",
    {
        "AutoScalingConfigurationArn": str,
    },
)

DescribeAutoScalingConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeAutoScalingConfigurationResponseResponseTypeDef",
    {
        "AutoScalingConfiguration": "AutoScalingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeCustomDomainsRequestTypeDef = TypedDict(
    "_RequiredDescribeCustomDomainsRequestTypeDef",
    {
        "ServiceArn": str,
    },
)
_OptionalDescribeCustomDomainsRequestTypeDef = TypedDict(
    "_OptionalDescribeCustomDomainsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class DescribeCustomDomainsRequestTypeDef(
    _RequiredDescribeCustomDomainsRequestTypeDef, _OptionalDescribeCustomDomainsRequestTypeDef
):
    pass


DescribeCustomDomainsResponseResponseTypeDef = TypedDict(
    "DescribeCustomDomainsResponseResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomains": List["CustomDomainTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServiceRequestTypeDef = TypedDict(
    "DescribeServiceRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

DescribeServiceResponseResponseTypeDef = TypedDict(
    "DescribeServiceResponseResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateCustomDomainRequestTypeDef = TypedDict(
    "DisassociateCustomDomainRequestTypeDef",
    {
        "ServiceArn": str,
        "DomainName": str,
    },
)

DisassociateCustomDomainResponseResponseTypeDef = TypedDict(
    "DisassociateCustomDomainResponseResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomain": "CustomDomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "KmsKey": str,
    },
)

HealthCheckConfigurationTypeDef = TypedDict(
    "HealthCheckConfigurationTypeDef",
    {
        "Protocol": HealthCheckProtocolType,
        "Path": str,
        "Interval": int,
        "Timeout": int,
        "HealthyThreshold": int,
        "UnhealthyThreshold": int,
    },
    total=False,
)

ImageConfigurationTypeDef = TypedDict(
    "ImageConfigurationTypeDef",
    {
        "RuntimeEnvironmentVariables": Dict[str, str],
        "StartCommand": str,
        "Port": str,
    },
    total=False,
)

_RequiredImageRepositoryTypeDef = TypedDict(
    "_RequiredImageRepositoryTypeDef",
    {
        "ImageIdentifier": str,
        "ImageRepositoryType": ImageRepositoryTypeType,
    },
)
_OptionalImageRepositoryTypeDef = TypedDict(
    "_OptionalImageRepositoryTypeDef",
    {
        "ImageConfiguration": "ImageConfigurationTypeDef",
    },
    total=False,
)


class ImageRepositoryTypeDef(_RequiredImageRepositoryTypeDef, _OptionalImageRepositoryTypeDef):
    pass


InstanceConfigurationTypeDef = TypedDict(
    "InstanceConfigurationTypeDef",
    {
        "Cpu": str,
        "Memory": str,
        "InstanceRoleArn": str,
    },
    total=False,
)

ListAutoScalingConfigurationsRequestTypeDef = TypedDict(
    "ListAutoScalingConfigurationsRequestTypeDef",
    {
        "AutoScalingConfigurationName": str,
        "LatestOnly": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAutoScalingConfigurationsResponseResponseTypeDef = TypedDict(
    "ListAutoScalingConfigurationsResponseResponseTypeDef",
    {
        "AutoScalingConfigurationSummaryList": List["AutoScalingConfigurationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConnectionsRequestTypeDef = TypedDict(
    "ListConnectionsRequestTypeDef",
    {
        "ConnectionName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListConnectionsResponseResponseTypeDef = TypedDict(
    "ListConnectionsResponseResponseTypeDef",
    {
        "ConnectionSummaryList": List["ConnectionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListOperationsRequestTypeDef = TypedDict(
    "_RequiredListOperationsRequestTypeDef",
    {
        "ServiceArn": str,
    },
)
_OptionalListOperationsRequestTypeDef = TypedDict(
    "_OptionalListOperationsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListOperationsRequestTypeDef(
    _RequiredListOperationsRequestTypeDef, _OptionalListOperationsRequestTypeDef
):
    pass


ListOperationsResponseResponseTypeDef = TypedDict(
    "ListOperationsResponseResponseTypeDef",
    {
        "OperationSummaryList": List["OperationSummaryTypeDef"],
        "NextToken": str,
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
        "ServiceSummaryList": List["ServiceSummaryTypeDef"],
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
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OperationSummaryTypeDef = TypedDict(
    "OperationSummaryTypeDef",
    {
        "Id": str,
        "Type": OperationTypeType,
        "Status": OperationStatusType,
        "TargetArn": str,
        "StartedAt": datetime,
        "EndedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

PauseServiceRequestTypeDef = TypedDict(
    "PauseServiceRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

PauseServiceResponseResponseTypeDef = TypedDict(
    "PauseServiceResponseResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
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

ResumeServiceRequestTypeDef = TypedDict(
    "ResumeServiceRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

ResumeServiceResponseResponseTypeDef = TypedDict(
    "ResumeServiceResponseResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "ServiceName": str,
        "ServiceId": str,
        "ServiceArn": str,
        "ServiceUrl": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": ServiceStatusType,
    },
    total=False,
)

_RequiredServiceTypeDef = TypedDict(
    "_RequiredServiceTypeDef",
    {
        "ServiceName": str,
        "ServiceId": str,
        "ServiceArn": str,
        "ServiceUrl": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": ServiceStatusType,
        "SourceConfiguration": "SourceConfigurationTypeDef",
        "InstanceConfiguration": "InstanceConfigurationTypeDef",
        "AutoScalingConfigurationSummary": "AutoScalingConfigurationSummaryTypeDef",
    },
)
_OptionalServiceTypeDef = TypedDict(
    "_OptionalServiceTypeDef",
    {
        "DeletedAt": datetime,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "HealthCheckConfiguration": "HealthCheckConfigurationTypeDef",
    },
    total=False,
)


class ServiceTypeDef(_RequiredServiceTypeDef, _OptionalServiceTypeDef):
    pass


SourceCodeVersionTypeDef = TypedDict(
    "SourceCodeVersionTypeDef",
    {
        "Type": Literal["BRANCH"],
        "Value": str,
    },
)

SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "CodeRepository": "CodeRepositoryTypeDef",
        "ImageRepository": "ImageRepositoryTypeDef",
        "AutoDeploymentsEnabled": bool,
        "AuthenticationConfiguration": "AuthenticationConfigurationTypeDef",
    },
    total=False,
)

StartDeploymentRequestTypeDef = TypedDict(
    "StartDeploymentRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

StartDeploymentResponseResponseTypeDef = TypedDict(
    "StartDeploymentResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
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

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateServiceRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceRequestTypeDef",
    {
        "ServiceArn": str,
    },
)
_OptionalUpdateServiceRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceRequestTypeDef",
    {
        "SourceConfiguration": "SourceConfigurationTypeDef",
        "InstanceConfiguration": "InstanceConfigurationTypeDef",
        "AutoScalingConfigurationArn": str,
        "HealthCheckConfiguration": "HealthCheckConfigurationTypeDef",
    },
    total=False,
)


class UpdateServiceRequestTypeDef(
    _RequiredUpdateServiceRequestTypeDef, _OptionalUpdateServiceRequestTypeDef
):
    pass


UpdateServiceResponseResponseTypeDef = TypedDict(
    "UpdateServiceResponseResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
