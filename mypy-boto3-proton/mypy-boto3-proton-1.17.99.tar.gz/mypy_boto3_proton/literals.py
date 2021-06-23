"""
Type annotations for proton service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/literals.html)

Usage::

    ```python
    from mypy_boto3_proton.literals import DeploymentStatusType

    data: DeploymentStatusType = "CANCELLED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DeploymentStatusType",
    "DeploymentUpdateTypeType",
    "EnvironmentAccountConnectionRequesterAccountTypeType",
    "EnvironmentAccountConnectionStatusType",
    "ListEnvironmentAccountConnectionsPaginatorName",
    "ListEnvironmentTemplateVersionsPaginatorName",
    "ListEnvironmentTemplatesPaginatorName",
    "ListEnvironmentsPaginatorName",
    "ListServiceInstancesPaginatorName",
    "ListServiceTemplateVersionsPaginatorName",
    "ListServiceTemplatesPaginatorName",
    "ListServicesPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ProvisioningType",
    "ServiceStatusType",
    "TemplateVersionStatusType",
)


DeploymentStatusType = Literal[
    "CANCELLED",
    "CANCELLING",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "FAILED",
    "IN_PROGRESS",
    "SUCCEEDED",
]
DeploymentUpdateTypeType = Literal["CURRENT_VERSION", "MAJOR_VERSION", "MINOR_VERSION", "NONE"]
EnvironmentAccountConnectionRequesterAccountTypeType = Literal[
    "ENVIRONMENT_ACCOUNT", "MANAGEMENT_ACCOUNT"
]
EnvironmentAccountConnectionStatusType = Literal["CONNECTED", "PENDING", "REJECTED"]
ListEnvironmentAccountConnectionsPaginatorName = Literal["list_environment_account_connections"]
ListEnvironmentTemplateVersionsPaginatorName = Literal["list_environment_template_versions"]
ListEnvironmentTemplatesPaginatorName = Literal["list_environment_templates"]
ListEnvironmentsPaginatorName = Literal["list_environments"]
ListServiceInstancesPaginatorName = Literal["list_service_instances"]
ListServiceTemplateVersionsPaginatorName = Literal["list_service_template_versions"]
ListServiceTemplatesPaginatorName = Literal["list_service_templates"]
ListServicesPaginatorName = Literal["list_services"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ProvisioningType = Literal["CUSTOMER_MANAGED"]
ServiceStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATE_FAILED_CLEANUP_COMPLETE",
    "CREATE_FAILED_CLEANUP_FAILED",
    "CREATE_FAILED_CLEANUP_IN_PROGRESS",
    "CREATE_IN_PROGRESS",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "UPDATE_COMPLETE_CLEANUP_FAILED",
    "UPDATE_FAILED",
    "UPDATE_FAILED_CLEANUP_COMPLETE",
    "UPDATE_FAILED_CLEANUP_FAILED",
    "UPDATE_FAILED_CLEANUP_IN_PROGRESS",
    "UPDATE_IN_PROGRESS",
]
TemplateVersionStatusType = Literal[
    "DRAFT", "PUBLISHED", "REGISTRATION_FAILED", "REGISTRATION_IN_PROGRESS"
]
