"""
Type annotations for apprunner service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/type_defs.html)

Usage::

    ```python
    from mypy_boto3_apprunner.type_defs import AssociateCustomDomainResponseTypeDef

    data: AssociateCustomDomainResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

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
    "AssociateCustomDomainResponseTypeDef",
    "AuthenticationConfigurationTypeDef",
    "AutoScalingConfigurationSummaryTypeDef",
    "AutoScalingConfigurationTypeDef",
    "CertificateValidationRecordTypeDef",
    "CodeConfigurationTypeDef",
    "CodeConfigurationValuesTypeDef",
    "CodeRepositoryTypeDef",
    "ConnectionSummaryTypeDef",
    "ConnectionTypeDef",
    "CreateAutoScalingConfigurationResponseTypeDef",
    "CreateConnectionResponseTypeDef",
    "CreateServiceResponseTypeDef",
    "CustomDomainTypeDef",
    "DeleteAutoScalingConfigurationResponseTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteServiceResponseTypeDef",
    "DescribeAutoScalingConfigurationResponseTypeDef",
    "DescribeCustomDomainsResponseTypeDef",
    "DescribeServiceResponseTypeDef",
    "DisassociateCustomDomainResponseTypeDef",
    "EncryptionConfigurationTypeDef",
    "HealthCheckConfigurationTypeDef",
    "ImageConfigurationTypeDef",
    "ImageRepositoryTypeDef",
    "InstanceConfigurationTypeDef",
    "ListAutoScalingConfigurationsResponseTypeDef",
    "ListConnectionsResponseTypeDef",
    "ListOperationsResponseTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OperationSummaryTypeDef",
    "PauseServiceResponseTypeDef",
    "ResumeServiceResponseTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTypeDef",
    "SourceCodeVersionTypeDef",
    "SourceConfigurationTypeDef",
    "StartDeploymentResponseTypeDef",
    "TagTypeDef",
    "UpdateServiceResponseTypeDef",
)

AssociateCustomDomainResponseTypeDef = TypedDict(
    "AssociateCustomDomainResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomain": "CustomDomainTypeDef",
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

CreateAutoScalingConfigurationResponseTypeDef = TypedDict(
    "CreateAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": "AutoScalingConfigurationTypeDef",
    },
)

CreateConnectionResponseTypeDef = TypedDict(
    "CreateConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
    },
)

CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "OperationId": str,
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


DeleteAutoScalingConfigurationResponseTypeDef = TypedDict(
    "DeleteAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": "AutoScalingConfigurationTypeDef",
    },
)

DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
    },
    total=False,
)

DeleteServiceResponseTypeDef = TypedDict(
    "DeleteServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "OperationId": str,
    },
)

DescribeAutoScalingConfigurationResponseTypeDef = TypedDict(
    "DescribeAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": "AutoScalingConfigurationTypeDef",
    },
)

_RequiredDescribeCustomDomainsResponseTypeDef = TypedDict(
    "_RequiredDescribeCustomDomainsResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomains": List["CustomDomainTypeDef"],
    },
)
_OptionalDescribeCustomDomainsResponseTypeDef = TypedDict(
    "_OptionalDescribeCustomDomainsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class DescribeCustomDomainsResponseTypeDef(
    _RequiredDescribeCustomDomainsResponseTypeDef, _OptionalDescribeCustomDomainsResponseTypeDef
):
    pass


DescribeServiceResponseTypeDef = TypedDict(
    "DescribeServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
    },
)

DisassociateCustomDomainResponseTypeDef = TypedDict(
    "DisassociateCustomDomainResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomain": "CustomDomainTypeDef",
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

_RequiredListAutoScalingConfigurationsResponseTypeDef = TypedDict(
    "_RequiredListAutoScalingConfigurationsResponseTypeDef",
    {
        "AutoScalingConfigurationSummaryList": List["AutoScalingConfigurationSummaryTypeDef"],
    },
)
_OptionalListAutoScalingConfigurationsResponseTypeDef = TypedDict(
    "_OptionalListAutoScalingConfigurationsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListAutoScalingConfigurationsResponseTypeDef(
    _RequiredListAutoScalingConfigurationsResponseTypeDef,
    _OptionalListAutoScalingConfigurationsResponseTypeDef,
):
    pass


_RequiredListConnectionsResponseTypeDef = TypedDict(
    "_RequiredListConnectionsResponseTypeDef",
    {
        "ConnectionSummaryList": List["ConnectionSummaryTypeDef"],
    },
)
_OptionalListConnectionsResponseTypeDef = TypedDict(
    "_OptionalListConnectionsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListConnectionsResponseTypeDef(
    _RequiredListConnectionsResponseTypeDef, _OptionalListConnectionsResponseTypeDef
):
    pass


ListOperationsResponseTypeDef = TypedDict(
    "ListOperationsResponseTypeDef",
    {
        "OperationSummaryList": List["OperationSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredListServicesResponseTypeDef = TypedDict(
    "_RequiredListServicesResponseTypeDef",
    {
        "ServiceSummaryList": List["ServiceSummaryTypeDef"],
    },
)
_OptionalListServicesResponseTypeDef = TypedDict(
    "_OptionalListServicesResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListServicesResponseTypeDef(
    _RequiredListServicesResponseTypeDef, _OptionalListServicesResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
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

_RequiredPauseServiceResponseTypeDef = TypedDict(
    "_RequiredPauseServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
    },
)
_OptionalPauseServiceResponseTypeDef = TypedDict(
    "_OptionalPauseServiceResponseTypeDef",
    {
        "OperationId": str,
    },
    total=False,
)


class PauseServiceResponseTypeDef(
    _RequiredPauseServiceResponseTypeDef, _OptionalPauseServiceResponseTypeDef
):
    pass


_RequiredResumeServiceResponseTypeDef = TypedDict(
    "_RequiredResumeServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
    },
)
_OptionalResumeServiceResponseTypeDef = TypedDict(
    "_OptionalResumeServiceResponseTypeDef",
    {
        "OperationId": str,
    },
    total=False,
)


class ResumeServiceResponseTypeDef(
    _RequiredResumeServiceResponseTypeDef, _OptionalResumeServiceResponseTypeDef
):
    pass


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

StartDeploymentResponseTypeDef = TypedDict(
    "StartDeploymentResponseTypeDef",
    {
        "OperationId": str,
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

UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "OperationId": str,
    },
)
