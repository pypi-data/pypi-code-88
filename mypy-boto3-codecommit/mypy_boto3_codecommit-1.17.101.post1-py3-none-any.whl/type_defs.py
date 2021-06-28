"""
Type annotations for codecommit service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codecommit.type_defs import ApprovalRuleEventMetadataTypeDef

    data: ApprovalRuleEventMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ApprovalStateType,
    ChangeTypeEnumType,
    ConflictDetailLevelTypeEnumType,
    ConflictResolutionStrategyTypeEnumType,
    FileModeTypeEnumType,
    MergeOptionTypeEnumType,
    ObjectTypeEnumType,
    OrderEnumType,
    OverrideStatusType,
    PullRequestEventTypeType,
    PullRequestStatusEnumType,
    RelativeFileVersionEnumType,
    ReplacementTypeEnumType,
    RepositoryTriggerEventEnumType,
    SortByEnumType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApprovalRuleEventMetadataTypeDef",
    "ApprovalRuleOverriddenEventMetadataTypeDef",
    "ApprovalRuleTemplateTypeDef",
    "ApprovalRuleTypeDef",
    "ApprovalStateChangedEventMetadataTypeDef",
    "ApprovalTypeDef",
    "AssociateApprovalRuleTemplateWithRepositoryInputTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesInputTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesOutputResponseTypeDef",
    "BatchDescribeMergeConflictsErrorTypeDef",
    "BatchDescribeMergeConflictsInputTypeDef",
    "BatchDescribeMergeConflictsOutputResponseTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesInputTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputResponseTypeDef",
    "BatchGetCommitsErrorTypeDef",
    "BatchGetCommitsInputTypeDef",
    "BatchGetCommitsOutputResponseTypeDef",
    "BatchGetRepositoriesInputTypeDef",
    "BatchGetRepositoriesOutputResponseTypeDef",
    "BlobMetadataTypeDef",
    "BranchInfoTypeDef",
    "CommentTypeDef",
    "CommentsForComparedCommitTypeDef",
    "CommentsForPullRequestTypeDef",
    "CommitTypeDef",
    "ConflictMetadataTypeDef",
    "ConflictResolutionTypeDef",
    "ConflictTypeDef",
    "CreateApprovalRuleTemplateInputTypeDef",
    "CreateApprovalRuleTemplateOutputResponseTypeDef",
    "CreateBranchInputTypeDef",
    "CreateCommitInputTypeDef",
    "CreateCommitOutputResponseTypeDef",
    "CreatePullRequestApprovalRuleInputTypeDef",
    "CreatePullRequestApprovalRuleOutputResponseTypeDef",
    "CreatePullRequestInputTypeDef",
    "CreatePullRequestOutputResponseTypeDef",
    "CreateRepositoryInputTypeDef",
    "CreateRepositoryOutputResponseTypeDef",
    "CreateUnreferencedMergeCommitInputTypeDef",
    "CreateUnreferencedMergeCommitOutputResponseTypeDef",
    "DeleteApprovalRuleTemplateInputTypeDef",
    "DeleteApprovalRuleTemplateOutputResponseTypeDef",
    "DeleteBranchInputTypeDef",
    "DeleteBranchOutputResponseTypeDef",
    "DeleteCommentContentInputTypeDef",
    "DeleteCommentContentOutputResponseTypeDef",
    "DeleteFileEntryTypeDef",
    "DeleteFileInputTypeDef",
    "DeleteFileOutputResponseTypeDef",
    "DeletePullRequestApprovalRuleInputTypeDef",
    "DeletePullRequestApprovalRuleOutputResponseTypeDef",
    "DeleteRepositoryInputTypeDef",
    "DeleteRepositoryOutputResponseTypeDef",
    "DescribeMergeConflictsInputTypeDef",
    "DescribeMergeConflictsOutputResponseTypeDef",
    "DescribePullRequestEventsInputTypeDef",
    "DescribePullRequestEventsOutputResponseTypeDef",
    "DifferenceTypeDef",
    "DisassociateApprovalRuleTemplateFromRepositoryInputTypeDef",
    "EvaluatePullRequestApprovalRulesInputTypeDef",
    "EvaluatePullRequestApprovalRulesOutputResponseTypeDef",
    "EvaluationTypeDef",
    "FileMetadataTypeDef",
    "FileModesTypeDef",
    "FileSizesTypeDef",
    "FileTypeDef",
    "FolderTypeDef",
    "GetApprovalRuleTemplateInputTypeDef",
    "GetApprovalRuleTemplateOutputResponseTypeDef",
    "GetBlobInputTypeDef",
    "GetBlobOutputResponseTypeDef",
    "GetBranchInputTypeDef",
    "GetBranchOutputResponseTypeDef",
    "GetCommentInputTypeDef",
    "GetCommentOutputResponseTypeDef",
    "GetCommentReactionsInputTypeDef",
    "GetCommentReactionsOutputResponseTypeDef",
    "GetCommentsForComparedCommitInputTypeDef",
    "GetCommentsForComparedCommitOutputResponseTypeDef",
    "GetCommentsForPullRequestInputTypeDef",
    "GetCommentsForPullRequestOutputResponseTypeDef",
    "GetCommitInputTypeDef",
    "GetCommitOutputResponseTypeDef",
    "GetDifferencesInputTypeDef",
    "GetDifferencesOutputResponseTypeDef",
    "GetFileInputTypeDef",
    "GetFileOutputResponseTypeDef",
    "GetFolderInputTypeDef",
    "GetFolderOutputResponseTypeDef",
    "GetMergeCommitInputTypeDef",
    "GetMergeCommitOutputResponseTypeDef",
    "GetMergeConflictsInputTypeDef",
    "GetMergeConflictsOutputResponseTypeDef",
    "GetMergeOptionsInputTypeDef",
    "GetMergeOptionsOutputResponseTypeDef",
    "GetPullRequestApprovalStatesInputTypeDef",
    "GetPullRequestApprovalStatesOutputResponseTypeDef",
    "GetPullRequestInputTypeDef",
    "GetPullRequestOutputResponseTypeDef",
    "GetPullRequestOverrideStateInputTypeDef",
    "GetPullRequestOverrideStateOutputResponseTypeDef",
    "GetRepositoryInputTypeDef",
    "GetRepositoryOutputResponseTypeDef",
    "GetRepositoryTriggersInputTypeDef",
    "GetRepositoryTriggersOutputResponseTypeDef",
    "IsBinaryFileTypeDef",
    "ListApprovalRuleTemplatesInputTypeDef",
    "ListApprovalRuleTemplatesOutputResponseTypeDef",
    "ListAssociatedApprovalRuleTemplatesForRepositoryInputTypeDef",
    "ListAssociatedApprovalRuleTemplatesForRepositoryOutputResponseTypeDef",
    "ListBranchesInputTypeDef",
    "ListBranchesOutputResponseTypeDef",
    "ListPullRequestsInputTypeDef",
    "ListPullRequestsOutputResponseTypeDef",
    "ListRepositoriesForApprovalRuleTemplateInputTypeDef",
    "ListRepositoriesForApprovalRuleTemplateOutputResponseTypeDef",
    "ListRepositoriesInputTypeDef",
    "ListRepositoriesOutputResponseTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputResponseTypeDef",
    "LocationTypeDef",
    "MergeBranchesByFastForwardInputTypeDef",
    "MergeBranchesByFastForwardOutputResponseTypeDef",
    "MergeBranchesBySquashInputTypeDef",
    "MergeBranchesBySquashOutputResponseTypeDef",
    "MergeBranchesByThreeWayInputTypeDef",
    "MergeBranchesByThreeWayOutputResponseTypeDef",
    "MergeHunkDetailTypeDef",
    "MergeHunkTypeDef",
    "MergeMetadataTypeDef",
    "MergeOperationsTypeDef",
    "MergePullRequestByFastForwardInputTypeDef",
    "MergePullRequestByFastForwardOutputResponseTypeDef",
    "MergePullRequestBySquashInputTypeDef",
    "MergePullRequestBySquashOutputResponseTypeDef",
    "MergePullRequestByThreeWayInputTypeDef",
    "MergePullRequestByThreeWayOutputResponseTypeDef",
    "ObjectTypesTypeDef",
    "OriginApprovalRuleTemplateTypeDef",
    "OverridePullRequestApprovalRulesInputTypeDef",
    "PaginatorConfigTypeDef",
    "PostCommentForComparedCommitInputTypeDef",
    "PostCommentForComparedCommitOutputResponseTypeDef",
    "PostCommentForPullRequestInputTypeDef",
    "PostCommentForPullRequestOutputResponseTypeDef",
    "PostCommentReplyInputTypeDef",
    "PostCommentReplyOutputResponseTypeDef",
    "PullRequestCreatedEventMetadataTypeDef",
    "PullRequestEventTypeDef",
    "PullRequestMergedStateChangedEventMetadataTypeDef",
    "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    "PullRequestStatusChangedEventMetadataTypeDef",
    "PullRequestTargetTypeDef",
    "PullRequestTypeDef",
    "PutCommentReactionInputTypeDef",
    "PutFileEntryTypeDef",
    "PutFileInputTypeDef",
    "PutFileOutputResponseTypeDef",
    "PutRepositoryTriggersInputTypeDef",
    "PutRepositoryTriggersOutputResponseTypeDef",
    "ReactionForCommentTypeDef",
    "ReactionValueFormatsTypeDef",
    "ReplaceContentEntryTypeDef",
    "RepositoryMetadataTypeDef",
    "RepositoryNameIdPairTypeDef",
    "RepositoryTriggerExecutionFailureTypeDef",
    "RepositoryTriggerTypeDef",
    "ResponseMetadataTypeDef",
    "SetFileModeEntryTypeDef",
    "SourceFileSpecifierTypeDef",
    "SubModuleTypeDef",
    "SymbolicLinkTypeDef",
    "TagResourceInputTypeDef",
    "TargetTypeDef",
    "TestRepositoryTriggersInputTypeDef",
    "TestRepositoryTriggersOutputResponseTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateApprovalRuleTemplateContentInputTypeDef",
    "UpdateApprovalRuleTemplateContentOutputResponseTypeDef",
    "UpdateApprovalRuleTemplateDescriptionInputTypeDef",
    "UpdateApprovalRuleTemplateDescriptionOutputResponseTypeDef",
    "UpdateApprovalRuleTemplateNameInputTypeDef",
    "UpdateApprovalRuleTemplateNameOutputResponseTypeDef",
    "UpdateCommentInputTypeDef",
    "UpdateCommentOutputResponseTypeDef",
    "UpdateDefaultBranchInputTypeDef",
    "UpdatePullRequestApprovalRuleContentInputTypeDef",
    "UpdatePullRequestApprovalRuleContentOutputResponseTypeDef",
    "UpdatePullRequestApprovalStateInputTypeDef",
    "UpdatePullRequestDescriptionInputTypeDef",
    "UpdatePullRequestDescriptionOutputResponseTypeDef",
    "UpdatePullRequestStatusInputTypeDef",
    "UpdatePullRequestStatusOutputResponseTypeDef",
    "UpdatePullRequestTitleInputTypeDef",
    "UpdatePullRequestTitleOutputResponseTypeDef",
    "UpdateRepositoryDescriptionInputTypeDef",
    "UpdateRepositoryNameInputTypeDef",
    "UserInfoTypeDef",
)

ApprovalRuleEventMetadataTypeDef = TypedDict(
    "ApprovalRuleEventMetadataTypeDef",
    {
        "approvalRuleName": str,
        "approvalRuleId": str,
        "approvalRuleContent": str,
    },
    total=False,
)

ApprovalRuleOverriddenEventMetadataTypeDef = TypedDict(
    "ApprovalRuleOverriddenEventMetadataTypeDef",
    {
        "revisionId": str,
        "overrideStatus": OverrideStatusType,
    },
    total=False,
)

ApprovalRuleTemplateTypeDef = TypedDict(
    "ApprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": str,
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateDescription": str,
        "approvalRuleTemplateContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
    },
    total=False,
)

ApprovalRuleTypeDef = TypedDict(
    "ApprovalRuleTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": "OriginApprovalRuleTemplateTypeDef",
    },
    total=False,
)

ApprovalStateChangedEventMetadataTypeDef = TypedDict(
    "ApprovalStateChangedEventMetadataTypeDef",
    {
        "revisionId": str,
        "approvalStatus": ApprovalStateType,
    },
    total=False,
)

ApprovalTypeDef = TypedDict(
    "ApprovalTypeDef",
    {
        "userArn": str,
        "approvalState": ApprovalStateType,
    },
    total=False,
)

AssociateApprovalRuleTemplateWithRepositoryInputTypeDef = TypedDict(
    "AssociateApprovalRuleTemplateWithRepositoryInputTypeDef",
    {
        "approvalRuleTemplateName": str,
        "repositoryName": str,
    },
)

BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef = TypedDict(
    "BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef",
    {
        "repositoryName": str,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

BatchAssociateApprovalRuleTemplateWithRepositoriesInputTypeDef = TypedDict(
    "BatchAssociateApprovalRuleTemplateWithRepositoriesInputTypeDef",
    {
        "approvalRuleTemplateName": str,
        "repositoryNames": List[str],
    },
)

BatchAssociateApprovalRuleTemplateWithRepositoriesOutputResponseTypeDef = TypedDict(
    "BatchAssociateApprovalRuleTemplateWithRepositoriesOutputResponseTypeDef",
    {
        "associatedRepositoryNames": List[str],
        "errors": List["BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDescribeMergeConflictsErrorTypeDef = TypedDict(
    "BatchDescribeMergeConflictsErrorTypeDef",
    {
        "filePath": str,
        "exceptionName": str,
        "message": str,
    },
)

_RequiredBatchDescribeMergeConflictsInputTypeDef = TypedDict(
    "_RequiredBatchDescribeMergeConflictsInputTypeDef",
    {
        "repositoryName": str,
        "destinationCommitSpecifier": str,
        "sourceCommitSpecifier": str,
        "mergeOption": MergeOptionTypeEnumType,
    },
)
_OptionalBatchDescribeMergeConflictsInputTypeDef = TypedDict(
    "_OptionalBatchDescribeMergeConflictsInputTypeDef",
    {
        "maxMergeHunks": int,
        "maxConflictFiles": int,
        "filePaths": List[str],
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
        "nextToken": str,
    },
    total=False,
)


class BatchDescribeMergeConflictsInputTypeDef(
    _RequiredBatchDescribeMergeConflictsInputTypeDef,
    _OptionalBatchDescribeMergeConflictsInputTypeDef,
):
    pass


BatchDescribeMergeConflictsOutputResponseTypeDef = TypedDict(
    "BatchDescribeMergeConflictsOutputResponseTypeDef",
    {
        "conflicts": List["ConflictTypeDef"],
        "nextToken": str,
        "errors": List["BatchDescribeMergeConflictsErrorTypeDef"],
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef = TypedDict(
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef",
    {
        "repositoryName": str,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

BatchDisassociateApprovalRuleTemplateFromRepositoriesInputTypeDef = TypedDict(
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesInputTypeDef",
    {
        "approvalRuleTemplateName": str,
        "repositoryNames": List[str],
    },
)

BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputResponseTypeDef = TypedDict(
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputResponseTypeDef",
    {
        "disassociatedRepositoryNames": List[str],
        "errors": List["BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetCommitsErrorTypeDef = TypedDict(
    "BatchGetCommitsErrorTypeDef",
    {
        "commitId": str,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

BatchGetCommitsInputTypeDef = TypedDict(
    "BatchGetCommitsInputTypeDef",
    {
        "commitIds": List[str],
        "repositoryName": str,
    },
)

BatchGetCommitsOutputResponseTypeDef = TypedDict(
    "BatchGetCommitsOutputResponseTypeDef",
    {
        "commits": List["CommitTypeDef"],
        "errors": List["BatchGetCommitsErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetRepositoriesInputTypeDef = TypedDict(
    "BatchGetRepositoriesInputTypeDef",
    {
        "repositoryNames": List[str],
    },
)

BatchGetRepositoriesOutputResponseTypeDef = TypedDict(
    "BatchGetRepositoriesOutputResponseTypeDef",
    {
        "repositories": List["RepositoryMetadataTypeDef"],
        "repositoriesNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BlobMetadataTypeDef = TypedDict(
    "BlobMetadataTypeDef",
    {
        "blobId": str,
        "path": str,
        "mode": str,
    },
    total=False,
)

BranchInfoTypeDef = TypedDict(
    "BranchInfoTypeDef",
    {
        "branchName": str,
        "commitId": str,
    },
    total=False,
)

CommentTypeDef = TypedDict(
    "CommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
        "callerReactions": List[str],
        "reactionCounts": Dict[str, int],
    },
    total=False,
)

CommentsForComparedCommitTypeDef = TypedDict(
    "CommentsForComparedCommitTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": "LocationTypeDef",
        "comments": List["CommentTypeDef"],
    },
    total=False,
)

CommentsForPullRequestTypeDef = TypedDict(
    "CommentsForPullRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": "LocationTypeDef",
        "comments": List["CommentTypeDef"],
    },
    total=False,
)

CommitTypeDef = TypedDict(
    "CommitTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "parents": List[str],
        "message": str,
        "author": "UserInfoTypeDef",
        "committer": "UserInfoTypeDef",
        "additionalData": str,
    },
    total=False,
)

ConflictMetadataTypeDef = TypedDict(
    "ConflictMetadataTypeDef",
    {
        "filePath": str,
        "fileSizes": "FileSizesTypeDef",
        "fileModes": "FileModesTypeDef",
        "objectTypes": "ObjectTypesTypeDef",
        "numberOfConflicts": int,
        "isBinaryFile": "IsBinaryFileTypeDef",
        "contentConflict": bool,
        "fileModeConflict": bool,
        "objectTypeConflict": bool,
        "mergeOperations": "MergeOperationsTypeDef",
    },
    total=False,
)

ConflictResolutionTypeDef = TypedDict(
    "ConflictResolutionTypeDef",
    {
        "replaceContents": List["ReplaceContentEntryTypeDef"],
        "deleteFiles": List["DeleteFileEntryTypeDef"],
        "setFileModes": List["SetFileModeEntryTypeDef"],
    },
    total=False,
)

ConflictTypeDef = TypedDict(
    "ConflictTypeDef",
    {
        "conflictMetadata": "ConflictMetadataTypeDef",
        "mergeHunks": List["MergeHunkTypeDef"],
    },
    total=False,
)

_RequiredCreateApprovalRuleTemplateInputTypeDef = TypedDict(
    "_RequiredCreateApprovalRuleTemplateInputTypeDef",
    {
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateContent": str,
    },
)
_OptionalCreateApprovalRuleTemplateInputTypeDef = TypedDict(
    "_OptionalCreateApprovalRuleTemplateInputTypeDef",
    {
        "approvalRuleTemplateDescription": str,
    },
    total=False,
)


class CreateApprovalRuleTemplateInputTypeDef(
    _RequiredCreateApprovalRuleTemplateInputTypeDef, _OptionalCreateApprovalRuleTemplateInputTypeDef
):
    pass


CreateApprovalRuleTemplateOutputResponseTypeDef = TypedDict(
    "CreateApprovalRuleTemplateOutputResponseTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBranchInputTypeDef = TypedDict(
    "CreateBranchInputTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
        "commitId": str,
    },
)

_RequiredCreateCommitInputTypeDef = TypedDict(
    "_RequiredCreateCommitInputTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
    },
)
_OptionalCreateCommitInputTypeDef = TypedDict(
    "_OptionalCreateCommitInputTypeDef",
    {
        "parentCommitId": str,
        "authorName": str,
        "email": str,
        "commitMessage": str,
        "keepEmptyFolders": bool,
        "putFiles": List["PutFileEntryTypeDef"],
        "deleteFiles": List["DeleteFileEntryTypeDef"],
        "setFileModes": List["SetFileModeEntryTypeDef"],
    },
    total=False,
)


class CreateCommitInputTypeDef(
    _RequiredCreateCommitInputTypeDef, _OptionalCreateCommitInputTypeDef
):
    pass


CreateCommitOutputResponseTypeDef = TypedDict(
    "CreateCommitOutputResponseTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "filesAdded": List["FileMetadataTypeDef"],
        "filesUpdated": List["FileMetadataTypeDef"],
        "filesDeleted": List["FileMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePullRequestApprovalRuleInputTypeDef = TypedDict(
    "CreatePullRequestApprovalRuleInputTypeDef",
    {
        "pullRequestId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
    },
)

CreatePullRequestApprovalRuleOutputResponseTypeDef = TypedDict(
    "CreatePullRequestApprovalRuleOutputResponseTypeDef",
    {
        "approvalRule": "ApprovalRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePullRequestInputTypeDef = TypedDict(
    "_RequiredCreatePullRequestInputTypeDef",
    {
        "title": str,
        "targets": List["TargetTypeDef"],
    },
)
_OptionalCreatePullRequestInputTypeDef = TypedDict(
    "_OptionalCreatePullRequestInputTypeDef",
    {
        "description": str,
        "clientRequestToken": str,
    },
    total=False,
)


class CreatePullRequestInputTypeDef(
    _RequiredCreatePullRequestInputTypeDef, _OptionalCreatePullRequestInputTypeDef
):
    pass


CreatePullRequestOutputResponseTypeDef = TypedDict(
    "CreatePullRequestOutputResponseTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRepositoryInputTypeDef = TypedDict(
    "_RequiredCreateRepositoryInputTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalCreateRepositoryInputTypeDef = TypedDict(
    "_OptionalCreateRepositoryInputTypeDef",
    {
        "repositoryDescription": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateRepositoryInputTypeDef(
    _RequiredCreateRepositoryInputTypeDef, _OptionalCreateRepositoryInputTypeDef
):
    pass


CreateRepositoryOutputResponseTypeDef = TypedDict(
    "CreateRepositoryOutputResponseTypeDef",
    {
        "repositoryMetadata": "RepositoryMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUnreferencedMergeCommitInputTypeDef = TypedDict(
    "_RequiredCreateUnreferencedMergeCommitInputTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
        "mergeOption": MergeOptionTypeEnumType,
    },
)
_OptionalCreateUnreferencedMergeCommitInputTypeDef = TypedDict(
    "_OptionalCreateUnreferencedMergeCommitInputTypeDef",
    {
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
        "authorName": str,
        "email": str,
        "commitMessage": str,
        "keepEmptyFolders": bool,
        "conflictResolution": "ConflictResolutionTypeDef",
    },
    total=False,
)


class CreateUnreferencedMergeCommitInputTypeDef(
    _RequiredCreateUnreferencedMergeCommitInputTypeDef,
    _OptionalCreateUnreferencedMergeCommitInputTypeDef,
):
    pass


CreateUnreferencedMergeCommitOutputResponseTypeDef = TypedDict(
    "CreateUnreferencedMergeCommitOutputResponseTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApprovalRuleTemplateInputTypeDef = TypedDict(
    "DeleteApprovalRuleTemplateInputTypeDef",
    {
        "approvalRuleTemplateName": str,
    },
)

DeleteApprovalRuleTemplateOutputResponseTypeDef = TypedDict(
    "DeleteApprovalRuleTemplateOutputResponseTypeDef",
    {
        "approvalRuleTemplateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBranchInputTypeDef = TypedDict(
    "DeleteBranchInputTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
    },
)

DeleteBranchOutputResponseTypeDef = TypedDict(
    "DeleteBranchOutputResponseTypeDef",
    {
        "deletedBranch": "BranchInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCommentContentInputTypeDef = TypedDict(
    "DeleteCommentContentInputTypeDef",
    {
        "commentId": str,
    },
)

DeleteCommentContentOutputResponseTypeDef = TypedDict(
    "DeleteCommentContentOutputResponseTypeDef",
    {
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFileEntryTypeDef = TypedDict(
    "DeleteFileEntryTypeDef",
    {
        "filePath": str,
    },
)

_RequiredDeleteFileInputTypeDef = TypedDict(
    "_RequiredDeleteFileInputTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
        "filePath": str,
        "parentCommitId": str,
    },
)
_OptionalDeleteFileInputTypeDef = TypedDict(
    "_OptionalDeleteFileInputTypeDef",
    {
        "keepEmptyFolders": bool,
        "commitMessage": str,
        "name": str,
        "email": str,
    },
    total=False,
)


class DeleteFileInputTypeDef(_RequiredDeleteFileInputTypeDef, _OptionalDeleteFileInputTypeDef):
    pass


DeleteFileOutputResponseTypeDef = TypedDict(
    "DeleteFileOutputResponseTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "treeId": str,
        "filePath": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePullRequestApprovalRuleInputTypeDef = TypedDict(
    "DeletePullRequestApprovalRuleInputTypeDef",
    {
        "pullRequestId": str,
        "approvalRuleName": str,
    },
)

DeletePullRequestApprovalRuleOutputResponseTypeDef = TypedDict(
    "DeletePullRequestApprovalRuleOutputResponseTypeDef",
    {
        "approvalRuleId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRepositoryInputTypeDef = TypedDict(
    "DeleteRepositoryInputTypeDef",
    {
        "repositoryName": str,
    },
)

DeleteRepositoryOutputResponseTypeDef = TypedDict(
    "DeleteRepositoryOutputResponseTypeDef",
    {
        "repositoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMergeConflictsInputTypeDef = TypedDict(
    "_RequiredDescribeMergeConflictsInputTypeDef",
    {
        "repositoryName": str,
        "destinationCommitSpecifier": str,
        "sourceCommitSpecifier": str,
        "mergeOption": MergeOptionTypeEnumType,
        "filePath": str,
    },
)
_OptionalDescribeMergeConflictsInputTypeDef = TypedDict(
    "_OptionalDescribeMergeConflictsInputTypeDef",
    {
        "maxMergeHunks": int,
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
        "nextToken": str,
    },
    total=False,
)


class DescribeMergeConflictsInputTypeDef(
    _RequiredDescribeMergeConflictsInputTypeDef, _OptionalDescribeMergeConflictsInputTypeDef
):
    pass


DescribeMergeConflictsOutputResponseTypeDef = TypedDict(
    "DescribeMergeConflictsOutputResponseTypeDef",
    {
        "conflictMetadata": "ConflictMetadataTypeDef",
        "mergeHunks": List["MergeHunkTypeDef"],
        "nextToken": str,
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribePullRequestEventsInputTypeDef = TypedDict(
    "_RequiredDescribePullRequestEventsInputTypeDef",
    {
        "pullRequestId": str,
    },
)
_OptionalDescribePullRequestEventsInputTypeDef = TypedDict(
    "_OptionalDescribePullRequestEventsInputTypeDef",
    {
        "pullRequestEventType": PullRequestEventTypeType,
        "actorArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class DescribePullRequestEventsInputTypeDef(
    _RequiredDescribePullRequestEventsInputTypeDef, _OptionalDescribePullRequestEventsInputTypeDef
):
    pass


DescribePullRequestEventsOutputResponseTypeDef = TypedDict(
    "DescribePullRequestEventsOutputResponseTypeDef",
    {
        "pullRequestEvents": List["PullRequestEventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DifferenceTypeDef = TypedDict(
    "DifferenceTypeDef",
    {
        "beforeBlob": "BlobMetadataTypeDef",
        "afterBlob": "BlobMetadataTypeDef",
        "changeType": ChangeTypeEnumType,
    },
    total=False,
)

DisassociateApprovalRuleTemplateFromRepositoryInputTypeDef = TypedDict(
    "DisassociateApprovalRuleTemplateFromRepositoryInputTypeDef",
    {
        "approvalRuleTemplateName": str,
        "repositoryName": str,
    },
)

EvaluatePullRequestApprovalRulesInputTypeDef = TypedDict(
    "EvaluatePullRequestApprovalRulesInputTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
    },
)

EvaluatePullRequestApprovalRulesOutputResponseTypeDef = TypedDict(
    "EvaluatePullRequestApprovalRulesOutputResponseTypeDef",
    {
        "evaluation": "EvaluationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EvaluationTypeDef = TypedDict(
    "EvaluationTypeDef",
    {
        "approved": bool,
        "overridden": bool,
        "approvalRulesSatisfied": List[str],
        "approvalRulesNotSatisfied": List[str],
    },
    total=False,
)

FileMetadataTypeDef = TypedDict(
    "FileMetadataTypeDef",
    {
        "absolutePath": str,
        "blobId": str,
        "fileMode": FileModeTypeEnumType,
    },
    total=False,
)

FileModesTypeDef = TypedDict(
    "FileModesTypeDef",
    {
        "source": FileModeTypeEnumType,
        "destination": FileModeTypeEnumType,
        "base": FileModeTypeEnumType,
    },
    total=False,
)

FileSizesTypeDef = TypedDict(
    "FileSizesTypeDef",
    {
        "source": int,
        "destination": int,
        "base": int,
    },
    total=False,
)

FileTypeDef = TypedDict(
    "FileTypeDef",
    {
        "blobId": str,
        "absolutePath": str,
        "relativePath": str,
        "fileMode": FileModeTypeEnumType,
    },
    total=False,
)

FolderTypeDef = TypedDict(
    "FolderTypeDef",
    {
        "treeId": str,
        "absolutePath": str,
        "relativePath": str,
    },
    total=False,
)

GetApprovalRuleTemplateInputTypeDef = TypedDict(
    "GetApprovalRuleTemplateInputTypeDef",
    {
        "approvalRuleTemplateName": str,
    },
)

GetApprovalRuleTemplateOutputResponseTypeDef = TypedDict(
    "GetApprovalRuleTemplateOutputResponseTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBlobInputTypeDef = TypedDict(
    "GetBlobInputTypeDef",
    {
        "repositoryName": str,
        "blobId": str,
    },
)

GetBlobOutputResponseTypeDef = TypedDict(
    "GetBlobOutputResponseTypeDef",
    {
        "content": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBranchInputTypeDef = TypedDict(
    "GetBranchInputTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
    },
    total=False,
)

GetBranchOutputResponseTypeDef = TypedDict(
    "GetBranchOutputResponseTypeDef",
    {
        "branch": "BranchInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCommentInputTypeDef = TypedDict(
    "GetCommentInputTypeDef",
    {
        "commentId": str,
    },
)

GetCommentOutputResponseTypeDef = TypedDict(
    "GetCommentOutputResponseTypeDef",
    {
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCommentReactionsInputTypeDef = TypedDict(
    "_RequiredGetCommentReactionsInputTypeDef",
    {
        "commentId": str,
    },
)
_OptionalGetCommentReactionsInputTypeDef = TypedDict(
    "_OptionalGetCommentReactionsInputTypeDef",
    {
        "reactionUserArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetCommentReactionsInputTypeDef(
    _RequiredGetCommentReactionsInputTypeDef, _OptionalGetCommentReactionsInputTypeDef
):
    pass


GetCommentReactionsOutputResponseTypeDef = TypedDict(
    "GetCommentReactionsOutputResponseTypeDef",
    {
        "reactionsForComment": List["ReactionForCommentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCommentsForComparedCommitInputTypeDef = TypedDict(
    "_RequiredGetCommentsForComparedCommitInputTypeDef",
    {
        "repositoryName": str,
        "afterCommitId": str,
    },
)
_OptionalGetCommentsForComparedCommitInputTypeDef = TypedDict(
    "_OptionalGetCommentsForComparedCommitInputTypeDef",
    {
        "beforeCommitId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetCommentsForComparedCommitInputTypeDef(
    _RequiredGetCommentsForComparedCommitInputTypeDef,
    _OptionalGetCommentsForComparedCommitInputTypeDef,
):
    pass


GetCommentsForComparedCommitOutputResponseTypeDef = TypedDict(
    "GetCommentsForComparedCommitOutputResponseTypeDef",
    {
        "commentsForComparedCommitData": List["CommentsForComparedCommitTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCommentsForPullRequestInputTypeDef = TypedDict(
    "_RequiredGetCommentsForPullRequestInputTypeDef",
    {
        "pullRequestId": str,
    },
)
_OptionalGetCommentsForPullRequestInputTypeDef = TypedDict(
    "_OptionalGetCommentsForPullRequestInputTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetCommentsForPullRequestInputTypeDef(
    _RequiredGetCommentsForPullRequestInputTypeDef, _OptionalGetCommentsForPullRequestInputTypeDef
):
    pass


GetCommentsForPullRequestOutputResponseTypeDef = TypedDict(
    "GetCommentsForPullRequestOutputResponseTypeDef",
    {
        "commentsForPullRequestData": List["CommentsForPullRequestTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCommitInputTypeDef = TypedDict(
    "GetCommitInputTypeDef",
    {
        "repositoryName": str,
        "commitId": str,
    },
)

GetCommitOutputResponseTypeDef = TypedDict(
    "GetCommitOutputResponseTypeDef",
    {
        "commit": "CommitTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDifferencesInputTypeDef = TypedDict(
    "_RequiredGetDifferencesInputTypeDef",
    {
        "repositoryName": str,
        "afterCommitSpecifier": str,
    },
)
_OptionalGetDifferencesInputTypeDef = TypedDict(
    "_OptionalGetDifferencesInputTypeDef",
    {
        "beforeCommitSpecifier": str,
        "beforePath": str,
        "afterPath": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetDifferencesInputTypeDef(
    _RequiredGetDifferencesInputTypeDef, _OptionalGetDifferencesInputTypeDef
):
    pass


GetDifferencesOutputResponseTypeDef = TypedDict(
    "GetDifferencesOutputResponseTypeDef",
    {
        "differences": List["DifferenceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFileInputTypeDef = TypedDict(
    "_RequiredGetFileInputTypeDef",
    {
        "repositoryName": str,
        "filePath": str,
    },
)
_OptionalGetFileInputTypeDef = TypedDict(
    "_OptionalGetFileInputTypeDef",
    {
        "commitSpecifier": str,
    },
    total=False,
)


class GetFileInputTypeDef(_RequiredGetFileInputTypeDef, _OptionalGetFileInputTypeDef):
    pass


GetFileOutputResponseTypeDef = TypedDict(
    "GetFileOutputResponseTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "filePath": str,
        "fileMode": FileModeTypeEnumType,
        "fileSize": int,
        "fileContent": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFolderInputTypeDef = TypedDict(
    "_RequiredGetFolderInputTypeDef",
    {
        "repositoryName": str,
        "folderPath": str,
    },
)
_OptionalGetFolderInputTypeDef = TypedDict(
    "_OptionalGetFolderInputTypeDef",
    {
        "commitSpecifier": str,
    },
    total=False,
)


class GetFolderInputTypeDef(_RequiredGetFolderInputTypeDef, _OptionalGetFolderInputTypeDef):
    pass


GetFolderOutputResponseTypeDef = TypedDict(
    "GetFolderOutputResponseTypeDef",
    {
        "commitId": str,
        "folderPath": str,
        "treeId": str,
        "subFolders": List["FolderTypeDef"],
        "files": List["FileTypeDef"],
        "symbolicLinks": List["SymbolicLinkTypeDef"],
        "subModules": List["SubModuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMergeCommitInputTypeDef = TypedDict(
    "_RequiredGetMergeCommitInputTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
    },
)
_OptionalGetMergeCommitInputTypeDef = TypedDict(
    "_OptionalGetMergeCommitInputTypeDef",
    {
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
    },
    total=False,
)


class GetMergeCommitInputTypeDef(
    _RequiredGetMergeCommitInputTypeDef, _OptionalGetMergeCommitInputTypeDef
):
    pass


GetMergeCommitOutputResponseTypeDef = TypedDict(
    "GetMergeCommitOutputResponseTypeDef",
    {
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
        "mergedCommitId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMergeConflictsInputTypeDef = TypedDict(
    "_RequiredGetMergeConflictsInputTypeDef",
    {
        "repositoryName": str,
        "destinationCommitSpecifier": str,
        "sourceCommitSpecifier": str,
        "mergeOption": MergeOptionTypeEnumType,
    },
)
_OptionalGetMergeConflictsInputTypeDef = TypedDict(
    "_OptionalGetMergeConflictsInputTypeDef",
    {
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "maxConflictFiles": int,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
        "nextToken": str,
    },
    total=False,
)


class GetMergeConflictsInputTypeDef(
    _RequiredGetMergeConflictsInputTypeDef, _OptionalGetMergeConflictsInputTypeDef
):
    pass


GetMergeConflictsOutputResponseTypeDef = TypedDict(
    "GetMergeConflictsOutputResponseTypeDef",
    {
        "mergeable": bool,
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
        "conflictMetadataList": List["ConflictMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMergeOptionsInputTypeDef = TypedDict(
    "_RequiredGetMergeOptionsInputTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
    },
)
_OptionalGetMergeOptionsInputTypeDef = TypedDict(
    "_OptionalGetMergeOptionsInputTypeDef",
    {
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
    },
    total=False,
)


class GetMergeOptionsInputTypeDef(
    _RequiredGetMergeOptionsInputTypeDef, _OptionalGetMergeOptionsInputTypeDef
):
    pass


GetMergeOptionsOutputResponseTypeDef = TypedDict(
    "GetMergeOptionsOutputResponseTypeDef",
    {
        "mergeOptions": List[MergeOptionTypeEnumType],
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPullRequestApprovalStatesInputTypeDef = TypedDict(
    "GetPullRequestApprovalStatesInputTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
    },
)

GetPullRequestApprovalStatesOutputResponseTypeDef = TypedDict(
    "GetPullRequestApprovalStatesOutputResponseTypeDef",
    {
        "approvals": List["ApprovalTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPullRequestInputTypeDef = TypedDict(
    "GetPullRequestInputTypeDef",
    {
        "pullRequestId": str,
    },
)

GetPullRequestOutputResponseTypeDef = TypedDict(
    "GetPullRequestOutputResponseTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPullRequestOverrideStateInputTypeDef = TypedDict(
    "GetPullRequestOverrideStateInputTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
    },
)

GetPullRequestOverrideStateOutputResponseTypeDef = TypedDict(
    "GetPullRequestOverrideStateOutputResponseTypeDef",
    {
        "overridden": bool,
        "overrider": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositoryInputTypeDef = TypedDict(
    "GetRepositoryInputTypeDef",
    {
        "repositoryName": str,
    },
)

GetRepositoryOutputResponseTypeDef = TypedDict(
    "GetRepositoryOutputResponseTypeDef",
    {
        "repositoryMetadata": "RepositoryMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositoryTriggersInputTypeDef = TypedDict(
    "GetRepositoryTriggersInputTypeDef",
    {
        "repositoryName": str,
    },
)

GetRepositoryTriggersOutputResponseTypeDef = TypedDict(
    "GetRepositoryTriggersOutputResponseTypeDef",
    {
        "configurationId": str,
        "triggers": List["RepositoryTriggerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IsBinaryFileTypeDef = TypedDict(
    "IsBinaryFileTypeDef",
    {
        "source": bool,
        "destination": bool,
        "base": bool,
    },
    total=False,
)

ListApprovalRuleTemplatesInputTypeDef = TypedDict(
    "ListApprovalRuleTemplatesInputTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListApprovalRuleTemplatesOutputResponseTypeDef = TypedDict(
    "ListApprovalRuleTemplatesOutputResponseTypeDef",
    {
        "approvalRuleTemplateNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssociatedApprovalRuleTemplatesForRepositoryInputTypeDef = TypedDict(
    "_RequiredListAssociatedApprovalRuleTemplatesForRepositoryInputTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalListAssociatedApprovalRuleTemplatesForRepositoryInputTypeDef = TypedDict(
    "_OptionalListAssociatedApprovalRuleTemplatesForRepositoryInputTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListAssociatedApprovalRuleTemplatesForRepositoryInputTypeDef(
    _RequiredListAssociatedApprovalRuleTemplatesForRepositoryInputTypeDef,
    _OptionalListAssociatedApprovalRuleTemplatesForRepositoryInputTypeDef,
):
    pass


ListAssociatedApprovalRuleTemplatesForRepositoryOutputResponseTypeDef = TypedDict(
    "ListAssociatedApprovalRuleTemplatesForRepositoryOutputResponseTypeDef",
    {
        "approvalRuleTemplateNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBranchesInputTypeDef = TypedDict(
    "_RequiredListBranchesInputTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalListBranchesInputTypeDef = TypedDict(
    "_OptionalListBranchesInputTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListBranchesInputTypeDef(
    _RequiredListBranchesInputTypeDef, _OptionalListBranchesInputTypeDef
):
    pass


ListBranchesOutputResponseTypeDef = TypedDict(
    "ListBranchesOutputResponseTypeDef",
    {
        "branches": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPullRequestsInputTypeDef = TypedDict(
    "_RequiredListPullRequestsInputTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalListPullRequestsInputTypeDef = TypedDict(
    "_OptionalListPullRequestsInputTypeDef",
    {
        "authorArn": str,
        "pullRequestStatus": PullRequestStatusEnumType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListPullRequestsInputTypeDef(
    _RequiredListPullRequestsInputTypeDef, _OptionalListPullRequestsInputTypeDef
):
    pass


ListPullRequestsOutputResponseTypeDef = TypedDict(
    "ListPullRequestsOutputResponseTypeDef",
    {
        "pullRequestIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRepositoriesForApprovalRuleTemplateInputTypeDef = TypedDict(
    "_RequiredListRepositoriesForApprovalRuleTemplateInputTypeDef",
    {
        "approvalRuleTemplateName": str,
    },
)
_OptionalListRepositoriesForApprovalRuleTemplateInputTypeDef = TypedDict(
    "_OptionalListRepositoriesForApprovalRuleTemplateInputTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListRepositoriesForApprovalRuleTemplateInputTypeDef(
    _RequiredListRepositoriesForApprovalRuleTemplateInputTypeDef,
    _OptionalListRepositoriesForApprovalRuleTemplateInputTypeDef,
):
    pass


ListRepositoriesForApprovalRuleTemplateOutputResponseTypeDef = TypedDict(
    "ListRepositoriesForApprovalRuleTemplateOutputResponseTypeDef",
    {
        "repositoryNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositoriesInputTypeDef = TypedDict(
    "ListRepositoriesInputTypeDef",
    {
        "nextToken": str,
        "sortBy": SortByEnumType,
        "order": OrderEnumType,
    },
    total=False,
)

ListRepositoriesOutputResponseTypeDef = TypedDict(
    "ListRepositoriesOutputResponseTypeDef",
    {
        "repositories": List["RepositoryNameIdPairTypeDef"],
        "nextToken": str,
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
        "tags": Dict[str, str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "filePath": str,
        "filePosition": int,
        "relativeFileVersion": RelativeFileVersionEnumType,
    },
    total=False,
)

_RequiredMergeBranchesByFastForwardInputTypeDef = TypedDict(
    "_RequiredMergeBranchesByFastForwardInputTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
    },
)
_OptionalMergeBranchesByFastForwardInputTypeDef = TypedDict(
    "_OptionalMergeBranchesByFastForwardInputTypeDef",
    {
        "targetBranch": str,
    },
    total=False,
)


class MergeBranchesByFastForwardInputTypeDef(
    _RequiredMergeBranchesByFastForwardInputTypeDef, _OptionalMergeBranchesByFastForwardInputTypeDef
):
    pass


MergeBranchesByFastForwardOutputResponseTypeDef = TypedDict(
    "MergeBranchesByFastForwardOutputResponseTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMergeBranchesBySquashInputTypeDef = TypedDict(
    "_RequiredMergeBranchesBySquashInputTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
    },
)
_OptionalMergeBranchesBySquashInputTypeDef = TypedDict(
    "_OptionalMergeBranchesBySquashInputTypeDef",
    {
        "targetBranch": str,
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
        "authorName": str,
        "email": str,
        "commitMessage": str,
        "keepEmptyFolders": bool,
        "conflictResolution": "ConflictResolutionTypeDef",
    },
    total=False,
)


class MergeBranchesBySquashInputTypeDef(
    _RequiredMergeBranchesBySquashInputTypeDef, _OptionalMergeBranchesBySquashInputTypeDef
):
    pass


MergeBranchesBySquashOutputResponseTypeDef = TypedDict(
    "MergeBranchesBySquashOutputResponseTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMergeBranchesByThreeWayInputTypeDef = TypedDict(
    "_RequiredMergeBranchesByThreeWayInputTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
    },
)
_OptionalMergeBranchesByThreeWayInputTypeDef = TypedDict(
    "_OptionalMergeBranchesByThreeWayInputTypeDef",
    {
        "targetBranch": str,
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
        "authorName": str,
        "email": str,
        "commitMessage": str,
        "keepEmptyFolders": bool,
        "conflictResolution": "ConflictResolutionTypeDef",
    },
    total=False,
)


class MergeBranchesByThreeWayInputTypeDef(
    _RequiredMergeBranchesByThreeWayInputTypeDef, _OptionalMergeBranchesByThreeWayInputTypeDef
):
    pass


MergeBranchesByThreeWayOutputResponseTypeDef = TypedDict(
    "MergeBranchesByThreeWayOutputResponseTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MergeHunkDetailTypeDef = TypedDict(
    "MergeHunkDetailTypeDef",
    {
        "startLine": int,
        "endLine": int,
        "hunkContent": str,
    },
    total=False,
)

MergeHunkTypeDef = TypedDict(
    "MergeHunkTypeDef",
    {
        "isConflict": bool,
        "source": "MergeHunkDetailTypeDef",
        "destination": "MergeHunkDetailTypeDef",
        "base": "MergeHunkDetailTypeDef",
    },
    total=False,
)

MergeMetadataTypeDef = TypedDict(
    "MergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": MergeOptionTypeEnumType,
    },
    total=False,
)

MergeOperationsTypeDef = TypedDict(
    "MergeOperationsTypeDef",
    {
        "source": ChangeTypeEnumType,
        "destination": ChangeTypeEnumType,
    },
    total=False,
)

_RequiredMergePullRequestByFastForwardInputTypeDef = TypedDict(
    "_RequiredMergePullRequestByFastForwardInputTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
    },
)
_OptionalMergePullRequestByFastForwardInputTypeDef = TypedDict(
    "_OptionalMergePullRequestByFastForwardInputTypeDef",
    {
        "sourceCommitId": str,
    },
    total=False,
)


class MergePullRequestByFastForwardInputTypeDef(
    _RequiredMergePullRequestByFastForwardInputTypeDef,
    _OptionalMergePullRequestByFastForwardInputTypeDef,
):
    pass


MergePullRequestByFastForwardOutputResponseTypeDef = TypedDict(
    "MergePullRequestByFastForwardOutputResponseTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMergePullRequestBySquashInputTypeDef = TypedDict(
    "_RequiredMergePullRequestBySquashInputTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
    },
)
_OptionalMergePullRequestBySquashInputTypeDef = TypedDict(
    "_OptionalMergePullRequestBySquashInputTypeDef",
    {
        "sourceCommitId": str,
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
        "commitMessage": str,
        "authorName": str,
        "email": str,
        "keepEmptyFolders": bool,
        "conflictResolution": "ConflictResolutionTypeDef",
    },
    total=False,
)


class MergePullRequestBySquashInputTypeDef(
    _RequiredMergePullRequestBySquashInputTypeDef, _OptionalMergePullRequestBySquashInputTypeDef
):
    pass


MergePullRequestBySquashOutputResponseTypeDef = TypedDict(
    "MergePullRequestBySquashOutputResponseTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMergePullRequestByThreeWayInputTypeDef = TypedDict(
    "_RequiredMergePullRequestByThreeWayInputTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
    },
)
_OptionalMergePullRequestByThreeWayInputTypeDef = TypedDict(
    "_OptionalMergePullRequestByThreeWayInputTypeDef",
    {
        "sourceCommitId": str,
        "conflictDetailLevel": ConflictDetailLevelTypeEnumType,
        "conflictResolutionStrategy": ConflictResolutionStrategyTypeEnumType,
        "commitMessage": str,
        "authorName": str,
        "email": str,
        "keepEmptyFolders": bool,
        "conflictResolution": "ConflictResolutionTypeDef",
    },
    total=False,
)


class MergePullRequestByThreeWayInputTypeDef(
    _RequiredMergePullRequestByThreeWayInputTypeDef, _OptionalMergePullRequestByThreeWayInputTypeDef
):
    pass


MergePullRequestByThreeWayOutputResponseTypeDef = TypedDict(
    "MergePullRequestByThreeWayOutputResponseTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ObjectTypesTypeDef = TypedDict(
    "ObjectTypesTypeDef",
    {
        "source": ObjectTypeEnumType,
        "destination": ObjectTypeEnumType,
        "base": ObjectTypeEnumType,
    },
    total=False,
)

OriginApprovalRuleTemplateTypeDef = TypedDict(
    "OriginApprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": str,
        "approvalRuleTemplateName": str,
    },
    total=False,
)

OverridePullRequestApprovalRulesInputTypeDef = TypedDict(
    "OverridePullRequestApprovalRulesInputTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
        "overrideStatus": OverrideStatusType,
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

_RequiredPostCommentForComparedCommitInputTypeDef = TypedDict(
    "_RequiredPostCommentForComparedCommitInputTypeDef",
    {
        "repositoryName": str,
        "afterCommitId": str,
        "content": str,
    },
)
_OptionalPostCommentForComparedCommitInputTypeDef = TypedDict(
    "_OptionalPostCommentForComparedCommitInputTypeDef",
    {
        "beforeCommitId": str,
        "location": "LocationTypeDef",
        "clientRequestToken": str,
    },
    total=False,
)


class PostCommentForComparedCommitInputTypeDef(
    _RequiredPostCommentForComparedCommitInputTypeDef,
    _OptionalPostCommentForComparedCommitInputTypeDef,
):
    pass


PostCommentForComparedCommitOutputResponseTypeDef = TypedDict(
    "PostCommentForComparedCommitOutputResponseTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": "LocationTypeDef",
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPostCommentForPullRequestInputTypeDef = TypedDict(
    "_RequiredPostCommentForPullRequestInputTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "content": str,
    },
)
_OptionalPostCommentForPullRequestInputTypeDef = TypedDict(
    "_OptionalPostCommentForPullRequestInputTypeDef",
    {
        "location": "LocationTypeDef",
        "clientRequestToken": str,
    },
    total=False,
)


class PostCommentForPullRequestInputTypeDef(
    _RequiredPostCommentForPullRequestInputTypeDef, _OptionalPostCommentForPullRequestInputTypeDef
):
    pass


PostCommentForPullRequestOutputResponseTypeDef = TypedDict(
    "PostCommentForPullRequestOutputResponseTypeDef",
    {
        "repositoryName": str,
        "pullRequestId": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": "LocationTypeDef",
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPostCommentReplyInputTypeDef = TypedDict(
    "_RequiredPostCommentReplyInputTypeDef",
    {
        "inReplyTo": str,
        "content": str,
    },
)
_OptionalPostCommentReplyInputTypeDef = TypedDict(
    "_OptionalPostCommentReplyInputTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)


class PostCommentReplyInputTypeDef(
    _RequiredPostCommentReplyInputTypeDef, _OptionalPostCommentReplyInputTypeDef
):
    pass


PostCommentReplyOutputResponseTypeDef = TypedDict(
    "PostCommentReplyOutputResponseTypeDef",
    {
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PullRequestCreatedEventMetadataTypeDef = TypedDict(
    "PullRequestCreatedEventMetadataTypeDef",
    {
        "repositoryName": str,
        "sourceCommitId": str,
        "destinationCommitId": str,
        "mergeBase": str,
    },
    total=False,
)

PullRequestEventTypeDef = TypedDict(
    "PullRequestEventTypeDef",
    {
        "pullRequestId": str,
        "eventDate": datetime,
        "pullRequestEventType": PullRequestEventTypeType,
        "actorArn": str,
        "pullRequestCreatedEventMetadata": "PullRequestCreatedEventMetadataTypeDef",
        "pullRequestStatusChangedEventMetadata": "PullRequestStatusChangedEventMetadataTypeDef",
        "pullRequestSourceReferenceUpdatedEventMetadata": "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
        "pullRequestMergedStateChangedEventMetadata": "PullRequestMergedStateChangedEventMetadataTypeDef",
        "approvalRuleEventMetadata": "ApprovalRuleEventMetadataTypeDef",
        "approvalStateChangedEventMetadata": "ApprovalStateChangedEventMetadataTypeDef",
        "approvalRuleOverriddenEventMetadata": "ApprovalRuleOverriddenEventMetadataTypeDef",
    },
    total=False,
)

PullRequestMergedStateChangedEventMetadataTypeDef = TypedDict(
    "PullRequestMergedStateChangedEventMetadataTypeDef",
    {
        "repositoryName": str,
        "destinationReference": str,
        "mergeMetadata": "MergeMetadataTypeDef",
    },
    total=False,
)

PullRequestSourceReferenceUpdatedEventMetadataTypeDef = TypedDict(
    "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "mergeBase": str,
    },
    total=False,
)

PullRequestStatusChangedEventMetadataTypeDef = TypedDict(
    "PullRequestStatusChangedEventMetadataTypeDef",
    {
        "pullRequestStatus": PullRequestStatusEnumType,
    },
    total=False,
)

PullRequestTargetTypeDef = TypedDict(
    "PullRequestTargetTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": "MergeMetadataTypeDef",
    },
    total=False,
)

PullRequestTypeDef = TypedDict(
    "PullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": PullRequestStatusEnumType,
        "authorArn": str,
        "pullRequestTargets": List["PullRequestTargetTypeDef"],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List["ApprovalRuleTypeDef"],
    },
    total=False,
)

PutCommentReactionInputTypeDef = TypedDict(
    "PutCommentReactionInputTypeDef",
    {
        "commentId": str,
        "reactionValue": str,
    },
)

_RequiredPutFileEntryTypeDef = TypedDict(
    "_RequiredPutFileEntryTypeDef",
    {
        "filePath": str,
    },
)
_OptionalPutFileEntryTypeDef = TypedDict(
    "_OptionalPutFileEntryTypeDef",
    {
        "fileMode": FileModeTypeEnumType,
        "fileContent": Union[bytes, IO[bytes], StreamingBody],
        "sourceFile": "SourceFileSpecifierTypeDef",
    },
    total=False,
)


class PutFileEntryTypeDef(_RequiredPutFileEntryTypeDef, _OptionalPutFileEntryTypeDef):
    pass


_RequiredPutFileInputTypeDef = TypedDict(
    "_RequiredPutFileInputTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
        "fileContent": Union[bytes, IO[bytes], StreamingBody],
        "filePath": str,
    },
)
_OptionalPutFileInputTypeDef = TypedDict(
    "_OptionalPutFileInputTypeDef",
    {
        "fileMode": FileModeTypeEnumType,
        "parentCommitId": str,
        "commitMessage": str,
        "name": str,
        "email": str,
    },
    total=False,
)


class PutFileInputTypeDef(_RequiredPutFileInputTypeDef, _OptionalPutFileInputTypeDef):
    pass


PutFileOutputResponseTypeDef = TypedDict(
    "PutFileOutputResponseTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRepositoryTriggersInputTypeDef = TypedDict(
    "PutRepositoryTriggersInputTypeDef",
    {
        "repositoryName": str,
        "triggers": List["RepositoryTriggerTypeDef"],
    },
)

PutRepositoryTriggersOutputResponseTypeDef = TypedDict(
    "PutRepositoryTriggersOutputResponseTypeDef",
    {
        "configurationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReactionForCommentTypeDef = TypedDict(
    "ReactionForCommentTypeDef",
    {
        "reaction": "ReactionValueFormatsTypeDef",
        "reactionUsers": List[str],
        "reactionsFromDeletedUsersCount": int,
    },
    total=False,
)

ReactionValueFormatsTypeDef = TypedDict(
    "ReactionValueFormatsTypeDef",
    {
        "emoji": str,
        "shortCode": str,
        "unicode": str,
    },
    total=False,
)

_RequiredReplaceContentEntryTypeDef = TypedDict(
    "_RequiredReplaceContentEntryTypeDef",
    {
        "filePath": str,
        "replacementType": ReplacementTypeEnumType,
    },
)
_OptionalReplaceContentEntryTypeDef = TypedDict(
    "_OptionalReplaceContentEntryTypeDef",
    {
        "content": Union[bytes, IO[bytes], StreamingBody],
        "fileMode": FileModeTypeEnumType,
    },
    total=False,
)


class ReplaceContentEntryTypeDef(
    _RequiredReplaceContentEntryTypeDef, _OptionalReplaceContentEntryTypeDef
):
    pass


RepositoryMetadataTypeDef = TypedDict(
    "RepositoryMetadataTypeDef",
    {
        "accountId": str,
        "repositoryId": str,
        "repositoryName": str,
        "repositoryDescription": str,
        "defaultBranch": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "cloneUrlHttp": str,
        "cloneUrlSsh": str,
        "Arn": str,
    },
    total=False,
)

RepositoryNameIdPairTypeDef = TypedDict(
    "RepositoryNameIdPairTypeDef",
    {
        "repositoryName": str,
        "repositoryId": str,
    },
    total=False,
)

RepositoryTriggerExecutionFailureTypeDef = TypedDict(
    "RepositoryTriggerExecutionFailureTypeDef",
    {
        "trigger": str,
        "failureMessage": str,
    },
    total=False,
)

_RequiredRepositoryTriggerTypeDef = TypedDict(
    "_RequiredRepositoryTriggerTypeDef",
    {
        "name": str,
        "destinationArn": str,
        "events": List[RepositoryTriggerEventEnumType],
    },
)
_OptionalRepositoryTriggerTypeDef = TypedDict(
    "_OptionalRepositoryTriggerTypeDef",
    {
        "customData": str,
        "branches": List[str],
    },
    total=False,
)


class RepositoryTriggerTypeDef(
    _RequiredRepositoryTriggerTypeDef, _OptionalRepositoryTriggerTypeDef
):
    pass


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

SetFileModeEntryTypeDef = TypedDict(
    "SetFileModeEntryTypeDef",
    {
        "filePath": str,
        "fileMode": FileModeTypeEnumType,
    },
)

_RequiredSourceFileSpecifierTypeDef = TypedDict(
    "_RequiredSourceFileSpecifierTypeDef",
    {
        "filePath": str,
    },
)
_OptionalSourceFileSpecifierTypeDef = TypedDict(
    "_OptionalSourceFileSpecifierTypeDef",
    {
        "isMove": bool,
    },
    total=False,
)


class SourceFileSpecifierTypeDef(
    _RequiredSourceFileSpecifierTypeDef, _OptionalSourceFileSpecifierTypeDef
):
    pass


SubModuleTypeDef = TypedDict(
    "SubModuleTypeDef",
    {
        "commitId": str,
        "absolutePath": str,
        "relativePath": str,
    },
    total=False,
)

SymbolicLinkTypeDef = TypedDict(
    "SymbolicLinkTypeDef",
    {
        "blobId": str,
        "absolutePath": str,
        "relativePath": str,
        "fileMode": FileModeTypeEnumType,
    },
    total=False,
)

TagResourceInputTypeDef = TypedDict(
    "TagResourceInputTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

_RequiredTargetTypeDef = TypedDict(
    "_RequiredTargetTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
    },
)
_OptionalTargetTypeDef = TypedDict(
    "_OptionalTargetTypeDef",
    {
        "destinationReference": str,
    },
    total=False,
)


class TargetTypeDef(_RequiredTargetTypeDef, _OptionalTargetTypeDef):
    pass


TestRepositoryTriggersInputTypeDef = TypedDict(
    "TestRepositoryTriggersInputTypeDef",
    {
        "repositoryName": str,
        "triggers": List["RepositoryTriggerTypeDef"],
    },
)

TestRepositoryTriggersOutputResponseTypeDef = TypedDict(
    "TestRepositoryTriggersOutputResponseTypeDef",
    {
        "successfulExecutions": List[str],
        "failedExecutions": List["RepositoryTriggerExecutionFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceInputTypeDef = TypedDict(
    "UntagResourceInputTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateApprovalRuleTemplateContentInputTypeDef = TypedDict(
    "_RequiredUpdateApprovalRuleTemplateContentInputTypeDef",
    {
        "approvalRuleTemplateName": str,
        "newRuleContent": str,
    },
)
_OptionalUpdateApprovalRuleTemplateContentInputTypeDef = TypedDict(
    "_OptionalUpdateApprovalRuleTemplateContentInputTypeDef",
    {
        "existingRuleContentSha256": str,
    },
    total=False,
)


class UpdateApprovalRuleTemplateContentInputTypeDef(
    _RequiredUpdateApprovalRuleTemplateContentInputTypeDef,
    _OptionalUpdateApprovalRuleTemplateContentInputTypeDef,
):
    pass


UpdateApprovalRuleTemplateContentOutputResponseTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateContentOutputResponseTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApprovalRuleTemplateDescriptionInputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateDescriptionInputTypeDef",
    {
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateDescription": str,
    },
)

UpdateApprovalRuleTemplateDescriptionOutputResponseTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateDescriptionOutputResponseTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApprovalRuleTemplateNameInputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateNameInputTypeDef",
    {
        "oldApprovalRuleTemplateName": str,
        "newApprovalRuleTemplateName": str,
    },
)

UpdateApprovalRuleTemplateNameOutputResponseTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateNameOutputResponseTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCommentInputTypeDef = TypedDict(
    "UpdateCommentInputTypeDef",
    {
        "commentId": str,
        "content": str,
    },
)

UpdateCommentOutputResponseTypeDef = TypedDict(
    "UpdateCommentOutputResponseTypeDef",
    {
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDefaultBranchInputTypeDef = TypedDict(
    "UpdateDefaultBranchInputTypeDef",
    {
        "repositoryName": str,
        "defaultBranchName": str,
    },
)

_RequiredUpdatePullRequestApprovalRuleContentInputTypeDef = TypedDict(
    "_RequiredUpdatePullRequestApprovalRuleContentInputTypeDef",
    {
        "pullRequestId": str,
        "approvalRuleName": str,
        "newRuleContent": str,
    },
)
_OptionalUpdatePullRequestApprovalRuleContentInputTypeDef = TypedDict(
    "_OptionalUpdatePullRequestApprovalRuleContentInputTypeDef",
    {
        "existingRuleContentSha256": str,
    },
    total=False,
)


class UpdatePullRequestApprovalRuleContentInputTypeDef(
    _RequiredUpdatePullRequestApprovalRuleContentInputTypeDef,
    _OptionalUpdatePullRequestApprovalRuleContentInputTypeDef,
):
    pass


UpdatePullRequestApprovalRuleContentOutputResponseTypeDef = TypedDict(
    "UpdatePullRequestApprovalRuleContentOutputResponseTypeDef",
    {
        "approvalRule": "ApprovalRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePullRequestApprovalStateInputTypeDef = TypedDict(
    "UpdatePullRequestApprovalStateInputTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
        "approvalState": ApprovalStateType,
    },
)

UpdatePullRequestDescriptionInputTypeDef = TypedDict(
    "UpdatePullRequestDescriptionInputTypeDef",
    {
        "pullRequestId": str,
        "description": str,
    },
)

UpdatePullRequestDescriptionOutputResponseTypeDef = TypedDict(
    "UpdatePullRequestDescriptionOutputResponseTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePullRequestStatusInputTypeDef = TypedDict(
    "UpdatePullRequestStatusInputTypeDef",
    {
        "pullRequestId": str,
        "pullRequestStatus": PullRequestStatusEnumType,
    },
)

UpdatePullRequestStatusOutputResponseTypeDef = TypedDict(
    "UpdatePullRequestStatusOutputResponseTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePullRequestTitleInputTypeDef = TypedDict(
    "UpdatePullRequestTitleInputTypeDef",
    {
        "pullRequestId": str,
        "title": str,
    },
)

UpdatePullRequestTitleOutputResponseTypeDef = TypedDict(
    "UpdatePullRequestTitleOutputResponseTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRepositoryDescriptionInputTypeDef = TypedDict(
    "_RequiredUpdateRepositoryDescriptionInputTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalUpdateRepositoryDescriptionInputTypeDef = TypedDict(
    "_OptionalUpdateRepositoryDescriptionInputTypeDef",
    {
        "repositoryDescription": str,
    },
    total=False,
)


class UpdateRepositoryDescriptionInputTypeDef(
    _RequiredUpdateRepositoryDescriptionInputTypeDef,
    _OptionalUpdateRepositoryDescriptionInputTypeDef,
):
    pass


UpdateRepositoryNameInputTypeDef = TypedDict(
    "UpdateRepositoryNameInputTypeDef",
    {
        "oldName": str,
        "newName": str,
    },
)

UserInfoTypeDef = TypedDict(
    "UserInfoTypeDef",
    {
        "name": str,
        "email": str,
        "date": str,
    },
    total=False,
)
