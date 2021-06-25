"""
Type annotations for route53domains service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_route53domains import Route53DomainsClient

    client: Route53DomainsClient = boto3.client("route53domains")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .paginator import ListDomainsPaginator, ListOperationsPaginator, ViewBillingPaginator
from .type_defs import (
    AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef,
    CancelDomainTransferToAnotherAwsAccountResponseTypeDef,
    CheckDomainAvailabilityResponseTypeDef,
    CheckDomainTransferabilityResponseTypeDef,
    ContactDetailTypeDef,
    DisableDomainTransferLockResponseTypeDef,
    EnableDomainTransferLockResponseTypeDef,
    GetContactReachabilityStatusResponseTypeDef,
    GetDomainDetailResponseTypeDef,
    GetDomainSuggestionsResponseTypeDef,
    GetOperationDetailResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListOperationsResponseTypeDef,
    ListTagsForDomainResponseTypeDef,
    NameserverTypeDef,
    RegisterDomainResponseTypeDef,
    RejectDomainTransferFromAnotherAwsAccountResponseTypeDef,
    RenewDomainResponseTypeDef,
    ResendContactReachabilityEmailResponseTypeDef,
    RetrieveDomainAuthCodeResponseTypeDef,
    TagTypeDef,
    TransferDomainResponseTypeDef,
    TransferDomainToAnotherAwsAccountResponseTypeDef,
    UpdateDomainContactPrivacyResponseTypeDef,
    UpdateDomainContactResponseTypeDef,
    UpdateDomainNameserversResponseTypeDef,
    ViewBillingResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Route53DomainsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    DomainLimitExceeded: Type[BotocoreClientError]
    DuplicateRequest: Type[BotocoreClientError]
    InvalidInput: Type[BotocoreClientError]
    OperationLimitExceeded: Type[BotocoreClientError]
    TLDRulesViolation: Type[BotocoreClientError]
    UnsupportedTLD: Type[BotocoreClientError]


class Route53DomainsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_domain_transfer_from_another_aws_account(
        self, *, DomainName: str, Password: str
    ) -> AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.accept_domain_transfer_from_another_aws_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#accept_domain_transfer_from_another_aws_account)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#can_paginate)
        """

    def cancel_domain_transfer_to_another_aws_account(
        self, *, DomainName: str
    ) -> CancelDomainTransferToAnotherAwsAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.cancel_domain_transfer_to_another_aws_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#cancel_domain_transfer_to_another_aws_account)
        """

    def check_domain_availability(
        self, *, DomainName: str, IdnLangCode: str = None
    ) -> CheckDomainAvailabilityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.check_domain_availability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#check_domain_availability)
        """

    def check_domain_transferability(
        self, *, DomainName: str, AuthCode: str = None
    ) -> CheckDomainTransferabilityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.check_domain_transferability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#check_domain_transferability)
        """

    def delete_tags_for_domain(self, *, DomainName: str, TagsToDelete: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.delete_tags_for_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#delete_tags_for_domain)
        """

    def disable_domain_auto_renew(self, *, DomainName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.disable_domain_auto_renew)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#disable_domain_auto_renew)
        """

    def disable_domain_transfer_lock(
        self, *, DomainName: str
    ) -> DisableDomainTransferLockResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.disable_domain_transfer_lock)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#disable_domain_transfer_lock)
        """

    def enable_domain_auto_renew(self, *, DomainName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.enable_domain_auto_renew)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#enable_domain_auto_renew)
        """

    def enable_domain_transfer_lock(
        self, *, DomainName: str
    ) -> EnableDomainTransferLockResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.enable_domain_transfer_lock)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#enable_domain_transfer_lock)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#generate_presigned_url)
        """

    def get_contact_reachability_status(
        self, *, domainName: str = None
    ) -> GetContactReachabilityStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.get_contact_reachability_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#get_contact_reachability_status)
        """

    def get_domain_detail(self, *, DomainName: str) -> GetDomainDetailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.get_domain_detail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#get_domain_detail)
        """

    def get_domain_suggestions(
        self, *, DomainName: str, SuggestionCount: int, OnlyAvailable: bool
    ) -> GetDomainSuggestionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.get_domain_suggestions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#get_domain_suggestions)
        """

    def get_operation_detail(self, *, OperationId: str) -> GetOperationDetailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.get_operation_detail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#get_operation_detail)
        """

    def list_domains(
        self, *, Marker: str = None, MaxItems: int = None
    ) -> ListDomainsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.list_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#list_domains)
        """

    def list_operations(
        self, *, SubmittedSince: datetime = None, Marker: str = None, MaxItems: int = None
    ) -> ListOperationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.list_operations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#list_operations)
        """

    def list_tags_for_domain(self, *, DomainName: str) -> ListTagsForDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.list_tags_for_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#list_tags_for_domain)
        """

    def register_domain(
        self,
        *,
        DomainName: str,
        DurationInYears: int,
        AdminContact: "ContactDetailTypeDef",
        RegistrantContact: "ContactDetailTypeDef",
        TechContact: "ContactDetailTypeDef",
        IdnLangCode: str = None,
        AutoRenew: bool = None,
        PrivacyProtectAdminContact: bool = None,
        PrivacyProtectRegistrantContact: bool = None,
        PrivacyProtectTechContact: bool = None
    ) -> RegisterDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.register_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#register_domain)
        """

    def reject_domain_transfer_from_another_aws_account(
        self, *, DomainName: str
    ) -> RejectDomainTransferFromAnotherAwsAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.reject_domain_transfer_from_another_aws_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#reject_domain_transfer_from_another_aws_account)
        """

    def renew_domain(
        self, *, DomainName: str, CurrentExpiryYear: int, DurationInYears: int = None
    ) -> RenewDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.renew_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#renew_domain)
        """

    def resend_contact_reachability_email(
        self, *, domainName: str = None
    ) -> ResendContactReachabilityEmailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.resend_contact_reachability_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#resend_contact_reachability_email)
        """

    def retrieve_domain_auth_code(
        self, *, DomainName: str
    ) -> RetrieveDomainAuthCodeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.retrieve_domain_auth_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#retrieve_domain_auth_code)
        """

    def transfer_domain(
        self,
        *,
        DomainName: str,
        DurationInYears: int,
        AdminContact: "ContactDetailTypeDef",
        RegistrantContact: "ContactDetailTypeDef",
        TechContact: "ContactDetailTypeDef",
        IdnLangCode: str = None,
        Nameservers: List["NameserverTypeDef"] = None,
        AuthCode: str = None,
        AutoRenew: bool = None,
        PrivacyProtectAdminContact: bool = None,
        PrivacyProtectRegistrantContact: bool = None,
        PrivacyProtectTechContact: bool = None
    ) -> TransferDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.transfer_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#transfer_domain)
        """

    def transfer_domain_to_another_aws_account(
        self, *, DomainName: str, AccountId: str
    ) -> TransferDomainToAnotherAwsAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.transfer_domain_to_another_aws_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#transfer_domain_to_another_aws_account)
        """

    def update_domain_contact(
        self,
        *,
        DomainName: str,
        AdminContact: "ContactDetailTypeDef" = None,
        RegistrantContact: "ContactDetailTypeDef" = None,
        TechContact: "ContactDetailTypeDef" = None
    ) -> UpdateDomainContactResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.update_domain_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#update_domain_contact)
        """

    def update_domain_contact_privacy(
        self,
        *,
        DomainName: str,
        AdminPrivacy: bool = None,
        RegistrantPrivacy: bool = None,
        TechPrivacy: bool = None
    ) -> UpdateDomainContactPrivacyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.update_domain_contact_privacy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#update_domain_contact_privacy)
        """

    def update_domain_nameservers(
        self, *, DomainName: str, Nameservers: List["NameserverTypeDef"], FIAuthKey: str = None
    ) -> UpdateDomainNameserversResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.update_domain_nameservers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#update_domain_nameservers)
        """

    def update_tags_for_domain(
        self, *, DomainName: str, TagsToUpdate: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.update_tags_for_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#update_tags_for_domain)
        """

    def view_billing(
        self,
        *,
        Start: datetime = None,
        End: datetime = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> ViewBillingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Client.view_billing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/client.html#view_billing)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Paginator.ListDomains)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators.html#listdomainspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_operations"]) -> ListOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Paginator.ListOperations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators.html#listoperationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["view_billing"]) -> ViewBillingPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53domains.html#Route53Domains.Paginator.ViewBilling)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators.html#viewbillingpaginator)
        """
