"""
Type annotations for sso-admin service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sso_admin.type_defs import AccessControlAttributeTypeDef

    data: AccessControlAttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    InstanceAccessControlAttributeConfigurationStatusType,
    PrincipalTypeType,
    ProvisioningStatusType,
    ProvisionTargetTypeType,
    StatusValuesType,
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
    "AccessControlAttributeTypeDef",
    "AccessControlAttributeValueTypeDef",
    "AccountAssignmentOperationStatusMetadataTypeDef",
    "AccountAssignmentOperationStatusTypeDef",
    "AccountAssignmentTypeDef",
    "AttachManagedPolicyToPermissionSetRequestTypeDef",
    "AttachedManagedPolicyTypeDef",
    "CreateAccountAssignmentRequestTypeDef",
    "CreateAccountAssignmentResponseResponseTypeDef",
    "CreateInstanceAccessControlAttributeConfigurationRequestTypeDef",
    "CreatePermissionSetRequestTypeDef",
    "CreatePermissionSetResponseResponseTypeDef",
    "DeleteAccountAssignmentRequestTypeDef",
    "DeleteAccountAssignmentResponseResponseTypeDef",
    "DeleteInlinePolicyFromPermissionSetRequestTypeDef",
    "DeleteInstanceAccessControlAttributeConfigurationRequestTypeDef",
    "DeletePermissionSetRequestTypeDef",
    "DescribeAccountAssignmentCreationStatusRequestTypeDef",
    "DescribeAccountAssignmentCreationStatusResponseResponseTypeDef",
    "DescribeAccountAssignmentDeletionStatusRequestTypeDef",
    "DescribeAccountAssignmentDeletionStatusResponseResponseTypeDef",
    "DescribeInstanceAccessControlAttributeConfigurationRequestTypeDef",
    "DescribeInstanceAccessControlAttributeConfigurationResponseResponseTypeDef",
    "DescribePermissionSetProvisioningStatusRequestTypeDef",
    "DescribePermissionSetProvisioningStatusResponseResponseTypeDef",
    "DescribePermissionSetRequestTypeDef",
    "DescribePermissionSetResponseResponseTypeDef",
    "DetachManagedPolicyFromPermissionSetRequestTypeDef",
    "GetInlinePolicyForPermissionSetRequestTypeDef",
    "GetInlinePolicyForPermissionSetResponseResponseTypeDef",
    "InstanceAccessControlAttributeConfigurationTypeDef",
    "InstanceMetadataTypeDef",
    "ListAccountAssignmentCreationStatusRequestTypeDef",
    "ListAccountAssignmentCreationStatusResponseResponseTypeDef",
    "ListAccountAssignmentDeletionStatusRequestTypeDef",
    "ListAccountAssignmentDeletionStatusResponseResponseTypeDef",
    "ListAccountAssignmentsRequestTypeDef",
    "ListAccountAssignmentsResponseResponseTypeDef",
    "ListAccountsForProvisionedPermissionSetRequestTypeDef",
    "ListAccountsForProvisionedPermissionSetResponseResponseTypeDef",
    "ListInstancesRequestTypeDef",
    "ListInstancesResponseResponseTypeDef",
    "ListManagedPoliciesInPermissionSetRequestTypeDef",
    "ListManagedPoliciesInPermissionSetResponseResponseTypeDef",
    "ListPermissionSetProvisioningStatusRequestTypeDef",
    "ListPermissionSetProvisioningStatusResponseResponseTypeDef",
    "ListPermissionSetsProvisionedToAccountRequestTypeDef",
    "ListPermissionSetsProvisionedToAccountResponseResponseTypeDef",
    "ListPermissionSetsRequestTypeDef",
    "ListPermissionSetsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "OperationStatusFilterTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionSetProvisioningStatusMetadataTypeDef",
    "PermissionSetProvisioningStatusTypeDef",
    "PermissionSetTypeDef",
    "ProvisionPermissionSetRequestTypeDef",
    "ProvisionPermissionSetResponseResponseTypeDef",
    "PutInlinePolicyToPermissionSetRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateInstanceAccessControlAttributeConfigurationRequestTypeDef",
    "UpdatePermissionSetRequestTypeDef",
)

AccessControlAttributeTypeDef = TypedDict(
    "AccessControlAttributeTypeDef",
    {
        "Key": str,
        "Value": "AccessControlAttributeValueTypeDef",
    },
)

AccessControlAttributeValueTypeDef = TypedDict(
    "AccessControlAttributeValueTypeDef",
    {
        "Source": List[str],
    },
)

AccountAssignmentOperationStatusMetadataTypeDef = TypedDict(
    "AccountAssignmentOperationStatusMetadataTypeDef",
    {
        "Status": StatusValuesType,
        "RequestId": str,
        "CreatedDate": datetime,
    },
    total=False,
)

AccountAssignmentOperationStatusTypeDef = TypedDict(
    "AccountAssignmentOperationStatusTypeDef",
    {
        "Status": StatusValuesType,
        "RequestId": str,
        "FailureReason": str,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
        "PermissionSetArn": str,
        "PrincipalType": PrincipalTypeType,
        "PrincipalId": str,
        "CreatedDate": datetime,
    },
    total=False,
)

AccountAssignmentTypeDef = TypedDict(
    "AccountAssignmentTypeDef",
    {
        "AccountId": str,
        "PermissionSetArn": str,
        "PrincipalType": PrincipalTypeType,
        "PrincipalId": str,
    },
    total=False,
)

AttachManagedPolicyToPermissionSetRequestTypeDef = TypedDict(
    "AttachManagedPolicyToPermissionSetRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "ManagedPolicyArn": str,
    },
)

AttachedManagedPolicyTypeDef = TypedDict(
    "AttachedManagedPolicyTypeDef",
    {
        "Name": str,
        "Arn": str,
    },
    total=False,
)

CreateAccountAssignmentRequestTypeDef = TypedDict(
    "CreateAccountAssignmentRequestTypeDef",
    {
        "InstanceArn": str,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
        "PermissionSetArn": str,
        "PrincipalType": PrincipalTypeType,
        "PrincipalId": str,
    },
)

CreateAccountAssignmentResponseResponseTypeDef = TypedDict(
    "CreateAccountAssignmentResponseResponseTypeDef",
    {
        "AccountAssignmentCreationStatus": "AccountAssignmentOperationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstanceAccessControlAttributeConfigurationRequestTypeDef = TypedDict(
    "CreateInstanceAccessControlAttributeConfigurationRequestTypeDef",
    {
        "InstanceArn": str,
        "InstanceAccessControlAttributeConfiguration": "InstanceAccessControlAttributeConfigurationTypeDef",
    },
)

_RequiredCreatePermissionSetRequestTypeDef = TypedDict(
    "_RequiredCreatePermissionSetRequestTypeDef",
    {
        "Name": str,
        "InstanceArn": str,
    },
)
_OptionalCreatePermissionSetRequestTypeDef = TypedDict(
    "_OptionalCreatePermissionSetRequestTypeDef",
    {
        "Description": str,
        "SessionDuration": str,
        "RelayState": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreatePermissionSetRequestTypeDef(
    _RequiredCreatePermissionSetRequestTypeDef, _OptionalCreatePermissionSetRequestTypeDef
):
    pass


CreatePermissionSetResponseResponseTypeDef = TypedDict(
    "CreatePermissionSetResponseResponseTypeDef",
    {
        "PermissionSet": "PermissionSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAccountAssignmentRequestTypeDef = TypedDict(
    "DeleteAccountAssignmentRequestTypeDef",
    {
        "InstanceArn": str,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
        "PermissionSetArn": str,
        "PrincipalType": PrincipalTypeType,
        "PrincipalId": str,
    },
)

DeleteAccountAssignmentResponseResponseTypeDef = TypedDict(
    "DeleteAccountAssignmentResponseResponseTypeDef",
    {
        "AccountAssignmentDeletionStatus": "AccountAssignmentOperationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInlinePolicyFromPermissionSetRequestTypeDef = TypedDict(
    "DeleteInlinePolicyFromPermissionSetRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

DeleteInstanceAccessControlAttributeConfigurationRequestTypeDef = TypedDict(
    "DeleteInstanceAccessControlAttributeConfigurationRequestTypeDef",
    {
        "InstanceArn": str,
    },
)

DeletePermissionSetRequestTypeDef = TypedDict(
    "DeletePermissionSetRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

DescribeAccountAssignmentCreationStatusRequestTypeDef = TypedDict(
    "DescribeAccountAssignmentCreationStatusRequestTypeDef",
    {
        "InstanceArn": str,
        "AccountAssignmentCreationRequestId": str,
    },
)

DescribeAccountAssignmentCreationStatusResponseResponseTypeDef = TypedDict(
    "DescribeAccountAssignmentCreationStatusResponseResponseTypeDef",
    {
        "AccountAssignmentCreationStatus": "AccountAssignmentOperationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountAssignmentDeletionStatusRequestTypeDef = TypedDict(
    "DescribeAccountAssignmentDeletionStatusRequestTypeDef",
    {
        "InstanceArn": str,
        "AccountAssignmentDeletionRequestId": str,
    },
)

DescribeAccountAssignmentDeletionStatusResponseResponseTypeDef = TypedDict(
    "DescribeAccountAssignmentDeletionStatusResponseResponseTypeDef",
    {
        "AccountAssignmentDeletionStatus": "AccountAssignmentOperationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceAccessControlAttributeConfigurationRequestTypeDef = TypedDict(
    "DescribeInstanceAccessControlAttributeConfigurationRequestTypeDef",
    {
        "InstanceArn": str,
    },
)

DescribeInstanceAccessControlAttributeConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeInstanceAccessControlAttributeConfigurationResponseResponseTypeDef",
    {
        "Status": InstanceAccessControlAttributeConfigurationStatusType,
        "StatusReason": str,
        "InstanceAccessControlAttributeConfiguration": "InstanceAccessControlAttributeConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePermissionSetProvisioningStatusRequestTypeDef = TypedDict(
    "DescribePermissionSetProvisioningStatusRequestTypeDef",
    {
        "InstanceArn": str,
        "ProvisionPermissionSetRequestId": str,
    },
)

DescribePermissionSetProvisioningStatusResponseResponseTypeDef = TypedDict(
    "DescribePermissionSetProvisioningStatusResponseResponseTypeDef",
    {
        "PermissionSetProvisioningStatus": "PermissionSetProvisioningStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePermissionSetRequestTypeDef = TypedDict(
    "DescribePermissionSetRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

DescribePermissionSetResponseResponseTypeDef = TypedDict(
    "DescribePermissionSetResponseResponseTypeDef",
    {
        "PermissionSet": "PermissionSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachManagedPolicyFromPermissionSetRequestTypeDef = TypedDict(
    "DetachManagedPolicyFromPermissionSetRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "ManagedPolicyArn": str,
    },
)

GetInlinePolicyForPermissionSetRequestTypeDef = TypedDict(
    "GetInlinePolicyForPermissionSetRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

GetInlinePolicyForPermissionSetResponseResponseTypeDef = TypedDict(
    "GetInlinePolicyForPermissionSetResponseResponseTypeDef",
    {
        "InlinePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceAccessControlAttributeConfigurationTypeDef = TypedDict(
    "InstanceAccessControlAttributeConfigurationTypeDef",
    {
        "AccessControlAttributes": List["AccessControlAttributeTypeDef"],
    },
)

InstanceMetadataTypeDef = TypedDict(
    "InstanceMetadataTypeDef",
    {
        "InstanceArn": str,
        "IdentityStoreId": str,
    },
    total=False,
)

_RequiredListAccountAssignmentCreationStatusRequestTypeDef = TypedDict(
    "_RequiredListAccountAssignmentCreationStatusRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
_OptionalListAccountAssignmentCreationStatusRequestTypeDef = TypedDict(
    "_OptionalListAccountAssignmentCreationStatusRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filter": "OperationStatusFilterTypeDef",
    },
    total=False,
)


class ListAccountAssignmentCreationStatusRequestTypeDef(
    _RequiredListAccountAssignmentCreationStatusRequestTypeDef,
    _OptionalListAccountAssignmentCreationStatusRequestTypeDef,
):
    pass


ListAccountAssignmentCreationStatusResponseResponseTypeDef = TypedDict(
    "ListAccountAssignmentCreationStatusResponseResponseTypeDef",
    {
        "AccountAssignmentsCreationStatus": List["AccountAssignmentOperationStatusMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccountAssignmentDeletionStatusRequestTypeDef = TypedDict(
    "_RequiredListAccountAssignmentDeletionStatusRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
_OptionalListAccountAssignmentDeletionStatusRequestTypeDef = TypedDict(
    "_OptionalListAccountAssignmentDeletionStatusRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filter": "OperationStatusFilterTypeDef",
    },
    total=False,
)


class ListAccountAssignmentDeletionStatusRequestTypeDef(
    _RequiredListAccountAssignmentDeletionStatusRequestTypeDef,
    _OptionalListAccountAssignmentDeletionStatusRequestTypeDef,
):
    pass


ListAccountAssignmentDeletionStatusResponseResponseTypeDef = TypedDict(
    "ListAccountAssignmentDeletionStatusResponseResponseTypeDef",
    {
        "AccountAssignmentsDeletionStatus": List["AccountAssignmentOperationStatusMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccountAssignmentsRequestTypeDef = TypedDict(
    "_RequiredListAccountAssignmentsRequestTypeDef",
    {
        "InstanceArn": str,
        "AccountId": str,
        "PermissionSetArn": str,
    },
)
_OptionalListAccountAssignmentsRequestTypeDef = TypedDict(
    "_OptionalListAccountAssignmentsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListAccountAssignmentsRequestTypeDef(
    _RequiredListAccountAssignmentsRequestTypeDef, _OptionalListAccountAssignmentsRequestTypeDef
):
    pass


ListAccountAssignmentsResponseResponseTypeDef = TypedDict(
    "ListAccountAssignmentsResponseResponseTypeDef",
    {
        "AccountAssignments": List["AccountAssignmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccountsForProvisionedPermissionSetRequestTypeDef = TypedDict(
    "_RequiredListAccountsForProvisionedPermissionSetRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
_OptionalListAccountsForProvisionedPermissionSetRequestTypeDef = TypedDict(
    "_OptionalListAccountsForProvisionedPermissionSetRequestTypeDef",
    {
        "ProvisioningStatus": ProvisioningStatusType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListAccountsForProvisionedPermissionSetRequestTypeDef(
    _RequiredListAccountsForProvisionedPermissionSetRequestTypeDef,
    _OptionalListAccountsForProvisionedPermissionSetRequestTypeDef,
):
    pass


ListAccountsForProvisionedPermissionSetResponseResponseTypeDef = TypedDict(
    "ListAccountsForProvisionedPermissionSetResponseResponseTypeDef",
    {
        "AccountIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstancesRequestTypeDef = TypedDict(
    "ListInstancesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListInstancesResponseResponseTypeDef = TypedDict(
    "ListInstancesResponseResponseTypeDef",
    {
        "Instances": List["InstanceMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListManagedPoliciesInPermissionSetRequestTypeDef = TypedDict(
    "_RequiredListManagedPoliciesInPermissionSetRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
_OptionalListManagedPoliciesInPermissionSetRequestTypeDef = TypedDict(
    "_OptionalListManagedPoliciesInPermissionSetRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListManagedPoliciesInPermissionSetRequestTypeDef(
    _RequiredListManagedPoliciesInPermissionSetRequestTypeDef,
    _OptionalListManagedPoliciesInPermissionSetRequestTypeDef,
):
    pass


ListManagedPoliciesInPermissionSetResponseResponseTypeDef = TypedDict(
    "ListManagedPoliciesInPermissionSetResponseResponseTypeDef",
    {
        "AttachedManagedPolicies": List["AttachedManagedPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPermissionSetProvisioningStatusRequestTypeDef = TypedDict(
    "_RequiredListPermissionSetProvisioningStatusRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
_OptionalListPermissionSetProvisioningStatusRequestTypeDef = TypedDict(
    "_OptionalListPermissionSetProvisioningStatusRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filter": "OperationStatusFilterTypeDef",
    },
    total=False,
)


class ListPermissionSetProvisioningStatusRequestTypeDef(
    _RequiredListPermissionSetProvisioningStatusRequestTypeDef,
    _OptionalListPermissionSetProvisioningStatusRequestTypeDef,
):
    pass


ListPermissionSetProvisioningStatusResponseResponseTypeDef = TypedDict(
    "ListPermissionSetProvisioningStatusResponseResponseTypeDef",
    {
        "PermissionSetsProvisioningStatus": List["PermissionSetProvisioningStatusMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPermissionSetsProvisionedToAccountRequestTypeDef = TypedDict(
    "_RequiredListPermissionSetsProvisionedToAccountRequestTypeDef",
    {
        "InstanceArn": str,
        "AccountId": str,
    },
)
_OptionalListPermissionSetsProvisionedToAccountRequestTypeDef = TypedDict(
    "_OptionalListPermissionSetsProvisionedToAccountRequestTypeDef",
    {
        "ProvisioningStatus": ProvisioningStatusType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListPermissionSetsProvisionedToAccountRequestTypeDef(
    _RequiredListPermissionSetsProvisionedToAccountRequestTypeDef,
    _OptionalListPermissionSetsProvisionedToAccountRequestTypeDef,
):
    pass


ListPermissionSetsProvisionedToAccountResponseResponseTypeDef = TypedDict(
    "ListPermissionSetsProvisionedToAccountResponseResponseTypeDef",
    {
        "NextToken": str,
        "PermissionSets": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPermissionSetsRequestTypeDef = TypedDict(
    "_RequiredListPermissionSetsRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
_OptionalListPermissionSetsRequestTypeDef = TypedDict(
    "_OptionalListPermissionSetsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListPermissionSetsRequestTypeDef(
    _RequiredListPermissionSetsRequestTypeDef, _OptionalListPermissionSetsRequestTypeDef
):
    pass


ListPermissionSetsResponseResponseTypeDef = TypedDict(
    "ListPermissionSetsResponseResponseTypeDef",
    {
        "PermissionSets": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestTypeDef",
    {
        "InstanceArn": str,
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListTagsForResourceRequestTypeDef(
    _RequiredListTagsForResourceRequestTypeDef, _OptionalListTagsForResourceRequestTypeDef
):
    pass


ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OperationStatusFilterTypeDef = TypedDict(
    "OperationStatusFilterTypeDef",
    {
        "Status": StatusValuesType,
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

PermissionSetProvisioningStatusMetadataTypeDef = TypedDict(
    "PermissionSetProvisioningStatusMetadataTypeDef",
    {
        "Status": StatusValuesType,
        "RequestId": str,
        "CreatedDate": datetime,
    },
    total=False,
)

PermissionSetProvisioningStatusTypeDef = TypedDict(
    "PermissionSetProvisioningStatusTypeDef",
    {
        "Status": StatusValuesType,
        "RequestId": str,
        "AccountId": str,
        "PermissionSetArn": str,
        "FailureReason": str,
        "CreatedDate": datetime,
    },
    total=False,
)

PermissionSetTypeDef = TypedDict(
    "PermissionSetTypeDef",
    {
        "Name": str,
        "PermissionSetArn": str,
        "Description": str,
        "CreatedDate": datetime,
        "SessionDuration": str,
        "RelayState": str,
    },
    total=False,
)

_RequiredProvisionPermissionSetRequestTypeDef = TypedDict(
    "_RequiredProvisionPermissionSetRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "TargetType": ProvisionTargetTypeType,
    },
)
_OptionalProvisionPermissionSetRequestTypeDef = TypedDict(
    "_OptionalProvisionPermissionSetRequestTypeDef",
    {
        "TargetId": str,
    },
    total=False,
)


class ProvisionPermissionSetRequestTypeDef(
    _RequiredProvisionPermissionSetRequestTypeDef, _OptionalProvisionPermissionSetRequestTypeDef
):
    pass


ProvisionPermissionSetResponseResponseTypeDef = TypedDict(
    "ProvisionPermissionSetResponseResponseTypeDef",
    {
        "PermissionSetProvisioningStatus": "PermissionSetProvisioningStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutInlinePolicyToPermissionSetRequestTypeDef = TypedDict(
    "PutInlinePolicyToPermissionSetRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "InlinePolicy": str,
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "InstanceArn": str,
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
        "InstanceArn": str,
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateInstanceAccessControlAttributeConfigurationRequestTypeDef = TypedDict(
    "UpdateInstanceAccessControlAttributeConfigurationRequestTypeDef",
    {
        "InstanceArn": str,
        "InstanceAccessControlAttributeConfiguration": "InstanceAccessControlAttributeConfigurationTypeDef",
    },
)

_RequiredUpdatePermissionSetRequestTypeDef = TypedDict(
    "_RequiredUpdatePermissionSetRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
_OptionalUpdatePermissionSetRequestTypeDef = TypedDict(
    "_OptionalUpdatePermissionSetRequestTypeDef",
    {
        "Description": str,
        "SessionDuration": str,
        "RelayState": str,
    },
    total=False,
)


class UpdatePermissionSetRequestTypeDef(
    _RequiredUpdatePermissionSetRequestTypeDef, _OptionalUpdatePermissionSetRequestTypeDef
):
    pass
