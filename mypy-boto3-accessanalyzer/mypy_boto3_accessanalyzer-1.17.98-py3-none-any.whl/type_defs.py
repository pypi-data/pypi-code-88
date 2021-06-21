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
from typing import Any, Dict, List

from .literals import (
    AccessPreviewStatusReasonCodeType,
    AccessPreviewStatusType,
    AclPermissionType,
    AnalyzerStatusType,
    FindingChangeTypeType,
    FindingSourceTypeType,
    FindingStatusType,
    JobErrorCodeType,
    JobStatusType,
    KmsGrantOperationType,
    OrderByType,
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
    "ArchiveRuleSummaryTypeDef",
    "CloudTrailDetailsTypeDef",
    "CloudTrailPropertiesTypeDef",
    "ConfigurationTypeDef",
    "CreateAccessPreviewResponseTypeDef",
    "CreateAnalyzerResponseTypeDef",
    "CriterionTypeDef",
    "FindingSourceDetailTypeDef",
    "FindingSourceTypeDef",
    "FindingSummaryTypeDef",
    "FindingTypeDef",
    "GeneratedPolicyPropertiesTypeDef",
    "GeneratedPolicyResultTypeDef",
    "GeneratedPolicyTypeDef",
    "GetAccessPreviewResponseTypeDef",
    "GetAnalyzedResourceResponseTypeDef",
    "GetAnalyzerResponseTypeDef",
    "GetArchiveRuleResponseTypeDef",
    "GetFindingResponseTypeDef",
    "GetGeneratedPolicyResponseTypeDef",
    "IamRoleConfigurationTypeDef",
    "InlineArchiveRuleTypeDef",
    "JobDetailsTypeDef",
    "JobErrorTypeDef",
    "KmsGrantConfigurationTypeDef",
    "KmsGrantConstraintsTypeDef",
    "KmsKeyConfigurationTypeDef",
    "ListAccessPreviewFindingsResponseTypeDef",
    "ListAccessPreviewsResponseTypeDef",
    "ListAnalyzedResourcesResponseTypeDef",
    "ListAnalyzersResponseTypeDef",
    "ListArchiveRulesResponseTypeDef",
    "ListFindingsResponseTypeDef",
    "ListPolicyGenerationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationTypeDef",
    "NetworkOriginConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PathElementTypeDef",
    "PolicyGenerationDetailsTypeDef",
    "PolicyGenerationTypeDef",
    "PositionTypeDef",
    "S3AccessPointConfigurationTypeDef",
    "S3BucketAclGrantConfigurationTypeDef",
    "S3BucketConfigurationTypeDef",
    "S3PublicAccessBlockConfigurationTypeDef",
    "SecretsManagerSecretConfigurationTypeDef",
    "SortCriteriaTypeDef",
    "SpanTypeDef",
    "SqsQueueConfigurationTypeDef",
    "StartPolicyGenerationResponseTypeDef",
    "StatusReasonTypeDef",
    "SubstringTypeDef",
    "TrailPropertiesTypeDef",
    "TrailTypeDef",
    "ValidatePolicyFindingTypeDef",
    "ValidatePolicyResponseTypeDef",
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


ArchiveRuleSummaryTypeDef = TypedDict(
    "ArchiveRuleSummaryTypeDef",
    {
        "createdAt": datetime,
        "filter": Dict[str, "CriterionTypeDef"],
        "ruleName": str,
        "updatedAt": datetime,
    },
)

_RequiredCloudTrailDetailsTypeDef = TypedDict(
    "_RequiredCloudTrailDetailsTypeDef",
    {
        "accessRole": str,
        "startTime": datetime,
        "trails": List["TrailTypeDef"],
    },
)
_OptionalCloudTrailDetailsTypeDef = TypedDict(
    "_OptionalCloudTrailDetailsTypeDef",
    {
        "endTime": datetime,
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

CreateAccessPreviewResponseTypeDef = TypedDict(
    "CreateAccessPreviewResponseTypeDef",
    {
        "id": str,
    },
)

CreateAnalyzerResponseTypeDef = TypedDict(
    "CreateAnalyzerResponseTypeDef",
    {
        "arn": str,
    },
    total=False,
)

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

GetAccessPreviewResponseTypeDef = TypedDict(
    "GetAccessPreviewResponseTypeDef",
    {
        "accessPreview": "AccessPreviewTypeDef",
    },
)

GetAnalyzedResourceResponseTypeDef = TypedDict(
    "GetAnalyzedResourceResponseTypeDef",
    {
        "resource": "AnalyzedResourceTypeDef",
    },
    total=False,
)

GetAnalyzerResponseTypeDef = TypedDict(
    "GetAnalyzerResponseTypeDef",
    {
        "analyzer": "AnalyzerSummaryTypeDef",
    },
)

GetArchiveRuleResponseTypeDef = TypedDict(
    "GetArchiveRuleResponseTypeDef",
    {
        "archiveRule": "ArchiveRuleSummaryTypeDef",
    },
)

GetFindingResponseTypeDef = TypedDict(
    "GetFindingResponseTypeDef",
    {
        "finding": "FindingTypeDef",
    },
    total=False,
)

GetGeneratedPolicyResponseTypeDef = TypedDict(
    "GetGeneratedPolicyResponseTypeDef",
    {
        "generatedPolicyResult": "GeneratedPolicyResultTypeDef",
        "jobDetails": "JobDetailsTypeDef",
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

_RequiredListAccessPreviewFindingsResponseTypeDef = TypedDict(
    "_RequiredListAccessPreviewFindingsResponseTypeDef",
    {
        "findings": List["AccessPreviewFindingTypeDef"],
    },
)
_OptionalListAccessPreviewFindingsResponseTypeDef = TypedDict(
    "_OptionalListAccessPreviewFindingsResponseTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListAccessPreviewFindingsResponseTypeDef(
    _RequiredListAccessPreviewFindingsResponseTypeDef,
    _OptionalListAccessPreviewFindingsResponseTypeDef,
):
    pass


_RequiredListAccessPreviewsResponseTypeDef = TypedDict(
    "_RequiredListAccessPreviewsResponseTypeDef",
    {
        "accessPreviews": List["AccessPreviewSummaryTypeDef"],
    },
)
_OptionalListAccessPreviewsResponseTypeDef = TypedDict(
    "_OptionalListAccessPreviewsResponseTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListAccessPreviewsResponseTypeDef(
    _RequiredListAccessPreviewsResponseTypeDef, _OptionalListAccessPreviewsResponseTypeDef
):
    pass


_RequiredListAnalyzedResourcesResponseTypeDef = TypedDict(
    "_RequiredListAnalyzedResourcesResponseTypeDef",
    {
        "analyzedResources": List["AnalyzedResourceSummaryTypeDef"],
    },
)
_OptionalListAnalyzedResourcesResponseTypeDef = TypedDict(
    "_OptionalListAnalyzedResourcesResponseTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListAnalyzedResourcesResponseTypeDef(
    _RequiredListAnalyzedResourcesResponseTypeDef, _OptionalListAnalyzedResourcesResponseTypeDef
):
    pass


_RequiredListAnalyzersResponseTypeDef = TypedDict(
    "_RequiredListAnalyzersResponseTypeDef",
    {
        "analyzers": List["AnalyzerSummaryTypeDef"],
    },
)
_OptionalListAnalyzersResponseTypeDef = TypedDict(
    "_OptionalListAnalyzersResponseTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListAnalyzersResponseTypeDef(
    _RequiredListAnalyzersResponseTypeDef, _OptionalListAnalyzersResponseTypeDef
):
    pass


_RequiredListArchiveRulesResponseTypeDef = TypedDict(
    "_RequiredListArchiveRulesResponseTypeDef",
    {
        "archiveRules": List["ArchiveRuleSummaryTypeDef"],
    },
)
_OptionalListArchiveRulesResponseTypeDef = TypedDict(
    "_OptionalListArchiveRulesResponseTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListArchiveRulesResponseTypeDef(
    _RequiredListArchiveRulesResponseTypeDef, _OptionalListArchiveRulesResponseTypeDef
):
    pass


_RequiredListFindingsResponseTypeDef = TypedDict(
    "_RequiredListFindingsResponseTypeDef",
    {
        "findings": List["FindingSummaryTypeDef"],
    },
)
_OptionalListFindingsResponseTypeDef = TypedDict(
    "_OptionalListFindingsResponseTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListFindingsResponseTypeDef(
    _RequiredListFindingsResponseTypeDef, _OptionalListFindingsResponseTypeDef
):
    pass


_RequiredListPolicyGenerationsResponseTypeDef = TypedDict(
    "_RequiredListPolicyGenerationsResponseTypeDef",
    {
        "policyGenerations": List["PolicyGenerationTypeDef"],
    },
)
_OptionalListPolicyGenerationsResponseTypeDef = TypedDict(
    "_OptionalListPolicyGenerationsResponseTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListPolicyGenerationsResponseTypeDef(
    _RequiredListPolicyGenerationsResponseTypeDef, _OptionalListPolicyGenerationsResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
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

StartPolicyGenerationResponseTypeDef = TypedDict(
    "StartPolicyGenerationResponseTypeDef",
    {
        "jobId": str,
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

_RequiredValidatePolicyResponseTypeDef = TypedDict(
    "_RequiredValidatePolicyResponseTypeDef",
    {
        "findings": List["ValidatePolicyFindingTypeDef"],
    },
)
_OptionalValidatePolicyResponseTypeDef = TypedDict(
    "_OptionalValidatePolicyResponseTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ValidatePolicyResponseTypeDef(
    _RequiredValidatePolicyResponseTypeDef, _OptionalValidatePolicyResponseTypeDef
):
    pass


VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "vpcId": str,
    },
)
