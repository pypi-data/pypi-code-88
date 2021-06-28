"""
Type annotations for secretsmanager service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/type_defs.html)

Usage::

    ```python
    from mypy_boto3_secretsmanager.type_defs import CancelRotateSecretRequestTypeDef

    data: CancelRotateSecretRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import FilterNameStringTypeType, SortOrderTypeType, StatusTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelRotateSecretRequestTypeDef",
    "CancelRotateSecretResponseResponseTypeDef",
    "CreateSecretRequestTypeDef",
    "CreateSecretResponseResponseTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteResourcePolicyResponseResponseTypeDef",
    "DeleteSecretRequestTypeDef",
    "DeleteSecretResponseResponseTypeDef",
    "DescribeSecretRequestTypeDef",
    "DescribeSecretResponseResponseTypeDef",
    "FilterTypeDef",
    "GetRandomPasswordRequestTypeDef",
    "GetRandomPasswordResponseResponseTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResponseResponseTypeDef",
    "GetSecretValueRequestTypeDef",
    "GetSecretValueResponseResponseTypeDef",
    "ListSecretVersionIdsRequestTypeDef",
    "ListSecretVersionIdsResponseResponseTypeDef",
    "ListSecretsRequestTypeDef",
    "ListSecretsResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResponseResponseTypeDef",
    "PutSecretValueRequestTypeDef",
    "PutSecretValueResponseResponseTypeDef",
    "RemoveRegionsFromReplicationRequestTypeDef",
    "RemoveRegionsFromReplicationResponseResponseTypeDef",
    "ReplicaRegionTypeTypeDef",
    "ReplicateSecretToRegionsRequestTypeDef",
    "ReplicateSecretToRegionsResponseResponseTypeDef",
    "ReplicationStatusTypeTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreSecretRequestTypeDef",
    "RestoreSecretResponseResponseTypeDef",
    "RotateSecretRequestTypeDef",
    "RotateSecretResponseResponseTypeDef",
    "RotationRulesTypeTypeDef",
    "SecretListEntryTypeDef",
    "SecretVersionsListEntryTypeDef",
    "StopReplicationToReplicaRequestTypeDef",
    "StopReplicationToReplicaResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateSecretRequestTypeDef",
    "UpdateSecretResponseResponseTypeDef",
    "UpdateSecretVersionStageRequestTypeDef",
    "UpdateSecretVersionStageResponseResponseTypeDef",
    "ValidateResourcePolicyRequestTypeDef",
    "ValidateResourcePolicyResponseResponseTypeDef",
    "ValidationErrorsEntryTypeDef",
)

CancelRotateSecretRequestTypeDef = TypedDict(
    "CancelRotateSecretRequestTypeDef",
    {
        "SecretId": str,
    },
)

CancelRotateSecretResponseResponseTypeDef = TypedDict(
    "CancelRotateSecretResponseResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSecretRequestTypeDef = TypedDict(
    "_RequiredCreateSecretRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateSecretRequestTypeDef = TypedDict(
    "_OptionalCreateSecretRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Description": str,
        "KmsKeyId": str,
        "SecretBinary": Union[bytes, IO[bytes], StreamingBody],
        "SecretString": str,
        "Tags": List["TagTypeDef"],
        "AddReplicaRegions": List["ReplicaRegionTypeTypeDef"],
        "ForceOverwriteReplicaSecret": bool,
    },
    total=False,
)


class CreateSecretRequestTypeDef(
    _RequiredCreateSecretRequestTypeDef, _OptionalCreateSecretRequestTypeDef
):
    pass


CreateSecretResponseResponseTypeDef = TypedDict(
    "CreateSecretResponseResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "VersionId": str,
        "ReplicationStatus": List["ReplicationStatusTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestTypeDef",
    {
        "SecretId": str,
    },
)

DeleteResourcePolicyResponseResponseTypeDef = TypedDict(
    "DeleteResourcePolicyResponseResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteSecretRequestTypeDef = TypedDict(
    "_RequiredDeleteSecretRequestTypeDef",
    {
        "SecretId": str,
    },
)
_OptionalDeleteSecretRequestTypeDef = TypedDict(
    "_OptionalDeleteSecretRequestTypeDef",
    {
        "RecoveryWindowInDays": int,
        "ForceDeleteWithoutRecovery": bool,
    },
    total=False,
)


class DeleteSecretRequestTypeDef(
    _RequiredDeleteSecretRequestTypeDef, _OptionalDeleteSecretRequestTypeDef
):
    pass


DeleteSecretResponseResponseTypeDef = TypedDict(
    "DeleteSecretResponseResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "DeletionDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecretRequestTypeDef = TypedDict(
    "DescribeSecretRequestTypeDef",
    {
        "SecretId": str,
    },
)

DescribeSecretResponseResponseTypeDef = TypedDict(
    "DescribeSecretResponseResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "Description": str,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaARN": str,
        "RotationRules": "RotationRulesTypeTypeDef",
        "LastRotatedDate": datetime,
        "LastChangedDate": datetime,
        "LastAccessedDate": datetime,
        "DeletedDate": datetime,
        "Tags": List["TagTypeDef"],
        "VersionIdsToStages": Dict[str, List[str]],
        "OwningService": str,
        "CreatedDate": datetime,
        "PrimaryRegion": str,
        "ReplicationStatus": List["ReplicationStatusTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Key": FilterNameStringTypeType,
        "Values": List[str],
    },
    total=False,
)

GetRandomPasswordRequestTypeDef = TypedDict(
    "GetRandomPasswordRequestTypeDef",
    {
        "PasswordLength": int,
        "ExcludeCharacters": str,
        "ExcludeNumbers": bool,
        "ExcludePunctuation": bool,
        "ExcludeUppercase": bool,
        "ExcludeLowercase": bool,
        "IncludeSpace": bool,
        "RequireEachIncludedType": bool,
    },
    total=False,
)

GetRandomPasswordResponseResponseTypeDef = TypedDict(
    "GetRandomPasswordResponseResponseTypeDef",
    {
        "RandomPassword": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestTypeDef",
    {
        "SecretId": str,
    },
)

GetResourcePolicyResponseResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "ResourcePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSecretValueRequestTypeDef = TypedDict(
    "_RequiredGetSecretValueRequestTypeDef",
    {
        "SecretId": str,
    },
)
_OptionalGetSecretValueRequestTypeDef = TypedDict(
    "_OptionalGetSecretValueRequestTypeDef",
    {
        "VersionId": str,
        "VersionStage": str,
    },
    total=False,
)


class GetSecretValueRequestTypeDef(
    _RequiredGetSecretValueRequestTypeDef, _OptionalGetSecretValueRequestTypeDef
):
    pass


GetSecretValueResponseResponseTypeDef = TypedDict(
    "GetSecretValueResponseResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "VersionId": str,
        "SecretBinary": bytes,
        "SecretString": str,
        "VersionStages": List[str],
        "CreatedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSecretVersionIdsRequestTypeDef = TypedDict(
    "_RequiredListSecretVersionIdsRequestTypeDef",
    {
        "SecretId": str,
    },
)
_OptionalListSecretVersionIdsRequestTypeDef = TypedDict(
    "_OptionalListSecretVersionIdsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "IncludeDeprecated": bool,
    },
    total=False,
)


class ListSecretVersionIdsRequestTypeDef(
    _RequiredListSecretVersionIdsRequestTypeDef, _OptionalListSecretVersionIdsRequestTypeDef
):
    pass


ListSecretVersionIdsResponseResponseTypeDef = TypedDict(
    "ListSecretVersionIdsResponseResponseTypeDef",
    {
        "Versions": List["SecretVersionsListEntryTypeDef"],
        "NextToken": str,
        "ARN": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecretsRequestTypeDef = TypedDict(
    "ListSecretsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
        "SortOrder": SortOrderTypeType,
    },
    total=False,
)

ListSecretsResponseResponseTypeDef = TypedDict(
    "ListSecretsResponseResponseTypeDef",
    {
        "SecretList": List["SecretListEntryTypeDef"],
        "NextToken": str,
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

_RequiredPutResourcePolicyRequestTypeDef = TypedDict(
    "_RequiredPutResourcePolicyRequestTypeDef",
    {
        "SecretId": str,
        "ResourcePolicy": str,
    },
)
_OptionalPutResourcePolicyRequestTypeDef = TypedDict(
    "_OptionalPutResourcePolicyRequestTypeDef",
    {
        "BlockPublicPolicy": bool,
    },
    total=False,
)


class PutResourcePolicyRequestTypeDef(
    _RequiredPutResourcePolicyRequestTypeDef, _OptionalPutResourcePolicyRequestTypeDef
):
    pass


PutResourcePolicyResponseResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutSecretValueRequestTypeDef = TypedDict(
    "_RequiredPutSecretValueRequestTypeDef",
    {
        "SecretId": str,
    },
)
_OptionalPutSecretValueRequestTypeDef = TypedDict(
    "_OptionalPutSecretValueRequestTypeDef",
    {
        "ClientRequestToken": str,
        "SecretBinary": Union[bytes, IO[bytes], StreamingBody],
        "SecretString": str,
        "VersionStages": List[str],
    },
    total=False,
)


class PutSecretValueRequestTypeDef(
    _RequiredPutSecretValueRequestTypeDef, _OptionalPutSecretValueRequestTypeDef
):
    pass


PutSecretValueResponseResponseTypeDef = TypedDict(
    "PutSecretValueResponseResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "VersionId": str,
        "VersionStages": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveRegionsFromReplicationRequestTypeDef = TypedDict(
    "RemoveRegionsFromReplicationRequestTypeDef",
    {
        "SecretId": str,
        "RemoveReplicaRegions": List[str],
    },
)

RemoveRegionsFromReplicationResponseResponseTypeDef = TypedDict(
    "RemoveRegionsFromReplicationResponseResponseTypeDef",
    {
        "ARN": str,
        "ReplicationStatus": List["ReplicationStatusTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicaRegionTypeTypeDef = TypedDict(
    "ReplicaRegionTypeTypeDef",
    {
        "Region": str,
        "KmsKeyId": str,
    },
    total=False,
)

_RequiredReplicateSecretToRegionsRequestTypeDef = TypedDict(
    "_RequiredReplicateSecretToRegionsRequestTypeDef",
    {
        "SecretId": str,
        "AddReplicaRegions": List["ReplicaRegionTypeTypeDef"],
    },
)
_OptionalReplicateSecretToRegionsRequestTypeDef = TypedDict(
    "_OptionalReplicateSecretToRegionsRequestTypeDef",
    {
        "ForceOverwriteReplicaSecret": bool,
    },
    total=False,
)


class ReplicateSecretToRegionsRequestTypeDef(
    _RequiredReplicateSecretToRegionsRequestTypeDef, _OptionalReplicateSecretToRegionsRequestTypeDef
):
    pass


ReplicateSecretToRegionsResponseResponseTypeDef = TypedDict(
    "ReplicateSecretToRegionsResponseResponseTypeDef",
    {
        "ARN": str,
        "ReplicationStatus": List["ReplicationStatusTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicationStatusTypeTypeDef = TypedDict(
    "ReplicationStatusTypeTypeDef",
    {
        "Region": str,
        "KmsKeyId": str,
        "Status": StatusTypeType,
        "StatusMessage": str,
        "LastAccessedDate": datetime,
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

RestoreSecretRequestTypeDef = TypedDict(
    "RestoreSecretRequestTypeDef",
    {
        "SecretId": str,
    },
)

RestoreSecretResponseResponseTypeDef = TypedDict(
    "RestoreSecretResponseResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRotateSecretRequestTypeDef = TypedDict(
    "_RequiredRotateSecretRequestTypeDef",
    {
        "SecretId": str,
    },
)
_OptionalRotateSecretRequestTypeDef = TypedDict(
    "_OptionalRotateSecretRequestTypeDef",
    {
        "ClientRequestToken": str,
        "RotationLambdaARN": str,
        "RotationRules": "RotationRulesTypeTypeDef",
    },
    total=False,
)


class RotateSecretRequestTypeDef(
    _RequiredRotateSecretRequestTypeDef, _OptionalRotateSecretRequestTypeDef
):
    pass


RotateSecretResponseResponseTypeDef = TypedDict(
    "RotateSecretResponseResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RotationRulesTypeTypeDef = TypedDict(
    "RotationRulesTypeTypeDef",
    {
        "AutomaticallyAfterDays": int,
    },
    total=False,
)

SecretListEntryTypeDef = TypedDict(
    "SecretListEntryTypeDef",
    {
        "ARN": str,
        "Name": str,
        "Description": str,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaARN": str,
        "RotationRules": "RotationRulesTypeTypeDef",
        "LastRotatedDate": datetime,
        "LastChangedDate": datetime,
        "LastAccessedDate": datetime,
        "DeletedDate": datetime,
        "Tags": List["TagTypeDef"],
        "SecretVersionsToStages": Dict[str, List[str]],
        "OwningService": str,
        "CreatedDate": datetime,
        "PrimaryRegion": str,
    },
    total=False,
)

SecretVersionsListEntryTypeDef = TypedDict(
    "SecretVersionsListEntryTypeDef",
    {
        "VersionId": str,
        "VersionStages": List[str],
        "LastAccessedDate": datetime,
        "CreatedDate": datetime,
    },
    total=False,
)

StopReplicationToReplicaRequestTypeDef = TypedDict(
    "StopReplicationToReplicaRequestTypeDef",
    {
        "SecretId": str,
    },
)

StopReplicationToReplicaResponseResponseTypeDef = TypedDict(
    "StopReplicationToReplicaResponseResponseTypeDef",
    {
        "ARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "SecretId": str,
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
        "SecretId": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateSecretRequestTypeDef = TypedDict(
    "_RequiredUpdateSecretRequestTypeDef",
    {
        "SecretId": str,
    },
)
_OptionalUpdateSecretRequestTypeDef = TypedDict(
    "_OptionalUpdateSecretRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Description": str,
        "KmsKeyId": str,
        "SecretBinary": Union[bytes, IO[bytes], StreamingBody],
        "SecretString": str,
    },
    total=False,
)


class UpdateSecretRequestTypeDef(
    _RequiredUpdateSecretRequestTypeDef, _OptionalUpdateSecretRequestTypeDef
):
    pass


UpdateSecretResponseResponseTypeDef = TypedDict(
    "UpdateSecretResponseResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSecretVersionStageRequestTypeDef = TypedDict(
    "_RequiredUpdateSecretVersionStageRequestTypeDef",
    {
        "SecretId": str,
        "VersionStage": str,
    },
)
_OptionalUpdateSecretVersionStageRequestTypeDef = TypedDict(
    "_OptionalUpdateSecretVersionStageRequestTypeDef",
    {
        "RemoveFromVersionId": str,
        "MoveToVersionId": str,
    },
    total=False,
)


class UpdateSecretVersionStageRequestTypeDef(
    _RequiredUpdateSecretVersionStageRequestTypeDef, _OptionalUpdateSecretVersionStageRequestTypeDef
):
    pass


UpdateSecretVersionStageResponseResponseTypeDef = TypedDict(
    "UpdateSecretVersionStageResponseResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredValidateResourcePolicyRequestTypeDef = TypedDict(
    "_RequiredValidateResourcePolicyRequestTypeDef",
    {
        "ResourcePolicy": str,
    },
)
_OptionalValidateResourcePolicyRequestTypeDef = TypedDict(
    "_OptionalValidateResourcePolicyRequestTypeDef",
    {
        "SecretId": str,
    },
    total=False,
)


class ValidateResourcePolicyRequestTypeDef(
    _RequiredValidateResourcePolicyRequestTypeDef, _OptionalValidateResourcePolicyRequestTypeDef
):
    pass


ValidateResourcePolicyResponseResponseTypeDef = TypedDict(
    "ValidateResourcePolicyResponseResponseTypeDef",
    {
        "PolicyValidationPassed": bool,
        "ValidationErrors": List["ValidationErrorsEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidationErrorsEntryTypeDef = TypedDict(
    "ValidationErrorsEntryTypeDef",
    {
        "CheckName": str,
        "ErrorMessage": str,
    },
    total=False,
)
