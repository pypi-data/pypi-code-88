"""
Type annotations for inspector service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector/type_defs.html)

Usage::

    ```python
    from mypy_boto3_inspector.type_defs import AddAttributesToFindingsRequestTypeDef

    data: AddAttributesToFindingsRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AgentHealthCodeType,
    AgentHealthType,
    AssessmentRunNotificationSnsStatusCodeType,
    AssessmentRunStateType,
    FailedItemErrorCodeType,
    InspectorEventType,
    PreviewStatusType,
    ReportFileFormatType,
    ReportStatusType,
    ReportTypeType,
    ScopeTypeType,
    SeverityType,
    StopActionType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddAttributesToFindingsRequestTypeDef",
    "AddAttributesToFindingsResponseResponseTypeDef",
    "AgentFilterTypeDef",
    "AgentPreviewTypeDef",
    "AssessmentRunAgentTypeDef",
    "AssessmentRunFilterTypeDef",
    "AssessmentRunNotificationTypeDef",
    "AssessmentRunStateChangeTypeDef",
    "AssessmentRunTypeDef",
    "AssessmentTargetFilterTypeDef",
    "AssessmentTargetTypeDef",
    "AssessmentTemplateFilterTypeDef",
    "AssessmentTemplateTypeDef",
    "AssetAttributesTypeDef",
    "AttributeTypeDef",
    "CreateAssessmentTargetRequestTypeDef",
    "CreateAssessmentTargetResponseResponseTypeDef",
    "CreateAssessmentTemplateRequestTypeDef",
    "CreateAssessmentTemplateResponseResponseTypeDef",
    "CreateExclusionsPreviewRequestTypeDef",
    "CreateExclusionsPreviewResponseResponseTypeDef",
    "CreateResourceGroupRequestTypeDef",
    "CreateResourceGroupResponseResponseTypeDef",
    "DeleteAssessmentRunRequestTypeDef",
    "DeleteAssessmentTargetRequestTypeDef",
    "DeleteAssessmentTemplateRequestTypeDef",
    "DescribeAssessmentRunsRequestTypeDef",
    "DescribeAssessmentRunsResponseResponseTypeDef",
    "DescribeAssessmentTargetsRequestTypeDef",
    "DescribeAssessmentTargetsResponseResponseTypeDef",
    "DescribeAssessmentTemplatesRequestTypeDef",
    "DescribeAssessmentTemplatesResponseResponseTypeDef",
    "DescribeCrossAccountAccessRoleResponseResponseTypeDef",
    "DescribeExclusionsRequestTypeDef",
    "DescribeExclusionsResponseResponseTypeDef",
    "DescribeFindingsRequestTypeDef",
    "DescribeFindingsResponseResponseTypeDef",
    "DescribeResourceGroupsRequestTypeDef",
    "DescribeResourceGroupsResponseResponseTypeDef",
    "DescribeRulesPackagesRequestTypeDef",
    "DescribeRulesPackagesResponseResponseTypeDef",
    "DurationRangeTypeDef",
    "EventSubscriptionTypeDef",
    "ExclusionPreviewTypeDef",
    "ExclusionTypeDef",
    "FailedItemDetailsTypeDef",
    "FindingFilterTypeDef",
    "FindingTypeDef",
    "GetAssessmentReportRequestTypeDef",
    "GetAssessmentReportResponseResponseTypeDef",
    "GetExclusionsPreviewRequestTypeDef",
    "GetExclusionsPreviewResponseResponseTypeDef",
    "GetTelemetryMetadataRequestTypeDef",
    "GetTelemetryMetadataResponseResponseTypeDef",
    "InspectorServiceAttributesTypeDef",
    "ListAssessmentRunAgentsRequestTypeDef",
    "ListAssessmentRunAgentsResponseResponseTypeDef",
    "ListAssessmentRunsRequestTypeDef",
    "ListAssessmentRunsResponseResponseTypeDef",
    "ListAssessmentTargetsRequestTypeDef",
    "ListAssessmentTargetsResponseResponseTypeDef",
    "ListAssessmentTemplatesRequestTypeDef",
    "ListAssessmentTemplatesResponseResponseTypeDef",
    "ListEventSubscriptionsRequestTypeDef",
    "ListEventSubscriptionsResponseResponseTypeDef",
    "ListExclusionsRequestTypeDef",
    "ListExclusionsResponseResponseTypeDef",
    "ListFindingsRequestTypeDef",
    "ListFindingsResponseResponseTypeDef",
    "ListRulesPackagesRequestTypeDef",
    "ListRulesPackagesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "PreviewAgentsRequestTypeDef",
    "PreviewAgentsResponseResponseTypeDef",
    "PrivateIpTypeDef",
    "RegisterCrossAccountAccessRoleRequestTypeDef",
    "RemoveAttributesFromFindingsRequestTypeDef",
    "RemoveAttributesFromFindingsResponseResponseTypeDef",
    "ResourceGroupTagTypeDef",
    "ResourceGroupTypeDef",
    "ResponseMetadataTypeDef",
    "RulesPackageTypeDef",
    "ScopeTypeDef",
    "SecurityGroupTypeDef",
    "SetTagsForResourceRequestTypeDef",
    "StartAssessmentRunRequestTypeDef",
    "StartAssessmentRunResponseResponseTypeDef",
    "StopAssessmentRunRequestTypeDef",
    "SubscribeToEventRequestTypeDef",
    "SubscriptionTypeDef",
    "TagTypeDef",
    "TelemetryMetadataTypeDef",
    "TimestampRangeTypeDef",
    "UnsubscribeFromEventRequestTypeDef",
    "UpdateAssessmentTargetRequestTypeDef",
)

AddAttributesToFindingsRequestTypeDef = TypedDict(
    "AddAttributesToFindingsRequestTypeDef",
    {
        "findingArns": List[str],
        "attributes": List["AttributeTypeDef"],
    },
)

AddAttributesToFindingsResponseResponseTypeDef = TypedDict(
    "AddAttributesToFindingsResponseResponseTypeDef",
    {
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AgentFilterTypeDef = TypedDict(
    "AgentFilterTypeDef",
    {
        "agentHealths": List[AgentHealthType],
        "agentHealthCodes": List[AgentHealthCodeType],
    },
)

_RequiredAgentPreviewTypeDef = TypedDict(
    "_RequiredAgentPreviewTypeDef",
    {
        "agentId": str,
    },
)
_OptionalAgentPreviewTypeDef = TypedDict(
    "_OptionalAgentPreviewTypeDef",
    {
        "hostname": str,
        "autoScalingGroup": str,
        "agentHealth": AgentHealthType,
        "agentVersion": str,
        "operatingSystem": str,
        "kernelVersion": str,
        "ipv4Address": str,
    },
    total=False,
)


class AgentPreviewTypeDef(_RequiredAgentPreviewTypeDef, _OptionalAgentPreviewTypeDef):
    pass


_RequiredAssessmentRunAgentTypeDef = TypedDict(
    "_RequiredAssessmentRunAgentTypeDef",
    {
        "agentId": str,
        "assessmentRunArn": str,
        "agentHealth": AgentHealthType,
        "agentHealthCode": AgentHealthCodeType,
        "telemetryMetadata": List["TelemetryMetadataTypeDef"],
    },
)
_OptionalAssessmentRunAgentTypeDef = TypedDict(
    "_OptionalAssessmentRunAgentTypeDef",
    {
        "agentHealthDetails": str,
        "autoScalingGroup": str,
    },
    total=False,
)


class AssessmentRunAgentTypeDef(
    _RequiredAssessmentRunAgentTypeDef, _OptionalAssessmentRunAgentTypeDef
):
    pass


AssessmentRunFilterTypeDef = TypedDict(
    "AssessmentRunFilterTypeDef",
    {
        "namePattern": str,
        "states": List[AssessmentRunStateType],
        "durationRange": "DurationRangeTypeDef",
        "rulesPackageArns": List[str],
        "startTimeRange": "TimestampRangeTypeDef",
        "completionTimeRange": "TimestampRangeTypeDef",
        "stateChangeTimeRange": "TimestampRangeTypeDef",
    },
    total=False,
)

_RequiredAssessmentRunNotificationTypeDef = TypedDict(
    "_RequiredAssessmentRunNotificationTypeDef",
    {
        "date": datetime,
        "event": InspectorEventType,
        "error": bool,
    },
)
_OptionalAssessmentRunNotificationTypeDef = TypedDict(
    "_OptionalAssessmentRunNotificationTypeDef",
    {
        "message": str,
        "snsTopicArn": str,
        "snsPublishStatusCode": AssessmentRunNotificationSnsStatusCodeType,
    },
    total=False,
)


class AssessmentRunNotificationTypeDef(
    _RequiredAssessmentRunNotificationTypeDef, _OptionalAssessmentRunNotificationTypeDef
):
    pass


AssessmentRunStateChangeTypeDef = TypedDict(
    "AssessmentRunStateChangeTypeDef",
    {
        "stateChangedAt": datetime,
        "state": AssessmentRunStateType,
    },
)

_RequiredAssessmentRunTypeDef = TypedDict(
    "_RequiredAssessmentRunTypeDef",
    {
        "arn": str,
        "name": str,
        "assessmentTemplateArn": str,
        "state": AssessmentRunStateType,
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
        "userAttributesForFindings": List["AttributeTypeDef"],
        "createdAt": datetime,
        "stateChangedAt": datetime,
        "dataCollected": bool,
        "stateChanges": List["AssessmentRunStateChangeTypeDef"],
        "notifications": List["AssessmentRunNotificationTypeDef"],
        "findingCounts": Dict[SeverityType, int],
    },
)
_OptionalAssessmentRunTypeDef = TypedDict(
    "_OptionalAssessmentRunTypeDef",
    {
        "startedAt": datetime,
        "completedAt": datetime,
    },
    total=False,
)


class AssessmentRunTypeDef(_RequiredAssessmentRunTypeDef, _OptionalAssessmentRunTypeDef):
    pass


AssessmentTargetFilterTypeDef = TypedDict(
    "AssessmentTargetFilterTypeDef",
    {
        "assessmentTargetNamePattern": str,
    },
    total=False,
)

_RequiredAssessmentTargetTypeDef = TypedDict(
    "_RequiredAssessmentTargetTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
_OptionalAssessmentTargetTypeDef = TypedDict(
    "_OptionalAssessmentTargetTypeDef",
    {
        "resourceGroupArn": str,
    },
    total=False,
)


class AssessmentTargetTypeDef(_RequiredAssessmentTargetTypeDef, _OptionalAssessmentTargetTypeDef):
    pass


AssessmentTemplateFilterTypeDef = TypedDict(
    "AssessmentTemplateFilterTypeDef",
    {
        "namePattern": str,
        "durationRange": "DurationRangeTypeDef",
        "rulesPackageArns": List[str],
    },
    total=False,
)

_RequiredAssessmentTemplateTypeDef = TypedDict(
    "_RequiredAssessmentTemplateTypeDef",
    {
        "arn": str,
        "name": str,
        "assessmentTargetArn": str,
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
        "userAttributesForFindings": List["AttributeTypeDef"],
        "assessmentRunCount": int,
        "createdAt": datetime,
    },
)
_OptionalAssessmentTemplateTypeDef = TypedDict(
    "_OptionalAssessmentTemplateTypeDef",
    {
        "lastAssessmentRunArn": str,
    },
    total=False,
)


class AssessmentTemplateTypeDef(
    _RequiredAssessmentTemplateTypeDef, _OptionalAssessmentTemplateTypeDef
):
    pass


_RequiredAssetAttributesTypeDef = TypedDict(
    "_RequiredAssetAttributesTypeDef",
    {
        "schemaVersion": int,
    },
)
_OptionalAssetAttributesTypeDef = TypedDict(
    "_OptionalAssetAttributesTypeDef",
    {
        "agentId": str,
        "autoScalingGroup": str,
        "amiId": str,
        "hostname": str,
        "ipv4Addresses": List[str],
        "tags": List["TagTypeDef"],
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
    },
    total=False,
)


class AssetAttributesTypeDef(_RequiredAssetAttributesTypeDef, _OptionalAssetAttributesTypeDef):
    pass


_RequiredAttributeTypeDef = TypedDict(
    "_RequiredAttributeTypeDef",
    {
        "key": str,
    },
)
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {
        "value": str,
    },
    total=False,
)


class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass


_RequiredCreateAssessmentTargetRequestTypeDef = TypedDict(
    "_RequiredCreateAssessmentTargetRequestTypeDef",
    {
        "assessmentTargetName": str,
    },
)
_OptionalCreateAssessmentTargetRequestTypeDef = TypedDict(
    "_OptionalCreateAssessmentTargetRequestTypeDef",
    {
        "resourceGroupArn": str,
    },
    total=False,
)


class CreateAssessmentTargetRequestTypeDef(
    _RequiredCreateAssessmentTargetRequestTypeDef, _OptionalCreateAssessmentTargetRequestTypeDef
):
    pass


CreateAssessmentTargetResponseResponseTypeDef = TypedDict(
    "CreateAssessmentTargetResponseResponseTypeDef",
    {
        "assessmentTargetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssessmentTemplateRequestTypeDef = TypedDict(
    "_RequiredCreateAssessmentTemplateRequestTypeDef",
    {
        "assessmentTargetArn": str,
        "assessmentTemplateName": str,
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
    },
)
_OptionalCreateAssessmentTemplateRequestTypeDef = TypedDict(
    "_OptionalCreateAssessmentTemplateRequestTypeDef",
    {
        "userAttributesForFindings": List["AttributeTypeDef"],
    },
    total=False,
)


class CreateAssessmentTemplateRequestTypeDef(
    _RequiredCreateAssessmentTemplateRequestTypeDef, _OptionalCreateAssessmentTemplateRequestTypeDef
):
    pass


CreateAssessmentTemplateResponseResponseTypeDef = TypedDict(
    "CreateAssessmentTemplateResponseResponseTypeDef",
    {
        "assessmentTemplateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateExclusionsPreviewRequestTypeDef = TypedDict(
    "CreateExclusionsPreviewRequestTypeDef",
    {
        "assessmentTemplateArn": str,
    },
)

CreateExclusionsPreviewResponseResponseTypeDef = TypedDict(
    "CreateExclusionsPreviewResponseResponseTypeDef",
    {
        "previewToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourceGroupRequestTypeDef = TypedDict(
    "CreateResourceGroupRequestTypeDef",
    {
        "resourceGroupTags": List["ResourceGroupTagTypeDef"],
    },
)

CreateResourceGroupResponseResponseTypeDef = TypedDict(
    "CreateResourceGroupResponseResponseTypeDef",
    {
        "resourceGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAssessmentRunRequestTypeDef = TypedDict(
    "DeleteAssessmentRunRequestTypeDef",
    {
        "assessmentRunArn": str,
    },
)

DeleteAssessmentTargetRequestTypeDef = TypedDict(
    "DeleteAssessmentTargetRequestTypeDef",
    {
        "assessmentTargetArn": str,
    },
)

DeleteAssessmentTemplateRequestTypeDef = TypedDict(
    "DeleteAssessmentTemplateRequestTypeDef",
    {
        "assessmentTemplateArn": str,
    },
)

DescribeAssessmentRunsRequestTypeDef = TypedDict(
    "DescribeAssessmentRunsRequestTypeDef",
    {
        "assessmentRunArns": List[str],
    },
)

DescribeAssessmentRunsResponseResponseTypeDef = TypedDict(
    "DescribeAssessmentRunsResponseResponseTypeDef",
    {
        "assessmentRuns": List["AssessmentRunTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssessmentTargetsRequestTypeDef = TypedDict(
    "DescribeAssessmentTargetsRequestTypeDef",
    {
        "assessmentTargetArns": List[str],
    },
)

DescribeAssessmentTargetsResponseResponseTypeDef = TypedDict(
    "DescribeAssessmentTargetsResponseResponseTypeDef",
    {
        "assessmentTargets": List["AssessmentTargetTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssessmentTemplatesRequestTypeDef = TypedDict(
    "DescribeAssessmentTemplatesRequestTypeDef",
    {
        "assessmentTemplateArns": List[str],
    },
)

DescribeAssessmentTemplatesResponseResponseTypeDef = TypedDict(
    "DescribeAssessmentTemplatesResponseResponseTypeDef",
    {
        "assessmentTemplates": List["AssessmentTemplateTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCrossAccountAccessRoleResponseResponseTypeDef = TypedDict(
    "DescribeCrossAccountAccessRoleResponseResponseTypeDef",
    {
        "roleArn": str,
        "valid": bool,
        "registeredAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeExclusionsRequestTypeDef = TypedDict(
    "_RequiredDescribeExclusionsRequestTypeDef",
    {
        "exclusionArns": List[str],
    },
)
_OptionalDescribeExclusionsRequestTypeDef = TypedDict(
    "_OptionalDescribeExclusionsRequestTypeDef",
    {
        "locale": Literal["EN_US"],
    },
    total=False,
)


class DescribeExclusionsRequestTypeDef(
    _RequiredDescribeExclusionsRequestTypeDef, _OptionalDescribeExclusionsRequestTypeDef
):
    pass


DescribeExclusionsResponseResponseTypeDef = TypedDict(
    "DescribeExclusionsResponseResponseTypeDef",
    {
        "exclusions": Dict[str, "ExclusionTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFindingsRequestTypeDef = TypedDict(
    "_RequiredDescribeFindingsRequestTypeDef",
    {
        "findingArns": List[str],
    },
)
_OptionalDescribeFindingsRequestTypeDef = TypedDict(
    "_OptionalDescribeFindingsRequestTypeDef",
    {
        "locale": Literal["EN_US"],
    },
    total=False,
)


class DescribeFindingsRequestTypeDef(
    _RequiredDescribeFindingsRequestTypeDef, _OptionalDescribeFindingsRequestTypeDef
):
    pass


DescribeFindingsResponseResponseTypeDef = TypedDict(
    "DescribeFindingsResponseResponseTypeDef",
    {
        "findings": List["FindingTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourceGroupsRequestTypeDef = TypedDict(
    "DescribeResourceGroupsRequestTypeDef",
    {
        "resourceGroupArns": List[str],
    },
)

DescribeResourceGroupsResponseResponseTypeDef = TypedDict(
    "DescribeResourceGroupsResponseResponseTypeDef",
    {
        "resourceGroups": List["ResourceGroupTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRulesPackagesRequestTypeDef = TypedDict(
    "_RequiredDescribeRulesPackagesRequestTypeDef",
    {
        "rulesPackageArns": List[str],
    },
)
_OptionalDescribeRulesPackagesRequestTypeDef = TypedDict(
    "_OptionalDescribeRulesPackagesRequestTypeDef",
    {
        "locale": Literal["EN_US"],
    },
    total=False,
)


class DescribeRulesPackagesRequestTypeDef(
    _RequiredDescribeRulesPackagesRequestTypeDef, _OptionalDescribeRulesPackagesRequestTypeDef
):
    pass


DescribeRulesPackagesResponseResponseTypeDef = TypedDict(
    "DescribeRulesPackagesResponseResponseTypeDef",
    {
        "rulesPackages": List["RulesPackageTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DurationRangeTypeDef = TypedDict(
    "DurationRangeTypeDef",
    {
        "minSeconds": int,
        "maxSeconds": int,
    },
    total=False,
)

EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "event": InspectorEventType,
        "subscribedAt": datetime,
    },
)

_RequiredExclusionPreviewTypeDef = TypedDict(
    "_RequiredExclusionPreviewTypeDef",
    {
        "title": str,
        "description": str,
        "recommendation": str,
        "scopes": List["ScopeTypeDef"],
    },
)
_OptionalExclusionPreviewTypeDef = TypedDict(
    "_OptionalExclusionPreviewTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
    },
    total=False,
)


class ExclusionPreviewTypeDef(_RequiredExclusionPreviewTypeDef, _OptionalExclusionPreviewTypeDef):
    pass


_RequiredExclusionTypeDef = TypedDict(
    "_RequiredExclusionTypeDef",
    {
        "arn": str,
        "title": str,
        "description": str,
        "recommendation": str,
        "scopes": List["ScopeTypeDef"],
    },
)
_OptionalExclusionTypeDef = TypedDict(
    "_OptionalExclusionTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
    },
    total=False,
)


class ExclusionTypeDef(_RequiredExclusionTypeDef, _OptionalExclusionTypeDef):
    pass


FailedItemDetailsTypeDef = TypedDict(
    "FailedItemDetailsTypeDef",
    {
        "failureCode": FailedItemErrorCodeType,
        "retryable": bool,
    },
)

FindingFilterTypeDef = TypedDict(
    "FindingFilterTypeDef",
    {
        "agentIds": List[str],
        "autoScalingGroups": List[str],
        "ruleNames": List[str],
        "severities": List[SeverityType],
        "rulesPackageArns": List[str],
        "attributes": List["AttributeTypeDef"],
        "userAttributes": List["AttributeTypeDef"],
        "creationTimeRange": "TimestampRangeTypeDef",
    },
    total=False,
)

_RequiredFindingTypeDef = TypedDict(
    "_RequiredFindingTypeDef",
    {
        "arn": str,
        "attributes": List["AttributeTypeDef"],
        "userAttributes": List["AttributeTypeDef"],
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
_OptionalFindingTypeDef = TypedDict(
    "_OptionalFindingTypeDef",
    {
        "schemaVersion": int,
        "service": str,
        "serviceAttributes": "InspectorServiceAttributesTypeDef",
        "assetType": Literal["ec2-instance"],
        "assetAttributes": "AssetAttributesTypeDef",
        "id": str,
        "title": str,
        "description": str,
        "recommendation": str,
        "severity": SeverityType,
        "numericSeverity": float,
        "confidence": int,
        "indicatorOfCompromise": bool,
    },
    total=False,
)


class FindingTypeDef(_RequiredFindingTypeDef, _OptionalFindingTypeDef):
    pass


GetAssessmentReportRequestTypeDef = TypedDict(
    "GetAssessmentReportRequestTypeDef",
    {
        "assessmentRunArn": str,
        "reportFileFormat": ReportFileFormatType,
        "reportType": ReportTypeType,
    },
)

GetAssessmentReportResponseResponseTypeDef = TypedDict(
    "GetAssessmentReportResponseResponseTypeDef",
    {
        "status": ReportStatusType,
        "url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetExclusionsPreviewRequestTypeDef = TypedDict(
    "_RequiredGetExclusionsPreviewRequestTypeDef",
    {
        "assessmentTemplateArn": str,
        "previewToken": str,
    },
)
_OptionalGetExclusionsPreviewRequestTypeDef = TypedDict(
    "_OptionalGetExclusionsPreviewRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "locale": Literal["EN_US"],
    },
    total=False,
)


class GetExclusionsPreviewRequestTypeDef(
    _RequiredGetExclusionsPreviewRequestTypeDef, _OptionalGetExclusionsPreviewRequestTypeDef
):
    pass


GetExclusionsPreviewResponseResponseTypeDef = TypedDict(
    "GetExclusionsPreviewResponseResponseTypeDef",
    {
        "previewStatus": PreviewStatusType,
        "exclusionPreviews": List["ExclusionPreviewTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTelemetryMetadataRequestTypeDef = TypedDict(
    "GetTelemetryMetadataRequestTypeDef",
    {
        "assessmentRunArn": str,
    },
)

GetTelemetryMetadataResponseResponseTypeDef = TypedDict(
    "GetTelemetryMetadataResponseResponseTypeDef",
    {
        "telemetryMetadata": List["TelemetryMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInspectorServiceAttributesTypeDef = TypedDict(
    "_RequiredInspectorServiceAttributesTypeDef",
    {
        "schemaVersion": int,
    },
)
_OptionalInspectorServiceAttributesTypeDef = TypedDict(
    "_OptionalInspectorServiceAttributesTypeDef",
    {
        "assessmentRunArn": str,
        "rulesPackageArn": str,
    },
    total=False,
)


class InspectorServiceAttributesTypeDef(
    _RequiredInspectorServiceAttributesTypeDef, _OptionalInspectorServiceAttributesTypeDef
):
    pass


_RequiredListAssessmentRunAgentsRequestTypeDef = TypedDict(
    "_RequiredListAssessmentRunAgentsRequestTypeDef",
    {
        "assessmentRunArn": str,
    },
)
_OptionalListAssessmentRunAgentsRequestTypeDef = TypedDict(
    "_OptionalListAssessmentRunAgentsRequestTypeDef",
    {
        "filter": "AgentFilterTypeDef",
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListAssessmentRunAgentsRequestTypeDef(
    _RequiredListAssessmentRunAgentsRequestTypeDef, _OptionalListAssessmentRunAgentsRequestTypeDef
):
    pass


ListAssessmentRunAgentsResponseResponseTypeDef = TypedDict(
    "ListAssessmentRunAgentsResponseResponseTypeDef",
    {
        "assessmentRunAgents": List["AssessmentRunAgentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentRunsRequestTypeDef = TypedDict(
    "ListAssessmentRunsRequestTypeDef",
    {
        "assessmentTemplateArns": List[str],
        "filter": "AssessmentRunFilterTypeDef",
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAssessmentRunsResponseResponseTypeDef = TypedDict(
    "ListAssessmentRunsResponseResponseTypeDef",
    {
        "assessmentRunArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentTargetsRequestTypeDef = TypedDict(
    "ListAssessmentTargetsRequestTypeDef",
    {
        "filter": "AssessmentTargetFilterTypeDef",
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAssessmentTargetsResponseResponseTypeDef = TypedDict(
    "ListAssessmentTargetsResponseResponseTypeDef",
    {
        "assessmentTargetArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentTemplatesRequestTypeDef = TypedDict(
    "ListAssessmentTemplatesRequestTypeDef",
    {
        "assessmentTargetArns": List[str],
        "filter": "AssessmentTemplateFilterTypeDef",
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAssessmentTemplatesResponseResponseTypeDef = TypedDict(
    "ListAssessmentTemplatesResponseResponseTypeDef",
    {
        "assessmentTemplateArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventSubscriptionsRequestTypeDef = TypedDict(
    "ListEventSubscriptionsRequestTypeDef",
    {
        "resourceArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListEventSubscriptionsResponseResponseTypeDef = TypedDict(
    "ListEventSubscriptionsResponseResponseTypeDef",
    {
        "subscriptions": List["SubscriptionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListExclusionsRequestTypeDef = TypedDict(
    "_RequiredListExclusionsRequestTypeDef",
    {
        "assessmentRunArn": str,
    },
)
_OptionalListExclusionsRequestTypeDef = TypedDict(
    "_OptionalListExclusionsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListExclusionsRequestTypeDef(
    _RequiredListExclusionsRequestTypeDef, _OptionalListExclusionsRequestTypeDef
):
    pass


ListExclusionsResponseResponseTypeDef = TypedDict(
    "ListExclusionsResponseResponseTypeDef",
    {
        "exclusionArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFindingsRequestTypeDef = TypedDict(
    "ListFindingsRequestTypeDef",
    {
        "assessmentRunArns": List[str],
        "filter": "FindingFilterTypeDef",
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListFindingsResponseResponseTypeDef = TypedDict(
    "ListFindingsResponseResponseTypeDef",
    {
        "findingArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRulesPackagesRequestTypeDef = TypedDict(
    "ListRulesPackagesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListRulesPackagesResponseResponseTypeDef = TypedDict(
    "ListRulesPackagesResponseResponseTypeDef",
    {
        "rulesPackageArns": List[str],
        "nextToken": str,
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
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "networkInterfaceId": str,
        "subnetId": str,
        "vpcId": str,
        "privateDnsName": str,
        "privateIpAddress": str,
        "privateIpAddresses": List["PrivateIpTypeDef"],
        "publicDnsName": str,
        "publicIp": str,
        "ipv6Addresses": List[str],
        "securityGroups": List["SecurityGroupTypeDef"],
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

_RequiredPreviewAgentsRequestTypeDef = TypedDict(
    "_RequiredPreviewAgentsRequestTypeDef",
    {
        "previewAgentsArn": str,
    },
)
_OptionalPreviewAgentsRequestTypeDef = TypedDict(
    "_OptionalPreviewAgentsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class PreviewAgentsRequestTypeDef(
    _RequiredPreviewAgentsRequestTypeDef, _OptionalPreviewAgentsRequestTypeDef
):
    pass


PreviewAgentsResponseResponseTypeDef = TypedDict(
    "PreviewAgentsResponseResponseTypeDef",
    {
        "agentPreviews": List["AgentPreviewTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PrivateIpTypeDef = TypedDict(
    "PrivateIpTypeDef",
    {
        "privateDnsName": str,
        "privateIpAddress": str,
    },
    total=False,
)

RegisterCrossAccountAccessRoleRequestTypeDef = TypedDict(
    "RegisterCrossAccountAccessRoleRequestTypeDef",
    {
        "roleArn": str,
    },
)

RemoveAttributesFromFindingsRequestTypeDef = TypedDict(
    "RemoveAttributesFromFindingsRequestTypeDef",
    {
        "findingArns": List[str],
        "attributeKeys": List[str],
    },
)

RemoveAttributesFromFindingsResponseResponseTypeDef = TypedDict(
    "RemoveAttributesFromFindingsResponseResponseTypeDef",
    {
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredResourceGroupTagTypeDef = TypedDict(
    "_RequiredResourceGroupTagTypeDef",
    {
        "key": str,
    },
)
_OptionalResourceGroupTagTypeDef = TypedDict(
    "_OptionalResourceGroupTagTypeDef",
    {
        "value": str,
    },
    total=False,
)


class ResourceGroupTagTypeDef(_RequiredResourceGroupTagTypeDef, _OptionalResourceGroupTagTypeDef):
    pass


ResourceGroupTypeDef = TypedDict(
    "ResourceGroupTypeDef",
    {
        "arn": str,
        "tags": List["ResourceGroupTagTypeDef"],
        "createdAt": datetime,
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

_RequiredRulesPackageTypeDef = TypedDict(
    "_RequiredRulesPackageTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "provider": str,
    },
)
_OptionalRulesPackageTypeDef = TypedDict(
    "_OptionalRulesPackageTypeDef",
    {
        "description": str,
    },
    total=False,
)


class RulesPackageTypeDef(_RequiredRulesPackageTypeDef, _OptionalRulesPackageTypeDef):
    pass


ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "key": ScopeTypeType,
        "value": str,
    },
    total=False,
)

SecurityGroupTypeDef = TypedDict(
    "SecurityGroupTypeDef",
    {
        "groupName": str,
        "groupId": str,
    },
    total=False,
)

_RequiredSetTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredSetTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalSetTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalSetTagsForResourceRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class SetTagsForResourceRequestTypeDef(
    _RequiredSetTagsForResourceRequestTypeDef, _OptionalSetTagsForResourceRequestTypeDef
):
    pass


_RequiredStartAssessmentRunRequestTypeDef = TypedDict(
    "_RequiredStartAssessmentRunRequestTypeDef",
    {
        "assessmentTemplateArn": str,
    },
)
_OptionalStartAssessmentRunRequestTypeDef = TypedDict(
    "_OptionalStartAssessmentRunRequestTypeDef",
    {
        "assessmentRunName": str,
    },
    total=False,
)


class StartAssessmentRunRequestTypeDef(
    _RequiredStartAssessmentRunRequestTypeDef, _OptionalStartAssessmentRunRequestTypeDef
):
    pass


StartAssessmentRunResponseResponseTypeDef = TypedDict(
    "StartAssessmentRunResponseResponseTypeDef",
    {
        "assessmentRunArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopAssessmentRunRequestTypeDef = TypedDict(
    "_RequiredStopAssessmentRunRequestTypeDef",
    {
        "assessmentRunArn": str,
    },
)
_OptionalStopAssessmentRunRequestTypeDef = TypedDict(
    "_OptionalStopAssessmentRunRequestTypeDef",
    {
        "stopAction": StopActionType,
    },
    total=False,
)


class StopAssessmentRunRequestTypeDef(
    _RequiredStopAssessmentRunRequestTypeDef, _OptionalStopAssessmentRunRequestTypeDef
):
    pass


SubscribeToEventRequestTypeDef = TypedDict(
    "SubscribeToEventRequestTypeDef",
    {
        "resourceArn": str,
        "event": InspectorEventType,
        "topicArn": str,
    },
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "resourceArn": str,
        "topicArn": str,
        "eventSubscriptions": List["EventSubscriptionTypeDef"],
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "value": str,
    },
    total=False,
)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


_RequiredTelemetryMetadataTypeDef = TypedDict(
    "_RequiredTelemetryMetadataTypeDef",
    {
        "messageType": str,
        "count": int,
    },
)
_OptionalTelemetryMetadataTypeDef = TypedDict(
    "_OptionalTelemetryMetadataTypeDef",
    {
        "dataSize": int,
    },
    total=False,
)


class TelemetryMetadataTypeDef(
    _RequiredTelemetryMetadataTypeDef, _OptionalTelemetryMetadataTypeDef
):
    pass


TimestampRangeTypeDef = TypedDict(
    "TimestampRangeTypeDef",
    {
        "beginDate": Union[datetime, str],
        "endDate": Union[datetime, str],
    },
    total=False,
)

UnsubscribeFromEventRequestTypeDef = TypedDict(
    "UnsubscribeFromEventRequestTypeDef",
    {
        "resourceArn": str,
        "event": InspectorEventType,
        "topicArn": str,
    },
)

_RequiredUpdateAssessmentTargetRequestTypeDef = TypedDict(
    "_RequiredUpdateAssessmentTargetRequestTypeDef",
    {
        "assessmentTargetArn": str,
        "assessmentTargetName": str,
    },
)
_OptionalUpdateAssessmentTargetRequestTypeDef = TypedDict(
    "_OptionalUpdateAssessmentTargetRequestTypeDef",
    {
        "resourceGroupArn": str,
    },
    total=False,
)


class UpdateAssessmentTargetRequestTypeDef(
    _RequiredUpdateAssessmentTargetRequestTypeDef, _OptionalUpdateAssessmentTargetRequestTypeDef
):
    pass
