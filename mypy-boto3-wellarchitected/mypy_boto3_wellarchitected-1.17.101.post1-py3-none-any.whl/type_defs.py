"""
Type annotations for wellarchitected service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/type_defs.html)

Usage::

    ```python
    from mypy_boto3_wellarchitected.type_defs import AnswerSummaryTypeDef

    data: AnswerSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    DifferenceStatusType,
    LensStatusType,
    NotificationTypeType,
    PermissionTypeType,
    RiskType,
    ShareInvitationActionType,
    ShareStatusType,
    WorkloadEnvironmentType,
    WorkloadImprovementStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AnswerSummaryTypeDef",
    "AnswerTypeDef",
    "AssociateLensesInputTypeDef",
    "ChoiceTypeDef",
    "CreateMilestoneInputTypeDef",
    "CreateMilestoneOutputResponseTypeDef",
    "CreateWorkloadInputTypeDef",
    "CreateWorkloadOutputResponseTypeDef",
    "CreateWorkloadShareInputTypeDef",
    "CreateWorkloadShareOutputResponseTypeDef",
    "DeleteWorkloadInputTypeDef",
    "DeleteWorkloadShareInputTypeDef",
    "DisassociateLensesInputTypeDef",
    "GetAnswerInputTypeDef",
    "GetAnswerOutputResponseTypeDef",
    "GetLensReviewInputTypeDef",
    "GetLensReviewOutputResponseTypeDef",
    "GetLensReviewReportInputTypeDef",
    "GetLensReviewReportOutputResponseTypeDef",
    "GetLensVersionDifferenceInputTypeDef",
    "GetLensVersionDifferenceOutputResponseTypeDef",
    "GetMilestoneInputTypeDef",
    "GetMilestoneOutputResponseTypeDef",
    "GetWorkloadInputTypeDef",
    "GetWorkloadOutputResponseTypeDef",
    "ImprovementSummaryTypeDef",
    "LensReviewReportTypeDef",
    "LensReviewSummaryTypeDef",
    "LensReviewTypeDef",
    "LensSummaryTypeDef",
    "LensUpgradeSummaryTypeDef",
    "ListAnswersInputTypeDef",
    "ListAnswersOutputResponseTypeDef",
    "ListLensReviewImprovementsInputTypeDef",
    "ListLensReviewImprovementsOutputResponseTypeDef",
    "ListLensReviewsInputTypeDef",
    "ListLensReviewsOutputResponseTypeDef",
    "ListLensesInputTypeDef",
    "ListLensesOutputResponseTypeDef",
    "ListMilestonesInputTypeDef",
    "ListMilestonesOutputResponseTypeDef",
    "ListNotificationsInputTypeDef",
    "ListNotificationsOutputResponseTypeDef",
    "ListShareInvitationsInputTypeDef",
    "ListShareInvitationsOutputResponseTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputResponseTypeDef",
    "ListWorkloadSharesInputTypeDef",
    "ListWorkloadSharesOutputResponseTypeDef",
    "ListWorkloadsInputTypeDef",
    "ListWorkloadsOutputResponseTypeDef",
    "MilestoneSummaryTypeDef",
    "MilestoneTypeDef",
    "NotificationSummaryTypeDef",
    "PillarDifferenceTypeDef",
    "PillarReviewSummaryTypeDef",
    "QuestionDifferenceTypeDef",
    "ResponseMetadataTypeDef",
    "ShareInvitationSummaryTypeDef",
    "ShareInvitationTypeDef",
    "TagResourceInputTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateAnswerInputTypeDef",
    "UpdateAnswerOutputResponseTypeDef",
    "UpdateLensReviewInputTypeDef",
    "UpdateLensReviewOutputResponseTypeDef",
    "UpdateShareInvitationInputTypeDef",
    "UpdateShareInvitationOutputResponseTypeDef",
    "UpdateWorkloadInputTypeDef",
    "UpdateWorkloadOutputResponseTypeDef",
    "UpdateWorkloadShareInputTypeDef",
    "UpdateWorkloadShareOutputResponseTypeDef",
    "UpgradeLensReviewInputTypeDef",
    "VersionDifferencesTypeDef",
    "WorkloadShareSummaryTypeDef",
    "WorkloadShareTypeDef",
    "WorkloadSummaryTypeDef",
    "WorkloadTypeDef",
)

AnswerSummaryTypeDef = TypedDict(
    "AnswerSummaryTypeDef",
    {
        "QuestionId": str,
        "PillarId": str,
        "QuestionTitle": str,
        "Choices": List["ChoiceTypeDef"],
        "SelectedChoices": List[str],
        "IsApplicable": bool,
        "Risk": RiskType,
    },
    total=False,
)

AnswerTypeDef = TypedDict(
    "AnswerTypeDef",
    {
        "QuestionId": str,
        "PillarId": str,
        "QuestionTitle": str,
        "QuestionDescription": str,
        "ImprovementPlanUrl": str,
        "HelpfulResourceUrl": str,
        "Choices": List["ChoiceTypeDef"],
        "SelectedChoices": List[str],
        "IsApplicable": bool,
        "Risk": RiskType,
        "Notes": str,
    },
    total=False,
)

AssociateLensesInputTypeDef = TypedDict(
    "AssociateLensesInputTypeDef",
    {
        "WorkloadId": str,
        "LensAliases": List[str],
    },
)

ChoiceTypeDef = TypedDict(
    "ChoiceTypeDef",
    {
        "ChoiceId": str,
        "Title": str,
        "Description": str,
    },
    total=False,
)

CreateMilestoneInputTypeDef = TypedDict(
    "CreateMilestoneInputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneName": str,
        "ClientRequestToken": str,
    },
)

CreateMilestoneOutputResponseTypeDef = TypedDict(
    "CreateMilestoneOutputResponseTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkloadInputTypeDef = TypedDict(
    "_RequiredCreateWorkloadInputTypeDef",
    {
        "WorkloadName": str,
        "Description": str,
        "Environment": WorkloadEnvironmentType,
        "ReviewOwner": str,
        "Lenses": List[str],
        "ClientRequestToken": str,
    },
)
_OptionalCreateWorkloadInputTypeDef = TypedDict(
    "_OptionalCreateWorkloadInputTypeDef",
    {
        "AccountIds": List[str],
        "AwsRegions": List[str],
        "NonAwsRegions": List[str],
        "PillarPriorities": List[str],
        "ArchitecturalDesign": str,
        "IndustryType": str,
        "Industry": str,
        "Notes": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateWorkloadInputTypeDef(
    _RequiredCreateWorkloadInputTypeDef, _OptionalCreateWorkloadInputTypeDef
):
    pass


CreateWorkloadOutputResponseTypeDef = TypedDict(
    "CreateWorkloadOutputResponseTypeDef",
    {
        "WorkloadId": str,
        "WorkloadArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkloadShareInputTypeDef = TypedDict(
    "CreateWorkloadShareInputTypeDef",
    {
        "WorkloadId": str,
        "SharedWith": str,
        "PermissionType": PermissionTypeType,
        "ClientRequestToken": str,
    },
)

CreateWorkloadShareOutputResponseTypeDef = TypedDict(
    "CreateWorkloadShareOutputResponseTypeDef",
    {
        "WorkloadId": str,
        "ShareId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWorkloadInputTypeDef = TypedDict(
    "DeleteWorkloadInputTypeDef",
    {
        "WorkloadId": str,
        "ClientRequestToken": str,
    },
)

DeleteWorkloadShareInputTypeDef = TypedDict(
    "DeleteWorkloadShareInputTypeDef",
    {
        "ShareId": str,
        "WorkloadId": str,
        "ClientRequestToken": str,
    },
)

DisassociateLensesInputTypeDef = TypedDict(
    "DisassociateLensesInputTypeDef",
    {
        "WorkloadId": str,
        "LensAliases": List[str],
    },
)

_RequiredGetAnswerInputTypeDef = TypedDict(
    "_RequiredGetAnswerInputTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "QuestionId": str,
    },
)
_OptionalGetAnswerInputTypeDef = TypedDict(
    "_OptionalGetAnswerInputTypeDef",
    {
        "MilestoneNumber": int,
    },
    total=False,
)


class GetAnswerInputTypeDef(_RequiredGetAnswerInputTypeDef, _OptionalGetAnswerInputTypeDef):
    pass


GetAnswerOutputResponseTypeDef = TypedDict(
    "GetAnswerOutputResponseTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "Answer": "AnswerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLensReviewInputTypeDef = TypedDict(
    "_RequiredGetLensReviewInputTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
    },
)
_OptionalGetLensReviewInputTypeDef = TypedDict(
    "_OptionalGetLensReviewInputTypeDef",
    {
        "MilestoneNumber": int,
    },
    total=False,
)


class GetLensReviewInputTypeDef(
    _RequiredGetLensReviewInputTypeDef, _OptionalGetLensReviewInputTypeDef
):
    pass


GetLensReviewOutputResponseTypeDef = TypedDict(
    "GetLensReviewOutputResponseTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReview": "LensReviewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLensReviewReportInputTypeDef = TypedDict(
    "_RequiredGetLensReviewReportInputTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
    },
)
_OptionalGetLensReviewReportInputTypeDef = TypedDict(
    "_OptionalGetLensReviewReportInputTypeDef",
    {
        "MilestoneNumber": int,
    },
    total=False,
)


class GetLensReviewReportInputTypeDef(
    _RequiredGetLensReviewReportInputTypeDef, _OptionalGetLensReviewReportInputTypeDef
):
    pass


GetLensReviewReportOutputResponseTypeDef = TypedDict(
    "GetLensReviewReportOutputResponseTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReviewReport": "LensReviewReportTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLensVersionDifferenceInputTypeDef = TypedDict(
    "GetLensVersionDifferenceInputTypeDef",
    {
        "LensAlias": str,
        "BaseLensVersion": str,
    },
)

GetLensVersionDifferenceOutputResponseTypeDef = TypedDict(
    "GetLensVersionDifferenceOutputResponseTypeDef",
    {
        "LensAlias": str,
        "BaseLensVersion": str,
        "LatestLensVersion": str,
        "VersionDifferences": "VersionDifferencesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMilestoneInputTypeDef = TypedDict(
    "GetMilestoneInputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
    },
)

GetMilestoneOutputResponseTypeDef = TypedDict(
    "GetMilestoneOutputResponseTypeDef",
    {
        "WorkloadId": str,
        "Milestone": "MilestoneTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkloadInputTypeDef = TypedDict(
    "GetWorkloadInputTypeDef",
    {
        "WorkloadId": str,
    },
)

GetWorkloadOutputResponseTypeDef = TypedDict(
    "GetWorkloadOutputResponseTypeDef",
    {
        "Workload": "WorkloadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImprovementSummaryTypeDef = TypedDict(
    "ImprovementSummaryTypeDef",
    {
        "QuestionId": str,
        "PillarId": str,
        "QuestionTitle": str,
        "Risk": RiskType,
        "ImprovementPlanUrl": str,
    },
    total=False,
)

LensReviewReportTypeDef = TypedDict(
    "LensReviewReportTypeDef",
    {
        "LensAlias": str,
        "Base64String": str,
    },
    total=False,
)

LensReviewSummaryTypeDef = TypedDict(
    "LensReviewSummaryTypeDef",
    {
        "LensAlias": str,
        "LensVersion": str,
        "LensName": str,
        "LensStatus": LensStatusType,
        "UpdatedAt": datetime,
        "RiskCounts": Dict[RiskType, int],
    },
    total=False,
)

LensReviewTypeDef = TypedDict(
    "LensReviewTypeDef",
    {
        "LensAlias": str,
        "LensVersion": str,
        "LensName": str,
        "LensStatus": LensStatusType,
        "PillarReviewSummaries": List["PillarReviewSummaryTypeDef"],
        "UpdatedAt": datetime,
        "Notes": str,
        "RiskCounts": Dict[RiskType, int],
        "NextToken": str,
    },
    total=False,
)

LensSummaryTypeDef = TypedDict(
    "LensSummaryTypeDef",
    {
        "LensAlias": str,
        "LensVersion": str,
        "LensName": str,
        "Description": str,
    },
    total=False,
)

LensUpgradeSummaryTypeDef = TypedDict(
    "LensUpgradeSummaryTypeDef",
    {
        "WorkloadId": str,
        "WorkloadName": str,
        "LensAlias": str,
        "CurrentLensVersion": str,
        "LatestLensVersion": str,
    },
    total=False,
)

_RequiredListAnswersInputTypeDef = TypedDict(
    "_RequiredListAnswersInputTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
    },
)
_OptionalListAnswersInputTypeDef = TypedDict(
    "_OptionalListAnswersInputTypeDef",
    {
        "PillarId": str,
        "MilestoneNumber": int,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAnswersInputTypeDef(_RequiredListAnswersInputTypeDef, _OptionalListAnswersInputTypeDef):
    pass


ListAnswersOutputResponseTypeDef = TypedDict(
    "ListAnswersOutputResponseTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "AnswerSummaries": List["AnswerSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLensReviewImprovementsInputTypeDef = TypedDict(
    "_RequiredListLensReviewImprovementsInputTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
    },
)
_OptionalListLensReviewImprovementsInputTypeDef = TypedDict(
    "_OptionalListLensReviewImprovementsInputTypeDef",
    {
        "PillarId": str,
        "MilestoneNumber": int,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListLensReviewImprovementsInputTypeDef(
    _RequiredListLensReviewImprovementsInputTypeDef, _OptionalListLensReviewImprovementsInputTypeDef
):
    pass


ListLensReviewImprovementsOutputResponseTypeDef = TypedDict(
    "ListLensReviewImprovementsOutputResponseTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "ImprovementSummaries": List["ImprovementSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLensReviewsInputTypeDef = TypedDict(
    "_RequiredListLensReviewsInputTypeDef",
    {
        "WorkloadId": str,
    },
)
_OptionalListLensReviewsInputTypeDef = TypedDict(
    "_OptionalListLensReviewsInputTypeDef",
    {
        "MilestoneNumber": int,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListLensReviewsInputTypeDef(
    _RequiredListLensReviewsInputTypeDef, _OptionalListLensReviewsInputTypeDef
):
    pass


ListLensReviewsOutputResponseTypeDef = TypedDict(
    "ListLensReviewsOutputResponseTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReviewSummaries": List["LensReviewSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLensesInputTypeDef = TypedDict(
    "ListLensesInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListLensesOutputResponseTypeDef = TypedDict(
    "ListLensesOutputResponseTypeDef",
    {
        "LensSummaries": List["LensSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMilestonesInputTypeDef = TypedDict(
    "_RequiredListMilestonesInputTypeDef",
    {
        "WorkloadId": str,
    },
)
_OptionalListMilestonesInputTypeDef = TypedDict(
    "_OptionalListMilestonesInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListMilestonesInputTypeDef(
    _RequiredListMilestonesInputTypeDef, _OptionalListMilestonesInputTypeDef
):
    pass


ListMilestonesOutputResponseTypeDef = TypedDict(
    "ListMilestonesOutputResponseTypeDef",
    {
        "WorkloadId": str,
        "MilestoneSummaries": List["MilestoneSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotificationsInputTypeDef = TypedDict(
    "ListNotificationsInputTypeDef",
    {
        "WorkloadId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListNotificationsOutputResponseTypeDef = TypedDict(
    "ListNotificationsOutputResponseTypeDef",
    {
        "NotificationSummaries": List["NotificationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListShareInvitationsInputTypeDef = TypedDict(
    "ListShareInvitationsInputTypeDef",
    {
        "WorkloadNamePrefix": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListShareInvitationsOutputResponseTypeDef = TypedDict(
    "ListShareInvitationsOutputResponseTypeDef",
    {
        "ShareInvitationSummaries": List["ShareInvitationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputTypeDef = TypedDict(
    "ListTagsForResourceInputTypeDef",
    {
        "WorkloadArn": str,
    },
)

ListTagsForResourceOutputResponseTypeDef = TypedDict(
    "ListTagsForResourceOutputResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWorkloadSharesInputTypeDef = TypedDict(
    "_RequiredListWorkloadSharesInputTypeDef",
    {
        "WorkloadId": str,
    },
)
_OptionalListWorkloadSharesInputTypeDef = TypedDict(
    "_OptionalListWorkloadSharesInputTypeDef",
    {
        "SharedWithPrefix": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListWorkloadSharesInputTypeDef(
    _RequiredListWorkloadSharesInputTypeDef, _OptionalListWorkloadSharesInputTypeDef
):
    pass


ListWorkloadSharesOutputResponseTypeDef = TypedDict(
    "ListWorkloadSharesOutputResponseTypeDef",
    {
        "WorkloadId": str,
        "WorkloadShareSummaries": List["WorkloadShareSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkloadsInputTypeDef = TypedDict(
    "ListWorkloadsInputTypeDef",
    {
        "WorkloadNamePrefix": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWorkloadsOutputResponseTypeDef = TypedDict(
    "ListWorkloadsOutputResponseTypeDef",
    {
        "WorkloadSummaries": List["WorkloadSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MilestoneSummaryTypeDef = TypedDict(
    "MilestoneSummaryTypeDef",
    {
        "MilestoneNumber": int,
        "MilestoneName": str,
        "RecordedAt": datetime,
        "WorkloadSummary": "WorkloadSummaryTypeDef",
    },
    total=False,
)

MilestoneTypeDef = TypedDict(
    "MilestoneTypeDef",
    {
        "MilestoneNumber": int,
        "MilestoneName": str,
        "RecordedAt": datetime,
        "Workload": "WorkloadTypeDef",
    },
    total=False,
)

NotificationSummaryTypeDef = TypedDict(
    "NotificationSummaryTypeDef",
    {
        "Type": NotificationTypeType,
        "LensUpgradeSummary": "LensUpgradeSummaryTypeDef",
    },
    total=False,
)

PillarDifferenceTypeDef = TypedDict(
    "PillarDifferenceTypeDef",
    {
        "PillarId": str,
        "DifferenceStatus": DifferenceStatusType,
        "QuestionDifferences": List["QuestionDifferenceTypeDef"],
    },
    total=False,
)

PillarReviewSummaryTypeDef = TypedDict(
    "PillarReviewSummaryTypeDef",
    {
        "PillarId": str,
        "PillarName": str,
        "Notes": str,
        "RiskCounts": Dict[RiskType, int],
    },
    total=False,
)

QuestionDifferenceTypeDef = TypedDict(
    "QuestionDifferenceTypeDef",
    {
        "QuestionId": str,
        "QuestionTitle": str,
        "DifferenceStatus": DifferenceStatusType,
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

ShareInvitationSummaryTypeDef = TypedDict(
    "ShareInvitationSummaryTypeDef",
    {
        "ShareInvitationId": str,
        "SharedBy": str,
        "SharedWith": str,
        "PermissionType": PermissionTypeType,
        "WorkloadName": str,
        "WorkloadId": str,
    },
    total=False,
)

ShareInvitationTypeDef = TypedDict(
    "ShareInvitationTypeDef",
    {
        "ShareInvitationId": str,
        "WorkloadId": str,
    },
    total=False,
)

TagResourceInputTypeDef = TypedDict(
    "TagResourceInputTypeDef",
    {
        "WorkloadArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceInputTypeDef = TypedDict(
    "UntagResourceInputTypeDef",
    {
        "WorkloadArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAnswerInputTypeDef = TypedDict(
    "_RequiredUpdateAnswerInputTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "QuestionId": str,
    },
)
_OptionalUpdateAnswerInputTypeDef = TypedDict(
    "_OptionalUpdateAnswerInputTypeDef",
    {
        "SelectedChoices": List[str],
        "Notes": str,
        "IsApplicable": bool,
    },
    total=False,
)


class UpdateAnswerInputTypeDef(
    _RequiredUpdateAnswerInputTypeDef, _OptionalUpdateAnswerInputTypeDef
):
    pass


UpdateAnswerOutputResponseTypeDef = TypedDict(
    "UpdateAnswerOutputResponseTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "Answer": "AnswerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateLensReviewInputTypeDef = TypedDict(
    "_RequiredUpdateLensReviewInputTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
    },
)
_OptionalUpdateLensReviewInputTypeDef = TypedDict(
    "_OptionalUpdateLensReviewInputTypeDef",
    {
        "LensNotes": str,
        "PillarNotes": Dict[str, str],
    },
    total=False,
)


class UpdateLensReviewInputTypeDef(
    _RequiredUpdateLensReviewInputTypeDef, _OptionalUpdateLensReviewInputTypeDef
):
    pass


UpdateLensReviewOutputResponseTypeDef = TypedDict(
    "UpdateLensReviewOutputResponseTypeDef",
    {
        "WorkloadId": str,
        "LensReview": "LensReviewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateShareInvitationInputTypeDef = TypedDict(
    "UpdateShareInvitationInputTypeDef",
    {
        "ShareInvitationId": str,
        "ShareInvitationAction": ShareInvitationActionType,
    },
)

UpdateShareInvitationOutputResponseTypeDef = TypedDict(
    "UpdateShareInvitationOutputResponseTypeDef",
    {
        "ShareInvitation": "ShareInvitationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWorkloadInputTypeDef = TypedDict(
    "_RequiredUpdateWorkloadInputTypeDef",
    {
        "WorkloadId": str,
    },
)
_OptionalUpdateWorkloadInputTypeDef = TypedDict(
    "_OptionalUpdateWorkloadInputTypeDef",
    {
        "WorkloadName": str,
        "Description": str,
        "Environment": WorkloadEnvironmentType,
        "AccountIds": List[str],
        "AwsRegions": List[str],
        "NonAwsRegions": List[str],
        "PillarPriorities": List[str],
        "ArchitecturalDesign": str,
        "ReviewOwner": str,
        "IsReviewOwnerUpdateAcknowledged": bool,
        "IndustryType": str,
        "Industry": str,
        "Notes": str,
        "ImprovementStatus": WorkloadImprovementStatusType,
    },
    total=False,
)


class UpdateWorkloadInputTypeDef(
    _RequiredUpdateWorkloadInputTypeDef, _OptionalUpdateWorkloadInputTypeDef
):
    pass


UpdateWorkloadOutputResponseTypeDef = TypedDict(
    "UpdateWorkloadOutputResponseTypeDef",
    {
        "Workload": "WorkloadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateWorkloadShareInputTypeDef = TypedDict(
    "UpdateWorkloadShareInputTypeDef",
    {
        "ShareId": str,
        "WorkloadId": str,
        "PermissionType": PermissionTypeType,
    },
)

UpdateWorkloadShareOutputResponseTypeDef = TypedDict(
    "UpdateWorkloadShareOutputResponseTypeDef",
    {
        "WorkloadId": str,
        "WorkloadShare": "WorkloadShareTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpgradeLensReviewInputTypeDef = TypedDict(
    "_RequiredUpgradeLensReviewInputTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "MilestoneName": str,
    },
)
_OptionalUpgradeLensReviewInputTypeDef = TypedDict(
    "_OptionalUpgradeLensReviewInputTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)


class UpgradeLensReviewInputTypeDef(
    _RequiredUpgradeLensReviewInputTypeDef, _OptionalUpgradeLensReviewInputTypeDef
):
    pass


VersionDifferencesTypeDef = TypedDict(
    "VersionDifferencesTypeDef",
    {
        "PillarDifferences": List["PillarDifferenceTypeDef"],
    },
    total=False,
)

WorkloadShareSummaryTypeDef = TypedDict(
    "WorkloadShareSummaryTypeDef",
    {
        "ShareId": str,
        "SharedWith": str,
        "PermissionType": PermissionTypeType,
        "Status": ShareStatusType,
    },
    total=False,
)

WorkloadShareTypeDef = TypedDict(
    "WorkloadShareTypeDef",
    {
        "ShareId": str,
        "SharedBy": str,
        "SharedWith": str,
        "PermissionType": PermissionTypeType,
        "Status": ShareStatusType,
        "WorkloadName": str,
        "WorkloadId": str,
    },
    total=False,
)

WorkloadSummaryTypeDef = TypedDict(
    "WorkloadSummaryTypeDef",
    {
        "WorkloadId": str,
        "WorkloadArn": str,
        "WorkloadName": str,
        "Owner": str,
        "UpdatedAt": datetime,
        "Lenses": List[str],
        "RiskCounts": Dict[RiskType, int],
        "ImprovementStatus": WorkloadImprovementStatusType,
    },
    total=False,
)

WorkloadTypeDef = TypedDict(
    "WorkloadTypeDef",
    {
        "WorkloadId": str,
        "WorkloadArn": str,
        "WorkloadName": str,
        "Description": str,
        "Environment": WorkloadEnvironmentType,
        "UpdatedAt": datetime,
        "AccountIds": List[str],
        "AwsRegions": List[str],
        "NonAwsRegions": List[str],
        "ArchitecturalDesign": str,
        "ReviewOwner": str,
        "ReviewRestrictionDate": datetime,
        "IsReviewOwnerUpdateAcknowledged": bool,
        "IndustryType": str,
        "Industry": str,
        "Notes": str,
        "ImprovementStatus": WorkloadImprovementStatusType,
        "RiskCounts": Dict[RiskType, int],
        "PillarPriorities": List[str],
        "Lenses": List[str],
        "Owner": str,
        "ShareInvitationId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)
