"""
Type annotations for fms service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/literals.html)

Usage::

    ```python
    from mypy_boto3_fms.literals import AccountRoleStatusType

    data: AccountRoleStatusType = "CREATING"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccountRoleStatusType",
    "CustomerPolicyScopeIdTypeType",
    "DependentServiceNameType",
    "ListComplianceStatusPaginatorName",
    "ListMemberAccountsPaginatorName",
    "ListPoliciesPaginatorName",
    "PolicyComplianceStatusTypeType",
    "RemediationActionTypeType",
    "SecurityServiceTypeType",
    "ViolationReasonType",
)


AccountRoleStatusType = Literal["CREATING", "DELETED", "DELETING", "PENDING_DELETION", "READY"]
CustomerPolicyScopeIdTypeType = Literal["ACCOUNT", "ORG_UNIT"]
DependentServiceNameType = Literal["AWSCONFIG", "AWSSHIELD_ADVANCED", "AWSVPC", "AWSWAF"]
ListComplianceStatusPaginatorName = Literal["list_compliance_status"]
ListMemberAccountsPaginatorName = Literal["list_member_accounts"]
ListPoliciesPaginatorName = Literal["list_policies"]
PolicyComplianceStatusTypeType = Literal["COMPLIANT", "NON_COMPLIANT"]
RemediationActionTypeType = Literal["MODIFY", "REMOVE"]
SecurityServiceTypeType = Literal[
    "DNS_FIREWALL",
    "NETWORK_FIREWALL",
    "SECURITY_GROUPS_COMMON",
    "SECURITY_GROUPS_CONTENT_AUDIT",
    "SECURITY_GROUPS_USAGE_AUDIT",
    "SHIELD_ADVANCED",
    "WAF",
    "WAFV2",
]
ViolationReasonType = Literal[
    "FMS_CREATED_SECURITY_GROUP_EDITED",
    "MISSING_EXPECTED_ROUTE_TABLE",
    "MISSING_FIREWALL",
    "MISSING_FIREWALL_SUBNET_IN_AZ",
    "NETWORK_FIREWALL_POLICY_MODIFIED",
    "RESOURCE_INCORRECT_WEB_ACL",
    "RESOURCE_MISSING_DNS_FIREWALL",
    "RESOURCE_MISSING_SECURITY_GROUP",
    "RESOURCE_MISSING_SHIELD_PROTECTION",
    "RESOURCE_MISSING_WEB_ACL",
    "RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION",
    "RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP",
    "SECURITY_GROUP_REDUNDANT",
    "SECURITY_GROUP_UNUSED",
    "WEB_ACL_MISSING_RULE_GROUP",
]
