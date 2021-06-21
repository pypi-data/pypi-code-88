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

from .literals import (
    ApprovalStateType,
    ChangeTypeEnumType,
    FileModeTypeEnumType,
    MergeOptionTypeEnumType,
    ObjectTypeEnumType,
    OverrideStatusType,
    PullRequestEventTypeType,
    PullRequestStatusEnumType,
    RelativeFileVersionEnumType,
    ReplacementTypeEnumType,
    RepositoryTriggerEventEnumType,
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
    "BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef",
    "BatchDescribeMergeConflictsErrorTypeDef",
    "BatchDescribeMergeConflictsOutputTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef",
    "BatchGetCommitsErrorTypeDef",
    "BatchGetCommitsOutputTypeDef",
    "BatchGetRepositoriesOutputTypeDef",
    "BlobMetadataTypeDef",
    "BranchInfoTypeDef",
    "CommentTypeDef",
    "CommentsForComparedCommitTypeDef",
    "CommentsForPullRequestTypeDef",
    "CommitTypeDef",
    "ConflictMetadataTypeDef",
    "ConflictResolutionTypeDef",
    "ConflictTypeDef",
    "CreateApprovalRuleTemplateOutputTypeDef",
    "CreateCommitOutputTypeDef",
    "CreatePullRequestApprovalRuleOutputTypeDef",
    "CreatePullRequestOutputTypeDef",
    "CreateRepositoryOutputTypeDef",
    "CreateUnreferencedMergeCommitOutputTypeDef",
    "DeleteApprovalRuleTemplateOutputTypeDef",
    "DeleteBranchOutputTypeDef",
    "DeleteCommentContentOutputTypeDef",
    "DeleteFileEntryTypeDef",
    "DeleteFileOutputTypeDef",
    "DeletePullRequestApprovalRuleOutputTypeDef",
    "DeleteRepositoryOutputTypeDef",
    "DescribeMergeConflictsOutputTypeDef",
    "DescribePullRequestEventsOutputTypeDef",
    "DifferenceTypeDef",
    "EvaluatePullRequestApprovalRulesOutputTypeDef",
    "EvaluationTypeDef",
    "FileMetadataTypeDef",
    "FileModesTypeDef",
    "FileSizesTypeDef",
    "FileTypeDef",
    "FolderTypeDef",
    "GetApprovalRuleTemplateOutputTypeDef",
    "GetBlobOutputTypeDef",
    "GetBranchOutputTypeDef",
    "GetCommentOutputTypeDef",
    "GetCommentReactionsOutputTypeDef",
    "GetCommentsForComparedCommitOutputTypeDef",
    "GetCommentsForPullRequestOutputTypeDef",
    "GetCommitOutputTypeDef",
    "GetDifferencesOutputTypeDef",
    "GetFileOutputTypeDef",
    "GetFolderOutputTypeDef",
    "GetMergeCommitOutputTypeDef",
    "GetMergeConflictsOutputTypeDef",
    "GetMergeOptionsOutputTypeDef",
    "GetPullRequestApprovalStatesOutputTypeDef",
    "GetPullRequestOutputTypeDef",
    "GetPullRequestOverrideStateOutputTypeDef",
    "GetRepositoryOutputTypeDef",
    "GetRepositoryTriggersOutputTypeDef",
    "IsBinaryFileTypeDef",
    "ListApprovalRuleTemplatesOutputTypeDef",
    "ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef",
    "ListBranchesOutputTypeDef",
    "ListPullRequestsOutputTypeDef",
    "ListRepositoriesForApprovalRuleTemplateOutputTypeDef",
    "ListRepositoriesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LocationTypeDef",
    "MergeBranchesByFastForwardOutputTypeDef",
    "MergeBranchesBySquashOutputTypeDef",
    "MergeBranchesByThreeWayOutputTypeDef",
    "MergeHunkDetailTypeDef",
    "MergeHunkTypeDef",
    "MergeMetadataTypeDef",
    "MergeOperationsTypeDef",
    "MergePullRequestByFastForwardOutputTypeDef",
    "MergePullRequestBySquashOutputTypeDef",
    "MergePullRequestByThreeWayOutputTypeDef",
    "ObjectTypesTypeDef",
    "OriginApprovalRuleTemplateTypeDef",
    "PaginatorConfigTypeDef",
    "PostCommentForComparedCommitOutputTypeDef",
    "PostCommentForPullRequestOutputTypeDef",
    "PostCommentReplyOutputTypeDef",
    "PullRequestCreatedEventMetadataTypeDef",
    "PullRequestEventTypeDef",
    "PullRequestMergedStateChangedEventMetadataTypeDef",
    "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    "PullRequestStatusChangedEventMetadataTypeDef",
    "PullRequestTargetTypeDef",
    "PullRequestTypeDef",
    "PutFileEntryTypeDef",
    "PutFileOutputTypeDef",
    "PutRepositoryTriggersOutputTypeDef",
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
    "TargetTypeDef",
    "TestRepositoryTriggersOutputTypeDef",
    "UpdateApprovalRuleTemplateContentOutputTypeDef",
    "UpdateApprovalRuleTemplateDescriptionOutputTypeDef",
    "UpdateApprovalRuleTemplateNameOutputTypeDef",
    "UpdateCommentOutputTypeDef",
    "UpdatePullRequestApprovalRuleContentOutputTypeDef",
    "UpdatePullRequestDescriptionOutputTypeDef",
    "UpdatePullRequestStatusOutputTypeDef",
    "UpdatePullRequestTitleOutputTypeDef",
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

BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef = TypedDict(
    "BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef",
    {
        "repositoryName": str,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef = TypedDict(
    "BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef",
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

BatchDescribeMergeConflictsOutputTypeDef = TypedDict(
    "BatchDescribeMergeConflictsOutputTypeDef",
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

BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef = TypedDict(
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef",
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

BatchGetCommitsOutputTypeDef = TypedDict(
    "BatchGetCommitsOutputTypeDef",
    {
        "commits": List["CommitTypeDef"],
        "errors": List["BatchGetCommitsErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetRepositoriesOutputTypeDef = TypedDict(
    "BatchGetRepositoriesOutputTypeDef",
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

CreateApprovalRuleTemplateOutputTypeDef = TypedDict(
    "CreateApprovalRuleTemplateOutputTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCommitOutputTypeDef = TypedDict(
    "CreateCommitOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "filesAdded": List["FileMetadataTypeDef"],
        "filesUpdated": List["FileMetadataTypeDef"],
        "filesDeleted": List["FileMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePullRequestApprovalRuleOutputTypeDef = TypedDict(
    "CreatePullRequestApprovalRuleOutputTypeDef",
    {
        "approvalRule": "ApprovalRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePullRequestOutputTypeDef = TypedDict(
    "CreatePullRequestOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRepositoryOutputTypeDef = TypedDict(
    "CreateRepositoryOutputTypeDef",
    {
        "repositoryMetadata": "RepositoryMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUnreferencedMergeCommitOutputTypeDef = TypedDict(
    "CreateUnreferencedMergeCommitOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApprovalRuleTemplateOutputTypeDef = TypedDict(
    "DeleteApprovalRuleTemplateOutputTypeDef",
    {
        "approvalRuleTemplateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBranchOutputTypeDef = TypedDict(
    "DeleteBranchOutputTypeDef",
    {
        "deletedBranch": "BranchInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCommentContentOutputTypeDef = TypedDict(
    "DeleteCommentContentOutputTypeDef",
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

DeleteFileOutputTypeDef = TypedDict(
    "DeleteFileOutputTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "treeId": str,
        "filePath": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePullRequestApprovalRuleOutputTypeDef = TypedDict(
    "DeletePullRequestApprovalRuleOutputTypeDef",
    {
        "approvalRuleId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRepositoryOutputTypeDef = TypedDict(
    "DeleteRepositoryOutputTypeDef",
    {
        "repositoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMergeConflictsOutputTypeDef = TypedDict(
    "DescribeMergeConflictsOutputTypeDef",
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

DescribePullRequestEventsOutputTypeDef = TypedDict(
    "DescribePullRequestEventsOutputTypeDef",
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

EvaluatePullRequestApprovalRulesOutputTypeDef = TypedDict(
    "EvaluatePullRequestApprovalRulesOutputTypeDef",
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

GetApprovalRuleTemplateOutputTypeDef = TypedDict(
    "GetApprovalRuleTemplateOutputTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBlobOutputTypeDef = TypedDict(
    "GetBlobOutputTypeDef",
    {
        "content": Union[bytes, IO[bytes]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBranchOutputTypeDef = TypedDict(
    "GetBranchOutputTypeDef",
    {
        "branch": "BranchInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCommentOutputTypeDef = TypedDict(
    "GetCommentOutputTypeDef",
    {
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCommentReactionsOutputTypeDef = TypedDict(
    "GetCommentReactionsOutputTypeDef",
    {
        "reactionsForComment": List["ReactionForCommentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCommentsForComparedCommitOutputTypeDef = TypedDict(
    "GetCommentsForComparedCommitOutputTypeDef",
    {
        "commentsForComparedCommitData": List["CommentsForComparedCommitTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCommentsForPullRequestOutputTypeDef = TypedDict(
    "GetCommentsForPullRequestOutputTypeDef",
    {
        "commentsForPullRequestData": List["CommentsForPullRequestTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCommitOutputTypeDef = TypedDict(
    "GetCommitOutputTypeDef",
    {
        "commit": "CommitTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDifferencesOutputTypeDef = TypedDict(
    "GetDifferencesOutputTypeDef",
    {
        "differences": List["DifferenceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFileOutputTypeDef = TypedDict(
    "GetFileOutputTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "filePath": str,
        "fileMode": FileModeTypeEnumType,
        "fileSize": int,
        "fileContent": Union[bytes, IO[bytes]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFolderOutputTypeDef = TypedDict(
    "GetFolderOutputTypeDef",
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

GetMergeCommitOutputTypeDef = TypedDict(
    "GetMergeCommitOutputTypeDef",
    {
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
        "mergedCommitId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMergeConflictsOutputTypeDef = TypedDict(
    "GetMergeConflictsOutputTypeDef",
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

GetMergeOptionsOutputTypeDef = TypedDict(
    "GetMergeOptionsOutputTypeDef",
    {
        "mergeOptions": List[MergeOptionTypeEnumType],
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPullRequestApprovalStatesOutputTypeDef = TypedDict(
    "GetPullRequestApprovalStatesOutputTypeDef",
    {
        "approvals": List["ApprovalTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPullRequestOutputTypeDef = TypedDict(
    "GetPullRequestOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPullRequestOverrideStateOutputTypeDef = TypedDict(
    "GetPullRequestOverrideStateOutputTypeDef",
    {
        "overridden": bool,
        "overrider": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositoryOutputTypeDef = TypedDict(
    "GetRepositoryOutputTypeDef",
    {
        "repositoryMetadata": "RepositoryMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositoryTriggersOutputTypeDef = TypedDict(
    "GetRepositoryTriggersOutputTypeDef",
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

ListApprovalRuleTemplatesOutputTypeDef = TypedDict(
    "ListApprovalRuleTemplatesOutputTypeDef",
    {
        "approvalRuleTemplateNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef = TypedDict(
    "ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef",
    {
        "approvalRuleTemplateNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBranchesOutputTypeDef = TypedDict(
    "ListBranchesOutputTypeDef",
    {
        "branches": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPullRequestsOutputTypeDef = TypedDict(
    "ListPullRequestsOutputTypeDef",
    {
        "pullRequestIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositoriesForApprovalRuleTemplateOutputTypeDef = TypedDict(
    "ListRepositoriesForApprovalRuleTemplateOutputTypeDef",
    {
        "repositoryNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositoriesOutputTypeDef = TypedDict(
    "ListRepositoriesOutputTypeDef",
    {
        "repositories": List["RepositoryNameIdPairTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
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

MergeBranchesByFastForwardOutputTypeDef = TypedDict(
    "MergeBranchesByFastForwardOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MergeBranchesBySquashOutputTypeDef = TypedDict(
    "MergeBranchesBySquashOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MergeBranchesByThreeWayOutputTypeDef = TypedDict(
    "MergeBranchesByThreeWayOutputTypeDef",
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

MergePullRequestByFastForwardOutputTypeDef = TypedDict(
    "MergePullRequestByFastForwardOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MergePullRequestBySquashOutputTypeDef = TypedDict(
    "MergePullRequestBySquashOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MergePullRequestByThreeWayOutputTypeDef = TypedDict(
    "MergePullRequestByThreeWayOutputTypeDef",
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PostCommentForComparedCommitOutputTypeDef = TypedDict(
    "PostCommentForComparedCommitOutputTypeDef",
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

PostCommentForPullRequestOutputTypeDef = TypedDict(
    "PostCommentForPullRequestOutputTypeDef",
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

PostCommentReplyOutputTypeDef = TypedDict(
    "PostCommentReplyOutputTypeDef",
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
        "fileContent": Union[bytes, IO[bytes]],
        "sourceFile": "SourceFileSpecifierTypeDef",
    },
    total=False,
)


class PutFileEntryTypeDef(_RequiredPutFileEntryTypeDef, _OptionalPutFileEntryTypeDef):
    pass


PutFileOutputTypeDef = TypedDict(
    "PutFileOutputTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRepositoryTriggersOutputTypeDef = TypedDict(
    "PutRepositoryTriggersOutputTypeDef",
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
        "content": Union[bytes, IO[bytes]],
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


TestRepositoryTriggersOutputTypeDef = TypedDict(
    "TestRepositoryTriggersOutputTypeDef",
    {
        "successfulExecutions": List[str],
        "failedExecutions": List["RepositoryTriggerExecutionFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApprovalRuleTemplateContentOutputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateContentOutputTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApprovalRuleTemplateDescriptionOutputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateDescriptionOutputTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApprovalRuleTemplateNameOutputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateNameOutputTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCommentOutputTypeDef = TypedDict(
    "UpdateCommentOutputTypeDef",
    {
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePullRequestApprovalRuleContentOutputTypeDef = TypedDict(
    "UpdatePullRequestApprovalRuleContentOutputTypeDef",
    {
        "approvalRule": "ApprovalRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePullRequestDescriptionOutputTypeDef = TypedDict(
    "UpdatePullRequestDescriptionOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePullRequestStatusOutputTypeDef = TypedDict(
    "UpdatePullRequestStatusOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePullRequestTitleOutputTypeDef = TypedDict(
    "UpdatePullRequestTitleOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
