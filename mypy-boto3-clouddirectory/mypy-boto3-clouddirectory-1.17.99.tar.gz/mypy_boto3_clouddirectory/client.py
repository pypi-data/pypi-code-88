"""
Type annotations for clouddirectory service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_clouddirectory import CloudDirectoryClient

    client: CloudDirectoryClient = boto3.client("clouddirectory")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import ConsistencyLevelType, DirectoryStateType, FacetStyleType, ObjectTypeType
from .paginator import (
    ListAppliedSchemaArnsPaginator,
    ListAttachedIndicesPaginator,
    ListDevelopmentSchemaArnsPaginator,
    ListDirectoriesPaginator,
    ListFacetAttributesPaginator,
    ListFacetNamesPaginator,
    ListIncomingTypedLinksPaginator,
    ListIndexPaginator,
    ListManagedSchemaArnsPaginator,
    ListObjectAttributesPaginator,
    ListObjectParentPathsPaginator,
    ListObjectPoliciesPaginator,
    ListOutgoingTypedLinksPaginator,
    ListPolicyAttachmentsPaginator,
    ListPublishedSchemaArnsPaginator,
    ListTagsForResourcePaginator,
    ListTypedLinkFacetAttributesPaginator,
    ListTypedLinkFacetNamesPaginator,
    LookupPolicyPaginator,
)
from .type_defs import (
    ApplySchemaResponseTypeDef,
    AttachObjectResponseTypeDef,
    AttachToIndexResponseTypeDef,
    AttachTypedLinkResponseTypeDef,
    AttributeKeyAndValueTypeDef,
    AttributeKeyTypeDef,
    AttributeNameAndValueTypeDef,
    BatchReadOperationTypeDef,
    BatchReadResponseTypeDef,
    BatchWriteOperationTypeDef,
    BatchWriteResponseTypeDef,
    CreateDirectoryResponseTypeDef,
    CreateIndexResponseTypeDef,
    CreateObjectResponseTypeDef,
    CreateSchemaResponseTypeDef,
    DeleteDirectoryResponseTypeDef,
    DeleteSchemaResponseTypeDef,
    DetachFromIndexResponseTypeDef,
    DetachObjectResponseTypeDef,
    DisableDirectoryResponseTypeDef,
    EnableDirectoryResponseTypeDef,
    FacetAttributeTypeDef,
    FacetAttributeUpdateTypeDef,
    GetAppliedSchemaVersionResponseTypeDef,
    GetDirectoryResponseTypeDef,
    GetFacetResponseTypeDef,
    GetLinkAttributesResponseTypeDef,
    GetObjectAttributesResponseTypeDef,
    GetObjectInformationResponseTypeDef,
    GetSchemaAsJsonResponseTypeDef,
    GetTypedLinkFacetInformationResponseTypeDef,
    LinkAttributeUpdateTypeDef,
    ListAppliedSchemaArnsResponseTypeDef,
    ListAttachedIndicesResponseTypeDef,
    ListDevelopmentSchemaArnsResponseTypeDef,
    ListDirectoriesResponseTypeDef,
    ListFacetAttributesResponseTypeDef,
    ListFacetNamesResponseTypeDef,
    ListIncomingTypedLinksResponseTypeDef,
    ListIndexResponseTypeDef,
    ListManagedSchemaArnsResponseTypeDef,
    ListObjectAttributesResponseTypeDef,
    ListObjectChildrenResponseTypeDef,
    ListObjectParentPathsResponseTypeDef,
    ListObjectParentsResponseTypeDef,
    ListObjectPoliciesResponseTypeDef,
    ListOutgoingTypedLinksResponseTypeDef,
    ListPolicyAttachmentsResponseTypeDef,
    ListPublishedSchemaArnsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTypedLinkFacetAttributesResponseTypeDef,
    ListTypedLinkFacetNamesResponseTypeDef,
    LookupPolicyResponseTypeDef,
    ObjectAttributeRangeTypeDef,
    ObjectAttributeUpdateTypeDef,
    ObjectReferenceTypeDef,
    PublishSchemaResponseTypeDef,
    PutSchemaFromJsonResponseTypeDef,
    SchemaFacetTypeDef,
    TagTypeDef,
    TypedLinkAttributeRangeTypeDef,
    TypedLinkFacetAttributeUpdateTypeDef,
    TypedLinkFacetTypeDef,
    TypedLinkSchemaAndFacetNameTypeDef,
    TypedLinkSpecifierTypeDef,
    UpdateObjectAttributesResponseTypeDef,
    UpdateSchemaResponseTypeDef,
    UpgradeAppliedSchemaResponseTypeDef,
    UpgradePublishedSchemaResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudDirectoryClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BatchWriteException: Type[BotocoreClientError]
    CannotListParentOfRootException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DirectoryAlreadyExistsException: Type[BotocoreClientError]
    DirectoryDeletedException: Type[BotocoreClientError]
    DirectoryNotDisabledException: Type[BotocoreClientError]
    DirectoryNotEnabledException: Type[BotocoreClientError]
    FacetAlreadyExistsException: Type[BotocoreClientError]
    FacetInUseException: Type[BotocoreClientError]
    FacetNotFoundException: Type[BotocoreClientError]
    FacetValidationException: Type[BotocoreClientError]
    IncompatibleSchemaException: Type[BotocoreClientError]
    IndexedAttributeMissingException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidArnException: Type[BotocoreClientError]
    InvalidAttachmentException: Type[BotocoreClientError]
    InvalidFacetUpdateException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidRuleException: Type[BotocoreClientError]
    InvalidSchemaDocException: Type[BotocoreClientError]
    InvalidTaggingRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    LinkNameAlreadyInUseException: Type[BotocoreClientError]
    NotIndexException: Type[BotocoreClientError]
    NotNodeException: Type[BotocoreClientError]
    NotPolicyException: Type[BotocoreClientError]
    ObjectAlreadyDetachedException: Type[BotocoreClientError]
    ObjectNotDetachedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    RetryableConflictException: Type[BotocoreClientError]
    SchemaAlreadyExistsException: Type[BotocoreClientError]
    SchemaAlreadyPublishedException: Type[BotocoreClientError]
    StillContainsLinksException: Type[BotocoreClientError]
    UnsupportedIndexTypeException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class CloudDirectoryClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_facet_to_object(
        self,
        *,
        DirectoryArn: str,
        SchemaFacet: "SchemaFacetTypeDef",
        ObjectReference: "ObjectReferenceTypeDef",
        ObjectAttributeList: List["AttributeKeyAndValueTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.add_facet_to_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#add_facet_to_object)
        """

    def apply_schema(
        self, *, PublishedSchemaArn: str, DirectoryArn: str
    ) -> ApplySchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.apply_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#apply_schema)
        """

    def attach_object(
        self,
        *,
        DirectoryArn: str,
        ParentReference: "ObjectReferenceTypeDef",
        ChildReference: "ObjectReferenceTypeDef",
        LinkName: str
    ) -> AttachObjectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.attach_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#attach_object)
        """

    def attach_policy(
        self,
        *,
        DirectoryArn: str,
        PolicyReference: "ObjectReferenceTypeDef",
        ObjectReference: "ObjectReferenceTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.attach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#attach_policy)
        """

    def attach_to_index(
        self,
        *,
        DirectoryArn: str,
        IndexReference: "ObjectReferenceTypeDef",
        TargetReference: "ObjectReferenceTypeDef"
    ) -> AttachToIndexResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.attach_to_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#attach_to_index)
        """

    def attach_typed_link(
        self,
        *,
        DirectoryArn: str,
        SourceObjectReference: "ObjectReferenceTypeDef",
        TargetObjectReference: "ObjectReferenceTypeDef",
        TypedLinkFacet: "TypedLinkSchemaAndFacetNameTypeDef",
        Attributes: List["AttributeNameAndValueTypeDef"]
    ) -> AttachTypedLinkResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.attach_typed_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#attach_typed_link)
        """

    def batch_read(
        self,
        *,
        DirectoryArn: str,
        Operations: List[BatchReadOperationTypeDef],
        ConsistencyLevel: ConsistencyLevelType = None
    ) -> BatchReadResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.batch_read)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#batch_read)
        """

    def batch_write(
        self, *, DirectoryArn: str, Operations: List[BatchWriteOperationTypeDef]
    ) -> BatchWriteResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.batch_write)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#batch_write)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#can_paginate)
        """

    def create_directory(self, *, Name: str, SchemaArn: str) -> CreateDirectoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.create_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#create_directory)
        """

    def create_facet(
        self,
        *,
        SchemaArn: str,
        Name: str,
        Attributes: List["FacetAttributeTypeDef"] = None,
        ObjectType: ObjectTypeType = None,
        FacetStyle: FacetStyleType = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.create_facet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#create_facet)
        """

    def create_index(
        self,
        *,
        DirectoryArn: str,
        OrderedIndexedAttributeList: List["AttributeKeyTypeDef"],
        IsUnique: bool,
        ParentReference: "ObjectReferenceTypeDef" = None,
        LinkName: str = None
    ) -> CreateIndexResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.create_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#create_index)
        """

    def create_object(
        self,
        *,
        DirectoryArn: str,
        SchemaFacets: List["SchemaFacetTypeDef"],
        ObjectAttributeList: List["AttributeKeyAndValueTypeDef"] = None,
        ParentReference: "ObjectReferenceTypeDef" = None,
        LinkName: str = None
    ) -> CreateObjectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.create_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#create_object)
        """

    def create_schema(self, *, Name: str) -> CreateSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.create_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#create_schema)
        """

    def create_typed_link_facet(
        self, *, SchemaArn: str, Facet: TypedLinkFacetTypeDef
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.create_typed_link_facet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#create_typed_link_facet)
        """

    def delete_directory(self, *, DirectoryArn: str) -> DeleteDirectoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.delete_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#delete_directory)
        """

    def delete_facet(self, *, SchemaArn: str, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.delete_facet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#delete_facet)
        """

    def delete_object(
        self, *, DirectoryArn: str, ObjectReference: "ObjectReferenceTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.delete_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#delete_object)
        """

    def delete_schema(self, *, SchemaArn: str) -> DeleteSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.delete_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#delete_schema)
        """

    def delete_typed_link_facet(self, *, SchemaArn: str, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.delete_typed_link_facet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#delete_typed_link_facet)
        """

    def detach_from_index(
        self,
        *,
        DirectoryArn: str,
        IndexReference: "ObjectReferenceTypeDef",
        TargetReference: "ObjectReferenceTypeDef"
    ) -> DetachFromIndexResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.detach_from_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#detach_from_index)
        """

    def detach_object(
        self, *, DirectoryArn: str, ParentReference: "ObjectReferenceTypeDef", LinkName: str
    ) -> DetachObjectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.detach_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#detach_object)
        """

    def detach_policy(
        self,
        *,
        DirectoryArn: str,
        PolicyReference: "ObjectReferenceTypeDef",
        ObjectReference: "ObjectReferenceTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.detach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#detach_policy)
        """

    def detach_typed_link(
        self, *, DirectoryArn: str, TypedLinkSpecifier: "TypedLinkSpecifierTypeDef"
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.detach_typed_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#detach_typed_link)
        """

    def disable_directory(self, *, DirectoryArn: str) -> DisableDirectoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.disable_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#disable_directory)
        """

    def enable_directory(self, *, DirectoryArn: str) -> EnableDirectoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.enable_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#enable_directory)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#generate_presigned_url)
        """

    def get_applied_schema_version(
        self, *, SchemaArn: str
    ) -> GetAppliedSchemaVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.get_applied_schema_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#get_applied_schema_version)
        """

    def get_directory(self, *, DirectoryArn: str) -> GetDirectoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.get_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#get_directory)
        """

    def get_facet(self, *, SchemaArn: str, Name: str) -> GetFacetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.get_facet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#get_facet)
        """

    def get_link_attributes(
        self,
        *,
        DirectoryArn: str,
        TypedLinkSpecifier: "TypedLinkSpecifierTypeDef",
        AttributeNames: List[str],
        ConsistencyLevel: ConsistencyLevelType = None
    ) -> GetLinkAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.get_link_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#get_link_attributes)
        """

    def get_object_attributes(
        self,
        *,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        SchemaFacet: "SchemaFacetTypeDef",
        AttributeNames: List[str],
        ConsistencyLevel: ConsistencyLevelType = None
    ) -> GetObjectAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.get_object_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#get_object_attributes)
        """

    def get_object_information(
        self,
        *,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        ConsistencyLevel: ConsistencyLevelType = None
    ) -> GetObjectInformationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.get_object_information)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#get_object_information)
        """

    def get_schema_as_json(self, *, SchemaArn: str) -> GetSchemaAsJsonResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.get_schema_as_json)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#get_schema_as_json)
        """

    def get_typed_link_facet_information(
        self, *, SchemaArn: str, Name: str
    ) -> GetTypedLinkFacetInformationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.get_typed_link_facet_information)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#get_typed_link_facet_information)
        """

    def list_applied_schema_arns(
        self,
        *,
        DirectoryArn: str,
        SchemaArn: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListAppliedSchemaArnsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_applied_schema_arns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_applied_schema_arns)
        """

    def list_attached_indices(
        self,
        *,
        DirectoryArn: str,
        TargetReference: "ObjectReferenceTypeDef",
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: ConsistencyLevelType = None
    ) -> ListAttachedIndicesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_attached_indices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_attached_indices)
        """

    def list_development_schema_arns(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListDevelopmentSchemaArnsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_development_schema_arns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_development_schema_arns)
        """

    def list_directories(
        self, *, NextToken: str = None, MaxResults: int = None, state: DirectoryStateType = None
    ) -> ListDirectoriesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_directories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_directories)
        """

    def list_facet_attributes(
        self, *, SchemaArn: str, Name: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFacetAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_facet_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_facet_attributes)
        """

    def list_facet_names(
        self, *, SchemaArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFacetNamesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_facet_names)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_facet_names)
        """

    def list_incoming_typed_links(
        self,
        *,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        FilterAttributeRanges: List["TypedLinkAttributeRangeTypeDef"] = None,
        FilterTypedLink: "TypedLinkSchemaAndFacetNameTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: ConsistencyLevelType = None
    ) -> ListIncomingTypedLinksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_incoming_typed_links)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_incoming_typed_links)
        """

    def list_index(
        self,
        *,
        DirectoryArn: str,
        IndexReference: "ObjectReferenceTypeDef",
        RangesOnIndexedValues: List["ObjectAttributeRangeTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        ConsistencyLevel: ConsistencyLevelType = None
    ) -> ListIndexResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_index)
        """

    def list_managed_schema_arns(
        self, *, SchemaArn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListManagedSchemaArnsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_managed_schema_arns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_managed_schema_arns)
        """

    def list_object_attributes(
        self,
        *,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: ConsistencyLevelType = None,
        FacetFilter: "SchemaFacetTypeDef" = None
    ) -> ListObjectAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_object_attributes)
        """

    def list_object_children(
        self,
        *,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: ConsistencyLevelType = None
    ) -> ListObjectChildrenResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_children)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_object_children)
        """

    def list_object_parent_paths(
        self,
        *,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListObjectParentPathsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_parent_paths)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_object_parent_paths)
        """

    def list_object_parents(
        self,
        *,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: ConsistencyLevelType = None,
        IncludeAllLinksToEachParent: bool = None
    ) -> ListObjectParentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_parents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_object_parents)
        """

    def list_object_policies(
        self,
        *,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: ConsistencyLevelType = None
    ) -> ListObjectPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_object_policies)
        """

    def list_outgoing_typed_links(
        self,
        *,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        FilterAttributeRanges: List["TypedLinkAttributeRangeTypeDef"] = None,
        FilterTypedLink: "TypedLinkSchemaAndFacetNameTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: ConsistencyLevelType = None
    ) -> ListOutgoingTypedLinksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_outgoing_typed_links)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_outgoing_typed_links)
        """

    def list_policy_attachments(
        self,
        *,
        DirectoryArn: str,
        PolicyReference: "ObjectReferenceTypeDef",
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: ConsistencyLevelType = None
    ) -> ListPolicyAttachmentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_policy_attachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_policy_attachments)
        """

    def list_published_schema_arns(
        self, *, SchemaArn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListPublishedSchemaArnsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_published_schema_arns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_published_schema_arns)
        """

    def list_tags_for_resource(
        self, *, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_tags_for_resource)
        """

    def list_typed_link_facet_attributes(
        self, *, SchemaArn: str, Name: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTypedLinkFacetAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_typed_link_facet_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_typed_link_facet_attributes)
        """

    def list_typed_link_facet_names(
        self, *, SchemaArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTypedLinkFacetNamesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.list_typed_link_facet_names)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#list_typed_link_facet_names)
        """

    def lookup_policy(
        self,
        *,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        NextToken: str = None,
        MaxResults: int = None
    ) -> LookupPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.lookup_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#lookup_policy)
        """

    def publish_schema(
        self, *, DevelopmentSchemaArn: str, Version: str, MinorVersion: str = None, Name: str = None
    ) -> PublishSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.publish_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#publish_schema)
        """

    def put_schema_from_json(
        self, *, SchemaArn: str, Document: str
    ) -> PutSchemaFromJsonResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.put_schema_from_json)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#put_schema_from_json)
        """

    def remove_facet_from_object(
        self,
        *,
        DirectoryArn: str,
        SchemaFacet: "SchemaFacetTypeDef",
        ObjectReference: "ObjectReferenceTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.remove_facet_from_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#remove_facet_from_object)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#untag_resource)
        """

    def update_facet(
        self,
        *,
        SchemaArn: str,
        Name: str,
        AttributeUpdates: List[FacetAttributeUpdateTypeDef] = None,
        ObjectType: ObjectTypeType = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.update_facet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#update_facet)
        """

    def update_link_attributes(
        self,
        *,
        DirectoryArn: str,
        TypedLinkSpecifier: "TypedLinkSpecifierTypeDef",
        AttributeUpdates: List["LinkAttributeUpdateTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.update_link_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#update_link_attributes)
        """

    def update_object_attributes(
        self,
        *,
        DirectoryArn: str,
        ObjectReference: "ObjectReferenceTypeDef",
        AttributeUpdates: List["ObjectAttributeUpdateTypeDef"]
    ) -> UpdateObjectAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.update_object_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#update_object_attributes)
        """

    def update_schema(self, *, SchemaArn: str, Name: str) -> UpdateSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.update_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#update_schema)
        """

    def update_typed_link_facet(
        self,
        *,
        SchemaArn: str,
        Name: str,
        AttributeUpdates: List[TypedLinkFacetAttributeUpdateTypeDef],
        IdentityAttributeOrder: List[str]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.update_typed_link_facet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#update_typed_link_facet)
        """

    def upgrade_applied_schema(
        self, *, PublishedSchemaArn: str, DirectoryArn: str, DryRun: bool = None
    ) -> UpgradeAppliedSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.upgrade_applied_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#upgrade_applied_schema)
        """

    def upgrade_published_schema(
        self,
        *,
        DevelopmentSchemaArn: str,
        PublishedSchemaArn: str,
        MinorVersion: str,
        DryRun: bool = None
    ) -> UpgradePublishedSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Client.upgrade_published_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/client.html#upgrade_published_schema)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applied_schema_arns"]
    ) -> ListAppliedSchemaArnsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAppliedSchemaArns)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listappliedschemaarnspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_indices"]
    ) -> ListAttachedIndicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAttachedIndices)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listattachedindicespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_development_schema_arns"]
    ) -> ListDevelopmentSchemaArnsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDevelopmentSchemaArns)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listdevelopmentschemaarnspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_directories"]
    ) -> ListDirectoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDirectories)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listdirectoriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_facet_attributes"]
    ) -> ListFacetAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetAttributes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listfacetattributespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_facet_names"]) -> ListFacetNamesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetNames)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listfacetnamespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_incoming_typed_links"]
    ) -> ListIncomingTypedLinksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIncomingTypedLinks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listincomingtypedlinkspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_index"]) -> ListIndexPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIndex)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listindexpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_managed_schema_arns"]
    ) -> ListManagedSchemaArnsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListManagedSchemaArns)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listmanagedschemaarnspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_object_attributes"]
    ) -> ListObjectAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectAttributes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listobjectattributespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_object_parent_paths"]
    ) -> ListObjectParentPathsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectParentPaths)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listobjectparentpathspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_object_policies"]
    ) -> ListObjectPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectPolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listobjectpoliciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_outgoing_typed_links"]
    ) -> ListOutgoingTypedLinksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListOutgoingTypedLinks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listoutgoingtypedlinkspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policy_attachments"]
    ) -> ListPolicyAttachmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPolicyAttachments)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listpolicyattachmentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_published_schema_arns"]
    ) -> ListPublishedSchemaArnsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPublishedSchemaArns)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listpublishedschemaarnspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTagsForResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listtagsforresourcepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_typed_link_facet_attributes"]
    ) -> ListTypedLinkFacetAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetAttributes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listtypedlinkfacetattributespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_typed_link_facet_names"]
    ) -> ListTypedLinkFacetNamesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetNames)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#listtypedlinkfacetnamespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["lookup_policy"]) -> LookupPolicyPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/clouddirectory.html#CloudDirectory.Paginator.LookupPolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/paginators.html#lookuppolicypaginator)
        """
