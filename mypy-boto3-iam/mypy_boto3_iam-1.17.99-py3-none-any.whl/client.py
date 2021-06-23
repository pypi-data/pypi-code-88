"""
Type annotations for iam service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iam import IAMClient

    client: IAMClient = boto3.client("iam")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    AccessAdvisorUsageGranularityTypeType,
    EntityTypeType,
    PolicyUsageTypeType,
    assignmentStatusTypeType,
    encodingTypeType,
    globalEndpointTokenVersionType,
    policyScopeTypeType,
    sortKeyTypeType,
    statusTypeType,
)
from .paginator import (
    GetAccountAuthorizationDetailsPaginator,
    GetGroupPaginator,
    ListAccessKeysPaginator,
    ListAccountAliasesPaginator,
    ListAttachedGroupPoliciesPaginator,
    ListAttachedRolePoliciesPaginator,
    ListAttachedUserPoliciesPaginator,
    ListEntitiesForPolicyPaginator,
    ListGroupPoliciesPaginator,
    ListGroupsForUserPaginator,
    ListGroupsPaginator,
    ListInstanceProfilesForRolePaginator,
    ListInstanceProfilesPaginator,
    ListMFADevicesPaginator,
    ListPoliciesPaginator,
    ListPolicyVersionsPaginator,
    ListRolePoliciesPaginator,
    ListRolesPaginator,
    ListServerCertificatesPaginator,
    ListSigningCertificatesPaginator,
    ListSSHPublicKeysPaginator,
    ListUserPoliciesPaginator,
    ListUsersPaginator,
    ListUserTagsPaginator,
    ListVirtualMFADevicesPaginator,
    SimulateCustomPolicyPaginator,
    SimulatePrincipalPolicyPaginator,
)
from .type_defs import (
    ContextEntryTypeDef,
    CreateAccessKeyResponseTypeDef,
    CreateGroupResponseTypeDef,
    CreateInstanceProfileResponseTypeDef,
    CreateLoginProfileResponseTypeDef,
    CreateOpenIDConnectProviderResponseTypeDef,
    CreatePolicyResponseTypeDef,
    CreatePolicyVersionResponseTypeDef,
    CreateRoleResponseTypeDef,
    CreateSAMLProviderResponseTypeDef,
    CreateServiceLinkedRoleResponseTypeDef,
    CreateServiceSpecificCredentialResponseTypeDef,
    CreateUserResponseTypeDef,
    CreateVirtualMFADeviceResponseTypeDef,
    DeleteServiceLinkedRoleResponseTypeDef,
    GenerateCredentialReportResponseTypeDef,
    GenerateOrganizationsAccessReportResponseTypeDef,
    GenerateServiceLastAccessedDetailsResponseTypeDef,
    GetAccessKeyLastUsedResponseTypeDef,
    GetAccountAuthorizationDetailsResponseTypeDef,
    GetAccountPasswordPolicyResponseTypeDef,
    GetAccountSummaryResponseTypeDef,
    GetContextKeysForPolicyResponseTypeDef,
    GetCredentialReportResponseTypeDef,
    GetGroupPolicyResponseTypeDef,
    GetGroupResponseTypeDef,
    GetInstanceProfileResponseTypeDef,
    GetLoginProfileResponseTypeDef,
    GetOpenIDConnectProviderResponseTypeDef,
    GetOrganizationsAccessReportResponseTypeDef,
    GetPolicyResponseTypeDef,
    GetPolicyVersionResponseTypeDef,
    GetRolePolicyResponseTypeDef,
    GetRoleResponseTypeDef,
    GetSAMLProviderResponseTypeDef,
    GetServerCertificateResponseTypeDef,
    GetServiceLastAccessedDetailsResponseTypeDef,
    GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef,
    GetServiceLinkedRoleDeletionStatusResponseTypeDef,
    GetSSHPublicKeyResponseTypeDef,
    GetUserPolicyResponseTypeDef,
    GetUserResponseTypeDef,
    ListAccessKeysResponseTypeDef,
    ListAccountAliasesResponseTypeDef,
    ListAttachedGroupPoliciesResponseTypeDef,
    ListAttachedRolePoliciesResponseTypeDef,
    ListAttachedUserPoliciesResponseTypeDef,
    ListEntitiesForPolicyResponseTypeDef,
    ListGroupPoliciesResponseTypeDef,
    ListGroupsForUserResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListInstanceProfilesForRoleResponseTypeDef,
    ListInstanceProfilesResponseTypeDef,
    ListInstanceProfileTagsResponseTypeDef,
    ListMFADevicesResponseTypeDef,
    ListMFADeviceTagsResponseTypeDef,
    ListOpenIDConnectProvidersResponseTypeDef,
    ListOpenIDConnectProviderTagsResponseTypeDef,
    ListPoliciesGrantingServiceAccessResponseTypeDef,
    ListPoliciesResponseTypeDef,
    ListPolicyTagsResponseTypeDef,
    ListPolicyVersionsResponseTypeDef,
    ListRolePoliciesResponseTypeDef,
    ListRolesResponseTypeDef,
    ListRoleTagsResponseTypeDef,
    ListSAMLProvidersResponseTypeDef,
    ListSAMLProviderTagsResponseTypeDef,
    ListServerCertificatesResponseTypeDef,
    ListServerCertificateTagsResponseTypeDef,
    ListServiceSpecificCredentialsResponseTypeDef,
    ListSigningCertificatesResponseTypeDef,
    ListSSHPublicKeysResponseTypeDef,
    ListUserPoliciesResponseTypeDef,
    ListUsersResponseTypeDef,
    ListUserTagsResponseTypeDef,
    ListVirtualMFADevicesResponseTypeDef,
    ResetServiceSpecificCredentialResponseTypeDef,
    SimulatePolicyResponseTypeDef,
    TagTypeDef,
    UpdateRoleDescriptionResponseTypeDef,
    UpdateSAMLProviderResponseTypeDef,
    UploadServerCertificateResponseTypeDef,
    UploadSigningCertificateResponseTypeDef,
    UploadSSHPublicKeyResponseTypeDef,
)
from .waiter import (
    InstanceProfileExistsWaiter,
    PolicyExistsWaiter,
    RoleExistsWaiter,
    UserExistsWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IAMClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    CredentialReportExpiredException: Type[BotocoreClientError]
    CredentialReportNotPresentException: Type[BotocoreClientError]
    CredentialReportNotReadyException: Type[BotocoreClientError]
    DeleteConflictException: Type[BotocoreClientError]
    DuplicateCertificateException: Type[BotocoreClientError]
    DuplicateSSHPublicKeyException: Type[BotocoreClientError]
    EntityAlreadyExistsException: Type[BotocoreClientError]
    EntityTemporarilyUnmodifiableException: Type[BotocoreClientError]
    InvalidAuthenticationCodeException: Type[BotocoreClientError]
    InvalidCertificateException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidPublicKeyException: Type[BotocoreClientError]
    InvalidUserTypeException: Type[BotocoreClientError]
    KeyPairMismatchException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MalformedCertificateException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    NoSuchEntityException: Type[BotocoreClientError]
    PasswordPolicyViolationException: Type[BotocoreClientError]
    PolicyEvaluationException: Type[BotocoreClientError]
    PolicyNotAttachableException: Type[BotocoreClientError]
    ReportGenerationLimitExceededException: Type[BotocoreClientError]
    ServiceFailureException: Type[BotocoreClientError]
    ServiceNotSupportedException: Type[BotocoreClientError]
    UnmodifiableEntityException: Type[BotocoreClientError]
    UnrecognizedPublicKeyEncodingException: Type[BotocoreClientError]


class IAMClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_client_id_to_open_id_connect_provider(
        self, *, OpenIDConnectProviderArn: str, ClientID: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.add_client_id_to_open_id_connect_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#add_client_id_to_open_id_connect_provider)
        """

    def add_role_to_instance_profile(self, *, InstanceProfileName: str, RoleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.add_role_to_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#add_role_to_instance_profile)
        """

    def add_user_to_group(self, *, GroupName: str, UserName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.add_user_to_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#add_user_to_group)
        """

    def attach_group_policy(self, *, GroupName: str, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.attach_group_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#attach_group_policy)
        """

    def attach_role_policy(self, *, RoleName: str, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.attach_role_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#attach_role_policy)
        """

    def attach_user_policy(self, *, UserName: str, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.attach_user_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#attach_user_policy)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#can_paginate)
        """

    def change_password(self, *, OldPassword: str, NewPassword: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.change_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#change_password)
        """

    def create_access_key(self, *, UserName: str = None) -> CreateAccessKeyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.create_access_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#create_access_key)
        """

    def create_account_alias(self, *, AccountAlias: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.create_account_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#create_account_alias)
        """

    def create_group(self, *, GroupName: str, Path: str = None) -> CreateGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.create_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#create_group)
        """

    def create_instance_profile(
        self, *, InstanceProfileName: str, Path: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateInstanceProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.create_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#create_instance_profile)
        """

    def create_login_profile(
        self, *, UserName: str, Password: str, PasswordResetRequired: bool = None
    ) -> CreateLoginProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.create_login_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#create_login_profile)
        """

    def create_open_id_connect_provider(
        self,
        *,
        Url: str,
        ThumbprintList: List[str],
        ClientIDList: List[str] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateOpenIDConnectProviderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.create_open_id_connect_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#create_open_id_connect_provider)
        """

    def create_policy(
        self,
        *,
        PolicyName: str,
        PolicyDocument: str,
        Path: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreatePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.create_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#create_policy)
        """

    def create_policy_version(
        self, *, PolicyArn: str, PolicyDocument: str, SetAsDefault: bool = None
    ) -> CreatePolicyVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.create_policy_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#create_policy_version)
        """

    def create_role(
        self,
        *,
        RoleName: str,
        AssumeRolePolicyDocument: str,
        Path: str = None,
        Description: str = None,
        MaxSessionDuration: int = None,
        PermissionsBoundary: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateRoleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.create_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#create_role)
        """

    def create_saml_provider(
        self, *, SAMLMetadataDocument: str, Name: str, Tags: List["TagTypeDef"] = None
    ) -> CreateSAMLProviderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.create_saml_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#create_saml_provider)
        """

    def create_service_linked_role(
        self, *, AWSServiceName: str, Description: str = None, CustomSuffix: str = None
    ) -> CreateServiceLinkedRoleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.create_service_linked_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#create_service_linked_role)
        """

    def create_service_specific_credential(
        self, *, UserName: str, ServiceName: str
    ) -> CreateServiceSpecificCredentialResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.create_service_specific_credential)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#create_service_specific_credential)
        """

    def create_user(
        self,
        *,
        UserName: str,
        Path: str = None,
        PermissionsBoundary: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#create_user)
        """

    def create_virtual_mfa_device(
        self, *, VirtualMFADeviceName: str, Path: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateVirtualMFADeviceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.create_virtual_mfa_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#create_virtual_mfa_device)
        """

    def deactivate_mfa_device(self, *, UserName: str, SerialNumber: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.deactivate_mfa_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#deactivate_mfa_device)
        """

    def delete_access_key(self, *, AccessKeyId: str, UserName: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_access_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_access_key)
        """

    def delete_account_alias(self, *, AccountAlias: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_account_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_account_alias)
        """

    def delete_account_password_policy(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_account_password_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_account_password_policy)
        """

    def delete_group(self, *, GroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_group)
        """

    def delete_group_policy(self, *, GroupName: str, PolicyName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_group_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_group_policy)
        """

    def delete_instance_profile(self, *, InstanceProfileName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_instance_profile)
        """

    def delete_login_profile(self, *, UserName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_login_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_login_profile)
        """

    def delete_open_id_connect_provider(self, *, OpenIDConnectProviderArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_open_id_connect_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_open_id_connect_provider)
        """

    def delete_policy(self, *, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_policy)
        """

    def delete_policy_version(self, *, PolicyArn: str, VersionId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_policy_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_policy_version)
        """

    def delete_role(self, *, RoleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_role)
        """

    def delete_role_permissions_boundary(self, *, RoleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_role_permissions_boundary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_role_permissions_boundary)
        """

    def delete_role_policy(self, *, RoleName: str, PolicyName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_role_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_role_policy)
        """

    def delete_saml_provider(self, *, SAMLProviderArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_saml_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_saml_provider)
        """

    def delete_server_certificate(self, *, ServerCertificateName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_server_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_server_certificate)
        """

    def delete_service_linked_role(
        self, *, RoleName: str
    ) -> DeleteServiceLinkedRoleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_service_linked_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_service_linked_role)
        """

    def delete_service_specific_credential(
        self, *, ServiceSpecificCredentialId: str, UserName: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_service_specific_credential)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_service_specific_credential)
        """

    def delete_signing_certificate(self, *, CertificateId: str, UserName: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_signing_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_signing_certificate)
        """

    def delete_ssh_public_key(self, *, UserName: str, SSHPublicKeyId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_ssh_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_ssh_public_key)
        """

    def delete_user(self, *, UserName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_user)
        """

    def delete_user_permissions_boundary(self, *, UserName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_user_permissions_boundary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_user_permissions_boundary)
        """

    def delete_user_policy(self, *, UserName: str, PolicyName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_user_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_user_policy)
        """

    def delete_virtual_mfa_device(self, *, SerialNumber: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.delete_virtual_mfa_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#delete_virtual_mfa_device)
        """

    def detach_group_policy(self, *, GroupName: str, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.detach_group_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#detach_group_policy)
        """

    def detach_role_policy(self, *, RoleName: str, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.detach_role_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#detach_role_policy)
        """

    def detach_user_policy(self, *, UserName: str, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.detach_user_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#detach_user_policy)
        """

    def enable_mfa_device(
        self,
        *,
        UserName: str,
        SerialNumber: str,
        AuthenticationCode1: str,
        AuthenticationCode2: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.enable_mfa_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#enable_mfa_device)
        """

    def generate_credential_report(self) -> GenerateCredentialReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.generate_credential_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#generate_credential_report)
        """

    def generate_organizations_access_report(
        self, *, EntityPath: str, OrganizationsPolicyId: str = None
    ) -> GenerateOrganizationsAccessReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.generate_organizations_access_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#generate_organizations_access_report)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#generate_presigned_url)
        """

    def generate_service_last_accessed_details(
        self, *, Arn: str, Granularity: AccessAdvisorUsageGranularityTypeType = None
    ) -> GenerateServiceLastAccessedDetailsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.generate_service_last_accessed_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#generate_service_last_accessed_details)
        """

    def get_access_key_last_used(self, *, AccessKeyId: str) -> GetAccessKeyLastUsedResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_access_key_last_used)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_access_key_last_used)
        """

    def get_account_authorization_details(
        self, *, Filter: List[EntityTypeType] = None, MaxItems: int = None, Marker: str = None
    ) -> GetAccountAuthorizationDetailsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_account_authorization_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_account_authorization_details)
        """

    def get_account_password_policy(self) -> GetAccountPasswordPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_account_password_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_account_password_policy)
        """

    def get_account_summary(self) -> GetAccountSummaryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_account_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_account_summary)
        """

    def get_context_keys_for_custom_policy(
        self, *, PolicyInputList: List[str]
    ) -> GetContextKeysForPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_context_keys_for_custom_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_context_keys_for_custom_policy)
        """

    def get_context_keys_for_principal_policy(
        self, *, PolicySourceArn: str, PolicyInputList: List[str] = None
    ) -> GetContextKeysForPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_context_keys_for_principal_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_context_keys_for_principal_policy)
        """

    def get_credential_report(self) -> GetCredentialReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_credential_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_credential_report)
        """

    def get_group(
        self, *, GroupName: str, Marker: str = None, MaxItems: int = None
    ) -> GetGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_group)
        """

    def get_group_policy(self, *, GroupName: str, PolicyName: str) -> GetGroupPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_group_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_group_policy)
        """

    def get_instance_profile(
        self, *, InstanceProfileName: str
    ) -> GetInstanceProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_instance_profile)
        """

    def get_login_profile(self, *, UserName: str) -> GetLoginProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_login_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_login_profile)
        """

    def get_open_id_connect_provider(
        self, *, OpenIDConnectProviderArn: str
    ) -> GetOpenIDConnectProviderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_open_id_connect_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_open_id_connect_provider)
        """

    def get_organizations_access_report(
        self,
        *,
        JobId: str,
        MaxItems: int = None,
        Marker: str = None,
        SortKey: sortKeyTypeType = None
    ) -> GetOrganizationsAccessReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_organizations_access_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_organizations_access_report)
        """

    def get_policy(self, *, PolicyArn: str) -> GetPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_policy)
        """

    def get_policy_version(
        self, *, PolicyArn: str, VersionId: str
    ) -> GetPolicyVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_policy_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_policy_version)
        """

    def get_role(self, *, RoleName: str) -> GetRoleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_role)
        """

    def get_role_policy(self, *, RoleName: str, PolicyName: str) -> GetRolePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_role_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_role_policy)
        """

    def get_saml_provider(self, *, SAMLProviderArn: str) -> GetSAMLProviderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_saml_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_saml_provider)
        """

    def get_server_certificate(
        self, *, ServerCertificateName: str
    ) -> GetServerCertificateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_server_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_server_certificate)
        """

    def get_service_last_accessed_details(
        self, *, JobId: str, MaxItems: int = None, Marker: str = None
    ) -> GetServiceLastAccessedDetailsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_service_last_accessed_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_service_last_accessed_details)
        """

    def get_service_last_accessed_details_with_entities(
        self, *, JobId: str, ServiceNamespace: str, MaxItems: int = None, Marker: str = None
    ) -> GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_service_last_accessed_details_with_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_service_last_accessed_details_with_entities)
        """

    def get_service_linked_role_deletion_status(
        self, *, DeletionTaskId: str
    ) -> GetServiceLinkedRoleDeletionStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_service_linked_role_deletion_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_service_linked_role_deletion_status)
        """

    def get_ssh_public_key(
        self, *, UserName: str, SSHPublicKeyId: str, Encoding: encodingTypeType
    ) -> GetSSHPublicKeyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_ssh_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_ssh_public_key)
        """

    def get_user(self, *, UserName: str = None) -> GetUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_user)
        """

    def get_user_policy(self, *, UserName: str, PolicyName: str) -> GetUserPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.get_user_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#get_user_policy)
        """

    def list_access_keys(
        self, *, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListAccessKeysResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_access_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_access_keys)
        """

    def list_account_aliases(
        self, *, Marker: str = None, MaxItems: int = None
    ) -> ListAccountAliasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_account_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_account_aliases)
        """

    def list_attached_group_policies(
        self, *, GroupName: str, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListAttachedGroupPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_attached_group_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_attached_group_policies)
        """

    def list_attached_role_policies(
        self, *, RoleName: str, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListAttachedRolePoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_attached_role_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_attached_role_policies)
        """

    def list_attached_user_policies(
        self, *, UserName: str, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListAttachedUserPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_attached_user_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_attached_user_policies)
        """

    def list_entities_for_policy(
        self,
        *,
        PolicyArn: str,
        EntityFilter: EntityTypeType = None,
        PathPrefix: str = None,
        PolicyUsageFilter: PolicyUsageTypeType = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> ListEntitiesForPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_entities_for_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_entities_for_policy)
        """

    def list_group_policies(
        self, *, GroupName: str, Marker: str = None, MaxItems: int = None
    ) -> ListGroupPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_group_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_group_policies)
        """

    def list_groups(
        self, *, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_groups)
        """

    def list_groups_for_user(
        self, *, UserName: str, Marker: str = None, MaxItems: int = None
    ) -> ListGroupsForUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_groups_for_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_groups_for_user)
        """

    def list_instance_profile_tags(
        self, *, InstanceProfileName: str, Marker: str = None, MaxItems: int = None
    ) -> ListInstanceProfileTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_instance_profile_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_instance_profile_tags)
        """

    def list_instance_profiles(
        self, *, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListInstanceProfilesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_instance_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_instance_profiles)
        """

    def list_instance_profiles_for_role(
        self, *, RoleName: str, Marker: str = None, MaxItems: int = None
    ) -> ListInstanceProfilesForRoleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_instance_profiles_for_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_instance_profiles_for_role)
        """

    def list_mfa_device_tags(
        self, *, SerialNumber: str, Marker: str = None, MaxItems: int = None
    ) -> ListMFADeviceTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_mfa_device_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_mfa_device_tags)
        """

    def list_mfa_devices(
        self, *, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListMFADevicesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_mfa_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_mfa_devices)
        """

    def list_open_id_connect_provider_tags(
        self, *, OpenIDConnectProviderArn: str, Marker: str = None, MaxItems: int = None
    ) -> ListOpenIDConnectProviderTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_open_id_connect_provider_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_open_id_connect_provider_tags)
        """

    def list_open_id_connect_providers(self) -> ListOpenIDConnectProvidersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_open_id_connect_providers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_open_id_connect_providers)
        """

    def list_policies(
        self,
        *,
        Scope: policyScopeTypeType = None,
        OnlyAttached: bool = None,
        PathPrefix: str = None,
        PolicyUsageFilter: PolicyUsageTypeType = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> ListPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_policies)
        """

    def list_policies_granting_service_access(
        self, *, Arn: str, ServiceNamespaces: List[str], Marker: str = None
    ) -> ListPoliciesGrantingServiceAccessResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_policies_granting_service_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_policies_granting_service_access)
        """

    def list_policy_tags(
        self, *, PolicyArn: str, Marker: str = None, MaxItems: int = None
    ) -> ListPolicyTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_policy_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_policy_tags)
        """

    def list_policy_versions(
        self, *, PolicyArn: str, Marker: str = None, MaxItems: int = None
    ) -> ListPolicyVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_policy_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_policy_versions)
        """

    def list_role_policies(
        self, *, RoleName: str, Marker: str = None, MaxItems: int = None
    ) -> ListRolePoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_role_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_role_policies)
        """

    def list_role_tags(
        self, *, RoleName: str, Marker: str = None, MaxItems: int = None
    ) -> ListRoleTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_role_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_role_tags)
        """

    def list_roles(
        self, *, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListRolesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_roles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_roles)
        """

    def list_saml_provider_tags(
        self, *, SAMLProviderArn: str, Marker: str = None, MaxItems: int = None
    ) -> ListSAMLProviderTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_saml_provider_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_saml_provider_tags)
        """

    def list_saml_providers(self) -> ListSAMLProvidersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_saml_providers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_saml_providers)
        """

    def list_server_certificate_tags(
        self, *, ServerCertificateName: str, Marker: str = None, MaxItems: int = None
    ) -> ListServerCertificateTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_server_certificate_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_server_certificate_tags)
        """

    def list_server_certificates(
        self, *, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListServerCertificatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_server_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_server_certificates)
        """

    def list_service_specific_credentials(
        self, *, UserName: str = None, ServiceName: str = None
    ) -> ListServiceSpecificCredentialsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_service_specific_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_service_specific_credentials)
        """

    def list_signing_certificates(
        self, *, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListSigningCertificatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_signing_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_signing_certificates)
        """

    def list_ssh_public_keys(
        self, *, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListSSHPublicKeysResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_ssh_public_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_ssh_public_keys)
        """

    def list_user_policies(
        self, *, UserName: str, Marker: str = None, MaxItems: int = None
    ) -> ListUserPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_user_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_user_policies)
        """

    def list_user_tags(
        self, *, UserName: str, Marker: str = None, MaxItems: int = None
    ) -> ListUserTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_user_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_user_tags)
        """

    def list_users(
        self, *, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ListUsersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_users)
        """

    def list_virtual_mfa_devices(
        self,
        *,
        AssignmentStatus: assignmentStatusTypeType = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> ListVirtualMFADevicesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.list_virtual_mfa_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#list_virtual_mfa_devices)
        """

    def put_group_policy(self, *, GroupName: str, PolicyName: str, PolicyDocument: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.put_group_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#put_group_policy)
        """

    def put_role_permissions_boundary(self, *, RoleName: str, PermissionsBoundary: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.put_role_permissions_boundary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#put_role_permissions_boundary)
        """

    def put_role_policy(self, *, RoleName: str, PolicyName: str, PolicyDocument: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.put_role_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#put_role_policy)
        """

    def put_user_permissions_boundary(self, *, UserName: str, PermissionsBoundary: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.put_user_permissions_boundary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#put_user_permissions_boundary)
        """

    def put_user_policy(self, *, UserName: str, PolicyName: str, PolicyDocument: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.put_user_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#put_user_policy)
        """

    def remove_client_id_from_open_id_connect_provider(
        self, *, OpenIDConnectProviderArn: str, ClientID: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.remove_client_id_from_open_id_connect_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#remove_client_id_from_open_id_connect_provider)
        """

    def remove_role_from_instance_profile(self, *, InstanceProfileName: str, RoleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.remove_role_from_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#remove_role_from_instance_profile)
        """

    def remove_user_from_group(self, *, GroupName: str, UserName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.remove_user_from_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#remove_user_from_group)
        """

    def reset_service_specific_credential(
        self, *, ServiceSpecificCredentialId: str, UserName: str = None
    ) -> ResetServiceSpecificCredentialResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.reset_service_specific_credential)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#reset_service_specific_credential)
        """

    def resync_mfa_device(
        self,
        *,
        UserName: str,
        SerialNumber: str,
        AuthenticationCode1: str,
        AuthenticationCode2: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.resync_mfa_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#resync_mfa_device)
        """

    def set_default_policy_version(self, *, PolicyArn: str, VersionId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.set_default_policy_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#set_default_policy_version)
        """

    def set_security_token_service_preferences(
        self, *, GlobalEndpointTokenVersion: globalEndpointTokenVersionType
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.set_security_token_service_preferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#set_security_token_service_preferences)
        """

    def simulate_custom_policy(
        self,
        *,
        PolicyInputList: List[str],
        ActionNames: List[str],
        PermissionsBoundaryPolicyInputList: List[str] = None,
        ResourceArns: List[str] = None,
        ResourcePolicy: str = None,
        ResourceOwner: str = None,
        CallerArn: str = None,
        ContextEntries: List[ContextEntryTypeDef] = None,
        ResourceHandlingOption: str = None,
        MaxItems: int = None,
        Marker: str = None
    ) -> SimulatePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.simulate_custom_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#simulate_custom_policy)
        """

    def simulate_principal_policy(
        self,
        *,
        PolicySourceArn: str,
        ActionNames: List[str],
        PolicyInputList: List[str] = None,
        PermissionsBoundaryPolicyInputList: List[str] = None,
        ResourceArns: List[str] = None,
        ResourcePolicy: str = None,
        ResourceOwner: str = None,
        CallerArn: str = None,
        ContextEntries: List[ContextEntryTypeDef] = None,
        ResourceHandlingOption: str = None,
        MaxItems: int = None,
        Marker: str = None
    ) -> SimulatePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.simulate_principal_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#simulate_principal_policy)
        """

    def tag_instance_profile(self, *, InstanceProfileName: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.tag_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#tag_instance_profile)
        """

    def tag_mfa_device(self, *, SerialNumber: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.tag_mfa_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#tag_mfa_device)
        """

    def tag_open_id_connect_provider(
        self, *, OpenIDConnectProviderArn: str, Tags: List["TagTypeDef"]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.tag_open_id_connect_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#tag_open_id_connect_provider)
        """

    def tag_policy(self, *, PolicyArn: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.tag_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#tag_policy)
        """

    def tag_role(self, *, RoleName: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.tag_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#tag_role)
        """

    def tag_saml_provider(self, *, SAMLProviderArn: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.tag_saml_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#tag_saml_provider)
        """

    def tag_server_certificate(
        self, *, ServerCertificateName: str, Tags: List["TagTypeDef"]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.tag_server_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#tag_server_certificate)
        """

    def tag_user(self, *, UserName: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.tag_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#tag_user)
        """

    def untag_instance_profile(self, *, InstanceProfileName: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.untag_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#untag_instance_profile)
        """

    def untag_mfa_device(self, *, SerialNumber: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.untag_mfa_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#untag_mfa_device)
        """

    def untag_open_id_connect_provider(
        self, *, OpenIDConnectProviderArn: str, TagKeys: List[str]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.untag_open_id_connect_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#untag_open_id_connect_provider)
        """

    def untag_policy(self, *, PolicyArn: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.untag_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#untag_policy)
        """

    def untag_role(self, *, RoleName: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.untag_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#untag_role)
        """

    def untag_saml_provider(self, *, SAMLProviderArn: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.untag_saml_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#untag_saml_provider)
        """

    def untag_server_certificate(self, *, ServerCertificateName: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.untag_server_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#untag_server_certificate)
        """

    def untag_user(self, *, UserName: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.untag_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#untag_user)
        """

    def update_access_key(
        self, *, AccessKeyId: str, Status: statusTypeType, UserName: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.update_access_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#update_access_key)
        """

    def update_account_password_policy(
        self,
        *,
        MinimumPasswordLength: int = None,
        RequireSymbols: bool = None,
        RequireNumbers: bool = None,
        RequireUppercaseCharacters: bool = None,
        RequireLowercaseCharacters: bool = None,
        AllowUsersToChangePassword: bool = None,
        MaxPasswordAge: int = None,
        PasswordReusePrevention: int = None,
        HardExpiry: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.update_account_password_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#update_account_password_policy)
        """

    def update_assume_role_policy(self, *, RoleName: str, PolicyDocument: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.update_assume_role_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#update_assume_role_policy)
        """

    def update_group(
        self, *, GroupName: str, NewPath: str = None, NewGroupName: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.update_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#update_group)
        """

    def update_login_profile(
        self, *, UserName: str, Password: str = None, PasswordResetRequired: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.update_login_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#update_login_profile)
        """

    def update_open_id_connect_provider_thumbprint(
        self, *, OpenIDConnectProviderArn: str, ThumbprintList: List[str]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.update_open_id_connect_provider_thumbprint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#update_open_id_connect_provider_thumbprint)
        """

    def update_role(
        self, *, RoleName: str, Description: str = None, MaxSessionDuration: int = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.update_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#update_role)
        """

    def update_role_description(
        self, *, RoleName: str, Description: str
    ) -> UpdateRoleDescriptionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.update_role_description)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#update_role_description)
        """

    def update_saml_provider(
        self, *, SAMLMetadataDocument: str, SAMLProviderArn: str
    ) -> UpdateSAMLProviderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.update_saml_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#update_saml_provider)
        """

    def update_server_certificate(
        self,
        *,
        ServerCertificateName: str,
        NewPath: str = None,
        NewServerCertificateName: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.update_server_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#update_server_certificate)
        """

    def update_service_specific_credential(
        self, *, ServiceSpecificCredentialId: str, Status: statusTypeType, UserName: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.update_service_specific_credential)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#update_service_specific_credential)
        """

    def update_signing_certificate(
        self, *, CertificateId: str, Status: statusTypeType, UserName: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.update_signing_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#update_signing_certificate)
        """

    def update_ssh_public_key(
        self, *, UserName: str, SSHPublicKeyId: str, Status: statusTypeType
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.update_ssh_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#update_ssh_public_key)
        """

    def update_user(self, *, UserName: str, NewPath: str = None, NewUserName: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#update_user)
        """

    def upload_server_certificate(
        self,
        *,
        ServerCertificateName: str,
        CertificateBody: str,
        PrivateKey: str,
        Path: str = None,
        CertificateChain: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> UploadServerCertificateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.upload_server_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#upload_server_certificate)
        """

    def upload_signing_certificate(
        self, *, CertificateBody: str, UserName: str = None
    ) -> UploadSigningCertificateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.upload_signing_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#upload_signing_certificate)
        """

    def upload_ssh_public_key(
        self, *, UserName: str, SSHPublicKeyBody: str
    ) -> UploadSSHPublicKeyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Client.upload_ssh_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/client.html#upload_ssh_public_key)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_account_authorization_details"]
    ) -> GetAccountAuthorizationDetailsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.GetAccountAuthorizationDetails)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#getaccountauthorizationdetailspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_group"]) -> GetGroupPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.GetGroup)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#getgrouppaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_access_keys"]) -> ListAccessKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListAccessKeys)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listaccesskeyspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_aliases"]
    ) -> ListAccountAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListAccountAliases)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listaccountaliasespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_group_policies"]
    ) -> ListAttachedGroupPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListAttachedGroupPolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listattachedgrouppoliciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_role_policies"]
    ) -> ListAttachedRolePoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListAttachedRolePolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listattachedrolepoliciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_user_policies"]
    ) -> ListAttachedUserPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListAttachedUserPolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listattacheduserpoliciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_entities_for_policy"]
    ) -> ListEntitiesForPolicyPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListEntitiesForPolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listentitiesforpolicypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_group_policies"]
    ) -> ListGroupPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListGroupPolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listgrouppoliciespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listgroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_groups_for_user"]
    ) -> ListGroupsForUserPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListGroupsForUser)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listgroupsforuserpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_profiles"]
    ) -> ListInstanceProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListInstanceProfiles)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listinstanceprofilespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_profiles_for_role"]
    ) -> ListInstanceProfilesForRolePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListInstanceProfilesForRole)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listinstanceprofilesforrolepaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_mfa_devices"]) -> ListMFADevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListMFADevices)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listmfadevicespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_policies"]) -> ListPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListPolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listpoliciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policy_versions"]
    ) -> ListPolicyVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListPolicyVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listpolicyversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_role_policies"]
    ) -> ListRolePoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListRolePolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listrolepoliciespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_roles"]) -> ListRolesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListRoles)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listrolespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ssh_public_keys"]
    ) -> ListSSHPublicKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListSSHPublicKeys)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listsshpublickeyspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_server_certificates"]
    ) -> ListServerCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListServerCertificates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listservercertificatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signing_certificates"]
    ) -> ListSigningCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListSigningCertificates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listsigningcertificatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_policies"]
    ) -> ListUserPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListUserPolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listuserpoliciespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_user_tags"]) -> ListUserTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListUserTags)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listusertagspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListUsers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listuserspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_virtual_mfa_devices"]
    ) -> ListVirtualMFADevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.ListVirtualMFADevices)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#listvirtualmfadevicespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["simulate_custom_policy"]
    ) -> SimulateCustomPolicyPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.SimulateCustomPolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#simulatecustompolicypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["simulate_principal_policy"]
    ) -> SimulatePrincipalPolicyPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Paginator.SimulatePrincipalPolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators.html#simulateprincipalpolicypaginator)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["instance_profile_exists"]
    ) -> InstanceProfileExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Waiter.instance_profile_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters.html#instanceprofileexistswaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["policy_exists"]) -> PolicyExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Waiter.policy_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters.html#policyexistswaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["role_exists"]) -> RoleExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Waiter.role_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters.html#roleexistswaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["user_exists"]) -> UserExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/iam.html#IAM.Waiter.user_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/waiters.html#userexistswaiter)
        """
