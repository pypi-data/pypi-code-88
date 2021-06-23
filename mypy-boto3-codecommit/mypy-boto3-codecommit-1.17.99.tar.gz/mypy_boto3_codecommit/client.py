"""
Type annotations for codecommit service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_codecommit import CodeCommitClient

    client: CodeCommitClient = boto3.client("codecommit")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import ClientMeta
from botocore.response import StreamingBody

from .literals import (
    ApprovalStateType,
    ConflictDetailLevelTypeEnumType,
    ConflictResolutionStrategyTypeEnumType,
    FileModeTypeEnumType,
    MergeOptionTypeEnumType,
    OrderEnumType,
    OverrideStatusType,
    PullRequestEventTypeType,
    PullRequestStatusEnumType,
    SortByEnumType,
)
from .paginator import (
    DescribePullRequestEventsPaginator,
    GetCommentsForComparedCommitPaginator,
    GetCommentsForPullRequestPaginator,
    GetDifferencesPaginator,
    ListBranchesPaginator,
    ListPullRequestsPaginator,
    ListRepositoriesPaginator,
)
from .type_defs import (
    BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef,
    BatchDescribeMergeConflictsOutputTypeDef,
    BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef,
    BatchGetCommitsOutputTypeDef,
    BatchGetRepositoriesOutputTypeDef,
    ConflictResolutionTypeDef,
    CreateApprovalRuleTemplateOutputTypeDef,
    CreateCommitOutputTypeDef,
    CreatePullRequestApprovalRuleOutputTypeDef,
    CreatePullRequestOutputTypeDef,
    CreateRepositoryOutputTypeDef,
    CreateUnreferencedMergeCommitOutputTypeDef,
    DeleteApprovalRuleTemplateOutputTypeDef,
    DeleteBranchOutputTypeDef,
    DeleteCommentContentOutputTypeDef,
    DeleteFileEntryTypeDef,
    DeleteFileOutputTypeDef,
    DeletePullRequestApprovalRuleOutputTypeDef,
    DeleteRepositoryOutputTypeDef,
    DescribeMergeConflictsOutputTypeDef,
    DescribePullRequestEventsOutputTypeDef,
    EvaluatePullRequestApprovalRulesOutputTypeDef,
    GetApprovalRuleTemplateOutputTypeDef,
    GetBlobOutputTypeDef,
    GetBranchOutputTypeDef,
    GetCommentOutputTypeDef,
    GetCommentReactionsOutputTypeDef,
    GetCommentsForComparedCommitOutputTypeDef,
    GetCommentsForPullRequestOutputTypeDef,
    GetCommitOutputTypeDef,
    GetDifferencesOutputTypeDef,
    GetFileOutputTypeDef,
    GetFolderOutputTypeDef,
    GetMergeCommitOutputTypeDef,
    GetMergeConflictsOutputTypeDef,
    GetMergeOptionsOutputTypeDef,
    GetPullRequestApprovalStatesOutputTypeDef,
    GetPullRequestOutputTypeDef,
    GetPullRequestOverrideStateOutputTypeDef,
    GetRepositoryOutputTypeDef,
    GetRepositoryTriggersOutputTypeDef,
    ListApprovalRuleTemplatesOutputTypeDef,
    ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef,
    ListBranchesOutputTypeDef,
    ListPullRequestsOutputTypeDef,
    ListRepositoriesForApprovalRuleTemplateOutputTypeDef,
    ListRepositoriesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    LocationTypeDef,
    MergeBranchesByFastForwardOutputTypeDef,
    MergeBranchesBySquashOutputTypeDef,
    MergeBranchesByThreeWayOutputTypeDef,
    MergePullRequestByFastForwardOutputTypeDef,
    MergePullRequestBySquashOutputTypeDef,
    MergePullRequestByThreeWayOutputTypeDef,
    PostCommentForComparedCommitOutputTypeDef,
    PostCommentForPullRequestOutputTypeDef,
    PostCommentReplyOutputTypeDef,
    PutFileEntryTypeDef,
    PutFileOutputTypeDef,
    PutRepositoryTriggersOutputTypeDef,
    RepositoryTriggerTypeDef,
    SetFileModeEntryTypeDef,
    TargetTypeDef,
    TestRepositoryTriggersOutputTypeDef,
    UpdateApprovalRuleTemplateContentOutputTypeDef,
    UpdateApprovalRuleTemplateDescriptionOutputTypeDef,
    UpdateApprovalRuleTemplateNameOutputTypeDef,
    UpdateCommentOutputTypeDef,
    UpdatePullRequestApprovalRuleContentOutputTypeDef,
    UpdatePullRequestDescriptionOutputTypeDef,
    UpdatePullRequestStatusOutputTypeDef,
    UpdatePullRequestTitleOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeCommitClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ActorDoesNotExistException: Type[BotocoreClientError]
    ApprovalRuleContentRequiredException: Type[BotocoreClientError]
    ApprovalRuleDoesNotExistException: Type[BotocoreClientError]
    ApprovalRuleNameAlreadyExistsException: Type[BotocoreClientError]
    ApprovalRuleNameRequiredException: Type[BotocoreClientError]
    ApprovalRuleTemplateContentRequiredException: Type[BotocoreClientError]
    ApprovalRuleTemplateDoesNotExistException: Type[BotocoreClientError]
    ApprovalRuleTemplateInUseException: Type[BotocoreClientError]
    ApprovalRuleTemplateNameAlreadyExistsException: Type[BotocoreClientError]
    ApprovalRuleTemplateNameRequiredException: Type[BotocoreClientError]
    ApprovalStateRequiredException: Type[BotocoreClientError]
    AuthorDoesNotExistException: Type[BotocoreClientError]
    BeforeCommitIdAndAfterCommitIdAreSameException: Type[BotocoreClientError]
    BlobIdDoesNotExistException: Type[BotocoreClientError]
    BlobIdRequiredException: Type[BotocoreClientError]
    BranchDoesNotExistException: Type[BotocoreClientError]
    BranchNameExistsException: Type[BotocoreClientError]
    BranchNameIsTagNameException: Type[BotocoreClientError]
    BranchNameRequiredException: Type[BotocoreClientError]
    CannotDeleteApprovalRuleFromTemplateException: Type[BotocoreClientError]
    CannotModifyApprovalRuleFromTemplateException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientRequestTokenRequiredException: Type[BotocoreClientError]
    CommentContentRequiredException: Type[BotocoreClientError]
    CommentContentSizeLimitExceededException: Type[BotocoreClientError]
    CommentDeletedException: Type[BotocoreClientError]
    CommentDoesNotExistException: Type[BotocoreClientError]
    CommentIdRequiredException: Type[BotocoreClientError]
    CommentNotCreatedByCallerException: Type[BotocoreClientError]
    CommitDoesNotExistException: Type[BotocoreClientError]
    CommitIdDoesNotExistException: Type[BotocoreClientError]
    CommitIdRequiredException: Type[BotocoreClientError]
    CommitIdsLimitExceededException: Type[BotocoreClientError]
    CommitIdsListRequiredException: Type[BotocoreClientError]
    CommitMessageLengthExceededException: Type[BotocoreClientError]
    CommitRequiredException: Type[BotocoreClientError]
    ConcurrentReferenceUpdateException: Type[BotocoreClientError]
    DefaultBranchCannotBeDeletedException: Type[BotocoreClientError]
    DirectoryNameConflictsWithFileNameException: Type[BotocoreClientError]
    EncryptionIntegrityChecksFailedException: Type[BotocoreClientError]
    EncryptionKeyAccessDeniedException: Type[BotocoreClientError]
    EncryptionKeyDisabledException: Type[BotocoreClientError]
    EncryptionKeyNotFoundException: Type[BotocoreClientError]
    EncryptionKeyUnavailableException: Type[BotocoreClientError]
    FileContentAndSourceFileSpecifiedException: Type[BotocoreClientError]
    FileContentRequiredException: Type[BotocoreClientError]
    FileContentSizeLimitExceededException: Type[BotocoreClientError]
    FileDoesNotExistException: Type[BotocoreClientError]
    FileEntryRequiredException: Type[BotocoreClientError]
    FileModeRequiredException: Type[BotocoreClientError]
    FileNameConflictsWithDirectoryNameException: Type[BotocoreClientError]
    FilePathConflictsWithSubmodulePathException: Type[BotocoreClientError]
    FileTooLargeException: Type[BotocoreClientError]
    FolderContentSizeLimitExceededException: Type[BotocoreClientError]
    FolderDoesNotExistException: Type[BotocoreClientError]
    IdempotencyParameterMismatchException: Type[BotocoreClientError]
    InvalidActorArnException: Type[BotocoreClientError]
    InvalidApprovalRuleContentException: Type[BotocoreClientError]
    InvalidApprovalRuleNameException: Type[BotocoreClientError]
    InvalidApprovalRuleTemplateContentException: Type[BotocoreClientError]
    InvalidApprovalRuleTemplateDescriptionException: Type[BotocoreClientError]
    InvalidApprovalRuleTemplateNameException: Type[BotocoreClientError]
    InvalidApprovalStateException: Type[BotocoreClientError]
    InvalidAuthorArnException: Type[BotocoreClientError]
    InvalidBlobIdException: Type[BotocoreClientError]
    InvalidBranchNameException: Type[BotocoreClientError]
    InvalidClientRequestTokenException: Type[BotocoreClientError]
    InvalidCommentIdException: Type[BotocoreClientError]
    InvalidCommitException: Type[BotocoreClientError]
    InvalidCommitIdException: Type[BotocoreClientError]
    InvalidConflictDetailLevelException: Type[BotocoreClientError]
    InvalidConflictResolutionException: Type[BotocoreClientError]
    InvalidConflictResolutionStrategyException: Type[BotocoreClientError]
    InvalidContinuationTokenException: Type[BotocoreClientError]
    InvalidDeletionParameterException: Type[BotocoreClientError]
    InvalidDescriptionException: Type[BotocoreClientError]
    InvalidDestinationCommitSpecifierException: Type[BotocoreClientError]
    InvalidEmailException: Type[BotocoreClientError]
    InvalidFileLocationException: Type[BotocoreClientError]
    InvalidFileModeException: Type[BotocoreClientError]
    InvalidFilePositionException: Type[BotocoreClientError]
    InvalidMaxConflictFilesException: Type[BotocoreClientError]
    InvalidMaxMergeHunksException: Type[BotocoreClientError]
    InvalidMaxResultsException: Type[BotocoreClientError]
    InvalidMergeOptionException: Type[BotocoreClientError]
    InvalidOrderException: Type[BotocoreClientError]
    InvalidOverrideStatusException: Type[BotocoreClientError]
    InvalidParentCommitIdException: Type[BotocoreClientError]
    InvalidPathException: Type[BotocoreClientError]
    InvalidPullRequestEventTypeException: Type[BotocoreClientError]
    InvalidPullRequestIdException: Type[BotocoreClientError]
    InvalidPullRequestStatusException: Type[BotocoreClientError]
    InvalidPullRequestStatusUpdateException: Type[BotocoreClientError]
    InvalidReactionUserArnException: Type[BotocoreClientError]
    InvalidReactionValueException: Type[BotocoreClientError]
    InvalidReferenceNameException: Type[BotocoreClientError]
    InvalidRelativeFileVersionEnumException: Type[BotocoreClientError]
    InvalidReplacementContentException: Type[BotocoreClientError]
    InvalidReplacementTypeException: Type[BotocoreClientError]
    InvalidRepositoryDescriptionException: Type[BotocoreClientError]
    InvalidRepositoryNameException: Type[BotocoreClientError]
    InvalidRepositoryTriggerBranchNameException: Type[BotocoreClientError]
    InvalidRepositoryTriggerCustomDataException: Type[BotocoreClientError]
    InvalidRepositoryTriggerDestinationArnException: Type[BotocoreClientError]
    InvalidRepositoryTriggerEventsException: Type[BotocoreClientError]
    InvalidRepositoryTriggerNameException: Type[BotocoreClientError]
    InvalidRepositoryTriggerRegionException: Type[BotocoreClientError]
    InvalidResourceArnException: Type[BotocoreClientError]
    InvalidRevisionIdException: Type[BotocoreClientError]
    InvalidRuleContentSha256Exception: Type[BotocoreClientError]
    InvalidSortByException: Type[BotocoreClientError]
    InvalidSourceCommitSpecifierException: Type[BotocoreClientError]
    InvalidSystemTagUsageException: Type[BotocoreClientError]
    InvalidTagKeysListException: Type[BotocoreClientError]
    InvalidTagsMapException: Type[BotocoreClientError]
    InvalidTargetBranchException: Type[BotocoreClientError]
    InvalidTargetException: Type[BotocoreClientError]
    InvalidTargetsException: Type[BotocoreClientError]
    InvalidTitleException: Type[BotocoreClientError]
    ManualMergeRequiredException: Type[BotocoreClientError]
    MaximumBranchesExceededException: Type[BotocoreClientError]
    MaximumConflictResolutionEntriesExceededException: Type[BotocoreClientError]
    MaximumFileContentToLoadExceededException: Type[BotocoreClientError]
    MaximumFileEntriesExceededException: Type[BotocoreClientError]
    MaximumItemsToCompareExceededException: Type[BotocoreClientError]
    MaximumNumberOfApprovalsExceededException: Type[BotocoreClientError]
    MaximumOpenPullRequestsExceededException: Type[BotocoreClientError]
    MaximumRepositoryNamesExceededException: Type[BotocoreClientError]
    MaximumRepositoryTriggersExceededException: Type[BotocoreClientError]
    MaximumRuleTemplatesAssociatedWithRepositoryException: Type[BotocoreClientError]
    MergeOptionRequiredException: Type[BotocoreClientError]
    MultipleConflictResolutionEntriesException: Type[BotocoreClientError]
    MultipleRepositoriesInPullRequestException: Type[BotocoreClientError]
    NameLengthExceededException: Type[BotocoreClientError]
    NoChangeException: Type[BotocoreClientError]
    NumberOfRuleTemplatesExceededException: Type[BotocoreClientError]
    NumberOfRulesExceededException: Type[BotocoreClientError]
    OverrideAlreadySetException: Type[BotocoreClientError]
    OverrideStatusRequiredException: Type[BotocoreClientError]
    ParentCommitDoesNotExistException: Type[BotocoreClientError]
    ParentCommitIdOutdatedException: Type[BotocoreClientError]
    ParentCommitIdRequiredException: Type[BotocoreClientError]
    PathDoesNotExistException: Type[BotocoreClientError]
    PathRequiredException: Type[BotocoreClientError]
    PullRequestAlreadyClosedException: Type[BotocoreClientError]
    PullRequestApprovalRulesNotSatisfiedException: Type[BotocoreClientError]
    PullRequestCannotBeApprovedByAuthorException: Type[BotocoreClientError]
    PullRequestDoesNotExistException: Type[BotocoreClientError]
    PullRequestIdRequiredException: Type[BotocoreClientError]
    PullRequestStatusRequiredException: Type[BotocoreClientError]
    PutFileEntryConflictException: Type[BotocoreClientError]
    ReactionLimitExceededException: Type[BotocoreClientError]
    ReactionValueRequiredException: Type[BotocoreClientError]
    ReferenceDoesNotExistException: Type[BotocoreClientError]
    ReferenceNameRequiredException: Type[BotocoreClientError]
    ReferenceTypeNotSupportedException: Type[BotocoreClientError]
    ReplacementContentRequiredException: Type[BotocoreClientError]
    ReplacementTypeRequiredException: Type[BotocoreClientError]
    RepositoryDoesNotExistException: Type[BotocoreClientError]
    RepositoryLimitExceededException: Type[BotocoreClientError]
    RepositoryNameExistsException: Type[BotocoreClientError]
    RepositoryNameRequiredException: Type[BotocoreClientError]
    RepositoryNamesRequiredException: Type[BotocoreClientError]
    RepositoryNotAssociatedWithPullRequestException: Type[BotocoreClientError]
    RepositoryTriggerBranchNameListRequiredException: Type[BotocoreClientError]
    RepositoryTriggerDestinationArnRequiredException: Type[BotocoreClientError]
    RepositoryTriggerEventsListRequiredException: Type[BotocoreClientError]
    RepositoryTriggerNameRequiredException: Type[BotocoreClientError]
    RepositoryTriggersListRequiredException: Type[BotocoreClientError]
    ResourceArnRequiredException: Type[BotocoreClientError]
    RestrictedSourceFileException: Type[BotocoreClientError]
    RevisionIdRequiredException: Type[BotocoreClientError]
    RevisionNotCurrentException: Type[BotocoreClientError]
    SameFileContentException: Type[BotocoreClientError]
    SamePathRequestException: Type[BotocoreClientError]
    SourceAndDestinationAreSameException: Type[BotocoreClientError]
    SourceFileOrContentRequiredException: Type[BotocoreClientError]
    TagKeysListRequiredException: Type[BotocoreClientError]
    TagPolicyException: Type[BotocoreClientError]
    TagsMapRequiredException: Type[BotocoreClientError]
    TargetRequiredException: Type[BotocoreClientError]
    TargetsRequiredException: Type[BotocoreClientError]
    TipOfSourceReferenceIsDifferentException: Type[BotocoreClientError]
    TipsDivergenceExceededException: Type[BotocoreClientError]
    TitleRequiredException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]


class CodeCommitClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_approval_rule_template_with_repository(
        self, *, approvalRuleTemplateName: str, repositoryName: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.associate_approval_rule_template_with_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#associate_approval_rule_template_with_repository)
        """

    def batch_associate_approval_rule_template_with_repositories(
        self, *, approvalRuleTemplateName: str, repositoryNames: List[str]
    ) -> BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.batch_associate_approval_rule_template_with_repositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#batch_associate_approval_rule_template_with_repositories)
        """

    def batch_describe_merge_conflicts(
        self,
        *,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: MergeOptionTypeEnumType,
        maxMergeHunks: int = None,
        maxConflictFiles: int = None,
        filePaths: List[str] = None,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None,
        nextToken: str = None
    ) -> BatchDescribeMergeConflictsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.batch_describe_merge_conflicts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#batch_describe_merge_conflicts)
        """

    def batch_disassociate_approval_rule_template_from_repositories(
        self, *, approvalRuleTemplateName: str, repositoryNames: List[str]
    ) -> BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.batch_disassociate_approval_rule_template_from_repositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#batch_disassociate_approval_rule_template_from_repositories)
        """

    def batch_get_commits(
        self, *, commitIds: List[str], repositoryName: str
    ) -> BatchGetCommitsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.batch_get_commits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#batch_get_commits)
        """

    def batch_get_repositories(
        self, *, repositoryNames: List[str]
    ) -> BatchGetRepositoriesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.batch_get_repositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#batch_get_repositories)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#can_paginate)
        """

    def create_approval_rule_template(
        self,
        *,
        approvalRuleTemplateName: str,
        approvalRuleTemplateContent: str,
        approvalRuleTemplateDescription: str = None
    ) -> CreateApprovalRuleTemplateOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.create_approval_rule_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#create_approval_rule_template)
        """

    def create_branch(self, *, repositoryName: str, branchName: str, commitId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.create_branch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#create_branch)
        """

    def create_commit(
        self,
        *,
        repositoryName: str,
        branchName: str,
        parentCommitId: str = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        putFiles: List[PutFileEntryTypeDef] = None,
        deleteFiles: List["DeleteFileEntryTypeDef"] = None,
        setFileModes: List["SetFileModeEntryTypeDef"] = None
    ) -> CreateCommitOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.create_commit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#create_commit)
        """

    def create_pull_request(
        self,
        *,
        title: str,
        targets: List[TargetTypeDef],
        description: str = None,
        clientRequestToken: str = None
    ) -> CreatePullRequestOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.create_pull_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#create_pull_request)
        """

    def create_pull_request_approval_rule(
        self, *, pullRequestId: str, approvalRuleName: str, approvalRuleContent: str
    ) -> CreatePullRequestApprovalRuleOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.create_pull_request_approval_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#create_pull_request_approval_rule)
        """

    def create_repository(
        self, *, repositoryName: str, repositoryDescription: str = None, tags: Dict[str, str] = None
    ) -> CreateRepositoryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.create_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#create_repository)
        """

    def create_unreferenced_merge_commit(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        mergeOption: MergeOptionTypeEnumType,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: ConflictResolutionTypeDef = None
    ) -> CreateUnreferencedMergeCommitOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.create_unreferenced_merge_commit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#create_unreferenced_merge_commit)
        """

    def delete_approval_rule_template(
        self, *, approvalRuleTemplateName: str
    ) -> DeleteApprovalRuleTemplateOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.delete_approval_rule_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#delete_approval_rule_template)
        """

    def delete_branch(self, *, repositoryName: str, branchName: str) -> DeleteBranchOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.delete_branch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#delete_branch)
        """

    def delete_comment_content(self, *, commentId: str) -> DeleteCommentContentOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.delete_comment_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#delete_comment_content)
        """

    def delete_file(
        self,
        *,
        repositoryName: str,
        branchName: str,
        filePath: str,
        parentCommitId: str,
        keepEmptyFolders: bool = None,
        commitMessage: str = None,
        name: str = None,
        email: str = None
    ) -> DeleteFileOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.delete_file)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#delete_file)
        """

    def delete_pull_request_approval_rule(
        self, *, pullRequestId: str, approvalRuleName: str
    ) -> DeletePullRequestApprovalRuleOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.delete_pull_request_approval_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#delete_pull_request_approval_rule)
        """

    def delete_repository(self, *, repositoryName: str) -> DeleteRepositoryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.delete_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#delete_repository)
        """

    def describe_merge_conflicts(
        self,
        *,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: MergeOptionTypeEnumType,
        filePath: str,
        maxMergeHunks: int = None,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None,
        nextToken: str = None
    ) -> DescribeMergeConflictsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.describe_merge_conflicts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#describe_merge_conflicts)
        """

    def describe_pull_request_events(
        self,
        *,
        pullRequestId: str,
        pullRequestEventType: PullRequestEventTypeType = None,
        actorArn: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> DescribePullRequestEventsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.describe_pull_request_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#describe_pull_request_events)
        """

    def disassociate_approval_rule_template_from_repository(
        self, *, approvalRuleTemplateName: str, repositoryName: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.disassociate_approval_rule_template_from_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#disassociate_approval_rule_template_from_repository)
        """

    def evaluate_pull_request_approval_rules(
        self, *, pullRequestId: str, revisionId: str
    ) -> EvaluatePullRequestApprovalRulesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.evaluate_pull_request_approval_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#evaluate_pull_request_approval_rules)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#generate_presigned_url)
        """

    def get_approval_rule_template(
        self, *, approvalRuleTemplateName: str
    ) -> GetApprovalRuleTemplateOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_approval_rule_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_approval_rule_template)
        """

    def get_blob(self, *, repositoryName: str, blobId: str) -> GetBlobOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_blob)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_blob)
        """

    def get_branch(
        self, *, repositoryName: str = None, branchName: str = None
    ) -> GetBranchOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_branch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_branch)
        """

    def get_comment(self, *, commentId: str) -> GetCommentOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_comment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_comment)
        """

    def get_comment_reactions(
        self,
        *,
        commentId: str,
        reactionUserArn: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetCommentReactionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_comment_reactions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_comment_reactions)
        """

    def get_comments_for_compared_commit(
        self,
        *,
        repositoryName: str,
        afterCommitId: str,
        beforeCommitId: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetCommentsForComparedCommitOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_comments_for_compared_commit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_comments_for_compared_commit)
        """

    def get_comments_for_pull_request(
        self,
        *,
        pullRequestId: str,
        repositoryName: str = None,
        beforeCommitId: str = None,
        afterCommitId: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetCommentsForPullRequestOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_comments_for_pull_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_comments_for_pull_request)
        """

    def get_commit(self, *, repositoryName: str, commitId: str) -> GetCommitOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_commit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_commit)
        """

    def get_differences(
        self,
        *,
        repositoryName: str,
        afterCommitSpecifier: str,
        beforeCommitSpecifier: str = None,
        beforePath: str = None,
        afterPath: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetDifferencesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_differences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_differences)
        """

    def get_file(
        self, *, repositoryName: str, filePath: str, commitSpecifier: str = None
    ) -> GetFileOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_file)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_file)
        """

    def get_folder(
        self, *, repositoryName: str, folderPath: str, commitSpecifier: str = None
    ) -> GetFolderOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_folder)
        """

    def get_merge_commit(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None
    ) -> GetMergeCommitOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_merge_commit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_merge_commit)
        """

    def get_merge_conflicts(
        self,
        *,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: MergeOptionTypeEnumType,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        maxConflictFiles: int = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None,
        nextToken: str = None
    ) -> GetMergeConflictsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_merge_conflicts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_merge_conflicts)
        """

    def get_merge_options(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None
    ) -> GetMergeOptionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_merge_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_merge_options)
        """

    def get_pull_request(self, *, pullRequestId: str) -> GetPullRequestOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_pull_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_pull_request)
        """

    def get_pull_request_approval_states(
        self, *, pullRequestId: str, revisionId: str
    ) -> GetPullRequestApprovalStatesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_pull_request_approval_states)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_pull_request_approval_states)
        """

    def get_pull_request_override_state(
        self, *, pullRequestId: str, revisionId: str
    ) -> GetPullRequestOverrideStateOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_pull_request_override_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_pull_request_override_state)
        """

    def get_repository(self, *, repositoryName: str) -> GetRepositoryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_repository)
        """

    def get_repository_triggers(self, *, repositoryName: str) -> GetRepositoryTriggersOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.get_repository_triggers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#get_repository_triggers)
        """

    def list_approval_rule_templates(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListApprovalRuleTemplatesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.list_approval_rule_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#list_approval_rule_templates)
        """

    def list_associated_approval_rule_templates_for_repository(
        self, *, repositoryName: str, nextToken: str = None, maxResults: int = None
    ) -> ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.list_associated_approval_rule_templates_for_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#list_associated_approval_rule_templates_for_repository)
        """

    def list_branches(
        self, *, repositoryName: str, nextToken: str = None
    ) -> ListBranchesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.list_branches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#list_branches)
        """

    def list_pull_requests(
        self,
        *,
        repositoryName: str,
        authorArn: str = None,
        pullRequestStatus: PullRequestStatusEnumType = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListPullRequestsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.list_pull_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#list_pull_requests)
        """

    def list_repositories(
        self, *, nextToken: str = None, sortBy: SortByEnumType = None, order: OrderEnumType = None
    ) -> ListRepositoriesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.list_repositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#list_repositories)
        """

    def list_repositories_for_approval_rule_template(
        self, *, approvalRuleTemplateName: str, nextToken: str = None, maxResults: int = None
    ) -> ListRepositoriesForApprovalRuleTemplateOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.list_repositories_for_approval_rule_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#list_repositories_for_approval_rule_template)
        """

    def list_tags_for_resource(
        self, *, resourceArn: str, nextToken: str = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#list_tags_for_resource)
        """

    def merge_branches_by_fast_forward(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str = None
    ) -> MergeBranchesByFastForwardOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.merge_branches_by_fast_forward)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#merge_branches_by_fast_forward)
        """

    def merge_branches_by_squash(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str = None,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: ConflictResolutionTypeDef = None
    ) -> MergeBranchesBySquashOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.merge_branches_by_squash)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#merge_branches_by_squash)
        """

    def merge_branches_by_three_way(
        self,
        *,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str = None,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: ConflictResolutionTypeDef = None
    ) -> MergeBranchesByThreeWayOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.merge_branches_by_three_way)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#merge_branches_by_three_way)
        """

    def merge_pull_request_by_fast_forward(
        self, *, pullRequestId: str, repositoryName: str, sourceCommitId: str = None
    ) -> MergePullRequestByFastForwardOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.merge_pull_request_by_fast_forward)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#merge_pull_request_by_fast_forward)
        """

    def merge_pull_request_by_squash(
        self,
        *,
        pullRequestId: str,
        repositoryName: str,
        sourceCommitId: str = None,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None,
        commitMessage: str = None,
        authorName: str = None,
        email: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: ConflictResolutionTypeDef = None
    ) -> MergePullRequestBySquashOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.merge_pull_request_by_squash)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#merge_pull_request_by_squash)
        """

    def merge_pull_request_by_three_way(
        self,
        *,
        pullRequestId: str,
        repositoryName: str,
        sourceCommitId: str = None,
        conflictDetailLevel: ConflictDetailLevelTypeEnumType = None,
        conflictResolutionStrategy: ConflictResolutionStrategyTypeEnumType = None,
        commitMessage: str = None,
        authorName: str = None,
        email: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: ConflictResolutionTypeDef = None
    ) -> MergePullRequestByThreeWayOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.merge_pull_request_by_three_way)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#merge_pull_request_by_three_way)
        """

    def override_pull_request_approval_rules(
        self, *, pullRequestId: str, revisionId: str, overrideStatus: OverrideStatusType
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.override_pull_request_approval_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#override_pull_request_approval_rules)
        """

    def post_comment_for_compared_commit(
        self,
        *,
        repositoryName: str,
        afterCommitId: str,
        content: str,
        beforeCommitId: str = None,
        location: "LocationTypeDef" = None,
        clientRequestToken: str = None
    ) -> PostCommentForComparedCommitOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.post_comment_for_compared_commit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#post_comment_for_compared_commit)
        """

    def post_comment_for_pull_request(
        self,
        *,
        pullRequestId: str,
        repositoryName: str,
        beforeCommitId: str,
        afterCommitId: str,
        content: str,
        location: "LocationTypeDef" = None,
        clientRequestToken: str = None
    ) -> PostCommentForPullRequestOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.post_comment_for_pull_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#post_comment_for_pull_request)
        """

    def post_comment_reply(
        self, *, inReplyTo: str, content: str, clientRequestToken: str = None
    ) -> PostCommentReplyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.post_comment_reply)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#post_comment_reply)
        """

    def put_comment_reaction(self, *, commentId: str, reactionValue: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.put_comment_reaction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#put_comment_reaction)
        """

    def put_file(
        self,
        *,
        repositoryName: str,
        branchName: str,
        fileContent: Union[bytes, IO[bytes], StreamingBody],
        filePath: str,
        fileMode: FileModeTypeEnumType = None,
        parentCommitId: str = None,
        commitMessage: str = None,
        name: str = None,
        email: str = None
    ) -> PutFileOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.put_file)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#put_file)
        """

    def put_repository_triggers(
        self, *, repositoryName: str, triggers: List["RepositoryTriggerTypeDef"]
    ) -> PutRepositoryTriggersOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.put_repository_triggers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#put_repository_triggers)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#tag_resource)
        """

    def test_repository_triggers(
        self, *, repositoryName: str, triggers: List["RepositoryTriggerTypeDef"]
    ) -> TestRepositoryTriggersOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.test_repository_triggers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#test_repository_triggers)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#untag_resource)
        """

    def update_approval_rule_template_content(
        self,
        *,
        approvalRuleTemplateName: str,
        newRuleContent: str,
        existingRuleContentSha256: str = None
    ) -> UpdateApprovalRuleTemplateContentOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.update_approval_rule_template_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_approval_rule_template_content)
        """

    def update_approval_rule_template_description(
        self, *, approvalRuleTemplateName: str, approvalRuleTemplateDescription: str
    ) -> UpdateApprovalRuleTemplateDescriptionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.update_approval_rule_template_description)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_approval_rule_template_description)
        """

    def update_approval_rule_template_name(
        self, *, oldApprovalRuleTemplateName: str, newApprovalRuleTemplateName: str
    ) -> UpdateApprovalRuleTemplateNameOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.update_approval_rule_template_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_approval_rule_template_name)
        """

    def update_comment(self, *, commentId: str, content: str) -> UpdateCommentOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.update_comment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_comment)
        """

    def update_default_branch(self, *, repositoryName: str, defaultBranchName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.update_default_branch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_default_branch)
        """

    def update_pull_request_approval_rule_content(
        self,
        *,
        pullRequestId: str,
        approvalRuleName: str,
        newRuleContent: str,
        existingRuleContentSha256: str = None
    ) -> UpdatePullRequestApprovalRuleContentOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_approval_rule_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_pull_request_approval_rule_content)
        """

    def update_pull_request_approval_state(
        self, *, pullRequestId: str, revisionId: str, approvalState: ApprovalStateType
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_approval_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_pull_request_approval_state)
        """

    def update_pull_request_description(
        self, *, pullRequestId: str, description: str
    ) -> UpdatePullRequestDescriptionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_description)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_pull_request_description)
        """

    def update_pull_request_status(
        self, *, pullRequestId: str, pullRequestStatus: PullRequestStatusEnumType
    ) -> UpdatePullRequestStatusOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_pull_request_status)
        """

    def update_pull_request_title(
        self, *, pullRequestId: str, title: str
    ) -> UpdatePullRequestTitleOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_title)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_pull_request_title)
        """

    def update_repository_description(
        self, *, repositoryName: str, repositoryDescription: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.update_repository_description)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_repository_description)
        """

    def update_repository_name(self, *, oldName: str, newName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Client.update_repository_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/client.html#update_repository_name)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_pull_request_events"]
    ) -> DescribePullRequestEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Paginator.DescribePullRequestEvents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#describepullrequesteventspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_comments_for_compared_commit"]
    ) -> GetCommentsForComparedCommitPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForComparedCommit)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#getcommentsforcomparedcommitpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_comments_for_pull_request"]
    ) -> GetCommentsForPullRequestPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForPullRequest)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#getcommentsforpullrequestpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_differences"]) -> GetDifferencesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Paginator.GetDifferences)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#getdifferencespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_branches"]) -> ListBranchesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Paginator.ListBranches)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#listbranchespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pull_requests"]
    ) -> ListPullRequestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Paginator.ListPullRequests)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#listpullrequestspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_repositories"]
    ) -> ListRepositoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codecommit.html#CodeCommit.Paginator.ListRepositories)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/paginators.html#listrepositoriespaginator)
        """
