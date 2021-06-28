"""
Type annotations for accessanalyzer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_accessanalyzer.type_defs import AccessPreviewFindingTypeDef

    data: AccessPreviewFindingTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AccessPreviewStatusReasonCodeType,
    AccessPreviewStatusType,
    AclPermissionType,
    AnalyzerStatusType,
    FindingChangeTypeType,
    FindingSourceTypeType,
    FindingStatusType,
    FindingStatusUpdateType,
    JobErrorCodeType,
    JobStatusType,
    KmsGrantOperationType,
    LocaleType,
    OrderByType,
    PolicyTypeType,
    ReasonCodeType,
    ResourceTypeType,
    TypeType,
    ValidatePolicyFindingTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessPreviewFindingTypeDef",
    "AccessPreviewStatusReasonTypeDef",
    "AccessPreviewSummaryTypeDef",
    "AccessPreviewTypeDef",
    "AclGranteeTypeDef",
    "AnalyzedResourceSummaryTypeDef",
    "AnalyzedResourceTypeDef",
    "AnalyzerSummaryTypeDef",
    "ApplyArchiveRuleRequestTypeDef",
    "ArchiveRuleSummaryTypeDef",
    "CancelPolicyGenerationRequestTypeDef",
    "CloudTrailDetailsTypeDef",
    "CloudTrailPropertiesTypeDef",
    "ConfigurationTypeDef",
    "CreateAccessPreviewRequestTypeDef",
    "CreateAccessPreviewResponseResponseTypeDef",
    "CreateAnalyzerRequestTypeDef",
    "CreateAnalyzerResponseResponseTypeDef",
    "CreateArchiveRuleRequestTypeDef",
    "CriterionTypeDef",
    "DeleteAnalyzerRequestTypeDef",
    "DeleteArchiveRuleRequestTypeDef",
    "FindingSourceDetailTypeDef",
    "FindingSourceTypeDef",
    "FindingSummaryTypeDef",
    "FindingTypeDef",
    "GeneratedPolicyPropertiesTypeDef",
    "GeneratedPolicyResultTypeDef",
    "GeneratedPolicyTypeDef",
    "GetAccessPreviewRequestTypeDef",
    "GetAccessPreviewResponseResponseTypeDef",
    "GetAnalyzedResourceRequestTypeDef",
    "GetAnalyzedResourceResponseResponseTypeDef",
    "GetAnalyzerRequestTypeDef",
    "GetAnalyzerResponseResponseTypeDef",
    "GetArchiveRuleRequestTypeDef",
    "GetArchiveRuleResponseResponseTypeDef",
    "GetFindingRequestTypeDef",
    "GetFindingResponseResponseTypeDef",
    "GetGeneratedPolicyRequestTypeDef",
    "GetGeneratedPolicyResponseResponseTypeDef",
    "IamRoleConfigurationTypeDef",
    "InlineArchiveRuleTypeDef",
    "JobDetailsTypeDef",
    "JobErrorTypeDef",
    "KmsGrantConfigurationTypeDef",
    "KmsGrantConstraintsTypeDef",
    "KmsKeyConfigurationTypeDef",
    "ListAccessPreviewFindingsRequestTypeDef",
    "ListAccessPreviewFindingsResponseResponseTypeDef",
    "ListAccessPreviewsRequestTypeDef",
    "ListAccessPreviewsResponseResponseTypeDef",
    "ListAnalyzedResourcesRequestTypeDef",
    "ListAnalyzedResourcesResponseResponseTypeDef",
    "ListAnalyzersRequestTypeDef",
    "ListAnalyzersResponseResponseTypeDef",
    "ListArchiveRulesRequestTypeDef",
    "ListArchiveRulesResponseResponseTypeDef",
    "ListFindingsRequestTypeDef",
    "ListFindingsResponseResponseTypeDef",
    "ListPolicyGenerationsRequestTypeDef",
    "ListPolicyGenerationsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "LocationTypeDef",
    "NetworkOriginConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PathElementTypeDef",
    "PolicyGenerationDetailsTypeDef",
    "PolicyGenerationTypeDef",
    "PositionTypeDef",
    "ResponseMetadataTypeDef",
    "S3AccessPointConfigurationTypeDef",
    "S3BucketAclGrantConfigurationTypeDef",
    "S3BucketConfigurationTypeDef",
    "S3PublicAccessBlockConfigurationTypeDef",
    "SecretsManagerSecretConfigurationTypeDef",
    "SortCriteriaTypeDef",
    "SpanTypeDef",
    "SqsQueueConfigurationTypeDef",
    "StartPolicyGenerationRequestTypeDef",
    "StartPolicyGenerationResponseResponseTypeDef",
    "StartResourceScanRequestTypeDef",
    "StatusReasonTypeDef",
    "SubstringTypeDef",
    "TagResourceRequestTypeDef",
    "TrailPropertiesTypeDef",
    "TrailTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateArchiveRuleRequestTypeDef",
    "UpdateFindingsRequestTypeDef",
    "ValidatePolicyFindingTypeDef",
    "ValidatePolicyRequestTypeDef",
    "ValidatePolicyResponseResponseTypeDef",
    "VpcConfigurationTypeDef",
)

_RequiredAccessPreviewFindingTypeDef = TypedDict(
    "_RequiredAccessPreviewFindingTypeDef",
    {
        "changeType": FindingChangeTypeType,
        "createdAt": datetime,
        "id": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
        "status": FindingStatusType,
    },
)
_OptionalAccessPreviewFindingTypeDef = TypedDict(
    "_OptionalAccessPreviewFindingTypeDef",
    {
        "action": List[str],
        "condition": Dict[str, str],
        "error": str,
        "existingFindingId": str,
        "existingFindingStatus": FindingStatusType,
        "isPublic": bool,
        "principal": Dict[str, str],
        "resource": str,
        "sources": List["FindingSourceTypeDef"],
    },
    total=False,
)


class AccessPreviewFindingTypeDef(
    _RequiredAccessPreviewFindingTypeDef, _OptionalAccessPreviewFindingTypeDef
):
    pass


AccessPreviewStatusReasonTypeDef = TypedDict(
    "AccessPreviewStatusReasonTypeDef",
    {
        "code": AccessPreviewStatusReasonCodeType,
    },
)

_RequiredAccessPreviewSummaryTypeDef = TypedDict(
    "_RequiredAccessPreviewSummaryTypeDef",
    {
        "analyzerArn": str,
        "createdAt": datetime,
        "id": str,
        "status": AccessPreviewStatusType,
    },
)
_OptionalAccessPreviewSummaryTypeDef = TypedDict(
    "_OptionalAccessPreviewSummaryTypeDef",
    {
        "statusReason": "AccessPreviewStatusReasonTypeDef",
    },
    total=False,
)


class AccessPreviewSummaryTypeDef(
    _RequiredAccessPreviewSummaryTypeDef, _OptionalAccessPreviewSummaryTypeDef
):
    pass


_RequiredAccessPreviewTypeDef = TypedDict(
    "_RequiredAccessPreviewTypeDef",
    {
        "analyzerArn": str,
        "configurations": Dict[str, "ConfigurationTypeDef"],
        "createdAt": datetime,
        "id": str,
        "status": AccessPreviewStatusType,
    },
)
_OptionalAccessPreviewTypeDef = TypedDict(
    "_OptionalAccessPreviewTypeDef",
    {
        "statusReason": "AccessPreviewStatusReasonTypeDef",
    },
    total=False,
)


class AccessPreviewTypeDef(_RequiredAccessPreviewTypeDef, _OptionalAccessPreviewTypeDef):
    pass


AclGranteeTypeDef = TypedDict(
    "AclGranteeTypeDef",
    {
        "id": str,
        "uri": str,
    },
    total=False,
)

AnalyzedResourceSummaryTypeDef = TypedDict(
    "AnalyzedResourceSummaryTypeDef",
    {
        "resourceArn": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
    },
)

_RequiredAnalyzedResourceTypeDef = TypedDict(
    "_RequiredAnalyzedResourceTypeDef",
    {
        "analyzedAt": datetime,
        "createdAt": datetime,
        "isPublic": bool,
        "resourceArn": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
        "updatedAt": datetime,
    },
)
_OptionalAnalyzedResourceTypeDef = TypedDict(
    "_OptionalAnalyzedResourceTypeDef",
    {
        "actions": List[str],
        "error": str,
        "sharedVia": List[str],
        "status": FindingStatusType,
    },
    total=False,
)


class AnalyzedResourceTypeDef(_RequiredAnalyzedResourceTypeDef, _OptionalAnalyzedResourceTypeDef):
    pass


_RequiredAnalyzerSummaryTypeDef = TypedDict(
    "_RequiredAnalyzerSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "name": str,
        "status": AnalyzerStatusType,
        "type": TypeType,
    },
)
_OptionalAnalyzerSummaryTypeDef = TypedDict(
    "_OptionalAnalyzerSummaryTypeDef",
    {
        "lastResourceAnalyzed": str,
        "lastResourceAnalyzedAt": datetime,
        "statusReason": "StatusReasonTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class AnalyzerSummaryTypeDef(_RequiredAnalyzerSummaryTypeDef, _OptionalAnalyzerSummaryTypeDef):
    pass


_RequiredApplyArchiveRuleRequestTypeDef = TypedDict(
    "_RequiredApplyArchiveRuleRequestTypeDef",
    {
        "analyzerArn": str,
        "ruleName": str,
    },
)
_OptionalApplyArchiveRuleRequestTypeDef = TypedDict(
    "_OptionalApplyArchiveRuleRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class ApplyArchiveRuleRequestTypeDef(
    _RequiredApplyArchiveRuleRequestTypeDef, _OptionalApplyArchiveRuleRequestTypeDef
):
    pass


ArchiveRuleSummaryTypeDef = TypedDict(
    "ArchiveRuleSummaryTypeDef",
    {
        "createdAt": datetime,
        "filter": Dict[str, "CriterionTypeDef"],
        "ruleName": str,
        "updatedAt": datetime,
    },
)

CancelPolicyGenerationRequestTypeDef = TypedDict(
    "CancelPolicyGenerationRequestTypeDef",
    {
        "jobId": str,
    },
)

_RequiredCloudTrailDetailsTypeDef = TypedDict(
    "_RequiredCloudTrailDetailsTypeDef",
    {
        "accessRole": str,
        "startTime": Union[datetime, str],
        "trails": List["TrailTypeDef"],
    },
)
_OptionalCloudTrailDetailsTypeDef = TypedDict(
    "_OptionalCloudTrailDetailsTypeDef",
    {
        "endTime": Union[datetime, str],
    },
    total=False,
)


class CloudTrailDetailsTypeDef(
    _RequiredCloudTrailDetailsTypeDef, _OptionalCloudTrailDetailsTypeDef
):
    pass


CloudTrailPropertiesTypeDef = TypedDict(
    "CloudTrailPropertiesTypeDef",
    {
        "endTime": datetime,
        "startTime": datetime,
        "trailProperties": List["TrailPropertiesTypeDef"],
    },
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "iamRole": "IamRoleConfigurationTypeDef",
        "kmsKey": "KmsKeyConfigurationTypeDef",
        "s3Bucket": "S3BucketConfigurationTypeDef",
        "secretsManagerSecret": "SecretsManagerSecretConfigurationTypeDef",
        "sqsQueue": "SqsQueueConfigurationTypeDef",
    },
    total=False,
)

_RequiredCreateAccessPreviewRequestTypeDef = TypedDict(
    "_RequiredCreateAccessPreviewRequestTypeDef",
    {
        "analyzerArn": str,
        "configurations": Dict[str, "ConfigurationTypeDef"],
    },
)
_OptionalCreateAccessPreviewRequestTypeDef = TypedDict(
    "_OptionalCreateAccessPreviewRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class CreateAccessPreviewRequestTypeDef(
    _RequiredCreateAccessPreviewRequestTypeDef, _OptionalCreateAccessPreviewRequestTypeDef
):
    pass


CreateAccessPreviewResponseResponseTypeDef = TypedDict(
    "CreateAccessPreviewResponseResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAnalyzerRequestTypeDef = TypedDict(
    "_RequiredCreateAnalyzerRequestTypeDef",
    {
        "analyzerName": str,
        "type": TypeType,
    },
)
_OptionalCreateAnalyzerRequestTypeDef = TypedDict(
    "_OptionalCreateAnalyzerRequestTypeDef",
    {
        "archiveRules": List["InlineArchiveRuleTypeDef"],
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateAnalyzerRequestTypeDef(
    _RequiredCreateAnalyzerRequestTypeDef, _OptionalCreateAnalyzerRequestTypeDef
):
    pass


CreateAnalyzerResponseResponseTypeDef = TypedDict(
    "CreateAnalyzerResponseResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateArchiveRuleRequestTypeDef = TypedDict(
    "_RequiredCreateArchiveRuleRequestTypeDef",
    {
        "analyzerName": str,
        "filter": Dict[str, "CriterionTypeDef"],
        "ruleName": str,
    },
)
_OptionalCreateArchiveRuleRequestTypeDef = TypedDict(
    "_OptionalCreateArchiveRuleRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class CreateArchiveRuleRequestTypeDef(
    _RequiredCreateArchiveRuleRequestTypeDef, _OptionalCreateArchiveRuleRequestTypeDef
):
    pass


CriterionTypeDef = TypedDict(
    "CriterionTypeDef",
    {
        "contains": List[str],
        "eq": List[str],
        "exists": bool,
        "neq": List[str],
    },
    total=False,
)

_RequiredDeleteAnalyzerRequestTypeDef = TypedDict(
    "_RequiredDeleteAnalyzerRequestTypeDef",
    {
        "analyzerName": str,
    },
)
_OptionalDeleteAnalyzerRequestTypeDef = TypedDict(
    "_OptionalDeleteAnalyzerRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteAnalyzerRequestTypeDef(
    _RequiredDeleteAnalyzerRequestTypeDef, _OptionalDeleteAnalyzerRequestTypeDef
):
    pass


_RequiredDeleteArchiveRuleRequestTypeDef = TypedDict(
    "_RequiredDeleteArchiveRuleRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
    },
)
_OptionalDeleteArchiveRuleRequestTypeDef = TypedDict(
    "_OptionalDeleteArchiveRuleRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteArchiveRuleRequestTypeDef(
    _RequiredDeleteArchiveRuleRequestTypeDef, _OptionalDeleteArchiveRuleRequestTypeDef
):
    pass


FindingSourceDetailTypeDef = TypedDict(
    "FindingSourceDetailTypeDef",
    {
        "accessPointArn": str,
    },
    total=False,
)

_RequiredFindingSourceTypeDef = TypedDict(
    "_RequiredFindingSourceTypeDef",
    {
        "type": FindingSourceTypeType,
    },
)
_OptionalFindingSourceTypeDef = TypedDict(
    "_OptionalFindingSourceTypeDef",
    {
        "detail": "FindingSourceDetailTypeDef",
    },
    total=False,
)


class FindingSourceTypeDef(_RequiredFindingSourceTypeDef, _OptionalFindingSourceTypeDef):
    pass


_RequiredFindingSummaryTypeDef = TypedDict(
    "_RequiredFindingSummaryTypeDef",
    {
        "analyzedAt": datetime,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "id": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
        "status": FindingStatusType,
        "updatedAt": datetime,
    },
)
_OptionalFindingSummaryTypeDef = TypedDict(
    "_OptionalFindingSummaryTypeDef",
    {
        "action": List[str],
        "error": str,
        "isPublic": bool,
        "principal": Dict[str, str],
        "resource": str,
        "sources": List["FindingSourceTypeDef"],
    },
    total=False,
)


class FindingSummaryTypeDef(_RequiredFindingSummaryTypeDef, _OptionalFindingSummaryTypeDef):
    pass


_RequiredFindingTypeDef = TypedDict(
    "_RequiredFindingTypeDef",
    {
        "analyzedAt": datetime,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "id": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
        "status": FindingStatusType,
        "updatedAt": datetime,
    },
)
_OptionalFindingTypeDef = TypedDict(
    "_OptionalFindingTypeDef",
    {
        "action": List[str],
        "error": str,
        "isPublic": bool,
        "principal": Dict[str, str],
        "resource": str,
        "sources": List["FindingSourceTypeDef"],
    },
    total=False,
)


class FindingTypeDef(_RequiredFindingTypeDef, _OptionalFindingTypeDef):
    pass


_RequiredGeneratedPolicyPropertiesTypeDef = TypedDict(
    "_RequiredGeneratedPolicyPropertiesTypeDef",
    {
        "principalArn": str,
    },
)
_OptionalGeneratedPolicyPropertiesTypeDef = TypedDict(
    "_OptionalGeneratedPolicyPropertiesTypeDef",
    {
        "cloudTrailProperties": "CloudTrailPropertiesTypeDef",
        "isComplete": bool,
    },
    total=False,
)


class GeneratedPolicyPropertiesTypeDef(
    _RequiredGeneratedPolicyPropertiesTypeDef, _OptionalGeneratedPolicyPropertiesTypeDef
):
    pass


_RequiredGeneratedPolicyResultTypeDef = TypedDict(
    "_RequiredGeneratedPolicyResultTypeDef",
    {
        "properties": "GeneratedPolicyPropertiesTypeDef",
    },
)
_OptionalGeneratedPolicyResultTypeDef = TypedDict(
    "_OptionalGeneratedPolicyResultTypeDef",
    {
        "generatedPolicies": List["GeneratedPolicyTypeDef"],
    },
    total=False,
)


class GeneratedPolicyResultTypeDef(
    _RequiredGeneratedPolicyResultTypeDef, _OptionalGeneratedPolicyResultTypeDef
):
    pass


GeneratedPolicyTypeDef = TypedDict(
    "GeneratedPolicyTypeDef",
    {
        "policy": str,
    },
)

GetAccessPreviewRequestTypeDef = TypedDict(
    "GetAccessPreviewRequestTypeDef",
    {
        "accessPreviewId": str,
        "analyzerArn": str,
    },
)

GetAccessPreviewResponseResponseTypeDef = TypedDict(
    "GetAccessPreviewResponseResponseTypeDef",
    {
        "accessPreview": "AccessPreviewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAnalyzedResourceRequestTypeDef = TypedDict(
    "GetAnalyzedResourceRequestTypeDef",
    {
        "analyzerArn": str,
        "resourceArn": str,
    },
)

GetAnalyzedResourceResponseResponseTypeDef = TypedDict(
    "GetAnalyzedResourceResponseResponseTypeDef",
    {
        "resource": "AnalyzedResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAnalyzerRequestTypeDef = TypedDict(
    "GetAnalyzerRequestTypeDef",
    {
        "analyzerName": str,
    },
)

GetAnalyzerResponseResponseTypeDef = TypedDict(
    "GetAnalyzerResponseResponseTypeDef",
    {
        "analyzer": "AnalyzerSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetArchiveRuleRequestTypeDef = TypedDict(
    "GetArchiveRuleRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
    },
)

GetArchiveRuleResponseResponseTypeDef = TypedDict(
    "GetArchiveRuleResponseResponseTypeDef",
    {
        "archiveRule": "ArchiveRuleSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingRequestTypeDef = TypedDict(
    "GetFindingRequestTypeDef",
    {
        "analyzerArn": str,
        "id": str,
    },
)

GetFindingResponseResponseTypeDef = TypedDict(
    "GetFindingResponseResponseTypeDef",
    {
        "finding": "FindingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetGeneratedPolicyRequestTypeDef = TypedDict(
    "_RequiredGetGeneratedPolicyRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalGetGeneratedPolicyRequestTypeDef = TypedDict(
    "_OptionalGetGeneratedPolicyRequestTypeDef",
    {
        "includeResourcePlaceholders": bool,
        "includeServiceLevelTemplate": bool,
    },
    total=False,
)


class GetGeneratedPolicyRequestTypeDef(
    _RequiredGetGeneratedPolicyRequestTypeDef, _OptionalGetGeneratedPolicyRequestTypeDef
):
    pass


GetGeneratedPolicyResponseResponseTypeDef = TypedDict(
    "GetGeneratedPolicyResponseResponseTypeDef",
    {
        "generatedPolicyResult": "GeneratedPolicyResultTypeDef",
        "jobDetails": "JobDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IamRoleConfigurationTypeDef = TypedDict(
    "IamRoleConfigurationTypeDef",
    {
        "trustPolicy": str,
    },
    total=False,
)

InlineArchiveRuleTypeDef = TypedDict(
    "InlineArchiveRuleTypeDef",
    {
        "filter": Dict[str, "CriterionTypeDef"],
        "ruleName": str,
    },
)

_RequiredJobDetailsTypeDef = TypedDict(
    "_RequiredJobDetailsTypeDef",
    {
        "jobId": str,
        "startedOn": datetime,
        "status": JobStatusType,
    },
)
_OptionalJobDetailsTypeDef = TypedDict(
    "_OptionalJobDetailsTypeDef",
    {
        "completedOn": datetime,
        "jobError": "JobErrorTypeDef",
    },
    total=False,
)


class JobDetailsTypeDef(_RequiredJobDetailsTypeDef, _OptionalJobDetailsTypeDef):
    pass


JobErrorTypeDef = TypedDict(
    "JobErrorTypeDef",
    {
        "code": JobErrorCodeType,
        "message": str,
    },
)

_RequiredKmsGrantConfigurationTypeDef = TypedDict(
    "_RequiredKmsGrantConfigurationTypeDef",
    {
        "granteePrincipal": str,
        "issuingAccount": str,
        "operations": List[KmsGrantOperationType],
    },
)
_OptionalKmsGrantConfigurationTypeDef = TypedDict(
    "_OptionalKmsGrantConfigurationTypeDef",
    {
        "constraints": "KmsGrantConstraintsTypeDef",
        "retiringPrincipal": str,
    },
    total=False,
)


class KmsGrantConfigurationTypeDef(
    _RequiredKmsGrantConfigurationTypeDef, _OptionalKmsGrantConfigurationTypeDef
):
    pass


KmsGrantConstraintsTypeDef = TypedDict(
    "KmsGrantConstraintsTypeDef",
    {
        "encryptionContextEquals": Dict[str, str],
        "encryptionContextSubset": Dict[str, str],
    },
    total=False,
)

KmsKeyConfigurationTypeDef = TypedDict(
    "KmsKeyConfigurationTypeDef",
    {
        "grants": List["KmsGrantConfigurationTypeDef"],
        "keyPolicies": Dict[str, str],
    },
    total=False,
)

_RequiredListAccessPreviewFindingsRequestTypeDef = TypedDict(
    "_RequiredListAccessPreviewFindingsRequestTypeDef",
    {
        "accessPreviewId": str,
        "analyzerArn": str,
    },
)
_OptionalListAccessPreviewFindingsRequestTypeDef = TypedDict(
    "_OptionalListAccessPreviewFindingsRequestTypeDef",
    {
        "filter": Dict[str, "CriterionTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListAccessPreviewFindingsRequestTypeDef(
    _RequiredListAccessPreviewFindingsRequestTypeDef,
    _OptionalListAccessPreviewFindingsRequestTypeDef,
):
    pass


ListAccessPreviewFindingsResponseResponseTypeDef = TypedDict(
    "ListAccessPreviewFindingsResponseResponseTypeDef",
    {
        "findings": List["AccessPreviewFindingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccessPreviewsRequestTypeDef = TypedDict(
    "_RequiredListAccessPreviewsRequestTypeDef",
    {
        "analyzerArn": str,
    },
)
_OptionalListAccessPreviewsRequestTypeDef = TypedDict(
    "_OptionalListAccessPreviewsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListAccessPreviewsRequestTypeDef(
    _RequiredListAccessPreviewsRequestTypeDef, _OptionalListAccessPreviewsRequestTypeDef
):
    pass


ListAccessPreviewsResponseResponseTypeDef = TypedDict(
    "ListAccessPreviewsResponseResponseTypeDef",
    {
        "accessPreviews": List["AccessPreviewSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAnalyzedResourcesRequestTypeDef = TypedDict(
    "_RequiredListAnalyzedResourcesRequestTypeDef",
    {
        "analyzerArn": str,
    },
)
_OptionalListAnalyzedResourcesRequestTypeDef = TypedDict(
    "_OptionalListAnalyzedResourcesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "resourceType": ResourceTypeType,
    },
    total=False,
)


class ListAnalyzedResourcesRequestTypeDef(
    _RequiredListAnalyzedResourcesRequestTypeDef, _OptionalListAnalyzedResourcesRequestTypeDef
):
    pass


ListAnalyzedResourcesResponseResponseTypeDef = TypedDict(
    "ListAnalyzedResourcesResponseResponseTypeDef",
    {
        "analyzedResources": List["AnalyzedResourceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAnalyzersRequestTypeDef = TypedDict(
    "ListAnalyzersRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "type": TypeType,
    },
    total=False,
)

ListAnalyzersResponseResponseTypeDef = TypedDict(
    "ListAnalyzersResponseResponseTypeDef",
    {
        "analyzers": List["AnalyzerSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListArchiveRulesRequestTypeDef = TypedDict(
    "_RequiredListArchiveRulesRequestTypeDef",
    {
        "analyzerName": str,
    },
)
_OptionalListArchiveRulesRequestTypeDef = TypedDict(
    "_OptionalListArchiveRulesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListArchiveRulesRequestTypeDef(
    _RequiredListArchiveRulesRequestTypeDef, _OptionalListArchiveRulesRequestTypeDef
):
    pass


ListArchiveRulesResponseResponseTypeDef = TypedDict(
    "ListArchiveRulesResponseResponseTypeDef",
    {
        "archiveRules": List["ArchiveRuleSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFindingsRequestTypeDef = TypedDict(
    "_RequiredListFindingsRequestTypeDef",
    {
        "analyzerArn": str,
    },
)
_OptionalListFindingsRequestTypeDef = TypedDict(
    "_OptionalListFindingsRequestTypeDef",
    {
        "filter": Dict[str, "CriterionTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "sort": "SortCriteriaTypeDef",
    },
    total=False,
)


class ListFindingsRequestTypeDef(
    _RequiredListFindingsRequestTypeDef, _OptionalListFindingsRequestTypeDef
):
    pass


ListFindingsResponseResponseTypeDef = TypedDict(
    "ListFindingsResponseResponseTypeDef",
    {
        "findings": List["FindingSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPolicyGenerationsRequestTypeDef = TypedDict(
    "ListPolicyGenerationsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "principalArn": str,
    },
    total=False,
)

ListPolicyGenerationsResponseResponseTypeDef = TypedDict(
    "ListPolicyGenerationsResponseResponseTypeDef",
    {
        "nextToken": str,
        "policyGenerations": List["PolicyGenerationTypeDef"],
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
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "path": List["PathElementTypeDef"],
        "span": "SpanTypeDef",
    },
)

NetworkOriginConfigurationTypeDef = TypedDict(
    "NetworkOriginConfigurationTypeDef",
    {
        "internetConfiguration": Dict[str, Any],
        "vpcConfiguration": "VpcConfigurationTypeDef",
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

PathElementTypeDef = TypedDict(
    "PathElementTypeDef",
    {
        "index": int,
        "key": str,
        "substring": "SubstringTypeDef",
        "value": str,
    },
    total=False,
)

PolicyGenerationDetailsTypeDef = TypedDict(
    "PolicyGenerationDetailsTypeDef",
    {
        "principalArn": str,
    },
)

_RequiredPolicyGenerationTypeDef = TypedDict(
    "_RequiredPolicyGenerationTypeDef",
    {
        "jobId": str,
        "principalArn": str,
        "startedOn": datetime,
        "status": JobStatusType,
    },
)
_OptionalPolicyGenerationTypeDef = TypedDict(
    "_OptionalPolicyGenerationTypeDef",
    {
        "completedOn": datetime,
    },
    total=False,
)


class PolicyGenerationTypeDef(_RequiredPolicyGenerationTypeDef, _OptionalPolicyGenerationTypeDef):
    pass


PositionTypeDef = TypedDict(
    "PositionTypeDef",
    {
        "column": int,
        "line": int,
        "offset": int,
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

S3AccessPointConfigurationTypeDef = TypedDict(
    "S3AccessPointConfigurationTypeDef",
    {
        "accessPointPolicy": str,
        "networkOrigin": "NetworkOriginConfigurationTypeDef",
        "publicAccessBlock": "S3PublicAccessBlockConfigurationTypeDef",
    },
    total=False,
)

S3BucketAclGrantConfigurationTypeDef = TypedDict(
    "S3BucketAclGrantConfigurationTypeDef",
    {
        "grantee": "AclGranteeTypeDef",
        "permission": AclPermissionType,
    },
)

S3BucketConfigurationTypeDef = TypedDict(
    "S3BucketConfigurationTypeDef",
    {
        "accessPoints": Dict[str, "S3AccessPointConfigurationTypeDef"],
        "bucketAclGrants": List["S3BucketAclGrantConfigurationTypeDef"],
        "bucketPolicy": str,
        "bucketPublicAccessBlock": "S3PublicAccessBlockConfigurationTypeDef",
    },
    total=False,
)

S3PublicAccessBlockConfigurationTypeDef = TypedDict(
    "S3PublicAccessBlockConfigurationTypeDef",
    {
        "ignorePublicAcls": bool,
        "restrictPublicBuckets": bool,
    },
)

SecretsManagerSecretConfigurationTypeDef = TypedDict(
    "SecretsManagerSecretConfigurationTypeDef",
    {
        "kmsKeyId": str,
        "secretPolicy": str,
    },
    total=False,
)

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "attributeName": str,
        "orderBy": OrderByType,
    },
    total=False,
)

SpanTypeDef = TypedDict(
    "SpanTypeDef",
    {
        "end": "PositionTypeDef",
        "start": "PositionTypeDef",
    },
)

SqsQueueConfigurationTypeDef = TypedDict(
    "SqsQueueConfigurationTypeDef",
    {
        "queuePolicy": str,
    },
    total=False,
)

_RequiredStartPolicyGenerationRequestTypeDef = TypedDict(
    "_RequiredStartPolicyGenerationRequestTypeDef",
    {
        "policyGenerationDetails": "PolicyGenerationDetailsTypeDef",
    },
)
_OptionalStartPolicyGenerationRequestTypeDef = TypedDict(
    "_OptionalStartPolicyGenerationRequestTypeDef",
    {
        "clientToken": str,
        "cloudTrailDetails": "CloudTrailDetailsTypeDef",
    },
    total=False,
)


class StartPolicyGenerationRequestTypeDef(
    _RequiredStartPolicyGenerationRequestTypeDef, _OptionalStartPolicyGenerationRequestTypeDef
):
    pass


StartPolicyGenerationResponseResponseTypeDef = TypedDict(
    "StartPolicyGenerationResponseResponseTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartResourceScanRequestTypeDef = TypedDict(
    "StartResourceScanRequestTypeDef",
    {
        "analyzerArn": str,
        "resourceArn": str,
    },
)

StatusReasonTypeDef = TypedDict(
    "StatusReasonTypeDef",
    {
        "code": ReasonCodeType,
    },
)

SubstringTypeDef = TypedDict(
    "SubstringTypeDef",
    {
        "length": int,
        "start": int,
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

_RequiredTrailPropertiesTypeDef = TypedDict(
    "_RequiredTrailPropertiesTypeDef",
    {
        "cloudTrailArn": str,
    },
)
_OptionalTrailPropertiesTypeDef = TypedDict(
    "_OptionalTrailPropertiesTypeDef",
    {
        "allRegions": bool,
        "regions": List[str],
    },
    total=False,
)


class TrailPropertiesTypeDef(_RequiredTrailPropertiesTypeDef, _OptionalTrailPropertiesTypeDef):
    pass


_RequiredTrailTypeDef = TypedDict(
    "_RequiredTrailTypeDef",
    {
        "cloudTrailArn": str,
    },
)
_OptionalTrailTypeDef = TypedDict(
    "_OptionalTrailTypeDef",
    {
        "allRegions": bool,
        "regions": List[str],
    },
    total=False,
)


class TrailTypeDef(_RequiredTrailTypeDef, _OptionalTrailTypeDef):
    pass


UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateArchiveRuleRequestTypeDef = TypedDict(
    "_RequiredUpdateArchiveRuleRequestTypeDef",
    {
        "analyzerName": str,
        "filter": Dict[str, "CriterionTypeDef"],
        "ruleName": str,
    },
)
_OptionalUpdateArchiveRuleRequestTypeDef = TypedDict(
    "_OptionalUpdateArchiveRuleRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class UpdateArchiveRuleRequestTypeDef(
    _RequiredUpdateArchiveRuleRequestTypeDef, _OptionalUpdateArchiveRuleRequestTypeDef
):
    pass


_RequiredUpdateFindingsRequestTypeDef = TypedDict(
    "_RequiredUpdateFindingsRequestTypeDef",
    {
        "analyzerArn": str,
        "status": FindingStatusUpdateType,
    },
)
_OptionalUpdateFindingsRequestTypeDef = TypedDict(
    "_OptionalUpdateFindingsRequestTypeDef",
    {
        "clientToken": str,
        "ids": List[str],
        "resourceArn": str,
    },
    total=False,
)


class UpdateFindingsRequestTypeDef(
    _RequiredUpdateFindingsRequestTypeDef, _OptionalUpdateFindingsRequestTypeDef
):
    pass


ValidatePolicyFindingTypeDef = TypedDict(
    "ValidatePolicyFindingTypeDef",
    {
        "findingDetails": str,
        "findingType": ValidatePolicyFindingTypeType,
        "issueCode": str,
        "learnMoreLink": str,
        "locations": List["LocationTypeDef"],
    },
)

_RequiredValidatePolicyRequestTypeDef = TypedDict(
    "_RequiredValidatePolicyRequestTypeDef",
    {
        "policyDocument": str,
        "policyType": PolicyTypeType,
    },
)
_OptionalValidatePolicyRequestTypeDef = TypedDict(
    "_OptionalValidatePolicyRequestTypeDef",
    {
        "locale": LocaleType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ValidatePolicyRequestTypeDef(
    _RequiredValidatePolicyRequestTypeDef, _OptionalValidatePolicyRequestTypeDef
):
    pass


ValidatePolicyResponseResponseTypeDef = TypedDict(
    "ValidatePolicyResponseResponseTypeDef",
    {
        "findings": List["ValidatePolicyFindingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "vpcId": str,
    },
)
