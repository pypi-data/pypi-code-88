"""
Type annotations for macie2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_macie2.type_defs import AcceptInvitationRequestTypeDef

    data: AcceptInvitationRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AdminStatusType,
    AllowsUnencryptedObjectUploadsType,
    DayOfWeekType,
    EffectivePermissionType,
    EncryptionTypeType,
    ErrorCodeType,
    FindingCategoryType,
    FindingPublishingFrequencyType,
    FindingsFilterActionType,
    FindingStatisticsSortAttributeNameType,
    FindingTypeType,
    GroupByType,
    IsDefinedInJobType,
    IsMonitoredByJobType,
    JobComparatorType,
    JobStatusType,
    JobTypeType,
    LastRunErrorStatusCodeType,
    ListJobsFilterKeyType,
    ListJobsSortAttributeNameType,
    MacieStatusType,
    OrderByType,
    RelationshipStatusType,
    ScopeFilterKeyType,
    SearchResourcesComparatorType,
    SearchResourcesSimpleCriterionKeyType,
    SearchResourcesSortAttributeNameType,
    SensitiveDataItemCategoryType,
    SeverityDescriptionType,
    SharedAccessType,
    SimpleCriterionKeyForJobType,
    StorageClassType,
    TimeRangeType,
    TypeType,
    UsageStatisticsFilterComparatorType,
    UsageStatisticsFilterKeyType,
    UsageStatisticsSortKeyType,
    UsageTypeType,
    UserIdentityTypeType,
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
    "AcceptInvitationRequestTypeDef",
    "AccessControlListTypeDef",
    "AccountDetailTypeDef",
    "AccountLevelPermissionsTypeDef",
    "AdminAccountTypeDef",
    "ApiCallDetailsTypeDef",
    "AssumedRoleTypeDef",
    "AwsAccountTypeDef",
    "AwsServiceTypeDef",
    "BatchGetCustomDataIdentifierSummaryTypeDef",
    "BatchGetCustomDataIdentifiersRequestTypeDef",
    "BatchGetCustomDataIdentifiersResponseResponseTypeDef",
    "BlockPublicAccessTypeDef",
    "BucketCountByEffectivePermissionTypeDef",
    "BucketCountByEncryptionTypeTypeDef",
    "BucketCountBySharedAccessTypeTypeDef",
    "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef",
    "BucketCriteriaAdditionalPropertiesTypeDef",
    "BucketLevelPermissionsTypeDef",
    "BucketMetadataTypeDef",
    "BucketPermissionConfigurationTypeDef",
    "BucketPolicyTypeDef",
    "BucketPublicAccessTypeDef",
    "BucketServerSideEncryptionTypeDef",
    "BucketSortCriteriaTypeDef",
    "CellTypeDef",
    "ClassificationDetailsTypeDef",
    "ClassificationExportConfigurationTypeDef",
    "ClassificationResultStatusTypeDef",
    "ClassificationResultTypeDef",
    "CreateClassificationJobRequestTypeDef",
    "CreateClassificationJobResponseResponseTypeDef",
    "CreateCustomDataIdentifierRequestTypeDef",
    "CreateCustomDataIdentifierResponseResponseTypeDef",
    "CreateFindingsFilterRequestTypeDef",
    "CreateFindingsFilterResponseResponseTypeDef",
    "CreateInvitationsRequestTypeDef",
    "CreateInvitationsResponseResponseTypeDef",
    "CreateMemberRequestTypeDef",
    "CreateMemberResponseResponseTypeDef",
    "CreateSampleFindingsRequestTypeDef",
    "CriteriaBlockForJobTypeDef",
    "CriteriaForJobTypeDef",
    "CriterionAdditionalPropertiesTypeDef",
    "CustomDataIdentifierSummaryTypeDef",
    "CustomDataIdentifiersTypeDef",
    "CustomDetectionTypeDef",
    "DeclineInvitationsRequestTypeDef",
    "DeclineInvitationsResponseResponseTypeDef",
    "DefaultDetectionTypeDef",
    "DeleteCustomDataIdentifierRequestTypeDef",
    "DeleteFindingsFilterRequestTypeDef",
    "DeleteInvitationsRequestTypeDef",
    "DeleteInvitationsResponseResponseTypeDef",
    "DeleteMemberRequestTypeDef",
    "DescribeBucketsRequestTypeDef",
    "DescribeBucketsResponseResponseTypeDef",
    "DescribeClassificationJobRequestTypeDef",
    "DescribeClassificationJobResponseResponseTypeDef",
    "DescribeOrganizationConfigurationResponseResponseTypeDef",
    "DisableOrganizationAdminAccountRequestTypeDef",
    "DisassociateMemberRequestTypeDef",
    "DomainDetailsTypeDef",
    "EnableMacieRequestTypeDef",
    "EnableOrganizationAdminAccountRequestTypeDef",
    "FederatedUserTypeDef",
    "FindingActionTypeDef",
    "FindingActorTypeDef",
    "FindingCriteriaTypeDef",
    "FindingStatisticsSortCriteriaTypeDef",
    "FindingTypeDef",
    "FindingsFilterListItemTypeDef",
    "GetAdministratorAccountResponseResponseTypeDef",
    "GetBucketStatisticsRequestTypeDef",
    "GetBucketStatisticsResponseResponseTypeDef",
    "GetClassificationExportConfigurationResponseResponseTypeDef",
    "GetCustomDataIdentifierRequestTypeDef",
    "GetCustomDataIdentifierResponseResponseTypeDef",
    "GetFindingStatisticsRequestTypeDef",
    "GetFindingStatisticsResponseResponseTypeDef",
    "GetFindingsFilterRequestTypeDef",
    "GetFindingsFilterResponseResponseTypeDef",
    "GetFindingsPublicationConfigurationResponseResponseTypeDef",
    "GetFindingsRequestTypeDef",
    "GetFindingsResponseResponseTypeDef",
    "GetInvitationsCountResponseResponseTypeDef",
    "GetMacieSessionResponseResponseTypeDef",
    "GetMasterAccountResponseResponseTypeDef",
    "GetMemberRequestTypeDef",
    "GetMemberResponseResponseTypeDef",
    "GetUsageStatisticsRequestTypeDef",
    "GetUsageStatisticsResponseResponseTypeDef",
    "GetUsageTotalsRequestTypeDef",
    "GetUsageTotalsResponseResponseTypeDef",
    "GroupCountTypeDef",
    "IamUserTypeDef",
    "InvitationTypeDef",
    "IpAddressDetailsTypeDef",
    "IpCityTypeDef",
    "IpCountryTypeDef",
    "IpGeoLocationTypeDef",
    "IpOwnerTypeDef",
    "JobDetailsTypeDef",
    "JobScheduleFrequencyTypeDef",
    "JobScopeTermTypeDef",
    "JobScopingBlockTypeDef",
    "JobSummaryTypeDef",
    "KeyValuePairTypeDef",
    "LastRunErrorStatusTypeDef",
    "ListClassificationJobsRequestTypeDef",
    "ListClassificationJobsResponseResponseTypeDef",
    "ListCustomDataIdentifiersRequestTypeDef",
    "ListCustomDataIdentifiersResponseResponseTypeDef",
    "ListFindingsFiltersRequestTypeDef",
    "ListFindingsFiltersResponseResponseTypeDef",
    "ListFindingsRequestTypeDef",
    "ListFindingsResponseResponseTypeDef",
    "ListInvitationsRequestTypeDef",
    "ListInvitationsResponseResponseTypeDef",
    "ListJobsFilterCriteriaTypeDef",
    "ListJobsFilterTermTypeDef",
    "ListJobsSortCriteriaTypeDef",
    "ListMembersRequestTypeDef",
    "ListMembersResponseResponseTypeDef",
    "ListOrganizationAdminAccountsRequestTypeDef",
    "ListOrganizationAdminAccountsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MatchingBucketTypeDef",
    "MatchingResourceTypeDef",
    "MemberTypeDef",
    "MonthlyScheduleTypeDef",
    "ObjectCountByEncryptionTypeTypeDef",
    "ObjectLevelStatisticsTypeDef",
    "OccurrencesTypeDef",
    "PageTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyDetailsTypeDef",
    "PutClassificationExportConfigurationRequestTypeDef",
    "PutClassificationExportConfigurationResponseResponseTypeDef",
    "PutFindingsPublicationConfigurationRequestTypeDef",
    "RangeTypeDef",
    "RecordTypeDef",
    "ReplicationDetailsTypeDef",
    "ResourcesAffectedTypeDef",
    "ResponseMetadataTypeDef",
    "S3BucketCriteriaForJobTypeDef",
    "S3BucketDefinitionForJobTypeDef",
    "S3BucketOwnerTypeDef",
    "S3BucketTypeDef",
    "S3DestinationTypeDef",
    "S3JobDefinitionTypeDef",
    "S3ObjectTypeDef",
    "ScopingTypeDef",
    "SearchResourcesBucketCriteriaTypeDef",
    "SearchResourcesCriteriaBlockTypeDef",
    "SearchResourcesCriteriaTypeDef",
    "SearchResourcesRequestTypeDef",
    "SearchResourcesResponseResponseTypeDef",
    "SearchResourcesSimpleCriterionTypeDef",
    "SearchResourcesSortCriteriaTypeDef",
    "SearchResourcesTagCriterionPairTypeDef",
    "SearchResourcesTagCriterionTypeDef",
    "SecurityHubConfigurationTypeDef",
    "SensitiveDataItemTypeDef",
    "ServerSideEncryptionTypeDef",
    "ServiceLimitTypeDef",
    "SessionContextAttributesTypeDef",
    "SessionContextTypeDef",
    "SessionIssuerTypeDef",
    "SeverityTypeDef",
    "SimpleCriterionForJobTypeDef",
    "SimpleScopeTermTypeDef",
    "SortCriteriaTypeDef",
    "StatisticsTypeDef",
    "TagCriterionForJobTypeDef",
    "TagCriterionPairForJobTypeDef",
    "TagResourceRequestTypeDef",
    "TagScopeTermTypeDef",
    "TagValuePairTypeDef",
    "TestCustomDataIdentifierRequestTypeDef",
    "TestCustomDataIdentifierResponseResponseTypeDef",
    "UnprocessedAccountTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateClassificationJobRequestTypeDef",
    "UpdateFindingsFilterRequestTypeDef",
    "UpdateFindingsFilterResponseResponseTypeDef",
    "UpdateMacieSessionRequestTypeDef",
    "UpdateMemberSessionRequestTypeDef",
    "UpdateOrganizationConfigurationRequestTypeDef",
    "UsageByAccountTypeDef",
    "UsageRecordTypeDef",
    "UsageStatisticsFilterTypeDef",
    "UsageStatisticsSortByTypeDef",
    "UsageTotalTypeDef",
    "UserIdentityRootTypeDef",
    "UserIdentityTypeDef",
    "UserPausedDetailsTypeDef",
    "WeeklyScheduleTypeDef",
)

_RequiredAcceptInvitationRequestTypeDef = TypedDict(
    "_RequiredAcceptInvitationRequestTypeDef",
    {
        "invitationId": str,
    },
)
_OptionalAcceptInvitationRequestTypeDef = TypedDict(
    "_OptionalAcceptInvitationRequestTypeDef",
    {
        "administratorAccountId": str,
        "masterAccount": str,
    },
    total=False,
)


class AcceptInvitationRequestTypeDef(
    _RequiredAcceptInvitationRequestTypeDef, _OptionalAcceptInvitationRequestTypeDef
):
    pass


AccessControlListTypeDef = TypedDict(
    "AccessControlListTypeDef",
    {
        "allowsPublicReadAccess": bool,
        "allowsPublicWriteAccess": bool,
    },
    total=False,
)

AccountDetailTypeDef = TypedDict(
    "AccountDetailTypeDef",
    {
        "accountId": str,
        "email": str,
    },
)

AccountLevelPermissionsTypeDef = TypedDict(
    "AccountLevelPermissionsTypeDef",
    {
        "blockPublicAccess": "BlockPublicAccessTypeDef",
    },
    total=False,
)

AdminAccountTypeDef = TypedDict(
    "AdminAccountTypeDef",
    {
        "accountId": str,
        "status": AdminStatusType,
    },
    total=False,
)

ApiCallDetailsTypeDef = TypedDict(
    "ApiCallDetailsTypeDef",
    {
        "api": str,
        "apiServiceName": str,
        "firstSeen": datetime,
        "lastSeen": datetime,
    },
    total=False,
)

AssumedRoleTypeDef = TypedDict(
    "AssumedRoleTypeDef",
    {
        "accessKeyId": str,
        "accountId": str,
        "arn": str,
        "principalId": str,
        "sessionContext": "SessionContextTypeDef",
    },
    total=False,
)

AwsAccountTypeDef = TypedDict(
    "AwsAccountTypeDef",
    {
        "accountId": str,
        "principalId": str,
    },
    total=False,
)

AwsServiceTypeDef = TypedDict(
    "AwsServiceTypeDef",
    {
        "invokedBy": str,
    },
    total=False,
)

BatchGetCustomDataIdentifierSummaryTypeDef = TypedDict(
    "BatchGetCustomDataIdentifierSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deleted": bool,
        "description": str,
        "id": str,
        "name": str,
    },
    total=False,
)

BatchGetCustomDataIdentifiersRequestTypeDef = TypedDict(
    "BatchGetCustomDataIdentifiersRequestTypeDef",
    {
        "ids": List[str],
    },
    total=False,
)

BatchGetCustomDataIdentifiersResponseResponseTypeDef = TypedDict(
    "BatchGetCustomDataIdentifiersResponseResponseTypeDef",
    {
        "customDataIdentifiers": List["BatchGetCustomDataIdentifierSummaryTypeDef"],
        "notFoundIdentifierIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BlockPublicAccessTypeDef = TypedDict(
    "BlockPublicAccessTypeDef",
    {
        "blockPublicAcls": bool,
        "blockPublicPolicy": bool,
        "ignorePublicAcls": bool,
        "restrictPublicBuckets": bool,
    },
    total=False,
)

BucketCountByEffectivePermissionTypeDef = TypedDict(
    "BucketCountByEffectivePermissionTypeDef",
    {
        "publiclyAccessible": int,
        "publiclyReadable": int,
        "publiclyWritable": int,
        "unknown": int,
    },
    total=False,
)

BucketCountByEncryptionTypeTypeDef = TypedDict(
    "BucketCountByEncryptionTypeTypeDef",
    {
        "kmsManaged": int,
        "s3Managed": int,
        "unencrypted": int,
        "unknown": int,
    },
    total=False,
)

BucketCountBySharedAccessTypeTypeDef = TypedDict(
    "BucketCountBySharedAccessTypeTypeDef",
    {
        "external": int,
        "internal": int,
        "notShared": int,
        "unknown": int,
    },
    total=False,
)

BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef = TypedDict(
    "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef",
    {
        "allowsUnencryptedObjectUploads": int,
        "deniesUnencryptedObjectUploads": int,
        "unknown": int,
    },
    total=False,
)

BucketCriteriaAdditionalPropertiesTypeDef = TypedDict(
    "BucketCriteriaAdditionalPropertiesTypeDef",
    {
        "eq": List[str],
        "gt": int,
        "gte": int,
        "lt": int,
        "lte": int,
        "neq": List[str],
        "prefix": str,
    },
    total=False,
)

BucketLevelPermissionsTypeDef = TypedDict(
    "BucketLevelPermissionsTypeDef",
    {
        "accessControlList": "AccessControlListTypeDef",
        "blockPublicAccess": "BlockPublicAccessTypeDef",
        "bucketPolicy": "BucketPolicyTypeDef",
    },
    total=False,
)

BucketMetadataTypeDef = TypedDict(
    "BucketMetadataTypeDef",
    {
        "accountId": str,
        "allowsUnencryptedObjectUploads": AllowsUnencryptedObjectUploadsType,
        "bucketArn": str,
        "bucketCreatedAt": datetime,
        "bucketName": str,
        "classifiableObjectCount": int,
        "classifiableSizeInBytes": int,
        "jobDetails": "JobDetailsTypeDef",
        "lastUpdated": datetime,
        "objectCount": int,
        "objectCountByEncryptionType": "ObjectCountByEncryptionTypeTypeDef",
        "publicAccess": "BucketPublicAccessTypeDef",
        "region": str,
        "replicationDetails": "ReplicationDetailsTypeDef",
        "serverSideEncryption": "BucketServerSideEncryptionTypeDef",
        "sharedAccess": SharedAccessType,
        "sizeInBytes": int,
        "sizeInBytesCompressed": int,
        "tags": List["KeyValuePairTypeDef"],
        "unclassifiableObjectCount": "ObjectLevelStatisticsTypeDef",
        "unclassifiableObjectSizeInBytes": "ObjectLevelStatisticsTypeDef",
        "versioning": bool,
    },
    total=False,
)

BucketPermissionConfigurationTypeDef = TypedDict(
    "BucketPermissionConfigurationTypeDef",
    {
        "accountLevelPermissions": "AccountLevelPermissionsTypeDef",
        "bucketLevelPermissions": "BucketLevelPermissionsTypeDef",
    },
    total=False,
)

BucketPolicyTypeDef = TypedDict(
    "BucketPolicyTypeDef",
    {
        "allowsPublicReadAccess": bool,
        "allowsPublicWriteAccess": bool,
    },
    total=False,
)

BucketPublicAccessTypeDef = TypedDict(
    "BucketPublicAccessTypeDef",
    {
        "effectivePermission": EffectivePermissionType,
        "permissionConfiguration": "BucketPermissionConfigurationTypeDef",
    },
    total=False,
)

BucketServerSideEncryptionTypeDef = TypedDict(
    "BucketServerSideEncryptionTypeDef",
    {
        "kmsMasterKeyId": str,
        "type": TypeType,
    },
    total=False,
)

BucketSortCriteriaTypeDef = TypedDict(
    "BucketSortCriteriaTypeDef",
    {
        "attributeName": str,
        "orderBy": OrderByType,
    },
    total=False,
)

CellTypeDef = TypedDict(
    "CellTypeDef",
    {
        "cellReference": str,
        "column": int,
        "columnName": str,
        "row": int,
    },
    total=False,
)

ClassificationDetailsTypeDef = TypedDict(
    "ClassificationDetailsTypeDef",
    {
        "detailedResultsLocation": str,
        "jobArn": str,
        "jobId": str,
        "result": "ClassificationResultTypeDef",
    },
    total=False,
)

ClassificationExportConfigurationTypeDef = TypedDict(
    "ClassificationExportConfigurationTypeDef",
    {
        "s3Destination": "S3DestinationTypeDef",
    },
    total=False,
)

ClassificationResultStatusTypeDef = TypedDict(
    "ClassificationResultStatusTypeDef",
    {
        "code": str,
        "reason": str,
    },
    total=False,
)

ClassificationResultTypeDef = TypedDict(
    "ClassificationResultTypeDef",
    {
        "additionalOccurrences": bool,
        "customDataIdentifiers": "CustomDataIdentifiersTypeDef",
        "mimeType": str,
        "sensitiveData": List["SensitiveDataItemTypeDef"],
        "sizeClassified": int,
        "status": "ClassificationResultStatusTypeDef",
    },
    total=False,
)

_RequiredCreateClassificationJobRequestTypeDef = TypedDict(
    "_RequiredCreateClassificationJobRequestTypeDef",
    {
        "clientToken": str,
        "jobType": JobTypeType,
        "name": str,
        "s3JobDefinition": "S3JobDefinitionTypeDef",
    },
)
_OptionalCreateClassificationJobRequestTypeDef = TypedDict(
    "_OptionalCreateClassificationJobRequestTypeDef",
    {
        "customDataIdentifierIds": List[str],
        "description": str,
        "initialRun": bool,
        "samplingPercentage": int,
        "scheduleFrequency": "JobScheduleFrequencyTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateClassificationJobRequestTypeDef(
    _RequiredCreateClassificationJobRequestTypeDef, _OptionalCreateClassificationJobRequestTypeDef
):
    pass


CreateClassificationJobResponseResponseTypeDef = TypedDict(
    "CreateClassificationJobResponseResponseTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomDataIdentifierRequestTypeDef = TypedDict(
    "CreateCustomDataIdentifierRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "ignoreWords": List[str],
        "keywords": List[str],
        "maximumMatchDistance": int,
        "name": str,
        "regex": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateCustomDataIdentifierResponseResponseTypeDef = TypedDict(
    "CreateCustomDataIdentifierResponseResponseTypeDef",
    {
        "customDataIdentifierId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFindingsFilterRequestTypeDef = TypedDict(
    "_RequiredCreateFindingsFilterRequestTypeDef",
    {
        "action": FindingsFilterActionType,
        "findingCriteria": "FindingCriteriaTypeDef",
        "name": str,
    },
)
_OptionalCreateFindingsFilterRequestTypeDef = TypedDict(
    "_OptionalCreateFindingsFilterRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "position": int,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateFindingsFilterRequestTypeDef(
    _RequiredCreateFindingsFilterRequestTypeDef, _OptionalCreateFindingsFilterRequestTypeDef
):
    pass


CreateFindingsFilterResponseResponseTypeDef = TypedDict(
    "CreateFindingsFilterResponseResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInvitationsRequestTypeDef = TypedDict(
    "_RequiredCreateInvitationsRequestTypeDef",
    {
        "accountIds": List[str],
    },
)
_OptionalCreateInvitationsRequestTypeDef = TypedDict(
    "_OptionalCreateInvitationsRequestTypeDef",
    {
        "disableEmailNotification": bool,
        "message": str,
    },
    total=False,
)


class CreateInvitationsRequestTypeDef(
    _RequiredCreateInvitationsRequestTypeDef, _OptionalCreateInvitationsRequestTypeDef
):
    pass


CreateInvitationsResponseResponseTypeDef = TypedDict(
    "CreateInvitationsResponseResponseTypeDef",
    {
        "unprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMemberRequestTypeDef = TypedDict(
    "_RequiredCreateMemberRequestTypeDef",
    {
        "account": "AccountDetailTypeDef",
    },
)
_OptionalCreateMemberRequestTypeDef = TypedDict(
    "_OptionalCreateMemberRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateMemberRequestTypeDef(
    _RequiredCreateMemberRequestTypeDef, _OptionalCreateMemberRequestTypeDef
):
    pass


CreateMemberResponseResponseTypeDef = TypedDict(
    "CreateMemberResponseResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSampleFindingsRequestTypeDef = TypedDict(
    "CreateSampleFindingsRequestTypeDef",
    {
        "findingTypes": List[FindingTypeType],
    },
    total=False,
)

CriteriaBlockForJobTypeDef = TypedDict(
    "CriteriaBlockForJobTypeDef",
    {
        "and": List["CriteriaForJobTypeDef"],
    },
    total=False,
)

CriteriaForJobTypeDef = TypedDict(
    "CriteriaForJobTypeDef",
    {
        "simpleCriterion": "SimpleCriterionForJobTypeDef",
        "tagCriterion": "TagCriterionForJobTypeDef",
    },
    total=False,
)

CriterionAdditionalPropertiesTypeDef = TypedDict(
    "CriterionAdditionalPropertiesTypeDef",
    {
        "eq": List[str],
        "eqExactMatch": List[str],
        "gt": int,
        "gte": int,
        "lt": int,
        "lte": int,
        "neq": List[str],
    },
    total=False,
)

CustomDataIdentifierSummaryTypeDef = TypedDict(
    "CustomDataIdentifierSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "description": str,
        "id": str,
        "name": str,
    },
    total=False,
)

CustomDataIdentifiersTypeDef = TypedDict(
    "CustomDataIdentifiersTypeDef",
    {
        "detections": List["CustomDetectionTypeDef"],
        "totalCount": int,
    },
    total=False,
)

CustomDetectionTypeDef = TypedDict(
    "CustomDetectionTypeDef",
    {
        "arn": str,
        "count": int,
        "name": str,
        "occurrences": "OccurrencesTypeDef",
    },
    total=False,
)

DeclineInvitationsRequestTypeDef = TypedDict(
    "DeclineInvitationsRequestTypeDef",
    {
        "accountIds": List[str],
    },
)

DeclineInvitationsResponseResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseResponseTypeDef",
    {
        "unprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefaultDetectionTypeDef = TypedDict(
    "DefaultDetectionTypeDef",
    {
        "count": int,
        "occurrences": "OccurrencesTypeDef",
        "type": str,
    },
    total=False,
)

DeleteCustomDataIdentifierRequestTypeDef = TypedDict(
    "DeleteCustomDataIdentifierRequestTypeDef",
    {
        "id": str,
    },
)

DeleteFindingsFilterRequestTypeDef = TypedDict(
    "DeleteFindingsFilterRequestTypeDef",
    {
        "id": str,
    },
)

DeleteInvitationsRequestTypeDef = TypedDict(
    "DeleteInvitationsRequestTypeDef",
    {
        "accountIds": List[str],
    },
)

DeleteInvitationsResponseResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseResponseTypeDef",
    {
        "unprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMemberRequestTypeDef = TypedDict(
    "DeleteMemberRequestTypeDef",
    {
        "id": str,
    },
)

DescribeBucketsRequestTypeDef = TypedDict(
    "DescribeBucketsRequestTypeDef",
    {
        "criteria": Dict[str, "BucketCriteriaAdditionalPropertiesTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "sortCriteria": "BucketSortCriteriaTypeDef",
    },
    total=False,
)

DescribeBucketsResponseResponseTypeDef = TypedDict(
    "DescribeBucketsResponseResponseTypeDef",
    {
        "buckets": List["BucketMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClassificationJobRequestTypeDef = TypedDict(
    "DescribeClassificationJobRequestTypeDef",
    {
        "jobId": str,
    },
)

DescribeClassificationJobResponseResponseTypeDef = TypedDict(
    "DescribeClassificationJobResponseResponseTypeDef",
    {
        "clientToken": str,
        "createdAt": datetime,
        "customDataIdentifierIds": List[str],
        "description": str,
        "initialRun": bool,
        "jobArn": str,
        "jobId": str,
        "jobStatus": JobStatusType,
        "jobType": JobTypeType,
        "lastRunErrorStatus": "LastRunErrorStatusTypeDef",
        "lastRunTime": datetime,
        "name": str,
        "s3JobDefinition": "S3JobDefinitionTypeDef",
        "samplingPercentage": int,
        "scheduleFrequency": "JobScheduleFrequencyTypeDef",
        "statistics": "StatisticsTypeDef",
        "tags": Dict[str, str],
        "userPausedDetails": "UserPausedDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseResponseTypeDef",
    {
        "autoEnable": bool,
        "maxAccountLimitReached": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableOrganizationAdminAccountRequestTypeDef = TypedDict(
    "DisableOrganizationAdminAccountRequestTypeDef",
    {
        "adminAccountId": str,
    },
)

DisassociateMemberRequestTypeDef = TypedDict(
    "DisassociateMemberRequestTypeDef",
    {
        "id": str,
    },
)

DomainDetailsTypeDef = TypedDict(
    "DomainDetailsTypeDef",
    {
        "domainName": str,
    },
    total=False,
)

EnableMacieRequestTypeDef = TypedDict(
    "EnableMacieRequestTypeDef",
    {
        "clientToken": str,
        "findingPublishingFrequency": FindingPublishingFrequencyType,
        "status": MacieStatusType,
    },
    total=False,
)

_RequiredEnableOrganizationAdminAccountRequestTypeDef = TypedDict(
    "_RequiredEnableOrganizationAdminAccountRequestTypeDef",
    {
        "adminAccountId": str,
    },
)
_OptionalEnableOrganizationAdminAccountRequestTypeDef = TypedDict(
    "_OptionalEnableOrganizationAdminAccountRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class EnableOrganizationAdminAccountRequestTypeDef(
    _RequiredEnableOrganizationAdminAccountRequestTypeDef,
    _OptionalEnableOrganizationAdminAccountRequestTypeDef,
):
    pass


FederatedUserTypeDef = TypedDict(
    "FederatedUserTypeDef",
    {
        "accessKeyId": str,
        "accountId": str,
        "arn": str,
        "principalId": str,
        "sessionContext": "SessionContextTypeDef",
    },
    total=False,
)

FindingActionTypeDef = TypedDict(
    "FindingActionTypeDef",
    {
        "actionType": Literal["AWS_API_CALL"],
        "apiCallDetails": "ApiCallDetailsTypeDef",
    },
    total=False,
)

FindingActorTypeDef = TypedDict(
    "FindingActorTypeDef",
    {
        "domainDetails": "DomainDetailsTypeDef",
        "ipAddressDetails": "IpAddressDetailsTypeDef",
        "userIdentity": "UserIdentityTypeDef",
    },
    total=False,
)

FindingCriteriaTypeDef = TypedDict(
    "FindingCriteriaTypeDef",
    {
        "criterion": Dict[str, "CriterionAdditionalPropertiesTypeDef"],
    },
    total=False,
)

FindingStatisticsSortCriteriaTypeDef = TypedDict(
    "FindingStatisticsSortCriteriaTypeDef",
    {
        "attributeName": FindingStatisticsSortAttributeNameType,
        "orderBy": OrderByType,
    },
    total=False,
)

FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "accountId": str,
        "archived": bool,
        "category": FindingCategoryType,
        "classificationDetails": "ClassificationDetailsTypeDef",
        "count": int,
        "createdAt": datetime,
        "description": str,
        "id": str,
        "partition": str,
        "policyDetails": "PolicyDetailsTypeDef",
        "region": str,
        "resourcesAffected": "ResourcesAffectedTypeDef",
        "sample": bool,
        "schemaVersion": str,
        "severity": "SeverityTypeDef",
        "title": str,
        "type": FindingTypeType,
        "updatedAt": datetime,
    },
    total=False,
)

FindingsFilterListItemTypeDef = TypedDict(
    "FindingsFilterListItemTypeDef",
    {
        "action": FindingsFilterActionType,
        "arn": str,
        "id": str,
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

GetAdministratorAccountResponseResponseTypeDef = TypedDict(
    "GetAdministratorAccountResponseResponseTypeDef",
    {
        "administrator": "InvitationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketStatisticsRequestTypeDef = TypedDict(
    "GetBucketStatisticsRequestTypeDef",
    {
        "accountId": str,
    },
    total=False,
)

GetBucketStatisticsResponseResponseTypeDef = TypedDict(
    "GetBucketStatisticsResponseResponseTypeDef",
    {
        "bucketCount": int,
        "bucketCountByEffectivePermission": "BucketCountByEffectivePermissionTypeDef",
        "bucketCountByEncryptionType": "BucketCountByEncryptionTypeTypeDef",
        "bucketCountByObjectEncryptionRequirement": "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef",
        "bucketCountBySharedAccessType": "BucketCountBySharedAccessTypeTypeDef",
        "classifiableObjectCount": int,
        "classifiableSizeInBytes": int,
        "lastUpdated": datetime,
        "objectCount": int,
        "sizeInBytes": int,
        "sizeInBytesCompressed": int,
        "unclassifiableObjectCount": "ObjectLevelStatisticsTypeDef",
        "unclassifiableObjectSizeInBytes": "ObjectLevelStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetClassificationExportConfigurationResponseResponseTypeDef = TypedDict(
    "GetClassificationExportConfigurationResponseResponseTypeDef",
    {
        "configuration": "ClassificationExportConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCustomDataIdentifierRequestTypeDef = TypedDict(
    "GetCustomDataIdentifierRequestTypeDef",
    {
        "id": str,
    },
)

GetCustomDataIdentifierResponseResponseTypeDef = TypedDict(
    "GetCustomDataIdentifierResponseResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deleted": bool,
        "description": str,
        "id": str,
        "ignoreWords": List[str],
        "keywords": List[str],
        "maximumMatchDistance": int,
        "name": str,
        "regex": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFindingStatisticsRequestTypeDef = TypedDict(
    "_RequiredGetFindingStatisticsRequestTypeDef",
    {
        "groupBy": GroupByType,
    },
)
_OptionalGetFindingStatisticsRequestTypeDef = TypedDict(
    "_OptionalGetFindingStatisticsRequestTypeDef",
    {
        "findingCriteria": "FindingCriteriaTypeDef",
        "size": int,
        "sortCriteria": "FindingStatisticsSortCriteriaTypeDef",
    },
    total=False,
)


class GetFindingStatisticsRequestTypeDef(
    _RequiredGetFindingStatisticsRequestTypeDef, _OptionalGetFindingStatisticsRequestTypeDef
):
    pass


GetFindingStatisticsResponseResponseTypeDef = TypedDict(
    "GetFindingStatisticsResponseResponseTypeDef",
    {
        "countsByGroup": List["GroupCountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingsFilterRequestTypeDef = TypedDict(
    "GetFindingsFilterRequestTypeDef",
    {
        "id": str,
    },
)

GetFindingsFilterResponseResponseTypeDef = TypedDict(
    "GetFindingsFilterResponseResponseTypeDef",
    {
        "action": FindingsFilterActionType,
        "arn": str,
        "description": str,
        "findingCriteria": "FindingCriteriaTypeDef",
        "id": str,
        "name": str,
        "position": int,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingsPublicationConfigurationResponseResponseTypeDef = TypedDict(
    "GetFindingsPublicationConfigurationResponseResponseTypeDef",
    {
        "securityHubConfiguration": "SecurityHubConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFindingsRequestTypeDef = TypedDict(
    "_RequiredGetFindingsRequestTypeDef",
    {
        "findingIds": List[str],
    },
)
_OptionalGetFindingsRequestTypeDef = TypedDict(
    "_OptionalGetFindingsRequestTypeDef",
    {
        "sortCriteria": "SortCriteriaTypeDef",
    },
    total=False,
)


class GetFindingsRequestTypeDef(
    _RequiredGetFindingsRequestTypeDef, _OptionalGetFindingsRequestTypeDef
):
    pass


GetFindingsResponseResponseTypeDef = TypedDict(
    "GetFindingsResponseResponseTypeDef",
    {
        "findings": List["FindingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInvitationsCountResponseResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseResponseTypeDef",
    {
        "invitationsCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMacieSessionResponseResponseTypeDef = TypedDict(
    "GetMacieSessionResponseResponseTypeDef",
    {
        "createdAt": datetime,
        "findingPublishingFrequency": FindingPublishingFrequencyType,
        "serviceRole": str,
        "status": MacieStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMasterAccountResponseResponseTypeDef = TypedDict(
    "GetMasterAccountResponseResponseTypeDef",
    {
        "master": "InvitationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMemberRequestTypeDef = TypedDict(
    "GetMemberRequestTypeDef",
    {
        "id": str,
    },
)

GetMemberResponseResponseTypeDef = TypedDict(
    "GetMemberResponseResponseTypeDef",
    {
        "accountId": str,
        "administratorAccountId": str,
        "arn": str,
        "email": str,
        "invitedAt": datetime,
        "masterAccountId": str,
        "relationshipStatus": RelationshipStatusType,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUsageStatisticsRequestTypeDef = TypedDict(
    "GetUsageStatisticsRequestTypeDef",
    {
        "filterBy": List["UsageStatisticsFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "sortBy": "UsageStatisticsSortByTypeDef",
        "timeRange": TimeRangeType,
    },
    total=False,
)

GetUsageStatisticsResponseResponseTypeDef = TypedDict(
    "GetUsageStatisticsResponseResponseTypeDef",
    {
        "nextToken": str,
        "records": List["UsageRecordTypeDef"],
        "timeRange": TimeRangeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUsageTotalsRequestTypeDef = TypedDict(
    "GetUsageTotalsRequestTypeDef",
    {
        "timeRange": str,
    },
    total=False,
)

GetUsageTotalsResponseResponseTypeDef = TypedDict(
    "GetUsageTotalsResponseResponseTypeDef",
    {
        "timeRange": TimeRangeType,
        "usageTotals": List["UsageTotalTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupCountTypeDef = TypedDict(
    "GroupCountTypeDef",
    {
        "count": int,
        "groupKey": str,
    },
    total=False,
)

IamUserTypeDef = TypedDict(
    "IamUserTypeDef",
    {
        "accountId": str,
        "arn": str,
        "principalId": str,
        "userName": str,
    },
    total=False,
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "accountId": str,
        "invitationId": str,
        "invitedAt": datetime,
        "relationshipStatus": RelationshipStatusType,
    },
    total=False,
)

IpAddressDetailsTypeDef = TypedDict(
    "IpAddressDetailsTypeDef",
    {
        "ipAddressV4": str,
        "ipCity": "IpCityTypeDef",
        "ipCountry": "IpCountryTypeDef",
        "ipGeoLocation": "IpGeoLocationTypeDef",
        "ipOwner": "IpOwnerTypeDef",
    },
    total=False,
)

IpCityTypeDef = TypedDict(
    "IpCityTypeDef",
    {
        "name": str,
    },
    total=False,
)

IpCountryTypeDef = TypedDict(
    "IpCountryTypeDef",
    {
        "code": str,
        "name": str,
    },
    total=False,
)

IpGeoLocationTypeDef = TypedDict(
    "IpGeoLocationTypeDef",
    {
        "lat": float,
        "lon": float,
    },
    total=False,
)

IpOwnerTypeDef = TypedDict(
    "IpOwnerTypeDef",
    {
        "asn": str,
        "asnOrg": str,
        "isp": str,
        "org": str,
    },
    total=False,
)

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "isDefinedInJob": IsDefinedInJobType,
        "isMonitoredByJob": IsMonitoredByJobType,
        "lastJobId": str,
        "lastJobRunTime": datetime,
    },
    total=False,
)

JobScheduleFrequencyTypeDef = TypedDict(
    "JobScheduleFrequencyTypeDef",
    {
        "dailySchedule": Dict[str, Any],
        "monthlySchedule": "MonthlyScheduleTypeDef",
        "weeklySchedule": "WeeklyScheduleTypeDef",
    },
    total=False,
)

JobScopeTermTypeDef = TypedDict(
    "JobScopeTermTypeDef",
    {
        "simpleScopeTerm": "SimpleScopeTermTypeDef",
        "tagScopeTerm": "TagScopeTermTypeDef",
    },
    total=False,
)

JobScopingBlockTypeDef = TypedDict(
    "JobScopingBlockTypeDef",
    {
        "and": List["JobScopeTermTypeDef"],
    },
    total=False,
)

JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "bucketDefinitions": List["S3BucketDefinitionForJobTypeDef"],
        "createdAt": datetime,
        "jobId": str,
        "jobStatus": JobStatusType,
        "jobType": JobTypeType,
        "lastRunErrorStatus": "LastRunErrorStatusTypeDef",
        "name": str,
        "userPausedDetails": "UserPausedDetailsTypeDef",
        "bucketCriteria": "S3BucketCriteriaForJobTypeDef",
    },
    total=False,
)

KeyValuePairTypeDef = TypedDict(
    "KeyValuePairTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

LastRunErrorStatusTypeDef = TypedDict(
    "LastRunErrorStatusTypeDef",
    {
        "code": LastRunErrorStatusCodeType,
    },
    total=False,
)

ListClassificationJobsRequestTypeDef = TypedDict(
    "ListClassificationJobsRequestTypeDef",
    {
        "filterCriteria": "ListJobsFilterCriteriaTypeDef",
        "maxResults": int,
        "nextToken": str,
        "sortCriteria": "ListJobsSortCriteriaTypeDef",
    },
    total=False,
)

ListClassificationJobsResponseResponseTypeDef = TypedDict(
    "ListClassificationJobsResponseResponseTypeDef",
    {
        "items": List["JobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomDataIdentifiersRequestTypeDef = TypedDict(
    "ListCustomDataIdentifiersRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListCustomDataIdentifiersResponseResponseTypeDef = TypedDict(
    "ListCustomDataIdentifiersResponseResponseTypeDef",
    {
        "items": List["CustomDataIdentifierSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFindingsFiltersRequestTypeDef = TypedDict(
    "ListFindingsFiltersRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListFindingsFiltersResponseResponseTypeDef = TypedDict(
    "ListFindingsFiltersResponseResponseTypeDef",
    {
        "findingsFilterListItems": List["FindingsFilterListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFindingsRequestTypeDef = TypedDict(
    "ListFindingsRequestTypeDef",
    {
        "findingCriteria": "FindingCriteriaTypeDef",
        "maxResults": int,
        "nextToken": str,
        "sortCriteria": "SortCriteriaTypeDef",
    },
    total=False,
)

ListFindingsResponseResponseTypeDef = TypedDict(
    "ListFindingsResponseResponseTypeDef",
    {
        "findingIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInvitationsRequestTypeDef = TypedDict(
    "ListInvitationsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListInvitationsResponseResponseTypeDef = TypedDict(
    "ListInvitationsResponseResponseTypeDef",
    {
        "invitations": List["InvitationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsFilterCriteriaTypeDef = TypedDict(
    "ListJobsFilterCriteriaTypeDef",
    {
        "excludes": List["ListJobsFilterTermTypeDef"],
        "includes": List["ListJobsFilterTermTypeDef"],
    },
    total=False,
)

ListJobsFilterTermTypeDef = TypedDict(
    "ListJobsFilterTermTypeDef",
    {
        "comparator": JobComparatorType,
        "key": ListJobsFilterKeyType,
        "values": List[str],
    },
    total=False,
)

ListJobsSortCriteriaTypeDef = TypedDict(
    "ListJobsSortCriteriaTypeDef",
    {
        "attributeName": ListJobsSortAttributeNameType,
        "orderBy": OrderByType,
    },
    total=False,
)

ListMembersRequestTypeDef = TypedDict(
    "ListMembersRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "onlyAssociated": str,
    },
    total=False,
)

ListMembersResponseResponseTypeDef = TypedDict(
    "ListMembersResponseResponseTypeDef",
    {
        "members": List["MemberTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationAdminAccountsRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListOrganizationAdminAccountsResponseResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseResponseTypeDef",
    {
        "adminAccounts": List["AdminAccountTypeDef"],
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
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MatchingBucketTypeDef = TypedDict(
    "MatchingBucketTypeDef",
    {
        "accountId": str,
        "bucketName": str,
        "classifiableObjectCount": int,
        "classifiableSizeInBytes": int,
        "jobDetails": "JobDetailsTypeDef",
        "objectCount": int,
        "objectCountByEncryptionType": "ObjectCountByEncryptionTypeTypeDef",
        "sizeInBytes": int,
        "sizeInBytesCompressed": int,
        "unclassifiableObjectCount": "ObjectLevelStatisticsTypeDef",
        "unclassifiableObjectSizeInBytes": "ObjectLevelStatisticsTypeDef",
    },
    total=False,
)

MatchingResourceTypeDef = TypedDict(
    "MatchingResourceTypeDef",
    {
        "matchingBucket": "MatchingBucketTypeDef",
    },
    total=False,
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "accountId": str,
        "administratorAccountId": str,
        "arn": str,
        "email": str,
        "invitedAt": datetime,
        "masterAccountId": str,
        "relationshipStatus": RelationshipStatusType,
        "tags": Dict[str, str],
        "updatedAt": datetime,
    },
    total=False,
)

MonthlyScheduleTypeDef = TypedDict(
    "MonthlyScheduleTypeDef",
    {
        "dayOfMonth": int,
    },
    total=False,
)

ObjectCountByEncryptionTypeTypeDef = TypedDict(
    "ObjectCountByEncryptionTypeTypeDef",
    {
        "customerManaged": int,
        "kmsManaged": int,
        "s3Managed": int,
        "unencrypted": int,
        "unknown": int,
    },
    total=False,
)

ObjectLevelStatisticsTypeDef = TypedDict(
    "ObjectLevelStatisticsTypeDef",
    {
        "fileType": int,
        "storageClass": int,
        "total": int,
    },
    total=False,
)

OccurrencesTypeDef = TypedDict(
    "OccurrencesTypeDef",
    {
        "cells": List["CellTypeDef"],
        "lineRanges": List["RangeTypeDef"],
        "offsetRanges": List["RangeTypeDef"],
        "pages": List["PageTypeDef"],
        "records": List["RecordTypeDef"],
    },
    total=False,
)

PageTypeDef = TypedDict(
    "PageTypeDef",
    {
        "lineRange": "RangeTypeDef",
        "offsetRange": "RangeTypeDef",
        "pageNumber": int,
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

PolicyDetailsTypeDef = TypedDict(
    "PolicyDetailsTypeDef",
    {
        "action": "FindingActionTypeDef",
        "actor": "FindingActorTypeDef",
    },
    total=False,
)

PutClassificationExportConfigurationRequestTypeDef = TypedDict(
    "PutClassificationExportConfigurationRequestTypeDef",
    {
        "configuration": "ClassificationExportConfigurationTypeDef",
    },
)

PutClassificationExportConfigurationResponseResponseTypeDef = TypedDict(
    "PutClassificationExportConfigurationResponseResponseTypeDef",
    {
        "configuration": "ClassificationExportConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutFindingsPublicationConfigurationRequestTypeDef = TypedDict(
    "PutFindingsPublicationConfigurationRequestTypeDef",
    {
        "clientToken": str,
        "securityHubConfiguration": "SecurityHubConfigurationTypeDef",
    },
    total=False,
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "end": int,
        "start": int,
        "startColumn": int,
    },
    total=False,
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "jsonPath": str,
        "recordIndex": int,
    },
    total=False,
)

ReplicationDetailsTypeDef = TypedDict(
    "ReplicationDetailsTypeDef",
    {
        "replicated": bool,
        "replicatedExternally": bool,
        "replicationAccounts": List[str],
    },
    total=False,
)

ResourcesAffectedTypeDef = TypedDict(
    "ResourcesAffectedTypeDef",
    {
        "s3Bucket": "S3BucketTypeDef",
        "s3Object": "S3ObjectTypeDef",
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

S3BucketCriteriaForJobTypeDef = TypedDict(
    "S3BucketCriteriaForJobTypeDef",
    {
        "excludes": "CriteriaBlockForJobTypeDef",
        "includes": "CriteriaBlockForJobTypeDef",
    },
    total=False,
)

S3BucketDefinitionForJobTypeDef = TypedDict(
    "S3BucketDefinitionForJobTypeDef",
    {
        "accountId": str,
        "buckets": List[str],
    },
)

S3BucketOwnerTypeDef = TypedDict(
    "S3BucketOwnerTypeDef",
    {
        "displayName": str,
        "id": str,
    },
    total=False,
)

S3BucketTypeDef = TypedDict(
    "S3BucketTypeDef",
    {
        "allowsUnencryptedObjectUploads": AllowsUnencryptedObjectUploadsType,
        "arn": str,
        "createdAt": datetime,
        "defaultServerSideEncryption": "ServerSideEncryptionTypeDef",
        "name": str,
        "owner": "S3BucketOwnerTypeDef",
        "publicAccess": "BucketPublicAccessTypeDef",
        "tags": List["KeyValuePairTypeDef"],
    },
    total=False,
)

_RequiredS3DestinationTypeDef = TypedDict(
    "_RequiredS3DestinationTypeDef",
    {
        "bucketName": str,
        "kmsKeyArn": str,
    },
)
_OptionalS3DestinationTypeDef = TypedDict(
    "_OptionalS3DestinationTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)


class S3DestinationTypeDef(_RequiredS3DestinationTypeDef, _OptionalS3DestinationTypeDef):
    pass


S3JobDefinitionTypeDef = TypedDict(
    "S3JobDefinitionTypeDef",
    {
        "bucketDefinitions": List["S3BucketDefinitionForJobTypeDef"],
        "scoping": "ScopingTypeDef",
        "bucketCriteria": "S3BucketCriteriaForJobTypeDef",
    },
    total=False,
)

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "bucketArn": str,
        "eTag": str,
        "extension": str,
        "key": str,
        "lastModified": datetime,
        "path": str,
        "publicAccess": bool,
        "serverSideEncryption": "ServerSideEncryptionTypeDef",
        "size": int,
        "storageClass": StorageClassType,
        "tags": List["KeyValuePairTypeDef"],
        "versionId": str,
    },
    total=False,
)

ScopingTypeDef = TypedDict(
    "ScopingTypeDef",
    {
        "excludes": "JobScopingBlockTypeDef",
        "includes": "JobScopingBlockTypeDef",
    },
    total=False,
)

SearchResourcesBucketCriteriaTypeDef = TypedDict(
    "SearchResourcesBucketCriteriaTypeDef",
    {
        "excludes": "SearchResourcesCriteriaBlockTypeDef",
        "includes": "SearchResourcesCriteriaBlockTypeDef",
    },
    total=False,
)

SearchResourcesCriteriaBlockTypeDef = TypedDict(
    "SearchResourcesCriteriaBlockTypeDef",
    {
        "and": List["SearchResourcesCriteriaTypeDef"],
    },
    total=False,
)

SearchResourcesCriteriaTypeDef = TypedDict(
    "SearchResourcesCriteriaTypeDef",
    {
        "simpleCriterion": "SearchResourcesSimpleCriterionTypeDef",
        "tagCriterion": "SearchResourcesTagCriterionTypeDef",
    },
    total=False,
)

SearchResourcesRequestTypeDef = TypedDict(
    "SearchResourcesRequestTypeDef",
    {
        "bucketCriteria": "SearchResourcesBucketCriteriaTypeDef",
        "maxResults": int,
        "nextToken": str,
        "sortCriteria": "SearchResourcesSortCriteriaTypeDef",
    },
    total=False,
)

SearchResourcesResponseResponseTypeDef = TypedDict(
    "SearchResourcesResponseResponseTypeDef",
    {
        "matchingResources": List["MatchingResourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchResourcesSimpleCriterionTypeDef = TypedDict(
    "SearchResourcesSimpleCriterionTypeDef",
    {
        "comparator": SearchResourcesComparatorType,
        "key": SearchResourcesSimpleCriterionKeyType,
        "values": List[str],
    },
    total=False,
)

SearchResourcesSortCriteriaTypeDef = TypedDict(
    "SearchResourcesSortCriteriaTypeDef",
    {
        "attributeName": SearchResourcesSortAttributeNameType,
        "orderBy": OrderByType,
    },
    total=False,
)

SearchResourcesTagCriterionPairTypeDef = TypedDict(
    "SearchResourcesTagCriterionPairTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

SearchResourcesTagCriterionTypeDef = TypedDict(
    "SearchResourcesTagCriterionTypeDef",
    {
        "comparator": SearchResourcesComparatorType,
        "tagValues": List["SearchResourcesTagCriterionPairTypeDef"],
    },
    total=False,
)

SecurityHubConfigurationTypeDef = TypedDict(
    "SecurityHubConfigurationTypeDef",
    {
        "publishClassificationFindings": bool,
        "publishPolicyFindings": bool,
    },
)

SensitiveDataItemTypeDef = TypedDict(
    "SensitiveDataItemTypeDef",
    {
        "category": SensitiveDataItemCategoryType,
        "detections": List["DefaultDetectionTypeDef"],
        "totalCount": int,
    },
    total=False,
)

ServerSideEncryptionTypeDef = TypedDict(
    "ServerSideEncryptionTypeDef",
    {
        "encryptionType": EncryptionTypeType,
        "kmsMasterKeyId": str,
    },
    total=False,
)

ServiceLimitTypeDef = TypedDict(
    "ServiceLimitTypeDef",
    {
        "isServiceLimited": bool,
        "unit": Literal["TERABYTES"],
        "value": int,
    },
    total=False,
)

SessionContextAttributesTypeDef = TypedDict(
    "SessionContextAttributesTypeDef",
    {
        "creationDate": datetime,
        "mfaAuthenticated": bool,
    },
    total=False,
)

SessionContextTypeDef = TypedDict(
    "SessionContextTypeDef",
    {
        "attributes": "SessionContextAttributesTypeDef",
        "sessionIssuer": "SessionIssuerTypeDef",
    },
    total=False,
)

SessionIssuerTypeDef = TypedDict(
    "SessionIssuerTypeDef",
    {
        "accountId": str,
        "arn": str,
        "principalId": str,
        "type": str,
        "userName": str,
    },
    total=False,
)

SeverityTypeDef = TypedDict(
    "SeverityTypeDef",
    {
        "description": SeverityDescriptionType,
        "score": int,
    },
    total=False,
)

SimpleCriterionForJobTypeDef = TypedDict(
    "SimpleCriterionForJobTypeDef",
    {
        "comparator": JobComparatorType,
        "key": SimpleCriterionKeyForJobType,
        "values": List[str],
    },
    total=False,
)

SimpleScopeTermTypeDef = TypedDict(
    "SimpleScopeTermTypeDef",
    {
        "comparator": JobComparatorType,
        "key": ScopeFilterKeyType,
        "values": List[str],
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

StatisticsTypeDef = TypedDict(
    "StatisticsTypeDef",
    {
        "approximateNumberOfObjectsToProcess": float,
        "numberOfRuns": float,
    },
    total=False,
)

TagCriterionForJobTypeDef = TypedDict(
    "TagCriterionForJobTypeDef",
    {
        "comparator": JobComparatorType,
        "tagValues": List["TagCriterionPairForJobTypeDef"],
    },
    total=False,
)

TagCriterionPairForJobTypeDef = TypedDict(
    "TagCriterionPairForJobTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TagScopeTermTypeDef = TypedDict(
    "TagScopeTermTypeDef",
    {
        "comparator": JobComparatorType,
        "key": str,
        "tagValues": List["TagValuePairTypeDef"],
        "target": Literal["S3_OBJECT"],
    },
    total=False,
)

TagValuePairTypeDef = TypedDict(
    "TagValuePairTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

_RequiredTestCustomDataIdentifierRequestTypeDef = TypedDict(
    "_RequiredTestCustomDataIdentifierRequestTypeDef",
    {
        "regex": str,
        "sampleText": str,
    },
)
_OptionalTestCustomDataIdentifierRequestTypeDef = TypedDict(
    "_OptionalTestCustomDataIdentifierRequestTypeDef",
    {
        "ignoreWords": List[str],
        "keywords": List[str],
        "maximumMatchDistance": int,
    },
    total=False,
)


class TestCustomDataIdentifierRequestTypeDef(
    _RequiredTestCustomDataIdentifierRequestTypeDef, _OptionalTestCustomDataIdentifierRequestTypeDef
):
    pass


TestCustomDataIdentifierResponseResponseTypeDef = TypedDict(
    "TestCustomDataIdentifierResponseResponseTypeDef",
    {
        "matchCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {
        "accountId": str,
        "errorCode": ErrorCodeType,
        "errorMessage": str,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateClassificationJobRequestTypeDef = TypedDict(
    "UpdateClassificationJobRequestTypeDef",
    {
        "jobId": str,
        "jobStatus": JobStatusType,
    },
)

_RequiredUpdateFindingsFilterRequestTypeDef = TypedDict(
    "_RequiredUpdateFindingsFilterRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateFindingsFilterRequestTypeDef = TypedDict(
    "_OptionalUpdateFindingsFilterRequestTypeDef",
    {
        "action": FindingsFilterActionType,
        "description": str,
        "findingCriteria": "FindingCriteriaTypeDef",
        "name": str,
        "position": int,
        "clientToken": str,
    },
    total=False,
)


class UpdateFindingsFilterRequestTypeDef(
    _RequiredUpdateFindingsFilterRequestTypeDef, _OptionalUpdateFindingsFilterRequestTypeDef
):
    pass


UpdateFindingsFilterResponseResponseTypeDef = TypedDict(
    "UpdateFindingsFilterResponseResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMacieSessionRequestTypeDef = TypedDict(
    "UpdateMacieSessionRequestTypeDef",
    {
        "findingPublishingFrequency": FindingPublishingFrequencyType,
        "status": MacieStatusType,
    },
    total=False,
)

UpdateMemberSessionRequestTypeDef = TypedDict(
    "UpdateMemberSessionRequestTypeDef",
    {
        "id": str,
        "status": MacieStatusType,
    },
)

UpdateOrganizationConfigurationRequestTypeDef = TypedDict(
    "UpdateOrganizationConfigurationRequestTypeDef",
    {
        "autoEnable": bool,
    },
)

UsageByAccountTypeDef = TypedDict(
    "UsageByAccountTypeDef",
    {
        "currency": Literal["USD"],
        "estimatedCost": str,
        "serviceLimit": "ServiceLimitTypeDef",
        "type": UsageTypeType,
    },
    total=False,
)

UsageRecordTypeDef = TypedDict(
    "UsageRecordTypeDef",
    {
        "accountId": str,
        "freeTrialStartDate": datetime,
        "usage": List["UsageByAccountTypeDef"],
    },
    total=False,
)

UsageStatisticsFilterTypeDef = TypedDict(
    "UsageStatisticsFilterTypeDef",
    {
        "comparator": UsageStatisticsFilterComparatorType,
        "key": UsageStatisticsFilterKeyType,
        "values": List[str],
    },
    total=False,
)

UsageStatisticsSortByTypeDef = TypedDict(
    "UsageStatisticsSortByTypeDef",
    {
        "key": UsageStatisticsSortKeyType,
        "orderBy": OrderByType,
    },
    total=False,
)

UsageTotalTypeDef = TypedDict(
    "UsageTotalTypeDef",
    {
        "currency": Literal["USD"],
        "estimatedCost": str,
        "type": UsageTypeType,
    },
    total=False,
)

UserIdentityRootTypeDef = TypedDict(
    "UserIdentityRootTypeDef",
    {
        "accountId": str,
        "arn": str,
        "principalId": str,
    },
    total=False,
)

UserIdentityTypeDef = TypedDict(
    "UserIdentityTypeDef",
    {
        "assumedRole": "AssumedRoleTypeDef",
        "awsAccount": "AwsAccountTypeDef",
        "awsService": "AwsServiceTypeDef",
        "federatedUser": "FederatedUserTypeDef",
        "iamUser": "IamUserTypeDef",
        "root": "UserIdentityRootTypeDef",
        "type": UserIdentityTypeType,
    },
    total=False,
)

UserPausedDetailsTypeDef = TypedDict(
    "UserPausedDetailsTypeDef",
    {
        "jobExpiresAt": datetime,
        "jobImminentExpirationHealthEventArn": str,
        "jobPausedAt": datetime,
    },
    total=False,
)

WeeklyScheduleTypeDef = TypedDict(
    "WeeklyScheduleTypeDef",
    {
        "dayOfWeek": DayOfWeekType,
    },
    total=False,
)
