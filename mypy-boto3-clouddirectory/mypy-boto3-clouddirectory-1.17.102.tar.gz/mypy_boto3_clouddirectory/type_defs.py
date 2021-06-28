"""
Type annotations for clouddirectory service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/type_defs.html)

Usage::

    ```python
    from mypy_boto3_clouddirectory.type_defs import AddFacetToObjectRequestTypeDef

    data: AddFacetToObjectRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    BatchReadExceptionTypeType,
    ConsistencyLevelType,
    DirectoryStateType,
    FacetAttributeTypeType,
    FacetStyleType,
    ObjectTypeType,
    RangeModeType,
    RequiredAttributeBehaviorType,
    RuleTypeType,
    UpdateActionTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddFacetToObjectRequestTypeDef",
    "ApplySchemaRequestTypeDef",
    "ApplySchemaResponseResponseTypeDef",
    "AttachObjectRequestTypeDef",
    "AttachObjectResponseResponseTypeDef",
    "AttachPolicyRequestTypeDef",
    "AttachToIndexRequestTypeDef",
    "AttachToIndexResponseResponseTypeDef",
    "AttachTypedLinkRequestTypeDef",
    "AttachTypedLinkResponseResponseTypeDef",
    "AttributeKeyAndValueTypeDef",
    "AttributeKeyTypeDef",
    "AttributeNameAndValueTypeDef",
    "BatchAddFacetToObjectTypeDef",
    "BatchAttachObjectResponseTypeDef",
    "BatchAttachObjectTypeDef",
    "BatchAttachPolicyTypeDef",
    "BatchAttachToIndexResponseTypeDef",
    "BatchAttachToIndexTypeDef",
    "BatchAttachTypedLinkResponseTypeDef",
    "BatchAttachTypedLinkTypeDef",
    "BatchCreateIndexResponseTypeDef",
    "BatchCreateIndexTypeDef",
    "BatchCreateObjectResponseTypeDef",
    "BatchCreateObjectTypeDef",
    "BatchDeleteObjectTypeDef",
    "BatchDetachFromIndexResponseTypeDef",
    "BatchDetachFromIndexTypeDef",
    "BatchDetachObjectResponseTypeDef",
    "BatchDetachObjectTypeDef",
    "BatchDetachPolicyTypeDef",
    "BatchDetachTypedLinkTypeDef",
    "BatchGetLinkAttributesResponseTypeDef",
    "BatchGetLinkAttributesTypeDef",
    "BatchGetObjectAttributesResponseTypeDef",
    "BatchGetObjectAttributesTypeDef",
    "BatchGetObjectInformationResponseTypeDef",
    "BatchGetObjectInformationTypeDef",
    "BatchListAttachedIndicesResponseTypeDef",
    "BatchListAttachedIndicesTypeDef",
    "BatchListIncomingTypedLinksResponseTypeDef",
    "BatchListIncomingTypedLinksTypeDef",
    "BatchListIndexResponseTypeDef",
    "BatchListIndexTypeDef",
    "BatchListObjectAttributesResponseTypeDef",
    "BatchListObjectAttributesTypeDef",
    "BatchListObjectChildrenResponseTypeDef",
    "BatchListObjectChildrenTypeDef",
    "BatchListObjectParentPathsResponseTypeDef",
    "BatchListObjectParentPathsTypeDef",
    "BatchListObjectParentsResponseTypeDef",
    "BatchListObjectParentsTypeDef",
    "BatchListObjectPoliciesResponseTypeDef",
    "BatchListObjectPoliciesTypeDef",
    "BatchListOutgoingTypedLinksResponseTypeDef",
    "BatchListOutgoingTypedLinksTypeDef",
    "BatchListPolicyAttachmentsResponseTypeDef",
    "BatchListPolicyAttachmentsTypeDef",
    "BatchLookupPolicyResponseTypeDef",
    "BatchLookupPolicyTypeDef",
    "BatchReadExceptionTypeDef",
    "BatchReadOperationResponseTypeDef",
    "BatchReadOperationTypeDef",
    "BatchReadRequestTypeDef",
    "BatchReadResponseResponseTypeDef",
    "BatchReadSuccessfulResponseTypeDef",
    "BatchRemoveFacetFromObjectTypeDef",
    "BatchUpdateLinkAttributesTypeDef",
    "BatchUpdateObjectAttributesResponseTypeDef",
    "BatchUpdateObjectAttributesTypeDef",
    "BatchWriteOperationResponseTypeDef",
    "BatchWriteOperationTypeDef",
    "BatchWriteRequestTypeDef",
    "BatchWriteResponseResponseTypeDef",
    "CreateDirectoryRequestTypeDef",
    "CreateDirectoryResponseResponseTypeDef",
    "CreateFacetRequestTypeDef",
    "CreateIndexRequestTypeDef",
    "CreateIndexResponseResponseTypeDef",
    "CreateObjectRequestTypeDef",
    "CreateObjectResponseResponseTypeDef",
    "CreateSchemaRequestTypeDef",
    "CreateSchemaResponseResponseTypeDef",
    "CreateTypedLinkFacetRequestTypeDef",
    "DeleteDirectoryRequestTypeDef",
    "DeleteDirectoryResponseResponseTypeDef",
    "DeleteFacetRequestTypeDef",
    "DeleteObjectRequestTypeDef",
    "DeleteSchemaRequestTypeDef",
    "DeleteSchemaResponseResponseTypeDef",
    "DeleteTypedLinkFacetRequestTypeDef",
    "DetachFromIndexRequestTypeDef",
    "DetachFromIndexResponseResponseTypeDef",
    "DetachObjectRequestTypeDef",
    "DetachObjectResponseResponseTypeDef",
    "DetachPolicyRequestTypeDef",
    "DetachTypedLinkRequestTypeDef",
    "DirectoryTypeDef",
    "DisableDirectoryRequestTypeDef",
    "DisableDirectoryResponseResponseTypeDef",
    "EnableDirectoryRequestTypeDef",
    "EnableDirectoryResponseResponseTypeDef",
    "FacetAttributeDefinitionTypeDef",
    "FacetAttributeReferenceTypeDef",
    "FacetAttributeTypeDef",
    "FacetAttributeUpdateTypeDef",
    "FacetTypeDef",
    "GetAppliedSchemaVersionRequestTypeDef",
    "GetAppliedSchemaVersionResponseResponseTypeDef",
    "GetDirectoryRequestTypeDef",
    "GetDirectoryResponseResponseTypeDef",
    "GetFacetRequestTypeDef",
    "GetFacetResponseResponseTypeDef",
    "GetLinkAttributesRequestTypeDef",
    "GetLinkAttributesResponseResponseTypeDef",
    "GetObjectAttributesRequestTypeDef",
    "GetObjectAttributesResponseResponseTypeDef",
    "GetObjectInformationRequestTypeDef",
    "GetObjectInformationResponseResponseTypeDef",
    "GetSchemaAsJsonRequestTypeDef",
    "GetSchemaAsJsonResponseResponseTypeDef",
    "GetTypedLinkFacetInformationRequestTypeDef",
    "GetTypedLinkFacetInformationResponseResponseTypeDef",
    "IndexAttachmentTypeDef",
    "LinkAttributeActionTypeDef",
    "LinkAttributeUpdateTypeDef",
    "ListAppliedSchemaArnsRequestTypeDef",
    "ListAppliedSchemaArnsResponseResponseTypeDef",
    "ListAttachedIndicesRequestTypeDef",
    "ListAttachedIndicesResponseResponseTypeDef",
    "ListDevelopmentSchemaArnsRequestTypeDef",
    "ListDevelopmentSchemaArnsResponseResponseTypeDef",
    "ListDirectoriesRequestTypeDef",
    "ListDirectoriesResponseResponseTypeDef",
    "ListFacetAttributesRequestTypeDef",
    "ListFacetAttributesResponseResponseTypeDef",
    "ListFacetNamesRequestTypeDef",
    "ListFacetNamesResponseResponseTypeDef",
    "ListIncomingTypedLinksRequestTypeDef",
    "ListIncomingTypedLinksResponseResponseTypeDef",
    "ListIndexRequestTypeDef",
    "ListIndexResponseResponseTypeDef",
    "ListManagedSchemaArnsRequestTypeDef",
    "ListManagedSchemaArnsResponseResponseTypeDef",
    "ListObjectAttributesRequestTypeDef",
    "ListObjectAttributesResponseResponseTypeDef",
    "ListObjectChildrenRequestTypeDef",
    "ListObjectChildrenResponseResponseTypeDef",
    "ListObjectParentPathsRequestTypeDef",
    "ListObjectParentPathsResponseResponseTypeDef",
    "ListObjectParentsRequestTypeDef",
    "ListObjectParentsResponseResponseTypeDef",
    "ListObjectPoliciesRequestTypeDef",
    "ListObjectPoliciesResponseResponseTypeDef",
    "ListOutgoingTypedLinksRequestTypeDef",
    "ListOutgoingTypedLinksResponseResponseTypeDef",
    "ListPolicyAttachmentsRequestTypeDef",
    "ListPolicyAttachmentsResponseResponseTypeDef",
    "ListPublishedSchemaArnsRequestTypeDef",
    "ListPublishedSchemaArnsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTypedLinkFacetAttributesRequestTypeDef",
    "ListTypedLinkFacetAttributesResponseResponseTypeDef",
    "ListTypedLinkFacetNamesRequestTypeDef",
    "ListTypedLinkFacetNamesResponseResponseTypeDef",
    "LookupPolicyRequestTypeDef",
    "LookupPolicyResponseResponseTypeDef",
    "ObjectAttributeActionTypeDef",
    "ObjectAttributeRangeTypeDef",
    "ObjectAttributeUpdateTypeDef",
    "ObjectIdentifierAndLinkNameTupleTypeDef",
    "ObjectReferenceTypeDef",
    "PaginatorConfigTypeDef",
    "PathToObjectIdentifiersTypeDef",
    "PolicyAttachmentTypeDef",
    "PolicyToPathTypeDef",
    "PublishSchemaRequestTypeDef",
    "PublishSchemaResponseResponseTypeDef",
    "PutSchemaFromJsonRequestTypeDef",
    "PutSchemaFromJsonResponseResponseTypeDef",
    "RemoveFacetFromObjectRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RuleTypeDef",
    "SchemaFacetTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TypedAttributeValueRangeTypeDef",
    "TypedAttributeValueTypeDef",
    "TypedLinkAttributeDefinitionTypeDef",
    "TypedLinkAttributeRangeTypeDef",
    "TypedLinkFacetAttributeUpdateTypeDef",
    "TypedLinkFacetTypeDef",
    "TypedLinkSchemaAndFacetNameTypeDef",
    "TypedLinkSpecifierTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateFacetRequestTypeDef",
    "UpdateLinkAttributesRequestTypeDef",
    "UpdateObjectAttributesRequestTypeDef",
    "UpdateObjectAttributesResponseResponseTypeDef",
    "UpdateSchemaRequestTypeDef",
    "UpdateSchemaResponseResponseTypeDef",
    "UpdateTypedLinkFacetRequestTypeDef",
    "UpgradeAppliedSchemaRequestTypeDef",
    "UpgradeAppliedSchemaResponseResponseTypeDef",
    "UpgradePublishedSchemaRequestTypeDef",
    "UpgradePublishedSchemaResponseResponseTypeDef",
)

_RequiredAddFacetToObjectRequestTypeDef = TypedDict(
    "_RequiredAddFacetToObjectRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacet": "SchemaFacetTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalAddFacetToObjectRequestTypeDef = TypedDict(
    "_OptionalAddFacetToObjectRequestTypeDef",
    {
        "ObjectAttributeList": List["AttributeKeyAndValueTypeDef"],
    },
    total=False,
)


class AddFacetToObjectRequestTypeDef(
    _RequiredAddFacetToObjectRequestTypeDef, _OptionalAddFacetToObjectRequestTypeDef
):
    pass


ApplySchemaRequestTypeDef = TypedDict(
    "ApplySchemaRequestTypeDef",
    {
        "PublishedSchemaArn": str,
        "DirectoryArn": str,
    },
)

ApplySchemaResponseResponseTypeDef = TypedDict(
    "ApplySchemaResponseResponseTypeDef",
    {
        "AppliedSchemaArn": str,
        "DirectoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachObjectRequestTypeDef = TypedDict(
    "AttachObjectRequestTypeDef",
    {
        "DirectoryArn": str,
        "ParentReference": "ObjectReferenceTypeDef",
        "ChildReference": "ObjectReferenceTypeDef",
        "LinkName": str,
    },
)

AttachObjectResponseResponseTypeDef = TypedDict(
    "AttachObjectResponseResponseTypeDef",
    {
        "AttachedObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachPolicyRequestTypeDef = TypedDict(
    "AttachPolicyRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": "ObjectReferenceTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

AttachToIndexRequestTypeDef = TypedDict(
    "AttachToIndexRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": "ObjectReferenceTypeDef",
        "TargetReference": "ObjectReferenceTypeDef",
    },
)

AttachToIndexResponseResponseTypeDef = TypedDict(
    "AttachToIndexResponseResponseTypeDef",
    {
        "AttachedObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachTypedLinkRequestTypeDef = TypedDict(
    "AttachTypedLinkRequestTypeDef",
    {
        "DirectoryArn": str,
        "SourceObjectReference": "ObjectReferenceTypeDef",
        "TargetObjectReference": "ObjectReferenceTypeDef",
        "TypedLinkFacet": "TypedLinkSchemaAndFacetNameTypeDef",
        "Attributes": List["AttributeNameAndValueTypeDef"],
    },
)

AttachTypedLinkResponseResponseTypeDef = TypedDict(
    "AttachTypedLinkResponseResponseTypeDef",
    {
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttributeKeyAndValueTypeDef = TypedDict(
    "AttributeKeyAndValueTypeDef",
    {
        "Key": "AttributeKeyTypeDef",
        "Value": "TypedAttributeValueTypeDef",
    },
)

AttributeKeyTypeDef = TypedDict(
    "AttributeKeyTypeDef",
    {
        "SchemaArn": str,
        "FacetName": str,
        "Name": str,
    },
)

AttributeNameAndValueTypeDef = TypedDict(
    "AttributeNameAndValueTypeDef",
    {
        "AttributeName": str,
        "Value": "TypedAttributeValueTypeDef",
    },
)

BatchAddFacetToObjectTypeDef = TypedDict(
    "BatchAddFacetToObjectTypeDef",
    {
        "SchemaFacet": "SchemaFacetTypeDef",
        "ObjectAttributeList": List["AttributeKeyAndValueTypeDef"],
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchAttachObjectResponseTypeDef = TypedDict(
    "BatchAttachObjectResponseTypeDef",
    {
        "attachedObjectIdentifier": str,
    },
    total=False,
)

BatchAttachObjectTypeDef = TypedDict(
    "BatchAttachObjectTypeDef",
    {
        "ParentReference": "ObjectReferenceTypeDef",
        "ChildReference": "ObjectReferenceTypeDef",
        "LinkName": str,
    },
)

BatchAttachPolicyTypeDef = TypedDict(
    "BatchAttachPolicyTypeDef",
    {
        "PolicyReference": "ObjectReferenceTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchAttachToIndexResponseTypeDef = TypedDict(
    "BatchAttachToIndexResponseTypeDef",
    {
        "AttachedObjectIdentifier": str,
    },
    total=False,
)

BatchAttachToIndexTypeDef = TypedDict(
    "BatchAttachToIndexTypeDef",
    {
        "IndexReference": "ObjectReferenceTypeDef",
        "TargetReference": "ObjectReferenceTypeDef",
    },
)

BatchAttachTypedLinkResponseTypeDef = TypedDict(
    "BatchAttachTypedLinkResponseTypeDef",
    {
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
    },
    total=False,
)

BatchAttachTypedLinkTypeDef = TypedDict(
    "BatchAttachTypedLinkTypeDef",
    {
        "SourceObjectReference": "ObjectReferenceTypeDef",
        "TargetObjectReference": "ObjectReferenceTypeDef",
        "TypedLinkFacet": "TypedLinkSchemaAndFacetNameTypeDef",
        "Attributes": List["AttributeNameAndValueTypeDef"],
    },
)

BatchCreateIndexResponseTypeDef = TypedDict(
    "BatchCreateIndexResponseTypeDef",
    {
        "ObjectIdentifier": str,
    },
    total=False,
)

_RequiredBatchCreateIndexTypeDef = TypedDict(
    "_RequiredBatchCreateIndexTypeDef",
    {
        "OrderedIndexedAttributeList": List["AttributeKeyTypeDef"],
        "IsUnique": bool,
    },
)
_OptionalBatchCreateIndexTypeDef = TypedDict(
    "_OptionalBatchCreateIndexTypeDef",
    {
        "ParentReference": "ObjectReferenceTypeDef",
        "LinkName": str,
        "BatchReferenceName": str,
    },
    total=False,
)


class BatchCreateIndexTypeDef(_RequiredBatchCreateIndexTypeDef, _OptionalBatchCreateIndexTypeDef):
    pass


BatchCreateObjectResponseTypeDef = TypedDict(
    "BatchCreateObjectResponseTypeDef",
    {
        "ObjectIdentifier": str,
    },
    total=False,
)

_RequiredBatchCreateObjectTypeDef = TypedDict(
    "_RequiredBatchCreateObjectTypeDef",
    {
        "SchemaFacet": List["SchemaFacetTypeDef"],
        "ObjectAttributeList": List["AttributeKeyAndValueTypeDef"],
    },
)
_OptionalBatchCreateObjectTypeDef = TypedDict(
    "_OptionalBatchCreateObjectTypeDef",
    {
        "ParentReference": "ObjectReferenceTypeDef",
        "LinkName": str,
        "BatchReferenceName": str,
    },
    total=False,
)


class BatchCreateObjectTypeDef(
    _RequiredBatchCreateObjectTypeDef, _OptionalBatchCreateObjectTypeDef
):
    pass


BatchDeleteObjectTypeDef = TypedDict(
    "BatchDeleteObjectTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchDetachFromIndexResponseTypeDef = TypedDict(
    "BatchDetachFromIndexResponseTypeDef",
    {
        "DetachedObjectIdentifier": str,
    },
    total=False,
)

BatchDetachFromIndexTypeDef = TypedDict(
    "BatchDetachFromIndexTypeDef",
    {
        "IndexReference": "ObjectReferenceTypeDef",
        "TargetReference": "ObjectReferenceTypeDef",
    },
)

BatchDetachObjectResponseTypeDef = TypedDict(
    "BatchDetachObjectResponseTypeDef",
    {
        "detachedObjectIdentifier": str,
    },
    total=False,
)

_RequiredBatchDetachObjectTypeDef = TypedDict(
    "_RequiredBatchDetachObjectTypeDef",
    {
        "ParentReference": "ObjectReferenceTypeDef",
        "LinkName": str,
    },
)
_OptionalBatchDetachObjectTypeDef = TypedDict(
    "_OptionalBatchDetachObjectTypeDef",
    {
        "BatchReferenceName": str,
    },
    total=False,
)


class BatchDetachObjectTypeDef(
    _RequiredBatchDetachObjectTypeDef, _OptionalBatchDetachObjectTypeDef
):
    pass


BatchDetachPolicyTypeDef = TypedDict(
    "BatchDetachPolicyTypeDef",
    {
        "PolicyReference": "ObjectReferenceTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchDetachTypedLinkTypeDef = TypedDict(
    "BatchDetachTypedLinkTypeDef",
    {
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
    },
)

BatchGetLinkAttributesResponseTypeDef = TypedDict(
    "BatchGetLinkAttributesResponseTypeDef",
    {
        "Attributes": List["AttributeKeyAndValueTypeDef"],
    },
    total=False,
)

BatchGetLinkAttributesTypeDef = TypedDict(
    "BatchGetLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
        "AttributeNames": List[str],
    },
)

BatchGetObjectAttributesResponseTypeDef = TypedDict(
    "BatchGetObjectAttributesResponseTypeDef",
    {
        "Attributes": List["AttributeKeyAndValueTypeDef"],
    },
    total=False,
)

BatchGetObjectAttributesTypeDef = TypedDict(
    "BatchGetObjectAttributesTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
        "SchemaFacet": "SchemaFacetTypeDef",
        "AttributeNames": List[str],
    },
)

BatchGetObjectInformationResponseTypeDef = TypedDict(
    "BatchGetObjectInformationResponseTypeDef",
    {
        "SchemaFacets": List["SchemaFacetTypeDef"],
        "ObjectIdentifier": str,
    },
    total=False,
)

BatchGetObjectInformationTypeDef = TypedDict(
    "BatchGetObjectInformationTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchListAttachedIndicesResponseTypeDef = TypedDict(
    "BatchListAttachedIndicesResponseTypeDef",
    {
        "IndexAttachments": List["IndexAttachmentTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListAttachedIndicesTypeDef = TypedDict(
    "_RequiredBatchListAttachedIndicesTypeDef",
    {
        "TargetReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListAttachedIndicesTypeDef = TypedDict(
    "_OptionalBatchListAttachedIndicesTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchListAttachedIndicesTypeDef(
    _RequiredBatchListAttachedIndicesTypeDef, _OptionalBatchListAttachedIndicesTypeDef
):
    pass


BatchListIncomingTypedLinksResponseTypeDef = TypedDict(
    "BatchListIncomingTypedLinksResponseTypeDef",
    {
        "LinkSpecifiers": List["TypedLinkSpecifierTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListIncomingTypedLinksTypeDef = TypedDict(
    "_RequiredBatchListIncomingTypedLinksTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListIncomingTypedLinksTypeDef = TypedDict(
    "_OptionalBatchListIncomingTypedLinksTypeDef",
    {
        "FilterAttributeRanges": List["TypedLinkAttributeRangeTypeDef"],
        "FilterTypedLink": "TypedLinkSchemaAndFacetNameTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchListIncomingTypedLinksTypeDef(
    _RequiredBatchListIncomingTypedLinksTypeDef, _OptionalBatchListIncomingTypedLinksTypeDef
):
    pass


BatchListIndexResponseTypeDef = TypedDict(
    "BatchListIndexResponseTypeDef",
    {
        "IndexAttachments": List["IndexAttachmentTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListIndexTypeDef = TypedDict(
    "_RequiredBatchListIndexTypeDef",
    {
        "IndexReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListIndexTypeDef = TypedDict(
    "_OptionalBatchListIndexTypeDef",
    {
        "RangesOnIndexedValues": List["ObjectAttributeRangeTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class BatchListIndexTypeDef(_RequiredBatchListIndexTypeDef, _OptionalBatchListIndexTypeDef):
    pass


BatchListObjectAttributesResponseTypeDef = TypedDict(
    "BatchListObjectAttributesResponseTypeDef",
    {
        "Attributes": List["AttributeKeyAndValueTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListObjectAttributesTypeDef = TypedDict(
    "_RequiredBatchListObjectAttributesTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListObjectAttributesTypeDef = TypedDict(
    "_OptionalBatchListObjectAttributesTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "FacetFilter": "SchemaFacetTypeDef",
    },
    total=False,
)


class BatchListObjectAttributesTypeDef(
    _RequiredBatchListObjectAttributesTypeDef, _OptionalBatchListObjectAttributesTypeDef
):
    pass


BatchListObjectChildrenResponseTypeDef = TypedDict(
    "BatchListObjectChildrenResponseTypeDef",
    {
        "Children": Dict[str, str],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListObjectChildrenTypeDef = TypedDict(
    "_RequiredBatchListObjectChildrenTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListObjectChildrenTypeDef = TypedDict(
    "_OptionalBatchListObjectChildrenTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchListObjectChildrenTypeDef(
    _RequiredBatchListObjectChildrenTypeDef, _OptionalBatchListObjectChildrenTypeDef
):
    pass


BatchListObjectParentPathsResponseTypeDef = TypedDict(
    "BatchListObjectParentPathsResponseTypeDef",
    {
        "PathToObjectIdentifiersList": List["PathToObjectIdentifiersTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListObjectParentPathsTypeDef = TypedDict(
    "_RequiredBatchListObjectParentPathsTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListObjectParentPathsTypeDef = TypedDict(
    "_OptionalBatchListObjectParentPathsTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchListObjectParentPathsTypeDef(
    _RequiredBatchListObjectParentPathsTypeDef, _OptionalBatchListObjectParentPathsTypeDef
):
    pass


BatchListObjectParentsResponseTypeDef = TypedDict(
    "BatchListObjectParentsResponseTypeDef",
    {
        "ParentLinks": List["ObjectIdentifierAndLinkNameTupleTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListObjectParentsTypeDef = TypedDict(
    "_RequiredBatchListObjectParentsTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListObjectParentsTypeDef = TypedDict(
    "_OptionalBatchListObjectParentsTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchListObjectParentsTypeDef(
    _RequiredBatchListObjectParentsTypeDef, _OptionalBatchListObjectParentsTypeDef
):
    pass


BatchListObjectPoliciesResponseTypeDef = TypedDict(
    "BatchListObjectPoliciesResponseTypeDef",
    {
        "AttachedPolicyIds": List[str],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListObjectPoliciesTypeDef = TypedDict(
    "_RequiredBatchListObjectPoliciesTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListObjectPoliciesTypeDef = TypedDict(
    "_OptionalBatchListObjectPoliciesTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchListObjectPoliciesTypeDef(
    _RequiredBatchListObjectPoliciesTypeDef, _OptionalBatchListObjectPoliciesTypeDef
):
    pass


BatchListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "BatchListOutgoingTypedLinksResponseTypeDef",
    {
        "TypedLinkSpecifiers": List["TypedLinkSpecifierTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListOutgoingTypedLinksTypeDef = TypedDict(
    "_RequiredBatchListOutgoingTypedLinksTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListOutgoingTypedLinksTypeDef = TypedDict(
    "_OptionalBatchListOutgoingTypedLinksTypeDef",
    {
        "FilterAttributeRanges": List["TypedLinkAttributeRangeTypeDef"],
        "FilterTypedLink": "TypedLinkSchemaAndFacetNameTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchListOutgoingTypedLinksTypeDef(
    _RequiredBatchListOutgoingTypedLinksTypeDef, _OptionalBatchListOutgoingTypedLinksTypeDef
):
    pass


BatchListPolicyAttachmentsResponseTypeDef = TypedDict(
    "BatchListPolicyAttachmentsResponseTypeDef",
    {
        "ObjectIdentifiers": List[str],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchListPolicyAttachmentsTypeDef = TypedDict(
    "_RequiredBatchListPolicyAttachmentsTypeDef",
    {
        "PolicyReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchListPolicyAttachmentsTypeDef = TypedDict(
    "_OptionalBatchListPolicyAttachmentsTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchListPolicyAttachmentsTypeDef(
    _RequiredBatchListPolicyAttachmentsTypeDef, _OptionalBatchListPolicyAttachmentsTypeDef
):
    pass


BatchLookupPolicyResponseTypeDef = TypedDict(
    "BatchLookupPolicyResponseTypeDef",
    {
        "PolicyToPathList": List["PolicyToPathTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredBatchLookupPolicyTypeDef = TypedDict(
    "_RequiredBatchLookupPolicyTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalBatchLookupPolicyTypeDef = TypedDict(
    "_OptionalBatchLookupPolicyTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchLookupPolicyTypeDef(
    _RequiredBatchLookupPolicyTypeDef, _OptionalBatchLookupPolicyTypeDef
):
    pass


BatchReadExceptionTypeDef = TypedDict(
    "BatchReadExceptionTypeDef",
    {
        "Type": BatchReadExceptionTypeType,
        "Message": str,
    },
    total=False,
)

BatchReadOperationResponseTypeDef = TypedDict(
    "BatchReadOperationResponseTypeDef",
    {
        "SuccessfulResponse": "BatchReadSuccessfulResponseTypeDef",
        "ExceptionResponse": "BatchReadExceptionTypeDef",
    },
    total=False,
)

BatchReadOperationTypeDef = TypedDict(
    "BatchReadOperationTypeDef",
    {
        "ListObjectAttributes": "BatchListObjectAttributesTypeDef",
        "ListObjectChildren": "BatchListObjectChildrenTypeDef",
        "ListAttachedIndices": "BatchListAttachedIndicesTypeDef",
        "ListObjectParentPaths": "BatchListObjectParentPathsTypeDef",
        "GetObjectInformation": "BatchGetObjectInformationTypeDef",
        "GetObjectAttributes": "BatchGetObjectAttributesTypeDef",
        "ListObjectParents": "BatchListObjectParentsTypeDef",
        "ListObjectPolicies": "BatchListObjectPoliciesTypeDef",
        "ListPolicyAttachments": "BatchListPolicyAttachmentsTypeDef",
        "LookupPolicy": "BatchLookupPolicyTypeDef",
        "ListIndex": "BatchListIndexTypeDef",
        "ListOutgoingTypedLinks": "BatchListOutgoingTypedLinksTypeDef",
        "ListIncomingTypedLinks": "BatchListIncomingTypedLinksTypeDef",
        "GetLinkAttributes": "BatchGetLinkAttributesTypeDef",
    },
    total=False,
)

_RequiredBatchReadRequestTypeDef = TypedDict(
    "_RequiredBatchReadRequestTypeDef",
    {
        "DirectoryArn": str,
        "Operations": List["BatchReadOperationTypeDef"],
    },
)
_OptionalBatchReadRequestTypeDef = TypedDict(
    "_OptionalBatchReadRequestTypeDef",
    {
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class BatchReadRequestTypeDef(_RequiredBatchReadRequestTypeDef, _OptionalBatchReadRequestTypeDef):
    pass


BatchReadResponseResponseTypeDef = TypedDict(
    "BatchReadResponseResponseTypeDef",
    {
        "Responses": List["BatchReadOperationResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchReadSuccessfulResponseTypeDef = TypedDict(
    "BatchReadSuccessfulResponseTypeDef",
    {
        "ListObjectAttributes": "BatchListObjectAttributesResponseTypeDef",
        "ListObjectChildren": "BatchListObjectChildrenResponseTypeDef",
        "GetObjectInformation": "BatchGetObjectInformationResponseTypeDef",
        "GetObjectAttributes": "BatchGetObjectAttributesResponseTypeDef",
        "ListAttachedIndices": "BatchListAttachedIndicesResponseTypeDef",
        "ListObjectParentPaths": "BatchListObjectParentPathsResponseTypeDef",
        "ListObjectPolicies": "BatchListObjectPoliciesResponseTypeDef",
        "ListPolicyAttachments": "BatchListPolicyAttachmentsResponseTypeDef",
        "LookupPolicy": "BatchLookupPolicyResponseTypeDef",
        "ListIndex": "BatchListIndexResponseTypeDef",
        "ListOutgoingTypedLinks": "BatchListOutgoingTypedLinksResponseTypeDef",
        "ListIncomingTypedLinks": "BatchListIncomingTypedLinksResponseTypeDef",
        "GetLinkAttributes": "BatchGetLinkAttributesResponseTypeDef",
        "ListObjectParents": "BatchListObjectParentsResponseTypeDef",
    },
    total=False,
)

BatchRemoveFacetFromObjectTypeDef = TypedDict(
    "BatchRemoveFacetFromObjectTypeDef",
    {
        "SchemaFacet": "SchemaFacetTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

BatchUpdateLinkAttributesTypeDef = TypedDict(
    "BatchUpdateLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
        "AttributeUpdates": List["LinkAttributeUpdateTypeDef"],
    },
)

BatchUpdateObjectAttributesResponseTypeDef = TypedDict(
    "BatchUpdateObjectAttributesResponseTypeDef",
    {
        "ObjectIdentifier": str,
    },
    total=False,
)

BatchUpdateObjectAttributesTypeDef = TypedDict(
    "BatchUpdateObjectAttributesTypeDef",
    {
        "ObjectReference": "ObjectReferenceTypeDef",
        "AttributeUpdates": List["ObjectAttributeUpdateTypeDef"],
    },
)

BatchWriteOperationResponseTypeDef = TypedDict(
    "BatchWriteOperationResponseTypeDef",
    {
        "CreateObject": "BatchCreateObjectResponseTypeDef",
        "AttachObject": "BatchAttachObjectResponseTypeDef",
        "DetachObject": "BatchDetachObjectResponseTypeDef",
        "UpdateObjectAttributes": "BatchUpdateObjectAttributesResponseTypeDef",
        "DeleteObject": Dict[str, Any],
        "AddFacetToObject": Dict[str, Any],
        "RemoveFacetFromObject": Dict[str, Any],
        "AttachPolicy": Dict[str, Any],
        "DetachPolicy": Dict[str, Any],
        "CreateIndex": "BatchCreateIndexResponseTypeDef",
        "AttachToIndex": "BatchAttachToIndexResponseTypeDef",
        "DetachFromIndex": "BatchDetachFromIndexResponseTypeDef",
        "AttachTypedLink": "BatchAttachTypedLinkResponseTypeDef",
        "DetachTypedLink": Dict[str, Any],
        "UpdateLinkAttributes": Dict[str, Any],
    },
    total=False,
)

BatchWriteOperationTypeDef = TypedDict(
    "BatchWriteOperationTypeDef",
    {
        "CreateObject": "BatchCreateObjectTypeDef",
        "AttachObject": "BatchAttachObjectTypeDef",
        "DetachObject": "BatchDetachObjectTypeDef",
        "UpdateObjectAttributes": "BatchUpdateObjectAttributesTypeDef",
        "DeleteObject": "BatchDeleteObjectTypeDef",
        "AddFacetToObject": "BatchAddFacetToObjectTypeDef",
        "RemoveFacetFromObject": "BatchRemoveFacetFromObjectTypeDef",
        "AttachPolicy": "BatchAttachPolicyTypeDef",
        "DetachPolicy": "BatchDetachPolicyTypeDef",
        "CreateIndex": "BatchCreateIndexTypeDef",
        "AttachToIndex": "BatchAttachToIndexTypeDef",
        "DetachFromIndex": "BatchDetachFromIndexTypeDef",
        "AttachTypedLink": "BatchAttachTypedLinkTypeDef",
        "DetachTypedLink": "BatchDetachTypedLinkTypeDef",
        "UpdateLinkAttributes": "BatchUpdateLinkAttributesTypeDef",
    },
    total=False,
)

BatchWriteRequestTypeDef = TypedDict(
    "BatchWriteRequestTypeDef",
    {
        "DirectoryArn": str,
        "Operations": List["BatchWriteOperationTypeDef"],
    },
)

BatchWriteResponseResponseTypeDef = TypedDict(
    "BatchWriteResponseResponseTypeDef",
    {
        "Responses": List["BatchWriteOperationResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDirectoryRequestTypeDef = TypedDict(
    "CreateDirectoryRequestTypeDef",
    {
        "Name": str,
        "SchemaArn": str,
    },
)

CreateDirectoryResponseResponseTypeDef = TypedDict(
    "CreateDirectoryResponseResponseTypeDef",
    {
        "DirectoryArn": str,
        "Name": str,
        "ObjectIdentifier": str,
        "AppliedSchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFacetRequestTypeDef = TypedDict(
    "_RequiredCreateFacetRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
_OptionalCreateFacetRequestTypeDef = TypedDict(
    "_OptionalCreateFacetRequestTypeDef",
    {
        "Attributes": List["FacetAttributeTypeDef"],
        "ObjectType": ObjectTypeType,
        "FacetStyle": FacetStyleType,
    },
    total=False,
)


class CreateFacetRequestTypeDef(
    _RequiredCreateFacetRequestTypeDef, _OptionalCreateFacetRequestTypeDef
):
    pass


_RequiredCreateIndexRequestTypeDef = TypedDict(
    "_RequiredCreateIndexRequestTypeDef",
    {
        "DirectoryArn": str,
        "OrderedIndexedAttributeList": List["AttributeKeyTypeDef"],
        "IsUnique": bool,
    },
)
_OptionalCreateIndexRequestTypeDef = TypedDict(
    "_OptionalCreateIndexRequestTypeDef",
    {
        "ParentReference": "ObjectReferenceTypeDef",
        "LinkName": str,
    },
    total=False,
)


class CreateIndexRequestTypeDef(
    _RequiredCreateIndexRequestTypeDef, _OptionalCreateIndexRequestTypeDef
):
    pass


CreateIndexResponseResponseTypeDef = TypedDict(
    "CreateIndexResponseResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateObjectRequestTypeDef = TypedDict(
    "_RequiredCreateObjectRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacets": List["SchemaFacetTypeDef"],
    },
)
_OptionalCreateObjectRequestTypeDef = TypedDict(
    "_OptionalCreateObjectRequestTypeDef",
    {
        "ObjectAttributeList": List["AttributeKeyAndValueTypeDef"],
        "ParentReference": "ObjectReferenceTypeDef",
        "LinkName": str,
    },
    total=False,
)


class CreateObjectRequestTypeDef(
    _RequiredCreateObjectRequestTypeDef, _OptionalCreateObjectRequestTypeDef
):
    pass


CreateObjectResponseResponseTypeDef = TypedDict(
    "CreateObjectResponseResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSchemaRequestTypeDef = TypedDict(
    "CreateSchemaRequestTypeDef",
    {
        "Name": str,
    },
)

CreateSchemaResponseResponseTypeDef = TypedDict(
    "CreateSchemaResponseResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTypedLinkFacetRequestTypeDef = TypedDict(
    "CreateTypedLinkFacetRequestTypeDef",
    {
        "SchemaArn": str,
        "Facet": "TypedLinkFacetTypeDef",
    },
)

DeleteDirectoryRequestTypeDef = TypedDict(
    "DeleteDirectoryRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)

DeleteDirectoryResponseResponseTypeDef = TypedDict(
    "DeleteDirectoryResponseResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFacetRequestTypeDef = TypedDict(
    "DeleteFacetRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

DeleteObjectRequestTypeDef = TypedDict(
    "DeleteObjectRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

DeleteSchemaRequestTypeDef = TypedDict(
    "DeleteSchemaRequestTypeDef",
    {
        "SchemaArn": str,
    },
)

DeleteSchemaResponseResponseTypeDef = TypedDict(
    "DeleteSchemaResponseResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTypedLinkFacetRequestTypeDef = TypedDict(
    "DeleteTypedLinkFacetRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

DetachFromIndexRequestTypeDef = TypedDict(
    "DetachFromIndexRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": "ObjectReferenceTypeDef",
        "TargetReference": "ObjectReferenceTypeDef",
    },
)

DetachFromIndexResponseResponseTypeDef = TypedDict(
    "DetachFromIndexResponseResponseTypeDef",
    {
        "DetachedObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachObjectRequestTypeDef = TypedDict(
    "DetachObjectRequestTypeDef",
    {
        "DirectoryArn": str,
        "ParentReference": "ObjectReferenceTypeDef",
        "LinkName": str,
    },
)

DetachObjectResponseResponseTypeDef = TypedDict(
    "DetachObjectResponseResponseTypeDef",
    {
        "DetachedObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachPolicyRequestTypeDef = TypedDict(
    "DetachPolicyRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": "ObjectReferenceTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)

DetachTypedLinkRequestTypeDef = TypedDict(
    "DetachTypedLinkRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
    },
)

DirectoryTypeDef = TypedDict(
    "DirectoryTypeDef",
    {
        "Name": str,
        "DirectoryArn": str,
        "State": DirectoryStateType,
        "CreationDateTime": datetime,
    },
    total=False,
)

DisableDirectoryRequestTypeDef = TypedDict(
    "DisableDirectoryRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)

DisableDirectoryResponseResponseTypeDef = TypedDict(
    "DisableDirectoryResponseResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableDirectoryRequestTypeDef = TypedDict(
    "EnableDirectoryRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)

EnableDirectoryResponseResponseTypeDef = TypedDict(
    "EnableDirectoryResponseResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFacetAttributeDefinitionTypeDef = TypedDict(
    "_RequiredFacetAttributeDefinitionTypeDef",
    {
        "Type": FacetAttributeTypeType,
    },
)
_OptionalFacetAttributeDefinitionTypeDef = TypedDict(
    "_OptionalFacetAttributeDefinitionTypeDef",
    {
        "DefaultValue": "TypedAttributeValueTypeDef",
        "IsImmutable": bool,
        "Rules": Dict[str, "RuleTypeDef"],
    },
    total=False,
)


class FacetAttributeDefinitionTypeDef(
    _RequiredFacetAttributeDefinitionTypeDef, _OptionalFacetAttributeDefinitionTypeDef
):
    pass


FacetAttributeReferenceTypeDef = TypedDict(
    "FacetAttributeReferenceTypeDef",
    {
        "TargetFacetName": str,
        "TargetAttributeName": str,
    },
)

_RequiredFacetAttributeTypeDef = TypedDict(
    "_RequiredFacetAttributeTypeDef",
    {
        "Name": str,
    },
)
_OptionalFacetAttributeTypeDef = TypedDict(
    "_OptionalFacetAttributeTypeDef",
    {
        "AttributeDefinition": "FacetAttributeDefinitionTypeDef",
        "AttributeReference": "FacetAttributeReferenceTypeDef",
        "RequiredBehavior": RequiredAttributeBehaviorType,
    },
    total=False,
)


class FacetAttributeTypeDef(_RequiredFacetAttributeTypeDef, _OptionalFacetAttributeTypeDef):
    pass


FacetAttributeUpdateTypeDef = TypedDict(
    "FacetAttributeUpdateTypeDef",
    {
        "Attribute": "FacetAttributeTypeDef",
        "Action": UpdateActionTypeType,
    },
    total=False,
)

FacetTypeDef = TypedDict(
    "FacetTypeDef",
    {
        "Name": str,
        "ObjectType": ObjectTypeType,
        "FacetStyle": FacetStyleType,
    },
    total=False,
)

GetAppliedSchemaVersionRequestTypeDef = TypedDict(
    "GetAppliedSchemaVersionRequestTypeDef",
    {
        "SchemaArn": str,
    },
)

GetAppliedSchemaVersionResponseResponseTypeDef = TypedDict(
    "GetAppliedSchemaVersionResponseResponseTypeDef",
    {
        "AppliedSchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDirectoryRequestTypeDef = TypedDict(
    "GetDirectoryRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)

GetDirectoryResponseResponseTypeDef = TypedDict(
    "GetDirectoryResponseResponseTypeDef",
    {
        "Directory": "DirectoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFacetRequestTypeDef = TypedDict(
    "GetFacetRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

GetFacetResponseResponseTypeDef = TypedDict(
    "GetFacetResponseResponseTypeDef",
    {
        "Facet": "FacetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLinkAttributesRequestTypeDef = TypedDict(
    "_RequiredGetLinkAttributesRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
        "AttributeNames": List[str],
    },
)
_OptionalGetLinkAttributesRequestTypeDef = TypedDict(
    "_OptionalGetLinkAttributesRequestTypeDef",
    {
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class GetLinkAttributesRequestTypeDef(
    _RequiredGetLinkAttributesRequestTypeDef, _OptionalGetLinkAttributesRequestTypeDef
):
    pass


GetLinkAttributesResponseResponseTypeDef = TypedDict(
    "GetLinkAttributesResponseResponseTypeDef",
    {
        "Attributes": List["AttributeKeyAndValueTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectAttributesRequestTypeDef = TypedDict(
    "_RequiredGetObjectAttributesRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
        "SchemaFacet": "SchemaFacetTypeDef",
        "AttributeNames": List[str],
    },
)
_OptionalGetObjectAttributesRequestTypeDef = TypedDict(
    "_OptionalGetObjectAttributesRequestTypeDef",
    {
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class GetObjectAttributesRequestTypeDef(
    _RequiredGetObjectAttributesRequestTypeDef, _OptionalGetObjectAttributesRequestTypeDef
):
    pass


GetObjectAttributesResponseResponseTypeDef = TypedDict(
    "GetObjectAttributesResponseResponseTypeDef",
    {
        "Attributes": List["AttributeKeyAndValueTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectInformationRequestTypeDef = TypedDict(
    "_RequiredGetObjectInformationRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalGetObjectInformationRequestTypeDef = TypedDict(
    "_OptionalGetObjectInformationRequestTypeDef",
    {
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class GetObjectInformationRequestTypeDef(
    _RequiredGetObjectInformationRequestTypeDef, _OptionalGetObjectInformationRequestTypeDef
):
    pass


GetObjectInformationResponseResponseTypeDef = TypedDict(
    "GetObjectInformationResponseResponseTypeDef",
    {
        "SchemaFacets": List["SchemaFacetTypeDef"],
        "ObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaAsJsonRequestTypeDef = TypedDict(
    "GetSchemaAsJsonRequestTypeDef",
    {
        "SchemaArn": str,
    },
)

GetSchemaAsJsonResponseResponseTypeDef = TypedDict(
    "GetSchemaAsJsonResponseResponseTypeDef",
    {
        "Name": str,
        "Document": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTypedLinkFacetInformationRequestTypeDef = TypedDict(
    "GetTypedLinkFacetInformationRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

GetTypedLinkFacetInformationResponseResponseTypeDef = TypedDict(
    "GetTypedLinkFacetInformationResponseResponseTypeDef",
    {
        "IdentityAttributeOrder": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IndexAttachmentTypeDef = TypedDict(
    "IndexAttachmentTypeDef",
    {
        "IndexedAttributes": List["AttributeKeyAndValueTypeDef"],
        "ObjectIdentifier": str,
    },
    total=False,
)

LinkAttributeActionTypeDef = TypedDict(
    "LinkAttributeActionTypeDef",
    {
        "AttributeActionType": UpdateActionTypeType,
        "AttributeUpdateValue": "TypedAttributeValueTypeDef",
    },
    total=False,
)

LinkAttributeUpdateTypeDef = TypedDict(
    "LinkAttributeUpdateTypeDef",
    {
        "AttributeKey": "AttributeKeyTypeDef",
        "AttributeAction": "LinkAttributeActionTypeDef",
    },
    total=False,
)

_RequiredListAppliedSchemaArnsRequestTypeDef = TypedDict(
    "_RequiredListAppliedSchemaArnsRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)
_OptionalListAppliedSchemaArnsRequestTypeDef = TypedDict(
    "_OptionalListAppliedSchemaArnsRequestTypeDef",
    {
        "SchemaArn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAppliedSchemaArnsRequestTypeDef(
    _RequiredListAppliedSchemaArnsRequestTypeDef, _OptionalListAppliedSchemaArnsRequestTypeDef
):
    pass


ListAppliedSchemaArnsResponseResponseTypeDef = TypedDict(
    "ListAppliedSchemaArnsResponseResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAttachedIndicesRequestTypeDef = TypedDict(
    "_RequiredListAttachedIndicesRequestTypeDef",
    {
        "DirectoryArn": str,
        "TargetReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListAttachedIndicesRequestTypeDef = TypedDict(
    "_OptionalListAttachedIndicesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class ListAttachedIndicesRequestTypeDef(
    _RequiredListAttachedIndicesRequestTypeDef, _OptionalListAttachedIndicesRequestTypeDef
):
    pass


ListAttachedIndicesResponseResponseTypeDef = TypedDict(
    "ListAttachedIndicesResponseResponseTypeDef",
    {
        "IndexAttachments": List["IndexAttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevelopmentSchemaArnsRequestTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDevelopmentSchemaArnsResponseResponseTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsResponseResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDirectoriesRequestTypeDef = TypedDict(
    "ListDirectoriesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "state": DirectoryStateType,
    },
    total=False,
)

ListDirectoriesResponseResponseTypeDef = TypedDict(
    "ListDirectoriesResponseResponseTypeDef",
    {
        "Directories": List["DirectoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFacetAttributesRequestTypeDef = TypedDict(
    "_RequiredListFacetAttributesRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
_OptionalListFacetAttributesRequestTypeDef = TypedDict(
    "_OptionalListFacetAttributesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListFacetAttributesRequestTypeDef(
    _RequiredListFacetAttributesRequestTypeDef, _OptionalListFacetAttributesRequestTypeDef
):
    pass


ListFacetAttributesResponseResponseTypeDef = TypedDict(
    "ListFacetAttributesResponseResponseTypeDef",
    {
        "Attributes": List["FacetAttributeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFacetNamesRequestTypeDef = TypedDict(
    "_RequiredListFacetNamesRequestTypeDef",
    {
        "SchemaArn": str,
    },
)
_OptionalListFacetNamesRequestTypeDef = TypedDict(
    "_OptionalListFacetNamesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListFacetNamesRequestTypeDef(
    _RequiredListFacetNamesRequestTypeDef, _OptionalListFacetNamesRequestTypeDef
):
    pass


ListFacetNamesResponseResponseTypeDef = TypedDict(
    "ListFacetNamesResponseResponseTypeDef",
    {
        "FacetNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIncomingTypedLinksRequestTypeDef = TypedDict(
    "_RequiredListIncomingTypedLinksRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListIncomingTypedLinksRequestTypeDef = TypedDict(
    "_OptionalListIncomingTypedLinksRequestTypeDef",
    {
        "FilterAttributeRanges": List["TypedLinkAttributeRangeTypeDef"],
        "FilterTypedLink": "TypedLinkSchemaAndFacetNameTypeDef",
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class ListIncomingTypedLinksRequestTypeDef(
    _RequiredListIncomingTypedLinksRequestTypeDef, _OptionalListIncomingTypedLinksRequestTypeDef
):
    pass


ListIncomingTypedLinksResponseResponseTypeDef = TypedDict(
    "ListIncomingTypedLinksResponseResponseTypeDef",
    {
        "LinkSpecifiers": List["TypedLinkSpecifierTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIndexRequestTypeDef = TypedDict(
    "_RequiredListIndexRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListIndexRequestTypeDef = TypedDict(
    "_OptionalListIndexRequestTypeDef",
    {
        "RangesOnIndexedValues": List["ObjectAttributeRangeTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class ListIndexRequestTypeDef(_RequiredListIndexRequestTypeDef, _OptionalListIndexRequestTypeDef):
    pass


ListIndexResponseResponseTypeDef = TypedDict(
    "ListIndexResponseResponseTypeDef",
    {
        "IndexAttachments": List["IndexAttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListManagedSchemaArnsRequestTypeDef = TypedDict(
    "ListManagedSchemaArnsRequestTypeDef",
    {
        "SchemaArn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListManagedSchemaArnsResponseResponseTypeDef = TypedDict(
    "ListManagedSchemaArnsResponseResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListObjectAttributesRequestTypeDef = TypedDict(
    "_RequiredListObjectAttributesRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListObjectAttributesRequestTypeDef = TypedDict(
    "_OptionalListObjectAttributesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
        "FacetFilter": "SchemaFacetTypeDef",
    },
    total=False,
)


class ListObjectAttributesRequestTypeDef(
    _RequiredListObjectAttributesRequestTypeDef, _OptionalListObjectAttributesRequestTypeDef
):
    pass


ListObjectAttributesResponseResponseTypeDef = TypedDict(
    "ListObjectAttributesResponseResponseTypeDef",
    {
        "Attributes": List["AttributeKeyAndValueTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListObjectChildrenRequestTypeDef = TypedDict(
    "_RequiredListObjectChildrenRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListObjectChildrenRequestTypeDef = TypedDict(
    "_OptionalListObjectChildrenRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class ListObjectChildrenRequestTypeDef(
    _RequiredListObjectChildrenRequestTypeDef, _OptionalListObjectChildrenRequestTypeDef
):
    pass


ListObjectChildrenResponseResponseTypeDef = TypedDict(
    "ListObjectChildrenResponseResponseTypeDef",
    {
        "Children": Dict[str, str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListObjectParentPathsRequestTypeDef = TypedDict(
    "_RequiredListObjectParentPathsRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListObjectParentPathsRequestTypeDef = TypedDict(
    "_OptionalListObjectParentPathsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListObjectParentPathsRequestTypeDef(
    _RequiredListObjectParentPathsRequestTypeDef, _OptionalListObjectParentPathsRequestTypeDef
):
    pass


ListObjectParentPathsResponseResponseTypeDef = TypedDict(
    "ListObjectParentPathsResponseResponseTypeDef",
    {
        "PathToObjectIdentifiersList": List["PathToObjectIdentifiersTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListObjectParentsRequestTypeDef = TypedDict(
    "_RequiredListObjectParentsRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListObjectParentsRequestTypeDef = TypedDict(
    "_OptionalListObjectParentsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
        "IncludeAllLinksToEachParent": bool,
    },
    total=False,
)


class ListObjectParentsRequestTypeDef(
    _RequiredListObjectParentsRequestTypeDef, _OptionalListObjectParentsRequestTypeDef
):
    pass


ListObjectParentsResponseResponseTypeDef = TypedDict(
    "ListObjectParentsResponseResponseTypeDef",
    {
        "Parents": Dict[str, str],
        "NextToken": str,
        "ParentLinks": List["ObjectIdentifierAndLinkNameTupleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListObjectPoliciesRequestTypeDef = TypedDict(
    "_RequiredListObjectPoliciesRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListObjectPoliciesRequestTypeDef = TypedDict(
    "_OptionalListObjectPoliciesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class ListObjectPoliciesRequestTypeDef(
    _RequiredListObjectPoliciesRequestTypeDef, _OptionalListObjectPoliciesRequestTypeDef
):
    pass


ListObjectPoliciesResponseResponseTypeDef = TypedDict(
    "ListObjectPoliciesResponseResponseTypeDef",
    {
        "AttachedPolicyIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListOutgoingTypedLinksRequestTypeDef = TypedDict(
    "_RequiredListOutgoingTypedLinksRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListOutgoingTypedLinksRequestTypeDef = TypedDict(
    "_OptionalListOutgoingTypedLinksRequestTypeDef",
    {
        "FilterAttributeRanges": List["TypedLinkAttributeRangeTypeDef"],
        "FilterTypedLink": "TypedLinkSchemaAndFacetNameTypeDef",
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class ListOutgoingTypedLinksRequestTypeDef(
    _RequiredListOutgoingTypedLinksRequestTypeDef, _OptionalListOutgoingTypedLinksRequestTypeDef
):
    pass


ListOutgoingTypedLinksResponseResponseTypeDef = TypedDict(
    "ListOutgoingTypedLinksResponseResponseTypeDef",
    {
        "TypedLinkSpecifiers": List["TypedLinkSpecifierTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPolicyAttachmentsRequestTypeDef = TypedDict(
    "_RequiredListPolicyAttachmentsRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": "ObjectReferenceTypeDef",
    },
)
_OptionalListPolicyAttachmentsRequestTypeDef = TypedDict(
    "_OptionalListPolicyAttachmentsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class ListPolicyAttachmentsRequestTypeDef(
    _RequiredListPolicyAttachmentsRequestTypeDef, _OptionalListPolicyAttachmentsRequestTypeDef
):
    pass


ListPolicyAttachmentsResponseResponseTypeDef = TypedDict(
    "ListPolicyAttachmentsResponseResponseTypeDef",
    {
        "ObjectIdentifiers": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPublishedSchemaArnsRequestTypeDef = TypedDict(
    "ListPublishedSchemaArnsRequestTypeDef",
    {
        "SchemaArn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPublishedSchemaArnsResponseResponseTypeDef = TypedDict(
    "ListPublishedSchemaArnsResponseResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
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

_RequiredListTypedLinkFacetAttributesRequestTypeDef = TypedDict(
    "_RequiredListTypedLinkFacetAttributesRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
_OptionalListTypedLinkFacetAttributesRequestTypeDef = TypedDict(
    "_OptionalListTypedLinkFacetAttributesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTypedLinkFacetAttributesRequestTypeDef(
    _RequiredListTypedLinkFacetAttributesRequestTypeDef,
    _OptionalListTypedLinkFacetAttributesRequestTypeDef,
):
    pass


ListTypedLinkFacetAttributesResponseResponseTypeDef = TypedDict(
    "ListTypedLinkFacetAttributesResponseResponseTypeDef",
    {
        "Attributes": List["TypedLinkAttributeDefinitionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTypedLinkFacetNamesRequestTypeDef = TypedDict(
    "_RequiredListTypedLinkFacetNamesRequestTypeDef",
    {
        "SchemaArn": str,
    },
)
_OptionalListTypedLinkFacetNamesRequestTypeDef = TypedDict(
    "_OptionalListTypedLinkFacetNamesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTypedLinkFacetNamesRequestTypeDef(
    _RequiredListTypedLinkFacetNamesRequestTypeDef, _OptionalListTypedLinkFacetNamesRequestTypeDef
):
    pass


ListTypedLinkFacetNamesResponseResponseTypeDef = TypedDict(
    "ListTypedLinkFacetNamesResponseResponseTypeDef",
    {
        "FacetNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLookupPolicyRequestTypeDef = TypedDict(
    "_RequiredLookupPolicyRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
    },
)
_OptionalLookupPolicyRequestTypeDef = TypedDict(
    "_OptionalLookupPolicyRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class LookupPolicyRequestTypeDef(
    _RequiredLookupPolicyRequestTypeDef, _OptionalLookupPolicyRequestTypeDef
):
    pass


LookupPolicyResponseResponseTypeDef = TypedDict(
    "LookupPolicyResponseResponseTypeDef",
    {
        "PolicyToPathList": List["PolicyToPathTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ObjectAttributeActionTypeDef = TypedDict(
    "ObjectAttributeActionTypeDef",
    {
        "ObjectAttributeActionType": UpdateActionTypeType,
        "ObjectAttributeUpdateValue": "TypedAttributeValueTypeDef",
    },
    total=False,
)

ObjectAttributeRangeTypeDef = TypedDict(
    "ObjectAttributeRangeTypeDef",
    {
        "AttributeKey": "AttributeKeyTypeDef",
        "Range": "TypedAttributeValueRangeTypeDef",
    },
    total=False,
)

ObjectAttributeUpdateTypeDef = TypedDict(
    "ObjectAttributeUpdateTypeDef",
    {
        "ObjectAttributeKey": "AttributeKeyTypeDef",
        "ObjectAttributeAction": "ObjectAttributeActionTypeDef",
    },
    total=False,
)

ObjectIdentifierAndLinkNameTupleTypeDef = TypedDict(
    "ObjectIdentifierAndLinkNameTupleTypeDef",
    {
        "ObjectIdentifier": str,
        "LinkName": str,
    },
    total=False,
)

ObjectReferenceTypeDef = TypedDict(
    "ObjectReferenceTypeDef",
    {
        "Selector": str,
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

PathToObjectIdentifiersTypeDef = TypedDict(
    "PathToObjectIdentifiersTypeDef",
    {
        "Path": str,
        "ObjectIdentifiers": List[str],
    },
    total=False,
)

PolicyAttachmentTypeDef = TypedDict(
    "PolicyAttachmentTypeDef",
    {
        "PolicyId": str,
        "ObjectIdentifier": str,
        "PolicyType": str,
    },
    total=False,
)

PolicyToPathTypeDef = TypedDict(
    "PolicyToPathTypeDef",
    {
        "Path": str,
        "Policies": List["PolicyAttachmentTypeDef"],
    },
    total=False,
)

_RequiredPublishSchemaRequestTypeDef = TypedDict(
    "_RequiredPublishSchemaRequestTypeDef",
    {
        "DevelopmentSchemaArn": str,
        "Version": str,
    },
)
_OptionalPublishSchemaRequestTypeDef = TypedDict(
    "_OptionalPublishSchemaRequestTypeDef",
    {
        "MinorVersion": str,
        "Name": str,
    },
    total=False,
)


class PublishSchemaRequestTypeDef(
    _RequiredPublishSchemaRequestTypeDef, _OptionalPublishSchemaRequestTypeDef
):
    pass


PublishSchemaResponseResponseTypeDef = TypedDict(
    "PublishSchemaResponseResponseTypeDef",
    {
        "PublishedSchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutSchemaFromJsonRequestTypeDef = TypedDict(
    "PutSchemaFromJsonRequestTypeDef",
    {
        "SchemaArn": str,
        "Document": str,
    },
)

PutSchemaFromJsonResponseResponseTypeDef = TypedDict(
    "PutSchemaFromJsonResponseResponseTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFacetFromObjectRequestTypeDef = TypedDict(
    "RemoveFacetFromObjectRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacet": "SchemaFacetTypeDef",
        "ObjectReference": "ObjectReferenceTypeDef",
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

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Type": RuleTypeType,
        "Parameters": Dict[str, str],
    },
    total=False,
)

SchemaFacetTypeDef = TypedDict(
    "SchemaFacetTypeDef",
    {
        "SchemaArn": str,
        "FacetName": str,
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
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

_RequiredTypedAttributeValueRangeTypeDef = TypedDict(
    "_RequiredTypedAttributeValueRangeTypeDef",
    {
        "StartMode": RangeModeType,
        "EndMode": RangeModeType,
    },
)
_OptionalTypedAttributeValueRangeTypeDef = TypedDict(
    "_OptionalTypedAttributeValueRangeTypeDef",
    {
        "StartValue": "TypedAttributeValueTypeDef",
        "EndValue": "TypedAttributeValueTypeDef",
    },
    total=False,
)


class TypedAttributeValueRangeTypeDef(
    _RequiredTypedAttributeValueRangeTypeDef, _OptionalTypedAttributeValueRangeTypeDef
):
    pass


TypedAttributeValueTypeDef = TypedDict(
    "TypedAttributeValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": Union[bytes, IO[bytes], StreamingBody],
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": Union[datetime, str],
    },
    total=False,
)

_RequiredTypedLinkAttributeDefinitionTypeDef = TypedDict(
    "_RequiredTypedLinkAttributeDefinitionTypeDef",
    {
        "Name": str,
        "Type": FacetAttributeTypeType,
        "RequiredBehavior": RequiredAttributeBehaviorType,
    },
)
_OptionalTypedLinkAttributeDefinitionTypeDef = TypedDict(
    "_OptionalTypedLinkAttributeDefinitionTypeDef",
    {
        "DefaultValue": "TypedAttributeValueTypeDef",
        "IsImmutable": bool,
        "Rules": Dict[str, "RuleTypeDef"],
    },
    total=False,
)


class TypedLinkAttributeDefinitionTypeDef(
    _RequiredTypedLinkAttributeDefinitionTypeDef, _OptionalTypedLinkAttributeDefinitionTypeDef
):
    pass


_RequiredTypedLinkAttributeRangeTypeDef = TypedDict(
    "_RequiredTypedLinkAttributeRangeTypeDef",
    {
        "Range": "TypedAttributeValueRangeTypeDef",
    },
)
_OptionalTypedLinkAttributeRangeTypeDef = TypedDict(
    "_OptionalTypedLinkAttributeRangeTypeDef",
    {
        "AttributeName": str,
    },
    total=False,
)


class TypedLinkAttributeRangeTypeDef(
    _RequiredTypedLinkAttributeRangeTypeDef, _OptionalTypedLinkAttributeRangeTypeDef
):
    pass


TypedLinkFacetAttributeUpdateTypeDef = TypedDict(
    "TypedLinkFacetAttributeUpdateTypeDef",
    {
        "Attribute": "TypedLinkAttributeDefinitionTypeDef",
        "Action": UpdateActionTypeType,
    },
)

TypedLinkFacetTypeDef = TypedDict(
    "TypedLinkFacetTypeDef",
    {
        "Name": str,
        "Attributes": List["TypedLinkAttributeDefinitionTypeDef"],
        "IdentityAttributeOrder": List[str],
    },
)

TypedLinkSchemaAndFacetNameTypeDef = TypedDict(
    "TypedLinkSchemaAndFacetNameTypeDef",
    {
        "SchemaArn": str,
        "TypedLinkName": str,
    },
)

TypedLinkSpecifierTypeDef = TypedDict(
    "TypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": "TypedLinkSchemaAndFacetNameTypeDef",
        "SourceObjectReference": "ObjectReferenceTypeDef",
        "TargetObjectReference": "ObjectReferenceTypeDef",
        "IdentityAttributeValues": List["AttributeNameAndValueTypeDef"],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateFacetRequestTypeDef = TypedDict(
    "_RequiredUpdateFacetRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
_OptionalUpdateFacetRequestTypeDef = TypedDict(
    "_OptionalUpdateFacetRequestTypeDef",
    {
        "AttributeUpdates": List["FacetAttributeUpdateTypeDef"],
        "ObjectType": ObjectTypeType,
    },
    total=False,
)


class UpdateFacetRequestTypeDef(
    _RequiredUpdateFacetRequestTypeDef, _OptionalUpdateFacetRequestTypeDef
):
    pass


UpdateLinkAttributesRequestTypeDef = TypedDict(
    "UpdateLinkAttributesRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": "TypedLinkSpecifierTypeDef",
        "AttributeUpdates": List["LinkAttributeUpdateTypeDef"],
    },
)

UpdateObjectAttributesRequestTypeDef = TypedDict(
    "UpdateObjectAttributesRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": "ObjectReferenceTypeDef",
        "AttributeUpdates": List["ObjectAttributeUpdateTypeDef"],
    },
)

UpdateObjectAttributesResponseResponseTypeDef = TypedDict(
    "UpdateObjectAttributesResponseResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSchemaRequestTypeDef = TypedDict(
    "UpdateSchemaRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

UpdateSchemaResponseResponseTypeDef = TypedDict(
    "UpdateSchemaResponseResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTypedLinkFacetRequestTypeDef = TypedDict(
    "UpdateTypedLinkFacetRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "AttributeUpdates": List["TypedLinkFacetAttributeUpdateTypeDef"],
        "IdentityAttributeOrder": List[str],
    },
)

_RequiredUpgradeAppliedSchemaRequestTypeDef = TypedDict(
    "_RequiredUpgradeAppliedSchemaRequestTypeDef",
    {
        "PublishedSchemaArn": str,
        "DirectoryArn": str,
    },
)
_OptionalUpgradeAppliedSchemaRequestTypeDef = TypedDict(
    "_OptionalUpgradeAppliedSchemaRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class UpgradeAppliedSchemaRequestTypeDef(
    _RequiredUpgradeAppliedSchemaRequestTypeDef, _OptionalUpgradeAppliedSchemaRequestTypeDef
):
    pass


UpgradeAppliedSchemaResponseResponseTypeDef = TypedDict(
    "UpgradeAppliedSchemaResponseResponseTypeDef",
    {
        "UpgradedSchemaArn": str,
        "DirectoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpgradePublishedSchemaRequestTypeDef = TypedDict(
    "_RequiredUpgradePublishedSchemaRequestTypeDef",
    {
        "DevelopmentSchemaArn": str,
        "PublishedSchemaArn": str,
        "MinorVersion": str,
    },
)
_OptionalUpgradePublishedSchemaRequestTypeDef = TypedDict(
    "_OptionalUpgradePublishedSchemaRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class UpgradePublishedSchemaRequestTypeDef(
    _RequiredUpgradePublishedSchemaRequestTypeDef, _OptionalUpgradePublishedSchemaRequestTypeDef
):
    pass


UpgradePublishedSchemaResponseResponseTypeDef = TypedDict(
    "UpgradePublishedSchemaResponseResponseTypeDef",
    {
        "UpgradedSchemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
