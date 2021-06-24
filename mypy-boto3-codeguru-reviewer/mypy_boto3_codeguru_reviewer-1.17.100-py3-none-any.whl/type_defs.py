"""
Type annotations for codeguru-reviewer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codeguru_reviewer.type_defs import AssociateRepositoryResponseTypeDef

    data: AssociateRepositoryResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from .literals import (
    AnalysisTypeType,
    EncryptionOptionType,
    JobStateType,
    ProviderTypeType,
    ReactionType,
    RecommendationCategoryType,
    RepositoryAssociationStateType,
    TypeType,
    VendorNameType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateRepositoryResponseTypeDef",
    "BranchDiffSourceCodeTypeTypeDef",
    "CodeArtifactsTypeDef",
    "CodeCommitRepositoryTypeDef",
    "CodeReviewSummaryTypeDef",
    "CodeReviewTypeDef",
    "CodeReviewTypeTypeDef",
    "CommitDiffSourceCodeTypeTypeDef",
    "CreateCodeReviewResponseTypeDef",
    "DescribeCodeReviewResponseTypeDef",
    "DescribeRecommendationFeedbackResponseTypeDef",
    "DescribeRepositoryAssociationResponseTypeDef",
    "DisassociateRepositoryResponseTypeDef",
    "EventInfoTypeDef",
    "KMSKeyDetailsTypeDef",
    "ListCodeReviewsResponseTypeDef",
    "ListRecommendationFeedbackResponseTypeDef",
    "ListRecommendationsResponseTypeDef",
    "ListRepositoryAssociationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricsSummaryTypeDef",
    "MetricsTypeDef",
    "PaginatorConfigTypeDef",
    "RecommendationFeedbackSummaryTypeDef",
    "RecommendationFeedbackTypeDef",
    "RecommendationSummaryTypeDef",
    "RepositoryAnalysisTypeDef",
    "RepositoryAssociationSummaryTypeDef",
    "RepositoryAssociationTypeDef",
    "RepositoryHeadSourceCodeTypeTypeDef",
    "RepositoryTypeDef",
    "RequestMetadataTypeDef",
    "S3BucketRepositoryTypeDef",
    "S3RepositoryDetailsTypeDef",
    "S3RepositoryTypeDef",
    "SourceCodeTypeTypeDef",
    "ThirdPartySourceRepositoryTypeDef",
    "WaiterConfigTypeDef",
)

AssociateRepositoryResponseTypeDef = TypedDict(
    "AssociateRepositoryResponseTypeDef",
    {
        "RepositoryAssociation": "RepositoryAssociationTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

BranchDiffSourceCodeTypeTypeDef = TypedDict(
    "BranchDiffSourceCodeTypeTypeDef",
    {
        "SourceBranchName": str,
        "DestinationBranchName": str,
    },
)

_RequiredCodeArtifactsTypeDef = TypedDict(
    "_RequiredCodeArtifactsTypeDef",
    {
        "SourceCodeArtifactsObjectKey": str,
    },
)
_OptionalCodeArtifactsTypeDef = TypedDict(
    "_OptionalCodeArtifactsTypeDef",
    {
        "BuildArtifactsObjectKey": str,
    },
    total=False,
)


class CodeArtifactsTypeDef(_RequiredCodeArtifactsTypeDef, _OptionalCodeArtifactsTypeDef):
    pass


CodeCommitRepositoryTypeDef = TypedDict(
    "CodeCommitRepositoryTypeDef",
    {
        "Name": str,
    },
)

CodeReviewSummaryTypeDef = TypedDict(
    "CodeReviewSummaryTypeDef",
    {
        "Name": str,
        "CodeReviewArn": str,
        "RepositoryName": str,
        "Owner": str,
        "ProviderType": ProviderTypeType,
        "State": JobStateType,
        "CreatedTimeStamp": datetime,
        "LastUpdatedTimeStamp": datetime,
        "Type": TypeType,
        "PullRequestId": str,
        "MetricsSummary": "MetricsSummaryTypeDef",
        "SourceCodeType": "SourceCodeTypeTypeDef",
    },
    total=False,
)

CodeReviewTypeDef = TypedDict(
    "CodeReviewTypeDef",
    {
        "Name": str,
        "CodeReviewArn": str,
        "RepositoryName": str,
        "Owner": str,
        "ProviderType": ProviderTypeType,
        "State": JobStateType,
        "StateReason": str,
        "CreatedTimeStamp": datetime,
        "LastUpdatedTimeStamp": datetime,
        "Type": TypeType,
        "PullRequestId": str,
        "SourceCodeType": "SourceCodeTypeTypeDef",
        "AssociationArn": str,
        "Metrics": "MetricsTypeDef",
        "AnalysisTypes": List[AnalysisTypeType],
    },
    total=False,
)

_RequiredCodeReviewTypeTypeDef = TypedDict(
    "_RequiredCodeReviewTypeTypeDef",
    {
        "RepositoryAnalysis": "RepositoryAnalysisTypeDef",
    },
)
_OptionalCodeReviewTypeTypeDef = TypedDict(
    "_OptionalCodeReviewTypeTypeDef",
    {
        "AnalysisTypes": List[AnalysisTypeType],
    },
    total=False,
)


class CodeReviewTypeTypeDef(_RequiredCodeReviewTypeTypeDef, _OptionalCodeReviewTypeTypeDef):
    pass


CommitDiffSourceCodeTypeTypeDef = TypedDict(
    "CommitDiffSourceCodeTypeTypeDef",
    {
        "SourceCommit": str,
        "DestinationCommit": str,
        "MergeBaseCommit": str,
    },
    total=False,
)

CreateCodeReviewResponseTypeDef = TypedDict(
    "CreateCodeReviewResponseTypeDef",
    {
        "CodeReview": "CodeReviewTypeDef",
    },
    total=False,
)

DescribeCodeReviewResponseTypeDef = TypedDict(
    "DescribeCodeReviewResponseTypeDef",
    {
        "CodeReview": "CodeReviewTypeDef",
    },
    total=False,
)

DescribeRecommendationFeedbackResponseTypeDef = TypedDict(
    "DescribeRecommendationFeedbackResponseTypeDef",
    {
        "RecommendationFeedback": "RecommendationFeedbackTypeDef",
    },
    total=False,
)

DescribeRepositoryAssociationResponseTypeDef = TypedDict(
    "DescribeRepositoryAssociationResponseTypeDef",
    {
        "RepositoryAssociation": "RepositoryAssociationTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

DisassociateRepositoryResponseTypeDef = TypedDict(
    "DisassociateRepositoryResponseTypeDef",
    {
        "RepositoryAssociation": "RepositoryAssociationTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

EventInfoTypeDef = TypedDict(
    "EventInfoTypeDef",
    {
        "Name": str,
        "State": str,
    },
    total=False,
)

KMSKeyDetailsTypeDef = TypedDict(
    "KMSKeyDetailsTypeDef",
    {
        "KMSKeyId": str,
        "EncryptionOption": EncryptionOptionType,
    },
    total=False,
)

ListCodeReviewsResponseTypeDef = TypedDict(
    "ListCodeReviewsResponseTypeDef",
    {
        "CodeReviewSummaries": List["CodeReviewSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListRecommendationFeedbackResponseTypeDef = TypedDict(
    "ListRecommendationFeedbackResponseTypeDef",
    {
        "RecommendationFeedbackSummaries": List["RecommendationFeedbackSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {
        "RecommendationSummaries": List["RecommendationSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListRepositoryAssociationsResponseTypeDef = TypedDict(
    "ListRepositoryAssociationsResponseTypeDef",
    {
        "RepositoryAssociationSummaries": List["RepositoryAssociationSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

MetricsSummaryTypeDef = TypedDict(
    "MetricsSummaryTypeDef",
    {
        "MeteredLinesOfCodeCount": int,
        "FindingsCount": int,
    },
    total=False,
)

MetricsTypeDef = TypedDict(
    "MetricsTypeDef",
    {
        "MeteredLinesOfCodeCount": int,
        "FindingsCount": int,
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

RecommendationFeedbackSummaryTypeDef = TypedDict(
    "RecommendationFeedbackSummaryTypeDef",
    {
        "RecommendationId": str,
        "Reactions": List[ReactionType],
        "UserId": str,
    },
    total=False,
)

RecommendationFeedbackTypeDef = TypedDict(
    "RecommendationFeedbackTypeDef",
    {
        "CodeReviewArn": str,
        "RecommendationId": str,
        "Reactions": List[ReactionType],
        "UserId": str,
        "CreatedTimeStamp": datetime,
        "LastUpdatedTimeStamp": datetime,
    },
    total=False,
)

RecommendationSummaryTypeDef = TypedDict(
    "RecommendationSummaryTypeDef",
    {
        "FilePath": str,
        "RecommendationId": str,
        "StartLine": int,
        "EndLine": int,
        "Description": str,
        "RecommendationCategory": RecommendationCategoryType,
    },
    total=False,
)

RepositoryAnalysisTypeDef = TypedDict(
    "RepositoryAnalysisTypeDef",
    {
        "RepositoryHead": "RepositoryHeadSourceCodeTypeTypeDef",
        "SourceCodeType": "SourceCodeTypeTypeDef",
    },
    total=False,
)

RepositoryAssociationSummaryTypeDef = TypedDict(
    "RepositoryAssociationSummaryTypeDef",
    {
        "AssociationArn": str,
        "ConnectionArn": str,
        "LastUpdatedTimeStamp": datetime,
        "AssociationId": str,
        "Name": str,
        "Owner": str,
        "ProviderType": ProviderTypeType,
        "State": RepositoryAssociationStateType,
    },
    total=False,
)

RepositoryAssociationTypeDef = TypedDict(
    "RepositoryAssociationTypeDef",
    {
        "AssociationId": str,
        "AssociationArn": str,
        "ConnectionArn": str,
        "Name": str,
        "Owner": str,
        "ProviderType": ProviderTypeType,
        "State": RepositoryAssociationStateType,
        "StateReason": str,
        "LastUpdatedTimeStamp": datetime,
        "CreatedTimeStamp": datetime,
        "KMSKeyDetails": "KMSKeyDetailsTypeDef",
        "S3RepositoryDetails": "S3RepositoryDetailsTypeDef",
    },
    total=False,
)

RepositoryHeadSourceCodeTypeTypeDef = TypedDict(
    "RepositoryHeadSourceCodeTypeTypeDef",
    {
        "BranchName": str,
    },
)

RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "CodeCommit": "CodeCommitRepositoryTypeDef",
        "Bitbucket": "ThirdPartySourceRepositoryTypeDef",
        "GitHubEnterpriseServer": "ThirdPartySourceRepositoryTypeDef",
        "S3Bucket": "S3RepositoryTypeDef",
    },
    total=False,
)

RequestMetadataTypeDef = TypedDict(
    "RequestMetadataTypeDef",
    {
        "RequestId": str,
        "Requester": str,
        "EventInfo": "EventInfoTypeDef",
        "VendorName": VendorNameType,
    },
    total=False,
)

_RequiredS3BucketRepositoryTypeDef = TypedDict(
    "_RequiredS3BucketRepositoryTypeDef",
    {
        "Name": str,
    },
)
_OptionalS3BucketRepositoryTypeDef = TypedDict(
    "_OptionalS3BucketRepositoryTypeDef",
    {
        "Details": "S3RepositoryDetailsTypeDef",
    },
    total=False,
)


class S3BucketRepositoryTypeDef(
    _RequiredS3BucketRepositoryTypeDef, _OptionalS3BucketRepositoryTypeDef
):
    pass


S3RepositoryDetailsTypeDef = TypedDict(
    "S3RepositoryDetailsTypeDef",
    {
        "BucketName": str,
        "CodeArtifacts": "CodeArtifactsTypeDef",
    },
    total=False,
)

S3RepositoryTypeDef = TypedDict(
    "S3RepositoryTypeDef",
    {
        "Name": str,
        "BucketName": str,
    },
)

SourceCodeTypeTypeDef = TypedDict(
    "SourceCodeTypeTypeDef",
    {
        "CommitDiff": "CommitDiffSourceCodeTypeTypeDef",
        "RepositoryHead": "RepositoryHeadSourceCodeTypeTypeDef",
        "BranchDiff": "BranchDiffSourceCodeTypeTypeDef",
        "S3BucketRepository": "S3BucketRepositoryTypeDef",
        "RequestMetadata": "RequestMetadataTypeDef",
    },
    total=False,
)

ThirdPartySourceRepositoryTypeDef = TypedDict(
    "ThirdPartySourceRepositoryTypeDef",
    {
        "Name": str,
        "ConnectionArn": str,
        "Owner": str,
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
