"""
Type annotations for ram service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ram.type_defs import AcceptResourceShareInvitationRequestTypeDef

    data: AcceptResourceShareInvitationRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ResourceOwnerType,
    ResourceShareAssociationStatusType,
    ResourceShareAssociationTypeType,
    ResourceShareFeatureSetType,
    ResourceShareInvitationStatusType,
    ResourceShareStatusType,
    ResourceStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptResourceShareInvitationRequestTypeDef",
    "AcceptResourceShareInvitationResponseResponseTypeDef",
    "AssociateResourceSharePermissionRequestTypeDef",
    "AssociateResourceSharePermissionResponseResponseTypeDef",
    "AssociateResourceShareRequestTypeDef",
    "AssociateResourceShareResponseResponseTypeDef",
    "CreateResourceShareRequestTypeDef",
    "CreateResourceShareResponseResponseTypeDef",
    "DeleteResourceShareRequestTypeDef",
    "DeleteResourceShareResponseResponseTypeDef",
    "DisassociateResourceSharePermissionRequestTypeDef",
    "DisassociateResourceSharePermissionResponseResponseTypeDef",
    "DisassociateResourceShareRequestTypeDef",
    "DisassociateResourceShareResponseResponseTypeDef",
    "EnableSharingWithAwsOrganizationResponseResponseTypeDef",
    "GetPermissionRequestTypeDef",
    "GetPermissionResponseResponseTypeDef",
    "GetResourcePoliciesRequestTypeDef",
    "GetResourcePoliciesResponseResponseTypeDef",
    "GetResourceShareAssociationsRequestTypeDef",
    "GetResourceShareAssociationsResponseResponseTypeDef",
    "GetResourceShareInvitationsRequestTypeDef",
    "GetResourceShareInvitationsResponseResponseTypeDef",
    "GetResourceSharesRequestTypeDef",
    "GetResourceSharesResponseResponseTypeDef",
    "ListPendingInvitationResourcesRequestTypeDef",
    "ListPendingInvitationResourcesResponseResponseTypeDef",
    "ListPermissionsRequestTypeDef",
    "ListPermissionsResponseResponseTypeDef",
    "ListPrincipalsRequestTypeDef",
    "ListPrincipalsResponseResponseTypeDef",
    "ListResourceSharePermissionsRequestTypeDef",
    "ListResourceSharePermissionsResponseResponseTypeDef",
    "ListResourceTypesRequestTypeDef",
    "ListResourceTypesResponseResponseTypeDef",
    "ListResourcesRequestTypeDef",
    "ListResourcesResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PrincipalTypeDef",
    "PromoteResourceShareCreatedFromPolicyRequestTypeDef",
    "PromoteResourceShareCreatedFromPolicyResponseResponseTypeDef",
    "RejectResourceShareInvitationRequestTypeDef",
    "RejectResourceShareInvitationResponseResponseTypeDef",
    "ResourceShareAssociationTypeDef",
    "ResourceShareInvitationTypeDef",
    "ResourceSharePermissionDetailTypeDef",
    "ResourceSharePermissionSummaryTypeDef",
    "ResourceShareTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceNameAndResourceTypeTypeDef",
    "TagFilterTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateResourceShareRequestTypeDef",
    "UpdateResourceShareResponseResponseTypeDef",
)

_RequiredAcceptResourceShareInvitationRequestTypeDef = TypedDict(
    "_RequiredAcceptResourceShareInvitationRequestTypeDef",
    {
        "resourceShareInvitationArn": str,
    },
)
_OptionalAcceptResourceShareInvitationRequestTypeDef = TypedDict(
    "_OptionalAcceptResourceShareInvitationRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class AcceptResourceShareInvitationRequestTypeDef(
    _RequiredAcceptResourceShareInvitationRequestTypeDef,
    _OptionalAcceptResourceShareInvitationRequestTypeDef,
):
    pass


AcceptResourceShareInvitationResponseResponseTypeDef = TypedDict(
    "AcceptResourceShareInvitationResponseResponseTypeDef",
    {
        "resourceShareInvitation": "ResourceShareInvitationTypeDef",
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateResourceSharePermissionRequestTypeDef = TypedDict(
    "_RequiredAssociateResourceSharePermissionRequestTypeDef",
    {
        "resourceShareArn": str,
        "permissionArn": str,
    },
)
_OptionalAssociateResourceSharePermissionRequestTypeDef = TypedDict(
    "_OptionalAssociateResourceSharePermissionRequestTypeDef",
    {
        "replace": bool,
        "clientToken": str,
        "permissionVersion": int,
    },
    total=False,
)


class AssociateResourceSharePermissionRequestTypeDef(
    _RequiredAssociateResourceSharePermissionRequestTypeDef,
    _OptionalAssociateResourceSharePermissionRequestTypeDef,
):
    pass


AssociateResourceSharePermissionResponseResponseTypeDef = TypedDict(
    "AssociateResourceSharePermissionResponseResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateResourceShareRequestTypeDef = TypedDict(
    "_RequiredAssociateResourceShareRequestTypeDef",
    {
        "resourceShareArn": str,
    },
)
_OptionalAssociateResourceShareRequestTypeDef = TypedDict(
    "_OptionalAssociateResourceShareRequestTypeDef",
    {
        "resourceArns": List[str],
        "principals": List[str],
        "clientToken": str,
    },
    total=False,
)


class AssociateResourceShareRequestTypeDef(
    _RequiredAssociateResourceShareRequestTypeDef, _OptionalAssociateResourceShareRequestTypeDef
):
    pass


AssociateResourceShareResponseResponseTypeDef = TypedDict(
    "AssociateResourceShareResponseResponseTypeDef",
    {
        "resourceShareAssociations": List["ResourceShareAssociationTypeDef"],
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResourceShareRequestTypeDef = TypedDict(
    "_RequiredCreateResourceShareRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateResourceShareRequestTypeDef = TypedDict(
    "_OptionalCreateResourceShareRequestTypeDef",
    {
        "resourceArns": List[str],
        "principals": List[str],
        "tags": List["TagTypeDef"],
        "allowExternalPrincipals": bool,
        "clientToken": str,
        "permissionArns": List[str],
    },
    total=False,
)


class CreateResourceShareRequestTypeDef(
    _RequiredCreateResourceShareRequestTypeDef, _OptionalCreateResourceShareRequestTypeDef
):
    pass


CreateResourceShareResponseResponseTypeDef = TypedDict(
    "CreateResourceShareResponseResponseTypeDef",
    {
        "resourceShare": "ResourceShareTypeDef",
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteResourceShareRequestTypeDef = TypedDict(
    "_RequiredDeleteResourceShareRequestTypeDef",
    {
        "resourceShareArn": str,
    },
)
_OptionalDeleteResourceShareRequestTypeDef = TypedDict(
    "_OptionalDeleteResourceShareRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteResourceShareRequestTypeDef(
    _RequiredDeleteResourceShareRequestTypeDef, _OptionalDeleteResourceShareRequestTypeDef
):
    pass


DeleteResourceShareResponseResponseTypeDef = TypedDict(
    "DeleteResourceShareResponseResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateResourceSharePermissionRequestTypeDef = TypedDict(
    "_RequiredDisassociateResourceSharePermissionRequestTypeDef",
    {
        "resourceShareArn": str,
        "permissionArn": str,
    },
)
_OptionalDisassociateResourceSharePermissionRequestTypeDef = TypedDict(
    "_OptionalDisassociateResourceSharePermissionRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DisassociateResourceSharePermissionRequestTypeDef(
    _RequiredDisassociateResourceSharePermissionRequestTypeDef,
    _OptionalDisassociateResourceSharePermissionRequestTypeDef,
):
    pass


DisassociateResourceSharePermissionResponseResponseTypeDef = TypedDict(
    "DisassociateResourceSharePermissionResponseResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateResourceShareRequestTypeDef = TypedDict(
    "_RequiredDisassociateResourceShareRequestTypeDef",
    {
        "resourceShareArn": str,
    },
)
_OptionalDisassociateResourceShareRequestTypeDef = TypedDict(
    "_OptionalDisassociateResourceShareRequestTypeDef",
    {
        "resourceArns": List[str],
        "principals": List[str],
        "clientToken": str,
    },
    total=False,
)


class DisassociateResourceShareRequestTypeDef(
    _RequiredDisassociateResourceShareRequestTypeDef,
    _OptionalDisassociateResourceShareRequestTypeDef,
):
    pass


DisassociateResourceShareResponseResponseTypeDef = TypedDict(
    "DisassociateResourceShareResponseResponseTypeDef",
    {
        "resourceShareAssociations": List["ResourceShareAssociationTypeDef"],
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableSharingWithAwsOrganizationResponseResponseTypeDef = TypedDict(
    "EnableSharingWithAwsOrganizationResponseResponseTypeDef",
    {
        "returnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPermissionRequestTypeDef = TypedDict(
    "_RequiredGetPermissionRequestTypeDef",
    {
        "permissionArn": str,
    },
)
_OptionalGetPermissionRequestTypeDef = TypedDict(
    "_OptionalGetPermissionRequestTypeDef",
    {
        "permissionVersion": int,
    },
    total=False,
)


class GetPermissionRequestTypeDef(
    _RequiredGetPermissionRequestTypeDef, _OptionalGetPermissionRequestTypeDef
):
    pass


GetPermissionResponseResponseTypeDef = TypedDict(
    "GetPermissionResponseResponseTypeDef",
    {
        "permission": "ResourceSharePermissionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourcePoliciesRequestTypeDef = TypedDict(
    "_RequiredGetResourcePoliciesRequestTypeDef",
    {
        "resourceArns": List[str],
    },
)
_OptionalGetResourcePoliciesRequestTypeDef = TypedDict(
    "_OptionalGetResourcePoliciesRequestTypeDef",
    {
        "principal": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetResourcePoliciesRequestTypeDef(
    _RequiredGetResourcePoliciesRequestTypeDef, _OptionalGetResourcePoliciesRequestTypeDef
):
    pass


GetResourcePoliciesResponseResponseTypeDef = TypedDict(
    "GetResourcePoliciesResponseResponseTypeDef",
    {
        "policies": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourceShareAssociationsRequestTypeDef = TypedDict(
    "_RequiredGetResourceShareAssociationsRequestTypeDef",
    {
        "associationType": ResourceShareAssociationTypeType,
    },
)
_OptionalGetResourceShareAssociationsRequestTypeDef = TypedDict(
    "_OptionalGetResourceShareAssociationsRequestTypeDef",
    {
        "resourceShareArns": List[str],
        "resourceArn": str,
        "principal": str,
        "associationStatus": ResourceShareAssociationStatusType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetResourceShareAssociationsRequestTypeDef(
    _RequiredGetResourceShareAssociationsRequestTypeDef,
    _OptionalGetResourceShareAssociationsRequestTypeDef,
):
    pass


GetResourceShareAssociationsResponseResponseTypeDef = TypedDict(
    "GetResourceShareAssociationsResponseResponseTypeDef",
    {
        "resourceShareAssociations": List["ResourceShareAssociationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceShareInvitationsRequestTypeDef = TypedDict(
    "GetResourceShareInvitationsRequestTypeDef",
    {
        "resourceShareInvitationArns": List[str],
        "resourceShareArns": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetResourceShareInvitationsResponseResponseTypeDef = TypedDict(
    "GetResourceShareInvitationsResponseResponseTypeDef",
    {
        "resourceShareInvitations": List["ResourceShareInvitationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourceSharesRequestTypeDef = TypedDict(
    "_RequiredGetResourceSharesRequestTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
    },
)
_OptionalGetResourceSharesRequestTypeDef = TypedDict(
    "_OptionalGetResourceSharesRequestTypeDef",
    {
        "resourceShareArns": List[str],
        "resourceShareStatus": ResourceShareStatusType,
        "name": str,
        "tagFilters": List["TagFilterTypeDef"],
        "nextToken": str,
        "maxResults": int,
        "permissionArn": str,
    },
    total=False,
)


class GetResourceSharesRequestTypeDef(
    _RequiredGetResourceSharesRequestTypeDef, _OptionalGetResourceSharesRequestTypeDef
):
    pass


GetResourceSharesResponseResponseTypeDef = TypedDict(
    "GetResourceSharesResponseResponseTypeDef",
    {
        "resourceShares": List["ResourceShareTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPendingInvitationResourcesRequestTypeDef = TypedDict(
    "_RequiredListPendingInvitationResourcesRequestTypeDef",
    {
        "resourceShareInvitationArn": str,
    },
)
_OptionalListPendingInvitationResourcesRequestTypeDef = TypedDict(
    "_OptionalListPendingInvitationResourcesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListPendingInvitationResourcesRequestTypeDef(
    _RequiredListPendingInvitationResourcesRequestTypeDef,
    _OptionalListPendingInvitationResourcesRequestTypeDef,
):
    pass


ListPendingInvitationResourcesResponseResponseTypeDef = TypedDict(
    "ListPendingInvitationResourcesResponseResponseTypeDef",
    {
        "resources": List["ResourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPermissionsRequestTypeDef = TypedDict(
    "ListPermissionsRequestTypeDef",
    {
        "resourceType": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListPermissionsResponseResponseTypeDef = TypedDict(
    "ListPermissionsResponseResponseTypeDef",
    {
        "permissions": List["ResourceSharePermissionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPrincipalsRequestTypeDef = TypedDict(
    "_RequiredListPrincipalsRequestTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
    },
)
_OptionalListPrincipalsRequestTypeDef = TypedDict(
    "_OptionalListPrincipalsRequestTypeDef",
    {
        "resourceArn": str,
        "principals": List[str],
        "resourceType": str,
        "resourceShareArns": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListPrincipalsRequestTypeDef(
    _RequiredListPrincipalsRequestTypeDef, _OptionalListPrincipalsRequestTypeDef
):
    pass


ListPrincipalsResponseResponseTypeDef = TypedDict(
    "ListPrincipalsResponseResponseTypeDef",
    {
        "principals": List["PrincipalTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourceSharePermissionsRequestTypeDef = TypedDict(
    "_RequiredListResourceSharePermissionsRequestTypeDef",
    {
        "resourceShareArn": str,
    },
)
_OptionalListResourceSharePermissionsRequestTypeDef = TypedDict(
    "_OptionalListResourceSharePermissionsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListResourceSharePermissionsRequestTypeDef(
    _RequiredListResourceSharePermissionsRequestTypeDef,
    _OptionalListResourceSharePermissionsRequestTypeDef,
):
    pass


ListResourceSharePermissionsResponseResponseTypeDef = TypedDict(
    "ListResourceSharePermissionsResponseResponseTypeDef",
    {
        "permissions": List["ResourceSharePermissionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceTypesRequestTypeDef = TypedDict(
    "ListResourceTypesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListResourceTypesResponseResponseTypeDef = TypedDict(
    "ListResourceTypesResponseResponseTypeDef",
    {
        "resourceTypes": List["ServiceNameAndResourceTypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourcesRequestTypeDef = TypedDict(
    "_RequiredListResourcesRequestTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
    },
)
_OptionalListResourcesRequestTypeDef = TypedDict(
    "_OptionalListResourcesRequestTypeDef",
    {
        "principal": str,
        "resourceType": str,
        "resourceArns": List[str],
        "resourceShareArns": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListResourcesRequestTypeDef(
    _RequiredListResourcesRequestTypeDef, _OptionalListResourcesRequestTypeDef
):
    pass


ListResourcesResponseResponseTypeDef = TypedDict(
    "ListResourcesResponseResponseTypeDef",
    {
        "resources": List["ResourceTypeDef"],
        "nextToken": str,
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

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "id": str,
        "resourceShareArn": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)

PromoteResourceShareCreatedFromPolicyRequestTypeDef = TypedDict(
    "PromoteResourceShareCreatedFromPolicyRequestTypeDef",
    {
        "resourceShareArn": str,
    },
)

PromoteResourceShareCreatedFromPolicyResponseResponseTypeDef = TypedDict(
    "PromoteResourceShareCreatedFromPolicyResponseResponseTypeDef",
    {
        "returnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRejectResourceShareInvitationRequestTypeDef = TypedDict(
    "_RequiredRejectResourceShareInvitationRequestTypeDef",
    {
        "resourceShareInvitationArn": str,
    },
)
_OptionalRejectResourceShareInvitationRequestTypeDef = TypedDict(
    "_OptionalRejectResourceShareInvitationRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class RejectResourceShareInvitationRequestTypeDef(
    _RequiredRejectResourceShareInvitationRequestTypeDef,
    _OptionalRejectResourceShareInvitationRequestTypeDef,
):
    pass


RejectResourceShareInvitationResponseResponseTypeDef = TypedDict(
    "RejectResourceShareInvitationResponseResponseTypeDef",
    {
        "resourceShareInvitation": "ResourceShareInvitationTypeDef",
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceShareAssociationTypeDef = TypedDict(
    "ResourceShareAssociationTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": ResourceShareAssociationTypeType,
        "status": ResourceShareAssociationStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)

ResourceShareInvitationTypeDef = TypedDict(
    "ResourceShareInvitationTypeDef",
    {
        "resourceShareInvitationArn": str,
        "resourceShareName": str,
        "resourceShareArn": str,
        "senderAccountId": str,
        "receiverAccountId": str,
        "invitationTimestamp": datetime,
        "status": ResourceShareInvitationStatusType,
        "resourceShareAssociations": List["ResourceShareAssociationTypeDef"],
        "receiverArn": str,
    },
    total=False,
)

ResourceSharePermissionDetailTypeDef = TypedDict(
    "ResourceSharePermissionDetailTypeDef",
    {
        "arn": str,
        "version": str,
        "defaultVersion": bool,
        "name": str,
        "resourceType": str,
        "permission": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "isResourceTypeDefault": bool,
    },
    total=False,
)

ResourceSharePermissionSummaryTypeDef = TypedDict(
    "ResourceSharePermissionSummaryTypeDef",
    {
        "arn": str,
        "version": str,
        "defaultVersion": bool,
        "name": str,
        "resourceType": str,
        "status": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "isResourceTypeDefault": bool,
    },
    total=False,
)

ResourceShareTypeDef = TypedDict(
    "ResourceShareTypeDef",
    {
        "resourceShareArn": str,
        "name": str,
        "owningAccountId": str,
        "allowExternalPrincipals": bool,
        "status": ResourceShareStatusType,
        "statusMessage": str,
        "tags": List["TagTypeDef"],
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "featureSet": ResourceShareFeatureSetType,
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "arn": str,
        "type": str,
        "resourceShareArn": str,
        "resourceGroupArn": str,
        "status": ResourceStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
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

ServiceNameAndResourceTypeTypeDef = TypedDict(
    "ServiceNameAndResourceTypeTypeDef",
    {
        "resourceType": str,
        "serviceName": str,
    },
    total=False,
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "tagKey": str,
        "tagValues": List[str],
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceShareArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceShareArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateResourceShareRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceShareRequestTypeDef",
    {
        "resourceShareArn": str,
    },
)
_OptionalUpdateResourceShareRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceShareRequestTypeDef",
    {
        "name": str,
        "allowExternalPrincipals": bool,
        "clientToken": str,
    },
    total=False,
)


class UpdateResourceShareRequestTypeDef(
    _RequiredUpdateResourceShareRequestTypeDef, _OptionalUpdateResourceShareRequestTypeDef
):
    pass


UpdateResourceShareResponseResponseTypeDef = TypedDict(
    "UpdateResourceShareResponseResponseTypeDef",
    {
        "resourceShare": "ResourceShareTypeDef",
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
