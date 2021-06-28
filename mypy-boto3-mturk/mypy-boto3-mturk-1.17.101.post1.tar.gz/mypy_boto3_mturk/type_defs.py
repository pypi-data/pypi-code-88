"""
Type annotations for mturk service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mturk.type_defs import AcceptQualificationRequestRequestTypeDef

    data: AcceptQualificationRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AssignmentStatusType,
    ComparatorType,
    EventTypeType,
    HITAccessActionsType,
    HITReviewStatusType,
    HITStatusType,
    NotificationTransportType,
    NotifyWorkersFailureCodeType,
    QualificationStatusType,
    QualificationTypeStatusType,
    ReviewableHITStatusType,
    ReviewActionStatusType,
    ReviewPolicyLevelType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptQualificationRequestRequestTypeDef",
    "ApproveAssignmentRequestTypeDef",
    "AssignmentTypeDef",
    "AssociateQualificationWithWorkerRequestTypeDef",
    "BonusPaymentTypeDef",
    "CreateAdditionalAssignmentsForHITRequestTypeDef",
    "CreateHITRequestTypeDef",
    "CreateHITResponseResponseTypeDef",
    "CreateHITTypeRequestTypeDef",
    "CreateHITTypeResponseResponseTypeDef",
    "CreateHITWithHITTypeRequestTypeDef",
    "CreateHITWithHITTypeResponseResponseTypeDef",
    "CreateQualificationTypeRequestTypeDef",
    "CreateQualificationTypeResponseResponseTypeDef",
    "CreateWorkerBlockRequestTypeDef",
    "DeleteHITRequestTypeDef",
    "DeleteQualificationTypeRequestTypeDef",
    "DeleteWorkerBlockRequestTypeDef",
    "DisassociateQualificationFromWorkerRequestTypeDef",
    "GetAccountBalanceResponseResponseTypeDef",
    "GetAssignmentRequestTypeDef",
    "GetAssignmentResponseResponseTypeDef",
    "GetFileUploadURLRequestTypeDef",
    "GetFileUploadURLResponseResponseTypeDef",
    "GetHITRequestTypeDef",
    "GetHITResponseResponseTypeDef",
    "GetQualificationScoreRequestTypeDef",
    "GetQualificationScoreResponseResponseTypeDef",
    "GetQualificationTypeRequestTypeDef",
    "GetQualificationTypeResponseResponseTypeDef",
    "HITLayoutParameterTypeDef",
    "HITTypeDef",
    "ListAssignmentsForHITRequestTypeDef",
    "ListAssignmentsForHITResponseResponseTypeDef",
    "ListBonusPaymentsRequestTypeDef",
    "ListBonusPaymentsResponseResponseTypeDef",
    "ListHITsForQualificationTypeRequestTypeDef",
    "ListHITsForQualificationTypeResponseResponseTypeDef",
    "ListHITsRequestTypeDef",
    "ListHITsResponseResponseTypeDef",
    "ListQualificationRequestsRequestTypeDef",
    "ListQualificationRequestsResponseResponseTypeDef",
    "ListQualificationTypesRequestTypeDef",
    "ListQualificationTypesResponseResponseTypeDef",
    "ListReviewPolicyResultsForHITRequestTypeDef",
    "ListReviewPolicyResultsForHITResponseResponseTypeDef",
    "ListReviewableHITsRequestTypeDef",
    "ListReviewableHITsResponseResponseTypeDef",
    "ListWorkerBlocksRequestTypeDef",
    "ListWorkerBlocksResponseResponseTypeDef",
    "ListWorkersWithQualificationTypeRequestTypeDef",
    "ListWorkersWithQualificationTypeResponseResponseTypeDef",
    "LocaleTypeDef",
    "NotificationSpecificationTypeDef",
    "NotifyWorkersFailureStatusTypeDef",
    "NotifyWorkersRequestTypeDef",
    "NotifyWorkersResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterMapEntryTypeDef",
    "PolicyParameterTypeDef",
    "QualificationRequestTypeDef",
    "QualificationRequirementTypeDef",
    "QualificationTypeDef",
    "QualificationTypeTypeDef",
    "RejectAssignmentRequestTypeDef",
    "RejectQualificationRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ReviewActionDetailTypeDef",
    "ReviewPolicyTypeDef",
    "ReviewReportTypeDef",
    "ReviewResultDetailTypeDef",
    "SendBonusRequestTypeDef",
    "SendTestEventNotificationRequestTypeDef",
    "UpdateExpirationForHITRequestTypeDef",
    "UpdateHITReviewStatusRequestTypeDef",
    "UpdateHITTypeOfHITRequestTypeDef",
    "UpdateNotificationSettingsRequestTypeDef",
    "UpdateQualificationTypeRequestTypeDef",
    "UpdateQualificationTypeResponseResponseTypeDef",
    "WorkerBlockTypeDef",
)

_RequiredAcceptQualificationRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptQualificationRequestRequestTypeDef",
    {
        "QualificationRequestId": str,
    },
)
_OptionalAcceptQualificationRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptQualificationRequestRequestTypeDef",
    {
        "IntegerValue": int,
    },
    total=False,
)


class AcceptQualificationRequestRequestTypeDef(
    _RequiredAcceptQualificationRequestRequestTypeDef,
    _OptionalAcceptQualificationRequestRequestTypeDef,
):
    pass


_RequiredApproveAssignmentRequestTypeDef = TypedDict(
    "_RequiredApproveAssignmentRequestTypeDef",
    {
        "AssignmentId": str,
    },
)
_OptionalApproveAssignmentRequestTypeDef = TypedDict(
    "_OptionalApproveAssignmentRequestTypeDef",
    {
        "RequesterFeedback": str,
        "OverrideRejection": bool,
    },
    total=False,
)


class ApproveAssignmentRequestTypeDef(
    _RequiredApproveAssignmentRequestTypeDef, _OptionalApproveAssignmentRequestTypeDef
):
    pass


AssignmentTypeDef = TypedDict(
    "AssignmentTypeDef",
    {
        "AssignmentId": str,
        "WorkerId": str,
        "HITId": str,
        "AssignmentStatus": AssignmentStatusType,
        "AutoApprovalTime": datetime,
        "AcceptTime": datetime,
        "SubmitTime": datetime,
        "ApprovalTime": datetime,
        "RejectionTime": datetime,
        "Deadline": datetime,
        "Answer": str,
        "RequesterFeedback": str,
    },
    total=False,
)

_RequiredAssociateQualificationWithWorkerRequestTypeDef = TypedDict(
    "_RequiredAssociateQualificationWithWorkerRequestTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
    },
)
_OptionalAssociateQualificationWithWorkerRequestTypeDef = TypedDict(
    "_OptionalAssociateQualificationWithWorkerRequestTypeDef",
    {
        "IntegerValue": int,
        "SendNotification": bool,
    },
    total=False,
)


class AssociateQualificationWithWorkerRequestTypeDef(
    _RequiredAssociateQualificationWithWorkerRequestTypeDef,
    _OptionalAssociateQualificationWithWorkerRequestTypeDef,
):
    pass


BonusPaymentTypeDef = TypedDict(
    "BonusPaymentTypeDef",
    {
        "WorkerId": str,
        "BonusAmount": str,
        "AssignmentId": str,
        "Reason": str,
        "GrantTime": datetime,
    },
    total=False,
)

_RequiredCreateAdditionalAssignmentsForHITRequestTypeDef = TypedDict(
    "_RequiredCreateAdditionalAssignmentsForHITRequestTypeDef",
    {
        "HITId": str,
        "NumberOfAdditionalAssignments": int,
    },
)
_OptionalCreateAdditionalAssignmentsForHITRequestTypeDef = TypedDict(
    "_OptionalCreateAdditionalAssignmentsForHITRequestTypeDef",
    {
        "UniqueRequestToken": str,
    },
    total=False,
)


class CreateAdditionalAssignmentsForHITRequestTypeDef(
    _RequiredCreateAdditionalAssignmentsForHITRequestTypeDef,
    _OptionalCreateAdditionalAssignmentsForHITRequestTypeDef,
):
    pass


_RequiredCreateHITRequestTypeDef = TypedDict(
    "_RequiredCreateHITRequestTypeDef",
    {
        "LifetimeInSeconds": int,
        "AssignmentDurationInSeconds": int,
        "Reward": str,
        "Title": str,
        "Description": str,
    },
)
_OptionalCreateHITRequestTypeDef = TypedDict(
    "_OptionalCreateHITRequestTypeDef",
    {
        "MaxAssignments": int,
        "AutoApprovalDelayInSeconds": int,
        "Keywords": str,
        "Question": str,
        "RequesterAnnotation": str,
        "QualificationRequirements": List["QualificationRequirementTypeDef"],
        "UniqueRequestToken": str,
        "AssignmentReviewPolicy": "ReviewPolicyTypeDef",
        "HITReviewPolicy": "ReviewPolicyTypeDef",
        "HITLayoutId": str,
        "HITLayoutParameters": List["HITLayoutParameterTypeDef"],
    },
    total=False,
)


class CreateHITRequestTypeDef(_RequiredCreateHITRequestTypeDef, _OptionalCreateHITRequestTypeDef):
    pass


CreateHITResponseResponseTypeDef = TypedDict(
    "CreateHITResponseResponseTypeDef",
    {
        "HIT": "HITTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHITTypeRequestTypeDef = TypedDict(
    "_RequiredCreateHITTypeRequestTypeDef",
    {
        "AssignmentDurationInSeconds": int,
        "Reward": str,
        "Title": str,
        "Description": str,
    },
)
_OptionalCreateHITTypeRequestTypeDef = TypedDict(
    "_OptionalCreateHITTypeRequestTypeDef",
    {
        "AutoApprovalDelayInSeconds": int,
        "Keywords": str,
        "QualificationRequirements": List["QualificationRequirementTypeDef"],
    },
    total=False,
)


class CreateHITTypeRequestTypeDef(
    _RequiredCreateHITTypeRequestTypeDef, _OptionalCreateHITTypeRequestTypeDef
):
    pass


CreateHITTypeResponseResponseTypeDef = TypedDict(
    "CreateHITTypeResponseResponseTypeDef",
    {
        "HITTypeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHITWithHITTypeRequestTypeDef = TypedDict(
    "_RequiredCreateHITWithHITTypeRequestTypeDef",
    {
        "HITTypeId": str,
        "LifetimeInSeconds": int,
    },
)
_OptionalCreateHITWithHITTypeRequestTypeDef = TypedDict(
    "_OptionalCreateHITWithHITTypeRequestTypeDef",
    {
        "MaxAssignments": int,
        "Question": str,
        "RequesterAnnotation": str,
        "UniqueRequestToken": str,
        "AssignmentReviewPolicy": "ReviewPolicyTypeDef",
        "HITReviewPolicy": "ReviewPolicyTypeDef",
        "HITLayoutId": str,
        "HITLayoutParameters": List["HITLayoutParameterTypeDef"],
    },
    total=False,
)


class CreateHITWithHITTypeRequestTypeDef(
    _RequiredCreateHITWithHITTypeRequestTypeDef, _OptionalCreateHITWithHITTypeRequestTypeDef
):
    pass


CreateHITWithHITTypeResponseResponseTypeDef = TypedDict(
    "CreateHITWithHITTypeResponseResponseTypeDef",
    {
        "HIT": "HITTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateQualificationTypeRequestTypeDef = TypedDict(
    "_RequiredCreateQualificationTypeRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "QualificationTypeStatus": QualificationTypeStatusType,
    },
)
_OptionalCreateQualificationTypeRequestTypeDef = TypedDict(
    "_OptionalCreateQualificationTypeRequestTypeDef",
    {
        "Keywords": str,
        "RetryDelayInSeconds": int,
        "Test": str,
        "AnswerKey": str,
        "TestDurationInSeconds": int,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)


class CreateQualificationTypeRequestTypeDef(
    _RequiredCreateQualificationTypeRequestTypeDef, _OptionalCreateQualificationTypeRequestTypeDef
):
    pass


CreateQualificationTypeResponseResponseTypeDef = TypedDict(
    "CreateQualificationTypeResponseResponseTypeDef",
    {
        "QualificationType": "QualificationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkerBlockRequestTypeDef = TypedDict(
    "CreateWorkerBlockRequestTypeDef",
    {
        "WorkerId": str,
        "Reason": str,
    },
)

DeleteHITRequestTypeDef = TypedDict(
    "DeleteHITRequestTypeDef",
    {
        "HITId": str,
    },
)

DeleteQualificationTypeRequestTypeDef = TypedDict(
    "DeleteQualificationTypeRequestTypeDef",
    {
        "QualificationTypeId": str,
    },
)

_RequiredDeleteWorkerBlockRequestTypeDef = TypedDict(
    "_RequiredDeleteWorkerBlockRequestTypeDef",
    {
        "WorkerId": str,
    },
)
_OptionalDeleteWorkerBlockRequestTypeDef = TypedDict(
    "_OptionalDeleteWorkerBlockRequestTypeDef",
    {
        "Reason": str,
    },
    total=False,
)


class DeleteWorkerBlockRequestTypeDef(
    _RequiredDeleteWorkerBlockRequestTypeDef, _OptionalDeleteWorkerBlockRequestTypeDef
):
    pass


_RequiredDisassociateQualificationFromWorkerRequestTypeDef = TypedDict(
    "_RequiredDisassociateQualificationFromWorkerRequestTypeDef",
    {
        "WorkerId": str,
        "QualificationTypeId": str,
    },
)
_OptionalDisassociateQualificationFromWorkerRequestTypeDef = TypedDict(
    "_OptionalDisassociateQualificationFromWorkerRequestTypeDef",
    {
        "Reason": str,
    },
    total=False,
)


class DisassociateQualificationFromWorkerRequestTypeDef(
    _RequiredDisassociateQualificationFromWorkerRequestTypeDef,
    _OptionalDisassociateQualificationFromWorkerRequestTypeDef,
):
    pass


GetAccountBalanceResponseResponseTypeDef = TypedDict(
    "GetAccountBalanceResponseResponseTypeDef",
    {
        "AvailableBalance": str,
        "OnHoldBalance": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssignmentRequestTypeDef = TypedDict(
    "GetAssignmentRequestTypeDef",
    {
        "AssignmentId": str,
    },
)

GetAssignmentResponseResponseTypeDef = TypedDict(
    "GetAssignmentResponseResponseTypeDef",
    {
        "Assignment": "AssignmentTypeDef",
        "HIT": "HITTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFileUploadURLRequestTypeDef = TypedDict(
    "GetFileUploadURLRequestTypeDef",
    {
        "AssignmentId": str,
        "QuestionIdentifier": str,
    },
)

GetFileUploadURLResponseResponseTypeDef = TypedDict(
    "GetFileUploadURLResponseResponseTypeDef",
    {
        "FileUploadURL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHITRequestTypeDef = TypedDict(
    "GetHITRequestTypeDef",
    {
        "HITId": str,
    },
)

GetHITResponseResponseTypeDef = TypedDict(
    "GetHITResponseResponseTypeDef",
    {
        "HIT": "HITTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQualificationScoreRequestTypeDef = TypedDict(
    "GetQualificationScoreRequestTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
    },
)

GetQualificationScoreResponseResponseTypeDef = TypedDict(
    "GetQualificationScoreResponseResponseTypeDef",
    {
        "Qualification": "QualificationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQualificationTypeRequestTypeDef = TypedDict(
    "GetQualificationTypeRequestTypeDef",
    {
        "QualificationTypeId": str,
    },
)

GetQualificationTypeResponseResponseTypeDef = TypedDict(
    "GetQualificationTypeResponseResponseTypeDef",
    {
        "QualificationType": "QualificationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HITLayoutParameterTypeDef = TypedDict(
    "HITLayoutParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

HITTypeDef = TypedDict(
    "HITTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": HITStatusType,
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List["QualificationRequirementTypeDef"],
        "HITReviewStatus": HITReviewStatusType,
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)

_RequiredListAssignmentsForHITRequestTypeDef = TypedDict(
    "_RequiredListAssignmentsForHITRequestTypeDef",
    {
        "HITId": str,
    },
)
_OptionalListAssignmentsForHITRequestTypeDef = TypedDict(
    "_OptionalListAssignmentsForHITRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "AssignmentStatuses": List[AssignmentStatusType],
    },
    total=False,
)


class ListAssignmentsForHITRequestTypeDef(
    _RequiredListAssignmentsForHITRequestTypeDef, _OptionalListAssignmentsForHITRequestTypeDef
):
    pass


ListAssignmentsForHITResponseResponseTypeDef = TypedDict(
    "ListAssignmentsForHITResponseResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "Assignments": List["AssignmentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBonusPaymentsRequestTypeDef = TypedDict(
    "ListBonusPaymentsRequestTypeDef",
    {
        "HITId": str,
        "AssignmentId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListBonusPaymentsResponseResponseTypeDef = TypedDict(
    "ListBonusPaymentsResponseResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "BonusPayments": List["BonusPaymentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListHITsForQualificationTypeRequestTypeDef = TypedDict(
    "_RequiredListHITsForQualificationTypeRequestTypeDef",
    {
        "QualificationTypeId": str,
    },
)
_OptionalListHITsForQualificationTypeRequestTypeDef = TypedDict(
    "_OptionalListHITsForQualificationTypeRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListHITsForQualificationTypeRequestTypeDef(
    _RequiredListHITsForQualificationTypeRequestTypeDef,
    _OptionalListHITsForQualificationTypeRequestTypeDef,
):
    pass


ListHITsForQualificationTypeResponseResponseTypeDef = TypedDict(
    "ListHITsForQualificationTypeResponseResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List["HITTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHITsRequestTypeDef = TypedDict(
    "ListHITsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListHITsResponseResponseTypeDef = TypedDict(
    "ListHITsResponseResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List["HITTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQualificationRequestsRequestTypeDef = TypedDict(
    "ListQualificationRequestsRequestTypeDef",
    {
        "QualificationTypeId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListQualificationRequestsResponseResponseTypeDef = TypedDict(
    "ListQualificationRequestsResponseResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "QualificationRequests": List["QualificationRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQualificationTypesRequestTypeDef = TypedDict(
    "_RequiredListQualificationTypesRequestTypeDef",
    {
        "MustBeRequestable": bool,
    },
)
_OptionalListQualificationTypesRequestTypeDef = TypedDict(
    "_OptionalListQualificationTypesRequestTypeDef",
    {
        "Query": str,
        "MustBeOwnedByCaller": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListQualificationTypesRequestTypeDef(
    _RequiredListQualificationTypesRequestTypeDef, _OptionalListQualificationTypesRequestTypeDef
):
    pass


ListQualificationTypesResponseResponseTypeDef = TypedDict(
    "ListQualificationTypesResponseResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "QualificationTypes": List["QualificationTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListReviewPolicyResultsForHITRequestTypeDef = TypedDict(
    "_RequiredListReviewPolicyResultsForHITRequestTypeDef",
    {
        "HITId": str,
    },
)
_OptionalListReviewPolicyResultsForHITRequestTypeDef = TypedDict(
    "_OptionalListReviewPolicyResultsForHITRequestTypeDef",
    {
        "PolicyLevels": List[ReviewPolicyLevelType],
        "RetrieveActions": bool,
        "RetrieveResults": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListReviewPolicyResultsForHITRequestTypeDef(
    _RequiredListReviewPolicyResultsForHITRequestTypeDef,
    _OptionalListReviewPolicyResultsForHITRequestTypeDef,
):
    pass


ListReviewPolicyResultsForHITResponseResponseTypeDef = TypedDict(
    "ListReviewPolicyResultsForHITResponseResponseTypeDef",
    {
        "HITId": str,
        "AssignmentReviewPolicy": "ReviewPolicyTypeDef",
        "HITReviewPolicy": "ReviewPolicyTypeDef",
        "AssignmentReviewReport": "ReviewReportTypeDef",
        "HITReviewReport": "ReviewReportTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReviewableHITsRequestTypeDef = TypedDict(
    "ListReviewableHITsRequestTypeDef",
    {
        "HITTypeId": str,
        "Status": ReviewableHITStatusType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListReviewableHITsResponseResponseTypeDef = TypedDict(
    "ListReviewableHITsResponseResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List["HITTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkerBlocksRequestTypeDef = TypedDict(
    "ListWorkerBlocksRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWorkerBlocksResponseResponseTypeDef = TypedDict(
    "ListWorkerBlocksResponseResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "WorkerBlocks": List["WorkerBlockTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWorkersWithQualificationTypeRequestTypeDef = TypedDict(
    "_RequiredListWorkersWithQualificationTypeRequestTypeDef",
    {
        "QualificationTypeId": str,
    },
)
_OptionalListWorkersWithQualificationTypeRequestTypeDef = TypedDict(
    "_OptionalListWorkersWithQualificationTypeRequestTypeDef",
    {
        "Status": QualificationStatusType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListWorkersWithQualificationTypeRequestTypeDef(
    _RequiredListWorkersWithQualificationTypeRequestTypeDef,
    _OptionalListWorkersWithQualificationTypeRequestTypeDef,
):
    pass


ListWorkersWithQualificationTypeResponseResponseTypeDef = TypedDict(
    "ListWorkersWithQualificationTypeResponseResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "Qualifications": List["QualificationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLocaleTypeDef = TypedDict(
    "_RequiredLocaleTypeDef",
    {
        "Country": str,
    },
)
_OptionalLocaleTypeDef = TypedDict(
    "_OptionalLocaleTypeDef",
    {
        "Subdivision": str,
    },
    total=False,
)


class LocaleTypeDef(_RequiredLocaleTypeDef, _OptionalLocaleTypeDef):
    pass


NotificationSpecificationTypeDef = TypedDict(
    "NotificationSpecificationTypeDef",
    {
        "Destination": str,
        "Transport": NotificationTransportType,
        "Version": str,
        "EventTypes": List[EventTypeType],
    },
)

NotifyWorkersFailureStatusTypeDef = TypedDict(
    "NotifyWorkersFailureStatusTypeDef",
    {
        "NotifyWorkersFailureCode": NotifyWorkersFailureCodeType,
        "NotifyWorkersFailureMessage": str,
        "WorkerId": str,
    },
    total=False,
)

NotifyWorkersRequestTypeDef = TypedDict(
    "NotifyWorkersRequestTypeDef",
    {
        "Subject": str,
        "MessageText": str,
        "WorkerIds": List[str],
    },
)

NotifyWorkersResponseResponseTypeDef = TypedDict(
    "NotifyWorkersResponseResponseTypeDef",
    {
        "NotifyWorkersFailureStatuses": List["NotifyWorkersFailureStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

ParameterMapEntryTypeDef = TypedDict(
    "ParameterMapEntryTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

PolicyParameterTypeDef = TypedDict(
    "PolicyParameterTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List["ParameterMapEntryTypeDef"],
    },
    total=False,
)

QualificationRequestTypeDef = TypedDict(
    "QualificationRequestTypeDef",
    {
        "QualificationRequestId": str,
        "QualificationTypeId": str,
        "WorkerId": str,
        "Test": str,
        "Answer": str,
        "SubmitTime": datetime,
    },
    total=False,
)

_RequiredQualificationRequirementTypeDef = TypedDict(
    "_RequiredQualificationRequirementTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": ComparatorType,
    },
)
_OptionalQualificationRequirementTypeDef = TypedDict(
    "_OptionalQualificationRequirementTypeDef",
    {
        "IntegerValues": List[int],
        "LocaleValues": List["LocaleTypeDef"],
        "RequiredToPreview": bool,
        "ActionsGuarded": HITAccessActionsType,
    },
    total=False,
)


class QualificationRequirementTypeDef(
    _RequiredQualificationRequirementTypeDef, _OptionalQualificationRequirementTypeDef
):
    pass


QualificationTypeDef = TypedDict(
    "QualificationTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
        "GrantTime": datetime,
        "IntegerValue": int,
        "LocaleValue": "LocaleTypeDef",
        "Status": QualificationStatusType,
    },
    total=False,
)

QualificationTypeTypeDef = TypedDict(
    "QualificationTypeTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": QualificationTypeStatusType,
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)

RejectAssignmentRequestTypeDef = TypedDict(
    "RejectAssignmentRequestTypeDef",
    {
        "AssignmentId": str,
        "RequesterFeedback": str,
    },
)

_RequiredRejectQualificationRequestRequestTypeDef = TypedDict(
    "_RequiredRejectQualificationRequestRequestTypeDef",
    {
        "QualificationRequestId": str,
    },
)
_OptionalRejectQualificationRequestRequestTypeDef = TypedDict(
    "_OptionalRejectQualificationRequestRequestTypeDef",
    {
        "Reason": str,
    },
    total=False,
)


class RejectQualificationRequestRequestTypeDef(
    _RequiredRejectQualificationRequestRequestTypeDef,
    _OptionalRejectQualificationRequestRequestTypeDef,
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

ReviewActionDetailTypeDef = TypedDict(
    "ReviewActionDetailTypeDef",
    {
        "ActionId": str,
        "ActionName": str,
        "TargetId": str,
        "TargetType": str,
        "Status": ReviewActionStatusType,
        "CompleteTime": datetime,
        "Result": str,
        "ErrorCode": str,
    },
    total=False,
)

_RequiredReviewPolicyTypeDef = TypedDict(
    "_RequiredReviewPolicyTypeDef",
    {
        "PolicyName": str,
    },
)
_OptionalReviewPolicyTypeDef = TypedDict(
    "_OptionalReviewPolicyTypeDef",
    {
        "Parameters": List["PolicyParameterTypeDef"],
    },
    total=False,
)


class ReviewPolicyTypeDef(_RequiredReviewPolicyTypeDef, _OptionalReviewPolicyTypeDef):
    pass


ReviewReportTypeDef = TypedDict(
    "ReviewReportTypeDef",
    {
        "ReviewResults": List["ReviewResultDetailTypeDef"],
        "ReviewActions": List["ReviewActionDetailTypeDef"],
    },
    total=False,
)

ReviewResultDetailTypeDef = TypedDict(
    "ReviewResultDetailTypeDef",
    {
        "ActionId": str,
        "SubjectId": str,
        "SubjectType": str,
        "QuestionId": str,
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredSendBonusRequestTypeDef = TypedDict(
    "_RequiredSendBonusRequestTypeDef",
    {
        "WorkerId": str,
        "BonusAmount": str,
        "AssignmentId": str,
        "Reason": str,
    },
)
_OptionalSendBonusRequestTypeDef = TypedDict(
    "_OptionalSendBonusRequestTypeDef",
    {
        "UniqueRequestToken": str,
    },
    total=False,
)


class SendBonusRequestTypeDef(_RequiredSendBonusRequestTypeDef, _OptionalSendBonusRequestTypeDef):
    pass


SendTestEventNotificationRequestTypeDef = TypedDict(
    "SendTestEventNotificationRequestTypeDef",
    {
        "Notification": "NotificationSpecificationTypeDef",
        "TestEventType": EventTypeType,
    },
)

UpdateExpirationForHITRequestTypeDef = TypedDict(
    "UpdateExpirationForHITRequestTypeDef",
    {
        "HITId": str,
        "ExpireAt": Union[datetime, str],
    },
)

_RequiredUpdateHITReviewStatusRequestTypeDef = TypedDict(
    "_RequiredUpdateHITReviewStatusRequestTypeDef",
    {
        "HITId": str,
    },
)
_OptionalUpdateHITReviewStatusRequestTypeDef = TypedDict(
    "_OptionalUpdateHITReviewStatusRequestTypeDef",
    {
        "Revert": bool,
    },
    total=False,
)


class UpdateHITReviewStatusRequestTypeDef(
    _RequiredUpdateHITReviewStatusRequestTypeDef, _OptionalUpdateHITReviewStatusRequestTypeDef
):
    pass


UpdateHITTypeOfHITRequestTypeDef = TypedDict(
    "UpdateHITTypeOfHITRequestTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
    },
)

_RequiredUpdateNotificationSettingsRequestTypeDef = TypedDict(
    "_RequiredUpdateNotificationSettingsRequestTypeDef",
    {
        "HITTypeId": str,
    },
)
_OptionalUpdateNotificationSettingsRequestTypeDef = TypedDict(
    "_OptionalUpdateNotificationSettingsRequestTypeDef",
    {
        "Notification": "NotificationSpecificationTypeDef",
        "Active": bool,
    },
    total=False,
)


class UpdateNotificationSettingsRequestTypeDef(
    _RequiredUpdateNotificationSettingsRequestTypeDef,
    _OptionalUpdateNotificationSettingsRequestTypeDef,
):
    pass


_RequiredUpdateQualificationTypeRequestTypeDef = TypedDict(
    "_RequiredUpdateQualificationTypeRequestTypeDef",
    {
        "QualificationTypeId": str,
    },
)
_OptionalUpdateQualificationTypeRequestTypeDef = TypedDict(
    "_OptionalUpdateQualificationTypeRequestTypeDef",
    {
        "Description": str,
        "QualificationTypeStatus": QualificationTypeStatusType,
        "Test": str,
        "AnswerKey": str,
        "TestDurationInSeconds": int,
        "RetryDelayInSeconds": int,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)


class UpdateQualificationTypeRequestTypeDef(
    _RequiredUpdateQualificationTypeRequestTypeDef, _OptionalUpdateQualificationTypeRequestTypeDef
):
    pass


UpdateQualificationTypeResponseResponseTypeDef = TypedDict(
    "UpdateQualificationTypeResponseResponseTypeDef",
    {
        "QualificationType": "QualificationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WorkerBlockTypeDef = TypedDict(
    "WorkerBlockTypeDef",
    {
        "WorkerId": str,
        "Reason": str,
    },
    total=False,
)
