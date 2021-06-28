"""
Type annotations for kms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kms.type_defs import AliasListEntryTypeDef

    data: AliasListEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AlgorithmSpecType,
    ConnectionErrorCodeTypeType,
    ConnectionStateTypeType,
    CustomerMasterKeySpecType,
    DataKeyPairSpecType,
    DataKeySpecType,
    EncryptionAlgorithmSpecType,
    ExpirationModelTypeType,
    GrantOperationType,
    KeyManagerTypeType,
    KeyStateType,
    KeyUsageTypeType,
    MessageTypeType,
    MultiRegionKeyTypeType,
    OriginTypeType,
    SigningAlgorithmSpecType,
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
    "AliasListEntryTypeDef",
    "CancelKeyDeletionRequestTypeDef",
    "CancelKeyDeletionResponseResponseTypeDef",
    "ConnectCustomKeyStoreRequestTypeDef",
    "CreateAliasRequestTypeDef",
    "CreateCustomKeyStoreRequestTypeDef",
    "CreateCustomKeyStoreResponseResponseTypeDef",
    "CreateGrantRequestTypeDef",
    "CreateGrantResponseResponseTypeDef",
    "CreateKeyRequestTypeDef",
    "CreateKeyResponseResponseTypeDef",
    "CustomKeyStoresListEntryTypeDef",
    "DecryptRequestTypeDef",
    "DecryptResponseResponseTypeDef",
    "DeleteAliasRequestTypeDef",
    "DeleteCustomKeyStoreRequestTypeDef",
    "DeleteImportedKeyMaterialRequestTypeDef",
    "DescribeCustomKeyStoresRequestTypeDef",
    "DescribeCustomKeyStoresResponseResponseTypeDef",
    "DescribeKeyRequestTypeDef",
    "DescribeKeyResponseResponseTypeDef",
    "DisableKeyRequestTypeDef",
    "DisableKeyRotationRequestTypeDef",
    "DisconnectCustomKeyStoreRequestTypeDef",
    "EnableKeyRequestTypeDef",
    "EnableKeyRotationRequestTypeDef",
    "EncryptRequestTypeDef",
    "EncryptResponseResponseTypeDef",
    "GenerateDataKeyPairRequestTypeDef",
    "GenerateDataKeyPairResponseResponseTypeDef",
    "GenerateDataKeyPairWithoutPlaintextRequestTypeDef",
    "GenerateDataKeyPairWithoutPlaintextResponseResponseTypeDef",
    "GenerateDataKeyRequestTypeDef",
    "GenerateDataKeyResponseResponseTypeDef",
    "GenerateDataKeyWithoutPlaintextRequestTypeDef",
    "GenerateDataKeyWithoutPlaintextResponseResponseTypeDef",
    "GenerateRandomRequestTypeDef",
    "GenerateRandomResponseResponseTypeDef",
    "GetKeyPolicyRequestTypeDef",
    "GetKeyPolicyResponseResponseTypeDef",
    "GetKeyRotationStatusRequestTypeDef",
    "GetKeyRotationStatusResponseResponseTypeDef",
    "GetParametersForImportRequestTypeDef",
    "GetParametersForImportResponseResponseTypeDef",
    "GetPublicKeyRequestTypeDef",
    "GetPublicKeyResponseResponseTypeDef",
    "GrantConstraintsTypeDef",
    "GrantListEntryTypeDef",
    "ImportKeyMaterialRequestTypeDef",
    "KeyListEntryTypeDef",
    "KeyMetadataTypeDef",
    "ListAliasesRequestTypeDef",
    "ListAliasesResponseResponseTypeDef",
    "ListGrantsRequestTypeDef",
    "ListGrantsResponseResponseTypeDef",
    "ListKeyPoliciesRequestTypeDef",
    "ListKeyPoliciesResponseResponseTypeDef",
    "ListKeysRequestTypeDef",
    "ListKeysResponseResponseTypeDef",
    "ListResourceTagsRequestTypeDef",
    "ListResourceTagsResponseResponseTypeDef",
    "ListRetirableGrantsRequestTypeDef",
    "MultiRegionConfigurationTypeDef",
    "MultiRegionKeyTypeDef",
    "PaginatorConfigTypeDef",
    "PutKeyPolicyRequestTypeDef",
    "ReEncryptRequestTypeDef",
    "ReEncryptResponseResponseTypeDef",
    "ReplicateKeyRequestTypeDef",
    "ReplicateKeyResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RetireGrantRequestTypeDef",
    "RevokeGrantRequestTypeDef",
    "ScheduleKeyDeletionRequestTypeDef",
    "ScheduleKeyDeletionResponseResponseTypeDef",
    "SignRequestTypeDef",
    "SignResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAliasRequestTypeDef",
    "UpdateCustomKeyStoreRequestTypeDef",
    "UpdateKeyDescriptionRequestTypeDef",
    "UpdatePrimaryRegionRequestTypeDef",
    "VerifyRequestTypeDef",
    "VerifyResponseResponseTypeDef",
)

AliasListEntryTypeDef = TypedDict(
    "AliasListEntryTypeDef",
    {
        "AliasName": str,
        "AliasArn": str,
        "TargetKeyId": str,
        "CreationDate": datetime,
        "LastUpdatedDate": datetime,
    },
    total=False,
)

CancelKeyDeletionRequestTypeDef = TypedDict(
    "CancelKeyDeletionRequestTypeDef",
    {
        "KeyId": str,
    },
)

CancelKeyDeletionResponseResponseTypeDef = TypedDict(
    "CancelKeyDeletionResponseResponseTypeDef",
    {
        "KeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConnectCustomKeyStoreRequestTypeDef = TypedDict(
    "ConnectCustomKeyStoreRequestTypeDef",
    {
        "CustomKeyStoreId": str,
    },
)

CreateAliasRequestTypeDef = TypedDict(
    "CreateAliasRequestTypeDef",
    {
        "AliasName": str,
        "TargetKeyId": str,
    },
)

CreateCustomKeyStoreRequestTypeDef = TypedDict(
    "CreateCustomKeyStoreRequestTypeDef",
    {
        "CustomKeyStoreName": str,
        "CloudHsmClusterId": str,
        "TrustAnchorCertificate": str,
        "KeyStorePassword": str,
    },
)

CreateCustomKeyStoreResponseResponseTypeDef = TypedDict(
    "CreateCustomKeyStoreResponseResponseTypeDef",
    {
        "CustomKeyStoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGrantRequestTypeDef = TypedDict(
    "_RequiredCreateGrantRequestTypeDef",
    {
        "KeyId": str,
        "GranteePrincipal": str,
        "Operations": List[GrantOperationType],
    },
)
_OptionalCreateGrantRequestTypeDef = TypedDict(
    "_OptionalCreateGrantRequestTypeDef",
    {
        "RetiringPrincipal": str,
        "Constraints": "GrantConstraintsTypeDef",
        "GrantTokens": List[str],
        "Name": str,
    },
    total=False,
)


class CreateGrantRequestTypeDef(
    _RequiredCreateGrantRequestTypeDef, _OptionalCreateGrantRequestTypeDef
):
    pass


CreateGrantResponseResponseTypeDef = TypedDict(
    "CreateGrantResponseResponseTypeDef",
    {
        "GrantToken": str,
        "GrantId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKeyRequestTypeDef = TypedDict(
    "CreateKeyRequestTypeDef",
    {
        "Policy": str,
        "Description": str,
        "KeyUsage": KeyUsageTypeType,
        "CustomerMasterKeySpec": CustomerMasterKeySpecType,
        "Origin": OriginTypeType,
        "CustomKeyStoreId": str,
        "BypassPolicyLockoutSafetyCheck": bool,
        "Tags": List["TagTypeDef"],
        "MultiRegion": bool,
    },
    total=False,
)

CreateKeyResponseResponseTypeDef = TypedDict(
    "CreateKeyResponseResponseTypeDef",
    {
        "KeyMetadata": "KeyMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomKeyStoresListEntryTypeDef = TypedDict(
    "CustomKeyStoresListEntryTypeDef",
    {
        "CustomKeyStoreId": str,
        "CustomKeyStoreName": str,
        "CloudHsmClusterId": str,
        "TrustAnchorCertificate": str,
        "ConnectionState": ConnectionStateTypeType,
        "ConnectionErrorCode": ConnectionErrorCodeTypeType,
        "CreationDate": datetime,
    },
    total=False,
)

_RequiredDecryptRequestTypeDef = TypedDict(
    "_RequiredDecryptRequestTypeDef",
    {
        "CiphertextBlob": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalDecryptRequestTypeDef = TypedDict(
    "_OptionalDecryptRequestTypeDef",
    {
        "EncryptionContext": Dict[str, str],
        "GrantTokens": List[str],
        "KeyId": str,
        "EncryptionAlgorithm": EncryptionAlgorithmSpecType,
    },
    total=False,
)


class DecryptRequestTypeDef(_RequiredDecryptRequestTypeDef, _OptionalDecryptRequestTypeDef):
    pass


DecryptResponseResponseTypeDef = TypedDict(
    "DecryptResponseResponseTypeDef",
    {
        "KeyId": str,
        "Plaintext": bytes,
        "EncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAliasRequestTypeDef = TypedDict(
    "DeleteAliasRequestTypeDef",
    {
        "AliasName": str,
    },
)

DeleteCustomKeyStoreRequestTypeDef = TypedDict(
    "DeleteCustomKeyStoreRequestTypeDef",
    {
        "CustomKeyStoreId": str,
    },
)

DeleteImportedKeyMaterialRequestTypeDef = TypedDict(
    "DeleteImportedKeyMaterialRequestTypeDef",
    {
        "KeyId": str,
    },
)

DescribeCustomKeyStoresRequestTypeDef = TypedDict(
    "DescribeCustomKeyStoresRequestTypeDef",
    {
        "CustomKeyStoreId": str,
        "CustomKeyStoreName": str,
        "Limit": int,
        "Marker": str,
    },
    total=False,
)

DescribeCustomKeyStoresResponseResponseTypeDef = TypedDict(
    "DescribeCustomKeyStoresResponseResponseTypeDef",
    {
        "CustomKeyStores": List["CustomKeyStoresListEntryTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeKeyRequestTypeDef = TypedDict(
    "_RequiredDescribeKeyRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalDescribeKeyRequestTypeDef = TypedDict(
    "_OptionalDescribeKeyRequestTypeDef",
    {
        "GrantTokens": List[str],
    },
    total=False,
)


class DescribeKeyRequestTypeDef(
    _RequiredDescribeKeyRequestTypeDef, _OptionalDescribeKeyRequestTypeDef
):
    pass


DescribeKeyResponseResponseTypeDef = TypedDict(
    "DescribeKeyResponseResponseTypeDef",
    {
        "KeyMetadata": "KeyMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableKeyRequestTypeDef = TypedDict(
    "DisableKeyRequestTypeDef",
    {
        "KeyId": str,
    },
)

DisableKeyRotationRequestTypeDef = TypedDict(
    "DisableKeyRotationRequestTypeDef",
    {
        "KeyId": str,
    },
)

DisconnectCustomKeyStoreRequestTypeDef = TypedDict(
    "DisconnectCustomKeyStoreRequestTypeDef",
    {
        "CustomKeyStoreId": str,
    },
)

EnableKeyRequestTypeDef = TypedDict(
    "EnableKeyRequestTypeDef",
    {
        "KeyId": str,
    },
)

EnableKeyRotationRequestTypeDef = TypedDict(
    "EnableKeyRotationRequestTypeDef",
    {
        "KeyId": str,
    },
)

_RequiredEncryptRequestTypeDef = TypedDict(
    "_RequiredEncryptRequestTypeDef",
    {
        "KeyId": str,
        "Plaintext": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalEncryptRequestTypeDef = TypedDict(
    "_OptionalEncryptRequestTypeDef",
    {
        "EncryptionContext": Dict[str, str],
        "GrantTokens": List[str],
        "EncryptionAlgorithm": EncryptionAlgorithmSpecType,
    },
    total=False,
)


class EncryptRequestTypeDef(_RequiredEncryptRequestTypeDef, _OptionalEncryptRequestTypeDef):
    pass


EncryptResponseResponseTypeDef = TypedDict(
    "EncryptResponseResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "KeyId": str,
        "EncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGenerateDataKeyPairRequestTypeDef = TypedDict(
    "_RequiredGenerateDataKeyPairRequestTypeDef",
    {
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpecType,
    },
)
_OptionalGenerateDataKeyPairRequestTypeDef = TypedDict(
    "_OptionalGenerateDataKeyPairRequestTypeDef",
    {
        "EncryptionContext": Dict[str, str],
        "GrantTokens": List[str],
    },
    total=False,
)


class GenerateDataKeyPairRequestTypeDef(
    _RequiredGenerateDataKeyPairRequestTypeDef, _OptionalGenerateDataKeyPairRequestTypeDef
):
    pass


GenerateDataKeyPairResponseResponseTypeDef = TypedDict(
    "GenerateDataKeyPairResponseResponseTypeDef",
    {
        "PrivateKeyCiphertextBlob": bytes,
        "PrivateKeyPlaintext": bytes,
        "PublicKey": bytes,
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGenerateDataKeyPairWithoutPlaintextRequestTypeDef = TypedDict(
    "_RequiredGenerateDataKeyPairWithoutPlaintextRequestTypeDef",
    {
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpecType,
    },
)
_OptionalGenerateDataKeyPairWithoutPlaintextRequestTypeDef = TypedDict(
    "_OptionalGenerateDataKeyPairWithoutPlaintextRequestTypeDef",
    {
        "EncryptionContext": Dict[str, str],
        "GrantTokens": List[str],
    },
    total=False,
)


class GenerateDataKeyPairWithoutPlaintextRequestTypeDef(
    _RequiredGenerateDataKeyPairWithoutPlaintextRequestTypeDef,
    _OptionalGenerateDataKeyPairWithoutPlaintextRequestTypeDef,
):
    pass


GenerateDataKeyPairWithoutPlaintextResponseResponseTypeDef = TypedDict(
    "GenerateDataKeyPairWithoutPlaintextResponseResponseTypeDef",
    {
        "PrivateKeyCiphertextBlob": bytes,
        "PublicKey": bytes,
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGenerateDataKeyRequestTypeDef = TypedDict(
    "_RequiredGenerateDataKeyRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalGenerateDataKeyRequestTypeDef = TypedDict(
    "_OptionalGenerateDataKeyRequestTypeDef",
    {
        "EncryptionContext": Dict[str, str],
        "NumberOfBytes": int,
        "KeySpec": DataKeySpecType,
        "GrantTokens": List[str],
    },
    total=False,
)


class GenerateDataKeyRequestTypeDef(
    _RequiredGenerateDataKeyRequestTypeDef, _OptionalGenerateDataKeyRequestTypeDef
):
    pass


GenerateDataKeyResponseResponseTypeDef = TypedDict(
    "GenerateDataKeyResponseResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "Plaintext": bytes,
        "KeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGenerateDataKeyWithoutPlaintextRequestTypeDef = TypedDict(
    "_RequiredGenerateDataKeyWithoutPlaintextRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalGenerateDataKeyWithoutPlaintextRequestTypeDef = TypedDict(
    "_OptionalGenerateDataKeyWithoutPlaintextRequestTypeDef",
    {
        "EncryptionContext": Dict[str, str],
        "KeySpec": DataKeySpecType,
        "NumberOfBytes": int,
        "GrantTokens": List[str],
    },
    total=False,
)


class GenerateDataKeyWithoutPlaintextRequestTypeDef(
    _RequiredGenerateDataKeyWithoutPlaintextRequestTypeDef,
    _OptionalGenerateDataKeyWithoutPlaintextRequestTypeDef,
):
    pass


GenerateDataKeyWithoutPlaintextResponseResponseTypeDef = TypedDict(
    "GenerateDataKeyWithoutPlaintextResponseResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "KeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GenerateRandomRequestTypeDef = TypedDict(
    "GenerateRandomRequestTypeDef",
    {
        "NumberOfBytes": int,
        "CustomKeyStoreId": str,
    },
    total=False,
)

GenerateRandomResponseResponseTypeDef = TypedDict(
    "GenerateRandomResponseResponseTypeDef",
    {
        "Plaintext": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyPolicyRequestTypeDef = TypedDict(
    "GetKeyPolicyRequestTypeDef",
    {
        "KeyId": str,
        "PolicyName": str,
    },
)

GetKeyPolicyResponseResponseTypeDef = TypedDict(
    "GetKeyPolicyResponseResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyRotationStatusRequestTypeDef = TypedDict(
    "GetKeyRotationStatusRequestTypeDef",
    {
        "KeyId": str,
    },
)

GetKeyRotationStatusResponseResponseTypeDef = TypedDict(
    "GetKeyRotationStatusResponseResponseTypeDef",
    {
        "KeyRotationEnabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetParametersForImportRequestTypeDef = TypedDict(
    "GetParametersForImportRequestTypeDef",
    {
        "KeyId": str,
        "WrappingAlgorithm": AlgorithmSpecType,
        "WrappingKeySpec": Literal["RSA_2048"],
    },
)

GetParametersForImportResponseResponseTypeDef = TypedDict(
    "GetParametersForImportResponseResponseTypeDef",
    {
        "KeyId": str,
        "ImportToken": bytes,
        "PublicKey": bytes,
        "ParametersValidTo": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPublicKeyRequestTypeDef = TypedDict(
    "_RequiredGetPublicKeyRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalGetPublicKeyRequestTypeDef = TypedDict(
    "_OptionalGetPublicKeyRequestTypeDef",
    {
        "GrantTokens": List[str],
    },
    total=False,
)


class GetPublicKeyRequestTypeDef(
    _RequiredGetPublicKeyRequestTypeDef, _OptionalGetPublicKeyRequestTypeDef
):
    pass


GetPublicKeyResponseResponseTypeDef = TypedDict(
    "GetPublicKeyResponseResponseTypeDef",
    {
        "KeyId": str,
        "PublicKey": bytes,
        "CustomerMasterKeySpec": CustomerMasterKeySpecType,
        "KeyUsage": KeyUsageTypeType,
        "EncryptionAlgorithms": List[EncryptionAlgorithmSpecType],
        "SigningAlgorithms": List[SigningAlgorithmSpecType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GrantConstraintsTypeDef = TypedDict(
    "GrantConstraintsTypeDef",
    {
        "EncryptionContextSubset": Dict[str, str],
        "EncryptionContextEquals": Dict[str, str],
    },
    total=False,
)

GrantListEntryTypeDef = TypedDict(
    "GrantListEntryTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
        "Name": str,
        "CreationDate": datetime,
        "GranteePrincipal": str,
        "RetiringPrincipal": str,
        "IssuingAccount": str,
        "Operations": List[GrantOperationType],
        "Constraints": "GrantConstraintsTypeDef",
    },
    total=False,
)

_RequiredImportKeyMaterialRequestTypeDef = TypedDict(
    "_RequiredImportKeyMaterialRequestTypeDef",
    {
        "KeyId": str,
        "ImportToken": Union[bytes, IO[bytes], StreamingBody],
        "EncryptedKeyMaterial": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalImportKeyMaterialRequestTypeDef = TypedDict(
    "_OptionalImportKeyMaterialRequestTypeDef",
    {
        "ValidTo": Union[datetime, str],
        "ExpirationModel": ExpirationModelTypeType,
    },
    total=False,
)


class ImportKeyMaterialRequestTypeDef(
    _RequiredImportKeyMaterialRequestTypeDef, _OptionalImportKeyMaterialRequestTypeDef
):
    pass


KeyListEntryTypeDef = TypedDict(
    "KeyListEntryTypeDef",
    {
        "KeyId": str,
        "KeyArn": str,
    },
    total=False,
)

_RequiredKeyMetadataTypeDef = TypedDict(
    "_RequiredKeyMetadataTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalKeyMetadataTypeDef = TypedDict(
    "_OptionalKeyMetadataTypeDef",
    {
        "AWSAccountId": str,
        "Arn": str,
        "CreationDate": datetime,
        "Enabled": bool,
        "Description": str,
        "KeyUsage": KeyUsageTypeType,
        "KeyState": KeyStateType,
        "DeletionDate": datetime,
        "ValidTo": datetime,
        "Origin": OriginTypeType,
        "CustomKeyStoreId": str,
        "CloudHsmClusterId": str,
        "ExpirationModel": ExpirationModelTypeType,
        "KeyManager": KeyManagerTypeType,
        "CustomerMasterKeySpec": CustomerMasterKeySpecType,
        "EncryptionAlgorithms": List[EncryptionAlgorithmSpecType],
        "SigningAlgorithms": List[SigningAlgorithmSpecType],
        "MultiRegion": bool,
        "MultiRegionConfiguration": "MultiRegionConfigurationTypeDef",
        "PendingDeletionWindowInDays": int,
    },
    total=False,
)


class KeyMetadataTypeDef(_RequiredKeyMetadataTypeDef, _OptionalKeyMetadataTypeDef):
    pass


ListAliasesRequestTypeDef = TypedDict(
    "ListAliasesRequestTypeDef",
    {
        "KeyId": str,
        "Limit": int,
        "Marker": str,
    },
    total=False,
)

ListAliasesResponseResponseTypeDef = TypedDict(
    "ListAliasesResponseResponseTypeDef",
    {
        "Aliases": List["AliasListEntryTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGrantsRequestTypeDef = TypedDict(
    "_RequiredListGrantsRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalListGrantsRequestTypeDef = TypedDict(
    "_OptionalListGrantsRequestTypeDef",
    {
        "Limit": int,
        "Marker": str,
        "GrantId": str,
        "GranteePrincipal": str,
    },
    total=False,
)


class ListGrantsRequestTypeDef(
    _RequiredListGrantsRequestTypeDef, _OptionalListGrantsRequestTypeDef
):
    pass


ListGrantsResponseResponseTypeDef = TypedDict(
    "ListGrantsResponseResponseTypeDef",
    {
        "Grants": List["GrantListEntryTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListKeyPoliciesRequestTypeDef = TypedDict(
    "_RequiredListKeyPoliciesRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalListKeyPoliciesRequestTypeDef = TypedDict(
    "_OptionalListKeyPoliciesRequestTypeDef",
    {
        "Limit": int,
        "Marker": str,
    },
    total=False,
)


class ListKeyPoliciesRequestTypeDef(
    _RequiredListKeyPoliciesRequestTypeDef, _OptionalListKeyPoliciesRequestTypeDef
):
    pass


ListKeyPoliciesResponseResponseTypeDef = TypedDict(
    "ListKeyPoliciesResponseResponseTypeDef",
    {
        "PolicyNames": List[str],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKeysRequestTypeDef = TypedDict(
    "ListKeysRequestTypeDef",
    {
        "Limit": int,
        "Marker": str,
    },
    total=False,
)

ListKeysResponseResponseTypeDef = TypedDict(
    "ListKeysResponseResponseTypeDef",
    {
        "Keys": List["KeyListEntryTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourceTagsRequestTypeDef = TypedDict(
    "_RequiredListResourceTagsRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalListResourceTagsRequestTypeDef = TypedDict(
    "_OptionalListResourceTagsRequestTypeDef",
    {
        "Limit": int,
        "Marker": str,
    },
    total=False,
)


class ListResourceTagsRequestTypeDef(
    _RequiredListResourceTagsRequestTypeDef, _OptionalListResourceTagsRequestTypeDef
):
    pass


ListResourceTagsResponseResponseTypeDef = TypedDict(
    "ListResourceTagsResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRetirableGrantsRequestTypeDef = TypedDict(
    "_RequiredListRetirableGrantsRequestTypeDef",
    {
        "RetiringPrincipal": str,
    },
)
_OptionalListRetirableGrantsRequestTypeDef = TypedDict(
    "_OptionalListRetirableGrantsRequestTypeDef",
    {
        "Limit": int,
        "Marker": str,
    },
    total=False,
)


class ListRetirableGrantsRequestTypeDef(
    _RequiredListRetirableGrantsRequestTypeDef, _OptionalListRetirableGrantsRequestTypeDef
):
    pass


MultiRegionConfigurationTypeDef = TypedDict(
    "MultiRegionConfigurationTypeDef",
    {
        "MultiRegionKeyType": MultiRegionKeyTypeType,
        "PrimaryKey": "MultiRegionKeyTypeDef",
        "ReplicaKeys": List["MultiRegionKeyTypeDef"],
    },
    total=False,
)

MultiRegionKeyTypeDef = TypedDict(
    "MultiRegionKeyTypeDef",
    {
        "Arn": str,
        "Region": str,
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

_RequiredPutKeyPolicyRequestTypeDef = TypedDict(
    "_RequiredPutKeyPolicyRequestTypeDef",
    {
        "KeyId": str,
        "PolicyName": str,
        "Policy": str,
    },
)
_OptionalPutKeyPolicyRequestTypeDef = TypedDict(
    "_OptionalPutKeyPolicyRequestTypeDef",
    {
        "BypassPolicyLockoutSafetyCheck": bool,
    },
    total=False,
)


class PutKeyPolicyRequestTypeDef(
    _RequiredPutKeyPolicyRequestTypeDef, _OptionalPutKeyPolicyRequestTypeDef
):
    pass


_RequiredReEncryptRequestTypeDef = TypedDict(
    "_RequiredReEncryptRequestTypeDef",
    {
        "CiphertextBlob": Union[bytes, IO[bytes], StreamingBody],
        "DestinationKeyId": str,
    },
)
_OptionalReEncryptRequestTypeDef = TypedDict(
    "_OptionalReEncryptRequestTypeDef",
    {
        "SourceEncryptionContext": Dict[str, str],
        "SourceKeyId": str,
        "DestinationEncryptionContext": Dict[str, str],
        "SourceEncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "DestinationEncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "GrantTokens": List[str],
    },
    total=False,
)


class ReEncryptRequestTypeDef(_RequiredReEncryptRequestTypeDef, _OptionalReEncryptRequestTypeDef):
    pass


ReEncryptResponseResponseTypeDef = TypedDict(
    "ReEncryptResponseResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "SourceKeyId": str,
        "KeyId": str,
        "SourceEncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "DestinationEncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReplicateKeyRequestTypeDef = TypedDict(
    "_RequiredReplicateKeyRequestTypeDef",
    {
        "KeyId": str,
        "ReplicaRegion": str,
    },
)
_OptionalReplicateKeyRequestTypeDef = TypedDict(
    "_OptionalReplicateKeyRequestTypeDef",
    {
        "Policy": str,
        "BypassPolicyLockoutSafetyCheck": bool,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class ReplicateKeyRequestTypeDef(
    _RequiredReplicateKeyRequestTypeDef, _OptionalReplicateKeyRequestTypeDef
):
    pass


ReplicateKeyResponseResponseTypeDef = TypedDict(
    "ReplicateKeyResponseResponseTypeDef",
    {
        "ReplicaKeyMetadata": "KeyMetadataTypeDef",
        "ReplicaPolicy": str,
        "ReplicaTags": List["TagTypeDef"],
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

RetireGrantRequestTypeDef = TypedDict(
    "RetireGrantRequestTypeDef",
    {
        "GrantToken": str,
        "KeyId": str,
        "GrantId": str,
    },
    total=False,
)

RevokeGrantRequestTypeDef = TypedDict(
    "RevokeGrantRequestTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
    },
)

_RequiredScheduleKeyDeletionRequestTypeDef = TypedDict(
    "_RequiredScheduleKeyDeletionRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalScheduleKeyDeletionRequestTypeDef = TypedDict(
    "_OptionalScheduleKeyDeletionRequestTypeDef",
    {
        "PendingWindowInDays": int,
    },
    total=False,
)


class ScheduleKeyDeletionRequestTypeDef(
    _RequiredScheduleKeyDeletionRequestTypeDef, _OptionalScheduleKeyDeletionRequestTypeDef
):
    pass


ScheduleKeyDeletionResponseResponseTypeDef = TypedDict(
    "ScheduleKeyDeletionResponseResponseTypeDef",
    {
        "KeyId": str,
        "DeletionDate": datetime,
        "KeyState": KeyStateType,
        "PendingWindowInDays": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSignRequestTypeDef = TypedDict(
    "_RequiredSignRequestTypeDef",
    {
        "KeyId": str,
        "Message": Union[bytes, IO[bytes], StreamingBody],
        "SigningAlgorithm": SigningAlgorithmSpecType,
    },
)
_OptionalSignRequestTypeDef = TypedDict(
    "_OptionalSignRequestTypeDef",
    {
        "MessageType": MessageTypeType,
        "GrantTokens": List[str],
    },
    total=False,
)


class SignRequestTypeDef(_RequiredSignRequestTypeDef, _OptionalSignRequestTypeDef):
    pass


SignResponseResponseTypeDef = TypedDict(
    "SignResponseResponseTypeDef",
    {
        "KeyId": str,
        "Signature": bytes,
        "SigningAlgorithm": SigningAlgorithmSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "KeyId": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "TagKey": str,
        "TagValue": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "KeyId": str,
        "TagKeys": List[str],
    },
)

UpdateAliasRequestTypeDef = TypedDict(
    "UpdateAliasRequestTypeDef",
    {
        "AliasName": str,
        "TargetKeyId": str,
    },
)

_RequiredUpdateCustomKeyStoreRequestTypeDef = TypedDict(
    "_RequiredUpdateCustomKeyStoreRequestTypeDef",
    {
        "CustomKeyStoreId": str,
    },
)
_OptionalUpdateCustomKeyStoreRequestTypeDef = TypedDict(
    "_OptionalUpdateCustomKeyStoreRequestTypeDef",
    {
        "NewCustomKeyStoreName": str,
        "KeyStorePassword": str,
        "CloudHsmClusterId": str,
    },
    total=False,
)


class UpdateCustomKeyStoreRequestTypeDef(
    _RequiredUpdateCustomKeyStoreRequestTypeDef, _OptionalUpdateCustomKeyStoreRequestTypeDef
):
    pass


UpdateKeyDescriptionRequestTypeDef = TypedDict(
    "UpdateKeyDescriptionRequestTypeDef",
    {
        "KeyId": str,
        "Description": str,
    },
)

UpdatePrimaryRegionRequestTypeDef = TypedDict(
    "UpdatePrimaryRegionRequestTypeDef",
    {
        "KeyId": str,
        "PrimaryRegion": str,
    },
)

_RequiredVerifyRequestTypeDef = TypedDict(
    "_RequiredVerifyRequestTypeDef",
    {
        "KeyId": str,
        "Message": Union[bytes, IO[bytes], StreamingBody],
        "Signature": Union[bytes, IO[bytes], StreamingBody],
        "SigningAlgorithm": SigningAlgorithmSpecType,
    },
)
_OptionalVerifyRequestTypeDef = TypedDict(
    "_OptionalVerifyRequestTypeDef",
    {
        "MessageType": MessageTypeType,
        "GrantTokens": List[str],
    },
    total=False,
)


class VerifyRequestTypeDef(_RequiredVerifyRequestTypeDef, _OptionalVerifyRequestTypeDef):
    pass


VerifyResponseResponseTypeDef = TypedDict(
    "VerifyResponseResponseTypeDef",
    {
        "KeyId": str,
        "SignatureValid": bool,
        "SigningAlgorithm": SigningAlgorithmSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
