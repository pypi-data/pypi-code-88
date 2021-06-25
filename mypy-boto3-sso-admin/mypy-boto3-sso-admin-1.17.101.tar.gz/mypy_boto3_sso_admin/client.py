"""
Type annotations for sso-admin service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sso_admin import SSOAdminClient

    client: SSOAdminClient = boto3.client("sso-admin")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import PrincipalTypeType, ProvisioningStatusType, ProvisionTargetTypeType
from .paginator import (
    ListAccountAssignmentCreationStatusPaginator,
    ListAccountAssignmentDeletionStatusPaginator,
    ListAccountAssignmentsPaginator,
    ListAccountsForProvisionedPermissionSetPaginator,
    ListInstancesPaginator,
    ListManagedPoliciesInPermissionSetPaginator,
    ListPermissionSetProvisioningStatusPaginator,
    ListPermissionSetsPaginator,
    ListPermissionSetsProvisionedToAccountPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    CreateAccountAssignmentResponseTypeDef,
    CreatePermissionSetResponseTypeDef,
    DeleteAccountAssignmentResponseTypeDef,
    DescribeAccountAssignmentCreationStatusResponseTypeDef,
    DescribeAccountAssignmentDeletionStatusResponseTypeDef,
    DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef,
    DescribePermissionSetProvisioningStatusResponseTypeDef,
    DescribePermissionSetResponseTypeDef,
    GetInlinePolicyForPermissionSetResponseTypeDef,
    InstanceAccessControlAttributeConfigurationTypeDef,
    ListAccountAssignmentCreationStatusResponseTypeDef,
    ListAccountAssignmentDeletionStatusResponseTypeDef,
    ListAccountAssignmentsResponseTypeDef,
    ListAccountsForProvisionedPermissionSetResponseTypeDef,
    ListInstancesResponseTypeDef,
    ListManagedPoliciesInPermissionSetResponseTypeDef,
    ListPermissionSetProvisioningStatusResponseTypeDef,
    ListPermissionSetsProvisionedToAccountResponseTypeDef,
    ListPermissionSetsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OperationStatusFilterTypeDef,
    ProvisionPermissionSetResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SSOAdminClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class SSOAdminClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def attach_managed_policy_to_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str, ManagedPolicyArn: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.attach_managed_policy_to_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#attach_managed_policy_to_permission_set)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#can_paginate)
        """

    def create_account_assignment(
        self,
        *,
        InstanceArn: str,
        TargetId: str,
        TargetType: Literal["AWS_ACCOUNT"],
        PermissionSetArn: str,
        PrincipalType: PrincipalTypeType,
        PrincipalId: str
    ) -> CreateAccountAssignmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.create_account_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#create_account_assignment)
        """

    def create_instance_access_control_attribute_configuration(
        self,
        *,
        InstanceArn: str,
        InstanceAccessControlAttributeConfiguration: "InstanceAccessControlAttributeConfigurationTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.create_instance_access_control_attribute_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#create_instance_access_control_attribute_configuration)
        """

    def create_permission_set(
        self,
        *,
        Name: str,
        InstanceArn: str,
        Description: str = None,
        SessionDuration: str = None,
        RelayState: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreatePermissionSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.create_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#create_permission_set)
        """

    def delete_account_assignment(
        self,
        *,
        InstanceArn: str,
        TargetId: str,
        TargetType: Literal["AWS_ACCOUNT"],
        PermissionSetArn: str,
        PrincipalType: PrincipalTypeType,
        PrincipalId: str
    ) -> DeleteAccountAssignmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.delete_account_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_account_assignment)
        """

    def delete_inline_policy_from_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.delete_inline_policy_from_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_inline_policy_from_permission_set)
        """

    def delete_instance_access_control_attribute_configuration(
        self, *, InstanceArn: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.delete_instance_access_control_attribute_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_instance_access_control_attribute_configuration)
        """

    def delete_permission_set(self, *, InstanceArn: str, PermissionSetArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.delete_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_permission_set)
        """

    def describe_account_assignment_creation_status(
        self, *, InstanceArn: str, AccountAssignmentCreationRequestId: str
    ) -> DescribeAccountAssignmentCreationStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.describe_account_assignment_creation_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_account_assignment_creation_status)
        """

    def describe_account_assignment_deletion_status(
        self, *, InstanceArn: str, AccountAssignmentDeletionRequestId: str
    ) -> DescribeAccountAssignmentDeletionStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.describe_account_assignment_deletion_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_account_assignment_deletion_status)
        """

    def describe_instance_access_control_attribute_configuration(
        self, *, InstanceArn: str
    ) -> DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.describe_instance_access_control_attribute_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_instance_access_control_attribute_configuration)
        """

    def describe_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> DescribePermissionSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.describe_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_permission_set)
        """

    def describe_permission_set_provisioning_status(
        self, *, InstanceArn: str, ProvisionPermissionSetRequestId: str
    ) -> DescribePermissionSetProvisioningStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.describe_permission_set_provisioning_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_permission_set_provisioning_status)
        """

    def detach_managed_policy_from_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str, ManagedPolicyArn: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.detach_managed_policy_from_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#detach_managed_policy_from_permission_set)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#generate_presigned_url)
        """

    def get_inline_policy_for_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> GetInlinePolicyForPermissionSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.get_inline_policy_for_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#get_inline_policy_for_permission_set)
        """

    def list_account_assignment_creation_status(
        self,
        *,
        InstanceArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filter: OperationStatusFilterTypeDef = None
    ) -> ListAccountAssignmentCreationStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignment_creation_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_account_assignment_creation_status)
        """

    def list_account_assignment_deletion_status(
        self,
        *,
        InstanceArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filter: OperationStatusFilterTypeDef = None
    ) -> ListAccountAssignmentDeletionStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignment_deletion_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_account_assignment_deletion_status)
        """

    def list_account_assignments(
        self,
        *,
        InstanceArn: str,
        AccountId: str,
        PermissionSetArn: str,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListAccountAssignmentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_account_assignments)
        """

    def list_accounts_for_provisioned_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        ProvisioningStatus: ProvisioningStatusType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListAccountsForProvisionedPermissionSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.list_accounts_for_provisioned_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_accounts_for_provisioned_permission_set)
        """

    def list_instances(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListInstancesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.list_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_instances)
        """

    def list_managed_policies_in_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListManagedPoliciesInPermissionSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.list_managed_policies_in_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_managed_policies_in_permission_set)
        """

    def list_permission_set_provisioning_status(
        self,
        *,
        InstanceArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filter: OperationStatusFilterTypeDef = None
    ) -> ListPermissionSetProvisioningStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_set_provisioning_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_permission_set_provisioning_status)
        """

    def list_permission_sets(
        self, *, InstanceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListPermissionSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_permission_sets)
        """

    def list_permission_sets_provisioned_to_account(
        self,
        *,
        InstanceArn: str,
        AccountId: str,
        ProvisioningStatus: ProvisioningStatusType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListPermissionSetsProvisionedToAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_sets_provisioned_to_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_permission_sets_provisioned_to_account)
        """

    def list_tags_for_resource(
        self, *, InstanceArn: str, ResourceArn: str, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_tags_for_resource)
        """

    def provision_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        TargetType: ProvisionTargetTypeType,
        TargetId: str = None
    ) -> ProvisionPermissionSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.provision_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#provision_permission_set)
        """

    def put_inline_policy_to_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str, InlinePolicy: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.put_inline_policy_to_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#put_inline_policy_to_permission_set)
        """

    def tag_resource(
        self, *, InstanceArn: str, ResourceArn: str, Tags: List["TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#tag_resource)
        """

    def untag_resource(
        self, *, InstanceArn: str, ResourceArn: str, TagKeys: List[str]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#untag_resource)
        """

    def update_instance_access_control_attribute_configuration(
        self,
        *,
        InstanceArn: str,
        InstanceAccessControlAttributeConfiguration: "InstanceAccessControlAttributeConfigurationTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.update_instance_access_control_attribute_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#update_instance_access_control_attribute_configuration)
        """

    def update_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        Description: str = None,
        SessionDuration: str = None,
        RelayState: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Client.update_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#update_permission_set)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignment_creation_status"]
    ) -> ListAccountAssignmentCreationStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentCreationStatus)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentcreationstatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignment_deletion_status"]
    ) -> ListAccountAssignmentDeletionStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentDeletionStatus)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentdeletionstatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignments"]
    ) -> ListAccountAssignmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignments)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accounts_for_provisioned_permission_set"]
    ) -> ListAccountsForProvisionedPermissionSetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountsForProvisionedPermissionSet)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountsforprovisionedpermissionsetpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Paginator.ListInstances)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_managed_policies_in_permission_set"]
    ) -> ListManagedPoliciesInPermissionSetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Paginator.ListManagedPoliciesInPermissionSet)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listmanagedpoliciesinpermissionsetpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_permission_set_provisioning_status"]
    ) -> ListPermissionSetProvisioningStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetProvisioningStatus)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listpermissionsetprovisioningstatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_permission_sets"]
    ) -> ListPermissionSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listpermissionsetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_permission_sets_provisioned_to_account"]
    ) -> ListPermissionSetsProvisionedToAccountPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetsProvisionedToAccount)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listpermissionsetsprovisionedtoaccountpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sso-admin.html#SSOAdmin.Paginator.ListTagsForResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listtagsforresourcepaginator)
        """
