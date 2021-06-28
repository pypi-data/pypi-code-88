"""
Type annotations for organizations service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/type_defs.html)

Usage::

    ```python
    from mypy_boto3_organizations.type_defs import AcceptHandshakeRequestTypeDef

    data: AcceptHandshakeRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccountJoinedMethodType,
    AccountStatusType,
    ActionTypeType,
    ChildTypeType,
    CreateAccountFailureReasonType,
    CreateAccountStateType,
    EffectivePolicyTypeType,
    HandshakePartyTypeType,
    HandshakeResourceTypeType,
    HandshakeStateType,
    IAMUserAccessToBillingType,
    OrganizationFeatureSetType,
    ParentTypeType,
    PolicyTypeStatusType,
    PolicyTypeType,
    TargetTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptHandshakeRequestTypeDef",
    "AcceptHandshakeResponseResponseTypeDef",
    "AccountTypeDef",
    "AttachPolicyRequestTypeDef",
    "CancelHandshakeRequestTypeDef",
    "CancelHandshakeResponseResponseTypeDef",
    "ChildTypeDef",
    "CreateAccountRequestTypeDef",
    "CreateAccountResponseResponseTypeDef",
    "CreateAccountStatusTypeDef",
    "CreateGovCloudAccountRequestTypeDef",
    "CreateGovCloudAccountResponseResponseTypeDef",
    "CreateOrganizationRequestTypeDef",
    "CreateOrganizationResponseResponseTypeDef",
    "CreateOrganizationalUnitRequestTypeDef",
    "CreateOrganizationalUnitResponseResponseTypeDef",
    "CreatePolicyRequestTypeDef",
    "CreatePolicyResponseResponseTypeDef",
    "DeclineHandshakeRequestTypeDef",
    "DeclineHandshakeResponseResponseTypeDef",
    "DelegatedAdministratorTypeDef",
    "DelegatedServiceTypeDef",
    "DeleteOrganizationalUnitRequestTypeDef",
    "DeletePolicyRequestTypeDef",
    "DeregisterDelegatedAdministratorRequestTypeDef",
    "DescribeAccountRequestTypeDef",
    "DescribeAccountResponseResponseTypeDef",
    "DescribeCreateAccountStatusRequestTypeDef",
    "DescribeCreateAccountStatusResponseResponseTypeDef",
    "DescribeEffectivePolicyRequestTypeDef",
    "DescribeEffectivePolicyResponseResponseTypeDef",
    "DescribeHandshakeRequestTypeDef",
    "DescribeHandshakeResponseResponseTypeDef",
    "DescribeOrganizationResponseResponseTypeDef",
    "DescribeOrganizationalUnitRequestTypeDef",
    "DescribeOrganizationalUnitResponseResponseTypeDef",
    "DescribePolicyRequestTypeDef",
    "DescribePolicyResponseResponseTypeDef",
    "DetachPolicyRequestTypeDef",
    "DisableAWSServiceAccessRequestTypeDef",
    "DisablePolicyTypeRequestTypeDef",
    "DisablePolicyTypeResponseResponseTypeDef",
    "EffectivePolicyTypeDef",
    "EnableAWSServiceAccessRequestTypeDef",
    "EnableAllFeaturesResponseResponseTypeDef",
    "EnablePolicyTypeRequestTypeDef",
    "EnablePolicyTypeResponseResponseTypeDef",
    "EnabledServicePrincipalTypeDef",
    "HandshakeFilterTypeDef",
    "HandshakePartyTypeDef",
    "HandshakeResourceTypeDef",
    "HandshakeTypeDef",
    "InviteAccountToOrganizationRequestTypeDef",
    "InviteAccountToOrganizationResponseResponseTypeDef",
    "ListAWSServiceAccessForOrganizationRequestTypeDef",
    "ListAWSServiceAccessForOrganizationResponseResponseTypeDef",
    "ListAccountsForParentRequestTypeDef",
    "ListAccountsForParentResponseResponseTypeDef",
    "ListAccountsRequestTypeDef",
    "ListAccountsResponseResponseTypeDef",
    "ListChildrenRequestTypeDef",
    "ListChildrenResponseResponseTypeDef",
    "ListCreateAccountStatusRequestTypeDef",
    "ListCreateAccountStatusResponseResponseTypeDef",
    "ListDelegatedAdministratorsRequestTypeDef",
    "ListDelegatedAdministratorsResponseResponseTypeDef",
    "ListDelegatedServicesForAccountRequestTypeDef",
    "ListDelegatedServicesForAccountResponseResponseTypeDef",
    "ListHandshakesForAccountRequestTypeDef",
    "ListHandshakesForAccountResponseResponseTypeDef",
    "ListHandshakesForOrganizationRequestTypeDef",
    "ListHandshakesForOrganizationResponseResponseTypeDef",
    "ListOrganizationalUnitsForParentRequestTypeDef",
    "ListOrganizationalUnitsForParentResponseResponseTypeDef",
    "ListParentsRequestTypeDef",
    "ListParentsResponseResponseTypeDef",
    "ListPoliciesForTargetRequestTypeDef",
    "ListPoliciesForTargetResponseResponseTypeDef",
    "ListPoliciesRequestTypeDef",
    "ListPoliciesResponseResponseTypeDef",
    "ListRootsRequestTypeDef",
    "ListRootsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTargetsForPolicyRequestTypeDef",
    "ListTargetsForPolicyResponseResponseTypeDef",
    "MoveAccountRequestTypeDef",
    "OrganizationTypeDef",
    "OrganizationalUnitTypeDef",
    "PaginatorConfigTypeDef",
    "ParentTypeDef",
    "PolicySummaryTypeDef",
    "PolicyTargetSummaryTypeDef",
    "PolicyTypeDef",
    "PolicyTypeSummaryTypeDef",
    "RegisterDelegatedAdministratorRequestTypeDef",
    "RemoveAccountFromOrganizationRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RootTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateOrganizationalUnitRequestTypeDef",
    "UpdateOrganizationalUnitResponseResponseTypeDef",
    "UpdatePolicyRequestTypeDef",
    "UpdatePolicyResponseResponseTypeDef",
)

AcceptHandshakeRequestTypeDef = TypedDict(
    "AcceptHandshakeRequestTypeDef",
    {
        "HandshakeId": str,
    },
)

AcceptHandshakeResponseResponseTypeDef = TypedDict(
    "AcceptHandshakeResponseResponseTypeDef",
    {
        "Handshake": "HandshakeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": AccountStatusType,
        "JoinedMethod": AccountJoinedMethodType,
        "JoinedTimestamp": datetime,
    },
    total=False,
)

AttachPolicyRequestTypeDef = TypedDict(
    "AttachPolicyRequestTypeDef",
    {
        "PolicyId": str,
        "TargetId": str,
    },
)

CancelHandshakeRequestTypeDef = TypedDict(
    "CancelHandshakeRequestTypeDef",
    {
        "HandshakeId": str,
    },
)

CancelHandshakeResponseResponseTypeDef = TypedDict(
    "CancelHandshakeResponseResponseTypeDef",
    {
        "Handshake": "HandshakeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChildTypeDef = TypedDict(
    "ChildTypeDef",
    {
        "Id": str,
        "Type": ChildTypeType,
    },
    total=False,
)

_RequiredCreateAccountRequestTypeDef = TypedDict(
    "_RequiredCreateAccountRequestTypeDef",
    {
        "Email": str,
        "AccountName": str,
    },
)
_OptionalCreateAccountRequestTypeDef = TypedDict(
    "_OptionalCreateAccountRequestTypeDef",
    {
        "RoleName": str,
        "IamUserAccessToBilling": IAMUserAccessToBillingType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateAccountRequestTypeDef(
    _RequiredCreateAccountRequestTypeDef, _OptionalCreateAccountRequestTypeDef
):
    pass


CreateAccountResponseResponseTypeDef = TypedDict(
    "CreateAccountResponseResponseTypeDef",
    {
        "CreateAccountStatus": "CreateAccountStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAccountStatusTypeDef = TypedDict(
    "CreateAccountStatusTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": CreateAccountStateType,
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": CreateAccountFailureReasonType,
    },
    total=False,
)

_RequiredCreateGovCloudAccountRequestTypeDef = TypedDict(
    "_RequiredCreateGovCloudAccountRequestTypeDef",
    {
        "Email": str,
        "AccountName": str,
    },
)
_OptionalCreateGovCloudAccountRequestTypeDef = TypedDict(
    "_OptionalCreateGovCloudAccountRequestTypeDef",
    {
        "RoleName": str,
        "IamUserAccessToBilling": IAMUserAccessToBillingType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateGovCloudAccountRequestTypeDef(
    _RequiredCreateGovCloudAccountRequestTypeDef, _OptionalCreateGovCloudAccountRequestTypeDef
):
    pass


CreateGovCloudAccountResponseResponseTypeDef = TypedDict(
    "CreateGovCloudAccountResponseResponseTypeDef",
    {
        "CreateAccountStatus": "CreateAccountStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOrganizationRequestTypeDef = TypedDict(
    "CreateOrganizationRequestTypeDef",
    {
        "FeatureSet": OrganizationFeatureSetType,
    },
    total=False,
)

CreateOrganizationResponseResponseTypeDef = TypedDict(
    "CreateOrganizationResponseResponseTypeDef",
    {
        "Organization": "OrganizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOrganizationalUnitRequestTypeDef = TypedDict(
    "_RequiredCreateOrganizationalUnitRequestTypeDef",
    {
        "ParentId": str,
        "Name": str,
    },
)
_OptionalCreateOrganizationalUnitRequestTypeDef = TypedDict(
    "_OptionalCreateOrganizationalUnitRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateOrganizationalUnitRequestTypeDef(
    _RequiredCreateOrganizationalUnitRequestTypeDef, _OptionalCreateOrganizationalUnitRequestTypeDef
):
    pass


CreateOrganizationalUnitResponseResponseTypeDef = TypedDict(
    "CreateOrganizationalUnitResponseResponseTypeDef",
    {
        "OrganizationalUnit": "OrganizationalUnitTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePolicyRequestTypeDef = TypedDict(
    "_RequiredCreatePolicyRequestTypeDef",
    {
        "Content": str,
        "Description": str,
        "Name": str,
        "Type": PolicyTypeType,
    },
)
_OptionalCreatePolicyRequestTypeDef = TypedDict(
    "_OptionalCreatePolicyRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreatePolicyRequestTypeDef(
    _RequiredCreatePolicyRequestTypeDef, _OptionalCreatePolicyRequestTypeDef
):
    pass


CreatePolicyResponseResponseTypeDef = TypedDict(
    "CreatePolicyResponseResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeclineHandshakeRequestTypeDef = TypedDict(
    "DeclineHandshakeRequestTypeDef",
    {
        "HandshakeId": str,
    },
)

DeclineHandshakeResponseResponseTypeDef = TypedDict(
    "DeclineHandshakeResponseResponseTypeDef",
    {
        "Handshake": "HandshakeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DelegatedAdministratorTypeDef = TypedDict(
    "DelegatedAdministratorTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": AccountStatusType,
        "JoinedMethod": AccountJoinedMethodType,
        "JoinedTimestamp": datetime,
        "DelegationEnabledDate": datetime,
    },
    total=False,
)

DelegatedServiceTypeDef = TypedDict(
    "DelegatedServiceTypeDef",
    {
        "ServicePrincipal": str,
        "DelegationEnabledDate": datetime,
    },
    total=False,
)

DeleteOrganizationalUnitRequestTypeDef = TypedDict(
    "DeleteOrganizationalUnitRequestTypeDef",
    {
        "OrganizationalUnitId": str,
    },
)

DeletePolicyRequestTypeDef = TypedDict(
    "DeletePolicyRequestTypeDef",
    {
        "PolicyId": str,
    },
)

DeregisterDelegatedAdministratorRequestTypeDef = TypedDict(
    "DeregisterDelegatedAdministratorRequestTypeDef",
    {
        "AccountId": str,
        "ServicePrincipal": str,
    },
)

DescribeAccountRequestTypeDef = TypedDict(
    "DescribeAccountRequestTypeDef",
    {
        "AccountId": str,
    },
)

DescribeAccountResponseResponseTypeDef = TypedDict(
    "DescribeAccountResponseResponseTypeDef",
    {
        "Account": "AccountTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCreateAccountStatusRequestTypeDef = TypedDict(
    "DescribeCreateAccountStatusRequestTypeDef",
    {
        "CreateAccountRequestId": str,
    },
)

DescribeCreateAccountStatusResponseResponseTypeDef = TypedDict(
    "DescribeCreateAccountStatusResponseResponseTypeDef",
    {
        "CreateAccountStatus": "CreateAccountStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEffectivePolicyRequestTypeDef = TypedDict(
    "_RequiredDescribeEffectivePolicyRequestTypeDef",
    {
        "PolicyType": EffectivePolicyTypeType,
    },
)
_OptionalDescribeEffectivePolicyRequestTypeDef = TypedDict(
    "_OptionalDescribeEffectivePolicyRequestTypeDef",
    {
        "TargetId": str,
    },
    total=False,
)


class DescribeEffectivePolicyRequestTypeDef(
    _RequiredDescribeEffectivePolicyRequestTypeDef, _OptionalDescribeEffectivePolicyRequestTypeDef
):
    pass


DescribeEffectivePolicyResponseResponseTypeDef = TypedDict(
    "DescribeEffectivePolicyResponseResponseTypeDef",
    {
        "EffectivePolicy": "EffectivePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHandshakeRequestTypeDef = TypedDict(
    "DescribeHandshakeRequestTypeDef",
    {
        "HandshakeId": str,
    },
)

DescribeHandshakeResponseResponseTypeDef = TypedDict(
    "DescribeHandshakeResponseResponseTypeDef",
    {
        "Handshake": "HandshakeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationResponseResponseTypeDef = TypedDict(
    "DescribeOrganizationResponseResponseTypeDef",
    {
        "Organization": "OrganizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationalUnitRequestTypeDef = TypedDict(
    "DescribeOrganizationalUnitRequestTypeDef",
    {
        "OrganizationalUnitId": str,
    },
)

DescribeOrganizationalUnitResponseResponseTypeDef = TypedDict(
    "DescribeOrganizationalUnitResponseResponseTypeDef",
    {
        "OrganizationalUnit": "OrganizationalUnitTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePolicyRequestTypeDef = TypedDict(
    "DescribePolicyRequestTypeDef",
    {
        "PolicyId": str,
    },
)

DescribePolicyResponseResponseTypeDef = TypedDict(
    "DescribePolicyResponseResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachPolicyRequestTypeDef = TypedDict(
    "DetachPolicyRequestTypeDef",
    {
        "PolicyId": str,
        "TargetId": str,
    },
)

DisableAWSServiceAccessRequestTypeDef = TypedDict(
    "DisableAWSServiceAccessRequestTypeDef",
    {
        "ServicePrincipal": str,
    },
)

DisablePolicyTypeRequestTypeDef = TypedDict(
    "DisablePolicyTypeRequestTypeDef",
    {
        "RootId": str,
        "PolicyType": PolicyTypeType,
    },
)

DisablePolicyTypeResponseResponseTypeDef = TypedDict(
    "DisablePolicyTypeResponseResponseTypeDef",
    {
        "Root": "RootTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EffectivePolicyTypeDef = TypedDict(
    "EffectivePolicyTypeDef",
    {
        "PolicyContent": str,
        "LastUpdatedTimestamp": datetime,
        "TargetId": str,
        "PolicyType": EffectivePolicyTypeType,
    },
    total=False,
)

EnableAWSServiceAccessRequestTypeDef = TypedDict(
    "EnableAWSServiceAccessRequestTypeDef",
    {
        "ServicePrincipal": str,
    },
)

EnableAllFeaturesResponseResponseTypeDef = TypedDict(
    "EnableAllFeaturesResponseResponseTypeDef",
    {
        "Handshake": "HandshakeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnablePolicyTypeRequestTypeDef = TypedDict(
    "EnablePolicyTypeRequestTypeDef",
    {
        "RootId": str,
        "PolicyType": PolicyTypeType,
    },
)

EnablePolicyTypeResponseResponseTypeDef = TypedDict(
    "EnablePolicyTypeResponseResponseTypeDef",
    {
        "Root": "RootTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnabledServicePrincipalTypeDef = TypedDict(
    "EnabledServicePrincipalTypeDef",
    {
        "ServicePrincipal": str,
        "DateEnabled": datetime,
    },
    total=False,
)

HandshakeFilterTypeDef = TypedDict(
    "HandshakeFilterTypeDef",
    {
        "ActionType": ActionTypeType,
        "ParentHandshakeId": str,
    },
    total=False,
)

HandshakePartyTypeDef = TypedDict(
    "HandshakePartyTypeDef",
    {
        "Id": str,
        "Type": HandshakePartyTypeType,
    },
)

HandshakeResourceTypeDef = TypedDict(
    "HandshakeResourceTypeDef",
    {
        "Value": str,
        "Type": HandshakeResourceTypeType,
        "Resources": List[Dict[str, Any]],
    },
    total=False,
)

HandshakeTypeDef = TypedDict(
    "HandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List["HandshakePartyTypeDef"],
        "State": HandshakeStateType,
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": ActionTypeType,
        "Resources": List["HandshakeResourceTypeDef"],
    },
    total=False,
)

_RequiredInviteAccountToOrganizationRequestTypeDef = TypedDict(
    "_RequiredInviteAccountToOrganizationRequestTypeDef",
    {
        "Target": "HandshakePartyTypeDef",
    },
)
_OptionalInviteAccountToOrganizationRequestTypeDef = TypedDict(
    "_OptionalInviteAccountToOrganizationRequestTypeDef",
    {
        "Notes": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class InviteAccountToOrganizationRequestTypeDef(
    _RequiredInviteAccountToOrganizationRequestTypeDef,
    _OptionalInviteAccountToOrganizationRequestTypeDef,
):
    pass


InviteAccountToOrganizationResponseResponseTypeDef = TypedDict(
    "InviteAccountToOrganizationResponseResponseTypeDef",
    {
        "Handshake": "HandshakeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAWSServiceAccessForOrganizationRequestTypeDef = TypedDict(
    "ListAWSServiceAccessForOrganizationRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAWSServiceAccessForOrganizationResponseResponseTypeDef = TypedDict(
    "ListAWSServiceAccessForOrganizationResponseResponseTypeDef",
    {
        "EnabledServicePrincipals": List["EnabledServicePrincipalTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccountsForParentRequestTypeDef = TypedDict(
    "_RequiredListAccountsForParentRequestTypeDef",
    {
        "ParentId": str,
    },
)
_OptionalListAccountsForParentRequestTypeDef = TypedDict(
    "_OptionalListAccountsForParentRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAccountsForParentRequestTypeDef(
    _RequiredListAccountsForParentRequestTypeDef, _OptionalListAccountsForParentRequestTypeDef
):
    pass


ListAccountsForParentResponseResponseTypeDef = TypedDict(
    "ListAccountsForParentResponseResponseTypeDef",
    {
        "Accounts": List["AccountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccountsRequestTypeDef = TypedDict(
    "ListAccountsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAccountsResponseResponseTypeDef = TypedDict(
    "ListAccountsResponseResponseTypeDef",
    {
        "Accounts": List["AccountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChildrenRequestTypeDef = TypedDict(
    "_RequiredListChildrenRequestTypeDef",
    {
        "ParentId": str,
        "ChildType": ChildTypeType,
    },
)
_OptionalListChildrenRequestTypeDef = TypedDict(
    "_OptionalListChildrenRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListChildrenRequestTypeDef(
    _RequiredListChildrenRequestTypeDef, _OptionalListChildrenRequestTypeDef
):
    pass


ListChildrenResponseResponseTypeDef = TypedDict(
    "ListChildrenResponseResponseTypeDef",
    {
        "Children": List["ChildTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCreateAccountStatusRequestTypeDef = TypedDict(
    "ListCreateAccountStatusRequestTypeDef",
    {
        "States": List[CreateAccountStateType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListCreateAccountStatusResponseResponseTypeDef = TypedDict(
    "ListCreateAccountStatusResponseResponseTypeDef",
    {
        "CreateAccountStatuses": List["CreateAccountStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDelegatedAdministratorsRequestTypeDef = TypedDict(
    "ListDelegatedAdministratorsRequestTypeDef",
    {
        "ServicePrincipal": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDelegatedAdministratorsResponseResponseTypeDef = TypedDict(
    "ListDelegatedAdministratorsResponseResponseTypeDef",
    {
        "DelegatedAdministrators": List["DelegatedAdministratorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDelegatedServicesForAccountRequestTypeDef = TypedDict(
    "_RequiredListDelegatedServicesForAccountRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListDelegatedServicesForAccountRequestTypeDef = TypedDict(
    "_OptionalListDelegatedServicesForAccountRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDelegatedServicesForAccountRequestTypeDef(
    _RequiredListDelegatedServicesForAccountRequestTypeDef,
    _OptionalListDelegatedServicesForAccountRequestTypeDef,
):
    pass


ListDelegatedServicesForAccountResponseResponseTypeDef = TypedDict(
    "ListDelegatedServicesForAccountResponseResponseTypeDef",
    {
        "DelegatedServices": List["DelegatedServiceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHandshakesForAccountRequestTypeDef = TypedDict(
    "ListHandshakesForAccountRequestTypeDef",
    {
        "Filter": "HandshakeFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListHandshakesForAccountResponseResponseTypeDef = TypedDict(
    "ListHandshakesForAccountResponseResponseTypeDef",
    {
        "Handshakes": List["HandshakeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHandshakesForOrganizationRequestTypeDef = TypedDict(
    "ListHandshakesForOrganizationRequestTypeDef",
    {
        "Filter": "HandshakeFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListHandshakesForOrganizationResponseResponseTypeDef = TypedDict(
    "ListHandshakesForOrganizationResponseResponseTypeDef",
    {
        "Handshakes": List["HandshakeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListOrganizationalUnitsForParentRequestTypeDef = TypedDict(
    "_RequiredListOrganizationalUnitsForParentRequestTypeDef",
    {
        "ParentId": str,
    },
)
_OptionalListOrganizationalUnitsForParentRequestTypeDef = TypedDict(
    "_OptionalListOrganizationalUnitsForParentRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListOrganizationalUnitsForParentRequestTypeDef(
    _RequiredListOrganizationalUnitsForParentRequestTypeDef,
    _OptionalListOrganizationalUnitsForParentRequestTypeDef,
):
    pass


ListOrganizationalUnitsForParentResponseResponseTypeDef = TypedDict(
    "ListOrganizationalUnitsForParentResponseResponseTypeDef",
    {
        "OrganizationalUnits": List["OrganizationalUnitTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListParentsRequestTypeDef = TypedDict(
    "_RequiredListParentsRequestTypeDef",
    {
        "ChildId": str,
    },
)
_OptionalListParentsRequestTypeDef = TypedDict(
    "_OptionalListParentsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListParentsRequestTypeDef(
    _RequiredListParentsRequestTypeDef, _OptionalListParentsRequestTypeDef
):
    pass


ListParentsResponseResponseTypeDef = TypedDict(
    "ListParentsResponseResponseTypeDef",
    {
        "Parents": List["ParentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPoliciesForTargetRequestTypeDef = TypedDict(
    "_RequiredListPoliciesForTargetRequestTypeDef",
    {
        "TargetId": str,
        "Filter": PolicyTypeType,
    },
)
_OptionalListPoliciesForTargetRequestTypeDef = TypedDict(
    "_OptionalListPoliciesForTargetRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListPoliciesForTargetRequestTypeDef(
    _RequiredListPoliciesForTargetRequestTypeDef, _OptionalListPoliciesForTargetRequestTypeDef
):
    pass


ListPoliciesForTargetResponseResponseTypeDef = TypedDict(
    "ListPoliciesForTargetResponseResponseTypeDef",
    {
        "Policies": List["PolicySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPoliciesRequestTypeDef = TypedDict(
    "_RequiredListPoliciesRequestTypeDef",
    {
        "Filter": PolicyTypeType,
    },
)
_OptionalListPoliciesRequestTypeDef = TypedDict(
    "_OptionalListPoliciesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListPoliciesRequestTypeDef(
    _RequiredListPoliciesRequestTypeDef, _OptionalListPoliciesRequestTypeDef
):
    pass


ListPoliciesResponseResponseTypeDef = TypedDict(
    "ListPoliciesResponseResponseTypeDef",
    {
        "Policies": List["PolicySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRootsRequestTypeDef = TypedDict(
    "ListRootsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListRootsResponseResponseTypeDef = TypedDict(
    "ListRootsResponseResponseTypeDef",
    {
        "Roots": List["RootTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestTypeDef",
    {
        "ResourceId": str,
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

_RequiredListTargetsForPolicyRequestTypeDef = TypedDict(
    "_RequiredListTargetsForPolicyRequestTypeDef",
    {
        "PolicyId": str,
    },
)
_OptionalListTargetsForPolicyRequestTypeDef = TypedDict(
    "_OptionalListTargetsForPolicyRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTargetsForPolicyRequestTypeDef(
    _RequiredListTargetsForPolicyRequestTypeDef, _OptionalListTargetsForPolicyRequestTypeDef
):
    pass


ListTargetsForPolicyResponseResponseTypeDef = TypedDict(
    "ListTargetsForPolicyResponseResponseTypeDef",
    {
        "Targets": List["PolicyTargetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MoveAccountRequestTypeDef = TypedDict(
    "MoveAccountRequestTypeDef",
    {
        "AccountId": str,
        "SourceParentId": str,
        "DestinationParentId": str,
    },
)

OrganizationTypeDef = TypedDict(
    "OrganizationTypeDef",
    {
        "Id": str,
        "Arn": str,
        "FeatureSet": OrganizationFeatureSetType,
        "MasterAccountArn": str,
        "MasterAccountId": str,
        "MasterAccountEmail": str,
        "AvailablePolicyTypes": List["PolicyTypeSummaryTypeDef"],
    },
    total=False,
)

OrganizationalUnitTypeDef = TypedDict(
    "OrganizationalUnitTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
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

ParentTypeDef = TypedDict(
    "ParentTypeDef",
    {
        "Id": str,
        "Type": ParentTypeType,
    },
    total=False,
)

PolicySummaryTypeDef = TypedDict(
    "PolicySummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": PolicyTypeType,
        "AwsManaged": bool,
    },
    total=False,
)

PolicyTargetSummaryTypeDef = TypedDict(
    "PolicyTargetSummaryTypeDef",
    {
        "TargetId": str,
        "Arn": str,
        "Name": str,
        "Type": TargetTypeType,
    },
    total=False,
)

PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "PolicySummary": "PolicySummaryTypeDef",
        "Content": str,
    },
    total=False,
)

PolicyTypeSummaryTypeDef = TypedDict(
    "PolicyTypeSummaryTypeDef",
    {
        "Type": PolicyTypeType,
        "Status": PolicyTypeStatusType,
    },
    total=False,
)

RegisterDelegatedAdministratorRequestTypeDef = TypedDict(
    "RegisterDelegatedAdministratorRequestTypeDef",
    {
        "AccountId": str,
        "ServicePrincipal": str,
    },
)

RemoveAccountFromOrganizationRequestTypeDef = TypedDict(
    "RemoveAccountFromOrganizationRequestTypeDef",
    {
        "AccountId": str,
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

RootTypeDef = TypedDict(
    "RootTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "PolicyTypes": List["PolicyTypeSummaryTypeDef"],
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceId": str,
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
        "ResourceId": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateOrganizationalUnitRequestTypeDef = TypedDict(
    "_RequiredUpdateOrganizationalUnitRequestTypeDef",
    {
        "OrganizationalUnitId": str,
    },
)
_OptionalUpdateOrganizationalUnitRequestTypeDef = TypedDict(
    "_OptionalUpdateOrganizationalUnitRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class UpdateOrganizationalUnitRequestTypeDef(
    _RequiredUpdateOrganizationalUnitRequestTypeDef, _OptionalUpdateOrganizationalUnitRequestTypeDef
):
    pass


UpdateOrganizationalUnitResponseResponseTypeDef = TypedDict(
    "UpdateOrganizationalUnitResponseResponseTypeDef",
    {
        "OrganizationalUnit": "OrganizationalUnitTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePolicyRequestTypeDef = TypedDict(
    "_RequiredUpdatePolicyRequestTypeDef",
    {
        "PolicyId": str,
    },
)
_OptionalUpdatePolicyRequestTypeDef = TypedDict(
    "_OptionalUpdatePolicyRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "Content": str,
    },
    total=False,
)


class UpdatePolicyRequestTypeDef(
    _RequiredUpdatePolicyRequestTypeDef, _OptionalUpdatePolicyRequestTypeDef
):
    pass


UpdatePolicyResponseResponseTypeDef = TypedDict(
    "UpdatePolicyResponseResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
