"""
Type annotations for proton service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/type_defs.html)

Usage::

    ```python
    from mypy_boto3_proton.type_defs import AcceptEnvironmentAccountConnectionInputTypeDef

    data: AcceptEnvironmentAccountConnectionInputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    DeploymentStatusType,
    DeploymentUpdateTypeType,
    EnvironmentAccountConnectionRequesterAccountTypeType,
    EnvironmentAccountConnectionStatusType,
    ServiceStatusType,
    TemplateVersionStatusType,
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
    "AcceptEnvironmentAccountConnectionInputTypeDef",
    "AcceptEnvironmentAccountConnectionOutputResponseTypeDef",
    "AccountSettingsTypeDef",
    "CancelEnvironmentDeploymentInputTypeDef",
    "CancelEnvironmentDeploymentOutputResponseTypeDef",
    "CancelServiceInstanceDeploymentInputTypeDef",
    "CancelServiceInstanceDeploymentOutputResponseTypeDef",
    "CancelServicePipelineDeploymentInputTypeDef",
    "CancelServicePipelineDeploymentOutputResponseTypeDef",
    "CompatibleEnvironmentTemplateInputTypeDef",
    "CompatibleEnvironmentTemplateTypeDef",
    "CreateEnvironmentAccountConnectionInputTypeDef",
    "CreateEnvironmentAccountConnectionOutputResponseTypeDef",
    "CreateEnvironmentInputTypeDef",
    "CreateEnvironmentOutputResponseTypeDef",
    "CreateEnvironmentTemplateInputTypeDef",
    "CreateEnvironmentTemplateOutputResponseTypeDef",
    "CreateEnvironmentTemplateVersionInputTypeDef",
    "CreateEnvironmentTemplateVersionOutputResponseTypeDef",
    "CreateServiceInputTypeDef",
    "CreateServiceOutputResponseTypeDef",
    "CreateServiceTemplateInputTypeDef",
    "CreateServiceTemplateOutputResponseTypeDef",
    "CreateServiceTemplateVersionInputTypeDef",
    "CreateServiceTemplateVersionOutputResponseTypeDef",
    "DeleteEnvironmentAccountConnectionInputTypeDef",
    "DeleteEnvironmentAccountConnectionOutputResponseTypeDef",
    "DeleteEnvironmentInputTypeDef",
    "DeleteEnvironmentOutputResponseTypeDef",
    "DeleteEnvironmentTemplateInputTypeDef",
    "DeleteEnvironmentTemplateOutputResponseTypeDef",
    "DeleteEnvironmentTemplateVersionInputTypeDef",
    "DeleteEnvironmentTemplateVersionOutputResponseTypeDef",
    "DeleteServiceInputTypeDef",
    "DeleteServiceOutputResponseTypeDef",
    "DeleteServiceTemplateInputTypeDef",
    "DeleteServiceTemplateOutputResponseTypeDef",
    "DeleteServiceTemplateVersionInputTypeDef",
    "DeleteServiceTemplateVersionOutputResponseTypeDef",
    "EnvironmentAccountConnectionSummaryTypeDef",
    "EnvironmentAccountConnectionTypeDef",
    "EnvironmentSummaryTypeDef",
    "EnvironmentTemplateFilterTypeDef",
    "EnvironmentTemplateSummaryTypeDef",
    "EnvironmentTemplateTypeDef",
    "EnvironmentTemplateVersionSummaryTypeDef",
    "EnvironmentTemplateVersionTypeDef",
    "EnvironmentTypeDef",
    "GetAccountSettingsOutputResponseTypeDef",
    "GetEnvironmentAccountConnectionInputTypeDef",
    "GetEnvironmentAccountConnectionOutputResponseTypeDef",
    "GetEnvironmentInputTypeDef",
    "GetEnvironmentOutputResponseTypeDef",
    "GetEnvironmentTemplateInputTypeDef",
    "GetEnvironmentTemplateOutputResponseTypeDef",
    "GetEnvironmentTemplateVersionInputTypeDef",
    "GetEnvironmentTemplateVersionOutputResponseTypeDef",
    "GetServiceInputTypeDef",
    "GetServiceInstanceInputTypeDef",
    "GetServiceInstanceOutputResponseTypeDef",
    "GetServiceOutputResponseTypeDef",
    "GetServiceTemplateInputTypeDef",
    "GetServiceTemplateOutputResponseTypeDef",
    "GetServiceTemplateVersionInputTypeDef",
    "GetServiceTemplateVersionOutputResponseTypeDef",
    "ListEnvironmentAccountConnectionsInputTypeDef",
    "ListEnvironmentAccountConnectionsOutputResponseTypeDef",
    "ListEnvironmentTemplateVersionsInputTypeDef",
    "ListEnvironmentTemplateVersionsOutputResponseTypeDef",
    "ListEnvironmentTemplatesInputTypeDef",
    "ListEnvironmentTemplatesOutputResponseTypeDef",
    "ListEnvironmentsInputTypeDef",
    "ListEnvironmentsOutputResponseTypeDef",
    "ListServiceInstancesInputTypeDef",
    "ListServiceInstancesOutputResponseTypeDef",
    "ListServiceTemplateVersionsInputTypeDef",
    "ListServiceTemplateVersionsOutputResponseTypeDef",
    "ListServiceTemplatesInputTypeDef",
    "ListServiceTemplatesOutputResponseTypeDef",
    "ListServicesInputTypeDef",
    "ListServicesOutputResponseTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RejectEnvironmentAccountConnectionInputTypeDef",
    "RejectEnvironmentAccountConnectionOutputResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3ObjectSourceTypeDef",
    "ServiceInstanceSummaryTypeDef",
    "ServiceInstanceTypeDef",
    "ServicePipelineTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTemplateSummaryTypeDef",
    "ServiceTemplateTypeDef",
    "ServiceTemplateVersionSummaryTypeDef",
    "ServiceTemplateVersionTypeDef",
    "ServiceTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "TemplateVersionSourceInputTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateAccountSettingsInputTypeDef",
    "UpdateAccountSettingsOutputResponseTypeDef",
    "UpdateEnvironmentAccountConnectionInputTypeDef",
    "UpdateEnvironmentAccountConnectionOutputResponseTypeDef",
    "UpdateEnvironmentInputTypeDef",
    "UpdateEnvironmentOutputResponseTypeDef",
    "UpdateEnvironmentTemplateInputTypeDef",
    "UpdateEnvironmentTemplateOutputResponseTypeDef",
    "UpdateEnvironmentTemplateVersionInputTypeDef",
    "UpdateEnvironmentTemplateVersionOutputResponseTypeDef",
    "UpdateServiceInputTypeDef",
    "UpdateServiceInstanceInputTypeDef",
    "UpdateServiceInstanceOutputResponseTypeDef",
    "UpdateServiceOutputResponseTypeDef",
    "UpdateServicePipelineInputTypeDef",
    "UpdateServicePipelineOutputResponseTypeDef",
    "UpdateServiceTemplateInputTypeDef",
    "UpdateServiceTemplateOutputResponseTypeDef",
    "UpdateServiceTemplateVersionInputTypeDef",
    "UpdateServiceTemplateVersionOutputResponseTypeDef",
    "WaiterConfigTypeDef",
)

AcceptEnvironmentAccountConnectionInputTypeDef = TypedDict(
    "AcceptEnvironmentAccountConnectionInputTypeDef",
    {
        "id": str,
    },
)

AcceptEnvironmentAccountConnectionOutputResponseTypeDef = TypedDict(
    "AcceptEnvironmentAccountConnectionOutputResponseTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "pipelineServiceRoleArn": str,
    },
    total=False,
)

CancelEnvironmentDeploymentInputTypeDef = TypedDict(
    "CancelEnvironmentDeploymentInputTypeDef",
    {
        "environmentName": str,
    },
)

CancelEnvironmentDeploymentOutputResponseTypeDef = TypedDict(
    "CancelEnvironmentDeploymentOutputResponseTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelServiceInstanceDeploymentInputTypeDef = TypedDict(
    "CancelServiceInstanceDeploymentInputTypeDef",
    {
        "serviceInstanceName": str,
        "serviceName": str,
    },
)

CancelServiceInstanceDeploymentOutputResponseTypeDef = TypedDict(
    "CancelServiceInstanceDeploymentOutputResponseTypeDef",
    {
        "serviceInstance": "ServiceInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelServicePipelineDeploymentInputTypeDef = TypedDict(
    "CancelServicePipelineDeploymentInputTypeDef",
    {
        "serviceName": str,
    },
)

CancelServicePipelineDeploymentOutputResponseTypeDef = TypedDict(
    "CancelServicePipelineDeploymentOutputResponseTypeDef",
    {
        "pipeline": "ServicePipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CompatibleEnvironmentTemplateInputTypeDef = TypedDict(
    "CompatibleEnvironmentTemplateInputTypeDef",
    {
        "majorVersion": str,
        "templateName": str,
    },
)

CompatibleEnvironmentTemplateTypeDef = TypedDict(
    "CompatibleEnvironmentTemplateTypeDef",
    {
        "majorVersion": str,
        "templateName": str,
    },
)

_RequiredCreateEnvironmentAccountConnectionInputTypeDef = TypedDict(
    "_RequiredCreateEnvironmentAccountConnectionInputTypeDef",
    {
        "environmentName": str,
        "managementAccountId": str,
        "roleArn": str,
    },
)
_OptionalCreateEnvironmentAccountConnectionInputTypeDef = TypedDict(
    "_OptionalCreateEnvironmentAccountConnectionInputTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class CreateEnvironmentAccountConnectionInputTypeDef(
    _RequiredCreateEnvironmentAccountConnectionInputTypeDef,
    _OptionalCreateEnvironmentAccountConnectionInputTypeDef,
):
    pass


CreateEnvironmentAccountConnectionOutputResponseTypeDef = TypedDict(
    "CreateEnvironmentAccountConnectionOutputResponseTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEnvironmentInputTypeDef = TypedDict(
    "_RequiredCreateEnvironmentInputTypeDef",
    {
        "name": str,
        "spec": str,
        "templateMajorVersion": str,
        "templateName": str,
    },
)
_OptionalCreateEnvironmentInputTypeDef = TypedDict(
    "_OptionalCreateEnvironmentInputTypeDef",
    {
        "description": str,
        "environmentAccountConnectionId": str,
        "protonServiceRoleArn": str,
        "tags": List["TagTypeDef"],
        "templateMinorVersion": str,
    },
    total=False,
)


class CreateEnvironmentInputTypeDef(
    _RequiredCreateEnvironmentInputTypeDef, _OptionalCreateEnvironmentInputTypeDef
):
    pass


CreateEnvironmentOutputResponseTypeDef = TypedDict(
    "CreateEnvironmentOutputResponseTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEnvironmentTemplateInputTypeDef = TypedDict(
    "_RequiredCreateEnvironmentTemplateInputTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateEnvironmentTemplateInputTypeDef = TypedDict(
    "_OptionalCreateEnvironmentTemplateInputTypeDef",
    {
        "description": str,
        "displayName": str,
        "encryptionKey": str,
        "provisioning": Literal["CUSTOMER_MANAGED"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateEnvironmentTemplateInputTypeDef(
    _RequiredCreateEnvironmentTemplateInputTypeDef, _OptionalCreateEnvironmentTemplateInputTypeDef
):
    pass


CreateEnvironmentTemplateOutputResponseTypeDef = TypedDict(
    "CreateEnvironmentTemplateOutputResponseTypeDef",
    {
        "environmentTemplate": "EnvironmentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEnvironmentTemplateVersionInputTypeDef = TypedDict(
    "_RequiredCreateEnvironmentTemplateVersionInputTypeDef",
    {
        "source": "TemplateVersionSourceInputTypeDef",
        "templateName": str,
    },
)
_OptionalCreateEnvironmentTemplateVersionInputTypeDef = TypedDict(
    "_OptionalCreateEnvironmentTemplateVersionInputTypeDef",
    {
        "clientToken": str,
        "description": str,
        "majorVersion": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateEnvironmentTemplateVersionInputTypeDef(
    _RequiredCreateEnvironmentTemplateVersionInputTypeDef,
    _OptionalCreateEnvironmentTemplateVersionInputTypeDef,
):
    pass


CreateEnvironmentTemplateVersionOutputResponseTypeDef = TypedDict(
    "CreateEnvironmentTemplateVersionOutputResponseTypeDef",
    {
        "environmentTemplateVersion": "EnvironmentTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceInputTypeDef = TypedDict(
    "_RequiredCreateServiceInputTypeDef",
    {
        "name": str,
        "spec": str,
        "templateMajorVersion": str,
        "templateName": str,
    },
)
_OptionalCreateServiceInputTypeDef = TypedDict(
    "_OptionalCreateServiceInputTypeDef",
    {
        "branchName": str,
        "description": str,
        "repositoryConnectionArn": str,
        "repositoryId": str,
        "tags": List["TagTypeDef"],
        "templateMinorVersion": str,
    },
    total=False,
)


class CreateServiceInputTypeDef(
    _RequiredCreateServiceInputTypeDef, _OptionalCreateServiceInputTypeDef
):
    pass


CreateServiceOutputResponseTypeDef = TypedDict(
    "CreateServiceOutputResponseTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceTemplateInputTypeDef = TypedDict(
    "_RequiredCreateServiceTemplateInputTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateServiceTemplateInputTypeDef = TypedDict(
    "_OptionalCreateServiceTemplateInputTypeDef",
    {
        "description": str,
        "displayName": str,
        "encryptionKey": str,
        "pipelineProvisioning": Literal["CUSTOMER_MANAGED"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateServiceTemplateInputTypeDef(
    _RequiredCreateServiceTemplateInputTypeDef, _OptionalCreateServiceTemplateInputTypeDef
):
    pass


CreateServiceTemplateOutputResponseTypeDef = TypedDict(
    "CreateServiceTemplateOutputResponseTypeDef",
    {
        "serviceTemplate": "ServiceTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceTemplateVersionInputTypeDef = TypedDict(
    "_RequiredCreateServiceTemplateVersionInputTypeDef",
    {
        "compatibleEnvironmentTemplates": List["CompatibleEnvironmentTemplateInputTypeDef"],
        "source": "TemplateVersionSourceInputTypeDef",
        "templateName": str,
    },
)
_OptionalCreateServiceTemplateVersionInputTypeDef = TypedDict(
    "_OptionalCreateServiceTemplateVersionInputTypeDef",
    {
        "clientToken": str,
        "description": str,
        "majorVersion": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateServiceTemplateVersionInputTypeDef(
    _RequiredCreateServiceTemplateVersionInputTypeDef,
    _OptionalCreateServiceTemplateVersionInputTypeDef,
):
    pass


CreateServiceTemplateVersionOutputResponseTypeDef = TypedDict(
    "CreateServiceTemplateVersionOutputResponseTypeDef",
    {
        "serviceTemplateVersion": "ServiceTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentAccountConnectionInputTypeDef = TypedDict(
    "DeleteEnvironmentAccountConnectionInputTypeDef",
    {
        "id": str,
    },
)

DeleteEnvironmentAccountConnectionOutputResponseTypeDef = TypedDict(
    "DeleteEnvironmentAccountConnectionOutputResponseTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentInputTypeDef = TypedDict(
    "DeleteEnvironmentInputTypeDef",
    {
        "name": str,
    },
)

DeleteEnvironmentOutputResponseTypeDef = TypedDict(
    "DeleteEnvironmentOutputResponseTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentTemplateInputTypeDef = TypedDict(
    "DeleteEnvironmentTemplateInputTypeDef",
    {
        "name": str,
    },
)

DeleteEnvironmentTemplateOutputResponseTypeDef = TypedDict(
    "DeleteEnvironmentTemplateOutputResponseTypeDef",
    {
        "environmentTemplate": "EnvironmentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentTemplateVersionInputTypeDef = TypedDict(
    "DeleteEnvironmentTemplateVersionInputTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)

DeleteEnvironmentTemplateVersionOutputResponseTypeDef = TypedDict(
    "DeleteEnvironmentTemplateVersionOutputResponseTypeDef",
    {
        "environmentTemplateVersion": "EnvironmentTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceInputTypeDef = TypedDict(
    "DeleteServiceInputTypeDef",
    {
        "name": str,
    },
)

DeleteServiceOutputResponseTypeDef = TypedDict(
    "DeleteServiceOutputResponseTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceTemplateInputTypeDef = TypedDict(
    "DeleteServiceTemplateInputTypeDef",
    {
        "name": str,
    },
)

DeleteServiceTemplateOutputResponseTypeDef = TypedDict(
    "DeleteServiceTemplateOutputResponseTypeDef",
    {
        "serviceTemplate": "ServiceTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceTemplateVersionInputTypeDef = TypedDict(
    "DeleteServiceTemplateVersionInputTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)

DeleteServiceTemplateVersionOutputResponseTypeDef = TypedDict(
    "DeleteServiceTemplateVersionOutputResponseTypeDef",
    {
        "serviceTemplateVersion": "ServiceTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentAccountConnectionSummaryTypeDef = TypedDict(
    "EnvironmentAccountConnectionSummaryTypeDef",
    {
        "arn": str,
        "environmentAccountId": str,
        "environmentName": str,
        "id": str,
        "lastModifiedAt": datetime,
        "managementAccountId": str,
        "requestedAt": datetime,
        "roleArn": str,
        "status": EnvironmentAccountConnectionStatusType,
    },
)

EnvironmentAccountConnectionTypeDef = TypedDict(
    "EnvironmentAccountConnectionTypeDef",
    {
        "arn": str,
        "environmentAccountId": str,
        "environmentName": str,
        "id": str,
        "lastModifiedAt": datetime,
        "managementAccountId": str,
        "requestedAt": datetime,
        "roleArn": str,
        "status": EnvironmentAccountConnectionStatusType,
    },
)

_RequiredEnvironmentSummaryTypeDef = TypedDict(
    "_RequiredEnvironmentSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "name": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
    },
)
_OptionalEnvironmentSummaryTypeDef = TypedDict(
    "_OptionalEnvironmentSummaryTypeDef",
    {
        "deploymentStatusMessage": str,
        "description": str,
        "environmentAccountConnectionId": str,
        "environmentAccountId": str,
        "protonServiceRoleArn": str,
        "provisioning": Literal["CUSTOMER_MANAGED"],
    },
    total=False,
)


class EnvironmentSummaryTypeDef(
    _RequiredEnvironmentSummaryTypeDef, _OptionalEnvironmentSummaryTypeDef
):
    pass


EnvironmentTemplateFilterTypeDef = TypedDict(
    "EnvironmentTemplateFilterTypeDef",
    {
        "majorVersion": str,
        "templateName": str,
    },
)

_RequiredEnvironmentTemplateSummaryTypeDef = TypedDict(
    "_RequiredEnvironmentTemplateSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
    },
)
_OptionalEnvironmentTemplateSummaryTypeDef = TypedDict(
    "_OptionalEnvironmentTemplateSummaryTypeDef",
    {
        "description": str,
        "displayName": str,
        "provisioning": Literal["CUSTOMER_MANAGED"],
        "recommendedVersion": str,
    },
    total=False,
)


class EnvironmentTemplateSummaryTypeDef(
    _RequiredEnvironmentTemplateSummaryTypeDef, _OptionalEnvironmentTemplateSummaryTypeDef
):
    pass


_RequiredEnvironmentTemplateTypeDef = TypedDict(
    "_RequiredEnvironmentTemplateTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
    },
)
_OptionalEnvironmentTemplateTypeDef = TypedDict(
    "_OptionalEnvironmentTemplateTypeDef",
    {
        "description": str,
        "displayName": str,
        "encryptionKey": str,
        "provisioning": Literal["CUSTOMER_MANAGED"],
        "recommendedVersion": str,
    },
    total=False,
)


class EnvironmentTemplateTypeDef(
    _RequiredEnvironmentTemplateTypeDef, _OptionalEnvironmentTemplateTypeDef
):
    pass


_RequiredEnvironmentTemplateVersionSummaryTypeDef = TypedDict(
    "_RequiredEnvironmentTemplateVersionSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "majorVersion": str,
        "minorVersion": str,
        "status": TemplateVersionStatusType,
        "templateName": str,
    },
)
_OptionalEnvironmentTemplateVersionSummaryTypeDef = TypedDict(
    "_OptionalEnvironmentTemplateVersionSummaryTypeDef",
    {
        "description": str,
        "recommendedMinorVersion": str,
        "statusMessage": str,
    },
    total=False,
)


class EnvironmentTemplateVersionSummaryTypeDef(
    _RequiredEnvironmentTemplateVersionSummaryTypeDef,
    _OptionalEnvironmentTemplateVersionSummaryTypeDef,
):
    pass


_RequiredEnvironmentTemplateVersionTypeDef = TypedDict(
    "_RequiredEnvironmentTemplateVersionTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "majorVersion": str,
        "minorVersion": str,
        "status": TemplateVersionStatusType,
        "templateName": str,
    },
)
_OptionalEnvironmentTemplateVersionTypeDef = TypedDict(
    "_OptionalEnvironmentTemplateVersionTypeDef",
    {
        "description": str,
        "recommendedMinorVersion": str,
        "schema": str,
        "statusMessage": str,
    },
    total=False,
)


class EnvironmentTemplateVersionTypeDef(
    _RequiredEnvironmentTemplateVersionTypeDef, _OptionalEnvironmentTemplateVersionTypeDef
):
    pass


_RequiredEnvironmentTypeDef = TypedDict(
    "_RequiredEnvironmentTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "name": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
    },
)
_OptionalEnvironmentTypeDef = TypedDict(
    "_OptionalEnvironmentTypeDef",
    {
        "deploymentStatusMessage": str,
        "description": str,
        "environmentAccountConnectionId": str,
        "environmentAccountId": str,
        "protonServiceRoleArn": str,
        "provisioning": Literal["CUSTOMER_MANAGED"],
        "spec": str,
    },
    total=False,
)


class EnvironmentTypeDef(_RequiredEnvironmentTypeDef, _OptionalEnvironmentTypeDef):
    pass


GetAccountSettingsOutputResponseTypeDef = TypedDict(
    "GetAccountSettingsOutputResponseTypeDef",
    {
        "accountSettings": "AccountSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentAccountConnectionInputTypeDef = TypedDict(
    "GetEnvironmentAccountConnectionInputTypeDef",
    {
        "id": str,
    },
)

GetEnvironmentAccountConnectionOutputResponseTypeDef = TypedDict(
    "GetEnvironmentAccountConnectionOutputResponseTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentInputTypeDef = TypedDict(
    "GetEnvironmentInputTypeDef",
    {
        "name": str,
    },
)

GetEnvironmentOutputResponseTypeDef = TypedDict(
    "GetEnvironmentOutputResponseTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentTemplateInputTypeDef = TypedDict(
    "GetEnvironmentTemplateInputTypeDef",
    {
        "name": str,
    },
)

GetEnvironmentTemplateOutputResponseTypeDef = TypedDict(
    "GetEnvironmentTemplateOutputResponseTypeDef",
    {
        "environmentTemplate": "EnvironmentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentTemplateVersionInputTypeDef = TypedDict(
    "GetEnvironmentTemplateVersionInputTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)

GetEnvironmentTemplateVersionOutputResponseTypeDef = TypedDict(
    "GetEnvironmentTemplateVersionOutputResponseTypeDef",
    {
        "environmentTemplateVersion": "EnvironmentTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceInputTypeDef = TypedDict(
    "GetServiceInputTypeDef",
    {
        "name": str,
    },
)

GetServiceInstanceInputTypeDef = TypedDict(
    "GetServiceInstanceInputTypeDef",
    {
        "name": str,
        "serviceName": str,
    },
)

GetServiceInstanceOutputResponseTypeDef = TypedDict(
    "GetServiceInstanceOutputResponseTypeDef",
    {
        "serviceInstance": "ServiceInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceOutputResponseTypeDef = TypedDict(
    "GetServiceOutputResponseTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceTemplateInputTypeDef = TypedDict(
    "GetServiceTemplateInputTypeDef",
    {
        "name": str,
    },
)

GetServiceTemplateOutputResponseTypeDef = TypedDict(
    "GetServiceTemplateOutputResponseTypeDef",
    {
        "serviceTemplate": "ServiceTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceTemplateVersionInputTypeDef = TypedDict(
    "GetServiceTemplateVersionInputTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)

GetServiceTemplateVersionOutputResponseTypeDef = TypedDict(
    "GetServiceTemplateVersionOutputResponseTypeDef",
    {
        "serviceTemplateVersion": "ServiceTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEnvironmentAccountConnectionsInputTypeDef = TypedDict(
    "_RequiredListEnvironmentAccountConnectionsInputTypeDef",
    {
        "requestedBy": EnvironmentAccountConnectionRequesterAccountTypeType,
    },
)
_OptionalListEnvironmentAccountConnectionsInputTypeDef = TypedDict(
    "_OptionalListEnvironmentAccountConnectionsInputTypeDef",
    {
        "environmentName": str,
        "maxResults": int,
        "nextToken": str,
        "statuses": List[EnvironmentAccountConnectionStatusType],
    },
    total=False,
)


class ListEnvironmentAccountConnectionsInputTypeDef(
    _RequiredListEnvironmentAccountConnectionsInputTypeDef,
    _OptionalListEnvironmentAccountConnectionsInputTypeDef,
):
    pass


ListEnvironmentAccountConnectionsOutputResponseTypeDef = TypedDict(
    "ListEnvironmentAccountConnectionsOutputResponseTypeDef",
    {
        "environmentAccountConnections": List["EnvironmentAccountConnectionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEnvironmentTemplateVersionsInputTypeDef = TypedDict(
    "_RequiredListEnvironmentTemplateVersionsInputTypeDef",
    {
        "templateName": str,
    },
)
_OptionalListEnvironmentTemplateVersionsInputTypeDef = TypedDict(
    "_OptionalListEnvironmentTemplateVersionsInputTypeDef",
    {
        "majorVersion": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListEnvironmentTemplateVersionsInputTypeDef(
    _RequiredListEnvironmentTemplateVersionsInputTypeDef,
    _OptionalListEnvironmentTemplateVersionsInputTypeDef,
):
    pass


ListEnvironmentTemplateVersionsOutputResponseTypeDef = TypedDict(
    "ListEnvironmentTemplateVersionsOutputResponseTypeDef",
    {
        "nextToken": str,
        "templateVersions": List["EnvironmentTemplateVersionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnvironmentTemplatesInputTypeDef = TypedDict(
    "ListEnvironmentTemplatesInputTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListEnvironmentTemplatesOutputResponseTypeDef = TypedDict(
    "ListEnvironmentTemplatesOutputResponseTypeDef",
    {
        "nextToken": str,
        "templates": List["EnvironmentTemplateSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnvironmentsInputTypeDef = TypedDict(
    "ListEnvironmentsInputTypeDef",
    {
        "environmentTemplates": List["EnvironmentTemplateFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListEnvironmentsOutputResponseTypeDef = TypedDict(
    "ListEnvironmentsOutputResponseTypeDef",
    {
        "environments": List["EnvironmentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceInstancesInputTypeDef = TypedDict(
    "ListServiceInstancesInputTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "serviceName": str,
    },
    total=False,
)

ListServiceInstancesOutputResponseTypeDef = TypedDict(
    "ListServiceInstancesOutputResponseTypeDef",
    {
        "nextToken": str,
        "serviceInstances": List["ServiceInstanceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServiceTemplateVersionsInputTypeDef = TypedDict(
    "_RequiredListServiceTemplateVersionsInputTypeDef",
    {
        "templateName": str,
    },
)
_OptionalListServiceTemplateVersionsInputTypeDef = TypedDict(
    "_OptionalListServiceTemplateVersionsInputTypeDef",
    {
        "majorVersion": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListServiceTemplateVersionsInputTypeDef(
    _RequiredListServiceTemplateVersionsInputTypeDef,
    _OptionalListServiceTemplateVersionsInputTypeDef,
):
    pass


ListServiceTemplateVersionsOutputResponseTypeDef = TypedDict(
    "ListServiceTemplateVersionsOutputResponseTypeDef",
    {
        "nextToken": str,
        "templateVersions": List["ServiceTemplateVersionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceTemplatesInputTypeDef = TypedDict(
    "ListServiceTemplatesInputTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListServiceTemplatesOutputResponseTypeDef = TypedDict(
    "ListServiceTemplatesOutputResponseTypeDef",
    {
        "nextToken": str,
        "templates": List["ServiceTemplateSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesInputTypeDef = TypedDict(
    "ListServicesInputTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListServicesOutputResponseTypeDef = TypedDict(
    "ListServicesOutputResponseTypeDef",
    {
        "nextToken": str,
        "services": List["ServiceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListTagsForResourceInputTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListTagsForResourceInputTypeDef(
    _RequiredListTagsForResourceInputTypeDef, _OptionalListTagsForResourceInputTypeDef
):
    pass


ListTagsForResourceOutputResponseTypeDef = TypedDict(
    "ListTagsForResourceOutputResponseTypeDef",
    {
        "nextToken": str,
        "tags": List["TagTypeDef"],
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

RejectEnvironmentAccountConnectionInputTypeDef = TypedDict(
    "RejectEnvironmentAccountConnectionInputTypeDef",
    {
        "id": str,
    },
)

RejectEnvironmentAccountConnectionOutputResponseTypeDef = TypedDict(
    "RejectEnvironmentAccountConnectionOutputResponseTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
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

S3ObjectSourceTypeDef = TypedDict(
    "S3ObjectSourceTypeDef",
    {
        "bucket": str,
        "key": str,
    },
)

_RequiredServiceInstanceSummaryTypeDef = TypedDict(
    "_RequiredServiceInstanceSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "environmentName": str,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "name": str,
        "serviceName": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
    },
)
_OptionalServiceInstanceSummaryTypeDef = TypedDict(
    "_OptionalServiceInstanceSummaryTypeDef",
    {
        "deploymentStatusMessage": str,
    },
    total=False,
)


class ServiceInstanceSummaryTypeDef(
    _RequiredServiceInstanceSummaryTypeDef, _OptionalServiceInstanceSummaryTypeDef
):
    pass


_RequiredServiceInstanceTypeDef = TypedDict(
    "_RequiredServiceInstanceTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "environmentName": str,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "name": str,
        "serviceName": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
    },
)
_OptionalServiceInstanceTypeDef = TypedDict(
    "_OptionalServiceInstanceTypeDef",
    {
        "deploymentStatusMessage": str,
        "spec": str,
    },
    total=False,
)


class ServiceInstanceTypeDef(_RequiredServiceInstanceTypeDef, _OptionalServiceInstanceTypeDef):
    pass


_RequiredServicePipelineTypeDef = TypedDict(
    "_RequiredServicePipelineTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
    },
)
_OptionalServicePipelineTypeDef = TypedDict(
    "_OptionalServicePipelineTypeDef",
    {
        "deploymentStatusMessage": str,
        "spec": str,
    },
    total=False,
)


class ServicePipelineTypeDef(_RequiredServicePipelineTypeDef, _OptionalServicePipelineTypeDef):
    pass


_RequiredServiceSummaryTypeDef = TypedDict(
    "_RequiredServiceSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
        "status": ServiceStatusType,
        "templateName": str,
    },
)
_OptionalServiceSummaryTypeDef = TypedDict(
    "_OptionalServiceSummaryTypeDef",
    {
        "description": str,
        "statusMessage": str,
    },
    total=False,
)


class ServiceSummaryTypeDef(_RequiredServiceSummaryTypeDef, _OptionalServiceSummaryTypeDef):
    pass


_RequiredServiceTemplateSummaryTypeDef = TypedDict(
    "_RequiredServiceTemplateSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
    },
)
_OptionalServiceTemplateSummaryTypeDef = TypedDict(
    "_OptionalServiceTemplateSummaryTypeDef",
    {
        "description": str,
        "displayName": str,
        "pipelineProvisioning": Literal["CUSTOMER_MANAGED"],
        "recommendedVersion": str,
    },
    total=False,
)


class ServiceTemplateSummaryTypeDef(
    _RequiredServiceTemplateSummaryTypeDef, _OptionalServiceTemplateSummaryTypeDef
):
    pass


_RequiredServiceTemplateTypeDef = TypedDict(
    "_RequiredServiceTemplateTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
    },
)
_OptionalServiceTemplateTypeDef = TypedDict(
    "_OptionalServiceTemplateTypeDef",
    {
        "description": str,
        "displayName": str,
        "encryptionKey": str,
        "pipelineProvisioning": Literal["CUSTOMER_MANAGED"],
        "recommendedVersion": str,
    },
    total=False,
)


class ServiceTemplateTypeDef(_RequiredServiceTemplateTypeDef, _OptionalServiceTemplateTypeDef):
    pass


_RequiredServiceTemplateVersionSummaryTypeDef = TypedDict(
    "_RequiredServiceTemplateVersionSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "majorVersion": str,
        "minorVersion": str,
        "status": TemplateVersionStatusType,
        "templateName": str,
    },
)
_OptionalServiceTemplateVersionSummaryTypeDef = TypedDict(
    "_OptionalServiceTemplateVersionSummaryTypeDef",
    {
        "description": str,
        "recommendedMinorVersion": str,
        "statusMessage": str,
    },
    total=False,
)


class ServiceTemplateVersionSummaryTypeDef(
    _RequiredServiceTemplateVersionSummaryTypeDef, _OptionalServiceTemplateVersionSummaryTypeDef
):
    pass


_RequiredServiceTemplateVersionTypeDef = TypedDict(
    "_RequiredServiceTemplateVersionTypeDef",
    {
        "arn": str,
        "compatibleEnvironmentTemplates": List["CompatibleEnvironmentTemplateTypeDef"],
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "majorVersion": str,
        "minorVersion": str,
        "status": TemplateVersionStatusType,
        "templateName": str,
    },
)
_OptionalServiceTemplateVersionTypeDef = TypedDict(
    "_OptionalServiceTemplateVersionTypeDef",
    {
        "description": str,
        "recommendedMinorVersion": str,
        "schema": str,
        "statusMessage": str,
    },
    total=False,
)


class ServiceTemplateVersionTypeDef(
    _RequiredServiceTemplateVersionTypeDef, _OptionalServiceTemplateVersionTypeDef
):
    pass


_RequiredServiceTypeDef = TypedDict(
    "_RequiredServiceTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
        "spec": str,
        "status": ServiceStatusType,
        "templateName": str,
    },
)
_OptionalServiceTypeDef = TypedDict(
    "_OptionalServiceTypeDef",
    {
        "branchName": str,
        "description": str,
        "pipeline": "ServicePipelineTypeDef",
        "repositoryConnectionArn": str,
        "repositoryId": str,
        "statusMessage": str,
    },
    total=False,
)


class ServiceTypeDef(_RequiredServiceTypeDef, _OptionalServiceTypeDef):
    pass


TagResourceInputTypeDef = TypedDict(
    "TagResourceInputTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TemplateVersionSourceInputTypeDef = TypedDict(
    "TemplateVersionSourceInputTypeDef",
    {
        "s3": "S3ObjectSourceTypeDef",
    },
    total=False,
)

UntagResourceInputTypeDef = TypedDict(
    "UntagResourceInputTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateAccountSettingsInputTypeDef = TypedDict(
    "UpdateAccountSettingsInputTypeDef",
    {
        "pipelineServiceRoleArn": str,
    },
    total=False,
)

UpdateAccountSettingsOutputResponseTypeDef = TypedDict(
    "UpdateAccountSettingsOutputResponseTypeDef",
    {
        "accountSettings": "AccountSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEnvironmentAccountConnectionInputTypeDef = TypedDict(
    "UpdateEnvironmentAccountConnectionInputTypeDef",
    {
        "id": str,
        "roleArn": str,
    },
)

UpdateEnvironmentAccountConnectionOutputResponseTypeDef = TypedDict(
    "UpdateEnvironmentAccountConnectionOutputResponseTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEnvironmentInputTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentInputTypeDef",
    {
        "deploymentType": DeploymentUpdateTypeType,
        "name": str,
    },
)
_OptionalUpdateEnvironmentInputTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentInputTypeDef",
    {
        "description": str,
        "environmentAccountConnectionId": str,
        "protonServiceRoleArn": str,
        "spec": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
    },
    total=False,
)


class UpdateEnvironmentInputTypeDef(
    _RequiredUpdateEnvironmentInputTypeDef, _OptionalUpdateEnvironmentInputTypeDef
):
    pass


UpdateEnvironmentOutputResponseTypeDef = TypedDict(
    "UpdateEnvironmentOutputResponseTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEnvironmentTemplateInputTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentTemplateInputTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateEnvironmentTemplateInputTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentTemplateInputTypeDef",
    {
        "description": str,
        "displayName": str,
    },
    total=False,
)


class UpdateEnvironmentTemplateInputTypeDef(
    _RequiredUpdateEnvironmentTemplateInputTypeDef, _OptionalUpdateEnvironmentTemplateInputTypeDef
):
    pass


UpdateEnvironmentTemplateOutputResponseTypeDef = TypedDict(
    "UpdateEnvironmentTemplateOutputResponseTypeDef",
    {
        "environmentTemplate": "EnvironmentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEnvironmentTemplateVersionInputTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentTemplateVersionInputTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)
_OptionalUpdateEnvironmentTemplateVersionInputTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentTemplateVersionInputTypeDef",
    {
        "description": str,
        "status": TemplateVersionStatusType,
    },
    total=False,
)


class UpdateEnvironmentTemplateVersionInputTypeDef(
    _RequiredUpdateEnvironmentTemplateVersionInputTypeDef,
    _OptionalUpdateEnvironmentTemplateVersionInputTypeDef,
):
    pass


UpdateEnvironmentTemplateVersionOutputResponseTypeDef = TypedDict(
    "UpdateEnvironmentTemplateVersionOutputResponseTypeDef",
    {
        "environmentTemplateVersion": "EnvironmentTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServiceInputTypeDef = TypedDict(
    "_RequiredUpdateServiceInputTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateServiceInputTypeDef = TypedDict(
    "_OptionalUpdateServiceInputTypeDef",
    {
        "description": str,
        "spec": str,
    },
    total=False,
)


class UpdateServiceInputTypeDef(
    _RequiredUpdateServiceInputTypeDef, _OptionalUpdateServiceInputTypeDef
):
    pass


_RequiredUpdateServiceInstanceInputTypeDef = TypedDict(
    "_RequiredUpdateServiceInstanceInputTypeDef",
    {
        "deploymentType": DeploymentUpdateTypeType,
        "name": str,
        "serviceName": str,
    },
)
_OptionalUpdateServiceInstanceInputTypeDef = TypedDict(
    "_OptionalUpdateServiceInstanceInputTypeDef",
    {
        "spec": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
    },
    total=False,
)


class UpdateServiceInstanceInputTypeDef(
    _RequiredUpdateServiceInstanceInputTypeDef, _OptionalUpdateServiceInstanceInputTypeDef
):
    pass


UpdateServiceInstanceOutputResponseTypeDef = TypedDict(
    "UpdateServiceInstanceOutputResponseTypeDef",
    {
        "serviceInstance": "ServiceInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceOutputResponseTypeDef = TypedDict(
    "UpdateServiceOutputResponseTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServicePipelineInputTypeDef = TypedDict(
    "_RequiredUpdateServicePipelineInputTypeDef",
    {
        "deploymentType": DeploymentUpdateTypeType,
        "serviceName": str,
        "spec": str,
    },
)
_OptionalUpdateServicePipelineInputTypeDef = TypedDict(
    "_OptionalUpdateServicePipelineInputTypeDef",
    {
        "templateMajorVersion": str,
        "templateMinorVersion": str,
    },
    total=False,
)


class UpdateServicePipelineInputTypeDef(
    _RequiredUpdateServicePipelineInputTypeDef, _OptionalUpdateServicePipelineInputTypeDef
):
    pass


UpdateServicePipelineOutputResponseTypeDef = TypedDict(
    "UpdateServicePipelineOutputResponseTypeDef",
    {
        "pipeline": "ServicePipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServiceTemplateInputTypeDef = TypedDict(
    "_RequiredUpdateServiceTemplateInputTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateServiceTemplateInputTypeDef = TypedDict(
    "_OptionalUpdateServiceTemplateInputTypeDef",
    {
        "description": str,
        "displayName": str,
    },
    total=False,
)


class UpdateServiceTemplateInputTypeDef(
    _RequiredUpdateServiceTemplateInputTypeDef, _OptionalUpdateServiceTemplateInputTypeDef
):
    pass


UpdateServiceTemplateOutputResponseTypeDef = TypedDict(
    "UpdateServiceTemplateOutputResponseTypeDef",
    {
        "serviceTemplate": "ServiceTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServiceTemplateVersionInputTypeDef = TypedDict(
    "_RequiredUpdateServiceTemplateVersionInputTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)
_OptionalUpdateServiceTemplateVersionInputTypeDef = TypedDict(
    "_OptionalUpdateServiceTemplateVersionInputTypeDef",
    {
        "compatibleEnvironmentTemplates": List["CompatibleEnvironmentTemplateInputTypeDef"],
        "description": str,
        "status": TemplateVersionStatusType,
    },
    total=False,
)


class UpdateServiceTemplateVersionInputTypeDef(
    _RequiredUpdateServiceTemplateVersionInputTypeDef,
    _OptionalUpdateServiceTemplateVersionInputTypeDef,
):
    pass


UpdateServiceTemplateVersionOutputResponseTypeDef = TypedDict(
    "UpdateServiceTemplateVersionOutputResponseTypeDef",
    {
        "serviceTemplateVersion": "ServiceTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
