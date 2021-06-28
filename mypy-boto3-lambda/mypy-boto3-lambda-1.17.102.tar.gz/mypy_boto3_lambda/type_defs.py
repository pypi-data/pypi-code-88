"""
Type annotations for lambda service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lambda.type_defs import AccountLimitTypeDef

    data: AccountLimitTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    CodeSigningPolicyType,
    EventSourcePositionType,
    InvocationTypeType,
    LastUpdateStatusReasonCodeType,
    LastUpdateStatusType,
    LogTypeType,
    PackageTypeType,
    ProvisionedConcurrencyStatusEnumType,
    RuntimeType,
    SourceAccessTypeType,
    StateReasonCodeType,
    StateType,
    TracingModeType,
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
    "AccountUsageTypeDef",
    "AddLayerVersionPermissionRequestTypeDef",
    "AddLayerVersionPermissionResponseResponseTypeDef",
    "AddPermissionRequestTypeDef",
    "AddPermissionResponseResponseTypeDef",
    "AliasConfigurationResponseTypeDef",
    "AliasRoutingConfigurationTypeDef",
    "AllowedPublishersTypeDef",
    "CodeSigningConfigTypeDef",
    "CodeSigningPoliciesTypeDef",
    "ConcurrencyTypeDef",
    "CreateAliasRequestTypeDef",
    "CreateCodeSigningConfigRequestTypeDef",
    "CreateCodeSigningConfigResponseResponseTypeDef",
    "CreateEventSourceMappingRequestTypeDef",
    "CreateFunctionRequestTypeDef",
    "DeadLetterConfigTypeDef",
    "DeleteAliasRequestTypeDef",
    "DeleteCodeSigningConfigRequestTypeDef",
    "DeleteEventSourceMappingRequestTypeDef",
    "DeleteFunctionCodeSigningConfigRequestTypeDef",
    "DeleteFunctionConcurrencyRequestTypeDef",
    "DeleteFunctionEventInvokeConfigRequestTypeDef",
    "DeleteFunctionRequestTypeDef",
    "DeleteLayerVersionRequestTypeDef",
    "DeleteProvisionedConcurrencyConfigRequestTypeDef",
    "DestinationConfigTypeDef",
    "EnvironmentErrorTypeDef",
    "EnvironmentResponseTypeDef",
    "EnvironmentTypeDef",
    "EventSourceMappingConfigurationResponseTypeDef",
    "FileSystemConfigTypeDef",
    "FunctionCodeLocationTypeDef",
    "FunctionCodeTypeDef",
    "FunctionConfigurationResponseTypeDef",
    "FunctionEventInvokeConfigResponseTypeDef",
    "GetAccountSettingsResponseResponseTypeDef",
    "GetAliasRequestTypeDef",
    "GetCodeSigningConfigRequestTypeDef",
    "GetCodeSigningConfigResponseResponseTypeDef",
    "GetEventSourceMappingRequestTypeDef",
    "GetFunctionCodeSigningConfigRequestTypeDef",
    "GetFunctionCodeSigningConfigResponseResponseTypeDef",
    "GetFunctionConcurrencyRequestTypeDef",
    "GetFunctionConcurrencyResponseResponseTypeDef",
    "GetFunctionConfigurationRequestTypeDef",
    "GetFunctionEventInvokeConfigRequestTypeDef",
    "GetFunctionRequestTypeDef",
    "GetFunctionResponseResponseTypeDef",
    "GetLayerVersionByArnRequestTypeDef",
    "GetLayerVersionPolicyRequestTypeDef",
    "GetLayerVersionPolicyResponseResponseTypeDef",
    "GetLayerVersionRequestTypeDef",
    "GetLayerVersionResponseResponseTypeDef",
    "GetPolicyRequestTypeDef",
    "GetPolicyResponseResponseTypeDef",
    "GetProvisionedConcurrencyConfigRequestTypeDef",
    "GetProvisionedConcurrencyConfigResponseResponseTypeDef",
    "ImageConfigErrorTypeDef",
    "ImageConfigResponseTypeDef",
    "ImageConfigTypeDef",
    "InvocationRequestTypeDef",
    "InvocationResponseTypeDef",
    "InvokeAsyncRequestTypeDef",
    "InvokeAsyncResponseResponseTypeDef",
    "LayerTypeDef",
    "LayerVersionContentInputTypeDef",
    "LayerVersionContentOutputTypeDef",
    "LayerVersionsListItemTypeDef",
    "LayersListItemTypeDef",
    "ListAliasesRequestTypeDef",
    "ListAliasesResponseResponseTypeDef",
    "ListCodeSigningConfigsRequestTypeDef",
    "ListCodeSigningConfigsResponseResponseTypeDef",
    "ListEventSourceMappingsRequestTypeDef",
    "ListEventSourceMappingsResponseResponseTypeDef",
    "ListFunctionEventInvokeConfigsRequestTypeDef",
    "ListFunctionEventInvokeConfigsResponseResponseTypeDef",
    "ListFunctionsByCodeSigningConfigRequestTypeDef",
    "ListFunctionsByCodeSigningConfigResponseResponseTypeDef",
    "ListFunctionsRequestTypeDef",
    "ListFunctionsResponseResponseTypeDef",
    "ListLayerVersionsRequestTypeDef",
    "ListLayerVersionsResponseResponseTypeDef",
    "ListLayersRequestTypeDef",
    "ListLayersResponseResponseTypeDef",
    "ListProvisionedConcurrencyConfigsRequestTypeDef",
    "ListProvisionedConcurrencyConfigsResponseResponseTypeDef",
    "ListTagsRequestTypeDef",
    "ListTagsResponseResponseTypeDef",
    "ListVersionsByFunctionRequestTypeDef",
    "ListVersionsByFunctionResponseResponseTypeDef",
    "OnFailureTypeDef",
    "OnSuccessTypeDef",
    "PaginatorConfigTypeDef",
    "ProvisionedConcurrencyConfigListItemTypeDef",
    "PublishLayerVersionRequestTypeDef",
    "PublishLayerVersionResponseResponseTypeDef",
    "PublishVersionRequestTypeDef",
    "PutFunctionCodeSigningConfigRequestTypeDef",
    "PutFunctionCodeSigningConfigResponseResponseTypeDef",
    "PutFunctionConcurrencyRequestTypeDef",
    "PutFunctionEventInvokeConfigRequestTypeDef",
    "PutProvisionedConcurrencyConfigRequestTypeDef",
    "PutProvisionedConcurrencyConfigResponseResponseTypeDef",
    "RemoveLayerVersionPermissionRequestTypeDef",
    "RemovePermissionRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SelfManagedEventSourceTypeDef",
    "SourceAccessConfigurationTypeDef",
    "TagResourceRequestTypeDef",
    "TracingConfigResponseTypeDef",
    "TracingConfigTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAliasRequestTypeDef",
    "UpdateCodeSigningConfigRequestTypeDef",
    "UpdateCodeSigningConfigResponseResponseTypeDef",
    "UpdateEventSourceMappingRequestTypeDef",
    "UpdateFunctionCodeRequestTypeDef",
    "UpdateFunctionConfigurationRequestTypeDef",
    "UpdateFunctionEventInvokeConfigRequestTypeDef",
    "VpcConfigResponseTypeDef",
    "VpcConfigTypeDef",
    "WaiterConfigTypeDef",
)

AccountLimitTypeDef = TypedDict(
    "AccountLimitTypeDef",
    {
        "TotalCodeSize": int,
        "CodeSizeUnzipped": int,
        "CodeSizeZipped": int,
        "ConcurrentExecutions": int,
        "UnreservedConcurrentExecutions": int,
    },
    total=False,
)

AccountUsageTypeDef = TypedDict(
    "AccountUsageTypeDef",
    {
        "TotalCodeSize": int,
        "FunctionCount": int,
    },
    total=False,
)

_RequiredAddLayerVersionPermissionRequestTypeDef = TypedDict(
    "_RequiredAddLayerVersionPermissionRequestTypeDef",
    {
        "LayerName": str,
        "VersionNumber": int,
        "StatementId": str,
        "Action": str,
        "Principal": str,
    },
)
_OptionalAddLayerVersionPermissionRequestTypeDef = TypedDict(
    "_OptionalAddLayerVersionPermissionRequestTypeDef",
    {
        "OrganizationId": str,
        "RevisionId": str,
    },
    total=False,
)


class AddLayerVersionPermissionRequestTypeDef(
    _RequiredAddLayerVersionPermissionRequestTypeDef,
    _OptionalAddLayerVersionPermissionRequestTypeDef,
):
    pass


AddLayerVersionPermissionResponseResponseTypeDef = TypedDict(
    "AddLayerVersionPermissionResponseResponseTypeDef",
    {
        "Statement": str,
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAddPermissionRequestTypeDef = TypedDict(
    "_RequiredAddPermissionRequestTypeDef",
    {
        "FunctionName": str,
        "StatementId": str,
        "Action": str,
        "Principal": str,
    },
)
_OptionalAddPermissionRequestTypeDef = TypedDict(
    "_OptionalAddPermissionRequestTypeDef",
    {
        "SourceArn": str,
        "SourceAccount": str,
        "EventSourceToken": str,
        "Qualifier": str,
        "RevisionId": str,
    },
    total=False,
)


class AddPermissionRequestTypeDef(
    _RequiredAddPermissionRequestTypeDef, _OptionalAddPermissionRequestTypeDef
):
    pass


AddPermissionResponseResponseTypeDef = TypedDict(
    "AddPermissionResponseResponseTypeDef",
    {
        "Statement": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AliasConfigurationResponseTypeDef = TypedDict(
    "AliasConfigurationResponseTypeDef",
    {
        "AliasArn": str,
        "Name": str,
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": "AliasRoutingConfigurationTypeDef",
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AliasRoutingConfigurationTypeDef = TypedDict(
    "AliasRoutingConfigurationTypeDef",
    {
        "AdditionalVersionWeights": Dict[str, float],
    },
    total=False,
)

AllowedPublishersTypeDef = TypedDict(
    "AllowedPublishersTypeDef",
    {
        "SigningProfileVersionArns": List[str],
    },
)

_RequiredCodeSigningConfigTypeDef = TypedDict(
    "_RequiredCodeSigningConfigTypeDef",
    {
        "CodeSigningConfigId": str,
        "CodeSigningConfigArn": str,
        "AllowedPublishers": "AllowedPublishersTypeDef",
        "CodeSigningPolicies": "CodeSigningPoliciesTypeDef",
        "LastModified": str,
    },
)
_OptionalCodeSigningConfigTypeDef = TypedDict(
    "_OptionalCodeSigningConfigTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class CodeSigningConfigTypeDef(
    _RequiredCodeSigningConfigTypeDef, _OptionalCodeSigningConfigTypeDef
):
    pass


CodeSigningPoliciesTypeDef = TypedDict(
    "CodeSigningPoliciesTypeDef",
    {
        "UntrustedArtifactOnDeployment": CodeSigningPolicyType,
    },
    total=False,
)

ConcurrencyTypeDef = TypedDict(
    "ConcurrencyTypeDef",
    {
        "ReservedConcurrentExecutions": int,
    },
    total=False,
)

_RequiredCreateAliasRequestTypeDef = TypedDict(
    "_RequiredCreateAliasRequestTypeDef",
    {
        "FunctionName": str,
        "Name": str,
        "FunctionVersion": str,
    },
)
_OptionalCreateAliasRequestTypeDef = TypedDict(
    "_OptionalCreateAliasRequestTypeDef",
    {
        "Description": str,
        "RoutingConfig": "AliasRoutingConfigurationTypeDef",
    },
    total=False,
)


class CreateAliasRequestTypeDef(
    _RequiredCreateAliasRequestTypeDef, _OptionalCreateAliasRequestTypeDef
):
    pass


_RequiredCreateCodeSigningConfigRequestTypeDef = TypedDict(
    "_RequiredCreateCodeSigningConfigRequestTypeDef",
    {
        "AllowedPublishers": "AllowedPublishersTypeDef",
    },
)
_OptionalCreateCodeSigningConfigRequestTypeDef = TypedDict(
    "_OptionalCreateCodeSigningConfigRequestTypeDef",
    {
        "Description": str,
        "CodeSigningPolicies": "CodeSigningPoliciesTypeDef",
    },
    total=False,
)


class CreateCodeSigningConfigRequestTypeDef(
    _RequiredCreateCodeSigningConfigRequestTypeDef, _OptionalCreateCodeSigningConfigRequestTypeDef
):
    pass


CreateCodeSigningConfigResponseResponseTypeDef = TypedDict(
    "CreateCodeSigningConfigResponseResponseTypeDef",
    {
        "CodeSigningConfig": "CodeSigningConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventSourceMappingRequestTypeDef = TypedDict(
    "_RequiredCreateEventSourceMappingRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalCreateEventSourceMappingRequestTypeDef = TypedDict(
    "_OptionalCreateEventSourceMappingRequestTypeDef",
    {
        "EventSourceArn": str,
        "Enabled": bool,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "ParallelizationFactor": int,
        "StartingPosition": EventSourcePositionType,
        "StartingPositionTimestamp": Union[datetime, str],
        "DestinationConfig": "DestinationConfigTypeDef",
        "MaximumRecordAgeInSeconds": int,
        "BisectBatchOnFunctionError": bool,
        "MaximumRetryAttempts": int,
        "TumblingWindowInSeconds": int,
        "Topics": List[str],
        "Queues": List[str],
        "SourceAccessConfigurations": List["SourceAccessConfigurationTypeDef"],
        "SelfManagedEventSource": "SelfManagedEventSourceTypeDef",
        "FunctionResponseTypes": List[Literal["ReportBatchItemFailures"]],
    },
    total=False,
)


class CreateEventSourceMappingRequestTypeDef(
    _RequiredCreateEventSourceMappingRequestTypeDef, _OptionalCreateEventSourceMappingRequestTypeDef
):
    pass


_RequiredCreateFunctionRequestTypeDef = TypedDict(
    "_RequiredCreateFunctionRequestTypeDef",
    {
        "FunctionName": str,
        "Role": str,
        "Code": "FunctionCodeTypeDef",
    },
)
_OptionalCreateFunctionRequestTypeDef = TypedDict(
    "_OptionalCreateFunctionRequestTypeDef",
    {
        "Runtime": RuntimeType,
        "Handler": str,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "Publish": bool,
        "VpcConfig": "VpcConfigTypeDef",
        "PackageType": PackageTypeType,
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "Environment": "EnvironmentTypeDef",
        "KMSKeyArn": str,
        "TracingConfig": "TracingConfigTypeDef",
        "Tags": Dict[str, str],
        "Layers": List[str],
        "FileSystemConfigs": List["FileSystemConfigTypeDef"],
        "ImageConfig": "ImageConfigTypeDef",
        "CodeSigningConfigArn": str,
    },
    total=False,
)


class CreateFunctionRequestTypeDef(
    _RequiredCreateFunctionRequestTypeDef, _OptionalCreateFunctionRequestTypeDef
):
    pass


DeadLetterConfigTypeDef = TypedDict(
    "DeadLetterConfigTypeDef",
    {
        "TargetArn": str,
    },
    total=False,
)

DeleteAliasRequestTypeDef = TypedDict(
    "DeleteAliasRequestTypeDef",
    {
        "FunctionName": str,
        "Name": str,
    },
)

DeleteCodeSigningConfigRequestTypeDef = TypedDict(
    "DeleteCodeSigningConfigRequestTypeDef",
    {
        "CodeSigningConfigArn": str,
    },
)

DeleteEventSourceMappingRequestTypeDef = TypedDict(
    "DeleteEventSourceMappingRequestTypeDef",
    {
        "UUID": str,
    },
)

DeleteFunctionCodeSigningConfigRequestTypeDef = TypedDict(
    "DeleteFunctionCodeSigningConfigRequestTypeDef",
    {
        "FunctionName": str,
    },
)

DeleteFunctionConcurrencyRequestTypeDef = TypedDict(
    "DeleteFunctionConcurrencyRequestTypeDef",
    {
        "FunctionName": str,
    },
)

_RequiredDeleteFunctionEventInvokeConfigRequestTypeDef = TypedDict(
    "_RequiredDeleteFunctionEventInvokeConfigRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalDeleteFunctionEventInvokeConfigRequestTypeDef = TypedDict(
    "_OptionalDeleteFunctionEventInvokeConfigRequestTypeDef",
    {
        "Qualifier": str,
    },
    total=False,
)


class DeleteFunctionEventInvokeConfigRequestTypeDef(
    _RequiredDeleteFunctionEventInvokeConfigRequestTypeDef,
    _OptionalDeleteFunctionEventInvokeConfigRequestTypeDef,
):
    pass


_RequiredDeleteFunctionRequestTypeDef = TypedDict(
    "_RequiredDeleteFunctionRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalDeleteFunctionRequestTypeDef = TypedDict(
    "_OptionalDeleteFunctionRequestTypeDef",
    {
        "Qualifier": str,
    },
    total=False,
)


class DeleteFunctionRequestTypeDef(
    _RequiredDeleteFunctionRequestTypeDef, _OptionalDeleteFunctionRequestTypeDef
):
    pass


DeleteLayerVersionRequestTypeDef = TypedDict(
    "DeleteLayerVersionRequestTypeDef",
    {
        "LayerName": str,
        "VersionNumber": int,
    },
)

DeleteProvisionedConcurrencyConfigRequestTypeDef = TypedDict(
    "DeleteProvisionedConcurrencyConfigRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": str,
    },
)

DestinationConfigTypeDef = TypedDict(
    "DestinationConfigTypeDef",
    {
        "OnSuccess": "OnSuccessTypeDef",
        "OnFailure": "OnFailureTypeDef",
    },
    total=False,
)

EnvironmentErrorTypeDef = TypedDict(
    "EnvironmentErrorTypeDef",
    {
        "ErrorCode": str,
        "Message": str,
    },
    total=False,
)

EnvironmentResponseTypeDef = TypedDict(
    "EnvironmentResponseTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": "EnvironmentErrorTypeDef",
    },
    total=False,
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
    },
    total=False,
)

EventSourceMappingConfigurationResponseTypeDef = TypedDict(
    "EventSourceMappingConfigurationResponseTypeDef",
    {
        "UUID": str,
        "StartingPosition": EventSourcePositionType,
        "StartingPositionTimestamp": datetime,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "ParallelizationFactor": int,
        "EventSourceArn": str,
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
        "DestinationConfig": "DestinationConfigTypeDef",
        "Topics": List[str],
        "Queues": List[str],
        "SourceAccessConfigurations": List["SourceAccessConfigurationTypeDef"],
        "SelfManagedEventSource": "SelfManagedEventSourceTypeDef",
        "MaximumRecordAgeInSeconds": int,
        "BisectBatchOnFunctionError": bool,
        "MaximumRetryAttempts": int,
        "TumblingWindowInSeconds": int,
        "FunctionResponseTypes": List[Literal["ReportBatchItemFailures"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FileSystemConfigTypeDef = TypedDict(
    "FileSystemConfigTypeDef",
    {
        "Arn": str,
        "LocalMountPath": str,
    },
)

FunctionCodeLocationTypeDef = TypedDict(
    "FunctionCodeLocationTypeDef",
    {
        "RepositoryType": str,
        "Location": str,
        "ImageUri": str,
        "ResolvedImageUri": str,
    },
    total=False,
)

FunctionCodeTypeDef = TypedDict(
    "FunctionCodeTypeDef",
    {
        "ZipFile": Union[bytes, IO[bytes], StreamingBody],
        "S3Bucket": str,
        "S3Key": str,
        "S3ObjectVersion": str,
        "ImageUri": str,
    },
    total=False,
)

FunctionConfigurationResponseTypeDef = TypedDict(
    "FunctionConfigurationResponseTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": RuntimeType,
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": "VpcConfigResponseTypeDef",
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "Environment": "EnvironmentResponseTypeDef",
        "KMSKeyArn": str,
        "TracingConfig": "TracingConfigResponseTypeDef",
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List["LayerTypeDef"],
        "State": StateType,
        "StateReason": str,
        "StateReasonCode": StateReasonCodeType,
        "LastUpdateStatus": LastUpdateStatusType,
        "LastUpdateStatusReason": str,
        "LastUpdateStatusReasonCode": LastUpdateStatusReasonCodeType,
        "FileSystemConfigs": List["FileSystemConfigTypeDef"],
        "PackageType": PackageTypeType,
        "ImageConfigResponse": "ImageConfigResponseTypeDef",
        "SigningProfileVersionArn": str,
        "SigningJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FunctionEventInvokeConfigResponseTypeDef = TypedDict(
    "FunctionEventInvokeConfigResponseTypeDef",
    {
        "LastModified": datetime,
        "FunctionArn": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": "DestinationConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccountSettingsResponseResponseTypeDef = TypedDict(
    "GetAccountSettingsResponseResponseTypeDef",
    {
        "AccountLimit": "AccountLimitTypeDef",
        "AccountUsage": "AccountUsageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAliasRequestTypeDef = TypedDict(
    "GetAliasRequestTypeDef",
    {
        "FunctionName": str,
        "Name": str,
    },
)

GetCodeSigningConfigRequestTypeDef = TypedDict(
    "GetCodeSigningConfigRequestTypeDef",
    {
        "CodeSigningConfigArn": str,
    },
)

GetCodeSigningConfigResponseResponseTypeDef = TypedDict(
    "GetCodeSigningConfigResponseResponseTypeDef",
    {
        "CodeSigningConfig": "CodeSigningConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventSourceMappingRequestTypeDef = TypedDict(
    "GetEventSourceMappingRequestTypeDef",
    {
        "UUID": str,
    },
)

GetFunctionCodeSigningConfigRequestTypeDef = TypedDict(
    "GetFunctionCodeSigningConfigRequestTypeDef",
    {
        "FunctionName": str,
    },
)

GetFunctionCodeSigningConfigResponseResponseTypeDef = TypedDict(
    "GetFunctionCodeSigningConfigResponseResponseTypeDef",
    {
        "CodeSigningConfigArn": str,
        "FunctionName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFunctionConcurrencyRequestTypeDef = TypedDict(
    "GetFunctionConcurrencyRequestTypeDef",
    {
        "FunctionName": str,
    },
)

GetFunctionConcurrencyResponseResponseTypeDef = TypedDict(
    "GetFunctionConcurrencyResponseResponseTypeDef",
    {
        "ReservedConcurrentExecutions": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFunctionConfigurationRequestTypeDef = TypedDict(
    "_RequiredGetFunctionConfigurationRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalGetFunctionConfigurationRequestTypeDef = TypedDict(
    "_OptionalGetFunctionConfigurationRequestTypeDef",
    {
        "Qualifier": str,
    },
    total=False,
)


class GetFunctionConfigurationRequestTypeDef(
    _RequiredGetFunctionConfigurationRequestTypeDef, _OptionalGetFunctionConfigurationRequestTypeDef
):
    pass


_RequiredGetFunctionEventInvokeConfigRequestTypeDef = TypedDict(
    "_RequiredGetFunctionEventInvokeConfigRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalGetFunctionEventInvokeConfigRequestTypeDef = TypedDict(
    "_OptionalGetFunctionEventInvokeConfigRequestTypeDef",
    {
        "Qualifier": str,
    },
    total=False,
)


class GetFunctionEventInvokeConfigRequestTypeDef(
    _RequiredGetFunctionEventInvokeConfigRequestTypeDef,
    _OptionalGetFunctionEventInvokeConfigRequestTypeDef,
):
    pass


_RequiredGetFunctionRequestTypeDef = TypedDict(
    "_RequiredGetFunctionRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalGetFunctionRequestTypeDef = TypedDict(
    "_OptionalGetFunctionRequestTypeDef",
    {
        "Qualifier": str,
    },
    total=False,
)


class GetFunctionRequestTypeDef(
    _RequiredGetFunctionRequestTypeDef, _OptionalGetFunctionRequestTypeDef
):
    pass


GetFunctionResponseResponseTypeDef = TypedDict(
    "GetFunctionResponseResponseTypeDef",
    {
        "Configuration": "FunctionConfigurationResponseTypeDef",
        "Code": "FunctionCodeLocationTypeDef",
        "Tags": Dict[str, str],
        "Concurrency": "ConcurrencyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLayerVersionByArnRequestTypeDef = TypedDict(
    "GetLayerVersionByArnRequestTypeDef",
    {
        "Arn": str,
    },
)

GetLayerVersionPolicyRequestTypeDef = TypedDict(
    "GetLayerVersionPolicyRequestTypeDef",
    {
        "LayerName": str,
        "VersionNumber": int,
    },
)

GetLayerVersionPolicyResponseResponseTypeDef = TypedDict(
    "GetLayerVersionPolicyResponseResponseTypeDef",
    {
        "Policy": str,
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLayerVersionRequestTypeDef = TypedDict(
    "GetLayerVersionRequestTypeDef",
    {
        "LayerName": str,
        "VersionNumber": int,
    },
)

GetLayerVersionResponseResponseTypeDef = TypedDict(
    "GetLayerVersionResponseResponseTypeDef",
    {
        "Content": "LayerVersionContentOutputTypeDef",
        "LayerArn": str,
        "LayerVersionArn": str,
        "Description": str,
        "CreatedDate": str,
        "Version": int,
        "CompatibleRuntimes": List[RuntimeType],
        "LicenseInfo": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPolicyRequestTypeDef = TypedDict(
    "_RequiredGetPolicyRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalGetPolicyRequestTypeDef = TypedDict(
    "_OptionalGetPolicyRequestTypeDef",
    {
        "Qualifier": str,
    },
    total=False,
)


class GetPolicyRequestTypeDef(_RequiredGetPolicyRequestTypeDef, _OptionalGetPolicyRequestTypeDef):
    pass


GetPolicyResponseResponseTypeDef = TypedDict(
    "GetPolicyResponseResponseTypeDef",
    {
        "Policy": str,
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProvisionedConcurrencyConfigRequestTypeDef = TypedDict(
    "GetProvisionedConcurrencyConfigRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": str,
    },
)

GetProvisionedConcurrencyConfigResponseResponseTypeDef = TypedDict(
    "GetProvisionedConcurrencyConfigResponseResponseTypeDef",
    {
        "RequestedProvisionedConcurrentExecutions": int,
        "AvailableProvisionedConcurrentExecutions": int,
        "AllocatedProvisionedConcurrentExecutions": int,
        "Status": ProvisionedConcurrencyStatusEnumType,
        "StatusReason": str,
        "LastModified": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageConfigErrorTypeDef = TypedDict(
    "ImageConfigErrorTypeDef",
    {
        "ErrorCode": str,
        "Message": str,
    },
    total=False,
)

ImageConfigResponseTypeDef = TypedDict(
    "ImageConfigResponseTypeDef",
    {
        "ImageConfig": "ImageConfigTypeDef",
        "Error": "ImageConfigErrorTypeDef",
    },
    total=False,
)

ImageConfigTypeDef = TypedDict(
    "ImageConfigTypeDef",
    {
        "EntryPoint": List[str],
        "Command": List[str],
        "WorkingDirectory": str,
    },
    total=False,
)

_RequiredInvocationRequestTypeDef = TypedDict(
    "_RequiredInvocationRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalInvocationRequestTypeDef = TypedDict(
    "_OptionalInvocationRequestTypeDef",
    {
        "InvocationType": InvocationTypeType,
        "LogType": LogTypeType,
        "ClientContext": str,
        "Payload": Union[bytes, IO[bytes], StreamingBody],
        "Qualifier": str,
    },
    total=False,
)


class InvocationRequestTypeDef(
    _RequiredInvocationRequestTypeDef, _OptionalInvocationRequestTypeDef
):
    pass


InvocationResponseTypeDef = TypedDict(
    "InvocationResponseTypeDef",
    {
        "StatusCode": int,
        "FunctionError": str,
        "LogResult": str,
        "Payload": IO[bytes],
        "ExecutedVersion": str,
    },
    total=False,
)

InvokeAsyncRequestTypeDef = TypedDict(
    "InvokeAsyncRequestTypeDef",
    {
        "FunctionName": str,
        "InvokeArgs": Union[bytes, IO[bytes], StreamingBody],
    },
)

InvokeAsyncResponseResponseTypeDef = TypedDict(
    "InvokeAsyncResponseResponseTypeDef",
    {
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "Arn": str,
        "CodeSize": int,
        "SigningProfileVersionArn": str,
        "SigningJobArn": str,
    },
    total=False,
)

LayerVersionContentInputTypeDef = TypedDict(
    "LayerVersionContentInputTypeDef",
    {
        "S3Bucket": str,
        "S3Key": str,
        "S3ObjectVersion": str,
        "ZipFile": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

LayerVersionContentOutputTypeDef = TypedDict(
    "LayerVersionContentOutputTypeDef",
    {
        "Location": str,
        "CodeSha256": str,
        "CodeSize": int,
        "SigningProfileVersionArn": str,
        "SigningJobArn": str,
    },
    total=False,
)

LayerVersionsListItemTypeDef = TypedDict(
    "LayerVersionsListItemTypeDef",
    {
        "LayerVersionArn": str,
        "Version": int,
        "Description": str,
        "CreatedDate": str,
        "CompatibleRuntimes": List[RuntimeType],
        "LicenseInfo": str,
    },
    total=False,
)

LayersListItemTypeDef = TypedDict(
    "LayersListItemTypeDef",
    {
        "LayerName": str,
        "LayerArn": str,
        "LatestMatchingVersion": "LayerVersionsListItemTypeDef",
    },
    total=False,
)

_RequiredListAliasesRequestTypeDef = TypedDict(
    "_RequiredListAliasesRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalListAliasesRequestTypeDef = TypedDict(
    "_OptionalListAliasesRequestTypeDef",
    {
        "FunctionVersion": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListAliasesRequestTypeDef(
    _RequiredListAliasesRequestTypeDef, _OptionalListAliasesRequestTypeDef
):
    pass


ListAliasesResponseResponseTypeDef = TypedDict(
    "ListAliasesResponseResponseTypeDef",
    {
        "NextMarker": str,
        "Aliases": List["AliasConfigurationResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCodeSigningConfigsRequestTypeDef = TypedDict(
    "ListCodeSigningConfigsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListCodeSigningConfigsResponseResponseTypeDef = TypedDict(
    "ListCodeSigningConfigsResponseResponseTypeDef",
    {
        "NextMarker": str,
        "CodeSigningConfigs": List["CodeSigningConfigTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventSourceMappingsRequestTypeDef = TypedDict(
    "ListEventSourceMappingsRequestTypeDef",
    {
        "EventSourceArn": str,
        "FunctionName": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListEventSourceMappingsResponseResponseTypeDef = TypedDict(
    "ListEventSourceMappingsResponseResponseTypeDef",
    {
        "NextMarker": str,
        "EventSourceMappings": List["EventSourceMappingConfigurationResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFunctionEventInvokeConfigsRequestTypeDef = TypedDict(
    "_RequiredListFunctionEventInvokeConfigsRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalListFunctionEventInvokeConfigsRequestTypeDef = TypedDict(
    "_OptionalListFunctionEventInvokeConfigsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListFunctionEventInvokeConfigsRequestTypeDef(
    _RequiredListFunctionEventInvokeConfigsRequestTypeDef,
    _OptionalListFunctionEventInvokeConfigsRequestTypeDef,
):
    pass


ListFunctionEventInvokeConfigsResponseResponseTypeDef = TypedDict(
    "ListFunctionEventInvokeConfigsResponseResponseTypeDef",
    {
        "FunctionEventInvokeConfigs": List["FunctionEventInvokeConfigResponseTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFunctionsByCodeSigningConfigRequestTypeDef = TypedDict(
    "_RequiredListFunctionsByCodeSigningConfigRequestTypeDef",
    {
        "CodeSigningConfigArn": str,
    },
)
_OptionalListFunctionsByCodeSigningConfigRequestTypeDef = TypedDict(
    "_OptionalListFunctionsByCodeSigningConfigRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListFunctionsByCodeSigningConfigRequestTypeDef(
    _RequiredListFunctionsByCodeSigningConfigRequestTypeDef,
    _OptionalListFunctionsByCodeSigningConfigRequestTypeDef,
):
    pass


ListFunctionsByCodeSigningConfigResponseResponseTypeDef = TypedDict(
    "ListFunctionsByCodeSigningConfigResponseResponseTypeDef",
    {
        "NextMarker": str,
        "FunctionArns": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFunctionsRequestTypeDef = TypedDict(
    "ListFunctionsRequestTypeDef",
    {
        "MasterRegion": str,
        "FunctionVersion": Literal["ALL"],
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListFunctionsResponseResponseTypeDef = TypedDict(
    "ListFunctionsResponseResponseTypeDef",
    {
        "NextMarker": str,
        "Functions": List["FunctionConfigurationResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLayerVersionsRequestTypeDef = TypedDict(
    "_RequiredListLayerVersionsRequestTypeDef",
    {
        "LayerName": str,
    },
)
_OptionalListLayerVersionsRequestTypeDef = TypedDict(
    "_OptionalListLayerVersionsRequestTypeDef",
    {
        "CompatibleRuntime": RuntimeType,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListLayerVersionsRequestTypeDef(
    _RequiredListLayerVersionsRequestTypeDef, _OptionalListLayerVersionsRequestTypeDef
):
    pass


ListLayerVersionsResponseResponseTypeDef = TypedDict(
    "ListLayerVersionsResponseResponseTypeDef",
    {
        "NextMarker": str,
        "LayerVersions": List["LayerVersionsListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLayersRequestTypeDef = TypedDict(
    "ListLayersRequestTypeDef",
    {
        "CompatibleRuntime": RuntimeType,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListLayersResponseResponseTypeDef = TypedDict(
    "ListLayersResponseResponseTypeDef",
    {
        "NextMarker": str,
        "Layers": List["LayersListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProvisionedConcurrencyConfigsRequestTypeDef = TypedDict(
    "_RequiredListProvisionedConcurrencyConfigsRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalListProvisionedConcurrencyConfigsRequestTypeDef = TypedDict(
    "_OptionalListProvisionedConcurrencyConfigsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListProvisionedConcurrencyConfigsRequestTypeDef(
    _RequiredListProvisionedConcurrencyConfigsRequestTypeDef,
    _OptionalListProvisionedConcurrencyConfigsRequestTypeDef,
):
    pass


ListProvisionedConcurrencyConfigsResponseResponseTypeDef = TypedDict(
    "ListProvisionedConcurrencyConfigsResponseResponseTypeDef",
    {
        "ProvisionedConcurrencyConfigs": List["ProvisionedConcurrencyConfigListItemTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsRequestTypeDef = TypedDict(
    "ListTagsRequestTypeDef",
    {
        "Resource": str,
    },
)

ListTagsResponseResponseTypeDef = TypedDict(
    "ListTagsResponseResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListVersionsByFunctionRequestTypeDef = TypedDict(
    "_RequiredListVersionsByFunctionRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalListVersionsByFunctionRequestTypeDef = TypedDict(
    "_OptionalListVersionsByFunctionRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListVersionsByFunctionRequestTypeDef(
    _RequiredListVersionsByFunctionRequestTypeDef, _OptionalListVersionsByFunctionRequestTypeDef
):
    pass


ListVersionsByFunctionResponseResponseTypeDef = TypedDict(
    "ListVersionsByFunctionResponseResponseTypeDef",
    {
        "NextMarker": str,
        "Versions": List["FunctionConfigurationResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OnFailureTypeDef = TypedDict(
    "OnFailureTypeDef",
    {
        "Destination": str,
    },
    total=False,
)

OnSuccessTypeDef = TypedDict(
    "OnSuccessTypeDef",
    {
        "Destination": str,
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

ProvisionedConcurrencyConfigListItemTypeDef = TypedDict(
    "ProvisionedConcurrencyConfigListItemTypeDef",
    {
        "FunctionArn": str,
        "RequestedProvisionedConcurrentExecutions": int,
        "AvailableProvisionedConcurrentExecutions": int,
        "AllocatedProvisionedConcurrentExecutions": int,
        "Status": ProvisionedConcurrencyStatusEnumType,
        "StatusReason": str,
        "LastModified": str,
    },
    total=False,
)

_RequiredPublishLayerVersionRequestTypeDef = TypedDict(
    "_RequiredPublishLayerVersionRequestTypeDef",
    {
        "LayerName": str,
        "Content": "LayerVersionContentInputTypeDef",
    },
)
_OptionalPublishLayerVersionRequestTypeDef = TypedDict(
    "_OptionalPublishLayerVersionRequestTypeDef",
    {
        "Description": str,
        "CompatibleRuntimes": List[RuntimeType],
        "LicenseInfo": str,
    },
    total=False,
)


class PublishLayerVersionRequestTypeDef(
    _RequiredPublishLayerVersionRequestTypeDef, _OptionalPublishLayerVersionRequestTypeDef
):
    pass


PublishLayerVersionResponseResponseTypeDef = TypedDict(
    "PublishLayerVersionResponseResponseTypeDef",
    {
        "Content": "LayerVersionContentOutputTypeDef",
        "LayerArn": str,
        "LayerVersionArn": str,
        "Description": str,
        "CreatedDate": str,
        "Version": int,
        "CompatibleRuntimes": List[RuntimeType],
        "LicenseInfo": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPublishVersionRequestTypeDef = TypedDict(
    "_RequiredPublishVersionRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalPublishVersionRequestTypeDef = TypedDict(
    "_OptionalPublishVersionRequestTypeDef",
    {
        "CodeSha256": str,
        "Description": str,
        "RevisionId": str,
    },
    total=False,
)


class PublishVersionRequestTypeDef(
    _RequiredPublishVersionRequestTypeDef, _OptionalPublishVersionRequestTypeDef
):
    pass


PutFunctionCodeSigningConfigRequestTypeDef = TypedDict(
    "PutFunctionCodeSigningConfigRequestTypeDef",
    {
        "CodeSigningConfigArn": str,
        "FunctionName": str,
    },
)

PutFunctionCodeSigningConfigResponseResponseTypeDef = TypedDict(
    "PutFunctionCodeSigningConfigResponseResponseTypeDef",
    {
        "CodeSigningConfigArn": str,
        "FunctionName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutFunctionConcurrencyRequestTypeDef = TypedDict(
    "PutFunctionConcurrencyRequestTypeDef",
    {
        "FunctionName": str,
        "ReservedConcurrentExecutions": int,
    },
)

_RequiredPutFunctionEventInvokeConfigRequestTypeDef = TypedDict(
    "_RequiredPutFunctionEventInvokeConfigRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalPutFunctionEventInvokeConfigRequestTypeDef = TypedDict(
    "_OptionalPutFunctionEventInvokeConfigRequestTypeDef",
    {
        "Qualifier": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": "DestinationConfigTypeDef",
    },
    total=False,
)


class PutFunctionEventInvokeConfigRequestTypeDef(
    _RequiredPutFunctionEventInvokeConfigRequestTypeDef,
    _OptionalPutFunctionEventInvokeConfigRequestTypeDef,
):
    pass


PutProvisionedConcurrencyConfigRequestTypeDef = TypedDict(
    "PutProvisionedConcurrencyConfigRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": str,
        "ProvisionedConcurrentExecutions": int,
    },
)

PutProvisionedConcurrencyConfigResponseResponseTypeDef = TypedDict(
    "PutProvisionedConcurrencyConfigResponseResponseTypeDef",
    {
        "RequestedProvisionedConcurrentExecutions": int,
        "AvailableProvisionedConcurrentExecutions": int,
        "AllocatedProvisionedConcurrentExecutions": int,
        "Status": ProvisionedConcurrencyStatusEnumType,
        "StatusReason": str,
        "LastModified": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRemoveLayerVersionPermissionRequestTypeDef = TypedDict(
    "_RequiredRemoveLayerVersionPermissionRequestTypeDef",
    {
        "LayerName": str,
        "VersionNumber": int,
        "StatementId": str,
    },
)
_OptionalRemoveLayerVersionPermissionRequestTypeDef = TypedDict(
    "_OptionalRemoveLayerVersionPermissionRequestTypeDef",
    {
        "RevisionId": str,
    },
    total=False,
)


class RemoveLayerVersionPermissionRequestTypeDef(
    _RequiredRemoveLayerVersionPermissionRequestTypeDef,
    _OptionalRemoveLayerVersionPermissionRequestTypeDef,
):
    pass


_RequiredRemovePermissionRequestTypeDef = TypedDict(
    "_RequiredRemovePermissionRequestTypeDef",
    {
        "FunctionName": str,
        "StatementId": str,
    },
)
_OptionalRemovePermissionRequestTypeDef = TypedDict(
    "_OptionalRemovePermissionRequestTypeDef",
    {
        "Qualifier": str,
        "RevisionId": str,
    },
    total=False,
)


class RemovePermissionRequestTypeDef(
    _RequiredRemovePermissionRequestTypeDef, _OptionalRemovePermissionRequestTypeDef
):
    pass


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

SelfManagedEventSourceTypeDef = TypedDict(
    "SelfManagedEventSourceTypeDef",
    {
        "Endpoints": Dict[Literal["KAFKA_BOOTSTRAP_SERVERS"], List[str]],
    },
    total=False,
)

SourceAccessConfigurationTypeDef = TypedDict(
    "SourceAccessConfigurationTypeDef",
    {
        "Type": SourceAccessTypeType,
        "URI": str,
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "Resource": str,
        "Tags": Dict[str, str],
    },
)

TracingConfigResponseTypeDef = TypedDict(
    "TracingConfigResponseTypeDef",
    {
        "Mode": TracingModeType,
    },
    total=False,
)

TracingConfigTypeDef = TypedDict(
    "TracingConfigTypeDef",
    {
        "Mode": TracingModeType,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "Resource": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAliasRequestTypeDef = TypedDict(
    "_RequiredUpdateAliasRequestTypeDef",
    {
        "FunctionName": str,
        "Name": str,
    },
)
_OptionalUpdateAliasRequestTypeDef = TypedDict(
    "_OptionalUpdateAliasRequestTypeDef",
    {
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": "AliasRoutingConfigurationTypeDef",
        "RevisionId": str,
    },
    total=False,
)


class UpdateAliasRequestTypeDef(
    _RequiredUpdateAliasRequestTypeDef, _OptionalUpdateAliasRequestTypeDef
):
    pass


_RequiredUpdateCodeSigningConfigRequestTypeDef = TypedDict(
    "_RequiredUpdateCodeSigningConfigRequestTypeDef",
    {
        "CodeSigningConfigArn": str,
    },
)
_OptionalUpdateCodeSigningConfigRequestTypeDef = TypedDict(
    "_OptionalUpdateCodeSigningConfigRequestTypeDef",
    {
        "Description": str,
        "AllowedPublishers": "AllowedPublishersTypeDef",
        "CodeSigningPolicies": "CodeSigningPoliciesTypeDef",
    },
    total=False,
)


class UpdateCodeSigningConfigRequestTypeDef(
    _RequiredUpdateCodeSigningConfigRequestTypeDef, _OptionalUpdateCodeSigningConfigRequestTypeDef
):
    pass


UpdateCodeSigningConfigResponseResponseTypeDef = TypedDict(
    "UpdateCodeSigningConfigResponseResponseTypeDef",
    {
        "CodeSigningConfig": "CodeSigningConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEventSourceMappingRequestTypeDef = TypedDict(
    "_RequiredUpdateEventSourceMappingRequestTypeDef",
    {
        "UUID": str,
    },
)
_OptionalUpdateEventSourceMappingRequestTypeDef = TypedDict(
    "_OptionalUpdateEventSourceMappingRequestTypeDef",
    {
        "FunctionName": str,
        "Enabled": bool,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "DestinationConfig": "DestinationConfigTypeDef",
        "MaximumRecordAgeInSeconds": int,
        "BisectBatchOnFunctionError": bool,
        "MaximumRetryAttempts": int,
        "ParallelizationFactor": int,
        "SourceAccessConfigurations": List["SourceAccessConfigurationTypeDef"],
        "TumblingWindowInSeconds": int,
        "FunctionResponseTypes": List[Literal["ReportBatchItemFailures"]],
    },
    total=False,
)


class UpdateEventSourceMappingRequestTypeDef(
    _RequiredUpdateEventSourceMappingRequestTypeDef, _OptionalUpdateEventSourceMappingRequestTypeDef
):
    pass


_RequiredUpdateFunctionCodeRequestTypeDef = TypedDict(
    "_RequiredUpdateFunctionCodeRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalUpdateFunctionCodeRequestTypeDef = TypedDict(
    "_OptionalUpdateFunctionCodeRequestTypeDef",
    {
        "ZipFile": Union[bytes, IO[bytes], StreamingBody],
        "S3Bucket": str,
        "S3Key": str,
        "S3ObjectVersion": str,
        "ImageUri": str,
        "Publish": bool,
        "DryRun": bool,
        "RevisionId": str,
    },
    total=False,
)


class UpdateFunctionCodeRequestTypeDef(
    _RequiredUpdateFunctionCodeRequestTypeDef, _OptionalUpdateFunctionCodeRequestTypeDef
):
    pass


_RequiredUpdateFunctionConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateFunctionConfigurationRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalUpdateFunctionConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateFunctionConfigurationRequestTypeDef",
    {
        "Role": str,
        "Handler": str,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "VpcConfig": "VpcConfigTypeDef",
        "Environment": "EnvironmentTypeDef",
        "Runtime": RuntimeType,
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "KMSKeyArn": str,
        "TracingConfig": "TracingConfigTypeDef",
        "RevisionId": str,
        "Layers": List[str],
        "FileSystemConfigs": List["FileSystemConfigTypeDef"],
        "ImageConfig": "ImageConfigTypeDef",
    },
    total=False,
)


class UpdateFunctionConfigurationRequestTypeDef(
    _RequiredUpdateFunctionConfigurationRequestTypeDef,
    _OptionalUpdateFunctionConfigurationRequestTypeDef,
):
    pass


_RequiredUpdateFunctionEventInvokeConfigRequestTypeDef = TypedDict(
    "_RequiredUpdateFunctionEventInvokeConfigRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalUpdateFunctionEventInvokeConfigRequestTypeDef = TypedDict(
    "_OptionalUpdateFunctionEventInvokeConfigRequestTypeDef",
    {
        "Qualifier": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": "DestinationConfigTypeDef",
    },
    total=False,
)


class UpdateFunctionEventInvokeConfigRequestTypeDef(
    _RequiredUpdateFunctionEventInvokeConfigRequestTypeDef,
    _OptionalUpdateFunctionEventInvokeConfigRequestTypeDef,
):
    pass


VpcConfigResponseTypeDef = TypedDict(
    "VpcConfigResponseTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
        "VpcId": str,
    },
    total=False,
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
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
