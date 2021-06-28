"""
Type annotations for codeguru-reviewer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codeguru_reviewer.type_defs import AssociateRepositoryRequestTypeDef

    data: AssociateRepositoryRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

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
    "AssociateRepositoryRequestTypeDef",
    "AssociateRepositoryResponseResponseTypeDef",
    "BranchDiffSourceCodeTypeTypeDef",
    "CodeArtifactsTypeDef",
    "CodeCommitRepositoryTypeDef",
    "CodeReviewSummaryTypeDef",
    "CodeReviewTypeDef",
    "CodeReviewTypeTypeDef",
    "CommitDiffSourceCodeTypeTypeDef",
    "CreateCodeReviewRequestTypeDef",
    "CreateCodeReviewResponseResponseTypeDef",
    "DescribeCodeReviewRequestTypeDef",
    "DescribeCodeReviewResponseResponseTypeDef",
    "DescribeRecommendationFeedbackRequestTypeDef",
    "DescribeRecommendationFeedbackResponseResponseTypeDef",
    "DescribeRepositoryAssociationRequestTypeDef",
    "DescribeRepositoryAssociationResponseResponseTypeDef",
    "DisassociateRepositoryRequestTypeDef",
    "DisassociateRepositoryResponseResponseTypeDef",
    "EventInfoTypeDef",
    "KMSKeyDetailsTypeDef",
    "ListCodeReviewsRequestTypeDef",
    "ListCodeReviewsResponseResponseTypeDef",
    "ListRecommendationFeedbackRequestTypeDef",
    "ListRecommendationFeedbackResponseResponseTypeDef",
    "ListRecommendationsRequestTypeDef",
    "ListRecommendationsResponseResponseTypeDef",
    "ListRepositoryAssociationsRequestTypeDef",
    "ListRepositoryAssociationsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MetricsSummaryTypeDef",
    "MetricsTypeDef",
    "PaginatorConfigTypeDef",
    "PutRecommendationFeedbackRequestTypeDef",
    "RecommendationFeedbackSummaryTypeDef",
    "RecommendationFeedbackTypeDef",
    "RecommendationSummaryTypeDef",
    "RepositoryAnalysisTypeDef",
    "RepositoryAssociationSummaryTypeDef",
    "RepositoryAssociationTypeDef",
    "RepositoryHeadSourceCodeTypeTypeDef",
    "RepositoryTypeDef",
    "RequestMetadataTypeDef",
    "ResponseMetadataTypeDef",
    "S3BucketRepositoryTypeDef",
    "S3RepositoryDetailsTypeDef",
    "S3RepositoryTypeDef",
    "SourceCodeTypeTypeDef",
    "TagResourceRequestTypeDef",
    "ThirdPartySourceRepositoryTypeDef",
    "UntagResourceRequestTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAssociateRepositoryRequestTypeDef = TypedDict(
    "_RequiredAssociateRepositoryRequestTypeDef",
    {
        "Repository": "RepositoryTypeDef",
    },
)
_OptionalAssociateRepositoryRequestTypeDef = TypedDict(
    "_OptionalAssociateRepositoryRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": Dict[str, str],
        "KMSKeyDetails": "KMSKeyDetailsTypeDef",
    },
    total=False,
)


class AssociateRepositoryRequestTypeDef(
    _RequiredAssociateRepositoryRequestTypeDef, _OptionalAssociateRepositoryRequestTypeDef
):
    pass


AssociateRepositoryResponseResponseTypeDef = TypedDict(
    "AssociateRepositoryResponseResponseTypeDef",
    {
        "RepositoryAssociation": "RepositoryAssociationTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredCreateCodeReviewRequestTypeDef = TypedDict(
    "_RequiredCreateCodeReviewRequestTypeDef",
    {
        "Name": str,
        "RepositoryAssociationArn": str,
        "Type": "CodeReviewTypeTypeDef",
    },
)
_OptionalCreateCodeReviewRequestTypeDef = TypedDict(
    "_OptionalCreateCodeReviewRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)


class CreateCodeReviewRequestTypeDef(
    _RequiredCreateCodeReviewRequestTypeDef, _OptionalCreateCodeReviewRequestTypeDef
):
    pass


CreateCodeReviewResponseResponseTypeDef = TypedDict(
    "CreateCodeReviewResponseResponseTypeDef",
    {
        "CodeReview": "CodeReviewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCodeReviewRequestTypeDef = TypedDict(
    "DescribeCodeReviewRequestTypeDef",
    {
        "CodeReviewArn": str,
    },
)

DescribeCodeReviewResponseResponseTypeDef = TypedDict(
    "DescribeCodeReviewResponseResponseTypeDef",
    {
        "CodeReview": "CodeReviewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRecommendationFeedbackRequestTypeDef = TypedDict(
    "_RequiredDescribeRecommendationFeedbackRequestTypeDef",
    {
        "CodeReviewArn": str,
        "RecommendationId": str,
    },
)
_OptionalDescribeRecommendationFeedbackRequestTypeDef = TypedDict(
    "_OptionalDescribeRecommendationFeedbackRequestTypeDef",
    {
        "UserId": str,
    },
    total=False,
)


class DescribeRecommendationFeedbackRequestTypeDef(
    _RequiredDescribeRecommendationFeedbackRequestTypeDef,
    _OptionalDescribeRecommendationFeedbackRequestTypeDef,
):
    pass


DescribeRecommendationFeedbackResponseResponseTypeDef = TypedDict(
    "DescribeRecommendationFeedbackResponseResponseTypeDef",
    {
        "RecommendationFeedback": "RecommendationFeedbackTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRepositoryAssociationRequestTypeDef = TypedDict(
    "DescribeRepositoryAssociationRequestTypeDef",
    {
        "AssociationArn": str,
    },
)

DescribeRepositoryAssociationResponseResponseTypeDef = TypedDict(
    "DescribeRepositoryAssociationResponseResponseTypeDef",
    {
        "RepositoryAssociation": "RepositoryAssociationTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateRepositoryRequestTypeDef = TypedDict(
    "DisassociateRepositoryRequestTypeDef",
    {
        "AssociationArn": str,
    },
)

DisassociateRepositoryResponseResponseTypeDef = TypedDict(
    "DisassociateRepositoryResponseResponseTypeDef",
    {
        "RepositoryAssociation": "RepositoryAssociationTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredListCodeReviewsRequestTypeDef = TypedDict(
    "_RequiredListCodeReviewsRequestTypeDef",
    {
        "Type": TypeType,
    },
)
_OptionalListCodeReviewsRequestTypeDef = TypedDict(
    "_OptionalListCodeReviewsRequestTypeDef",
    {
        "ProviderTypes": List[ProviderTypeType],
        "States": List[JobStateType],
        "RepositoryNames": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListCodeReviewsRequestTypeDef(
    _RequiredListCodeReviewsRequestTypeDef, _OptionalListCodeReviewsRequestTypeDef
):
    pass


ListCodeReviewsResponseResponseTypeDef = TypedDict(
    "ListCodeReviewsResponseResponseTypeDef",
    {
        "CodeReviewSummaries": List["CodeReviewSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecommendationFeedbackRequestTypeDef = TypedDict(
    "_RequiredListRecommendationFeedbackRequestTypeDef",
    {
        "CodeReviewArn": str,
    },
)
_OptionalListRecommendationFeedbackRequestTypeDef = TypedDict(
    "_OptionalListRecommendationFeedbackRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "UserIds": List[str],
        "RecommendationIds": List[str],
    },
    total=False,
)


class ListRecommendationFeedbackRequestTypeDef(
    _RequiredListRecommendationFeedbackRequestTypeDef,
    _OptionalListRecommendationFeedbackRequestTypeDef,
):
    pass


ListRecommendationFeedbackResponseResponseTypeDef = TypedDict(
    "ListRecommendationFeedbackResponseResponseTypeDef",
    {
        "RecommendationFeedbackSummaries": List["RecommendationFeedbackSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecommendationsRequestTypeDef = TypedDict(
    "_RequiredListRecommendationsRequestTypeDef",
    {
        "CodeReviewArn": str,
    },
)
_OptionalListRecommendationsRequestTypeDef = TypedDict(
    "_OptionalListRecommendationsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListRecommendationsRequestTypeDef(
    _RequiredListRecommendationsRequestTypeDef, _OptionalListRecommendationsRequestTypeDef
):
    pass


ListRecommendationsResponseResponseTypeDef = TypedDict(
    "ListRecommendationsResponseResponseTypeDef",
    {
        "RecommendationSummaries": List["RecommendationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositoryAssociationsRequestTypeDef = TypedDict(
    "ListRepositoryAssociationsRequestTypeDef",
    {
        "ProviderTypes": List[ProviderTypeType],
        "States": List[RepositoryAssociationStateType],
        "Names": List[str],
        "Owners": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListRepositoryAssociationsResponseResponseTypeDef = TypedDict(
    "ListRepositoryAssociationsResponseResponseTypeDef",
    {
        "RepositoryAssociationSummaries": List["RepositoryAssociationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

PutRecommendationFeedbackRequestTypeDef = TypedDict(
    "PutRecommendationFeedbackRequestTypeDef",
    {
        "CodeReviewArn": str,
        "RecommendationId": str,
        "Reactions": List[ReactionType],
    },
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "Tags": Dict[str, str],
    },
)

ThirdPartySourceRepositoryTypeDef = TypedDict(
    "ThirdPartySourceRepositoryTypeDef",
    {
        "Name": str,
        "ConnectionArn": str,
        "Owner": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "TagKeys": List[str],
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
