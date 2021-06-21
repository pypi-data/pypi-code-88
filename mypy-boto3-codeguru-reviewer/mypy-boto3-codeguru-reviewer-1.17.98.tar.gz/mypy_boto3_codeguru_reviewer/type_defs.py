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
    EncryptionOptionType,
    JobStateType,
    ProviderTypeType,
    ReactionType,
    RepositoryAssociationStateType,
    TypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateRepositoryResponseTypeDef",
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
    "SourceCodeTypeTypeDef",
    "ThirdPartySourceRepositoryTypeDef",
)

AssociateRepositoryResponseTypeDef = TypedDict(
    "AssociateRepositoryResponseTypeDef",
    {
        "RepositoryAssociation": "RepositoryAssociationTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

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
    },
    total=False,
)

CodeReviewTypeTypeDef = TypedDict(
    "CodeReviewTypeTypeDef",
    {
        "RepositoryAnalysis": "RepositoryAnalysisTypeDef",
    },
)

CommitDiffSourceCodeTypeTypeDef = TypedDict(
    "CommitDiffSourceCodeTypeTypeDef",
    {
        "SourceCommit": str,
        "DestinationCommit": str,
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
    },
    total=False,
)

RepositoryAnalysisTypeDef = TypedDict(
    "RepositoryAnalysisTypeDef",
    {
        "RepositoryHead": "RepositoryHeadSourceCodeTypeTypeDef",
    },
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
    },
    total=False,
)

SourceCodeTypeTypeDef = TypedDict(
    "SourceCodeTypeTypeDef",
    {
        "CommitDiff": "CommitDiffSourceCodeTypeTypeDef",
        "RepositoryHead": "RepositoryHeadSourceCodeTypeTypeDef",
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
