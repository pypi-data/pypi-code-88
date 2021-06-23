"""
Type annotations for dlm service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_dlm import DLMClient

    client: DLMClient = boto3.client("dlm")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .literals import (
    GettablePolicyStateValuesType,
    ResourceTypeValuesType,
    SettablePolicyStateValuesType,
)
from .type_defs import (
    CreateLifecyclePolicyResponseTypeDef,
    GetLifecyclePoliciesResponseTypeDef,
    GetLifecyclePolicyResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PolicyDetailsTypeDef,
)

__all__ = ("DLMClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class DLMClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dlm.html#DLM.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dlm.html#DLM.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/client.html#can_paginate)
        """

    def create_lifecycle_policy(
        self,
        *,
        ExecutionRoleArn: str,
        Description: str,
        State: SettablePolicyStateValuesType,
        PolicyDetails: "PolicyDetailsTypeDef",
        Tags: Dict[str, str] = None
    ) -> CreateLifecyclePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dlm.html#DLM.Client.create_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/client.html#create_lifecycle_policy)
        """

    def delete_lifecycle_policy(self, *, PolicyId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dlm.html#DLM.Client.delete_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/client.html#delete_lifecycle_policy)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dlm.html#DLM.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/client.html#generate_presigned_url)
        """

    def get_lifecycle_policies(
        self,
        *,
        PolicyIds: List[str] = None,
        State: GettablePolicyStateValuesType = None,
        ResourceTypes: List[ResourceTypeValuesType] = None,
        TargetTags: List[str] = None,
        TagsToAdd: List[str] = None
    ) -> GetLifecyclePoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dlm.html#DLM.Client.get_lifecycle_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/client.html#get_lifecycle_policies)
        """

    def get_lifecycle_policy(self, *, PolicyId: str) -> GetLifecyclePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dlm.html#DLM.Client.get_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/client.html#get_lifecycle_policy)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dlm.html#DLM.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/client.html#list_tags_for_resource)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dlm.html#DLM.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dlm.html#DLM.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/client.html#untag_resource)
        """

    def update_lifecycle_policy(
        self,
        *,
        PolicyId: str,
        ExecutionRoleArn: str = None,
        State: SettablePolicyStateValuesType = None,
        Description: str = None,
        PolicyDetails: "PolicyDetailsTypeDef" = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dlm.html#DLM.Client.update_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/client.html#update_lifecycle_policy)
        """
