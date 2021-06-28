"""
Type annotations for support service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support/type_defs.html)

Usage::

    ```python
    from mypy_boto3_support.type_defs import AddAttachmentsToSetRequestTypeDef

    data: AddAttachmentsToSetRequestTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddAttachmentsToSetRequestTypeDef",
    "AddAttachmentsToSetResponseResponseTypeDef",
    "AddCommunicationToCaseRequestTypeDef",
    "AddCommunicationToCaseResponseResponseTypeDef",
    "AttachmentDetailsTypeDef",
    "AttachmentTypeDef",
    "CaseDetailsTypeDef",
    "CategoryTypeDef",
    "CommunicationTypeDef",
    "CreateCaseRequestTypeDef",
    "CreateCaseResponseResponseTypeDef",
    "DescribeAttachmentRequestTypeDef",
    "DescribeAttachmentResponseResponseTypeDef",
    "DescribeCasesRequestTypeDef",
    "DescribeCasesResponseResponseTypeDef",
    "DescribeCommunicationsRequestTypeDef",
    "DescribeCommunicationsResponseResponseTypeDef",
    "DescribeServicesRequestTypeDef",
    "DescribeServicesResponseResponseTypeDef",
    "DescribeSeverityLevelsRequestTypeDef",
    "DescribeSeverityLevelsResponseResponseTypeDef",
    "DescribeTrustedAdvisorCheckRefreshStatusesRequestTypeDef",
    "DescribeTrustedAdvisorCheckRefreshStatusesResponseResponseTypeDef",
    "DescribeTrustedAdvisorCheckResultRequestTypeDef",
    "DescribeTrustedAdvisorCheckResultResponseResponseTypeDef",
    "DescribeTrustedAdvisorCheckSummariesRequestTypeDef",
    "DescribeTrustedAdvisorCheckSummariesResponseResponseTypeDef",
    "DescribeTrustedAdvisorChecksRequestTypeDef",
    "DescribeTrustedAdvisorChecksResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RecentCaseCommunicationsTypeDef",
    "RefreshTrustedAdvisorCheckRequestTypeDef",
    "RefreshTrustedAdvisorCheckResponseResponseTypeDef",
    "ResolveCaseRequestTypeDef",
    "ResolveCaseResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceTypeDef",
    "SeverityLevelTypeDef",
    "TrustedAdvisorCategorySpecificSummaryTypeDef",
    "TrustedAdvisorCheckDescriptionTypeDef",
    "TrustedAdvisorCheckRefreshStatusTypeDef",
    "TrustedAdvisorCheckResultTypeDef",
    "TrustedAdvisorCheckSummaryTypeDef",
    "TrustedAdvisorCostOptimizingSummaryTypeDef",
    "TrustedAdvisorResourceDetailTypeDef",
    "TrustedAdvisorResourcesSummaryTypeDef",
)

_RequiredAddAttachmentsToSetRequestTypeDef = TypedDict(
    "_RequiredAddAttachmentsToSetRequestTypeDef",
    {
        "attachments": List["AttachmentTypeDef"],
    },
)
_OptionalAddAttachmentsToSetRequestTypeDef = TypedDict(
    "_OptionalAddAttachmentsToSetRequestTypeDef",
    {
        "attachmentSetId": str,
    },
    total=False,
)


class AddAttachmentsToSetRequestTypeDef(
    _RequiredAddAttachmentsToSetRequestTypeDef, _OptionalAddAttachmentsToSetRequestTypeDef
):
    pass


AddAttachmentsToSetResponseResponseTypeDef = TypedDict(
    "AddAttachmentsToSetResponseResponseTypeDef",
    {
        "attachmentSetId": str,
        "expiryTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAddCommunicationToCaseRequestTypeDef = TypedDict(
    "_RequiredAddCommunicationToCaseRequestTypeDef",
    {
        "communicationBody": str,
    },
)
_OptionalAddCommunicationToCaseRequestTypeDef = TypedDict(
    "_OptionalAddCommunicationToCaseRequestTypeDef",
    {
        "caseId": str,
        "ccEmailAddresses": List[str],
        "attachmentSetId": str,
    },
    total=False,
)


class AddCommunicationToCaseRequestTypeDef(
    _RequiredAddCommunicationToCaseRequestTypeDef, _OptionalAddCommunicationToCaseRequestTypeDef
):
    pass


AddCommunicationToCaseResponseResponseTypeDef = TypedDict(
    "AddCommunicationToCaseResponseResponseTypeDef",
    {
        "result": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachmentDetailsTypeDef = TypedDict(
    "AttachmentDetailsTypeDef",
    {
        "attachmentId": str,
        "fileName": str,
    },
    total=False,
)

AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "fileName": str,
        "data": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

CaseDetailsTypeDef = TypedDict(
    "CaseDetailsTypeDef",
    {
        "caseId": str,
        "displayId": str,
        "subject": str,
        "status": str,
        "serviceCode": str,
        "categoryCode": str,
        "severityCode": str,
        "submittedBy": str,
        "timeCreated": str,
        "recentCommunications": "RecentCaseCommunicationsTypeDef",
        "ccEmailAddresses": List[str],
        "language": str,
    },
    total=False,
)

CategoryTypeDef = TypedDict(
    "CategoryTypeDef",
    {
        "code": str,
        "name": str,
    },
    total=False,
)

CommunicationTypeDef = TypedDict(
    "CommunicationTypeDef",
    {
        "caseId": str,
        "body": str,
        "submittedBy": str,
        "timeCreated": str,
        "attachmentSet": List["AttachmentDetailsTypeDef"],
    },
    total=False,
)

_RequiredCreateCaseRequestTypeDef = TypedDict(
    "_RequiredCreateCaseRequestTypeDef",
    {
        "subject": str,
        "communicationBody": str,
    },
)
_OptionalCreateCaseRequestTypeDef = TypedDict(
    "_OptionalCreateCaseRequestTypeDef",
    {
        "serviceCode": str,
        "severityCode": str,
        "categoryCode": str,
        "ccEmailAddresses": List[str],
        "language": str,
        "issueType": str,
        "attachmentSetId": str,
    },
    total=False,
)


class CreateCaseRequestTypeDef(
    _RequiredCreateCaseRequestTypeDef, _OptionalCreateCaseRequestTypeDef
):
    pass


CreateCaseResponseResponseTypeDef = TypedDict(
    "CreateCaseResponseResponseTypeDef",
    {
        "caseId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAttachmentRequestTypeDef = TypedDict(
    "DescribeAttachmentRequestTypeDef",
    {
        "attachmentId": str,
    },
)

DescribeAttachmentResponseResponseTypeDef = TypedDict(
    "DescribeAttachmentResponseResponseTypeDef",
    {
        "attachment": "AttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCasesRequestTypeDef = TypedDict(
    "DescribeCasesRequestTypeDef",
    {
        "caseIdList": List[str],
        "displayId": str,
        "afterTime": str,
        "beforeTime": str,
        "includeResolvedCases": bool,
        "nextToken": str,
        "maxResults": int,
        "language": str,
        "includeCommunications": bool,
    },
    total=False,
)

DescribeCasesResponseResponseTypeDef = TypedDict(
    "DescribeCasesResponseResponseTypeDef",
    {
        "cases": List["CaseDetailsTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeCommunicationsRequestTypeDef = TypedDict(
    "_RequiredDescribeCommunicationsRequestTypeDef",
    {
        "caseId": str,
    },
)
_OptionalDescribeCommunicationsRequestTypeDef = TypedDict(
    "_OptionalDescribeCommunicationsRequestTypeDef",
    {
        "beforeTime": str,
        "afterTime": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class DescribeCommunicationsRequestTypeDef(
    _RequiredDescribeCommunicationsRequestTypeDef, _OptionalDescribeCommunicationsRequestTypeDef
):
    pass


DescribeCommunicationsResponseResponseTypeDef = TypedDict(
    "DescribeCommunicationsResponseResponseTypeDef",
    {
        "communications": List["CommunicationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServicesRequestTypeDef = TypedDict(
    "DescribeServicesRequestTypeDef",
    {
        "serviceCodeList": List[str],
        "language": str,
    },
    total=False,
)

DescribeServicesResponseResponseTypeDef = TypedDict(
    "DescribeServicesResponseResponseTypeDef",
    {
        "services": List["ServiceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSeverityLevelsRequestTypeDef = TypedDict(
    "DescribeSeverityLevelsRequestTypeDef",
    {
        "language": str,
    },
    total=False,
)

DescribeSeverityLevelsResponseResponseTypeDef = TypedDict(
    "DescribeSeverityLevelsResponseResponseTypeDef",
    {
        "severityLevels": List["SeverityLevelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrustedAdvisorCheckRefreshStatusesRequestTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckRefreshStatusesRequestTypeDef",
    {
        "checkIds": List[str],
    },
)

DescribeTrustedAdvisorCheckRefreshStatusesResponseResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckRefreshStatusesResponseResponseTypeDef",
    {
        "statuses": List["TrustedAdvisorCheckRefreshStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTrustedAdvisorCheckResultRequestTypeDef = TypedDict(
    "_RequiredDescribeTrustedAdvisorCheckResultRequestTypeDef",
    {
        "checkId": str,
    },
)
_OptionalDescribeTrustedAdvisorCheckResultRequestTypeDef = TypedDict(
    "_OptionalDescribeTrustedAdvisorCheckResultRequestTypeDef",
    {
        "language": str,
    },
    total=False,
)


class DescribeTrustedAdvisorCheckResultRequestTypeDef(
    _RequiredDescribeTrustedAdvisorCheckResultRequestTypeDef,
    _OptionalDescribeTrustedAdvisorCheckResultRequestTypeDef,
):
    pass


DescribeTrustedAdvisorCheckResultResponseResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckResultResponseResponseTypeDef",
    {
        "result": "TrustedAdvisorCheckResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrustedAdvisorCheckSummariesRequestTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckSummariesRequestTypeDef",
    {
        "checkIds": List[str],
    },
)

DescribeTrustedAdvisorCheckSummariesResponseResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckSummariesResponseResponseTypeDef",
    {
        "summaries": List["TrustedAdvisorCheckSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrustedAdvisorChecksRequestTypeDef = TypedDict(
    "DescribeTrustedAdvisorChecksRequestTypeDef",
    {
        "language": str,
    },
)

DescribeTrustedAdvisorChecksResponseResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorChecksResponseResponseTypeDef",
    {
        "checks": List["TrustedAdvisorCheckDescriptionTypeDef"],
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

RecentCaseCommunicationsTypeDef = TypedDict(
    "RecentCaseCommunicationsTypeDef",
    {
        "communications": List["CommunicationTypeDef"],
        "nextToken": str,
    },
    total=False,
)

RefreshTrustedAdvisorCheckRequestTypeDef = TypedDict(
    "RefreshTrustedAdvisorCheckRequestTypeDef",
    {
        "checkId": str,
    },
)

RefreshTrustedAdvisorCheckResponseResponseTypeDef = TypedDict(
    "RefreshTrustedAdvisorCheckResponseResponseTypeDef",
    {
        "status": "TrustedAdvisorCheckRefreshStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolveCaseRequestTypeDef = TypedDict(
    "ResolveCaseRequestTypeDef",
    {
        "caseId": str,
    },
    total=False,
)

ResolveCaseResponseResponseTypeDef = TypedDict(
    "ResolveCaseResponseResponseTypeDef",
    {
        "initialCaseStatus": str,
        "finalCaseStatus": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "code": str,
        "name": str,
        "categories": List["CategoryTypeDef"],
    },
    total=False,
)

SeverityLevelTypeDef = TypedDict(
    "SeverityLevelTypeDef",
    {
        "code": str,
        "name": str,
    },
    total=False,
)

TrustedAdvisorCategorySpecificSummaryTypeDef = TypedDict(
    "TrustedAdvisorCategorySpecificSummaryTypeDef",
    {
        "costOptimizing": "TrustedAdvisorCostOptimizingSummaryTypeDef",
    },
    total=False,
)

TrustedAdvisorCheckDescriptionTypeDef = TypedDict(
    "TrustedAdvisorCheckDescriptionTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "category": str,
        "metadata": List[str],
    },
)

TrustedAdvisorCheckRefreshStatusTypeDef = TypedDict(
    "TrustedAdvisorCheckRefreshStatusTypeDef",
    {
        "checkId": str,
        "status": str,
        "millisUntilNextRefreshable": int,
    },
)

TrustedAdvisorCheckResultTypeDef = TypedDict(
    "TrustedAdvisorCheckResultTypeDef",
    {
        "checkId": str,
        "timestamp": str,
        "status": str,
        "resourcesSummary": "TrustedAdvisorResourcesSummaryTypeDef",
        "categorySpecificSummary": "TrustedAdvisorCategorySpecificSummaryTypeDef",
        "flaggedResources": List["TrustedAdvisorResourceDetailTypeDef"],
    },
)

_RequiredTrustedAdvisorCheckSummaryTypeDef = TypedDict(
    "_RequiredTrustedAdvisorCheckSummaryTypeDef",
    {
        "checkId": str,
        "timestamp": str,
        "status": str,
        "resourcesSummary": "TrustedAdvisorResourcesSummaryTypeDef",
        "categorySpecificSummary": "TrustedAdvisorCategorySpecificSummaryTypeDef",
    },
)
_OptionalTrustedAdvisorCheckSummaryTypeDef = TypedDict(
    "_OptionalTrustedAdvisorCheckSummaryTypeDef",
    {
        "hasFlaggedResources": bool,
    },
    total=False,
)


class TrustedAdvisorCheckSummaryTypeDef(
    _RequiredTrustedAdvisorCheckSummaryTypeDef, _OptionalTrustedAdvisorCheckSummaryTypeDef
):
    pass


TrustedAdvisorCostOptimizingSummaryTypeDef = TypedDict(
    "TrustedAdvisorCostOptimizingSummaryTypeDef",
    {
        "estimatedMonthlySavings": float,
        "estimatedPercentMonthlySavings": float,
    },
)

_RequiredTrustedAdvisorResourceDetailTypeDef = TypedDict(
    "_RequiredTrustedAdvisorResourceDetailTypeDef",
    {
        "status": str,
        "resourceId": str,
        "metadata": List[str],
    },
)
_OptionalTrustedAdvisorResourceDetailTypeDef = TypedDict(
    "_OptionalTrustedAdvisorResourceDetailTypeDef",
    {
        "region": str,
        "isSuppressed": bool,
    },
    total=False,
)


class TrustedAdvisorResourceDetailTypeDef(
    _RequiredTrustedAdvisorResourceDetailTypeDef, _OptionalTrustedAdvisorResourceDetailTypeDef
):
    pass


TrustedAdvisorResourcesSummaryTypeDef = TypedDict(
    "TrustedAdvisorResourcesSummaryTypeDef",
    {
        "resourcesProcessed": int,
        "resourcesFlagged": int,
        "resourcesIgnored": int,
        "resourcesSuppressed": int,
    },
)
