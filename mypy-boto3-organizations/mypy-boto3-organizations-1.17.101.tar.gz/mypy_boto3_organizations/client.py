"""
Type annotations for organizations service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_organizations import OrganizationsClient

    client: OrganizationsClient = boto3.client("organizations")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    ChildTypeType,
    CreateAccountStateType,
    EffectivePolicyTypeType,
    IAMUserAccessToBillingType,
    OrganizationFeatureSetType,
    PolicyTypeType,
)
from .paginator import (
    ListAccountsForParentPaginator,
    ListAccountsPaginator,
    ListAWSServiceAccessForOrganizationPaginator,
    ListChildrenPaginator,
    ListCreateAccountStatusPaginator,
    ListDelegatedAdministratorsPaginator,
    ListDelegatedServicesForAccountPaginator,
    ListHandshakesForAccountPaginator,
    ListHandshakesForOrganizationPaginator,
    ListOrganizationalUnitsForParentPaginator,
    ListParentsPaginator,
    ListPoliciesForTargetPaginator,
    ListPoliciesPaginator,
    ListRootsPaginator,
    ListTagsForResourcePaginator,
    ListTargetsForPolicyPaginator,
)
from .type_defs import (
    AcceptHandshakeResponseTypeDef,
    CancelHandshakeResponseTypeDef,
    CreateAccountResponseTypeDef,
    CreateGovCloudAccountResponseTypeDef,
    CreateOrganizationalUnitResponseTypeDef,
    CreateOrganizationResponseTypeDef,
    CreatePolicyResponseTypeDef,
    DeclineHandshakeResponseTypeDef,
    DescribeAccountResponseTypeDef,
    DescribeCreateAccountStatusResponseTypeDef,
    DescribeEffectivePolicyResponseTypeDef,
    DescribeHandshakeResponseTypeDef,
    DescribeOrganizationalUnitResponseTypeDef,
    DescribeOrganizationResponseTypeDef,
    DescribePolicyResponseTypeDef,
    DisablePolicyTypeResponseTypeDef,
    EnableAllFeaturesResponseTypeDef,
    EnablePolicyTypeResponseTypeDef,
    HandshakeFilterTypeDef,
    HandshakePartyTypeDef,
    InviteAccountToOrganizationResponseTypeDef,
    ListAccountsForParentResponseTypeDef,
    ListAccountsResponseTypeDef,
    ListAWSServiceAccessForOrganizationResponseTypeDef,
    ListChildrenResponseTypeDef,
    ListCreateAccountStatusResponseTypeDef,
    ListDelegatedAdministratorsResponseTypeDef,
    ListDelegatedServicesForAccountResponseTypeDef,
    ListHandshakesForAccountResponseTypeDef,
    ListHandshakesForOrganizationResponseTypeDef,
    ListOrganizationalUnitsForParentResponseTypeDef,
    ListParentsResponseTypeDef,
    ListPoliciesForTargetResponseTypeDef,
    ListPoliciesResponseTypeDef,
    ListRootsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetsForPolicyResponseTypeDef,
    TagTypeDef,
    UpdateOrganizationalUnitResponseTypeDef,
    UpdatePolicyResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("OrganizationsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AWSOrganizationsNotInUseException: Type[BotocoreClientError]
    AccessDeniedException: Type[BotocoreClientError]
    AccessDeniedForDependencyException: Type[BotocoreClientError]
    AccountAlreadyRegisteredException: Type[BotocoreClientError]
    AccountNotFoundException: Type[BotocoreClientError]
    AccountNotRegisteredException: Type[BotocoreClientError]
    AccountOwnerNotVerifiedException: Type[BotocoreClientError]
    AlreadyInOrganizationException: Type[BotocoreClientError]
    ChildNotFoundException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConstraintViolationException: Type[BotocoreClientError]
    CreateAccountStatusNotFoundException: Type[BotocoreClientError]
    DestinationParentNotFoundException: Type[BotocoreClientError]
    DuplicateAccountException: Type[BotocoreClientError]
    DuplicateHandshakeException: Type[BotocoreClientError]
    DuplicateOrganizationalUnitException: Type[BotocoreClientError]
    DuplicatePolicyAttachmentException: Type[BotocoreClientError]
    DuplicatePolicyException: Type[BotocoreClientError]
    EffectivePolicyNotFoundException: Type[BotocoreClientError]
    FinalizingOrganizationException: Type[BotocoreClientError]
    HandshakeAlreadyInStateException: Type[BotocoreClientError]
    HandshakeConstraintViolationException: Type[BotocoreClientError]
    HandshakeNotFoundException: Type[BotocoreClientError]
    InvalidHandshakeTransitionException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    MasterCannotLeaveOrganizationException: Type[BotocoreClientError]
    OrganizationNotEmptyException: Type[BotocoreClientError]
    OrganizationalUnitNotEmptyException: Type[BotocoreClientError]
    OrganizationalUnitNotFoundException: Type[BotocoreClientError]
    ParentNotFoundException: Type[BotocoreClientError]
    PolicyChangesInProgressException: Type[BotocoreClientError]
    PolicyInUseException: Type[BotocoreClientError]
    PolicyNotAttachedException: Type[BotocoreClientError]
    PolicyNotFoundException: Type[BotocoreClientError]
    PolicyTypeAlreadyEnabledException: Type[BotocoreClientError]
    PolicyTypeNotAvailableForOrganizationException: Type[BotocoreClientError]
    PolicyTypeNotEnabledException: Type[BotocoreClientError]
    RootNotFoundException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    SourceParentNotFoundException: Type[BotocoreClientError]
    TargetNotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnsupportedAPIEndpointException: Type[BotocoreClientError]


class OrganizationsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_handshake(self, *, HandshakeId: str) -> AcceptHandshakeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.accept_handshake)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#accept_handshake)
        """

    def attach_policy(self, *, PolicyId: str, TargetId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.attach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#attach_policy)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#can_paginate)
        """

    def cancel_handshake(self, *, HandshakeId: str) -> CancelHandshakeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.cancel_handshake)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#cancel_handshake)
        """

    def create_account(
        self,
        *,
        Email: str,
        AccountName: str,
        RoleName: str = None,
        IamUserAccessToBilling: IAMUserAccessToBillingType = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.create_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#create_account)
        """

    def create_gov_cloud_account(
        self,
        *,
        Email: str,
        AccountName: str,
        RoleName: str = None,
        IamUserAccessToBilling: IAMUserAccessToBillingType = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateGovCloudAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.create_gov_cloud_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#create_gov_cloud_account)
        """

    def create_organization(
        self, *, FeatureSet: OrganizationFeatureSetType = None
    ) -> CreateOrganizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.create_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#create_organization)
        """

    def create_organizational_unit(
        self, *, ParentId: str, Name: str, Tags: List["TagTypeDef"] = None
    ) -> CreateOrganizationalUnitResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.create_organizational_unit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#create_organizational_unit)
        """

    def create_policy(
        self,
        *,
        Content: str,
        Description: str,
        Name: str,
        Type: PolicyTypeType,
        Tags: List["TagTypeDef"] = None
    ) -> CreatePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.create_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#create_policy)
        """

    def decline_handshake(self, *, HandshakeId: str) -> DeclineHandshakeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.decline_handshake)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#decline_handshake)
        """

    def delete_organization(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.delete_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#delete_organization)
        """

    def delete_organizational_unit(self, *, OrganizationalUnitId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.delete_organizational_unit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#delete_organizational_unit)
        """

    def delete_policy(self, *, PolicyId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.delete_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#delete_policy)
        """

    def deregister_delegated_administrator(self, *, AccountId: str, ServicePrincipal: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.deregister_delegated_administrator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#deregister_delegated_administrator)
        """

    def describe_account(self, *, AccountId: str) -> DescribeAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.describe_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#describe_account)
        """

    def describe_create_account_status(
        self, *, CreateAccountRequestId: str
    ) -> DescribeCreateAccountStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.describe_create_account_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#describe_create_account_status)
        """

    def describe_effective_policy(
        self, *, PolicyType: EffectivePolicyTypeType, TargetId: str = None
    ) -> DescribeEffectivePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.describe_effective_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#describe_effective_policy)
        """

    def describe_handshake(self, *, HandshakeId: str) -> DescribeHandshakeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.describe_handshake)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#describe_handshake)
        """

    def describe_organization(self) -> DescribeOrganizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.describe_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#describe_organization)
        """

    def describe_organizational_unit(
        self, *, OrganizationalUnitId: str
    ) -> DescribeOrganizationalUnitResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.describe_organizational_unit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#describe_organizational_unit)
        """

    def describe_policy(self, *, PolicyId: str) -> DescribePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.describe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#describe_policy)
        """

    def detach_policy(self, *, PolicyId: str, TargetId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.detach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#detach_policy)
        """

    def disable_aws_service_access(self, *, ServicePrincipal: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.disable_aws_service_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#disable_aws_service_access)
        """

    def disable_policy_type(
        self, *, RootId: str, PolicyType: PolicyTypeType
    ) -> DisablePolicyTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.disable_policy_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#disable_policy_type)
        """

    def enable_all_features(self) -> EnableAllFeaturesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.enable_all_features)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#enable_all_features)
        """

    def enable_aws_service_access(self, *, ServicePrincipal: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.enable_aws_service_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#enable_aws_service_access)
        """

    def enable_policy_type(
        self, *, RootId: str, PolicyType: PolicyTypeType
    ) -> EnablePolicyTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.enable_policy_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#enable_policy_type)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#generate_presigned_url)
        """

    def invite_account_to_organization(
        self, *, Target: "HandshakePartyTypeDef", Notes: str = None, Tags: List["TagTypeDef"] = None
    ) -> InviteAccountToOrganizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.invite_account_to_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#invite_account_to_organization)
        """

    def leave_organization(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.leave_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#leave_organization)
        """

    def list_accounts(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListAccountsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.list_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_accounts)
        """

    def list_accounts_for_parent(
        self, *, ParentId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAccountsForParentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.list_accounts_for_parent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_accounts_for_parent)
        """

    def list_aws_service_access_for_organization(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListAWSServiceAccessForOrganizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.list_aws_service_access_for_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_aws_service_access_for_organization)
        """

    def list_children(
        self,
        *,
        ParentId: str,
        ChildType: ChildTypeType,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListChildrenResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.list_children)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_children)
        """

    def list_create_account_status(
        self,
        *,
        States: List[CreateAccountStateType] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListCreateAccountStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.list_create_account_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_create_account_status)
        """

    def list_delegated_administrators(
        self, *, ServicePrincipal: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListDelegatedAdministratorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.list_delegated_administrators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_delegated_administrators)
        """

    def list_delegated_services_for_account(
        self, *, AccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDelegatedServicesForAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.list_delegated_services_for_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_delegated_services_for_account)
        """

    def list_handshakes_for_account(
        self,
        *,
        Filter: HandshakeFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListHandshakesForAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.list_handshakes_for_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_handshakes_for_account)
        """

    def list_handshakes_for_organization(
        self,
        *,
        Filter: HandshakeFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListHandshakesForOrganizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.list_handshakes_for_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_handshakes_for_organization)
        """

    def list_organizational_units_for_parent(
        self, *, ParentId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListOrganizationalUnitsForParentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.list_organizational_units_for_parent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_organizational_units_for_parent)
        """

    def list_parents(
        self, *, ChildId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListParentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.list_parents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_parents)
        """

    def list_policies(
        self, *, Filter: PolicyTypeType, NextToken: str = None, MaxResults: int = None
    ) -> ListPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.list_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_policies)
        """

    def list_policies_for_target(
        self,
        *,
        TargetId: str,
        Filter: PolicyTypeType,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListPoliciesForTargetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.list_policies_for_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_policies_for_target)
        """

    def list_roots(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListRootsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.list_roots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_roots)
        """

    def list_tags_for_resource(
        self, *, ResourceId: str, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_tags_for_resource)
        """

    def list_targets_for_policy(
        self, *, PolicyId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTargetsForPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.list_targets_for_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_targets_for_policy)
        """

    def move_account(
        self, *, AccountId: str, SourceParentId: str, DestinationParentId: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.move_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#move_account)
        """

    def register_delegated_administrator(self, *, AccountId: str, ServicePrincipal: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.register_delegated_administrator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#register_delegated_administrator)
        """

    def remove_account_from_organization(self, *, AccountId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.remove_account_from_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#remove_account_from_organization)
        """

    def tag_resource(self, *, ResourceId: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceId: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#untag_resource)
        """

    def update_organizational_unit(
        self, *, OrganizationalUnitId: str, Name: str = None
    ) -> UpdateOrganizationalUnitResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.update_organizational_unit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#update_organizational_unit)
        """

    def update_policy(
        self, *, PolicyId: str, Name: str = None, Description: str = None, Content: str = None
    ) -> UpdatePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Client.update_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#update_policy)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_aws_service_access_for_organization"]
    ) -> ListAWSServiceAccessForOrganizationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Paginator.ListAWSServiceAccessForOrganization)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listawsserviceaccessfororganizationpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_accounts"]) -> ListAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Paginator.ListAccounts)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listaccountspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accounts_for_parent"]
    ) -> ListAccountsForParentPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Paginator.ListAccountsForParent)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listaccountsforparentpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_children"]) -> ListChildrenPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Paginator.ListChildren)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listchildrenpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_create_account_status"]
    ) -> ListCreateAccountStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Paginator.ListCreateAccountStatus)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listcreateaccountstatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_delegated_administrators"]
    ) -> ListDelegatedAdministratorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Paginator.ListDelegatedAdministrators)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listdelegatedadministratorspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_delegated_services_for_account"]
    ) -> ListDelegatedServicesForAccountPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Paginator.ListDelegatedServicesForAccount)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listdelegatedservicesforaccountpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_handshakes_for_account"]
    ) -> ListHandshakesForAccountPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForAccount)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listhandshakesforaccountpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_handshakes_for_organization"]
    ) -> ListHandshakesForOrganizationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForOrganization)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listhandshakesfororganizationpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organizational_units_for_parent"]
    ) -> ListOrganizationalUnitsForParentPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Paginator.ListOrganizationalUnitsForParent)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listorganizationalunitsforparentpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_parents"]) -> ListParentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Paginator.ListParents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listparentspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_policies"]) -> ListPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Paginator.ListPolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listpoliciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policies_for_target"]
    ) -> ListPoliciesForTargetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Paginator.ListPoliciesForTarget)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listpoliciesfortargetpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_roots"]) -> ListRootsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Paginator.ListRoots)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listrootspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Paginator.ListTagsForResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listtagsforresourcepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_targets_for_policy"]
    ) -> ListTargetsForPolicyPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/organizations.html#Organizations.Paginator.ListTargetsForPolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listtargetsforpolicypaginator)
        """
