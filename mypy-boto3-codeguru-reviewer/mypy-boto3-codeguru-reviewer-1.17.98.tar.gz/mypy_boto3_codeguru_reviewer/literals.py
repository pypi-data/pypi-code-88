"""
Type annotations for codeguru-reviewer service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/literals.html)

Usage::

    ```python
    from mypy_boto3_codeguru_reviewer.literals import EncryptionOptionType

    data: EncryptionOptionType = "AWS_OWNED_CMK"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "EncryptionOptionType",
    "JobStateType",
    "ListRepositoryAssociationsPaginatorName",
    "ProviderTypeType",
    "ReactionType",
    "RepositoryAssociationStateType",
    "TypeType",
)


EncryptionOptionType = Literal["AWS_OWNED_CMK", "CUSTOMER_MANAGED_CMK"]
JobStateType = Literal["Completed", "Deleting", "Failed", "Pending"]
ListRepositoryAssociationsPaginatorName = Literal["list_repository_associations"]
ProviderTypeType = Literal["Bitbucket", "CodeCommit", "GitHub", "GitHubEnterpriseServer"]
ReactionType = Literal["ThumbsDown", "ThumbsUp"]
RepositoryAssociationStateType = Literal[
    "Associated", "Associating", "Disassociated", "Disassociating", "Failed"
]
TypeType = Literal["PullRequest", "RepositoryAnalysis"]
